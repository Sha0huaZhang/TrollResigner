#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
from pathlib import Path

from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                             QWidget, QPushButton, QTextEdit, QLabel, QLineEdit,
                             QMessageBox, QProgressBar)
from PyQt5.QtCore import QThread, pyqtSignal


class SignWorker(QThread):
    log_signal = pyqtSignal(str)
    finished_signal = pyqtSignal(bool, str)

    def __init__(self, team_id):
        super().__init__()
        self.team_id = team_id

    def run(self):
        self.log_signal.emit("[信息] 开始调用 MachOX 签名...")
        machox_path = Path(__file__).parent / "MachOX"
        if not machox_path.exists():
            self.log_signal.emit(f"[错误] 找不到 MachOX: {machox_path}")
            self.finished_signal.emit(False, "MachOX not found")
            return

        desktop = Path.home() / "Desktop"
        output_path = desktop / "helper_resign"
        cmd = [str(machox_path), "-i", "dummy", "-o", str(output_path), "-t", self.team_id]

        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in iter(proc.stdout.readline, ''):
                self.log_signal.emit(f"[MachOX] {line.strip()}")
            proc.wait()
            if proc.returncode == 0 and output_path.exists():
                self.log_signal.emit(f"[成功] 签名成功！文件: {output_path}")
                self.finished_signal.emit(True, str(output_path))
            else:
                self.log_signal.emit(f"[错误] 签名失败，返回码: {proc.returncode}")
                self.finished_signal.emit(False, "Sign failed")
        except Exception as e:
            self.log_signal.emit(f"[错误] 签名异常: {e}")
            self.finished_signal.emit(False, str(e))


class InjectWorker(QThread):
    log_signal = pyqtSignal(str)
    finished_signal = pyqtSignal(bool, str)

    def __init__(self, target_app):
        super().__init__()
        self.target_app = target_app

    def run(self):
        self.log_signal.emit("[信息] 开始调用 restorehelper.py 注入...")
        helper_path = Path(__file__).parent / "restorehelper.py"
        if not helper_path.exists():
            self.log_signal.emit(f"[错误] 找不到 restorehelper.py: {helper_path}")
            self.finished_signal.emit(False, "restorehelper.py not found")
            return

        cmd = ["python3", str(helper_path), self.target_app]
        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in iter(proc.stdout.readline, ''):
                self.log_signal.emit(f"[restorehelper] {line.strip()}")
            proc.wait()
            if proc.returncode == 0:
                self.log_signal.emit("[成功] 注入成功！设备将重启。")
                self.finished_signal.emit(True, "Inject success")
            else:
                self.log_signal.emit(f"[错误] 注入失败，返回码: {proc.returncode}")
                self.finished_signal.emit(False, "Inject failed")
        except Exception as e:
            self.log_signal.emit(f"[错误] 注入异常: {e}")
            self.finished_signal.emit(False, str(e))


class TrollResignerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TrollResigner")
        self.setMinimumSize(600, 500)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        # 步骤 1: Team ID
        step1 = QHBoxLayout()
        step1.addWidget(QLabel("1. 开发者证书 Team ID:"))
        self.team_input = QLineEdit()
        self.team_input.setPlaceholderText("输入你的 Team ID (如 A11A111AAA)")
        step1.addWidget(self.team_input)
        layout.addLayout(step1)

        # 步骤 2: 签名按钮
        self.sign_btn = QPushButton("2. 开始签名 (MachOX)")
        self.sign_btn.clicked.connect(self.start_sign)
        layout.addWidget(self.sign_btn)

        # 步骤 3: 系统应用名称（手动输入）
        step3 = QHBoxLayout()
        step3.addWidget(QLabel("3. 替换的系统应用名称:"))
        self.app_input = QLineEdit()
        self.app_input.setPlaceholderText("如: tips (不区分大小写)")
        step3.addWidget(self.app_input)
        self.inject_btn = QPushButton("开始注入 (restorehelper.py)")
        self.inject_btn.clicked.connect(self.start_inject)
        self.inject_btn.setEnabled(False)
        step3.addWidget(self.inject_btn)
        layout.addLayout(step3)

        # 日志区域
        layout.addWidget(QLabel("运行日志:"))
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        layout.addWidget(self.log)

        self.progress = QProgressBar()
        self.progress.setVisible(False)
        layout.addWidget(self.progress)

        self.sign_worker = None
        self.inject_worker = None

    def log_msg(self, msg):
        self.log.append(msg)

    def start_sign(self):
        team_id = self.team_input.text().strip()
        if not team_id:
            QMessageBox.warning(self, "警告", "请输入 Team ID")
            return

        self.sign_btn.setEnabled(False)
        self.progress.setVisible(True)
        self.log_msg("[信息] 准备签名...")
        self.sign_worker = SignWorker(team_id)
        self.sign_worker.log_signal.connect(self.log_msg)
        self.sign_worker.finished_signal.connect(self.on_sign_finished)
        self.sign_worker.start()

    def on_sign_finished(self, success, msg):
        self.sign_btn.setEnabled(True)
        self.progress.setVisible(False)
        if success:
            self.log_msg("[信息] 签名完成，可进行注入")
            self.inject_btn.setEnabled(True)
            QMessageBox.information(self, "成功", f"签名成功！\n{msg}")
        else:
            self.log_msg(f"[错误] 签名失败: {msg}")
            QMessageBox.critical(self, "失败", f"签名失败\n{msg}")

    def start_inject(self):
        app_name = self.app_input.text().strip()
        if not app_name:
            QMessageBox.warning(self, "警告", "请输入系统应用名称")
            return

        self.inject_btn.setEnabled(False)
        self.progress.setVisible(True)
        self.log_msg(f"[信息] 准备注入 {app_name}.app ...")
        self.inject_worker = InjectWorker(app_name)
        self.inject_worker.log_signal.connect(self.log_msg)
        self.inject_worker.finished_signal.connect(self.on_inject_finished)
        self.inject_worker.start()

    def on_inject_finished(self, success, msg):
        self.inject_btn.setEnabled(True)
        self.progress.setVisible(False)
        if success:
            self.log_msg("[信息] 注入流程结束")
            QMessageBox.information(self, "完成", "注入完成，设备将重启")
        else:
            self.log_msg(f"[错误] 注入失败: {msg}")
            QMessageBox.critical(self, "失败", f"注入失败\n{msg}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TrollResignerGUI()
    win.show()
    sys.exit(app.exec_())

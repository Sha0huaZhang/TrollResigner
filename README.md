# TrollResigner

**SHA256**

**restorehelper.py**

SHA256:f40e19fd46d979dc18bcbcc9d7f9f85b75dbdab5a5acef80e581a0bde629cc52
# Details / 详情
TrollResigner is a tool to install TrollStore on iOS 16.7 (20H19) - iOS 16.7.x & iOS 17.0.1.

TrollResigner 是 TrollStore 在 iOS 16.7 (20H19) - iOS 16.7.x & iOS 17.0.1的安装工具。
# Supported Versions / 支持版本
iOS 16.7 (20H19) - iOS 16.7.x & iOS 17.0.1

| From | To | arm64 (A8) | arm64 (A9-A11) | arm64e (A12-A17/M1-M2) |
|-|-|-|-|-|
| -- | 14.0beta1| Unsupported | Unsupported | Unsupported |
| 14.0beta2 | 14.8.1 | TrollInstallerX | TrollInstallerX | TrollHelperOTA |
| 15.0 | 15.5beta4 | TrollHelperOTA | TrollHelperOTA | TrollHelperOTA|
| 15.5 | 15.5 | TrollInstallerMDC | TrollInstallerX | TrollHelperOTA |
| 15.6beta1 | 15.6beta3 | TrollHelperOTA | TrollHelperOTA | TrollHelperOTA |
| 15.6beta4 | 15.6.1 | TrollInstallerMDC | TrollInstallerX | TrollHelperOTA |
| 15.7| 15.7.1 | TrollInstallerMDC | TrollInstallerX | TrollInstallerX |
| 15.7.2| 15.8.6 | TrollMisaka | TrollInstallerX | TrollInstallerX |
| 15.8.7| 15.8.8| TrollRestore | TrollRestore | Not Applicable|
| 16.0beta1 | 16.0beta5 | Not Applicable | TrollInstallerX | TrollHelperOTA |
| 16.0beta6 | 16.6.1 | Not Applicable | TrollInstallerX | TrollInstallerX |
| 16.7 RC | 16.7 RC| Not Applicable | TrollRestore | TrollRestore |
| 16.7 | 16.7.16| Not Applicable | TrollResigner | TrollResigner|
| 17.0beta1 | 17.0beta4 | Not Applicable| TrollInstallerX | TrollRestore |
| 17.0beta5 | 17.0 | Not Applicable | TrollRestore | TrollRestore |
| 17.0.1 | 17.0.1 | Not Applicable| TrollResigner| TrollResigner|
| 17.0.2 | -- | Not Applicable | Unsupported | Unsupported |


*Some data from https://ios.cfw.guide

# Usage / 使用方法
# I . TrollResigner_GUI (For User)             


**Install Python3** (If not installed):  
**安装Python 3** （如果尚未安装）：

Install Python 3 from https://python.org    
    从 https://python.org 下载Python 3

Check:In Terminal,run    
    检查版本：在终端运行
    
```bash
python3 --version
```

Make sure the version was Python 3.9 or higher.    
    确保你的版本为Python 3.9及以上

**Install pymobiledevice3** (If not installed):    
**安装pymobiledevice3** （如果尚未安装）：

In Terminal,run    
    在终端运行

```bash
pip3 install pymobiledevice3
```

Check:In Terminal, run    
    检查版本：在终端运行

```bash
pymobiledevice3 version
```

Make sure the version was 4.14.0 or higher.    
    确保你的版本为4.14.0及以上

**Install PyQt5** (If not installed):    
**安装 PyQt5**（如果尚未安装）：    

In Terminal, run    
    在终端运行

        pip3 install PyQt5
  
**Build MachOX / 构建 MachOX**

In Terminal, run    
    在终端运行    

        git clone https://github.com/ShaOhuaZhang/MachOX.git
        cd MachOX
        make

**Get your Team ID / 获取你的 Team ID**    
      
In Terminal, run    
    在终端运行    
        
        security find-identity -v -p basic | grep "Apple Development"


Copy the Team ID from the output (e.g., `A11A111AAA`)    
    从输出中获取你的 Team ID （如`A11A111AAA`）

**Install TrollStore / 安装TrollStore**

In Terminal, run    
    在终端运行

        python3 trollresigner_gui_zh.py

或    
or

        python3 trollresigner_gui_en.py


Follow the on-screen instructions to select a system app to replace (e.g., `tips`)       
按提示输入一个系统应用的名字（如：`tips`）    


After the device restarts, enter the system app you entered    
等待设备重启后，进入你输入的系统应用

Click `Install TrollStore` and wait    
点击 `Install TrollStore` 并等待    

# II . TrollResigner_CLI (For Developer)       

**Install Python3** (If not installed):  
**安装Python 3** （如果尚未安装）：

Install Python 3 from https://python.org    
    从 https://python.org 下载Python 3

Check:In Terminal,run    
    检查版本：在终端运行
    
```bash
python3 --version
```

Make sure the version was Python 3.9 or higher.    
    确保你的版本为Python 3.9及以上

**Install pymobiledevice3** (If not installed):    
**安装pymobiledevice3** （如果尚未安装）：

In Terminal,run    
    在终端运行

```bash
pip3 install pymobiledevice3
```

Check:In Terminal, run    
    检查版本：在终端运行

```bash
pymobiledevice3 version
```

Make sure the version was 4.14.0 or higher.    
    确保你的版本为4.14.0及以上
     
**Build MachOX / 构建 MachOX**

In Terminal, run    
    在终端运行    

        git clone https://github.com/ShaOhuaZhang/MachOX.git
        cd MachOX
        make

**Get your Team ID / 获取你的 Team ID**    
      
In Terminal, run    
    在终端运行    
        
        security find-identity -v -p basic | grep "Apple Development"


Copy the Team ID from the output (e.g., `A11A111AAA`)    
    从输出中获取你的 Team ID （如`A11A111AAA`）

**Sign your file / 签名 Helper**    

In Terminal, run    
    在终端运行    
        
        ./MachOX -i dummy -o ~/Desktop/helper_resign -t YOUR_TEAM_ID
        
**Verify the output / 验证输出**    

The signed helper will be saved to your Desktop as `helper_resign`    
    签名后的 Helper 文件将保存在桌面，文件名为 `helper_resign`

**Rename the output / 重命名输出文件**    

In Terminal, run    
    在终端运行

    mv ~/Desktop/helper_resign ~/Desktop/TrollStorePersistanceHelper_Resign

**Run RestoreHelper / 运行 RestoreHelper**    

In Terminal, run    
    在终端运行
       
        python3 restorehelper.py    

Follow the on-screen instructions to select a system app to replace (e.g., `tips`)       
按提示输入一个系统应用的名字（如：`tips`）    


After the device restarts, enter the system app you entered    
等待设备重启后，进入你输入的系统应用

Click `Install TrollStore` and wait    
点击 `Install TrollStore` 并等待

# Credits/致谢:
(in alphabetical/按首字母排列)

JJTech (@JJTech0130) [https://GitHub.com/JJTech0130](https://GitHub.com/JJTech0130) : TrollRestore & SparseRestore & CVE-2024-44252    
    Lars Fröder (@opa334) [https://GitHub.com/opa334](https://GitHub.com/opa334) : TrollStore & ChOma

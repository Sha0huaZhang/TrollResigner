# Disclosure History / 披露历史

## English

This vulnerability was submitted to the Apple Security Bounty program on May 5, 2026.

**Report ID:** OE110620235331

### Timeline

| Date | Event |
|------|-------|
| 2026/5/5 21:40 | Initial submission |
| 2026/5/6 18:27 | Supplementary evidence: persistent attack after reboot |
| 2026/5/7 09:08 | Apple: /etc/passwd is world-readable, expected behavior |
| 2026/5/7 19:22 | Response regarding toolchain limitations |
| 2026/5/9 18:31 | Submitted cross-app data access evidence |
| 2026/5/12 01:55 | Apple: simulator not accepted |
| 2026/5/23 23:29 | Submitted complete toolchain (MachOX + TrollResigner) |
| 2026/5/26 22:31 | Detailed technical explanation |
| 2026/5/28 12:56 | Apple: report closed, no further updates |

### Communication Log

**May 5, 2026 21:40** - Initial report submitted.

**May 6, 2026 18:27** - Supplementary evidence provided:

> After the initial forced triggering via Airplane Mode + Bluetooth + date change, the device was left idle with no further interaction. Over the following days, multiple additional crash logs (stacks_*.ips) were automatically generated, containing the same exception codes (0x20 / 0xbaaaaaad) and pointing to the same backupd (UID 0) process. This demonstrates that the UAF is not merely a transient race condition.

**May 7, 2026 09:08** - Apple response (Nick, Product Security):

> Thank you for your report. The file /etc/passwd is world-readable by design on iOS, so any app can read it without special entitlements, this is expected behavior. If you're able to demonstrate access to a data-vaulted file using this technique, please reach back out with that evidence.

**May 7, 2026 19:22** - Response regarding toolchain limitations:

> When I install and run my app through Xcode (⌘R), Xcode overwrites my manually injected entitlements.plist with its own signature. When I install my app through TrollStore, TrollStore also overwrites my original signature. At this point, I cannot find a development or debugging environment that preserves my original manual signature and the injected entitlements.plist.

**May 9, 2026 18:31** - Submitted cross-app sandbox bypass evidence.

**May 12, 2026 01:55** - Apple response (Nick, Product Security):

> However, the screenshot shows this running in the iOS Simulator, which does not enforce the same security boundaries as a physical device. We would need to see this demonstrated on a real device to consider re-opening the report.

**May 23, 2026 23:29** - Submitted complete toolchain (MachOX + TrollResigner) with full source code and binaries.

**May 26, 2026 22:31** - Detailed technical explanation of the CoreTrust bypass attack chain.

**May 28, 2026 12:56** - Apple final response (Nick, Product Security):

> the testing needs to be done on Apple hardware and not in a simulator as previously mentioned. We are closing this report and will not be providing any more updates.

### Conclusion

After providing:
- Initial vulnerability report
- Supplementary crash logs demonstrating persistence
- Cross-app sandbox bypass evidence
- Complete toolchain (MachOX + TrollResigner) with source code

Apple closed the report without acknowledging a security issue, stating that testing must be performed on physical Apple hardware (without providing any means to do so without toolchain interference).

Given that Apple has not fixed this issue within a reasonable timeframe, this tool is released to protect users and promote community research.

*Note: Personal identifying information of Apple engineers has been redacted. All communications are presented factually without subjective commentary.*

---

## 中文

本漏洞已于 2026 年 5 月 5 日通过 Apple 安全赏金计划提交。

**报告编号：** OE110620235331

### 时间线

| 日期 | 事件 |
|------|------|
| 2026/5/5 21:40 | 首次提交报告 |
| 2026/5/6 18:27 | 补充证据：重启后攻击仍持续 |
| 2026/5/7 09:08 | Apple 回复：/etc/passwd 为世界可读，属于预期行为 |
| 2026/5/7 19:22 | 回复关于工具链限制的说明 |
| 2026/5/9 18:31 | 提交跨 App 数据访问证据 |
| 2026/5/12 01:55 | Apple 回复：模拟器不被接受 |
| 2026/5/23 23:29 | 提交完整工具链（MachOX + TrollResigner） |
| 2026/5/26 22:31 | 详细技术说明 |
| 2026/5/28 12:56 | Apple 最终回复：关闭报告，不再更新 |

### 沟通记录

**2026 年 5 月 5 日 21:40** - 首次提交报告。

**2026 年 5 月 6 日 18:27** - 补充证据：

> 通过飞行模式 + 蓝牙 + 日期变更强制触发后，设备被闲置无任何进一步操作。在随后的几天里，系统自动生成了多个额外的崩溃日志（stacks_*.ips），包含相同的异常代码（0x20 / 0xbaaaaaad），并指向同一个 backupd（UID 0）进程。这证明该 UAF 不仅仅是一个难以触发的竞态条件。

**2026 年 5 月 7 日 09:08** - Apple 回复（Nick，Product Security）：

> 感谢您的报告。/etc/passwd 文件在 iOS 设计中是世界可读的，任何 App 无需特殊权限即可读取，这属于预期行为。如果您能证明此技术可以访问数据保管箱（data-vaulted）文件，请提供相关证据。

**2026 年 5 月 7 日 19:22** - 关于工具链限制的回复：

> 当我通过 Xcode（⌘R）安装运行我的 App 时，Xcode 会用自己的签名覆盖我手动注入的 entitlements.plist。当我通过 TrollStore 安装我的 App 时，TrollStore 同样会覆盖我的原始签名。目前，我找不到任何能够保留原始手动签名和注入的 entitlements.plist 的开发或调试环境。

**2026 年 5 月 9 日 18:31** - 提交跨 App 沙盒逃逸证据。

**2026 年 5 月 12 日 01:55** - Apple 回复（Nick，Product Security）：

> 然而，截图显示此运行是在 iOS 模拟器中进行的，模拟器并不强制执行与物理设备相同的安全边界。我们需要在真实设备上看到此演示，才能考虑重新打开报告。

**2026 年 5 月 23 日 23:29** - 提交完整工具链（MachOX + TrollResigner），包含完整源代码和二进制文件。

**2026 年 5 月 26 日 22:31** - CoreTrust 绕过攻击链的详细技术说明。

**2026 年 5 月 28 日 12:56** - Apple 最终回复（Nick，Product Security）：

> 如前所述，测试需要在 Apple 硬件上进行，而不是在模拟器中。我们将关闭此报告，并不会提供进一步的更新。

### 结论

在提供了以下内容后：
- 初始漏洞报告
- 证明持久性的补充崩溃日志
- 跨 App 沙盒逃逸证据
- 包含源代码的完整工具链（MachOX + TrollResigner）

Apple 关闭了报告，未确认安全问题，理由是必须在物理 Apple 硬件上进行测试（且未提供任何能在无工具链干扰下进行测试的方法）。

鉴于 Apple 未在合理时间内修复此问题，为保护用户安全并促进社区研究，决定公开本工具。

*注：Apple 工程师的个人身份信息已做脱敏处理。所有沟通内容均客观陈述，不包含主观评论。*

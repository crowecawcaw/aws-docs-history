

# Release notes
<a name="release-notes"></a>

## Release notes for v3.0.4
<a name="release-notes-3-0-4"></a>

### Features
<a name="release-notes-features"></a>

Compared with version 2.0.3, version 3.0.x adds optional [rule-based screen recording redaction](rule-based-redaction-screen-recording.md). Configured in contact flows, it creates a separate redacted recording using URL or window title rules in denylist or allowlist mode, with no agent action required.

### New components
<a name="release-notes-new-components"></a>
+ Browser helper (`Amazon.Connect.Client.Messaging.NativeHost.exe`, a new executable) – Relays browser context from the extension to the Connect Customer Client Application.
+ Window-monitoring library (`Amazon.Connect.Client.WindowMonitor.dll`, a new library) – Tracks application-window changes and positions.

### Fixes in 3.0.4
<a name="release-notes-fixes"></a>
+ Fixed a `NativeHost.exe` crash that could occur after complete browser shutdown, and eliminated associated Windows Event Viewer error logs. Closing only the CCP tab or another browser tab did not trigger the defect. Screen recordings and other Connect Customer features were unaffected in earlier versions as `NativeHost.exe` automatically restarts whenever the agent reopens the browser and CCP.

### System prerequisites
<a name="release-notes-prerequisites"></a>

No additional prerequisites need to be installed on the agent's workstation for this release.

## Version summary
<a name="version-summary"></a>

The following table summarizes the differences between Connect Customer Client Application versions. Version 3.0.4 is cumulative: it includes the capabilities introduced in 3.0.2 and the corrections delivered in 3.0.3 and 3.0.4.


| Version | Release date | Download | Summary | 
| --- | --- | --- | --- | 
| 3.0.4 | August 13, 2026 | [Download v3.0.4](https://d4yqf2f7seiym.cloudfront.net/builds/AmazonConnectClientWin-v3.0.4.zip) | Fixes an Amazon.Connect.Client.Messaging.NativeHost.exe crash during full browser shutdown and the resulting Windows Event Viewer errors. Includes all earlier 3.x changes. | 
| 3.0.3 | July 30, 2026 | - | Improves redaction completion at contact end, window-monitoring cleanup, and support for international characters in window titles. | 
| 3.0.2 | June 1, 2026 | - | Adds optional [rule-based screen recording redaction](rule-based-redaction-screen-recording.md) and supporting browser and Windows monitoring components. | 
| 2.0.3 | June 13, 2025 | [Download v2.0.3](https://d4yqf2f7seiym.cloudfront.net/builds/AmazonConnectClientWin-v2.0.3.zip) | Provides standard agent screen recording. It does not include rule-based redaction for screen recordings. | 
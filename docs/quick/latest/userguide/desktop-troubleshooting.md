

# Troubleshooting
<a name="desktop-troubleshooting"></a>

## Installation and launch issues
<a name="desktop-ts-install"></a>
+ macOS reports an unidentified developer: open System Settings, choose Privacy & Security, and choose Open Anyway.
+ The application does not launch: restart, verify the minimum requirements, and check disk space. As a last resort, delete `~/.quickwork/` (macOS) or `%USERPROFILE%\.quickwork\` (Windows) and reinstall. Deleting this directory removes all local data.

## Connection issues
<a name="desktop-ts-connection"></a>
+ A messaging, email, or calendar connection fails: disconnect and reconnect in Customize, on the Connectors tab, verify your permissions in the third-party service, and check your internet connection.
+ A connection shows Not synced: verify connectivity, then disconnect and reconnect; if it persists, the service might be having an outage.
+ Sign-in or responses fail only on a corporate network or virtual private network (VPN): confirm the required Quick domains are reachable, and address Transport Layer Security (TLS) inspection with your network administrator (see [Security, privacy, and architecture](desktop-security.md)). If it persists, export logs and contact AWS Support.

## Performance issues
<a name="desktop-ts-performance"></a>
+ Slow responses: switch to Fast mode, reduce thinking effort to Off or Low, close unused applications, and check your connection.
+ High memory usage: reduce the number of indexed folders, disable semantic search where you do not need it, lower Maximum parallel tasks, and restart to clear cache. Search indexing pauses automatically when free disk space falls below 8.0 GiB.

## File access issues
<a name="desktop-ts-file-access"></a>
+ Quick cannot find a file: confirm the parent folder is added on the Knowledge tab in Customize. System temporary directories are always accessible. After you add a folder, Quick reads it immediately; indexing runs in the background.
+ Search returns no results: confirm keyword search is on for the folder, check that indexing status is Ready, confirm the file is within the maximum index size, and enable semantic search for natural-language queries.

## Browser automation issues
<a name="desktop-ts-browser"></a>

Verify Browser Automation is enabled in Customize, on the Connectors tab. If you use your own browser, complete the remote-debugging setup and test the connection; otherwise, confirm a supported browser is installed.

## Schedule issues
<a name="desktop-ts-schedules"></a>
+ A schedule did not run: confirm the schedule is enabled in Mission Control. Schedules run in the cloud, so they run even when your computer is off; but a run that needs a local tool (file access, browser, or code execution) requires your computer to be on with the desktop running and connected at that time.
+ Unexpected results: in Mission Control, review the schedule's instructions and capabilities, consider a higher model (Balanced or Smart), and run it manually to observe results.

## Managing agent-hours consumption
<a name="desktop-ts-agent-hours"></a>
+ Reduce the number of background schedules; each run consumes agent hours.
+ Match the model and thinking effort to task complexity: Fast with thinking Off for simple tasks; Balanced or Smart with higher thinking levels consume more agent hours.

## Session usage
<a name="desktop-ts-session-usage"></a>

View current session usage by selecting your profile. The session limit is a service-protection limit that spreads your monthly agent-hours allocation over time. When you reach it, the application indicates the allocation has been used, and the limit recovers gradually.

## MCP server issues
<a name="desktop-ts-mcp"></a>
+ Local: verify the command and that the executable is installed, check argument formatting, raise the timeout, and verify environment variables.
+ Remote: verify the URL and that the server is running, verify any authentication header, and check network and firewall settings.
+ Imported: verify the configuration file path and that the source application is installed.

## Exporting diagnostics
<a name="desktop-ts-diagnostics"></a>

Export logs from Settings, on the Advanced tab, by selecting a time range and choosing Export Diagnostics. If you cannot open the application, find logs at `~/Library/Application Support/QuickWork/` and `~/Library/Logs/QuickWork/` (macOS) or `%APPDATA%\QuickWork\` and `%APPDATA%\QuickWork\logs\` (Windows).

## Getting additional help
<a name="desktop-ts-help"></a>

Export diagnostics and share them with your support team, contact your organization's IT administrator for enterprise issues, and visit the Amazon Quick documentation for the latest guidance.
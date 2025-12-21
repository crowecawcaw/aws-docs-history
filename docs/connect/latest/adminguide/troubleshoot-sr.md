# Download the Amazon Connect Client Application log files for

troubleshooting

When you open an AWS Support ticket for issues with screen recordings, include the
log files for Amazon Connect Client Application and shared worker from the agent desktop.

## Amazon Connect Client Application log files (Windows)

On the agent's desktop, navigate to:

- `C:\ProgramData\Amazon\Amazon.Connect.Client.Service\logs`

This file contains the logs including the Websocket connection between
browser and Client Application, and another Websocket connection between
**Amazon.Connect.Client** and
**Amazon.Connect.RecordingSession**.

- `%USERPROFILE%\AppData\Local\Amazon\Amazon.Connect.Client.RecordingSession\Logs`

This file contains logs for screen recording activities. (Not
applicable for version 1.x.)

## Shared Worker logs (Windows and ChromeOS)

Open your CCP. It must be open so you can view the
**ClientAppInterface** shared worker.

### Chrome

1. Open a Chrome browser. For the URL type
   `chrome://inspect/#workers`.
2. In the **Shared workers** section, locate the
   shared worker named **ClientAppInterface**.
3. Choose **inspect** to open a DevTools
   instance.
4. Choose the **Console** tab, right-click the log
   dump, and then select **Save as...** to store the
   log dump to a local file.

### Firefox

1. Open a Firefox browser. For the URL type
   `about:debugging#workers`.
2. In the **Shared workers** section, choose
   **Inspect** for
   **/connect/ccp-naws/static/client-app-interface.js**.
3. Right-click the **Console** tab and select
   **Save all Messages to File** to store the log
   dump to a local file.

### Edge (Chromium)

1. Open a Chrome browser. For the URL type
   `edge://inspect/#workers`.
2. In the **Shared workers** section, locate the
   shared worker named **ClientAppInterface**.
3. Choose **inspect** to open a DevTools
   instance.
4. Choose the **Console** tab, right-click the log
   dump, and then select **Save as...** to store the
   log dump to a local file.

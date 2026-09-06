

# Download the Connect Customer Client Application log files for troubleshooting
<a name="troubleshoot-sr"></a>

When you open an AWS Support ticket for issues with screen recordings, include the log files for Connect Customer Client Application and shared worker from the agent desktop.

## Connect Customer Client Application log files (Windows)
<a name="windows-client-logs"></a>

On the agent's desktop, navigate to:
+ `C:\ProgramData\Amazon\Amazon.Connect.Client.Service\logs`

  This file contains the logs including the Websocket connection between browser and Client Application, and another Websocket connection between **Amazon.Connect.Client** and **Amazon.Connect.RecordingSession**.
+ `%USERPROFILE%\AppData\Local\Amazon\Amazon.Connect.Client.RecordingSession\Logs`

  This file contains logs for screen recording activities. (Not applicable for version 1.x.)
+ `%USERPROFILE%\AppData\Local\Amazon\Amazon.Connect.Client.Messaging.NativeHost\Logs`

  This file contains logs for extension IPC messages. (Not applicable for version < 3.x.)

## Shared Worker logs (Windows and ChromeOS)
<a name="shared-worker-logs"></a>

Open your CCP. It must be open so you can view the **ClientAppInterface** shared worker.

### Chrome
<a name="chrome-logs"></a>

1. Open a Chrome browser. For the URL type `chrome://inspect/#workers`.

1. In the **Shared workers** section, locate the shared worker named **ClientAppInterface**.

1. Choose **inspect** to open a DevTools instance.

1. Choose the **Console** tab, open the context menu for the log dump, and then select **Save as...** to store the log dump to a local file.

### Firefox
<a name="firefox-logs"></a>

1. Open a Firefox browser. For the URL type `about:debugging#workers`.

1. In the **Shared workers** section, choose **Inspect** for **/connect/ccp-naws/static/client-app-interface.js**.

1. Open the context menu for the **Console** tab and select **Save all Messages to File** to store the log dump to a local file.

### Edge (Chromium)
<a name="edge-logs"></a>

1. Open a Chrome browser. For the URL type `edge://inspect/#workers`.

1. In the **Shared workers** section, locate the shared worker named **ClientAppInterface**.

1. Choose **inspect** to open a DevTools instance.

1. Choose the **Console** tab, open the context menu for the log dump, and then select **Save as...** to store the log dump to a local file.

## Troubleshoot rule-based redaction
<a name="troubleshoot-rule-based-redaction"></a>

If you use [Rule-based redaction for screen recordings](rule-based-redaction-screen-recording.md), the following sections describe common issues and how to resolve them.

### The redacted recording is missing
<a name="troubleshoot-redacted-recording-missing"></a>

The redacted recording is produced after the contact ends and after the unredacted recording is finalized. It can take longer than the unredacted version to appear, especially when conversational analytics call recording redaction is also enabled, because the redacted audio must be available before the redacted video is stitched. Allow extra time before treating it as missing.

If the redacted recording still has not appeared after a reasonable wait, check the following.
+ Confirm that screen recording was enabled for the contact by checking the contact record.
+ Confirm that the contact flow invoked the **Set recording, analytics, and processing behavior** block with rule-based redaction enabled before the contact was routed to the agent. For instructions, see [Configure rule-based redaction](configure-rule-based-redaction.md).
+ Confirm that the Connect Customer browser extension was installed and enabled on the agent's browser during the contact. See [Deploy the browser extension](deploy-browser-extension.md).
+ Confirm that the Connect Customer Client Application on the agent workstation is version 3.0.2 or later.

### The redacted recording has no audio
<a name="troubleshoot-redacted-recording-no-audio"></a>

When rule-based redaction is enabled for a contact, Connect Customer stitches the redacted video with the redacted call recording only if conversational analytics call recording redaction is also enabled for the contact. If conversational analytics call recording redaction is not enabled, the redacted recording is produced with no audio. This prevents the original audio from being exposed alongside a redacted video and is by design.
+ To produce a redacted recording that includes redacted audio, enable conversational analytics call recording redaction for the contact in addition to rule-based screen redaction. See [Use sensitive data redaction with conversational analytics](https://docs.aws.amazon.com/connect/latest/adminguide/sensitive-data-redaction.html).
+ If a user needs to review the original audio, remove the **Screen recording (redacted) - Access** permission and grant them the **Screen recording - Access** permission so they can play the unredacted recording, which preserves the original audio.

### The redaction overlay appears in the wrong position
<a name="troubleshoot-redaction-overlay-position"></a>
+ Confirm that the agent's Connect Customer Client Application is version 3.0.2 or later. Earlier versions have known issues with multi-monitor DPI scaling.
+ Confirm that the Connect Customer browser extension is version 2.1.0 or later.
+ If the issue persists on a specific workstation, collect diagnostic logs using the Connect Customer Client Application log collection tool, then open an [AWS Support case](https://console.aws.amazon.com/support/home).

### The Connect Customer browser extension is missing on an agent's workstation
<a name="troubleshoot-extension-missing"></a>

The extension is deployed at user scope through your enterprise browser policy, so this typically indicates that the agent is not in the targeted user group, or that the policy has not yet been applied on the workstation.
+ Confirm that the agent is included in the security group or Entra ID group that your enterprise extension policy targets. For details, see [Deploy the browser extension](deploy-browser-extension.md).
+ On the agent's workstation, open `chrome://extensions`, `edge://extensions`, or `about:addons` to confirm whether the extension is present and enabled.
+ If the policy was applied recently, ask the agent to restart the browser so the policy refresh picks up the new extension.
+ For Chrome and Edge, you can also open `chrome://policy` or `edge://policy` and confirm that **ExtensionSettings** contains the Connect Customer extension ID with status **OK**.

### An authorized user cannot view a redacted recording
<a name="troubleshoot-cannot-view-redacted"></a>
+ Confirm that the user's security profile includes the **Screen recording (redacted) - Access** permission. If the user also needs to download the redacted recording, confirm that the profile includes **Screen recording (redacted) - Enable download button**. For details, see [Permissions for redacted recordings](rule-based-redaction-screen-recording.md#permissions-for-redacted-recordings).
+ Confirm that the contact flow for the contact enabled rule-based redaction. A contact that was recorded without a redaction rule does not produce a redacted file.

### A redacted recording shows unredacted content
<a name="troubleshoot-redacted-shows-unredacted"></a>
+ Confirm that the Connect Customer browser extension is installed and was enabled during the contact. If the extension is uninstalled or disabled, the Connect Customer Client Application records without redaction.
+ Confirm that the Connect Customer Client Application on the agent workstation is version 3.0.2 or later.

### Related information
<a name="troubleshoot-redaction-related"></a>

For general agent screen recording troubleshooting, including browser Local Network Access (LNA) restrictions, see [Troubleshoot screen recording](troubleshoot-screen-recording.md).
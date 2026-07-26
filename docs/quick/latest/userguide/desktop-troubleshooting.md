# Troubleshooting

The following sections describe common issues you might encounter when using the
Amazon Quick desktop application and how to resolve them.

## Installation and launch issues

macOS displays an "unidentified developer" warning

If macOS prevents you from opening the Amazon Quick desktop
application because it's from an unidentified developer, use the
following procedure to allow it.

1. Open **System Settings** on your Mac.
2. Choose **Privacy & Security**.
3. Scroll to the Security section and choose **Open Anyway** next to the message about Quick.
4. Confirm that you want to open the application.

###### Note

On first launch, your operating system might prompt you to confirm that you want to open the application. Choose **Open** to continue.

The application doesn't launch

If the Amazon Quick desktop application doesn't launch, try the following steps.

1. Restart your computer and try opening the application again.
2. Verify that your operating system meets the minimum requirements.
3. Check that you have sufficient disk space available.
4. If the issue persists, delete the `~/.quickwork/` directory (macOS) or `%USERPROFILE%\.quickwork\` directory (Windows) and reinstall the application.

###### Warning

Deleting the `~/.quickwork/` (macOS) or `%USERPROFILE%\.quickwork\` (Windows) directory removes all local data, including conversations, knowledge graph, memory, and saved credentials. Use this step only as a last resort.

## Connection issues

Slack or Outlook connection fails

If a connection to Slack or Microsoft Outlook fails, try the following steps.

1. Disconnect the service in **Settings** > **Capabilities** > **Connectors**.
2. Reconnect the service by choosing **Sign in** and completing the authentication flow.
3. Verify that your account has the required permissions in the third-party service.
4. Check that your internet connection is active and stable.

Microsoft Teams connection fails

If a connection to Microsoft Teams fails, follow the same steps as for Slack or Outlook. Verify that your organization's administrator has not restricted third-party application access.

Connection shows "Not synced" status

If a connection shows a "Not synced" status, try the following steps.

1. Verify that you have an active internet connection.
2. Disconnect and reconnect the service in **Settings** > **Capabilities** > **Connectors**.
3. If the issue persists, the third-party service might be experiencing an outage. Check the service's status page.

Google Workspace connections fail

If connections to Google services (Gmail, Google Calendar, Google Drive, Google Docs, Google Sheets, Google Slides, Google Meet, or Google Analytics) fail, verify the following.

1. Your Google account is not restricted by your organization's admin policies.
2. You have granted the required OAuth permissions during the sign-in flow.
3. You are signing in with the correct Google account.

Sign-in or responses fail on a corporate network or VPN

The Amazon Quick desktop application might fail to sign in or load
responses only when you are connected to a corporate network, VPN, or
secure web gateway, but work normally when you disconnect. When that
happens, your organization's network is likely blocking or inspecting the
connection. Complete the following steps with your network
administrator.

1. Confirm that the required Amazon Quick domains are
   reachable from your network. For the list of domains to add to your
   allow list, see [Network access and required domains](desktop-security.md#desktop-network-access "desktop-security.md#desktop-network-access").
2. If your organization inspects encrypted traffic (TLS or
   SSL inspection), your operating system's certificate store must trust
   the inspection certificate authority, or the Amazon Quick domains must
   be excluded from inspection. Your network administrator can confirm
   whether inspection is active and configure either
   option.

If the issue persists after your network administrator confirms the
domains are reachable and resolves any inspection issues, export your
application logs (see [Exporting diagnostics](#desktop-ts-diagnostics "#desktop-ts-diagnostics")) and contact AWS
Support.

## Performance issues

Slow responses

If Quick responses are slow, try the following steps.

1. Switch to the **Fast** response mode for quicker responses. Choose the response preferences selector in the chat input area and select **Fast**.
2. Reduce the **thinking effort** level. Lower thinking effort (Off or Low) produces faster responses.
3. Close unused applications to free up system resources.
4. Check your internet connection speed. AI model requests require a network connection to API Gateway.

High memory usage

If the Amazon Quick desktop application uses excessive memory, try the following steps.

1. Reduce the number of folders indexed in **Settings** > **My computer**. Disable **Semantic search** for folders that don't require it, as semantic search uses more resources than keyword search.
2. Lower the **Max parallel tasks** slider in **Settings** > **Customization** > **Performance**. The default value is 50. Reducing this value limits the number of concurrent background operations.
3. Restart the application to clear cached data.
4. Adjust search indexing limits in **Settings** > **My computer** > **Search indexing**. Lower the **Storage limit**, **Max file size for indexing**, or **Max folder size for indexing** sliders.

###### Note

Search indexing automatically pauses when free disk space falls below 8.0 GiB.

## File access issues

Quick can't find a file

If Quick can't find a file you reference in chat, verify the following.

1. The file's parent folder is added in **Settings** > **My computer** > **Local folders**. Quick can only access files in folders you explicitly grant access to, with the exception of system temporary directories, which are always accessible. On Windows, these are `C:\TEMP`, `C:\TMP`, `\TEMP`, and `\TMP`. On macOS and Linux, these are `/tmp`, `/var/tmp`, and `/usr/tmp`.
2. Choose **+ Add folder** to grant access to additional folders.
3. After adding a folder, Quick can immediately read files in it. Indexing for search happens in the background.

Search returns no results

If file search returns no results, try the following steps.

1. Verify that **Keyword search** is toggled on for the folder in **Settings** > **My computer** > **Local folders**. Expand the folder to see its indexing toggles.
2. Check the indexing status. A **Ready** status with file and entry counts confirms indexing is complete.
3. If you recently added a new folder, wait for indexing to complete. The status shows progress.
4. Check that the file is not larger than the **Max file size for indexing** limit in **Settings** > **My computer** > **Search indexing**. Files larger than this limit are skipped during indexing but are still available to the agent through direct file access.
5. For broader search, enable **Semantic search** on the folder to allow natural language queries.

## Browser automation issues

Browser automation doesn't work

If Quick can't browse web pages, try the following steps.

1. Verify that **Browser Automation** is enabled in **Settings** > **Capabilities** > **Tools**.
2. If using "Use my Chrome" mode, verify the setup in **Settings** > **Customization** > **Browser**. Open Chrome and navigate to `chrome://inspect/#remote-debugging`. Choose **Enable remote debugging**. Return to Quick and choose **Test Connection** to verify the connection.
3. If using the default mode, Quick launches a separate Chrome instance with a copy of your profile. Ensure Chrome is installed on your system.

## Scheduled task issues

A scheduled task didn't run

Scheduled tasks run locally on your computer. If an agent didn't run at its scheduled time, verify the following.

1. Your computer was turned on and awake at the scheduled time.
2. The Amazon Quick desktop application was running.
3. The agent is enabled. Check the toggle in **Mission Control**, accessible from the top bar.
4. Your internet connection was active. Agents that access connected services or AI models require a network connection.

###### Important

If your computer is off or the application is closed when an agent is scheduled to run, the agent does not run until the next scheduled time.

Agent produces unexpected results

If a scheduled task produces unexpected results, try the following steps.

1. Open **Mission Control** from the top bar and select the agent.
2. Review the **Prompt** tab to verify the agent's instructions are correct.
3. Check the **Capabilities** tab to verify the correct MCP servers are attached.
4. Consider changing the **Model** in the **Overview** tab. Use **Balanced** or **Smart** for more complex agent tasks.
5. Choose the **Run** button (play icon) to manually trigger the agent and observe the results.

## Managing agent hours consumption

If you are monitoring or reducing
agent hours consumption, consider the following configurations.

- **Scheduled tasks** – Consider
  reducing the number of tasks that run in the background. Each scheduled
  task execution consumes agent hours.
- **Response mode and thinking level**
  – Use the **Fast** response mode with
  thinking level set to **Off** for simpler
  tasks. **Balanced** and **Smart** modes with higher thinking levels (Low,
  Medium, High) consume more agent hours per interaction. Match the
  response mode and thinking level to the complexity of the task.

## Understanding session usage limits

You can view your current session usage by selecting your profile in the
bottom left area of the desktop application. The session usage limit is a
service protection limit that distributes your monthly agent hours allocation
over time rather than allowing the full allocation to be consumed at once.

When you reach the session limit, the desktop application displays a message
indicating that your session allocation has been used. The limit resets on a
rolling window, recovering gradually over time.

If you encounter this limit frequently, see
[Managing agent hours consumption](#desktop-ts-agent-hours "#desktop-ts-agent-hours").

## MCP server issues

MCP server fails to connect

If an MCP server fails to connect, try the following steps based on the connection type.

**Local MCP server:**

1. Verify that the command is correct and the executable is installed on your system.
2. Check that the arguments are space-separated and correctly formatted.
3. Increase the **Timeout** value if the server takes longer than 30 seconds to start (configurable from 5 to 300 seconds).
4. Verify that any required **Environment variables** are correctly set.

**Remote MCP server:**

1. Verify that the URL is correct and the server is running.
2. If authentication is required, verify the **Token** value is a valid bearer token.
3. Check your network connection and any firewall settings.

**Imported MCP server:**

1. Verify that the config file path is correct.
2. Ensure the source application (Kiro, Claude Code, AIM, and so on) is properly installed.

## Exporting diagnostics

If you need to share diagnostic information for troubleshooting, you can export diagnostic logs from the application.

1. Open **Settings** > **Customization**.
2. Scroll to the **Troubleshooting** section.
3. Select a time range from the dropdown (for example, **Last 2 hours**).
4. Choose **Export Diagnostics** to save diagnostic logs to your desktop.

If you cannot open the application to export diagnostics, you can find the
log files directly on your machine at the following locations.

- **macOS** –
  `~/Library/Application Support/QuickWork/` for the
  current log, and `~/Library/Logs/QuickWork/` for
  dated logs.
- **Windows** –
  `%APPDATA%\QuickWork\` for the current log, and
  `%APPDATA%\QuickWork\logs\` for dated logs.

## Resetting the application

If other troubleshooting steps don't resolve your issue, you can reset the application by clearing all data.

###### Warning

This action is irreversible. It removes all Quick data, including conversations, cached messages, knowledge graph, saved credentials, and user preferences. The application quits after cleanup.

1. Open **Settings** > **Customization**.
2. Scroll to the **Danger zone** section.
3. Choose **Clear all data**.
4. Confirm the action.
5. To fully uninstall on macOS, drag `Amazon Quick.app` to Trash. On Windows, open **Settings** > **Apps** > **Installed apps**, find Amazon Quick, and choose **Uninstall**.

## Getting additional help

If the preceding troubleshooting steps don't resolve your issue, you can use the following resources.

- **Export diagnostics** and share them with your support team.
- Contact your organization's IT administrator for enterprise account issues.
- Visit the Amazon Quick documentation for the latest guidance.

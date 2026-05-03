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

1. Disconnect the service in **Settings** > **Capabilities** > **Connections**.
2. Reconnect the service by choosing **Sign in** and completing the authentication flow.
3. Verify that your account has the required permissions in the third-party service.
4. Check that your internet connection is active and stable.

Microsoft Teams connection fails

If a connection to Microsoft Teams fails, follow the same steps as for Slack or Outlook. Verify that your organization's administrator has not restricted third-party application access.

Connection shows "Not synced" status

If a connection shows a "Not synced" status, try the following steps.

1. Verify that you have an active internet connection.
2. Disconnect and reconnect the service in **Settings** > **Capabilities** > **Connections**.
3. If the issue persists, the third-party service might be experiencing an outage. Check the service's status page.

Google Workspace connections fail

If connections to Google services (Gmail, Google Calendar, Google Drive, Google Docs, Google Sheets, Google Slides, Google Meet, or Google Analytics) fail, verify the following.

1. Your Google account is not restricted by your organization's admin policies.
2. You have granted the required OAuth permissions during the sign-in flow.
3. You are signing in with the correct Google account.

## Performance issues

Slow responses

If Quick responses are slow, try the following steps.

1. Switch to the **Fast** AI model mode for quicker responses. Choose the model selector in the chat input area and select **Fast**.
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

1. The file's parent folder is added in **Settings** > **My computer** > **Local folders**. Quick can only access files in folders you explicitly grant access to.
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

1. Verify that **Browser Automation** is enabled in **Settings** > **Capabilities** > **System**.
2. If using "Use my Chrome" mode, verify the setup in **Settings** > **Customization** > **Browser**. Open Chrome and navigate to `chrome://inspect/#remote-debugging`. Choose **Enable remote debugging**. Return to Quick and choose **Test Connection** to verify the connection.
3. If using the default mode, Quick launches a separate Chrome instance with a copy of your profile. Ensure Chrome is installed on your system.

## Scheduled agent issues

A scheduled agent didn't run

Scheduled agents run locally on your computer. If an agent didn't run at its scheduled time, verify the following.

1. Your computer was turned on and awake at the scheduled time.
2. The Amazon Quick desktop application was running.
3. The agent is enabled. Check the toggle in **Settings** > **Capabilities** > **Scheduled tasks**, or open the **Agents** panel from the top bar.
4. Your internet connection was active. Agents that access connected services or AI models require a network connection.

###### Important

If your computer is off or the application is closed when an agent is scheduled to run, the agent does not run until the next scheduled time.

Agent produces unexpected results

If a scheduled agent produces unexpected results, try the following steps.

1. Open **Settings** > **Capabilities** > **Scheduled tasks** and select the agent.
2. Review the **Prompt** tab to verify the agent's instructions are correct.
3. Check the **Capabilities** tab to verify the correct MCP servers are attached.
4. Consider changing the **Model** in the **Overview** tab. Use **Balanced** or **Smart** for more complex agent tasks.
5. Choose the **Run** button (play icon) to manually trigger the agent and observe the results.

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
- **Developer menu** – Choose the connection status dot (green dot in the top-right corner) to access Mission Control, Metrics overlay, Debug panel, and Memory panel for advanced diagnostics.
- Contact your organization's IT administrator for enterprise account issues.
- Visit the Amazon Quick documentation for the latest guidance.

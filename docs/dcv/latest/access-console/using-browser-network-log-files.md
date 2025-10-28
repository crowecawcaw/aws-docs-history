# Using browser and network log files

The web browser communicates with the Handler component to view and modify resources. If there are issues with communication
between the web browser and the Handler, you can troubleshoot using the browser and network log files.

## Accessing Chrome console logs

From a Chrome browser, access the console log window.

1. Do one of the following:
   - Use the shortcut key. For Windows and Linux, use `Ctrl+Shift+J`. For macOS, use, `Cmd+Opt+J`.
   - Select the Chrome menu button on the upper right hand side, select **More Tools** then choose **Developer Tools**.

2. Select the **Console** tab in the **Developer Tools** pane.

In the **Console** tab, errors are highlight in red and warnings are highlight in yellow.

## Accessing Chrome network logs

From a Chrome browser, the network tab contains network calls for uploaded and downloaded resources.

1. Do one of the following:
   - Use the shortcut key. For Windows and Linux, use `Ctrl+Shift+J`. For macOS, use, `Cmd+Opt+J`.
   - Select the Chrome menu button on the upper right hand side, select **More Tools** then choose **Developer Tools**.

2. Select the **Network** tab in the **Developer Tools** pane.
3. Refresh the page.

Errors are highlighted in red. Select an error to see more information about it.

The **Status Code** in both the **Headers** and the **Response** tabs can be used to diagnose issues.

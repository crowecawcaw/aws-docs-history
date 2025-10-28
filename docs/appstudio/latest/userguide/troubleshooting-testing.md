# Troubleshooting in the Testing environment

This topic contains information about troubleshooting apps published to the Testing environment.

###### Note

An HTTP 500 response
from an automation or data action may be caused by a runtime crash in your expressions, a connector failure, or throttling from a data source
that is connected to your application. Use the instructions in
[Using your browser console to debug](#troubleshooting-testing-browser-console "#troubleshooting-testing-browser-console") to
view the debug logs that will show the underlying error details.

## Using the debug panel

Similar to the building debug panel used when building your apps, App Studio provides a collapsible debug panel in the Testing environment.
This panel shows informational messages such as page load time, user navigation, and app events. It also contains errors and warnings.
The debug panel automatically updates with new messages as events occur.

## Using your browser console to debug

Since actions are not invoked while previewing your app, your app will need to be published to the Testing environment to
test its call and response handling. If an error occurs during the execution of your automation
or if you want to understand why the application behaves in certain way, you can use your browser’s console for real time
debugging.

###### To use your browser console to debug apps in the Testing environment

1. Append `?debug=true` to the end of the URL and press enter. Note that if the URL
   already has a query string (it contains `?`), instead append `&debug=true` to the end of the URL.
2. Open your browser console to start debugging by exploring your action or API inputs and outputs.
   - In Chrome: Right click in your browser and choose **Inspect**. For more information about
     debugging with Chrome DevTools, see the [Chrome DevTools documentation](https://developer.chrome.com/docs/devtools "https://developer.chrome.com/docs/devtools").
   - In Firefox: Press and hold or right-click on a webpage element, then choose **Inspect Element**.
     For more information about debugging with Firefox DevTools, see the
     [Firefox DevTools User Docs](https://firefox-source-docs.mozilla.org/devtools-user/ "https://firefox-source-docs.mozilla.org/devtools-user/").

The following list contains some common issues that produce errors:

- **Runtime errors**
  - **Problem:** If an automation or expression is configured incorrectly, it can cause an error when the automation is run. Common
    errors are renaming assets, resulting in incorrect expressions, other JavaScript compilation errors, or attemps to use data or assets
    that are `undefined`.
  - **Solution:** Check each usage of custom code input (expressions, JavaScript, and JSON)
    and make sure there are no compilation errors in the code editor or debug panel.

- **Connector issues**
  - **Problem:** Because App Studio apps do not communicate with
    external services with connectors until they are published, errors can occur in the Testing environment that did not occur during preview.
    If an action in an automation that uses a connector fails, it could be from a misconfiguration in the action that sends the request to the
    connector, or with the connector configuration itself.
  - **Solution:** You should use **Mocked output** to test automations early
    in the preview environment to prevent these errors. Ensure your connector is configured correctly, for more information,
    see [Troubleshooting connectors](troubleshooting-connectors.md "troubleshooting-connectors.md"). Lastly, you can use CloudWatch to
    review the logs. For more information, see [Debugging with logs from published apps in Amazon CloudWatch Logs](troubleshooting-cloudwatch.md "troubleshooting-cloudwatch.md").
    In the `ConnectorService` namespace logs, there should be error message or metadata that originated from the connector.

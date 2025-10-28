# Viewing integrations with code repositories

This topic describes how to view integrations in the Amazon Inspector console.

###### To view integrations in the Amazon Inspector console

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. From the navigation pane, choose **Code Security**.
3. Choose **Integrations**.
   From this tab, you can review all of your configured integrations and review basic information about all of your integrations.
   This information includes the name of the integration, status of the integration, and source code provider name.

###### Re-authenticate to provider

After you create the integration, you can encounter a scenario where Amazon Inspector is unable to refresh the access token.
This can occur if the integration host is unavailable or Amazon Inspector experiences other communication issues.
To remediate the issue, you can re-authenticate the connection from the **Integrations** tab on the **Code Security** page.
Under the **Status** column, the integration shows as **Inactive**, and Amazon Inspector provides the option to re-authenticate.
Choose **Re-authenticate**.
You're redirected to the integration workflow where you can complete the connection setup.

If you delete system settings for your integration, you can lose connection indefinitely.
If this occurs, you must [delete the integration](code-security-assessments-connect-delete-integrations.md "code-security-assessments-connect-delete-integrations.md") and create a new integration.
When you delete an integration, you lose all projects and scan configurations associated with the integration.

# Removing the browser extension as an integration

To disable the browser extension to your existing web experience, Admin users can
use the Amazon Q Business console or the Amazon Q Business API, AWS SDK, or AWS CLI.

###### Topics

- [Using the console](#removing-using-console "#removing-using-console")
- [Using the AWS API](#removing-browser-extension-using-aws-api "#removing-browser-extension-using-aws-api")
- [Blocking and removing the browser extension](#blocking-removing-extension "#blocking-removing-extension")

## Using the console

1. Sign in to the Amazon Q console.
2. Choose **Applications**, then select the name of your
   application environment from the list.
3. Choose **Integrations** under
   **Enhancements**.
4. Choose **Edit** in the **Browser
   extensions** section on the main page.
5. Deselect the **Browser extensions** you no longer
   want integrate with.

## Using the AWS API

You can disable browser extensions using the [`UpdateWebExperience`](../api-reference/API_UpdateWebExperience.md "../api-reference/API_UpdateWebExperience.md") API

## Blocking and removing the browser extension

Once you disable your browser extension, your users will no longer be able to
login. However, you will still need to take steps to uninstall the extension on
user's browser via

- Uninstall the browser extension for all users by updating the policy
  settings using the mobile device management software (MDM) using one of
  the following:
  - Firefox policy settings: [https://mozilla.github.io/policy-templates/#extensionsettings](https://mozilla.github.io/policy-templates/#extensionsettings "https://mozilla.github.io/policy-templates/#extensionsettings")
  - Chrome policy settings: [https://chromeenterprise.google/policies/#ExtensionSettings](https://chromeenterprise.google/policies/#ExtensionSettings "https://chromeenterprise.google/policies/#ExtensionSettings")
  - Edge policy settings: [https://learn.microsoft.com/en-us/DeployEdge/microsoft-edge-policies#extensionsettings](https://learn.microsoft.com/en-us/DeployEdge/microsoft-edge-policies#extensionsettings "https://learn.microsoft.com/en-us/DeployEdge/microsoft-edge-policies#extensionsettings")
    and guide: [https://learn.microsoft.com/en-us/deployedge/microsoft-edge-manage-extensions-ref-guide](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-manage-extensions-ref-guide "https://learn.microsoft.com/en-us/deployedge/microsoft-edge-manage-extensions-ref-guide")

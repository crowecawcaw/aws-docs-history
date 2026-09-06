

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Removing the browser extension as an integration
<a name="removing-browser-extension"></a>

To disable the browser extension to your existing web experience, Admin users can use the Amazon Q Business console or the Amazon Q Business API, AWS SDK, or AWS CLI.

**Topics**
+ [Using the console](#removing-using-console)
+ [Using the AWS API](#removing-browser-extension-using-aws-api)
+ [Blocking and removing the browser extension](#blocking-removing-extension)

## Using the console
<a name="removing-using-console"></a>

1. Sign in to the Amazon Q console.

1. Choose **Applications**, then select the name of your application environment from the list.

1. Choose **Integrations** under **Enhancements**.

1. Choose **Edit** in the **Browser extensions** section on the main page.

1. Deselect the **Browser extensions** you no longer want integrate with.

## Using the AWS API
<a name="removing-browser-extension-using-aws-api"></a>

You can disable browser extensions using the [`UpdateWebExperience`](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateWebExperience.html) API

## Blocking and removing the browser extension
<a name="blocking-removing-extension"></a>

Once you disable your browser extension, your users will no longer be able to login. However, you will still need to take steps to uninstall the extension on user's browser via
+ Uninstall the browser extension for all users by updating the policy settings using the mobile device management software (MDM) using one of the following:
  + Firefox policy settings: [https://mozilla.github.io/policy-templates/\#extensionsettings](https://mozilla.github.io/policy-templates/#extensionsettings)
  + Chrome policy settings: [https://chromeenterprise.google/policies/\#ExtensionSettings](https://chromeenterprise.google/policies/#ExtensionSettings)
  + Edge policy settings: [https://learn.microsoft.com/en-us/DeployEdge/microsoft-edge-policies\#extensionsettings](https://learn.microsoft.com/en-us/DeployEdge/microsoft-edge-policies#extensionsettings) and guide: [https://learn.microsoft.com/en-us/deployedge/microsoft-edge-manage-extensions-ref-guide](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-manage-extensions-ref-guide)
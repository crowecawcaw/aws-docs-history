

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Configuring the Amazon Q Business Microsoft Teams (Teams) integration for use
<a name="msteams-configuration"></a>

**Note**  
When Amazon Q is invoked by a user in a public Teams channel, it generates responses based on the invoking user's permissions, which may include content that other channel members aren't authorized to access. To prevent unintended exposure of sensitive information, carefully evaluate the use of Amazon Q in public channels. 
The Amazon Q Business customer integrating Microsoft Teams (Teams) must have a paid Teams organization.
Amazon Q supports users who authenticate using external SAML providers through IAM Identity Center. For more information, see [Create an IAM Identity Center-integrated application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html).
Amazon Q application environment created with IAM Federation do not support integrations with Teams at this time.
Access using the Amazon Q Business API is not supported at this time.
Amazon Q Business does not use your user data for service improvement or for training its underlying large language models (LLMs). For more information, see [Amazon Q Business Service improvement](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/service-improvement.html).
Uploading documents and conversations will follow the same behavior as the web experience. For more information, see the [Chat and file uploads](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-web-experience.html#upload-documents) section in the Using web experience topic.

**Topics**
+ [Prerequisites](#msteams-configuration-prerequisites)
+ [Adding an Amazon Q Business integration for Microsoft Teams](#msteams-adding)
+ [Removing Microsoft Teams as an integration](#msteams-removing)

## Prerequisites
<a name="msteams-configuration-prerequisites"></a>

As admins, before you can add the Amazon Q Business integration to your Microsoft Teams (Teams), you must complete the following steps:

1. You must have a Microsoft 365 Business subscription and be a *Global Admin* or someone with administrative permissions, specifically `AppCatalog.ReadWrite.All`.

1. [Get started with Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/getting-started.html)

1. [Create an IAM Identity Center-integrated application environment](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html) environment and create your Amazon Q Business web experience.
**Note**  
[IAM federated application environment](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html) environments do not support integrations with Teams.

1. Optionally, to enhance your end users' experience with Amazon Q in Teams, you can enable *Allow end users to send queries directly to the LLM* in your Admin controls and guardrails. For more information, see the [Response settings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-global-controls.html#guardrails-global-response) topic in [Admin controls and guardrails](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html) and `chatMode` if you are configuring programmatically.

1. Add the two IAM roles and trust policies for adding integrations. For more information, see [IAM roles and trust policy for your integrations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/amazon-q-business-integrations-iam.html)

1. Your Microsoft 365 tenant ID. For more information, see [How to find your tenant ID - Microsoft Entra](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant) in the Microsoft Learn portal.

## Adding an Amazon Q Business integration for Microsoft Teams
<a name="msteams-adding"></a>

To use the Amazon Q Business Teams integration, you must allow it to connect to your Amazon Q Business application environment and web experience. To do this, admins can use the Amazon Q Business console, API, SDK, or AWS CLI.

**Note**  
This integration can only be added using the AWS Management Console at this time.

**Topics**
+ [Using the console](#msteams-adding-console)
+ [Installing the Amazon Q Business app in your Microsoft Teams organization](#msteams-installing)

### Using the console
<a name="msteams-adding-console"></a>

1. Sign in to the Amazon Q console.

1. Choose **Applications**, then select the name of your application environment from the list.

1. Choose **Integrations** under **Enhancements**.

1. Choose **Add integration** from the **Integrations** section on the main page.

1. Choose **Microsoft Teams** as your integration.

1. On the **Add Teams integration page**, enter the **Name** of your integration. This is the display name for the integration resource in AWS.

1. Add a **description** (optional).

1. Enter your **Teams Tenant ID**. This can be found in the *Microsoft Entra Admin Center*. For more information, see [How to find your tenant ID - Microsoft Entra](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant)

1. Choose the type of **Service access** method that you want the Teams integration to use as authorization while accessing your service. You can **Create a new service role** or **Use an existing service role**. For more information, see [IAM role for allowing the integration to call Amazon Q Business on your end user's behalf](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/amazon-q-business-integrations-iam-allow-integration-access.html).

1. Choose the **Access management access** for the Teams integration to authorize to connect to IAM Identity center. For more information, see [IAM role for allowing Amazon Q Business to monitor the resources that the integration creates in your account](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/amazon-q-business-integrations-iam-allow-qbusiness-monitor.html).

1. Optionally, add any **Tags** that are relevant for this Teams integration.

1. Choose **Add integration**.

1. Once the integration has been successfully created, you will move to the **Integration details page**.

1. Choose **Deploy integration**.

1. Choose **Access Teams**.
**Note**  
This link will take you to the Teams domain outside of AWS.

1. You will continue this procedure within the Teams domain.

### Installing the Amazon Q Business app in your Microsoft Teams organization
<a name="msteams-installing"></a>

The following instructions show how to install the Amazon Q Business App in your Microsoft Teams (Teams) workspace using a link from the Amazon Q console as shown in the previous topic.

**Note**  
Only a Teams *Global Admin* or someone with administrative permissions can add the Amazon Q Business App to your Teams organization, specifically `AppCatalog.ReadWrite.All`.
There can be only one instance of the Amazon Q App per Teams organization. That instance will be connected to the application environment that the Teams integration was configured with in the previous topic.

1. Open the link and login as Global Admin or or someone with administrative permissions can add the Amazon Q Business App to the Microsoft Teams admin center for your organization.

1. Choose **Teams apps** in the left navigation.

1. Choose **Amazon Q Business** from the list of available apps.

1. Review and grant admin consent by choosing the **Permissions** tab and reviewing the permissions and choose **Grant admin consent**.
**Note**  
If permissions are already granted, proceed to the end of the procedure, there is no further action required.

1. Authenticate and choose **Accept** for Amazon Q Business app.

1. Confirm that an app titled **Amazon Q Business Permissions** tab now says **Admin consent granted for all required permissions**.

All users assigned to the app from the **Teams admin center** can now find the app in the **Built for your org** section of the **Apps** page of their Teams app.

## Removing Microsoft Teams as an integration
<a name="msteams-removing"></a>

To remove the Microsoft Teams (Teams) integration, admin users can use the Amazon Q Business console.

**Note**  
This integration can only be removed using the AWS Management Console at this time.

### Using the console
<a name="msteams-removing-console"></a>

1. Sign in to the Amazon Q console.

1. Choose **Applications**, then select the name of your application environment from the list.

1. Choose **Integrations** under **Enhancements**.

1. Find and select your Teams integration from the **Integrations** section on the main page.

1. Choose **Delete** and confirm your choice.

Once you disable your Microsoft Teams (Teams) integration, your users will no longer be able to login. However you will still need to take steps to uninstall the Amazon Q Business App in your Teams organization.
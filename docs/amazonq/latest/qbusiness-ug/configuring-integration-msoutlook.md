

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Configuring the Amazon Q Business Microsoft Outlook Add-in for use
<a name="configuring-integration-msoutlook"></a>

**Note**  
The Amazon Q Business customer integrating Microsoft Outlook (Outlook) must have a paid Outlook organization.
Amazon Q supports users who authenticate using external SAML providers through IAM Identity Center. For more information, see [Create an IAM Identity Center-integrated application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html).
Amazon Q application environment created with IAM federation does not support the Outlook Add-in.
Access using the Amazon Q Business API is not supported at this time.
Amazon Q Business does not use user data for service improvement or for training its underlying large language models (LLMs). For more information, see [Amazon Q Business Service improvement](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/service-improvement.html).
Uploading documents and conversations will follow the same behavior as the web experience. For more information, see the [Chat and file uploads section ](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-web-experience.html#upload-documents) in the Using web experience topic.

**Topics**
+ [Prerequisites for integrating the Amazon Q Microsoft Outlook Add-in](#integration-msoutlooks-prerequisites)
+ [Integrating Microsoft Outlook with the Amazon Q Business Add-in](#integrating-integration-msoutlook)

## Prerequisites for integrating the Amazon Q Microsoft Outlook Add-in
<a name="integration-msoutlooks-prerequisites"></a>

As admins, before you can integrate the Amazon Q Business Microsoft Outlook (Outlook) Add-in, you must complete the following steps.

1. You must have a Microsoft 365 Business subscription and be a *Global Admin* or someone with administrative permissions, specifically `AppCatalog`.`ReadWrite`. `All`.

1. You need your Microsoft 365 tenant ID. For more information, see [How to find your tenant ID - Microsoft Entra](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant) in the *Microsoft Learn portal*.

1. [Get started with Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/getting-started.html)

1. [Create an IAM Identity Center-integrated application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html) and create your Amazon Q Business web experience.
**Note**  
[IAM federated application environments](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html) do not support integrations with Outlook.

1. Add the two IAM roles and trust policies for adding integrations. For more information, see [IAM roles and trust policy for your integrations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/amazon-q-business-integrations-iam.html).

1. To use this feature, you must enable **Allow end users to send queries directly to the LLM** in your Admin controls and guardrails. For more information, see the [Response settings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-global-controls.html#guardrails-global-response) topic in [Admin controls and guardrails](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html) and [`chatMode`](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ChatSync.html#qbusiness-ChatSync-request-chatMode) if you are configuring programmatically.

## Integrating Microsoft Outlook with the Amazon Q Business Add-in
<a name="integrating-integration-msoutlook"></a>

To use the Amazon Q Business Add-in for Microsoft Outlook, you must allow it to connect to your Amazon Q Business application environment and web experience. 

**Note**  
This integration can only be added using the Amazon Q Business console.

### Using the console
<a name="integrating-integration-msoutlook-using-console"></a>

1. Sign in to the Amazon Q Business console.

1. Choose **Applications**, then select the name of your application environment from the list.

1. Choose **Integrations** under **Enhancements**.

1. Choose **Add integration** from the **Integrations** section on the main page.

1. Choose **Microsoft Outlook** as your integration.

1. On the **Add Outlook integration page**, enter the **Name** of your integration. This is the display name for the integration resource in AWS.

1. Add a **description** (optional).

1. In the **Workspace** section, enter your Microsoft **Tenant ID**. This can be found in the *Microsoft Entra Admin Center*. For more information, see [How to find your tenant ID - Microsoft Entra](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant)

1. Choose the type of **Service access** method that you want the Outlook integration to use as authorization while accessing your service. You can **Create a new service role** or **Use an existing service role**. For more information, see [IAM role for allowing the integration to call Amazon Q Business on your end user's behalf](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/amazon-q-business-integrations-iam-allow-integration-access.html).

1. Choose the **Access management access** for the Outlook integration to authorize to connect to IAM Identity center. For more information, see [IAM role for allowing Amazon Q Business to monitor the resources that the integration creates in your account](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/amazon-q-business-integrations-iam-allow-qbusiness-monitor.html).

1. Optionally, add any **Tags** that are relevant for this Teams integration.

1. Choose **Add integration**.

1. Once you have added the integration, Amazon Q will deploy your integration. You will see that update on the **Integration details page**.

   Once the integration is *deployed*, choose the name of your Outlook integration from the list of integrations in the **Integrations** section.

1. Copy the **Manifest URL** in the **Integration details** section.
**Note**  
You will now continue the remainder of this procedure within the *Microsoft 365 admin center*.

1. In the Microsoft 365 admin center, choose **Integrated apps** from the left navigation and choose **Upload custom apps** This will open the **Deploy New App** page.

1. Choose **Office Add-in** as your App type.

1. Paste the manifest URL link you copied in the **Provide link to manifest file** and choose **Validate**.

1. Choose the users you want to add in the **Add users** section.

1. Choose **Accept permissions** in the **Accept permissions requests** section and deploy the Add-in. Once deployment is completed, you users will be able to install the Amazon Q Business Add-in in their Microsoft Outlook.
**Note**  
Authentication may be required.
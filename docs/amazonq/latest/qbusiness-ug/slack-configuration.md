

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Configuring the Amazon Q Business Slack integration for use
<a name="slack-configuration"></a>

The Amazon Q Business integration for Slack is only available for use by Amazon Q Business Pro users.

**Note**  
When Amazon Q is invoked by a user in a public Slack channel, it generates responses based on the invoking user's permissions, which may include content that other channel members aren't authorized to access. To prevent unintended exposure of sensitive information, carefully evaluate the use of Amazon Q in public channels. 
The Amazon Q Business customer integrating Slack must have a paid Slack workspace.
Amazon Q only supports user access management through IAM Identity Center for Slack integrations. This includes authentication using external SAML providers through IAM Identity Center. To integrate Slack with Amazon Q, you must create an IAM Identity Center-integrated application. For more information, see [Create an IAM Identity Center-integrated application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html).
Amazon Q doesn't support Slack integrations for [Amazon Q applications using IAM federation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html) for user access management.
Access using the Amazon Q Business API is not supported at this time.
Amazon Q Business does not use your user data for service improvement or for training its underlying large language models (LLMs). For more information, see [Amazon Q Business Service improvement](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/service-improvement.html).
Uploading documents and conversations will follow the same behavior as the web experience. For more information, see the [Chat and file uploads](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-web-experience.html#upload-documents) section in the Using web experience topic.

**Topics**
+ [Prerequisites](#slack-configuration-prerequisites)
+ [Adding an Amazon Q Business integration for Slack](#slack-adding)
+ [Removing Slack as an integration](#slack-removing)

## Prerequisites
<a name="slack-configuration-prerequisites"></a>

As admins, before you can add the Amazon Q Business integration to your Slack, you must complete the following steps:

1. Must have a paid Slack workspace

1. [Get started with Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/getting-started.html)

1. [Create an IAM Identity Center-integrated application environment](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html) environment and create your Amazon Q Business web experience.
**Note**  
Amazon Q doesn't support Slack integrations for [Amazon Q applications using IAM federation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html) for user access management.

1. Optionally, to enhance your end users' experience with Amazon Q in Slack, you can enable ** Allow end users to send queries directly to the LLM** in your Admin controls and guardrails. For more information, see the [Response settings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-global-controls.html#guardrails-global-response) topic in [Admin controls and guardrails](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html) and `chatMode` if you are configuring programmatically.

1. Add the two IAM roles and trust policies for adding integrations. For more information, see [IAM roles and trust policy for your integrations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/amazon-q-business-integrations-iam.html)

1. Admin access to your Slack workspace.

1. Your Slack workspace ID. Your WorkSpace ID must start with a *T*. One way to find your Slack workspace ID is by navigating to your Slack workspace and starting a chat with the *Slack Developer Tools* app running the `/sdt whoami` command. For more information, see [Locate your Slack URL or ID](https://slack.com/help/articles/221769328-Locate-your-Slack-URL-or-ID) in the Slack help center.

## Adding an Amazon Q Business integration for Slack
<a name="slack-adding"></a>

To use the Amazon Q Business Slack integration, you must allow it to connect to your Amazon Q Business application environment and web experience. To do this, admins can use the Amazon Q Business console, API, SDK, or AWS CLI.

**Note**  
This integration can only be added using the AWS Management Console at this time.

**Topics**
+ [Using the console](#slack-adding-console)
+ [Installing the Amazon Q Business App in your Slack workspace](#slack-installing)

### Using the console
<a name="slack-adding-console"></a>

1. Sign in to the Amazon Q console.

1. Choose **Applications**, then select the name of your application environment from the list.

1. Choose **Integrations** under **Enhancements**.

1. Choose **Add integration** from the **Integrations** section on the main page.

1. Choose **Slack** as your integration.

1. On the **Add Slack integration page**, enter the **Name** of your integration. This is the display name for the integration resource in AWS.

1. Add a **description** (optional).

1.  Enter your Slack workspace ID. This is a unique identifier of your Slack workspace starting and can be found using the Slack developer tools app. To find your workspace ID:

   1. Navigate to your Slack workspace and in “Apps” search for “Slack Developer Tools”.

   1.  Open the Slack Developer Tools app and run the command /sdt whoami 

   1.  You will receive a response that contains your Workspace ID starting with a “T” 

   1. For other ways to locate your workspace ID, refer to [Locate your Slack URL or ID](https://slack.com/help/articles/221769328-Locate-your-Slack-URL-or-ID) in the Slack help center.

1. Choose the type of **Service access** method that you want the Slack integration to use as authorization while accessing your service. You can **Create a new service role** or **Use an existing service role**. For more information, see [IAM role for allowing the integration to call Amazon Q Business on your end user's behalf](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/amazon-q-business-integrations-iam-allow-integration-access.html).

1. Choose the **Access management access** for the Slack integration to authorize to connect to IAM Identity center. For more information, see [IAM role for allowing Amazon Q Business to monitor the resources that the integration creates in your account](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/amazon-q-business-integrations-iam-allow-qbusiness-monitor.html).

1. Optionally, add any **Tags** that are relevant for this Slack integration.

1. Choose **Add integration**.

1. Once the integration has been successfully created, you will move to the **Integration details page**.

1. Choose **Deploy integration**.

1. Choose **Access Slack**.
**Note**  
This link will take you to the Slack domain outside of AWS.

1. You will continue this procedure within the Slack domain.

### Installing the Amazon Q Business App in your Slack workspace
<a name="slack-installing"></a>

The following instructions show how to install the Amazon Q Business App in your Slack workspace using a link from the Amazon Q console as shown in the previous topic.

**Note**  
Only a Slack workspace owner can use the link to install the Amazon Q App into your Slack workspace.
There can be only one instance of the Amazon Q App per Slack workspace. That instance will be connected to the application environment that integration was configured with in the previous topic.
You may see a "This app is not approved by Slack banner." This message can be ignored.

1. The link will open to a Slack login page where after you login (as admin) you will need to find and be asked to install the Amazon Q app within your Slack workspace.

1. Choose **Allow** to install your Amazon Q App for Slack.

1. Once the installation is complete, you will see the page confirming that the **Congratulations\! Your Slack App has been successfully installed.**

1. Choose **Open the Amazon Q Business App in Slack**.

1. This will open your Slack workspace where all users will be required to sign-in.

## Removing Slack as an integration
<a name="slack-removing"></a>

To remove the Slack integration, admin users can use the Amazon Q Business console.

**Note**  
This integration can only be removed using the AWS Management Console at this time.

### Using the console
<a name="slack-removing-console"></a>

1. Sign in to the Amazon Q console.

1. Choose **Applications**, then select the name of your application environment from the list.

1. Choose **Integrations** under **Enhancements**.

1. Find and select your Slack integration from the **Integrations** section on the main page.

1. Choose **Delete** and confirm your choice.

Once you disable your Slacks integration, your users will no longer be able to login. However you will still need to take steps to uninstall the Amazon Q Business App in your Slack Workspace.
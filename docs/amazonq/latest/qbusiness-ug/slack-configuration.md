# Configuring the Amazon Q Business Slack integration

for use

The Amazon Q Business integration for Slack is only available for use by Amazon Q Business Pro
users.

###### Note

- When Amazon Q is invoked by a user in a public Slack channel, it
  generates responses based on the invoking user's permissions, which may
  include content that other channel members aren't authorized to access.
  To prevent unintended exposure of sensitive information, carefully
  evaluate the use of Amazon Q in public channels.
- The Amazon Q Business customer integrating Slack must have a paid Slack
  workspace.
- Amazon Q only supports user access management through IAM Identity Center for Slack
  integrations. This includes authentication using external SAML providers
  through IAM Identity Center. To integrate Slack with Amazon Q, you must create an
  IAM Identity Center-integrated application. For more information, see [Create an IAM Identity Center-integrated
  application](create-application.md "create-application.md").
- Amazon Q doesn't support Slack integrations for [Amazon Q applications using IAM
  federation](create-application-iam.md "create-application-iam.md") for user access management.
- Access using the Amazon Q Business API is not supported at this time.
- Amazon Q Business does not use your user data for service improvement or for
  training its underlying large language models (LLMs). For more
  information, see [Amazon Q Business Service improvement](service-improvement.md "service-improvement.md").
- Uploading documents and conversations will follow the same behavior as
  the web experience. For more information, see the [Chat and file uploads](using-web-experience.md#upload-documents "using-web-experience.md#upload-documents") section in the Using web experience
  topic.

###### Topics

- [Prerequisites](#slack-configuration-prerequisites "#slack-configuration-prerequisites")
- [Adding an Amazon Q Business integration for
  Slack](#slack-adding "#slack-adding")
- [Removing Slack as an integration](#slack-removing "#slack-removing")

## Prerequisites

As admins, before you can add the Amazon Q Business integration to your Slack, you
must complete the following steps:

1. Must have a paid Slack workspace
2. [Get started
   with Amazon Q Business](getting-started.md "getting-started.md")
3. [Create an
   IAM Identity Center-integrated application environment](create-application.md "create-application.md") environment
   and create your Amazon Q Business web experience.

###### Note

Amazon Q doesn't support Slack integrations for [Amazon Q applications using IAM
federation](create-application-iam.md "create-application-iam.md") for user access management. 4. Optionally, to enhance your end users' experience with Amazon Q in
Slack, you can enable **Allow end users to send
queries directly to the LLM** in your Admin controls and
guardrails. For more information, see the [Response settings](guardrails-global-controls.md#guardrails-global-response "guardrails-global-controls.md#guardrails-global-response") topic in [Admin controls and
guardrails](guardrails.md "guardrails.md") and `chatMode` if you are configuring
programmatically. 5. Add the two IAM roles and trust policies for adding integrations.
For more information, see [IAM roles and trust policy for your
integrations](amazon-q-business-integrations-iam.md "amazon-q-business-integrations-iam.md") 6. Admin access to your Slack workspace. 7. Your Slack workspace ID. Your WorkSpace ID must start with a
_T_. One way to find your Slack workspace ID is
by navigating to your Slack workspace and starting a chat with the
_Slack Developer Tools_ app running the
`/sdt whoami` command. For more information, see [Locate your Slack URL or ID](https://slack.com/help/articles/221769328-Locate-your-Slack-URL-or-ID "https://slack.com/help/articles/221769328-Locate-your-Slack-URL-or-ID") in the Slack help
center.

## Adding an Amazon Q Business integration for

Slack

To use the Amazon Q Business Slack integration, you must allow it to connect to your
Amazon Q Business application environment and web experience. To do this, admins can use the
Amazon Q Business console, API, SDK, or AWS CLI.

###### Note

This integration can only be added using the AWS Management Console at this
time.

###### Topics

- [Using the console](#slack-adding-console "#slack-adding-console")
- [Installing the Amazon Q Business App in your
  Slack workspace](#slack-installing "#slack-installing")

### Using the console

1. Sign in to the Amazon Q console.
2. Choose **Applications**, then select the name of
   your application environment from the list.
3. Choose **Integrations** under
   **Enhancements**.
4. Choose **Add integration** from the
   **Integrations** section on the main
   page.
5. Choose **Slack** as your integration.
6. On the **Add Slack integration page**, enter the
   **Name** of your integration. This is the
   display name for the integration resource in AWS.
7. Add a **description** (optional).
8. Enter your Slack workspace ID. This is a unique identifier of
   your Slack workspace starting and can be found using the Slack
   developer tools app. To find your workspace ID:
   1. Navigate to your Slack workspace and in “Apps” search for
      “Slack Developer Tools”.
   2. Open the Slack Developer Tools app and run the command
      /sdt whoami
   3. You will receive a response that contains your Workspace
      ID starting with a “T”
   4. For other ways to locate your workspace ID, refer to
      [Locate your Slack URL or ID](https://slack.com/help/articles/221769328-Locate-your-Slack-URL-or-ID "https://slack.com/help/articles/221769328-Locate-your-Slack-URL-or-ID") in the Slack help
      center.

9. Choose the type of **Service access** method that
   you want the Slack integration to use as authorization while
   accessing your service. You can **Create a new service
   role** or **Use an existing service
   role**. For more information, see [IAM role for allowing the integration to call Amazon Q Business on
   your end user's behalf](amazon-q-business-integrations-iam-allow-integration-access.md "amazon-q-business-integrations-iam-allow-integration-access.md").
10. Choose the **Access management access** for the
    Slack integration to authorize to connect to IAM Identity center.
    For more information, see [IAM role for allowing Amazon Q Business to monitor the resources
    that the integration creates in your account](amazon-q-business-integrations-iam-allow-qbusiness-monitor.md "amazon-q-business-integrations-iam-allow-qbusiness-monitor.md").
11. Optionally, add any **Tags** that are relevant
    for this Slack integration.
12. Choose **Add integration**.
13. Once the integration has been successfully created, you will move
    to the **Integration details page**.
14. Choose **Deploy integration**.
15. Choose **Access Slack**.

###### Note

This link will take you to the Slack domain outside of
AWS. 16. You will continue this procedure within the Slack domain.

### Installing the Amazon Q Business App in your

Slack workspace

The following instructions show how to install the Amazon Q Business App in your
Slack workspace using a link from the Amazon Q console as shown in the
previous topic.

###### Note

- Only a Slack workspace owner can use the link to install the
  Amazon Q App into your Slack workspace.
- There can be only one instance of the Amazon Q App per Slack
  workspace. That instance will be connected to the application environment
  that integration was configured with in the previous
  topic.
- You may see a "This app is not approved by Slack banner." This
  message can be ignored.

1. The link will open to a Slack login page where after you login (as
   admin) you will need to find and be asked to install the Amazon Q app
   within your Slack workspace.
2. Choose **Allow** to install your Amazon Q App for
   Slack.
3. Once the installation is complete, you will see the page
   confirming that the **Congratulations! Your Slack App has
   been successfully installed.**
4. Choose **Open the Amazon Q Business App in
   Slack**.
5. This will open your Slack workspace where all users will be
   required to sign-in.

## Removing Slack as an integration

To remove the Slack integration, admin users can use the Amazon Q Business
console.

###### Note

This integration can only be removed using the AWS Management Console at this
time.

### Using the console

1. Sign in to the Amazon Q console.
2. Choose **Applications**, then select the name of
   your application environment from the list.
3. Choose **Integrations** under
   **Enhancements**.
4. Find and select your Slack integration from the
   **Integrations** section on the main
   page.
5. Choose **Delete** and confirm your choice.

Once you disable your Slacks integration, your users will no longer be
able to login. However you will still need to take steps to uninstall the
Amazon Q Business App in your Slack Workspace.

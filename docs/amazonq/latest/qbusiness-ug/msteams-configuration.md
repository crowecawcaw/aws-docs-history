# Configuring the Amazon Q Business Microsoft Teams

(Teams) integration for use

###### Note

- When Amazon Q is invoked by a user in a public Teams channel, it
  generates responses based on the invoking user's permissions, which may
  include content that other channel members aren't authorized to access.
  To prevent unintended exposure of sensitive information, carefully
  evaluate the use of Amazon Q in public channels.
- The Amazon Q Business customer integrating Microsoft Teams (Teams) must have
  a paid Teams organization.
- Amazon Q supports users who authenticate using external SAML providers
  through IAM Identity Center. For more information, see [Create an IAM Identity Center-integrated
  application](create-application.md "create-application.md").
- Amazon Q application environment created with IAM Federation do not support
  integrations with Teams at this time.
- Access using the Amazon Q Business API is not supported at this time.
- Amazon Q Business does not use your user data for service improvement or for
  training its underlying large language models (LLMs). For more
  information, see [Amazon Q Business Service improvement](service-improvement.md "service-improvement.md").
- Uploading documents and conversations will follow the same behavior as
  the web experience. For more information, see the [Chat and file uploads](using-web-experience.md#upload-documents "using-web-experience.md#upload-documents") section in the Using web experience
  topic.

###### Topics

- [Prerequisites](#msteams-configuration-prerequisites "#msteams-configuration-prerequisites")
- [Adding an Amazon Q Business integration for Microsoft
  Teams](#msteams-adding "#msteams-adding")
- [Removing Microsoft Teams as an
  integration](#msteams-removing "#msteams-removing")

## Prerequisites

As admins, before you can add the Amazon Q Business integration to your Microsoft
Teams (Teams), you must complete the following steps:

1. You must have a Microsoft 365 Business subscription and be a
   _Global Admin_ or someone with administrative
   permissions, specifically `AppCatalog.ReadWrite.All`.
2. [Get started
   with Amazon Q Business](getting-started.md "getting-started.md")
3. [Create an
   IAM Identity Center-integrated application environment](create-application.md "create-application.md") environment
   and create your Amazon Q Business web experience.

###### Note

[IAM federated application environment](create-application-iam.md "create-application-iam.md") environments do not
support integrations with Teams. 4. Optionally, to enhance your end users' experience with Amazon Q in
Teams, you can enable _Allow end users to send queries directly
to the LLM_ in your Admin controls and guardrails. For
more information, see the [Response settings](guardrails-global-controls.md#guardrails-global-response "guardrails-global-controls.md#guardrails-global-response") topic in [Admin controls and
guardrails](guardrails.md "guardrails.md") and `chatMode` if you are configuring
programmatically. 5. Add the two IAM roles and trust policies for adding integrations.
For more information, see [IAM roles and trust policy for your integrations](amazon-q-business-integrations-iam.md "amazon-q-business-integrations-iam.md") 6. Your Microsoft 365 tenant ID. For more information, see [How to find your tenant ID - Microsoft Entra](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant "https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant") in the
Microsoft Learn portal.

## Adding an Amazon Q Business integration for Microsoft

Teams

To use the Amazon Q Business Teams integration, you must allow it to connect to your
Amazon Q Business application environment and web experience. To do this, admins can use the
Amazon Q Business console, API, SDK, or AWS CLI.

###### Note

This integration can only be added using the AWS Management Console at this
time.

###### Topics

- [Using the console](#msteams-adding-console "#msteams-adding-console")
- [Installing the Amazon Q Business app in your
  Microsoft Teams organization](#msteams-installing "#msteams-installing")

### Using the console

1. Sign in to the Amazon Q console.
2. Choose **Applications**, then select the name of
   your application environment from the list.
3. Choose **Integrations** under
   **Enhancements**.
4. Choose **Add integration** from the
   **Integrations** section on the main
   page.
5. Choose **Microsoft Teams** as your
   integration.
6. On the **Add Teams integration page**, enter the
   **Name** of your integration. This is the
   display name for the integration resource in AWS.
7. Add a **description** (optional).
8. Enter your **Teams Tenant ID**. This can be found
   in the _Microsoft Entra Admin Center_. For more
   information, see [How to find your tenant ID - Microsoft Entra](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant "https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant")
9. Choose the type of **Service access** method that
   you want the Teams integration to use as authorization while
   accessing your service. You can **Create a new service
   role** or **Use an existing service
   role**. For more information, see [IAM role for allowing the integration to
   call Amazon Q Business on your end user's behalf](amazon-q-business-integrations-iam-allow-integration-access.md "amazon-q-business-integrations-iam-allow-integration-access.md").
10. Choose the **Access management access** for the
    Teams integration to authorize to connect to IAM Identity center.
    For more information, see [IAM role for allowing Amazon Q Business to monitor the resources
    that the integration creates in your account](amazon-q-business-integrations-iam-allow-qbusiness-monitor.md "amazon-q-business-integrations-iam-allow-qbusiness-monitor.md").
11. Optionally, add any **Tags** that are relevant
    for this Teams integration.
12. Choose **Add integration**.
13. Once the integration has been successfully created, you will move
    to the **Integration details page**.
14. Choose **Deploy integration**.
15. Choose **Access Teams**.

###### Note

This link will take you to the Teams domain outside of
AWS. 16. You will continue this procedure within the Teams domain.

### Installing the Amazon Q Business app in your

Microsoft Teams organization

The following instructions show how to install the Amazon Q Business App in your
Microsoft Teams (Teams) workspace using a link from the Amazon Q console as
shown in the previous topic.

###### Note

- Only a Teams _Global Admin_ or someone with
  administrative permissions can add the Amazon Q Business App to your
  Teams organization, specifically
  `AppCatalog.ReadWrite.All`.
- There can be only one instance of the Amazon Q App per Teams
  organization. That instance will be connected to the
  application environment that the Teams integration was configured with in
  the previous topic.

1. Open the link and login as Global Admin or or someone with
   administrative permissions can add the Amazon Q Business App to the
   Microsoft Teams admin center for your organization.
2. Choose **Teams apps** in the left
   navigation.
3. Choose **Amazon Q Business** from the list of available
   apps.
4. Review and grant admin consent by choosing the
   **Permissions** tab and reviewing the
   permissions and choose **Grant admin
   consent**.

###### Note

If permissions are already granted, proceed to the end of the
procedure, there is no further action required. 5. Authenticate and choose **Accept** for Amazon Q Business
app. 6. Confirm that an app titled **Amazon Q Business
Permissions** tab now says **Admin consent
granted for all required permissions**.

All users assigned to the app from the **Teams admin
center** can now find the app in the **Built for your
org** section of the **Apps** page of their
Teams app.

## Removing Microsoft Teams as an

integration

To remove the Microsoft Teams (Teams) integration, admin users can use the
Amazon Q Business console.

###### Note

This integration can only be removed using the AWS Management Console at this
time.

### Using the console

1. Sign in to the Amazon Q console.
2. Choose **Applications**, then select the name of
   your application environment from the list.
3. Choose **Integrations** under
   **Enhancements**.
4. Find and select your Teams integration from the
   **Integrations** section on the main
   page.
5. Choose **Delete** and confirm your choice.

Once you disable your Microsoft Teams (Teams) integration, your users will
no longer be able to login. However you will still need to take steps to
uninstall the Amazon Q Business App in your Teams organization.

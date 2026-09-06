

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Making authenticated Amazon Q Business API calls using IAM federation
<a name="making-sigv4-authenticated-api-calls-iam"></a>

Amazon Q Business can securely handle data with integrated authentication and authorization. During data ingestion, Amazon Q Business preserves the authorization information—access control lists (ACLs)—from the data source so users can only request answers from the data they already have access to. Through IAM Federation, Amazon Q Business uses [trusted identity propagation](https://docs.aws.amazon.com/singlesignon/latest/userguide/using-apps-with-trusted-token-issuer.html) to ensure that an end user is authenticated and receives fine-grained authorization to their user ID and group-based resources.

In order to achieve this, a subset of the Amazon Q Business APIs ([Chat](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Chat.html), [ChatSync](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ChatSync.html), [SearchRelevantContent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_SearchRelevantContent.html), [ListConversations](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListConversations.html), [ListMessages](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListMessages.html), [DeleteConversation](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteConversation.html), [PutFeedback](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PutFeedback.html)) require identity-aware [AWS Sig V4 credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/signing-elements.html) for the authenticated user on whose behalf the API call is being made.

This page provides an overview of the workflows needed to obtain AWS Sig V4 credentials for a user authenticated using an identity provider (IdP), such as Okta. While we use Okta as an example, the same principles and steps apply to any other identity provider synced with your IAM instance.

**Important**  
Amazon Q Business doesn't support OIDC for Google and Microsoft Entra ID.

**Note**  
Federated groups aren't supported through IAM Federation. If you want to ingest federated groups, use the [PutGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PutGroup.html) API.

**Topics**
+ [Prerequisites](#sigv4-auth-api-calls-prereqs-iam)
+ [One-time setup](#control-plane-setup-iam)
+ [Workflow for each API call session for authenticated user](#data-plane-workflow-iam)

## Prerequisites
<a name="sigv4-auth-api-calls-prereqs-iam"></a>

Before you begin setting up for making Sig V4 authenticated API calls, make sure you've done the following:
+ [Created an Amazon Q Business application](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateApplication.html).
+ Created an Okta IdP instance and configured users and groups within it. While we use Okta as an example, the same principles and steps apply to any other identity provider connected to your IAM instance.
+ Created an IAM instance for your Amazon Q Business application and connected Okta as your identity source.
+ Configured access to the AWS CLI.

## One-time setup
<a name="control-plane-setup-iam"></a>

The following section outlines the steps to set up the Amazon Q Business control plane. You only need to perform these steps once.

1. Create an [OIDC app integration](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm) in Okta.

1. Create the IAM identity provider using the following command:

   ```
   aws iam \
   create-open-id-connect-provider \
   --url {{issuer-url}}
   ```

   Then, copy the `OpenIDConnectProviderArn` from the output.

1. Next, create the IAM role. To do so, perform the following steps:

   1. Create a directory named `policies`.

   1. In that directory, create and save a file named `trustpolicyforfederation.json` with the following JSON included:

1. Next, create the IAM policy for your web experience. To do so, perform the following steps:

   1. In the `policies` directory, create and save a new file named `permspolicyforfederation.json` with the following JSON included:

1. Finally, create and attach the roles in IAM using the following command:

   ```
   aws iam \
   create-role \
   --role-name 
   --assume-role-policy-document {{file://policies/trustpolicyforfederation.json}} \
   --policy-document {{file://policies/permspolicyforfederation.json}}
   ```

## Workflow for each API call session for authenticated user
<a name="data-plane-workflow-iam"></a>

1. First, use the `IdToken` from Okta to call the [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) API to get AWS credentials. To do so, use the following command:

   ```
   aws sts
   assume-role-with-web-identity
   --role-arn {{role arn}}
   --role-session-name {{session-name}}
   --web-identity-token {{id-token-from-okta}}
   ```

1. Then, set the following environment variables in your command line environment using the credentials you received as a response from the [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) API call.

   ```
   AWS_ACCESS_KEY_ID="{{identity-aware-sigv4-access-key}}"
   AWS_SECRET_ACCESS_KEY="{{identity-aware-sigv4-secret-key}}"
   AWS_SESSION_TOKEN="{{identity-aware-sigv4-session-token}}"
   ```

1. Then, make Amazon Q Business API calls using the following command:

   ```
   aws qbusiness \
   chat-sync \
   --application-id {{application-id}}
   --user-message {{sample-chat-request}}
   ```
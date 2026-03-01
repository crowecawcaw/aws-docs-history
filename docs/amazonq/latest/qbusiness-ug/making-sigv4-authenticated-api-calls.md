# Making authenticated Amazon Q Business API calls using IAM Identity Center

###### Important

**This documentation is for developers building custom
applications that integrate with Amazon Q Business APIs.** These
instructions help you create a trusted backend component in your custom application
that can make authenticated API calls on behalf of your users. This is NOT for the
built-in Amazon Q Business web experience — that handles authentication
automatically through the AWS console.

Amazon Q Business can securely handle data with integrated authentication and
authorization. During data ingestion, Amazon Q Business preserves the
authorization information—access control lists (ACLs)—from the data source
so users can only request answers from the data they already have access to. Through
IAM Identity Center, Amazon Q Business uses [trusted identity propagation](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md") to ensure that an end user
is authenticated and receives fine-grained authorization to their user ID and
group-based resources.

In order to achieve this, a subset of the Amazon Q Business APIs ([Chat](../api-reference/API_Chat.md "../api-reference/API_Chat.md"),
[ChatSync](../api-reference/API_ChatSync.md "../api-reference/API_ChatSync.md"), [SearchRelevantContent](../api-reference/API_SearchRelevantContent.md "../api-reference/API_SearchRelevantContent.md"), [ListConversations](../api-reference/API_ListConversations.md "../api-reference/API_ListConversations.md"), [ListMessages](../api-reference/API_ListMessages.md "../api-reference/API_ListMessages.md"), [DeleteConversation](../api-reference/API_DeleteConversation.md "../api-reference/API_DeleteConversation.md"), [PutFeedback](../api-reference/API_PutFeedback.md "../api-reference/API_PutFeedback.md")) require identity-aware [AWS Sig V4
credentials](../../../IAM/latest/UserGuide/signing-elements.md "../../../IAM/latest/UserGuide/signing-elements.md") for the authenticated user on whose behalf the API call is being
made.

###### Note

This page provides an overview of the workflows needed to obtain AWS Sig V4
credentials for a user authenticated using an OIDC-compliant external identity
provider (IdP), such as Okta. While we use Okta as an
example, the same principles and steps apply to any other identity provider synced
with your IAM Identity Center instance.

## Architecture overview

The following diagram shows how your custom application components interact with
AWS services to make authenticated API calls:

![Sequence diagram showing a 12-step authentication flow for Amazon Q Business custom applications. The flow shows an end user accessing a custom app frontend, which requests Amazon Q Business data from the trusted backend. The backend exchanges tokens with an external IdP, IAM Identity Center, and AWS STS to obtain SigV4 credentials for authenticated API calls to Amazon Q Business APIs.](images/qbusiness-sigv4-authentication-flow.png)

**Key components:**

- **Custom app frontend**: Your user-facing
  application (web, mobile, etc.)
- **Custom app trusted backend**: Your
  server-side component that handles AWS API calls
- **External IdP**: Your identity provider
  (Okta, Azure AD, etc.)
- **IAM Identity Center**: AWS service that manages
  identity federation
- **Amazon Q Business APIs**: The APIs
  your application calls (`Chat`,
  `SearchRelevantContent`, etc.)

###### Note

Your custom application's backend component must implement this authentication
flow. End users interact with your frontend, which communicates with your
trusted backend to make Amazon Q Business API calls.

###### Topics

- [Prerequisites](#sigv4-auth-api-calls-prereqs "#sigv4-auth-api-calls-prereqs")
- [One-time setup](#control-plane-setup "#control-plane-setup")
- [Workflow for custom application backend API calls for an authenticated user](#data-plane-workflow "#data-plane-workflow")

## Prerequisites

Before you begin setting up for making Sig V4 authenticated API calls, make sure
you've done the following:

- [Created an Amazon Q Business
  application](create-application.md "create-application.md").
- Created an Okta IdP instance and configured users and
  groups within it. While we use Okta as an example, the same
  principles and steps apply to any other OIDC-compliant external identity
  provider synced with your IAM Identity Center instance.
- Created an IAM Identity Center instance for your Amazon Q Business application
  that uses Okta as your as the identity source.
- [Synchronized the users and groups from
  Okta](../../../singlesignon/latest/userguide/gs-okta.md#gs-ok-step4 "../../../singlesignon/latest/userguide/gs-okta.md#gs-ok-step4") with IAM Identity Center.
- Configured access to the [AWS CLI](../../../cli/latest/userguide/getting-started-quickstart.md "../../../cli/latest/userguide/getting-started-quickstart.md").

## One-time setup

The following section outlines the steps to set up the Amazon Q Business
control plane. You only need to perform these steps once.

1. Create an [OIDC app integration](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm "https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm") in Okta.
2. Then, in the IAM Identity Center instance you have created, create a [Trusted Token Issuer to trust IdP issuer with the issuer URL](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-trusted-token-issuer.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-trusted-token-issuer.html").
   For example,
   `https://<your-okta-instance>.okta.com/oauth2/default`.
3. In your IAM Identity Center instance, create a [customer managed custom application](../../../cli/latest/reference/sso-admin/create-application.md "../../../cli/latest/reference/sso-admin/create-application.md") using
   the following AWS CLI command:

```

aws sso-admin create-application \
--application-provider-arn arn:aws:sso::aws:applicationProvider/custom \
--instance-arn `your-identity-center-arn` \
--name `your-custom-application-name`

```

4. Then, [disable user assignment or provide explicit user
   assignments to the custom application](../../../cli/latest/reference/sso-admin/put-application-assignment-configuration.md "../../../cli/latest/reference/sso-admin/put-application-assignment-configuration.md") you created using the
   following AWS CLI command:

```

aws sso-admin put-application-assignment-configuration \
--application-arn `your-custom-application-arn` \
--no-assignment-required

```

5. Then, add a JWT bearer grant to your application environment using the [put application environment grant](../../../cli/latest/reference/sso-admin/put-application-grant.md "../../../cli/latest/reference/sso-admin/put-application-grant.md") CLI command. For
   example:

```

aws sso-admin put-application-grant \
--cli-input-json '{
   "ApplicationArn":"`identity-center-custom-application-arn`",
   "Grant":{
      "JwtBearer":{
         "AuthorizedTokenIssuers":[
            {
               "AuthorizedAudiences":[
                  "`idp-authorized-audience`"
               ],
               "TrustedTokenIssuerArn":"`trusted-token-issuer-arn`"
            }
         ]
      }
   },
   "GrantType":"urn:ietf:params:oauth:grant-type:jwt-bearer"
}'

```

6. You will then need to add an authentication method for a Amazon Q Business application environment using the [put application environment authentication method](../../../cli/latest/reference/sso-admin/put-application-authentication-method.md "../../../cli/latest/reference/sso-admin/put-application-authentication-method.md")
   AWS CLI command:

```

aws sso-admin put-application-authentication-method \
--cli-input-json '{
    "ApplicationArn": "`identity-center-custom-application-arn`",
    "AuthenticationMethod": {
        "Iam": {
            "ActorPolicy": {
                "Version": "2012-10-17",
                "Statement": [{
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "`your-aws-account-id`",
                        "Service": "qbusiness.amazonaws.com"
                    },
                    "Action": [
                        "sso-oauth:CreateTokenWithIAM"
                    ],
                    "Resource": "`your-identity-center-custom-application-arn`",
                    "Condition": {
                        "ArnEquals": {
                            "aws:SourceArn": "arn:${ArnPartition}:${Service}:${Region}:${AppAccountId}:${Resource}"
                        },
                        "StringEquals": {
                            "aws:SourceAccount": "${AppAccountId}"
                        }
                    }
                }]
            }
        }
    },
    "AuthenticationMethodType": "IAM"
}'
```

7. Next, add a list of authorized targets for an IAM Identity Center access scope for an
   Amazon Q Business application environment using the following [put application environment access scope](../../../cli/latest/reference/sso-admin/put-application-authentication-method.md "../../../cli/latest/reference/sso-admin/put-application-authentication-method.md") AWS CLI
   command:

```
aws sso-admin put-application-access-scope \
--application-arn `identity-center-custom-application-arn` \
--scope "qbusiness:conversations:access"
```

8. Then, create an IAM role that your application environment will use to call [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") API with the following policies:

**Trust policy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "QCLITrustPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "qbusiness.amazonaws.com"
 ]
 },
 "Action": [
 "sts:AssumeRole",
 "sts:SetContext"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "111122223333"
 }
 }
 }]
}`

```

**Permissions policy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessConversationPermission",
 "Effect": "Allow",
 "Action": [
 "qbusiness:Chat",
 "qbusiness:ChatSync",
 "qbusiness:ListMessages",
 "qbusiness:ListConversations",
 "qbusiness:DeleteConversation",
 "qbusiness:PutFeedback",
 "qbusiness:GetWebExperience",
 "qbusiness:GetApplication",
 "qbusiness:ListPlugins",
 "qbusiness:GetChatControlsConfiguration",
 "qbusiness:GetMedia"
 ],
 "Resource": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 },
 {
 "Sid": "QBusinessKMSDecryptPermissions",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:111122223333:key/`key-id`"
 ]
 },
 {
 "Sid": "QBusinessSetContextPermissions",
 "Effect": "Allow",
 "Action": "sts:SetContext",
 "Resource": "arn:aws:sts:*:111122223333:assumed-role/`role-name`/`session-name`"
 }
 ]
}`

```

9. Then, get the list of synced users and groups in your IAM Identity Center-integrated
   Amazon Q Business application using the following AWS CLI
   command:

```

aws sso-admin list-application-assignments \
--application-arn `your-custom-application-arn`
```

10. Finally, add a subscription for each user or group in your
    IAM Identity Center-integrated Amazon Q Business application using the following
    AWS CLI commands:

**To provision a user subscription**

```

aws qbusiness create-subscription \
--application-id `application-id` \
--principal user=`idc-user-id` \
--type `subscription-type`
```

**To provision a group subscription**

```

aws qbusiness create-subscription \
--application-id `application-id` \
--principal group=`idc-group-id` \
--type `subscription-type`

```

## Workflow for custom application backend API calls for an authenticated user

After you've completed the [one-time setup](making-sigv4-authenticated-api-calls.md#control-plane-setup "making-sigv4-authenticated-api-calls.md#control-plane-setup") tasks, you can use one of two
workflows to generate identity-aware credentials to make API calls for your
IAM Identity Center-integrated Amazon Q Business application:

- the AWS SDK trusted identity propagation plugin (TIP\_ workflow
  (recommended), or a longer API workflow.
- The API workflow requires a manual token exchange with IAM Identity Center and uses
  AWS STS to generate identity-aware credentials for your Amazon Q Business application.

The AWS SDK TIP plugin workflow streamlines the authorization process by
eliminating the need for manual token exchange and credential generation. Once set
up, it automatically handles token exchange and credential management.

The TIP plugin workflow is the recommended approach for implementing
identity-aware authorization. It is currently supported by the Java and JavaScript
SDK. For more information, see [Trusted identity propagation (TIP) plugin](../../../sdkref/latest/guide/access-tip.md "../../../sdkref/latest/guide/access-tip.md") in the
_AWS SDKs and Tools Reference Guide_.

Use the Java or JavaScript SDK to create the plugin and make calls to
Amazon Q Business using the following:

- `webTokenProvider` – A function that
  the customer implements to obtain an OpenID token from their
  external identity provider.
- `accessRoleArn` – The IAM role ARN
  to be assumed by the plugin with the user's identity context to get
  the identity-enhanced credentials.
- `applicationArn` – The unique
  identifier string for the client or application. This value is an
  application ARN that has OAuth grants
  configured.
- `applicationRoleArn` – The IAM role
  ARN to be assumed with `AssumeRoleWithWebIdentity` so that the OIDC
  and AWS STS clients can be bootstrapped. If
  `applicationRoleArn` is not provided, it is
  mandatory to provide both `ssoOidcClient` and
  `stsClient` parameters.
- `ssoOidcClient` – An IAM Identity Center OIDC
  client, such as `SsoOidcClient` for Java or
  `client-sso-oidc` for Javascript, with
  customer-defined configurations. If not provided, an OIDC client
  using `applicationRoleArn` will be instantiated
  and used.
- `stsClient` – An AWS STS client with
  customer-defined configurations, used to assume
  `accessRoleArn` with the user's identity
  context. If not provided, an AWS STS client using
  `applicationRoleArn` will be instantiated
  and used.
  If both `ssoOidcClient` and
  `stsClient`, and
  `applicationRoleArn` are provided, the former is
  prioritized.

```
// Option-1: Build and pass OIDC and STS clients
SsoOidcClient oidcClient = SsoOidcClient.builder()
    .region(Region.US_EAST_1)
    .credentialsProvider(credentialsProvider).build();

StsClient stsClient = StsClient.builder()
    .region(Region.US_EAST_1)
    .credentialsProvider(credentialsProvider).build();

TrustedIdentityPropagationPlugin trustedIdentityPropagationPlugin = TrustedIdentityPropagationPlugin.builder()
        .webTokenProvider(() -> webToken)
        .applicationArn(idcApplicationArn)
        .accessRoleArn(accessRoleArn)
        .ssoOidcClient(client)
        .stsClient(stsClient)
        .build();

// Option-2: Pass applicationRoleArn and defer the STS & OIDC clients creation to the plugin
TrustedIdentityPropagationPlugin trustedIdentityPropagationPlugin = TrustedIdentityPropagationPlugin.builder()
        .webTokenProvider(() -> webToken)
        .applicationArn(idcApplicationArn)
        .accessRoleArn(accessRoleArn)
        .applicationRoleArn(applicationRoleArn)
        .build();

QBusinessClient qBusinessClient = QBusinessClient.builder()
        .region(Region.US_EAST_1)
        .addPlugin(trustedIdentityPropagationPlugin)
        .build();

// Create ChatSyncRequest
ChatSyncRequest chatSyncRequest = ChatSyncRequest.builder()
        .applicationId(applicationId)
        .userMessage(userMessage)
        // You can add conversationId, attachments, chatMode, etc. here
        .build();

// Call chatSync operation
ChatSyncResponse chatSyncResponse = qBusinessClient.chatSync(chatSyncRequest);
```

1. First, use the [CreateTokenWithIAM](../../../singlesignon/latest/OIDCAPIReference/API_CreateTokenWithIAM.md "../../../singlesignon/latest/OIDCAPIReference/API_CreateTokenWithIAM.md") API call to
   obtain an IAM Identity Center-provided JWT bearer grant token using your:
   - `**clientID**`: Your IAM Identity Center
     custom application environment ARN.
   - `**grantType**`: For example,
     `'urn:ietf:params:oauth:grant-type:jwt-bearer'`.
   - `**assertion**`: The user
     authenticated ID token obtained from
     Okta.

2. Then, use the [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") API call to obtain user
   decorated AWS Sig V4 credentials using your:
   - `**RoleArn**`: The IAM role
     ARN.
   - `**RoleSessionName**`: A
     unique session name.
   - `**DurationSeconds**`: The
     session duration in seconds.
   - `**ProvidedContexts**`: A list
     of previously acquired trusted context assertions in the
     format of a JSON array. The trusted context assertion is
     signed and encrypted by AWS STS. For example:

   ```
   [{
       'ProviderArn': "arn:aws:iam::aws:contextProvider/IdentityCenter",
       'ContextAssertion': claims["sts:identity_context"]
   }]
   ```

   ###### Note

   The `ContextAssertion` uses the
   “sts:identity_context” object from the claims object of
   the decoded JWT bearer grant token obtained as part of
   Step 1 in this procedure.

3. Use the identity-aware AWS Sig V4 credentials in the previous
   step to initialize the AWS SDK client and then make Amazon Q Business API calls using that client.

First, set the following environment variables in your command
line environment:

```
AWS_ACCESS_KEY_ID="`identity-aware-sigv4-access-key`"
AWS_SECRET_ACCESS_KEY="`identity-aware-sigv4-secret-key`"
AWS_SESSION_TOKEN="`identity-aware-sigv4-session-token`"
```

Then, run the following Python script from the same
window:

```
import boto3
import json
import random

import boto3

aq_client = boto3.client(
    "qbusiness",
    region_name="your-aws-region"
)

resp = aq_client.chat_sync(
    applicationId = "amazon-qbusiness-application-id",
    userMessage = "chat-request",
    clientToken = str(random.randint(0,10000)
)

print(f"Amazon Q Business response: {resp["systemMessage"]}")
```

###### Important

As a security best practice, the credentials should not be
hard coded in your scripts or code. For more information, refer
to [Boto 3 documentation on using credentials](https://boto3.amazonaws.com/v1/documentation/api/1.9.156/guide/configuration.html "https://boto3.amazonaws.com/v1/documentation/api/1.9.156/guide/configuration.html").

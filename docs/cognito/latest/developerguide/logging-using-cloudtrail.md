# Amazon Cognito logging in AWS CloudTrail

Amazon Cognito is integrated with AWS CloudTrail, a service that provides a record of actions taken by a
user, role, or an AWS service in Amazon Cognito. CloudTrail captures a subset of API calls for Amazon Cognito as
events, including calls from the Amazon Cognito console and from code calls to the Amazon Cognito API
operations. If you create a trail, you can choose to deliver CloudTrail events to an Amazon S3 bucket,
including events for Amazon Cognito. If you don't configure a trail, you can still view the most recent
events in the CloudTrail console in **Event history**. Using the information
collected by CloudTrail, you can determine the request that was made to Amazon Cognito, the IP address from
which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, including how to configure and activate it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

You can also create Amazon CloudWatch alarms for specific CloudTrail events. For example, you can set up
CloudWatch to trigger an alarm if an identity pool configuration is changed. For more information,
see [Creating CloudWatch alarms for
CloudTrail events: Examples](../../../awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.md").

###### Topics

- [Information that Amazon Cognito sends to
  CloudTrail](#amazon-cognito-info-in-cloudtrail "#amazon-cognito-info-in-cloudtrail")
- [Analyzing Amazon Cognito CloudTrail events with Amazon CloudWatch Logs
  Insights](#analyzingcteventscwinsight "#analyzingcteventscwinsight")
- [Example Amazon Cognito events](understanding-amazon-cognito-entries.md "understanding-amazon-cognito-entries.md")

## Information that Amazon Cognito sends to

CloudTrail

CloudTrail is turned on when you create your AWS account. When supported event activity
occurs in Amazon Cognito, that activity is recorded in a CloudTrail event along with other AWS service
events in **Event history**. You can view, search, and download recent
events in your AWS account. For more information, see [Viewing events with CloudTrail event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Amazon Cognito,
create a trail. A CloudTrail trail delivers log files to an Amazon S3 bucket. By default, when you
create a trail in the console, the trail applies to all Regions. The trail logs events from
all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you
specify. Additionally, you can configure other AWS services to further analyze and act
upon the event data collected in CloudTrail logs. For more information, see:

- [Overview for
  creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-list "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-list")
- [Configuring amazon
  SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail
  log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or IAM user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

###### Confidential data in AWS CloudTrail

Because user pools and identity pools process user data, Amazon Cognito obscures some private
fields in your CloudTrail events with the value `HIDDEN_DUE_TO_SECURITY_REASONS`. For
examples of fields that Amazon Cognito doesn't populate to events, see [Example Amazon Cognito events](understanding-amazon-cognito-entries.md "understanding-amazon-cognito-entries.md"). Amazon Cognito only obscures some fields that
commonly contain user information, like passwords and tokens. Amazon Cognito doesn't perform any
automatic detection or masking of personally-identifying information that you populate to
non-private fields in your API requests.

### User pool events

Amazon Cognito supports logging for all of the actions listed on the [User pool actions](../../../cognito-user-identity-pools/latest/APIReference/API_Operations.md "../../../cognito-user-identity-pools/latest/APIReference/API_Operations.md") page as events in CloudTrail log files. Amazon Cognito logs user pool events
to CloudTrail as _management events_.

The `eventType` field in a Amazon Cognito user pools CloudTrail entry tells you whether your app
made the request to the [Amazon Cognito user pools API](../../../cognito-user-identity-pools/latest/APIReference/Welcome.md "../../../cognito-user-identity-pools/latest/APIReference/Welcome.md")
or to an [endpoint that serves
resources for OpenID Connect, SAML 2.0, or managed login pages](cognito-userpools-server-contract-reference.md "cognito-userpools-server-contract-reference.md"). API requests have
an `eventType` of `AwsApiCall` and endpoint requests have an
`eventType` of `AwsServiceEvent`.

Amazon Cognito logs the following requests to your managed login services as events in
CloudTrail.

Hosted UI (classic) events

| Hosted UI (classic) events in CloudTrail                     | Operation                                                                                                                                                                                                                                               | Description |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `Login_GET`, `CognitoAuthentication`                         | A user views or submits credentials to your [Login endpoint](login-endpoint.md "login-endpoint.md").                                                                                                                                                    |
| `OAuth2_Authorize_GET`,<br>`Beta_Authorize_GET`              | A user views your [Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md").                                                                                                                                                          |
| `OAuth2Response_GET`,<br>`OAuth2Response_POST`               | A user submits an IdP token to your `/oauth2/idpresponse`<br>endpoint.                                                                                                                                                                                  |
| `SAML2Response_POST`,<br>`Beta_SAML2Response_POST`           | A user submits an IdP SAML assertion to your<br>`/saml2/idpresponse` endpoint.                                                                                                                                                                          |
| `Login_OIDC_SAML_POST`                                       | A user enters a username at your [Login endpoint](login-endpoint.md "login-endpoint.md") and matches with an [IdP identifier](cognito-user-pools-integrating-3rd-party-saml-providers.md "cognito-user-pools-integrating-3rd-party-saml-providers.md"). |
| `Token_POST`, `Beta_Token_POST`                              | A user submits an authorization code to your [Token endpoint](token-endpoint.md "token-endpoint.md").                                                                                                                                                   |
| `Signup_GET`, `Signup_POST`                                  | A user submits sign-up information to your `/signup`<br>endpoint.                                                                                                                                                                                       |
| `Confirm_GET`, `Confirm_POST`                                | A user submits a confirmation code in the hosted UI.                                                                                                                                                                                                    |
| `ResendCode_POST`                                            | A user submits a request to resend a confirmation code in the hosted<br>UI.                                                                                                                                                                             |
| `ForgotPassword_GET`,<br>`ForgotPassword_POST`               | A user submits a request to reset their password to your<br>`/forgotPassword` endpoint.                                                                                                                                                                 |
| `ConfirmForgotPassword_GET`,<br>`ConfirmForgotPassword_POST` | A user submits a code to your `/confirmForgotPassword`<br>endpoint that confirms their `ForgotPassword` request.                                                                                                                                        |
| `ResetPassword_GET`, `ResetPassword_POST`                    | A user submits a new password in the hosted UI.                                                                                                                                                                                                         |
| `Mfa_GET`, `Mfa_POST`                                        | A user submits a multi-factor authentication (MFA) code in the hosted<br>UI.                                                                                                                                                                            |
| `MfaOption_GET`, `MfaOption_POST`                            | A user chooses their preferred method for MFA in the hosted UI.                                                                                                                                                                                         |
| `MfaRegister_GET`, `MfaRegister_POST`                        | A user submits a multi-factor authentication (MFA) code in the hosted<br>UI when registering the MFA.                                                                                                                                                   |
| `Logout`                                                     | A user signs out at your `/logout` endpoint.                                                                                                                                                                                                            |
| `SAML2Logout_POST`                                           | A user signs out at your `/saml2/logout` endpoint.                                                                                                                                                                                                      |
| `Error_GET`                                                  | A user views an error page in the hosted UI.                                                                                                                                                                                                            |
| `UserInfo_GET`, `UserInfo_POST`                              | A user or IdP exchanges information with your [userInfo endpoint](userinfo-endpoint.md "userinfo-endpoint.md").                                                                                                                                         |
| `Confirm_With_Link_GET`                                      | A user submits a confirmation based on a link that Amazon Cognito sent in an<br>email message.                                                                                                                                                          |
| `Event_Feedback_GET`                                         | A user submits feedback to Amazon Cognito about a [threat<br>protection](cognito-user-pool-settings-threat-protection.md "cognito-user-pool-settings-threat-protection.md") event.                                                                      |

Managed login events

| Managed login events in CloudTrail | Operation                                                                                                                                     | Description |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `login_POST`                       | A user submits credentials to your [Login endpoint](login-endpoint.md "login-endpoint.md").                                                   |
| `login_continue_POST`              | A user who has already signed in one time chooses to sign in<br>again.                                                                        |
| `forgotPassword_POST`              | A user resets their password.                                                                                                                 |
| `selectChallenge_POST`             | A user responds to an authentication challenge after they submit their<br>username or credentials.                                            |
| `confirmUser_GET`                  | A user opens the link in a [confirmation or verification email message](signing-up-users-in-your-app.md "signing-up-users-in-your-app.md").   |
| `mfa_back_POST`                    | A user chooses the \*_Back_<br>• button after an MFA<br>prompt.                                                                               |
| `mfa_options_POST`                 | A user selects an MFA option.                                                                                                                 |
| `mfa_phone_register_POST`          | A user submits a phone number to register as a MFA factor. This<br>operation causes Amazon Cognito to send an MFA code to their phone number. |
| `mfa_phone_verify_POST`            | A user submits an MFA code sent to their phone number.                                                                                        |
| `mfa_phone_resendCode_POST`        | A user submits a request to resend a MFA code to their phone<br>number.                                                                       |
| `mfa_totp_POST`                    | A user submits a TOTP MFA code.                                                                                                               |
| `signup_POST`                      | A user submits information to your `/signup` managed login<br>page.                                                                           |
| `signup_confirm_POST`              | A user submits a confirmation code from an email or SMS<br>message.                                                                           |
| `verifyCode_POST`                  | A user submits a one-time password (OTP) for passwordless<br>authentication.                                                                  |
| `passkeys_add_POST`                | A user submits a request to register a new passkey credential.                                                                                |
| `passkeys_add_GET`                 | A user navigates to the page where they can register a passkey.                                                                               |
| `login_passkey_POST`               | A user signs in with a passkey.                                                                                                               |

###### Note

Amazon Cognito records `UserSub` but not `UserName` in CloudTrail logs
for requests that are specific to a user. You can find a user for a given
`UserSub` by calling the `ListUsers` API, and using a filter for
sub.

### Identity pools events

**Data events**

Amazon Cognito logs the following Amazon Cognito Identity events to CloudTrail as _data
events_. [Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") are high-volume data-plane API operations that
CloudTrail doesn’t log by default. Additional charges apply for data events.

- [GetCredentialsForIdentity](../../../cognitoidentity/latest/APIReference/API_GetCredentialsForIdentity.md "../../../cognitoidentity/latest/APIReference/API_GetCredentialsForIdentity.md")
- [GetId](../../../cognitoidentity/latest/APIReference/API_GetId.md "../../../cognitoidentity/latest/APIReference/API_GetId.md")
- [GetOpenIdToken](../../../cognitoidentity/latest/APIReference/API_GetOpenIdToken.md "../../../cognitoidentity/latest/APIReference/API_GetOpenIdToken.md")
- [GetOpenIdTokenForDeveloperIdentity](../../../cognitoidentity/latest/APIReference/API_GetOpenIdTokenForDeveloperIdentity.md "../../../cognitoidentity/latest/APIReference/API_GetOpenIdTokenForDeveloperIdentity.md")
- [UnlinkIdentity](../../../cognitoidentity/latest/APIReference/API_UnlinkIdentity.md "../../../cognitoidentity/latest/APIReference/API_UnlinkIdentity.md")

To generate CloudTrail logs for these API operations, you must activate data events in your
trail and choose event selectors for **Cognito identity pools**. For more
information, see [Logging
data events for trails](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md") in the _AWS CloudTrail User
Guide_.

You can also add identity pools event selectors to your trail with the following CLI
command.

```
aws cloudtrail put-event-selectors --trail-name `<trail name>` --advanced-event-selectors \
"{\
   \"Name\": \"Cognito Selector\",\
   \"FieldSelectors\": [\
      {\
         \"Field\": \"eventCategory\",\
         \"Equals\": [\
            \"Data\"\
         ]\
      },\
      {\
         \"Field\": \"resources.type\",\
         \"Equals\": [\
            \"AWS::Cognito::IdentityPool\"\
         ]\
      }\
   ]\
}"
```

**Management events**

Amazon Cognito logs the remainder of Amazon Cognito identity pools API operations as _management events_. CloudTrail logs management event API operations by
default.

For a list of the Amazon Cognito identity pools API operations that Amazon Cognito logs to CloudTrail, see the
[Amazon Cognito identity pools API
Reference](../../../cognitoidentity/latest/APIReference/API_Operations.md "../../../cognitoidentity/latest/APIReference/API_Operations.md").

**Amazon Cognito Sync**

Amazon Cognito logs all Amazon Cognito Sync API operations as management events. For a list of the
Amazon Cognito Sync API operations that Amazon Cognito logs to CloudTrail, see the [Amazon Cognito Sync API
Reference](../../../cognitosync/latest/APIReference/API_Operations.md "../../../cognitosync/latest/APIReference/API_Operations.md").

## Analyzing Amazon Cognito CloudTrail events with Amazon CloudWatch Logs

Insights

You can search and analyze your Amazon Cognito CloudTrail events with Amazon CloudWatch Logs Insights. When you
configure your trail to send events to CloudWatch Logs, CloudTrail sends only the events that match your
trail settings.

To query or research your Amazon Cognito CloudTrail events, in the CloudTrail console, make sure that you
select the **Management events** option in your trail settings so that
you can monitor the management operations performed on your AWS resources. You can
optionally select the **Insights events** option in your trail settings
when you want to identify errors, unusual activity, or unusual user behavior in your
account.

### Sample Amazon Cognito queries

You can use the following queries in the Amazon CloudWatch console.

**General queries**

Find the 25 most recently added log events.

```
fields @timestamp, @message | sort @timestamp desc | limit 25
| filter eventSource = "cognito-idp.amazonaws.com"
```

Get a list of the 25 most recently added log events that include exceptions.

```
fields @timestamp, @message | sort @timestamp desc | limit 25
| filter eventSource = "cognito-idp.amazonaws.com" and @message like /Exception/
```

**Exception and Error Queries**

Find the 25 most recently added log events with error code
`NotAuthorizedException` along with Amazon Cognito user pool
`sub`.

```
fields @timestamp, additionalEventData.sub as user | sort @timestamp desc | limit 25
| filter eventSource = "cognito-idp.amazonaws.com" and errorCode= "NotAuthorizedException"
```

Find the number of records with `sourceIPAddress` and corresponding
`eventName`.

```
filter eventSource = "cognito-idp.amazonaws.com"
| stats count(*) by sourceIPAddress, eventName
```

Find the top 25 IP addresses that triggered a `NotAuthorizedException`
error.

```
filter eventSource = "cognito-idp.amazonaws.com" and errorCode= "NotAuthorizedException"
| stats count(*) as count by sourceIPAddress, eventName
| sort count desc | limit 25
```

Find the top 25 IP addresses that called the `ForgotPassword` API.

```
filter eventSource = "cognito-idp.amazonaws.com" and eventName = 'ForgotPassword'
| stats count(*) as count by sourceIPAddress
| sort count desc | limit 25
```

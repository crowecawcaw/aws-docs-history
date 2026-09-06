

# Amazon Cognito logging in AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

Amazon Cognito is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon Cognito. CloudTrail captures a subset of API calls for Amazon Cognito as events, including calls from the Amazon Cognito console and from code calls to the Amazon Cognito API operations. If you create a trail, you can choose to deliver CloudTrail events to an Amazon S3 bucket, including events for Amazon Cognito. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to Amazon Cognito, the IP address from which the request was made, who made the request, when it was made, and additional details. 

To learn more about CloudTrail, including how to configure and activate it, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

You can also create Amazon CloudWatch alarms for specific CloudTrail events. For example, you can set up CloudWatch to trigger an alarm if an identity pool configuration is changed. For more information, see [Creating CloudWatch alarms for CloudTrail events: Examples](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html).

**Topics**
+ [Information that Amazon Cognito sends to CloudTrail](#amazon-cognito-info-in-cloudtrail)
+ [Analyzing Amazon Cognito CloudTrail events with Amazon CloudWatch Logs Insights](#analyzingcteventscwinsight)
+ [Example Amazon Cognito events](understanding-amazon-cognito-entries.md)

## Information that Amazon Cognito sends to CloudTrail
<a name="amazon-cognito-info-in-cloudtrail"></a>

CloudTrail is turned on when you create your AWS account. When supported event activity occurs in Amazon Cognito, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for Amazon Cognito, create a trail. A CloudTrail trail delivers log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see: 
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-list)
+ [Configuring amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with root or IAM user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

**Confidential data in AWS CloudTrail**  
Because user pools and identity pools process user data, Amazon Cognito obscures some private fields in your CloudTrail events with the value `HIDDEN_DUE_TO_SECURITY_REASONS`. For examples of fields that Amazon Cognito doesn't populate to events, see [Example Amazon Cognito events](understanding-amazon-cognito-entries.md). Amazon Cognito only obscures some fields that commonly contain user information, like passwords and tokens. Amazon Cognito doesn't perform any automatic detection or masking of personally-identifying information that you populate to non-private fields in your API requests.

### User pool events
<a name="user-pools-cloudtrail-events"></a>

Amazon Cognito supports logging for all of the actions listed on the [User pool actions](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_Operations.html) page as events in CloudTrail log files. Amazon Cognito logs user pool events to CloudTrail as *management events*.

The `eventType` field in a Amazon Cognito user pools CloudTrail entry tells you whether your app made the request to the [Amazon Cognito user pools API](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/Welcome.html) or to an [endpoint that serves resources for OpenID Connect, SAML 2.0, or managed login pages](cognito-userpools-server-contract-reference.md). API requests have an `eventType` of `AwsApiCall` and endpoint requests have an `eventType` of `AwsServiceEvent`.

Amazon Cognito logs the following requests to your managed login services as events in CloudTrail.

------
#### [ Hosted UI (classic) events ]


**Hosted UI (classic) events in CloudTrail**  

| Operation | Description | 
| --- | --- | 
| Login\_GET, CognitoAuthentication | A user views or submits credentials to your [Login endpoint](login-endpoint.md). | 
| OAuth2\_Authorize\_GET, Beta\_Authorize\_GET | A user views your [Authorize endpoint](authorization-endpoint.md). | 
| OAuth2Response\_GET, OAuth2Response\_POST | A user submits an IdP token to your /oauth2/idpresponse endpoint. | 
| SAML2Response\_POST, Beta\_SAML2Response\_POST | A user submits an IdP SAML assertion to your /saml2/idpresponse endpoint. | 
| Login\_OIDC\_SAML\_POST | A user enters a username at your [Login endpoint](login-endpoint.md) and matches with an [IdP identifier](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-integrating-3rd-party-saml-providers.html). | 
| Token\_POST, Beta\_Token\_POST | A user submits an authorization code to your [Token endpoint](token-endpoint.md). | 
| Signup\_GET, Signup\_POST | A user submits sign-up information to your /signup endpoint. | 
| Confirm\_GET, Confirm\_POST | A user submits a confirmation code in the hosted UI. | 
| ResendCode\_POST | A user submits a request to resend a confirmation code in the hosted UI. | 
| ForgotPassword\_GET, ForgotPassword\_POST | A user submits a request to reset their password to your /forgotPassword endpoint. | 
| ConfirmForgotPassword\_GET, ConfirmForgotPassword\_POST | A user submits a code to your /confirmForgotPassword endpoint that confirms their ForgotPassword request. | 
| ResetPassword\_GET, ResetPassword\_POST | A user submits a new password in the hosted UI. | 
| Mfa\_GET, Mfa\_POST | A user submits a multi-factor authentication (MFA) code in the hosted UI. | 
| MfaOption\_GET, MfaOption\_POST | A user chooses their preferred method for MFA in the hosted UI. | 
| MfaRegister\_GET, MfaRegister\_POST | A user submits a multi-factor authentication (MFA) code in the hosted UI when registering the MFA. | 
| Logout | A user signs out at your /logout endpoint. | 
| SAML2Logout\_POST | A user signs out at your /saml2/logout endpoint. | 
| Error\_GET | A user views an error page in the hosted UI. | 
| UserInfo\_GET, UserInfo\_POST | A user or IdP exchanges information with your [userInfo endpoint](userinfo-endpoint.md). | 
| Confirm\_With\_Link\_GET | A user submits a confirmation based on a link that Amazon Cognito sent in an email message. | 
| Event\_Feedback\_GET | A user submits feedback to Amazon Cognito about a [threat protection](cognito-user-pool-settings-threat-protection.md) event. | 

------
#### [ Managed login events ]


**Managed login events in CloudTrail**  

| Operation | Description | 
| --- | --- | 
| login\_POST | A user submits credentials to your [Login endpoint](login-endpoint.md). | 
| login\_continue\_POST | A user who has already signed in one time chooses to sign in again. | 
| forgotPassword\_POST | A user resets their password. | 
| selectChallenge\_POST | A user responds to an authentication challenge after they submit their username or credentials. | 
| confirmUser\_GET | A user opens the link in a [confirmation or verification email message](signing-up-users-in-your-app.md). | 
| mfa\_back\_POST | A user chooses the Back button after an MFA prompt. | 
| mfa\_options\_POST | A user selects an MFA option. | 
| mfa\_phone\_register\_POST | A user submits a phone number to register as a MFA factor. This operation causes Amazon Cognito to send an MFA code to their phone number. | 
| mfa\_phone\_verify\_POST | A user submits an MFA code sent to their phone number. | 
| mfa\_phone\_resendCode\_POST | A user submits a request to resend a MFA code to their phone number. | 
| mfa\_totp\_POST | A user submits a TOTP MFA code. | 
| signup\_POST | A user submits information to your /signup managed login page. | 
| signup\_confirm\_POST | A user submits a confirmation code from an email or SMS message. | 
| verifyCode\_POST | A user submits a one-time password (OTP) for passwordless authentication. | 
| passkeys\_add\_POST | A user submits a request to register a new passkey credential. | 
| passkeys\_add\_GET | A user navigates to the page where they can register a passkey. | 
| login\_passkey\_POST | A user signs in with a passkey. | 

------

**Note**  
Amazon Cognito records `UserSub` but not `UserName` in CloudTrail logs for requests that are specific to a user. You can find a user for a given `UserSub` by calling the `ListUsers` API, and using a filter for sub. 

### Identity pools events
<a name="identity-pools-cloudtrail-events"></a>

**Data events**

Amazon Cognito logs the following Amazon Cognito Identity events to CloudTrail as *data events*. [Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events) are high-volume data-plane API operations that CloudTrail doesn’t log by default. Additional charges apply for data events.
+ [GetCredentialsForIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetCredentialsForIdentity.html)
+ [GetId](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetId.html)
+ [GetOpenIdToken](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetOpenIdToken.html)
+ [GetOpenIdTokenForDeveloperIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetOpenIdTokenForDeveloperIdentity.html)
+ [UnlinkIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_UnlinkIdentity.html)

To generate CloudTrail logs for these API operations, you must activate data events in your trail and choose event selectors for **Cognito identity pools**. For more information, see [Logging data events for trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *AWS CloudTrail User Guide*.

You can also add identity pools event selectors to your trail with the following CLI command.

```
aws cloudtrail put-event-selectors --trail-name {{<trail name>}} --advanced-event-selectors \
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

Amazon Cognito logs the remainder of Amazon Cognito identity pools API operations as *management events*. CloudTrail logs management event API operations by default.

For a list of the Amazon Cognito identity pools API operations that Amazon Cognito logs to CloudTrail, see the [Amazon Cognito identity pools API Reference](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_Operations.html).

**Amazon Cognito Sync**

Amazon Cognito logs all Amazon Cognito Sync API operations as management events. For a list of the Amazon Cognito Sync API operations that Amazon Cognito logs to CloudTrail, see the [Amazon Cognito Sync API Reference](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_Operations.html).

## Analyzing Amazon Cognito CloudTrail events with Amazon CloudWatch Logs Insights
<a name="analyzingcteventscwinsight"></a>

You can search and analyze your Amazon Cognito CloudTrail events with Amazon CloudWatch Logs Insights. When you configure your trail to send events to CloudWatch Logs, CloudTrail sends only the events that match your trail settings.

To query or research your Amazon Cognito CloudTrail events, in the CloudTrail console, make sure that you select the **Management events** option in your trail settings so that you can monitor the management operations performed on your AWS resources. You can optionally select the **Insights events** option in your trail settings when you want to identify errors, unusual activity, or unusual user behavior in your account.

### Sample Amazon Cognito queries
<a name="analyzingcteventscwinsight-samplequeries"></a>

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

Find the 25 most recently added log events with error code `NotAuthorizedException` along with Amazon Cognito user pool `sub`.

```
fields @timestamp, additionalEventData.sub as user | sort @timestamp desc | limit 25
| filter eventSource = "cognito-idp.amazonaws.com" and errorCode= "NotAuthorizedException"
```

Find the number of records with `sourceIPAddress` and corresponding `eventName`.

```
filter eventSource = "cognito-idp.amazonaws.com"
| stats count(*) by sourceIPAddress, eventName
```

Find the top 25 IP addresses that triggered a `NotAuthorizedException` error.

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
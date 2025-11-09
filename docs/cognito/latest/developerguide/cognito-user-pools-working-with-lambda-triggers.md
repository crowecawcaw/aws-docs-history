# Customizing user pool

workflows with Lambda triggers

Amazon Cognito works with AWS Lambda functions to modify the authentication behavior of your user
pool. You can configure your user pool to automatically invoke Lambda functions before their
first sign-up, after they complete authentication, and at several stages in between. Your
functions can modify the default behavior of your authentication flow, make API requests to
modify your user pool or other AWS resources, and communicate with external systems. The
code in your Lambda functions is your own. Amazon Cognito sends event data to your function, waits for
the function to process the data, and in most cases anticipates a response event that
reflects any changes you want to make to the session.

Within the system of request and response events, you can introduce your own
authentication challenges, migrate users between your user pool and another identity store,
customize messages, and modify JSON web tokens (JWTs).

Lambda triggers can customize the response that Amazon Cognito delivers to your user after they
initiate an action in your user pool. For example, you can prevent sign-in by a user who
would otherwise succeed. They can also perform runtime operations against your AWS
environment, external APIs, databases, or identity stores. The migrate user trigger, for
example, can combine external action with a change in Amazon Cognito: you can look up user
information in an external directory, then set attributes on a new user based on that
external information.

When you have a Lambda trigger assigned to your user pool, Amazon Cognito interrupts its default
flow to request information from your function. Amazon Cognito generates a JSON _event_ and passes it to your function. The event contains
information about your user's request to create a user account, sign in, reset a password,
or update an attribute. Your function then has an opportunity to take action, or to send the
event back unmodified. An event returned unmodified notifies your user pool to proceed with
the default action for the event. For example, your pre sign-up trigger can automatically
confirm users for the `PreSignUp_SignUp` trigger source, but return the event
unchanged for external and administrator-created users.

The following table summarizes some of the ways you can use Lambda triggers to customize
user pool operations:

| User Pool Flow                                                                                                                    | Operation                                                                                                                         | Description                                                              |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Custom Authentication Flow**                                                                                                    | **Define Auth Challenge**                                                                                                         | Determines the next challenge in a custom auth flow                      |
| **Create Auth Challenge**                                                                                                         | Creates a challenge in a custom auth flow                                                                                         |
| **Verify Auth Challenge Response**                                                                                                | Determines if a response is correct in a custom auth flow                                                                         |
| **Authentication<br>Events**                                                                                                      | **[Pre authentication Lambda<br>trigger](user-pool-lambda-pre-authentication.md "user-pool-lambda-pre-authentication.md")**       | Custom validation to accept or deny the sign-in request                  |
| **[Post authentication Lambda<br>trigger](user-pool-lambda-post-authentication.md "user-pool-lambda-post-authentication.md")**    | Logs events for custom analytics                                                                                                  |
| **[Pre token generation Lambda<br>trigger](user-pool-lambda-pre-token-generation.md "user-pool-lambda-pre-token-generation.md")** | Augments or suppresses token claims                                                                                               |
| **Sign-Up**                                                                                                                       | **[Pre sign-up Lambda trigger](user-pool-lambda-pre-sign-up.md "user-pool-lambda-pre-sign-up.md")**                               | Performs custom validation that accepts or denies the sign-up<br>request |
| **[Post confirmation Lambda trigger](user-pool-lambda-post-confirmation.md "user-pool-lambda-post-confirmation.md")**             | Adds custom welcome messages or event logging for custom<br>analytics                                                             |
| **[Migrate user Lambda trigger](user-pool-lambda-migrate-user.md "user-pool-lambda-migrate-user.md")**                            | Migrates a user from an existing user directory to user pools                                                                     |
| **Messages**                                                                                                                      | **[Custom message Lambda trigger](user-pool-lambda-custom-message.md "user-pool-lambda-custom-message.md")**                      | Performs advanced customization and localization of messages             |
| **Token Creation**                                                                                                                | **[Pre token generation Lambda<br>trigger](user-pool-lambda-pre-token-generation.md "user-pool-lambda-pre-token-generation.md")** | Adds or removes attributes in ID and access tokens                       |
| **Email and SMS third-party<br>providers**                                                                                        | **[Custom sender Lambda<br>triggers](user-pool-lambda-custom-sender-triggers.md "user-pool-lambda-custom-sender-triggers.md")**   | Uses a third-party provider to send SMS and email messages               |

###### Topics

- [Things to know about Lambda
  triggers](#important-lambda-considerations "#important-lambda-considerations")
- [Add a user pool Lambda trigger](#triggers-working-with-lambda "#triggers-working-with-lambda")
- [User pool
  Lambda trigger event](#cognito-user-pools-lambda-trigger-event-parameter-shared "#cognito-user-pools-lambda-trigger-event-parameter-shared")
- [User pool Lambda
  trigger common parameters](#cognito-user-pools-lambda-trigger-syntax-shared "#cognito-user-pools-lambda-trigger-syntax-shared")
- [Client metadata](#working-with-lambda-trigger-client-metadata "#working-with-lambda-trigger-client-metadata")
- [Connecting API operations to Lambda
  triggers](#lambda-triggers-by-event "#lambda-triggers-by-event")
- [Connecting Lambda triggers to user
  pool functional operations](#working-with-lambda-trigger-sources "#working-with-lambda-trigger-sources")
- [Pre sign-up Lambda trigger](user-pool-lambda-pre-sign-up.md "user-pool-lambda-pre-sign-up.md")
- [Post confirmation Lambda trigger](user-pool-lambda-post-confirmation.md "user-pool-lambda-post-confirmation.md")
- [Pre authentication Lambda
  trigger](user-pool-lambda-pre-authentication.md "user-pool-lambda-pre-authentication.md")
- [Post authentication Lambda
  trigger](user-pool-lambda-post-authentication.md "user-pool-lambda-post-authentication.md")
- [Custom authentication challenge Lambda
  triggers](user-pool-lambda-challenge.md "user-pool-lambda-challenge.md")
- [Pre token generation Lambda
  trigger](user-pool-lambda-pre-token-generation.md "user-pool-lambda-pre-token-generation.md")
- [Migrate user Lambda trigger](user-pool-lambda-migrate-user.md "user-pool-lambda-migrate-user.md")
- [Custom message Lambda trigger](user-pool-lambda-custom-message.md "user-pool-lambda-custom-message.md")
- [Custom sender Lambda
  triggers](user-pool-lambda-custom-sender-triggers.md "user-pool-lambda-custom-sender-triggers.md")

## Things to know about Lambda

triggers

When you are preparing your user pools for Lambda functions, consider the
following:

- The events that Amazon Cognito sends to your Lambda triggers might change with new
  features. The positions of response and request elements in the JSON hierarchy
  might change, or element names might be added. In your Lambda function, you can
  expect to receive the input-element key-value pairs described in this guide, but
  stricter input validation can cause your functions to fail.
- You can choose one of multiple versions of the events that Amazon Cognito sends to some
  triggers. Some versions might require you to accept a change to your Amazon Cognito
  pricing. For more information about pricing, see [Amazon Cognito Pricing](https://aws.amazon.com/cognito/pricing/ "https://aws.amazon.com/cognito/pricing/"). To
  customize access tokens in a [Pre token generation Lambda
  trigger](user-pool-lambda-pre-token-generation.md "user-pool-lambda-pre-token-generation.md"), you must configure your
  user pool with a feature plan other than _Lite_
  and update your Lambda trigger configuration to use event version 2.
- Except for [Custom sender Lambda
  triggers](user-pool-lambda-custom-sender-triggers.md "user-pool-lambda-custom-sender-triggers.md"), Amazon Cognito invokes Lambda
  functions synchronously. When Amazon Cognito calls your Lambda function, it must respond
  within 5 seconds. If it doesn't and if the call can be retried, Amazon Cognito retries
  the call. After three unsuccessful attempts, the function times out. You can't
  change this five-second timeout value. For more information, see [Lambda programming model](../../../lambda/latest/dg/foundation-progmodel.md "../../../lambda/latest/dg/foundation-progmodel.md")
  in the AWS Lambda Developer Guide.

Amazon Cognito doesn't retry function calls that return an [Invoke error](../../../lambda/latest/dg/API_Invoke.md#API_Invoke_Errors "../../../lambda/latest/dg/API_Invoke.md#API_Invoke_Errors") with an HTTP status code of
500-599. These codes indicate a configuration issue that leaves Lambda unable to
launch the function. For more information, see [Error
handling and automatic retries in AWS Lambda](../../../lambda/latest/dg/invocation-retries.md "../../../lambda/latest/dg/invocation-retries.md").

- You can't declare a function version in your Lambda trigger configuration.
  Amazon Cognito user pools invoke the latest version of your function by default. However, you can
  associate a function version with an alias and set your trigger
  `LambdaArn` to the alias ARN in a [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") or [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md") API request. This option isn't available in the
  AWS Management Console. For more information about aliases, see [Lambda function
  aliases](../../../lambda/latest/dg/configuration-aliases.md "../../../lambda/latest/dg/configuration-aliases.md") in the _AWS Lambda Developer
  Guide_.
- If you delete a Lambda trigger, you must update the corresponding trigger in
  the user pool. For example, if you delete the post authentication trigger, you
  must set the **Post authentication** trigger in the
  corresponding user pool to **none**.
- If your Lambda function doesn't return the request and response parameters to
  Amazon Cognito, or returns an error, the authentication event doesn't succeed. You can
  return an error in your function to prevent a user's sign-up, authentication,
  token generation, or any other stage of their authentication flow that invokes
  Lambda trigger.

Managed login returns errors that Lambda triggers generate as error text above
the sign-in prompt. The Amazon Cognito user pools API returns trigger errors in the format
``[trigger]` failed with error
 `[error text from response]``. As a best
practice, only generate errors in your Lambda functions that you want your users
to see. Use output methods like `print()` to log any sensitive or
debugging information to CloudWatch Logs. For an example, see [Pre sign-up example:
Deny sign-up if user name has fewer than five characters](user-pool-lambda-pre-sign-up.md#aws-lambda-triggers-pre-registration-example-3 "user-pool-lambda-pre-sign-up.md#aws-lambda-triggers-pre-registration-example-3").

- You can add a Lambda function in another AWS account as a trigger for your
  user pool. You must add cross-account triggers with the [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") and UpdateUserPool API operations, or their equivalents in AWS CloudFormation and
  the AWS CLI. You can't add cross-account functions in the AWS Management Console.
- When you add a Lambda trigger in the Amazon Cognito console, Amazon Cognito adds a resource-based
  policy to your function that permits your user pool to invoke the function. When
  you create a Lambda trigger outside of the Amazon Cognito console, including a
  cross-account function, you must add permissions to the resource-based policy of
  the Lambda function. Your added permissions must allow Amazon Cognito to invoke the
  function on behalf of your user pool. You can [add permissions from
  the Lambda Console](../../../lambda/latest/dg/access-control-resource-based.md "../../../lambda/latest/dg/access-control-resource-based.md") or use the Lambda [AddPermission](../../../lambda/latest/dg/API_AddPermission.md "../../../lambda/latest/dg/API_AddPermission.md") API
  operation.

###### Example Lambda Resource-Based Policy

The following example Lambda resource-based policy grants Amazon Cognito a limited
ability to invoke a Lambda function. Amazon Cognito can only invoke the function when
it does so on behalf of both the user pool in the `aws:SourceArn`
condition and the account in the `aws:SourceAccount`
condition.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "default",
 "Statement": [
 {
 "Sid": "LambdaCognitoIdpTrust",
 "Effect": "Allow",
 "Principal": {
 "Service": "cognito-idp.amazonaws.com"
 },
 "Action": "lambda:InvokeFunction",
 "Resource": "arn:`aws`:lambda:`us-east-1`:`111122223333`:function:`MyFunction`",
 "Condition": {
 "StringEquals": {
 "AWS:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "AWS:SourceArn": "arn:`aws`:cognito-idp:`us-east-1`:`111122223333`:userpool/`us-east-1_EXAMPLE`"
 }
 }
 }
 ]
}`

```

## Add a user pool Lambda trigger

###### To add a user pool Lambda trigger with the console

1. Use the [Lambda console](https://console.aws.amazon.com/lambda/home "https://console.aws.amazon.com/lambda/home") to
   create a Lambda function. For more information on Lambda functions, see the
   [AWS Lambda Developer Guide](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md").
2. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"),
   and then choose **User Pools**.
3. Choose an existing user pool from the list, or [create a user
   pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md").
4. Choose the **Extensions** menu and locate **Lambda
   triggers**.
5. Choose **Add a Lambda trigger**.
6. Select a Lambda trigger **Category** based on the stage of
   authentication that you want to customize.
7. Select **Assign Lambda function** and select a function in the
   same AWS Region as your user pool.

###### Note

If your AWS Identity and Access Management (IAM) credentials have permission to update the Lambda
function, Amazon Cognito adds a Lambda resource-based policy. With this policy, Amazon Cognito
can invoke the function that you select. If the signed-in credentials do not
have sufficient IAM permissions, you must update the resource-based policy
separately. For more information, see [Things to know about Lambda
triggers](#important-lambda-considerations "#important-lambda-considerations"). 8. Choose **Save changes**. 9. You can use CloudWatch in the Lambda console to log your Lambda function . For more
information, see [Accessing CloudWatch Logs for Lambda](../../../lambda/latest/dg/monitoring-functions-logs.md "../../../lambda/latest/dg/monitoring-functions-logs.md").

## User pool

Lambda trigger event

Amazon Cognito passes event information to your Lambda function. The Lambda function returns the
same event object back to Amazon Cognito with any changes in the response. If your function
returns the input event without modification, Amazon Cognito proceed with default behavior. The
following shows the parameters that are common to all Lambda trigger input events. For
trigger-specific event syntax, review the event schema on the section of this guide for
each trigger.

JSON

```
{
    "version": "`string`",
    "triggerSource": "`string`",
    "region": `AWSRegion`,
    "userPoolId": "`string`",
    "userName": "`string`",
    "callerContext":
        {
            "awsSdkVersion": "`string`",
            "clientId": "`string`"
        },
    "request":
        {
            "userAttributes": {
                "`string`": "`string`",
                ....
            }
        },
    "response": {}
}
```

## User pool Lambda

trigger common parameters

**version**

The version number of your Lambda function.

**triggerSource**

The name of the event that triggered the Lambda function. For a description
of each triggerSource see [Connecting Lambda triggers to user
pool functional operations](#working-with-lambda-trigger-sources "#working-with-lambda-trigger-sources").

**region**

The AWS Region as an `AWSRegion` instance.

**userPoolId**

The ID of the user pool.

**userName**

The current user's username.

**callerContext**

Metadata about the request and the code environment. It contains the
fields **awsSdkVersion** and
**clientId**.

**awsSdkVersion**

The version of the AWS SDK that generated the
request.

\***\*clientId\*\***

The ID of the user pool app client.

**request**

Details of your user's API request. It includes the following fields, and
any request parameters that are particular to the trigger. For example, an
event that Amazon Cognito sends to a pre-authentication trigger will also contain a
`userNotFound` parameter. You can process the value of this
parameter to take a custom action when your user tries to sign in with an
unregistered username.

**userAttributes**

One or more key-value pairs of user attribute names and
values, for example `"email":
 "john@example.com"`.

**response**

This parameter doesn't contain any information in the original request.
Your Lambda function must return the entire event to Amazon Cognito, and add any
return parameters to the `response`. To see what return
parameters your function can include, refer to the documentation for the
trigger that you want to use.

## Client metadata

You can submit custom parameters to your Lambda trigger functions in API operations and
[Token endpoint](token-endpoint.md "token-endpoint.md") requests. With
client metadata, your application can collect additional information about the
environment where requests originate. When you pass client metadata to your Lambda
functions, they can process the additional data and make use of it in logging or
customization of authentication flows. Client metadata is string pairs of your choosing
and design in a JSON key-value format.

###### Client metadata example use cases

- Pass geolocation data at sign-up to the [pre sign-up trigger](user-pool-lambda-pre-sign-up.md "user-pool-lambda-pre-sign-up.md") and
  prevent sign-in from unwanted locations.
- Pass tenant ID data to [custom
  challenge triggers](user-pool-lambda-challenge.md "user-pool-lambda-challenge.md") and issue different challenges to customers from
  different business units.
- Pass a user's token to the [pre token generation
  trigger](user-pool-lambda-pre-token-generation.md "user-pool-lambda-pre-token-generation.md") and generate a log of the principal that an M2M request was
  made on behalf of. For an example request, see [Client credentials with basic authorization](token-endpoint.md#exchanging-client-credentials-for-an-access-token-in-request-body "token-endpoint.md#exchanging-client-credentials-for-an-access-token-in-request-body").

Here is an example of passing client metadata to the pre sign-up trigger.

SignUp request
The following is an example [SignUp](../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md#CognitoUserPools-SignUp-request-ValidationData "../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md#CognitoUserPools-SignUp-request-ValidationData") request with client metadata that Amazon Cognito passes to a pre
sign-up trigger.

```
POST HTTP/1.1
Host: cognito-idp.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.SignUp
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "ClientId": "1example23456789",
    "Username": "mary_major",
    "Password": "<Password>",
    "SecretHash": "<Secret hash>",
    "ClientMetadata": {
        "IpAddress" : "192.0.2.252",
        "GeoLocation" : "Netherlands (Kingdom of the) [NL]"
    }
    "UserAttributes": [
        {
            "Name": "name",
            "Value": "Mary"
        },
        {
            "Name": "email",
            "Value": "mary_major@example.com"
        },
        {
            "Name": "phone_number",
            "Value": "+12065551212"
        }
    ],
}
```

Lambda trigger input event
The request results in the following request body to your pre sign-up
function.

```
{
    "callerContext": {
        "awsSdkVersion": "aws-sdk-unknown-unknown",
        "clientId": "1example23456789"
    },
    "region": "us-west-2",
    "request": {
        "clientMetadata": {
            "GeoLocation": "Netherlands (Kingdom of the) [NL]",
            "IpAddress": "192.0.2.252"
        },
        "userAttributes": {
            "email": "mary_major@example.com",
            "name": "Mary",
            "phone_number": "+12065551212"
        },
        "validationData": null
    },
    "response": {
        "autoConfirmUser": false,
        "autoVerifyEmail": false,
        "autoVerifyPhone": false
    },
    "triggerSource": "PreSignUp_SignUp",
    "userName": "mary_major2",
    "userPoolId": "us-west-2_EXAMPLE",
    "version": "1"
}
```

###### Client metadata for machine-to-machine (M2M) client credentials

You can pass client
metadata in M2M requests. Client metadata is additional information from a
user or application environment that can contribute to the outcomes of a [Pre token generation Lambda
trigger](user-pool-lambda-pre-token-generation.md "user-pool-lambda-pre-token-generation.md"). In authentication operations with a user principal, you can pass client metadata
to the pre token generation trigger in the body of [AdminRespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.md") and [RespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md "../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md") API requests. Because applications conduct the
flow for generation of access tokens for M2M with direct requests to the [Token endpoint](token-endpoint.md "token-endpoint.md"), they have a different
model. In the POST body of token requests for client credentials, pass an
`aws_client_metadata` parameter with the client metadata object
URL-encoded (`x-www-form-urlencoded`) to string. For an example request,
see [Client credentials with basic authorization](token-endpoint.md#exchanging-client-credentials-for-an-access-token-in-request-body "token-endpoint.md#exchanging-client-credentials-for-an-access-token-in-request-body"). The following is an example parameter that passes the key-value pairs
`{"environment": "dev", "language": "en-US"}`.

```
aws_client_metadata=%7B%22environment%22%3A%20%22dev%22,%20%22language%22%3A%20%22en-US%22%7D
```

###### Temporary user attributes: `validationData`

Some authentication operations also have a `validationData` parameter.
Like client metadata, this is an opportunity to pass external information that Amazon Cognito
doesn't automatically gather to Lambda triggers. The validation data field is
intended to provide your Lambda function witth additional user context in sign-up and
sign-in operations. [SignUp](../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md#CognitoUserPools-SignUp-request-ValidationData "../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md#CognitoUserPools-SignUp-request-ValidationData") and [AdminCreateUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.md#CognitoUserPools-AdminCreateUser-request-ValidationData "../../../cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.md#CognitoUserPools-AdminCreateUser-request-ValidationData") pass `validationData` to the [pre sign-up trigger](user-pool-lambda-pre-sign-up.md "user-pool-lambda-pre-sign-up.md"). [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md#CognitoUserPools-InitiateAuth-request-ClientMetadata "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md#CognitoUserPools-InitiateAuth-request-ClientMetadata") and [AdminInitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md#CognitoUserPools-AdminInitiateAuth-request-ClientMetadata "../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md#CognitoUserPools-AdminInitiateAuth-request-ClientMetadata") pass `ClientMetadata` in the API request
body as `validationData` in the input event to the [pre authentication](user-pool-lambda-pre-authentication.md "user-pool-lambda-pre-authentication.md") and
[migrate user](user-pool-lambda-migrate-user.md "user-pool-lambda-migrate-user.md")
triggers.

To map API operations to the functions that they can pass client metadata to, refer to
the trigger source sections that follow.

## Connecting API operations to Lambda

triggers

The following sections describe the Lambda triggers that Amazon Cognito invokes from the
activity in your user pool.

When your app signs in users through the Amazon Cognito user pools API, managed login, or user pool
endpoints, Amazon Cognito invokes your Lambda functions based on the session context. For more
information about the Amazon Cognito user pools API and user pool endpoints, see [Understanding API, OIDC, and managed login pages
authentication](authentication-flows-public-server-side.md#user-pools-API-operations "authentication-flows-public-server-side.md#user-pools-API-operations"). The
tables in the sections that follow describe events that cause Amazon Cognito to invoke a
function, and the `triggerSource` string that Amazon Cognito includes in the
request.

###### Topics

- [Lambda triggers in the
  Amazon Cognito API](#lambda-triggers-native-users-native-api "#lambda-triggers-native-users-native-api")
- [Lambda triggers for Amazon Cognito
  local users in managed login](#lambda-triggers-native-users-hosted-UI "#lambda-triggers-native-users-hosted-UI")
- [Lambda triggers for federated
  users](#lambda-triggers-for-federated-users "#lambda-triggers-for-federated-users")

### Lambda triggers in the

Amazon Cognito API

The following table describes the source strings for the Lambda triggers that Amazon Cognito
can invoke when your app creates, signs in, or updates a local user.

| Local user trigger sources in the Amazon Cognito API                                                                                                                                                                                                                                                                                                                                                                                  | API operation                                                                                               | Lambda trigger                           | Trigger source |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------- | -------------- |
| [AdminCreateUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.md")                                                                                                                                                                                                                                                  | Pre sign-up                                                                                                 | `PreSignUp_AdminCreateUser`              |
| Pre token generation                                                                                                                                                                                                                                                                                                                                                                                                                  | `TokenGeneration_NewPasswordChallenge`                                                                      |
| Custom message                                                                                                                                                                                                                                                                                                                                                                                                                        | `CustomMessage_AdminCreateUser`                                                                             |
| Custom email sender                                                                                                                                                                                                                                                                                                                                                                                                                   | `CustomEmailSender_AdminCreateUser`                                                                         |
| Custom SMS sender                                                                                                                                                                                                                                                                                                                                                                                                                     | `CustomSMSSender_AdminCreateUser`                                                                           |
| [SignUp](../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md "../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md")                                                                                                                                                                                                                                                                             | Pre sign-up                                                                                                 | `PreSignUp_SignUp`                       |
| Custom message                                                                                                                                                                                                                                                                                                                                                                                                                        | `CustomMessage_SignUp`                                                                                      |
| Custom email sender                                                                                                                                                                                                                                                                                                                                                                                                                   | `CustomEmailSender_SignUp`                                                                                  |
| Custom SMS sender                                                                                                                                                                                                                                                                                                                                                                                                                     | `CustomSMSSender_SignUp`                                                                                    |
| [ConfirmSignUp](../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmSignUp.md "../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmSignUp.md")<br>[AdminConfirmSignUp](../../../cognito-user-identity-pools/latest/APIReference/API_AdminConfirmSignUp.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminConfirmSignUp.md")                                                       | Post confirmation                                                                                           | `PostConfirmation_ConfirmSignUp`         |
| [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md")<br>[AdminInitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md")                                                             | Pre authentication                                                                                          | `PreAuthentication_Authentication`       |
| Post authentication                                                                                                                                                                                                                                                                                                                                                                                                                   | `PostAuthentication_Authentication`                                                                         |
| Define auth challenge                                                                                                                                                                                                                                                                                                                                                                                                                 | `DefineAuthChallenge_Authentication`                                                                        |
| Create auth challenge                                                                                                                                                                                                                                                                                                                                                                                                                 | `CreateAuthChallenge_Authentication`                                                                        |
| Verify auth challenge                                                                                                                                                                                                                                                                                                                                                                                                                 | `VerifyAuthChallenge_Authentication`                                                                        |
| Pre token generation                                                                                                                                                                                                                                                                                                                                                                                                                  | `TokenGeneration_Authentication`<br>`TokenGeneration_AuthenticateDevice`<br>`TokenGeneration_RefreshTokens` |
| Migrate user                                                                                                                                                                                                                                                                                                                                                                                                                          | `UserMigration_Authentication`                                                                              |
| Custom message                                                                                                                                                                                                                                                                                                                                                                                                                        | `CustomMessage_Authentication`                                                                              |
| Custom email sender                                                                                                                                                                                                                                                                                                                                                                                                                   | `CustomEmailSender_AccountTakeOverNotification`<br>`CustomEmailSender_Authentication`                       |
| Custom SMS sender                                                                                                                                                                                                                                                                                                                                                                                                                     | `CustomSMSSender_Authentication`                                                                            |
| [RespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md "../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md")<br>[AdminRespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.md") | Post authentication                                                                                         | `PostAuthentication_Authentication`      |
| Define auth challenge                                                                                                                                                                                                                                                                                                                                                                                                                 | `DefineAuthChallenge_Authentication`                                                                        |
| Create auth challenge                                                                                                                                                                                                                                                                                                                                                                                                                 | `CreateAuthChallenge_Authentication`                                                                        |
| Verify auth challenge                                                                                                                                                                                                                                                                                                                                                                                                                 | `VerifyAuthChallenge_Authentication`                                                                        |
| Pre token generation                                                                                                                                                                                                                                                                                                                                                                                                                  | `TokenGeneration_Authentication`<br>`TokenGeneration_AuthenticateDevice`<br>`TokenGeneration_RefreshTokens` |
| Custom message                                                                                                                                                                                                                                                                                                                                                                                                                        | `CustomMessage_Authentication`                                                                              |
| Custom email sender                                                                                                                                                                                                                                                                                                                                                                                                                   | `CustomEmailSender_AccountTakeOverNotification`<br>`CustomEmailSender_Authentication`                       |
| Custom SMS sender                                                                                                                                                                                                                                                                                                                                                                                                                     | `CustomSMSSender_Authentication`                                                                            |
| [ForgotPassword](../../../cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.md")                                                                                                                                                                                                                                                     | Migrate user                                                                                                | `UserMigration_ForgotPassword`           |
| Custom message                                                                                                                                                                                                                                                                                                                                                                                                                        | `CustomMessage_ForgotPassword`                                                                              |
| Custom email sender                                                                                                                                                                                                                                                                                                                                                                                                                   | `CustomEmailSender_ForgotPassword`                                                                          |
| Custom SMS sender                                                                                                                                                                                                                                                                                                                                                                                                                     | `CustomSMSSender_ForgotPassword`                                                                            |
| [ConfirmForgotPassword](../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmForgotPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmForgotPassword.md")                                                                                                                                                                                                                                | Post confirmation                                                                                           | `PostConfirmation_ConfirmForgotPassword` |
| [UpdateUserAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.md")<br>[AdminUpdateUserAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.md")             | Custom message                                                                                              | `CustomMessage_UpdateUserAttribute`      |
| Custom email sender                                                                                                                                                                                                                                                                                                                                                                                                                   | `CustomEmailSender_UpdateUserAttribute`                                                                     |
| Custom SMS sender                                                                                                                                                                                                                                                                                                                                                                                                                     | `CustomSMSSender_UpdateUserAttribute`                                                                       |
| [VerifyUserAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_VerifyUserAttributes.md "../../../cognito-user-identity-pools/latest/APIReference/API_VerifyUserAttributes.md")                                                                                                                                                                                                                                   | Custom message                                                                                              | `CustomMessage_VerifyUserAttribute`      |
| Custom email sender                                                                                                                                                                                                                                                                                                                                                                                                                   | `CustomEmailSender_VerifyUserAttribute`                                                                     |
| Custom SMS sender                                                                                                                                                                                                                                                                                                                                                                                                                     | `CustomSMSSender_VerifyUserAttribute`                                                                       |
| [GetTokensFromRefreshToken](../../../cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.md")                                                                                                                                                                                                                    | Pre token generation                                                                                        | `TokenGeneration_Authentication`         |

### Lambda triggers for Amazon Cognito

local users in managed login

The following table describes the source strings for the Lambda triggers that Amazon Cognito
can invoke when a local user signs in to your user pool with managed login.

| Local user trigger sources in managed login | Managed login URI                                                                                           | Lambda trigger                           | Trigger source |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------- | -------------- |
| `/signup`                                   | Pre sign-up                                                                                                 | `PreSignUp_SignUp`                       |
| Custom message                              | `CustomMessage_SignUp`                                                                                      |
| Custom email sender                         | `CustomEmailSender_SignUp`                                                                                  |
| Custom SMS sender                           | `CustomSMSSender_SignUp`                                                                                    |
| `/confirmuser`                              | Post confirmation                                                                                           | `PostConfirmation_ConfirmSignUp`         |
| `/login`                                    | Pre authentication                                                                                          | `PreAuthentication_Authentication`       |
| Pre token generation                        | `TokenGeneration_Authentication`<br>`TokenGeneration_AuthenticateDevice`<br>`TokenGeneration_RefreshTokens` |
| Migrate user                                | `UserMigration_Authentication`                                                                              |
| Custom message                              | `CustomMessage_Authentication`                                                                              |
| Custom email sender                         | `CustomEmailSender_AccountTakeOverNotification`<br>`CustomEmailSender_Authentication`                       |
| Custom SMS sender                           | `CustomSMSSender_Authentication`                                                                            |
| `/forgotpassword`                           | Migrate user                                                                                                | `UserMigration_ForgotPassword`           |
| Custom message                              | `CustomMessage_ForgotPassword`                                                                              |
| Custom email sender                         | `CustomEmailSender_ForgotPassword`                                                                          |
| Custom SMS sender                           | `CustomSMSSender_ForgotPassword`                                                                            |
| `/confirmforgotpassword`                    | Post confirmation                                                                                           | `PostConfirmation_ConfirmForgotPassword` |

### Lambda triggers for federated

users

You can use the following Lambda triggers to customize your user pool workflows for
users who sign in with a federated provider.

###### Note

Federated users can use managed login to sign in, or you can generate a
request to the [Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md") that silently redirects them to their
identity provider sign-in page. You can't sign in federated users with the Amazon Cognito
user pools API.

| Federated user trigger sources | Sign-in event                       | Lambda trigger                     | Trigger source |
| ------------------------------ | ----------------------------------- | ---------------------------------- | -------------- |
| First sign-in                  | Pre sign-up                         | `PreSignUp_ExternalProvider`       |
| Post confirmation              | `PostConfirmation_ConfirmSignUp`    |
| Pre token generation           | `TokenGeneration_HostedAuth`        |
| Subsequent sign-ins            | Pre authentication                  | `PreAuthentication_Authentication` |
| Post authentication            | `PostAuthentication_Authentication` |
| Pre token generation           | `TokenGeneration_HostedAuth`        |

Federated sign-in does not invoke any [Custom authentication challenge Lambda
triggers](user-pool-lambda-challenge.md "user-pool-lambda-challenge.md"), [Migrate user Lambda trigger](user-pool-lambda-migrate-user.md "user-pool-lambda-migrate-user.md"), [Custom message Lambda trigger](user-pool-lambda-custom-message.md "user-pool-lambda-custom-message.md"), or [Custom sender Lambda
triggers](user-pool-lambda-custom-sender-triggers.md "user-pool-lambda-custom-sender-triggers.md") in your user pool.

## Connecting Lambda triggers to user

pool functional operations

Each Lambda trigger serves a functional role in your user pool. For example, a trigger
can modify your sign-up flow, or add a custom authentication challenge. The event that
Amazon Cognito sends to a Lambda function can reflect one of multiple actions that make up that
functional role. For example, Amazon Cognito invokes a pre sign-up trigger when your user signs
up, and when you create a user. Each of these different cases for the same functional
role has its own `triggerSource` value. Your Lambda function can process
incoming events differently based on the operation that invoked it.

Amazon Cognito also invokes all assigned functions when an event corresponds to a trigger
source. For example, when a user signs in to a user pool where you assigned migrate user
and pre authentication triggers, they activate both.

| Sign-up, confirmation, and sign-in (authentication) triggers | Trigger                                  | triggerSource value                           | Event |
| ------------------------------------------------------------ | ---------------------------------------- | --------------------------------------------- | ----- |
| Pre sign-up                                                  | `PreSignUp_SignUp`                       | Pre sign-up.                                  |
| Pre sign-up                                                  | `PreSignUp_AdminCreateUser`              | Pre sign-up when an admin creates a new user. |
| Pre sign-up                                                  | `PreSignUp_ExternalProvider`             | Pre sign-up for external identity providers.  |
| Post confirmation                                            | `PostConfirmation_ConfirmSignUp`         | Post sign-up confirmation.                    |
| Post confirmation                                            | `PostConfirmation_ConfirmForgotPassword` | Post Forgot Password confirmation.            |
| Pre authentication                                           | `PreAuthentication_Authentication`       | Pre authentication.                           |
| Post authentication                                          | `PostAuthentication_Authentication`      | Post authentication.                          |

| Custom authentication challenge triggers | Trigger                                      | triggerSource value             | Event |
| ---------------------------------------- | -------------------------------------------- | ------------------------------- | ----- |
| Define auth challenge                    | `DefineAuthChallenge_Authentication`         | Define Auth Challenge.          |
| Create auth challenge                    | `CreateAuthChallenge_Authentication`         | Create Auth Challenge.          |
| Verify auth challenge                    | `VerifyAuthChallengeResponse_Authentication` | Verify Auth Challenge Response. |

| Pre token generation triggers | Trigger                                | triggerSource value                                                                                    | Event |
| ----------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------ | ----- |
| Pre token generation          | `TokenGeneration_HostedAuth`           | Amazon Cognito authenticates the user from your managed login sign-in<br>page.                         |
| Pre token generation          | `TokenGeneration_Authentication`       | User authentication or token refresh complete.                                                         |
| Pre token generation          | `TokenGeneration_NewPasswordChallenge` | Admin creates the user. Amazon Cognito invokes this when the user must change<br>a temporary password. |
| Pre token generation          | `TokenGeneration_AuthenticateDevice`   | End of the authentication of a user device.                                                            |
| Pre token generation          | `TokenGeneration_RefreshTokens`        | User tries to refresh the identity and access tokens.                                                  |

| Migrate user triggers | Trigger                        | triggerSource value                             | Event |
| --------------------- | ------------------------------ | ----------------------------------------------- | ----- |
| User migration        | `UserMigration_Authentication` | User migration at the time of sign-in.          |
| User migration        | `UserMigration_ForgotPassword` | User migration during the forgot-password flow. |

| Custom message triggers | Trigger                             | triggerSource value                                                                                                     | Event |
| ----------------------- | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----- |
| Custom message          | `CustomMessage_SignUp`              | Custom message when a user signs up in your user pool.                                                                  |
| Custom message          | `CustomMessage_AdminCreateUser`     | Custom message when you create a user as an administrator and Amazon Cognito<br>sends them a temporary password.        |
| Custom message          | `CustomMessage_ResendCode`          | Custom message when your existing user requests a new confirmation<br>code.                                             |
| Custom message          | `CustomMessage_ForgotPassword`      | Custom message when your user requests a password reset.                                                                |
| Custom message          | `CustomMessage_UpdateUserAttribute` | Custom message when a user changes their email address or phone<br>number and Amazon Cognito sends a verification code. |
| Custom message          | `CustomMessage_VerifyUserAttribute` | Custom message when a user adds an email address or phone number and<br>Amazon Cognito sends a verification code.       |
| Custom message          | `CustomMessage_Authentication`      | Custom message when a user who has configured SMS MFA signs<br>in.                                                      |

| Custom sender triggers | Trigger                                                                          | triggerSource value                                                                                                                                             | Event |
| ---------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| Custom sender          | `CustomEmailSender_SignUp`<br>`CustomSmsSender_SignUp`                           | When a user signs up in your user pool.                                                                                                                         |
| Custom sender          | `CustomEmailSender_AdminCreateUser`<br>`CustomSmsSender_AdminCreateUser`         | When you create a user as an administrator and Amazon Cognito sends them a<br>temporary password.                                                               |
| Custom sender          | `CustomEmailSender_ForgotPassword`<br>`CustomSmsSender_ForgotPassword`           | When your user requests a password reset.                                                                                                                       |
| Custom sender          | `CustomEmailSender_UpdateUserAttribute`<br>`CustomSmsSender_UpdateUserAttribute` | When a user changes their email address or phone number and Amazon Cognito<br>sends a verification code.                                                        |
| Custom sender          | `CustomEmailSender_VerifyUserAttribute`<br>`CustomSmsSender_VerifyUserAttribute` | When a user adds an email address or phone number and Amazon Cognito sends a<br>verification code.                                                              |
| Custom sender          | `CustomEmailSender_Authentication`<br>`CustomSmsSender_Authentication`           | When a user who has configured SMS or email MFA or OTP signs<br>in.                                                                                             |
| Custom sender          | `CustomEmailSender_AccountTakeOverNotification`                                  | When your threat protection settings take an automated action against<br>a user's sign-in attempt and the action for the risk level includes a<br>notification. |

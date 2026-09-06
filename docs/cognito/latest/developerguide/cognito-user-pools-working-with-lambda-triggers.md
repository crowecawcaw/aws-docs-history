

# Customizing user pool workflows with Lambda triggers
<a name="cognito-user-pools-working-with-lambda-triggers"></a>

Amazon Cognito works with AWS Lambda functions to modify the authentication behavior of your user pool. You can configure your user pool to automatically invoke Lambda functions before their first sign-up, after they complete authentication, and at several stages in between. Your functions can modify the default behavior of your authentication flow, make API requests to modify your user pool or other AWS resources, and communicate with external systems. The code in your Lambda functions is your own. Amazon Cognito sends event data to your function, waits for the function to process the data, and in most cases anticipates a response event that reflects any changes you want to make to the session.

Within the system of request and response events, you can introduce your own authentication challenges, migrate users between your user pool and another identity store, customize messages, and modify JSON web tokens (JWTs).

Lambda triggers can customize the response that Amazon Cognito delivers to your user after they initiate an action in your user pool. For example, you can prevent sign-in by a user who would otherwise succeed. They can also perform runtime operations against your AWS environment, external APIs, databases, or identity stores. The migrate user trigger, for example, can combine external action with a change in Amazon Cognito: you can look up user information in an external directory, then set attributes on a new user based on that external information.

When you have a Lambda trigger assigned to your user pool, Amazon Cognito interrupts its default flow to request information from your function. Amazon Cognito generates a JSON *event* and passes it to your function. The event contains information about your user's request to create a user account, sign in, reset a password, or update an attribute. Your function then has an opportunity to take action, or to send the event back unmodified. An event returned unmodified notifies your user pool to proceed with the default action for the event. For example, your pre sign-up trigger can automatically confirm users for the `PreSignUp_SignUp` trigger source, but return the event unchanged for external and administrator-created users.

The following table summarizes some of the ways you can use Lambda triggers to customize user pool operations:




- ** **Custom Authentication Flow** **
  - **Operation:** Define Auth Challenge / **Description:** Determines the next challenge in a custom auth flow
  - **Operation:** Create Auth Challenge / **Description:** Creates a challenge in a custom auth flow
  - **Operation:** Verify Auth Challenge Response / **Description:** Determines if a response is correct in a custom auth flow

- ****Authentication Events****
  - **Operation:** [Pre authentication Lambda trigger](user-pool-lambda-pre-authentication.md) / **Description:** Custom validation to accept or deny the sign-in request
  - **Operation:** [Post authentication Lambda trigger](user-pool-lambda-post-authentication.md) / **Description:** Logs events for custom analytics
  - **Operation:** [Pre token generation Lambda trigger](user-pool-lambda-pre-token-generation.md) / **Description:** Augments or suppresses token claims

- ****Federation****
  - **Operation:** [Inbound federation Lambda trigger](user-pool-lambda-inbound-federation.md)
  - **Description:** Transforms federated user attributes before user creation or update in Amazon Cognito user pools

- ****Sign-Up****
  - **Operation:** [Pre sign-up Lambda trigger](user-pool-lambda-pre-sign-up.md) / **Description:** Performs custom validation that accepts or denies the sign-up request
  - **Operation:** [Post confirmation Lambda trigger](user-pool-lambda-post-confirmation.md) / **Description:** Adds custom welcome messages or event logging for custom analytics
  - **Operation:** [Migrate user Lambda trigger](user-pool-lambda-migrate-user.md) / **Description:** Migrates a user from an existing user directory to user pools

- ****Messages****
  - **Operation:** [Custom message Lambda trigger](user-pool-lambda-custom-message.md)
  - **Description:** Performs advanced customization and localization of messages

- ****Token Creation****
  - **Operation:** [Pre token generation Lambda trigger](user-pool-lambda-pre-token-generation.md)
  - **Description:** Adds or removes attributes in ID and access tokens

- ****Email and SMS third-party providers****
  - **Operation:** [Custom sender Lambda triggers](user-pool-lambda-custom-sender-triggers.md)
  - **Description:** Uses a third-party provider to send SMS and email messages



**Topics**
+ [Things to know about Lambda triggers](#important-lambda-considerations)
+ [Add a user pool Lambda trigger](#triggers-working-with-lambda)
+ [User pool Lambda trigger event](#cognito-user-pools-lambda-trigger-event-parameter-shared)
+ [User pool Lambda trigger common parameters](#cognito-user-pools-lambda-trigger-syntax-shared)
+ [Client metadata](#working-with-lambda-trigger-client-metadata)
+ [Connecting API operations to Lambda triggers](#lambda-triggers-by-event)
+ [Connecting Lambda triggers to user pool functional operations](#working-with-lambda-trigger-sources)
+ [Pre sign-up Lambda trigger](user-pool-lambda-pre-sign-up.md)
+ [Post confirmation Lambda trigger](user-pool-lambda-post-confirmation.md)
+ [Pre authentication Lambda trigger](user-pool-lambda-pre-authentication.md)
+ [Post authentication Lambda trigger](user-pool-lambda-post-authentication.md)
+ [Inbound federation Lambda trigger](user-pool-lambda-inbound-federation.md)
+ [Custom authentication challenge Lambda triggers](user-pool-lambda-challenge.md)
+ [Pre token generation Lambda trigger](user-pool-lambda-pre-token-generation.md)
+ [Migrate user Lambda trigger](user-pool-lambda-migrate-user.md)
+ [Custom message Lambda trigger](user-pool-lambda-custom-message.md)
+ [Custom sender Lambda triggers](user-pool-lambda-custom-sender-triggers.md)

## Things to know about Lambda triggers
<a name="important-lambda-considerations"></a>

When you are preparing your user pools for Lambda functions, consider the following:
+ The events that Amazon Cognito sends to your Lambda triggers might change with new features. The positions of response and request elements in the JSON hierarchy might change, or element names might be added. In your Lambda function, you can expect to receive the input-element key-value pairs described in this guide, but stricter input validation can cause your functions to fail.
+ You can choose one of multiple versions of the events that Amazon Cognito sends to some triggers. Some versions might require you to accept a change to your Amazon Cognito pricing. For more information about pricing, see [Amazon Cognito Pricing](https://aws.amazon.com/cognito/pricing/). To customize access tokens in a [Pre token generation Lambda trigger](user-pool-lambda-pre-token-generation.md), you must configure your user pool with a feature plan other than *Lite* and update your Lambda trigger configuration to use event version 2.
+ Except for [Custom sender Lambda triggers](user-pool-lambda-custom-sender-triggers.md), Amazon Cognito invokes Lambda functions synchronously. When Amazon Cognito calls your Lambda function, it must respond within 5 seconds. If it doesn't and if the call can be retried, Amazon Cognito may retry the call. If all retry attempts fail, the function times out. You can't change this five-second timeout value. For more information, see [Lambda programming model](https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html) in the AWS Lambda Developer Guide.

  Amazon Cognito doesn't retry function calls that return an [Invoke error](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_Errors) with an HTTP status code of 500-599. These codes indicate a configuration issue that leaves Lambda unable to launch the function. For more information, see [Error handling and automatic retries in AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html).
+ You can't declare a function version in your Lambda trigger configuration. Amazon Cognito user pools invoke the latest version of your function by default. However, you can associate a function version with an alias and set your trigger `LambdaArn` to the alias ARN in a [CreateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.html) or [UpdateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.html) API request. This option isn't available in the AWS Management Console. For more information about aliases, see [Lambda function aliases](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html) in the *AWS Lambda Developer Guide*.
+ If you delete a Lambda trigger, you must update the corresponding trigger in the user pool. For example, if you delete the post authentication trigger, you must set the **Post authentication** trigger in the corresponding user pool to **none**. 
+ If your Lambda function doesn't return the request and response parameters to Amazon Cognito, or returns an error, the authentication event doesn't succeed. You can return an error in your function to prevent a user's sign-up, authentication, token generation, or any other stage of their authentication flow that invokes Lambda trigger.

  Managed login returns errors that Lambda triggers generate as error text above the sign-in prompt. The Amazon Cognito user pools API returns trigger errors in the format `{{[trigger]}} failed with error {{[error text from response]}}`. As a best practice, only generate errors in your Lambda functions that you want your users to see. Use output methods like `print()` to log any sensitive or debugging information to CloudWatch Logs. For an example, see [Pre sign-up example: Deny sign-up if user name has fewer than five characters](user-pool-lambda-pre-sign-up.md#aws-lambda-triggers-pre-registration-example-3).
+ You can add a Lambda function in another AWS account as a trigger for your user pool. You must add cross-account triggers with the [CreateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.html) and [UpdateUserPool](https://docs.aws.amazon.com/) API operations, or their equivalents in CloudFormation and the AWS CLI. You can't add cross-account functions in the AWS Management Console.
+ When you add a Lambda trigger in the Amazon Cognito console, Amazon Cognito adds a resource-based policy to your function that permits your user pool to invoke the function. When you create a Lambda trigger outside of the Amazon Cognito console, including a cross-account function, you must add permissions to the resource-based policy of the Lambda function. Your added permissions must allow Amazon Cognito to invoke the function on behalf of your user pool. You can [add permissions from the Lambda Console](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) or use the Lambda [AddPermission](https://docs.aws.amazon.com/lambda/latest/dg/API_AddPermission.html) API operation.

**Example Lambda Resource-Based Policy**  
The following example Lambda resource-based policy grants Amazon Cognito a limited ability to invoke a Lambda function. Amazon Cognito can only invoke the function when it does so on behalf of both the user pool in the `aws:SourceArn` condition and the account in the `aws:SourceAccount` condition.

------
#### [ JSON ]

****  

  ```
  {
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
              "Resource": "arn:{{aws}}:lambda:{{us-east-1}}:{{111122223333}}:function:{{MyFunction}}",
              "Condition": {
                  "StringEquals": {
                      "AWS:SourceAccount": "{{111122223333}}"
                  },
                  "ArnLike": {
                      "AWS:SourceArn": "arn:{{aws}}:cognito-idp:{{us-east-1}}:{{111122223333}}:userpool/{{us-east-1_EXAMPLE}}"
                  }
              }
          }
      ]
  }
  ```

------

## Add a user pool Lambda trigger
<a name="triggers-working-with-lambda"></a>

**To add a user pool Lambda trigger with the console**

1. Use the [Lambda console](https://console.aws.amazon.com/lambda/home) to create a Lambda function. For more information on Lambda functions, see the [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/).

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home), and then choose **User Pools**.

1. Choose an existing user pool from the list, or [create a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-as-user-directory.html).

1. Choose the **Extensions** menu and locate **Lambda triggers**.

1. Choose **Add a Lambda trigger**.

1. Select a Lambda trigger **Category** based on the stage of authentication that you want to customize.

1. Select **Assign Lambda function** and select a function in the same AWS Region as your user pool.
**Note**  
If your AWS Identity and Access Management (IAM) credentials have permission to update the Lambda function, Amazon Cognito adds a Lambda resource-based policy. With this policy, Amazon Cognito can invoke the function that you select. If the signed-in credentials do not have sufficient IAM permissions, you must update the resource-based policy separately. For more information, see [Things to know about Lambda triggers](#important-lambda-considerations).

1. Choose **Save changes**.

1. You can use CloudWatch in the Lambda console to log your Lambda function . For more information, see [Accessing CloudWatch Logs for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions-logs.html).

## User pool Lambda trigger event
<a name="cognito-user-pools-lambda-trigger-event-parameter-shared"></a>

Amazon Cognito passes event information to your Lambda function. The Lambda function returns the same event object back to Amazon Cognito with any changes in the response. If your function returns the input event without modification, Amazon Cognito proceed with default behavior. The following shows the parameters that are common to all Lambda trigger input events. For trigger-specific event syntax, review the event schema on the section of this guide for each trigger.

------
#### [ JSON ]

```
{
    "version": "{{string}}",
    "triggerSource": "{{string}}",
    "region": {{AWSRegion}},
    "userPoolId": "{{string}}",
    "userName": "{{string}}",
    "callerContext": 
        {
            "awsSdkVersion": "{{string}}",
            "clientId": "{{string}}"
        },
    "request":
        {
            "userAttributes": {
                "{{string}}": "{{string}}",
                ....
            }
        },
    "response": {}
}
```

------

## User pool Lambda trigger common parameters
<a name="cognito-user-pools-lambda-trigger-syntax-shared"></a>

**version**  
The version number of your Lambda function.

**triggerSource**  
The name of the event that triggered the Lambda function. For a description of each triggerSource see [Connecting Lambda triggers to user pool functional operations](#working-with-lambda-trigger-sources).

**region**  
The AWS Region as an `AWSRegion` instance.

**userPoolId**  
The ID of the user pool.

**userName**  
The current user's username.

**callerContext**  
Metadata about the request and the code environment. It contains the fields **awsSdkVersion** and **clientId**.    
**awsSdkVersion**  
The version of the AWS SDK that generated the request.  
****clientId****  
The ID of the user pool app client.

**request**  
Details of your user's API request. It includes the following fields, and any request parameters that are particular to the trigger. For example, an event that Amazon Cognito sends to a pre-authentication trigger will also contain a `userNotFound` parameter. You can process the value of this parameter to take a custom action when your user tries to sign in with an unregistered username.    
**userAttributes**  
One or more key-value pairs of user attribute names and values, for example `"email": "john@example.com"`.

**response**  
This parameter doesn't contain any information in the original request. Your Lambda function must return the entire event to Amazon Cognito, and add any return parameters to the `response`. To see what return parameters your function can include, refer to the documentation for the trigger that you want to use.

## Client metadata
<a name="working-with-lambda-trigger-client-metadata"></a>

You can submit custom parameters to your Lambda trigger functions in API operations and [Token endpoint](token-endpoint.md) requests. With client metadata, your application can collect additional information about the environment where requests originate. When you pass client metadata to your Lambda functions, they can process the additional data and make use of it in logging or customization of authentication flows. Client metadata is string pairs of your choosing and design in a JSON key-value format.

**Client metadata example use cases**
+ Pass geolocation data at sign-up to the [pre sign-up trigger](user-pool-lambda-pre-sign-up.md) and prevent sign-in from unwanted locations.
+ Pass tenant ID data to [custom challenge triggers](user-pool-lambda-challenge.md) and issue different challenges to customers from different business units.
+ Pass a user's token to the [pre token generation trigger](user-pool-lambda-pre-token-generation.md) and generate a log of the principal that an M2M request was made on behalf of. For an example request, see [Client credentials with basic authorization](token-endpoint.md#exchanging-client-credentials-for-an-access-token-in-request-body).

Here is an example of passing client metadata to the pre sign-up trigger.

------
#### [ SignUp request ]

The following is an example [SignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html#CognitoUserPools-SignUp-request-ValidationData) request with client metadata that Amazon Cognito passes to a pre sign-up trigger.

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

------
#### [ Lambda trigger input event ]

The request results in the following request body to your pre sign-up function.

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

------

**Client metadata for machine-to-machine (M2M) client credentials**  
You can pass [client metadata](#working-with-lambda-trigger-client-metadata) in M2M requests. Client metadata is additional information from a user or application environment that can contribute to the outcomes of a [Pre token generation Lambda trigger](user-pool-lambda-pre-token-generation.md). In authentication operations with a user principal, you can pass client metadata to the pre token generation trigger in the body of [AdminRespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.html) and [RespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.html) API requests. Because applications conduct the flow for generation of access tokens for M2M with direct requests to the [Token endpoint](token-endpoint.md), they have a different model. In the POST body of token requests for client credentials, pass an `aws_client_metadata` parameter with the client metadata object URL-encoded (`x-www-form-urlencoded`) to string. For an example request, see [Client credentials with basic authorization](token-endpoint.md#exchanging-client-credentials-for-an-access-token-in-request-body). The following is an example parameter that passes the key-value pairs `{"environment": "dev", "language": "en-US"}`.

```
aws_client_metadata=%7B%22environment%22%3A%20%22dev%22,%20%22language%22%3A%20%22en-US%22%7D
```

**Temporary user attributes: `validationData`**  
Some authentication operations also have a `validationData` parameter. Like client metadata, this is an opportunity to pass external information that Amazon Cognito doesn't automatically gather to Lambda triggers. The validation data field is intended to provide your Lambda function witth additional user context in sign-up and sign-in operations. [SignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html#CognitoUserPools-SignUp-request-ValidationData) and [AdminCreateUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.html#CognitoUserPools-AdminCreateUser-request-ValidationData) pass `validationData` to the [pre sign-up trigger](user-pool-lambda-pre-sign-up.md). [InitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html#CognitoUserPools-InitiateAuth-request-ClientMetadata) and [AdminInitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.html#CognitoUserPools-AdminInitiateAuth-request-ClientMetadata) pass `ClientMetadata` in the API request body as `validationData` in the input event to the [pre authentication](user-pool-lambda-pre-authentication.md) and [migrate user](user-pool-lambda-migrate-user.md) triggers.

To map API operations to the functions that they can pass client metadata to, refer to the trigger source sections that follow.

## Connecting API operations to Lambda triggers
<a name="lambda-triggers-by-event"></a>

The following sections describe the Lambda triggers that Amazon Cognito invokes from the activity in your user pool.

When your app signs in users through the Amazon Cognito user pools API, managed login, or user pool endpoints, Amazon Cognito invokes your Lambda functions based on the session context. For more information about the Amazon Cognito user pools API and user pool endpoints, see [Understanding API, OIDC, and managed login pages authentication](authentication-flows-public-server-side.md#user-pools-API-operations). The tables in the sections that follow describe events that cause Amazon Cognito to invoke a function, and the `triggerSource` string that Amazon Cognito includes in the request.

**Topics**
+ [Lambda triggers in the Amazon Cognito API](#lambda-triggers-native-users-native-api)
+ [Lambda triggers for Amazon Cognito local users in managed login](#lambda-triggers-native-users-hosted-UI)
+ [Lambda triggers for federated users](#lambda-triggers-for-federated-users)

### Lambda triggers in the Amazon Cognito API
<a name="lambda-triggers-native-users-native-api"></a>

The following table describes the source strings for the Lambda triggers that Amazon Cognito can invoke when your app creates, signs in, or updates a local user.


**Local user trigger sources in the Amazon Cognito API**  


- ** [AdminCreateUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.html) **
  - **Lambda trigger:** Pre sign-up / **Trigger source:** `PreSignUp_AdminCreateUser`
  - **Lambda trigger:** Pre token generation / **Trigger source:** `TokenGeneration_NewPasswordChallenge`
  - **Lambda trigger:** Custom message / **Trigger source:** `CustomMessage_AdminCreateUser`
  - **Lambda trigger:** Custom email sender / **Trigger source:** `CustomEmailSender_AdminCreateUser`
  - **Lambda trigger:** Custom SMS sender / **Trigger source:** `CustomSMSSender_AdminCreateUser`

- ** [SignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html) **
  - **Lambda trigger:** Pre sign-up / **Trigger source:** `PreSignUp_SignUp`
  - **Lambda trigger:** Custom message / **Trigger source:** `CustomMessage_SignUp`
  - **Lambda trigger:** Custom email sender / **Trigger source:** `CustomEmailSender_SignUp`
  - **Lambda trigger:** Custom SMS sender / **Trigger source:** `CustomSMSSender_SignUp`

- ** [ConfirmSignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmSignUp.html) [AdminConfirmSignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminConfirmSignUp.html) **
  - **Lambda trigger:** Post confirmation
  - **Trigger source:** `PostConfirmation_ConfirmSignUp`

- ** [InitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html) [AdminInitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.html) **
  - **Lambda trigger:** Pre authentication / **Trigger source:** `PreAuthentication_Authentication`
  - **Lambda trigger:** Post authentication / **Trigger source:** `PostAuthentication_Authentication`
  - **Lambda trigger:** Define auth challenge / **Trigger source:** `DefineAuthChallenge_Authentication`
  - **Lambda trigger:** Create auth challenge / **Trigger source:** `CreateAuthChallenge_Authentication`
  - **Lambda trigger:** Verify auth challenge / **Trigger source:** `VerifyAuthChallenge_Authentication`
  - **Lambda trigger:** Pre token generation / **Trigger source:** `TokenGeneration_Authentication`<br />`TokenGeneration_AuthenticateDevice`<br />`TokenGeneration_RefreshTokens`
  - **Lambda trigger:** Migrate user / **Trigger source:** `UserMigration_Authentication`
  - **Lambda trigger:** Custom message / **Trigger source:** `CustomMessage_Authentication`
  - **Lambda trigger:** Custom email sender / **Trigger source:** `CustomEmailSender_AccountTakeOverNotification`<br />`CustomEmailSender_Authentication`
  - **Lambda trigger:** Custom SMS sender / **Trigger source:** `CustomSMSSender_Authentication`

- ** [RespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.html) [AdminRespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.html) **
  - **Lambda trigger:** Post authentication / **Trigger source:** `PostAuthentication_Authentication`
  - **Lambda trigger:** Define auth challenge / **Trigger source:** `DefineAuthChallenge_Authentication`
  - **Lambda trigger:** Create auth challenge / **Trigger source:** `CreateAuthChallenge_Authentication`
  - **Lambda trigger:** Verify auth challenge / **Trigger source:** `VerifyAuthChallenge_Authentication`
  - **Lambda trigger:** Pre token generation / **Trigger source:** `TokenGeneration_Authentication`<br />`TokenGeneration_AuthenticateDevice`<br />`TokenGeneration_RefreshTokens`
  - **Lambda trigger:** Custom message / **Trigger source:** `CustomMessage_Authentication`
  - **Lambda trigger:** Custom email sender / **Trigger source:** `CustomEmailSender_AccountTakeOverNotification`<br />`CustomEmailSender_Authentication`
  - **Lambda trigger:** Custom SMS sender / **Trigger source:** `CustomSMSSender_Authentication`

- ** [ForgotPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.html) **
  - **Lambda trigger:** Migrate user / **Trigger source:** `UserMigration_ForgotPassword`
  - **Lambda trigger:** Custom message / **Trigger source:** `CustomMessage_ForgotPassword`
  - **Lambda trigger:** Custom email sender / **Trigger source:** `CustomEmailSender_ForgotPassword`
  - **Lambda trigger:** Custom SMS sender / **Trigger source:** `CustomSMSSender_ForgotPassword`

- ** [ConfirmForgotPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmForgotPassword.html) **
  - **Lambda trigger:** Post confirmation
  - **Trigger source:** `PostConfirmation_ConfirmForgotPassword`

- ** [UpdateUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.html) [AdminUpdateUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.html) **
  - **Lambda trigger:** Custom message / **Trigger source:** `CustomMessage_UpdateUserAttribute`
  - **Lambda trigger:** Custom email sender / **Trigger source:** `CustomEmailSender_UpdateUserAttribute`
  - **Lambda trigger:** Custom SMS sender / **Trigger source:** `CustomSMSSender_UpdateUserAttribute`

- ** [VerifyUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_VerifyUserAttributes.html) **
  - **Lambda trigger:** Custom message / **Trigger source:** `CustomMessage_VerifyUserAttribute`
  - **Lambda trigger:** Custom email sender / **Trigger source:** `CustomEmailSender_VerifyUserAttribute`
  - **Lambda trigger:** Custom SMS sender / **Trigger source:** `CustomSMSSender_VerifyUserAttribute`

- ** [GetTokensFromRefreshToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.html) **
  - **Lambda trigger:** Pre token generation
  - **Trigger source:** `TokenGeneration_Authentication`



### Lambda triggers for Amazon Cognito local users in managed login
<a name="lambda-triggers-native-users-hosted-UI"></a>

The following table describes the source strings for the Lambda triggers that Amazon Cognito can invoke when a local user signs in to your user pool with managed login.


**Local user trigger sources in managed login**  


- **`/signup`**
  - **Lambda trigger:** Pre sign-up / **Trigger source:** `PreSignUp_SignUp`
  - **Lambda trigger:** Custom message / **Trigger source:** `CustomMessage_SignUp`
  - **Lambda trigger:** Custom email sender / **Trigger source:** `CustomEmailSender_SignUp`
  - **Lambda trigger:** Custom SMS sender / **Trigger source:** `CustomSMSSender_SignUp`

- **`/confirmuser`**
  - **Lambda trigger:** Post confirmation
  - **Trigger source:** `PostConfirmation_ConfirmSignUp`

- **`/login`**
  - **Lambda trigger:** Pre authentication / **Trigger source:** `PreAuthentication_Authentication`
  - **Lambda trigger:** Pre token generation / **Trigger source:** `TokenGeneration_Authentication`<br />`TokenGeneration_AuthenticateDevice`<br />`TokenGeneration_RefreshTokens`
  - **Lambda trigger:** Migrate user / **Trigger source:** `UserMigration_Authentication`
  - **Lambda trigger:** Custom message / **Trigger source:** `CustomMessage_Authentication`
  - **Lambda trigger:** Custom email sender / **Trigger source:** `CustomEmailSender_AccountTakeOverNotification`<br />`CustomEmailSender_Authentication`
  - **Lambda trigger:** Custom SMS sender / **Trigger source:** `CustomSMSSender_Authentication`

- **`/forgotpassword`**
  - **Lambda trigger:** Migrate user / **Trigger source:** `UserMigration_ForgotPassword`
  - **Lambda trigger:** Custom message / **Trigger source:** `CustomMessage_ForgotPassword`
  - **Lambda trigger:** Custom email sender / **Trigger source:** `CustomEmailSender_ForgotPassword`
  - **Lambda trigger:** Custom SMS sender / **Trigger source:** `CustomSMSSender_ForgotPassword`

- **`/confirmforgotpassword`**
  - **Lambda trigger:** Post confirmation
  - **Trigger source:** `PostConfirmation_ConfirmForgotPassword`



### Lambda triggers for federated users
<a name="lambda-triggers-for-federated-users"></a>

You can use the following Lambda triggers to customize your user pool workflows for users who sign in with a federated provider. 

**Note**  
Federated users can use managed login to sign in, or you can generate a request to the [Authorize endpoint](authorization-endpoint.md) that silently redirects them to their identity provider sign-in page. You can't sign in federated users with the Amazon Cognito user pools API.


**Federated user trigger sources**  


- **First sign-in**
  - **Lambda trigger:** Pre sign-up / **Trigger source:** `PreSignUp_ExternalProvider`
  - **Lambda trigger:** Post confirmation / **Trigger source:** `PostConfirmation_ConfirmSignUp`
  - **Lambda trigger:** Pre token generation / **Trigger source:** `TokenGeneration_HostedAuth`

- **Subsequent sign-ins**
  - **Lambda trigger:** Pre authentication / **Trigger source:** `PreAuthentication_Authentication`
  - **Lambda trigger:** Post authentication / **Trigger source:** `PostAuthentication_Authentication`
  - **Lambda trigger:** Pre token generation / **Trigger source:** `TokenGeneration_HostedAuth`



Federated sign-in does not invoke any [Custom authentication challenge Lambda triggers](user-pool-lambda-challenge.md), [Migrate user Lambda trigger](user-pool-lambda-migrate-user.md), [Custom message Lambda trigger](user-pool-lambda-custom-message.md), or [Custom sender Lambda triggers](user-pool-lambda-custom-sender-triggers.md) in your user pool.

## Connecting Lambda triggers to user pool functional operations
<a name="working-with-lambda-trigger-sources"></a>

Each Lambda trigger serves a functional role in your user pool. For example, a trigger can modify your sign-up flow, or add a custom authentication challenge. The event that Amazon Cognito sends to a Lambda function can reflect one of multiple actions that make up that functional role. For example, Amazon Cognito invokes a pre sign-up trigger when your user signs up, and when you create a user. Each of these different cases for the same functional role has its own `triggerSource` value. Your Lambda function can process incoming events differently based on the operation that invoked it.

Amazon Cognito also invokes all assigned functions when an event corresponds to a trigger source. For example, when a user signs in to a user pool where you assigned migrate user and pre authentication triggers, they activate both.


**Sign-up, confirmation, and sign-in (authentication) triggers**  

| Trigger | triggerSource value | Event | 
| --- | --- | --- | 
| Pre sign-up | PreSignUp\_SignUp | Pre sign-up. | 
| Pre sign-up | PreSignUp\_AdminCreateUser | Pre sign-up when an admin creates a new user. | 
| Pre sign-up | PreSignUp\_ExternalProvider | Pre sign-up for external identity providers. | 
| Post confirmation | PostConfirmation\_ConfirmSignUp | Post sign-up confirmation. | 
| Post confirmation | PostConfirmation\_ConfirmForgotPassword | Post Forgot Password confirmation. | 
| Pre authentication | PreAuthentication\_Authentication | Pre authentication. | 
| Post authentication | PostAuthentication\_Authentication | Post authentication. | 


**Custom authentication challenge triggers**  

| Trigger | triggerSource value | Event | 
| --- | --- | --- | 
| Define auth challenge | DefineAuthChallenge\_Authentication | Define Auth Challenge. | 
| Create auth challenge | CreateAuthChallenge\_Authentication | Create Auth Challenge. | 
| Verify auth challenge | VerifyAuthChallengeResponse\_Authentication | Verify Auth Challenge Response. | 


**Federation triggers**  

| Trigger | triggerSource value | Event | 
| --- | --- | --- | 
| Inbound federation | InboundFederation\_ExternalProvider | Inbound federation. | 


**Pre token generation triggers**  

| Trigger | triggerSource value | Event | 
| --- | --- | --- | 
| Pre token generation | TokenGeneration\_HostedAuth |  Amazon Cognito authenticates the user from your managed login sign-in page. | 
| Pre token generation | TokenGeneration\_Authentication | User authentication or token refresh complete. | 
| Pre token generation | TokenGeneration\_NewPasswordChallenge | Admin creates the user. Amazon Cognito invokes this when the user must change a temporary password. | 
| Pre token generation | TokenGeneration\_AuthenticateDevice | End of the authentication of a user device. | 
| Pre token generation | TokenGeneration\_RefreshTokens | User tries to refresh the identity and access tokens. | 


**Migrate user triggers**  

| Trigger | triggerSource value | Event | 
| --- | --- | --- | 
| User migration | UserMigration\_Authentication | User migration at the time of sign-in. | 
| User migration | UserMigration\_ForgotPassword | User migration during the forgot-password flow. | 


**Custom message triggers**  

| Trigger | triggerSource value | Event | 
| --- | --- | --- | 
| Custom message | CustomMessage\_SignUp | Custom message when a user signs up in your user pool. | 
| Custom message | CustomMessage\_AdminCreateUser | Custom message when you create a user as an administrator and Amazon Cognito sends them a temporary password. | 
| Custom message | CustomMessage\_ResendCode | Custom message when your existing user requests a new confirmation code. | 
| Custom message | CustomMessage\_ForgotPassword | Custom message when your user requests a password reset. | 
| Custom message | CustomMessage\_UpdateUserAttribute | Custom message when a user changes their email address or phone number and Amazon Cognito sends a verification code. | 
| Custom message | CustomMessage\_VerifyUserAttribute | Custom message when a user adds an email address or phone number and Amazon Cognito sends a verification code. | 
| Custom message | CustomMessage\_Authentication | Custom message when a user who has configured SMS MFA signs in. | 


**Custom sender triggers**  

| Trigger | triggerSource value | Event | 
| --- | --- | --- | 
| Custom sender | `CustomEmailSender_SignUp`<br />`CustomSmsSender_SignUp` | When a user signs up in your user pool. | 
| Custom sender | `CustomEmailSender_AdminCreateUser`<br />`CustomSmsSender_AdminCreateUser` | When you create a user as an administrator and Amazon Cognito sends them a temporary password. | 
| Custom sender | `CustomEmailSender_ForgotPassword`<br />`CustomSmsSender_ForgotPassword` | When your user requests a password reset. | 
| Custom sender | `CustomEmailSender_UpdateUserAttribute`<br />`CustomSmsSender_UpdateUserAttribute` | When a user changes their email address or phone number and Amazon Cognito sends a verification code. | 
| Custom sender | `CustomEmailSender_VerifyUserAttribute`<br />`CustomSmsSender_VerifyUserAttribute` | When a user adds an email address or phone number and Amazon Cognito sends a verification code. | 
| Custom sender | `CustomEmailSender_Authentication`<br />`CustomSmsSender_Authentication` | When a user who has configured SMS or email MFA or OTP signs in. | 
| Custom sender | CustomEmailSender\_AccountTakeOverNotification | When your threat protection settings take an automated action against a user's sign-in attempt and the action for the risk level includes a notification. | 
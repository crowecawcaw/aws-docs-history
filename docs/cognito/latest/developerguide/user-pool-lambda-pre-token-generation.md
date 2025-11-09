# Pre token generation Lambda

trigger

Because Amazon Cognito invokes this trigger before token generation, you can customize the
claims in user pool tokens. With the **Basic features** of the version one
or `V1_0` pre token generation trigger event, you can customize the identity (ID)
token. In user pools with the Essentials or Plus feature plan, you can generate the version
two or `V2_0` trigger event with access token customization, and the version
three or `V3_0` trigger event with access token customization for
machine-to-machine (M2M) client-credentials grants.

Amazon Cognito sends a `V1_0` event as a request to your function with data that it
would write to the ID token. A `V2_0` or `V3_0` event is a single
request with the data that Amazon Cognito would write to both the identity and access tokens. To
customize both tokens, you must update your function to use trigger version two or three,
and send data for both tokens in the same response.

Amazon Cognito applies version two event responses to access tokens from user authentication, where
a human user has presented credentials to your user pool. Version three event responses
apply to access tokens from user authentication and machine authentication, where automated
systems authorize access token requests with app client secrets. Aside from the
circumstances of the resulting access tokens, version two and three events are
identical.

This Lambda trigger can add, remove, and modify some claims in identity and access tokens
before Amazon Cognito issues them to your app. To use this feature, associate a Lambda function from
the Amazon Cognito user pools console or update your user pool `LambdaConfig` through the AWS Command Line Interface
(AWS CLI).

## Event

versions

Your user pool can deliver different versions of a pre token generation trigger event
to your Lambda function. A `V1_0` trigger delivers the parameters for
modification of ID tokens. A `V2_0` or `V3_0` trigger delivers
parameters for the following.

1. The functions of a `V1_0` trigger.
2. The ability to customize access tokens.
3. The ability to pass complex datatypes to ID and access token claim
   values:
   - String
   - Number
   - Boolean
   - Array of strings, numbers, booleans, or a combination of any of
     these
   - JSON

###### Note

In the ID token, you can populate complex objects to the values of claims except
for `phone_number_verified`, `email_verified`,
`updated_at`, and `address`.

User pools deliver `V1_0` events by default. To configure your user pool to
send a `V2_0` event, choose a **Trigger event
version** of **Basic features + access token
customization for user identities** when you configure your trigger in the
Amazon Cognito console. To produce `V3_0` events, choose \***\*Basic features + access token customization for user and machine
identities\*\***. You can also set the value of
`LambdaVersion` in the [LambdaConfig](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md#CognitoUserPools-UpdateUserPool-request-LambdaConfig "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md#CognitoUserPools-UpdateUserPool-request-LambdaConfig") parameters in an [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md") or [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") API request. Event versions one, two,
and three are available in the **Essentials** and
**Plus** feature plans. M2M operations for version three events
have a pricing structure separate from the monthly active users (MAU) formula. For more
information, see [Amazon Cognito
Pricing](https://aws.amazon.com/cognito/pricing/ "https://aws.amazon.com/cognito/pricing/").

###### Note

User pools that were operational with the **Advanced security
features** option on or before November 22, 2024 at 1800 GMT, and that
remain on the **Lite** feature tier have access to event versions
one and two of the pre token generation trigger. User pools in this legacy tier
_without_ advanced security features have
access to event version one. Version three is _only_ available in Essentials and Plus.

## Claims and

scopes reference

Amazon Cognito limits the claims and scopes that you can add, modify, or suppress in access and
identity tokens. The following table describes the claims that your Lambda function can
and can't modify, and the trigger event parameters that affect the presence or value of
the claim.

| Claim                                                             | Default token type | Can add? | Can modify? | Can suppress? | Event parameter<br>• add or modify | Event parameter<br>• suppress                                                                          | Identity type                                                                                       | Event version                                                                                 |
| ----------------------------------------------------------------- | ------------------ | -------- | ----------- | ------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Any claim not in the user pool token schema                       | None               | Yes      | Yes         | N/A           | `claimsToAddOrOverride`            | `claimsToSuppress`                                                                                     | User, machine[1](#cognito-pretoken-machine-ids-tier-note "#cognito-pretoken-machine-ids-tier-note") | All[2](#cognito-pretoken-id-access-versions-note "#cognito-pretoken-id-access-versions-note") |
| `scope`                                                           | Access             | Yes      | Yes         | Yes           | `scopesToAdd`                      | `scopesToSuppress`                                                                                     | User, machine[1](#cognito-pretoken-machine-ids-tier-note "#cognito-pretoken-machine-ids-tier-note") | `v2_0`, `v3_0`                                                                                |
| `cognito:groups`                                                  | ID, Access         | Yes      | Yes         | Yes           | `groupsToOverride`                 | `claimsToSuppress`                                                                                     | User                                                                                                | All[2](#cognito-pretoken-id-access-versions-note "#cognito-pretoken-id-access-versions-note") |
| `cognito:preferred_role`                                          | ID                 | Yes      | Yes         | Yes           | `preferredRole`                    | `claimsToSuppress`[3](#cognito-pretoken-suppress-groups-note "#cognito-pretoken-suppress-groups-note") | User                                                                                                | All                                                                                           |
| `cognito:roles`                                                   | ID                 | Yes      | Yes         | Yes           | `iamRolesToOverride`               | `claimsToSuppress`[3](#cognito-pretoken-suppress-groups-note "#cognito-pretoken-suppress-groups-note") | User                                                                                                | All                                                                                           |
| `cognito:username`                                                | ID                 | No       | No          | No            | N/A                                | N/A                                                                                                    | User                                                                                                | N/A                                                                                           |
| Any other claim with a `cognito:` prefix                          | None               | No       | No          | No            | N/A                                | N/A                                                                                                    | N/A                                                                                                 | N/A                                                                                           |
| `username`                                                        | Access             | No       | No          | No            | N/A                                | N/A                                                                                                    | User                                                                                                | `v2_0`, `v3_0`                                                                                |
| `sub`                                                             | ID, Access         | No       | No          | No            | N/A                                | N/A                                                                                                    | User                                                                                                | N/A                                                                                           |
| standard OIDC attribute                                           | ID                 | Yes      | Yes         | Yes           | `claimsToAddOrOverride`            | `claimsToSuppress`                                                                                     | User                                                                                                | All                                                                                           |
| `custom:` attribute                                               | ID                 | Yes      | Yes         | Yes           | `claimsToAddOrOverride`            | `claimsToSuppress`                                                                                     | User                                                                                                | All                                                                                           |
| `dev:` attribute                                                  | ID                 | No       | No          | Yes           | N/A                                | `claimsToSuppress`                                                                                     | User                                                                                                | All                                                                                           |
| `identities`                                                      | ID                 | No       | No          | No            | N/A                                | N/A                                                                                                    | User                                                                                                | N/A                                                                                           |
| `aud`[4](#cognito-pretoken-aud-note "#cognito-pretoken-aud-note") | ID                 | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |
| `client_id`                                                       | Access             | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |
| `event_id`                                                        | Access             | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |
| `device_key`                                                      | Access             | No       | No          | No            | N/A                                | N/A                                                                                                    | User                                                                                                | N/A                                                                                           |
| `version`                                                         | Access             | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |
| `acr`                                                             | ID, Access         | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |
| `amr`                                                             | ID, Access         | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |
| `at_hash`                                                         | ID                 | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |
| `auth_time`                                                       | ID, Access         | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |
| `azp`                                                             | ID, Access         | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |
| `exp`                                                             | ID, Access         | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |
| `iat`                                                             | ID, Access         | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |
| `iss`                                                             | ID, Access         | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |
| `jti`                                                             | ID, Access         | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |
| `nbf`                                                             | ID, Access         | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |
| `nonce`                                                           | ID, Access         | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |
| `origin_jti`                                                      | ID, Access         | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |
| `token_use`                                                       | ID, Access         | No       | No          | No            | N/A                                | N/A                                                                                                    | User, machine                                                                                       | N/A                                                                                           |

1 Access tokens for machine identities are only available
with `v3_0` of the trigger input event. Event version three is only available
in the **Essentials** and **Plus** feature tiers. User
pools on the **Lite** tier can receive `v1_0` events. User
pools on the **Lite** tier with advanced security features can receive
`v1_0` and `v2_0` events.

2 Configure your pre token generation trigger to event
version `v1_0` for ID token only, `v2_0` for ID and access token,
`v3_0` for ID and access token with capabilities for machine
identities.

3 To suppress the `cognito:preferred_role` and
`cognito:roles` claims, add `cognito:groups` to
`claimsToSuppress`.

4 You can add an `aud` claim to access tokens, but
its value must match the app client ID of the current session. You can derive the client
ID in the request event from `event.callerContext.clientId`.

## Customizing the identity

token

With all event versions of the pre token generation Lambda trigger, you can customize
the content of an identity (ID) token from your user pool. The ID token provides user
attributes from a trusted identity source for sign-in to a web or mobile app. For more
information about ID tokens, see [Understanding the identity (ID)
token](amazon-cognito-user-pools-using-the-id-token.md "amazon-cognito-user-pools-using-the-id-token.md").

The uses of the pre token generation Lambda trigger with an ID token include the
following.

- Make a change at runtime to the IAM role that your user requests from an
  identity pool.
- Add user attributes from an external source.
- Add or replace existing user attribute values.
- Suppress disclosure of user attributes that, because of your user's authorized
  scopes and the read access to attributes that you granted to your app client,
  would otherwise be passed to your app.

## Customizing the

access token

With event versions two and three of the pre token generation Lambda trigger, you can
customize the content of an access token from your user pool. The access token
authorizes users to retrieve information from access-protected resources like Amazon Cognito
token-authorized API operations and third-party APIs. For machine-to-machine (M2M)
authorization with a client credentials grant, Amazon Cognito only invokes the pre token
generation trigger when your user pool is configured for a version three
(`V3_0`) event. For more information about access tokens, see [Understanding the access
token](amazon-cognito-user-pools-using-the-access-token.md "amazon-cognito-user-pools-using-the-access-token.md").

The uses of the pre token generation Lambda trigger with an access token include the
following.

- Add or suppress scopes in the `scope` claim. For example, you can
  add scopes to an access token that resulted from Amazon Cognito user pools API authentication,
  which only assigns the scope `aws.cognito.signin.user.admin`.
- Change a user's membership in user pool groups.
- Add claims that aren't already present in an Amazon Cognito access token.
- Suppress disclosure of claims that would otherwise be passed to your
  app.

To support access customization in your user pool, you must configure the user pool to
generate an updated version of the trigger request. Update your user pool as shown in
the following procedure.

AWS Management Console

###### To support access token customization in a pre token generation Lambda

trigger

1. Go to the [Amazon Cognito
   console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"), and then choose **User
   Pools**.
2. Choose an existing user pool from the list, or [create a user pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md").
3. Choose the **Extensions** menu and locate
   **Lambda triggers**.
4. Add or edit a **Pre token generation
   trigger**.
5. Choose a Lambda function under **Assign Lambda
   function**.
6. Choose a **Trigger event version** of
   **Basic features + access token customization for user
   identities** or **Basic features + access token
   customization for user and machine identities**. This
   setting updates the request parameters that Amazon Cognito sends to your
   function to include fields for access token customization.

User pools API
**To support access token customization in a pre token
generation Lambda trigger**

Generate a [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") or [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md") API request. You must
specify a value for all parameters that you don't want set to a default
value. For more information, see [Updating user pool and app client
configuration](cognito-user-pool-updating.md "cognito-user-pool-updating.md").

Include the following content in the `LambdaVersion` parameter
of your request. A `LambdaVersion` value of `V2_0`
causes your user pool to add parameters for, and apply changes to, access
tokens. A `LambdaVersion` value of `V3_0` produces the
same event as `V2_0`, but causes your user pool to _also_ apply changes to M2M access tokens. To
invoke a specific function version, use a Lambda function ARN with a function
version as the value of `LambdaArn`.

```
"PreTokenGenerationConfig": {
   "LambdaArn": "`arn:aws:lambda:us-west-2:123456789012:function:MyFunction`",
   **"LambdaVersion": "`V3_0`"**
},
```

###### Client metadata for machine-to-machine (M2M) client credentials

You can pass [client
metadata](cognito-user-pools-working-with-lambda-triggers.md#working-with-lambda-trigger-client-metadata "cognito-user-pools-working-with-lambda-triggers.md#working-with-lambda-trigger-client-metadata") in M2M requests. Client metadata is additional information from a
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

###### More resources

- [How to customize access tokens in Amazon Cognito user pools](https://aws.amazon.com/blogs/security/how-to-customize-access-tokens-in-amazon-cognito-user-pools/ "https://aws.amazon.com/blogs/security/how-to-customize-access-tokens-in-amazon-cognito-user-pools/")

###### Topics

- [Pre token
  generation Lambda trigger sources](#user-pool-lambda-pre-token-generation-trigger-source "#user-pool-lambda-pre-token-generation-trigger-source")
- [Pre
  token generation Lambda trigger parameters](#cognito-user-pools-lambda-trigger-syntax-pre-token-generation "#cognito-user-pools-lambda-trigger-syntax-pre-token-generation")
- [Pre token trigger event version two example: Add and suppress claims, scopes, and
  groups](#aws-lambda-triggers-pre-token-generation-example-version-2-overview "#aws-lambda-triggers-pre-token-generation-example-version-2-overview")
- [Pre token generation event version two example: Add claims with complex
  objects](#aws-lambda-triggers-pre-token-generation-example-version-2-complex-objects "#aws-lambda-triggers-pre-token-generation-example-version-2-complex-objects")
- [Pre token
  generation event version one example: Add a new claim and suppress an existing
  claim](#aws-lambda-triggers-pre-token-generation-version-1-add-claim "#aws-lambda-triggers-pre-token-generation-version-1-add-claim")
- [Pre
  token generation event version one example: Modify the user's group
  membership](#aws-lambda-triggers-pre-token-generation-version-1-change-group "#aws-lambda-triggers-pre-token-generation-version-1-change-group")

## Pre token

generation Lambda trigger sources

| triggerSource value                    | Event                                                                                                                    |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `TokenGeneration_HostedAuth`           | Called during authentication from the Amazon Cognito managed login sign-in<br>page.                                      |
| `TokenGeneration_Authentication`       | Called after user authentication flows have completed.                                                                   |
| `TokenGeneration_NewPasswordChallenge` | Called after the user is created by an admin. This flow is invoked<br>when the user has to change a temporary password.  |
| `TokenGeneration_ClientCredentials`    | Called after an M2M client credentials grant. Your user pool only<br>sends this event when your event version is `V3_0`. |
| `TokenGeneration_AuthenticateDevice`   | Called at the end of the authentication of a user device.                                                                |
| `TokenGeneration_RefreshTokens`        | Called when a user tries to refresh the identity and access<br>tokens.                                                   |

## Pre

token generation Lambda trigger parameters

The request that Amazon Cognito passes to this Lambda function is a combination of the parameters below and the
[common parameters](cognito-user-pools-working-with-lambda-triggers.md#cognito-user-pools-lambda-trigger-syntax-shared "cognito-user-pools-working-with-lambda-triggers.md#cognito-user-pools-lambda-trigger-syntax-shared") that Amazon Cognito adds to all requests. When you add a pre token generation Lambda trigger to your user pool, you can
choose a trigger version. This version determines whether Amazon Cognito passes a request to your
Lambda function with additional parameters for access-token customization.

Version one
The version one token can set group membership, IAM roles, and new
claims in ID tokens. Group membership overrides also apply to the
`cognito:groups` claim in access tokens.

```
{
    "request": {
        "userAttributes": {"string": "string"},
        "groupConfiguration": {
                "groupsToOverride": [
                    "string",
                    "string"
                ],
                "iamRolesToOverride": [
                    "string",
                    "string"
                ],
                "preferredRole": "string"
        },
        "clientMetadata": {"string": "string"}
    },
    "response": {
        "claimsOverrideDetails": {
            "claimsToAddOrOverride": {"string": "string"},
            "claimsToSuppress": [
                "string",
                "string"
            ],
            "groupOverrideDetails": {
                "groupsToOverride": [
                    "string",
                    "string"
                ],
                "iamRolesToOverride": [
                    "string",
                    "string"
                ],
                "preferredRole": "string"
            }
        }
    }
}
```

Versions two and three
The versions two and three request events add fields that customize the
access token. User pools apply changes from version three events to access
tokens for machine identities. These versions also add support for complex
`claimsToOverride` data types in the response object. Your
Lambda function can return the following types of data in the value of
`claimsToOverride`:

- String
- Number
- Boolean
- Array of strings, numbers, booleans, or a combination of any of
  these
- JSON

```
{
    "request": {
        "userAttributes": {
            "string": "string"
        },
        "scopes": ["string", "string"],
        "groupConfiguration": {
            "groupsToOverride": ["string", "string"],
            "iamRolesToOverride": ["string", "string"],
            "preferredRole": "string"
        },
        "clientMetadata": {
            "string": "string"
        }
    },
    "response": {
        "claimsAndScopeOverrideDetails": {
            "idTokenGeneration": {
                "claimsToAddOrOverride": {
                    "string": `[accepted datatype]`
                },
                "claimsToSuppress": ["string", "string"]
            },
            "accessTokenGeneration": {
                "claimsToAddOrOverride": {
                    "string": `[accepted datatype]`
                },
                "claimsToSuppress": ["string", "string"],
                "scopesToAdd": ["string", "string"],
                "scopesToSuppress": ["string", "string"]
            },
            "groupOverrideDetails": {
                "groupsToOverride": ["string", "string"],
                "iamRolesToOverride": ["string", "string"],
                "preferredRole": "string"
            }
        }
    }
}
```

### Pre token generation request parameters

| Name               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Minimum trigger event version |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| userAttributes     | The attributes of your user's profile in your user pool.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1                             |
| groupConfiguration | The input object that contains the current group configuration.<br>The object includes `groupsToOverride`,<br>`iamRolesToOverride`, and<br>`preferredRole`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1                             |
| groupsToOverride   | The [user pool<br>groups](cognito-user-pools-user-groups.md#cognito-user-pools-user-groups.title "cognito-user-pools-user-groups.md#cognito-user-pools-user-groups.title") that your user is a member of.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 1                             |
| iamRolesToOverride | You can associate a user pool group with an AWS Identity and Access Management (IAM)<br>role. This element is a list of all IAM roles from the groups that<br>your user is a member of.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 1                             |
| preferredRole      | You can set a [precedence](cognito-user-pools-user-groups.md#assigning-precedence-values-to-groups.title "cognito-user-pools-user-groups.md#assigning-precedence-values-to-groups.title") for user pool groups. This element contains<br>the name of the IAM role from the group with the highest<br>precendence in the `groupsToOverride` element.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 1                             |
| clientMetadata     | One or more key-value pairs that you can specify and provide as<br>custom input to the Lambda function for the pre token generation<br>trigger.<br>To pass this data to your Lambda function, use the ClientMetadata<br>parameter in the [AdminRespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.md") and [RespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md "../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md") API operations. Amazon Cognito doesn't<br>include data from the `ClientMetadata` parameter in<br>[AdminInitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md") and [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md")<br>API operations in the request that it passes to the pre token<br>generation function. | 1                             |
| scopes             | Access token scopes. The scopes that are present in an access<br>token are the user pool standard and custom scopes that your user<br>requested, and that you authorized your app client to issue.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 2                             |

### Pre token generation response parameters

| Name                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Minimum trigger event version                                                          |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| claimsOverrideDetails         | A container for all elements in a `V1_0` trigger event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 1                                                                                      |
| claimsAndScopeOverrideDetails | A container for all elements in a `V2_0` or<br>`V3_0` trigger event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 2                                                                                      |
| idTokenGeneration             | The claims that you want to override, add, or suppress in your<br>user’s ID token. This parent to ID token customization values<br>appears only in event version 2 and above, but the child elements<br>appear in version 1 events.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 2                                                                                      |
| accessTokenGeneration         | The claims and scopes that you want to override, add, or suppress<br>in your user’s access token. This parent to access token<br>customization values appears only in event version 2 and<br>above.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 2                                                                                      |
| claimsToAddOrOverride         | A map of one or more claims and their values that you want to add<br>or modify. For group-related claims, use<br>`groupOverrideDetails` instead.<br>In event version 2 and above, this element appears under both<br>`accessTokenGeneration` and<br>`idTokenGeneration`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1[\*](#cognito-pretoken-complex-objects-note "#cognito-pretoken-complex-objects-note") |
| claimsToSuppress              | A list of claims that you want Amazon Cognito to suppress. If your function<br>both suppresses and replaces a claim value, then Amazon Cognito suppresses<br>the claim.<br>In event version 2 and above, this element appears under both<br>`accessTokenGeneration` and<br>`idTokenGeneration`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 1                                                                                      |
| groupOverrideDetails          | The output object that contains the current group configuration.<br>The object includes `groupsToOverride`,<br>`iamRolesToOverride`, and<br>`preferredRole`.<br>Your function replaces the `groupOverrideDetails`<br>object with the object that you provide. If you provide an empty or<br>null object in the response, then Amazon Cognito suppresses the groups. To<br>keep the existing group configuration the same, copy the value of<br>the `groupConfiguration` object of the request to the<br>`groupOverrideDetails` object in the response. Then<br>pass it back to the service.<br>Amazon Cognito ID and access tokens both contain the<br>`cognito:groups` claim. Your<br>`groupOverrideDetails` object replaces the<br>`cognito:groups` claim in access tokens and ID<br>tokens. Group overrides are the only changes to the access token<br>that version 1 events can make. | 1                                                                                      |
| scopesToAdd                   | A list of scopes that you want to add to the `scope`<br>claim in your user's access token. You can't add scope values that<br>contain one or more blank-space characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 2                                                                                      |
| scopesToSuppress              | A list of scopes that you want to remove from the<br>`scope` claim in your user's access token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 2                                                                                      |

\* Response objects to version one events can return
strings. Response objects to version two and three events can return [complex
objects](#user-pool-lambda-pre-token-generation-event-versions "#user-pool-lambda-pre-token-generation-event-versions").

## Pre token trigger event version two example: Add and suppress claims, scopes, and

groups

This example makes the following modifications to a user's tokens.

1. Sets their `family_name` as `Doe` in the ID
   token.
2. Prevents `email` and `phone_number` claims from
   appearing in the ID token.
3. Sets their ID token `cognito:roles` claim to
   `"arn:aws:iam::123456789012:role\/sns_callerA","arn:aws:iam::123456789012:role\/sns_callerC","arn:aws:iam::123456789012:role\/sns_callerB"`.
4. Sets their ID token `cognito:preferred_role` claim to
   `arn:aws:iam::123456789012:role/sns_caller`.
5. Adds the scopes `openid`, `email`, and
   `solar-system-data/asteroids.add` to the access token.
6. Suppresses the scope `phone_number` and
   `aws.cognito.signin.user.admin` from the access token. Removal of
   `phone_number` prevents retrieval of the user's phone number from
   `userInfo`. Removal of `aws.cognito.signin.user.admin`
   prevents API requests by the user to read and modify their own profile with the
   Amazon Cognito user pools API.

###### Note

The removal of `phone_number` from scopes only prevents
retrieval of a user's phone number if the remaining scopes in the access
token include `openid` and at least one more standard scope. For
more information, see [About
scopes](cognito-user-pools-define-resource-servers.md#cognito-user-pools-define-resource-servers-about-scopes "cognito-user-pools-define-resource-servers.md#cognito-user-pools-define-resource-servers-about-scopes"). 7. Sets their ID and access token `cognito:groups` claim to
`"new-group-A","new-group-B","new-group-C"`.

JavaScript

```
export const handler = function(event, context) {
  event.response = {
    "claimsAndScopeOverrideDetails": {
      "idTokenGeneration": {
        "claimsToAddOrOverride": {
          "family_name": "Doe"
        },
        "claimsToSuppress": [
          "email",
          "phone_number"
        ]
      },
      "accessTokenGeneration": {
        "scopesToAdd": [
          "openid",
          "email",
          "solar-system-data/asteroids.add"
        ],
        "scopesToSuppress": [
          "phone_number",
          "aws.cognito.signin.user.admin"
        ]
      },
      "groupOverrideDetails": {
        "groupsToOverride": [
          "new-group-A",
          "new-group-B",
          "new-group-C"
        ],
        "iamRolesToOverride": [
          "arn:aws:iam::123456789012:role/new_roleA",
          "arn:aws:iam::123456789012:role/new_roleB",
          "arn:aws:iam::123456789012:role/new_roleC"
        ],
        "preferredRole": "arn:aws:iam::123456789012:role/new_role",
      }
    }
  };
  // Return to Amazon Cognito
  context.done(null, event);
};
```

Amazon Cognito passes event information to your Lambda function. The function then returns the same event
object to Amazon Cognito, with any changes in the response. In the Lambda console, you can set up a test
event with data that is relevant to your Lambda trigger. The following is a test event for this code sample:

JSON

```
{
    "version": "2",
    "triggerSource": "TokenGeneration_Authentication",
    "region": "us-east-1",
    "userPoolId": "us-east-1_EXAMPLE",
    "userName": "JaneDoe",
    "callerContext": {
        "awsSdkVersion": "aws-sdk-unknown-unknown",
        "clientId": "1example23456789"
    },
    "request": {
        "userAttributes": {
            "sub": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "cognito:user_status": "CONFIRMED",
            "email_verified": "true",
            "phone_number_verified": "true",
            "phone_number": "+12065551212",
            "family_name": "Zoe",
            "email": "Jane.Doe@example.com"
        },
        "groupConfiguration": {
            "groupsToOverride": ["group-1", "group-2", "group-3"],
            "iamRolesToOverride": ["arn:aws:iam::123456789012:role/sns_caller1", "arn:aws:iam::123456789012:role/sns_caller2", "arn:aws:iam::123456789012:role/sns_caller3"],
            "preferredRole": ["arn:aws:iam::123456789012:role/sns_caller"]
        },
        "scopes": [
            "aws.cognito.signin.user.admin", "openid", "email", "phone"
        ]
    },
    "response": {
        "claimsAndScopeOverrideDetails": []
    }
}
```

## Pre token generation event version two example: Add claims with complex

objects

This example makes the following modifications to a user's tokens.

1. Adds claims of number, string, boolean, and JSON types to the ID token. This
   is the only change that version two trigger events makes available to the ID
   token.
2. Adds claims of number, string, boolean, and JSON types to the access
   token.
3. Adds three scopes to the access token.
4. Suppresses the `email` claim in the ID and access tokens.
5. Suppresses the `aws.cognito.signin.user.admin` scope in the access
   token.

JavaScript

```
export const handler = function(event, context) {

    var scopes = ["MyAPI.read", "MyAPI.write", "MyAPI.admin"]
    var claims = {}
    claims["aud"]= event.callerContext.clientId;
    claims["booleanTest"] = false;
    claims["longTest"] = 9223372036854775807;
    claims["exponentTest"] = 1.7976931348623157E308;
    claims["ArrayTest"] = ["test", 9223372036854775807, 1.7976931348623157E308, true];
    claims["longStringTest"] = "\{\
        \"first_json_block\": \{\
            \"key_A\": \"value_A\",\
            \"key_B\": \"value_B\"\
        \},\
        \"second_json_block\": \{\
            \"key_C\": \{\
                \"subkey_D\": [\
                    \"value_D\",\
                    \"value_E\"\
                ],\
                \"subkey_F\": \"value_F\"\
            \},\
            \"key_G\": \"value_G\"\
        \}\
    \}";
    claims["jsonTest"] = {
    	"first_json_block": {
    		"key_A": "value_A",
    		"key_B": "value_B"
    	},
    	"second_json_block": {
    		"key_C": {
    			"subkey_D": [
    				"value_D",
    				"value_E"
    			],
    			"subkey_F": "value_F"
    		},
    		"key_G": "value_G"
    	}
    };
    event.response = {
        "claimsAndScopeOverrideDetails": {
            "idTokenGeneration": {
                "claimsToAddOrOverride": claims,
                "claimsToSuppress": ["email"]
            },
            "accessTokenGeneration": {
                "claimsToAddOrOverride": claims,
                "claimsToSuppress": ["email"],
                "scopesToAdd": scopes,
                "scopesToSuppress": ["aws.cognito.signin.user.admin"]
            }
        }
    };
    console.info("EVENT response\n" + JSON.stringify(event, (_, v) => typeof v === 'bigint' ? v.toString() : v, 2))
    console.info("EVENT response size\n" + JSON.stringify(event, (_, v) => typeof v === 'bigint' ? v.toString() : v).length)
    // Return to Amazon Cognito
    context.done(null, event);
};
```

Amazon Cognito passes event information to your Lambda function. The function then returns the same event
object to Amazon Cognito, with any changes in the response. In the Lambda console, you can set up a test
event with data that is relevant to your Lambda trigger. The following is a test event for this code sample:

JSON

```
{
    "version": "2",
    "triggerSource": "TokenGeneration_HostedAuth",
    "region": "us-west-2",
    "userPoolId": "us-west-2_EXAMPLE",
    "userName": "JaneDoe",
    "callerContext": {
        "awsSdkVersion": "aws-sdk-unknown-unknown",
        "clientId": "1example23456789"
    },
    "request": {
        "userAttributes": {
            "sub": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "cognito:user_status": "CONFIRMED"
            "email_verified": "true",
            "phone_number_verified": "true",
            "phone_number": "+12065551212",
            "email": "Jane.Doe@example.com"
        },
        "groupConfiguration": {
            "groupsToOverride": ["group-1", "group-2", "group-3"],
            "iamRolesToOverride": ["arn:aws:iam::123456789012:role/sns_caller1"],
            "preferredRole": ["arn:aws:iam::123456789012:role/sns_caller1"]
        },
        "scopes": [
            "aws.cognito.signin.user.admin",
            "phone",
            "openid",
            "profile",
            "email"
        ]
    },
    "response": {
        "claimsAndScopeOverrideDetails": []
    }
}
```

## Pre token

generation event version one example: Add a new claim and suppress an existing
claim

This example uses a version 1 trigger event with a pre token generation Lambda function
to add a new claim and suppresses an existing claim.

Node.js

```
const handler = async (event) => {
  event.response = {
    claimsOverrideDetails: {
      claimsToAddOrOverride: {
        my_first_attribute: "first_value",
        my_second_attribute: "second_value",
      },
      claimsToSuppress: ["email"],
    },
  };

  return event;
};

export { handler };

```

Amazon Cognito passes event information to your Lambda function. The function then returns the same event
object to Amazon Cognito, with any changes in the response. In the Lambda console, you can set up a test
event with data that is relevant to your Lambda trigger. The following is a test event for this code sample: Because the code example doesn't process any request parameters, you can use
a test event with an empty request. For more information about common request
parameters, see [User pool
Lambda trigger event](cognito-user-pools-working-with-lambda-triggers.md#cognito-user-pools-lambda-trigger-event-parameter-shared "cognito-user-pools-working-with-lambda-triggers.md#cognito-user-pools-lambda-trigger-event-parameter-shared").

JSON

```
{
  "request": {},
  "response": {}
}
```

## Pre

token generation event version one example: Modify the user's group
membership

This example uses a version 1 trigger event with a pre token generation Lambda function
to modify the user's group membership.

Node.js

```
const handler = async (event) => {
  event.response = {
    claimsOverrideDetails: {
      groupOverrideDetails: {
        groupsToOverride: ["group-A", "group-B", "group-C"],
        iamRolesToOverride: [
          "arn:aws:iam::XXXXXXXXXXXX:role/sns_callerA",
          "arn:aws:iam::XXXXXXXXX:role/sns_callerB",
          "arn:aws:iam::XXXXXXXXXX:role/sns_callerC",
        ],
        preferredRole: "arn:aws:iam::XXXXXXXXXXX:role/sns_caller",
      },
    },
  };

  return event;
};

export { handler };

```

Amazon Cognito passes event information to your Lambda function. The function then returns the same event
object to Amazon Cognito, with any changes in the response. In the Lambda console, you can set up a test
event with data that is relevant to your Lambda trigger. The following is a test event for this code sample:

JSON

```
{
  "request": {},
  "response": {}
}
```

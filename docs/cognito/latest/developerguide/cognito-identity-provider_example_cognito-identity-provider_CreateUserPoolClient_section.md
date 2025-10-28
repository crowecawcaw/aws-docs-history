# Use `CreateUserPoolClient` with an AWS SDK or CLI

The following code examples show how to use `CreateUserPoolClient`.

CLI

**AWS CLI**

**To create a user pool client**

The following `create-user-pool-client` example creates a new user pool client with a client secret, explicit read and write attributes, sign in with username-password and SRP flows, sign-in with three IdPs, access to a subset of OAuth scopes, PinPoint analytics, and an extended authentication session validity.

```
`aws cognito-idp create-user-pool-client \
 --user-pool-id `us-west-2_EXAMPLE` \
 --client-name `MyTestClient` \
 --generate-secret \
 --refresh-token-validity `10` \
 --access-token-validity `60` \
 --id-token-validity `60` \
 --token-validity-units `AccessToken=minutes,IdToken=minutes,RefreshToken=days` \
 --read-attributes `email` `phone_number` `email_verified` `phone_number_verified` \
 --write-attributes `email` `phone_number` \
 --explicit-auth-flows `ALLOW_USER_PASSWORD_AUTH` `ALLOW_USER_SRP_AUTH` `ALLOW_REFRESH_TOKEN_AUTH` \
 --supported-identity-providers `Google` `Facebook` `MyOIDC` \
 --callback-urls `https://www.amazon.com` `https://example.com` `http://localhost:8001` `myapp://example` \
 --allowed-o-auth-flows `code` `implicit` \
 --allowed-o-auth-scopes `openid` `profile` `aws.cognito.signin.user.admin` `solar-system-data/asteroids.add` \
 --allowed-o-auth-flows-user-pool-client \
 --analytics-configuration `ApplicationArn=arn:aws:mobiletargeting:us-west-2:767671399759:apps/thisisanexamplepinpointapplicationid,UserDataShared=TRUE` \
 --prevent-user-existence-errors `ENABLED` \
 --enable-token-revocation \
 --enable-propagate-additional-user-context-data \
 --auth-session-validity `4``

```

Output:

```
{
    "UserPoolClient": {
        "UserPoolId": "us-west-2_EXAMPLE",
        "ClientName": "MyTestClient",
        "ClientId": "123abc456defEXAMPLE",
        "ClientSecret": "this1234is5678my91011example1213client1415secret",
        "LastModifiedDate": 1726788459.464,
        "CreationDate": 1726788459.464,
        "RefreshTokenValidity": 10,
        "AccessTokenValidity": 60,
        "IdTokenValidity": 60,
        "TokenValidityUnits": {
            "AccessToken": "minutes",
            "IdToken": "minutes",
            "RefreshToken": "days"
        },
        "ReadAttributes": [
            "email_verified",
            "phone_number_verified",
            "phone_number",
            "email"
        ],
        "WriteAttributes": [
            "phone_number",
            "email"
        ],
        "ExplicitAuthFlows": [
            "ALLOW_USER_PASSWORD_AUTH",
            "ALLOW_USER_SRP_AUTH",
            "ALLOW_REFRESH_TOKEN_AUTH"
        ],
        "SupportedIdentityProviders": [
            "Google",
            "MyOIDC",
            "Facebook"
        ],
        "CallbackURLs": [
            "https://example.com",
            "https://www.amazon.com",
            "myapp://example",
            "http://localhost:8001"
        ],
        "AllowedOAuthFlows": [
            "implicit",
            "code"
        ],
        "AllowedOAuthScopes": [
            "aws.cognito.signin.user.admin",
            "openid",
            "profile",
            "solar-system-data/asteroids.add"
        ],
        "AllowedOAuthFlowsUserPoolClient": true,
        "AnalyticsConfiguration": {
            "ApplicationArn": "arn:aws:mobiletargeting:us-west-2:123456789012:apps/thisisanexamplepinpointapplicationid",
            "RoleArn": "arn:aws:iam::123456789012:role/aws-service-role/cognito-idp.amazonaws.com/AWSServiceRoleForAmazonCognitoIdp",
            "UserDataShared": true
        },
        "PreventUserExistenceErrors": "ENABLED",
        "EnableTokenRevocation": true,
        "EnablePropagateAdditionalUserContextData": true,
        "AuthSessionValidity": 4
    }
}
```

For more information, see [Application-specific settings with app clients](user-pool-settings-client-apps.md "user-pool-settings-client-apps.md") in the _Amazon Cognito Developer Guide_.

- For API details, see
  [CreateUserPoolClient](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-pool-client.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-pool-client.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cognito#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cognito#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.cognitoidentityprovider.CognitoIdentityProviderClient;
import software.amazon.awssdk.services.cognitoidentityprovider.model.CognitoIdentityProviderException;
import software.amazon.awssdk.services.cognitoidentityprovider.model.CreateUserPoolClientRequest;
import software.amazon.awssdk.services.cognitoidentityprovider.model.CreateUserPoolClientResponse;

/**
 * A user pool client app is an application that authenticates with Amazon
 * Cognito user pools.
 * When you create a user pool, you can configure app clients that allow mobile
 * or web applications
 * to call API operations to authenticate users, manage user attributes and
 * profiles,
 * and implement sign-up and sign-in flows.
 *
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class CreateUserPoolClient {
    public static void main(String[] args) {
        final String usage = """

                Usage:
                    <clientName> <userPoolId>\s

                Where:
                    clientName - The name for the user pool client to create.
                    userPoolId - The ID for the user pool.
                """;

        if (args.length != 2) {
            System.out.println(usage);
            System.exit(1);
        }

        String clientName = args[0];
        String userPoolId = args[1];
        CognitoIdentityProviderClient cognitoClient = CognitoIdentityProviderClient.builder()
                .region(Region.US_EAST_1)
                .build();

        createPoolClient(cognitoClient, clientName, userPoolId);
        cognitoClient.close();
    }

    public static void createPoolClient(CognitoIdentityProviderClient cognitoClient, String clientName,
            String userPoolId) {
        try {
            CreateUserPoolClientRequest request = CreateUserPoolClientRequest.builder()
                    .clientName(clientName)
                    .userPoolId(userPoolId)
                    .build();

            CreateUserPoolClientResponse response = cognitoClient.createUserPoolClient(request);
            System.out.println("User pool " + response.userPoolClient().clientName() + " created. ID: "
                    + response.userPoolClient().clientId());

        } catch (CognitoIdentityProviderException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [CreateUserPoolClient](../../../goto/SdkForJavaV2/cognito-idp-2016-04-18/CreateUserPoolClient.md "../../../goto/SdkForJavaV2/cognito-idp-2016-04-18/CreateUserPoolClient.md")
  in _AWS SDK for Java 2.x API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

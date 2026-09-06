

# Example application for identity pools
<a name="getting-started-identity-pools-application"></a>

The most common use case for Amazon Cognito identity pools is to federate users from multiple sign-in systems and deliver temporary, limited-access AWS credentials directly to the client. This eliminates the need to build a credentials broker for permissions to access your AWS resources. For example, you might need to let users sign in with their social media accounts and access app assets from Amazon S3 for your mobile application. Identity pools also deliver credentials to users who sign in with user pools.

In this tutorial, you'll create a web application where you can obtain temporary authenticated and guest credentials in the enhanced and basic [authentication flows](authentication-flow.md) with supported identity providers (IdPs) in identity pools. If you're already experienced in web development, download the example app from GitHub.

[Download the example application from GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/cognito/scenarios/identity_pools_example_demo/web)

This example application demonstrates the following capabilities of Amazon Cognito identity pools:

**Authentication flows in identity pools**  
+ Enhanced authentication flow with detailed API request breakdowns
+ Basic authentication flow with detailed API request breakdowns

**Implementing guest (unauthenticated) access**  
+ Provide limited AWS service access without requiring sign-in

**Integration with supported identity providers**  
+ Social IdPs (Facebook, Amazon, Twitter, Apple, and Google) for consumer access
+ Enterprise IdPs (through OpenID Connect or SAML) for corporate users
+ Amazon Cognito user pools

**AWS credentials management**  
+ Exchanging identity provider tokens for temporary AWS credentials
+ Using temporary credentials to access AWS services securely

After you set up the application on your development webserver and access it in a browser, you see the following options.

![Screenshot of the Amazon Cognito identity pool demo application web interface showing the main page with authentication method options and interactive demo sections.](http://docs.aws.amazon.com/cognito/latest/developerguide/images/amazon-cognito-identity-pool-demo-app.png)


**Topics**
+ [Prerequisites](#demo-prerequisites)
+ [Authentication provider setup](#demo-authentication-provider-setup)
+ [Deploy the demo application](#demo-deploy-application)
+ [Explore authentication methods in your identity pool](#explore-authentication-methods-in-identity-pools-application)
+ [Next steps](#next-steps)

## Prerequisites
<a name="demo-prerequisites"></a>

Before you begin, you'll need the following resources configured.
+ An AWS account with access to Amazon Cognito. If you do not have an AWS account, follow the instructions in [Getting started with AWS](cognito-getting-started-account-iam.md).
+ Python 3.8 or later installed on your development machine.
+ GitHub access.
+ AWS credentials configured with permissions to make authenticated requests to Amazon Cognito APIs. These credentials are required for [developer authentication](authentication-flow.md#authentication-flow-developer).

For more information about implementing AWS credentials and identity pool federation in your specific SDK, see [Getting credentials](getting-credentials.md).

## Authentication provider setup
<a name="demo-authentication-provider-setup"></a>

For best results with this application, set up and integrate one or more third-party identity providers (IdPs) or Amazon Cognito user pools with your Amazon Cognito identity pool. After you complete the prerequisites and before you run this demo application, choose which identity providers to configure. The [Amazon Cognito console](https://console.aws.amazon.com/cognito/v2/identity/identity-pools) walks you through the process of configuring identity pools and providers.

**Amazon Cognito user pools**  
+ [Authentication with Amazon Cognito user pools](authentication.md)
+ [Application-specific settings with app clients](user-pool-settings-client-apps.md)

**Social identity providers**  
+ Google: [Setting up Google as an identity pool IdP](google.md)
+ Facebook: [Setting up Facebook as an identity pools IdP](facebook.md)
+ Amazon: [Setting up Login with Amazon as an identity pools IdP](amazon.md)

**OpenID Connect (OIDC) providers**  
+ [Setting up an OIDC provider as an identity pool IdP](open-id.md)

**SAML providers**  
+ [Setting up a SAML provider as an identity pool IdP](saml-identity-provider.md)

**Note**  
For this demo application, you don't need to set up all supported identity providers. You can start with one that matches your use case. Each link provides detailed configuration instructions.

## Deploy the demo application
<a name="demo-deploy-application"></a>

### Clone the repository
<a name="demo-step-1-clone-repository"></a>

1. Open a terminal window.

1. Clone the `aws-doc-sdk-examples` repository or otherwise retrieve [this folder in the repo](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/cognito/scenarios/identity_pools_example_demo/web).

   ```
   git clone https://github.com/awsdocs/aws-doc-sdk-examples.git
   ```

1. Navigate to the project directory.

   ```
   cd python/example_code/cognito/scenarios/identity_pools_example_demo/web
   ```

### Create an identity pool
<a name="demo-step-2-create-identity-pool"></a>

To create an Amazon Cognito identity pool for your application, follow the instructions in [Identity pools console overview](identity-pools.md).

**To configure an identity pool for the demo application**

1. Open the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home).

1. From the left navigation menu, choose **Identity pools**. Choose an existing identity pool, or create a new one.

1. Under **User access**, enable **Authenticated access** and **Guest access**. Configure a new or existing [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) and [assign it the permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-permissions.html) that you want to grant to each type of user.

1. Under **User access**, set up any identity providers that you want to configure.

1. Under **Identity pool properties**, enable **Basic (classic) authentication**.

1. Keep your browser open to the console for your identity pool. You will use the identity pool ID and other configuration information in your application setup.

### Configure and run the application
<a name="demo-step-3-configure-run-application"></a>

The following steps guide you through initial setup of your demo application.

**To configure the demo application**

1. Open a command line in `python/example_code/cognito/scenarios/identity_pools_example_demo/web` in your `aws-doc-sdk-examples` clone.

1. Create a `.env` file by copying the [example environment file](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/cognito/scenarios/identity_pools_example_demo/web/.env.example).

   ```
   cp .env.example .env
   ```

1. Open the `.env` file in a text editor. Replace the example values in the file with your own configuration values.

1. Install backend dependencies.

   ```
   pip install -r requirements.txt
   ```

1. Start the backend server:

   ```
   cd backend 
   python oauth_server.py
   ```

1. Open a new terminal window, navigate to the project directory and start the frontend server:

   ```
   cd frontend
   python -m http.server 8001
   ```

1. Open your browser to the application at [http://localhost:8001](http://localhost:8001). Your browser will display the demo application interface, ready for testing identity pools authentication.

## Explore authentication methods in your identity pool
<a name="explore-authentication-methods-in-identity-pools-application"></a>

This section guides you through basic and enhanced authentication flows using the Amazon Cognito identity pools demo application. With this demo, you'll learn how identity pools work with various identity providers to provide temporary AWS credentials to your application users.

In the **Interactive demo** section of the example application, you will first choose between two types of access supported by identity pools.

**[Unauthenticated (guest) access](#unauthenticated-access)**  
Provide AWS credentials to users who haven't yet authenticated.

**Authenticated access**  
Exchange identity provider tokens for AWS credentials with a full scope of available permissions. Choose an identity provider from among those that you configured in your `.env` file.

## Unauthenticated (guest) access
<a name="unauthenticated-access"></a>

This step demonstrates how to obtain temporary AWS credentials for unauthenticated (guest) users through your identity pool's guest access feature. In the demo application, you'll test both enhanced and basic flows to see how identity pools issue credentials without requiring user sign-in. Guest access uses the same API sequence as authenticated access, but without providing identity provider tokens (such as OAuth tokens from Google, Facebook, or SAML assertions from enterprise providers).

Continue reading if you are looking for information about providing limited AWS access to users without requiring authentication. After you implement guest access, you'll learn how to securely provide AWS credentials to anonymous users and understand the differences between the two authentication flows.

**Important**  
Unauthenticated access can issue credentials to anyone with internet access, so it's best used for AWS resources that require minimal security, such as public APIs and graphics assets. Before proceeding with this step, check if you've configured your identity pool with guest access enabled and ensure proper IAM policies are in place to limit permissions.

------
#### [ Guest access with enhanced flow ]

The enhanced flow is a streamlined approach to obtaining AWS credentials for unauthenticated users with two API requests.

**To test guest access with the enhanced flow**

1. In the demo application, navigate to **Interactive demo** section

1. Choose the **Guest access** tab.

1. Choose the **Enhanced flow** tab.

1. Choose **Test guest access**.

1. The app obtains temporary AWS credentials from your identity pools without additional authentication prompts.

1. After successful authentication, you will see the web interface displaying the **Results** panel, and you have two options to explore them:

   1. **View credentials only** button: Choose this button if you want to directly see temporary AWS credentials generated without the API flow details. 

      ```
      {
        "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "Credentials": {
          "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
          "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
          "SessionToken": "IQoJb3JpZ2luX2VjEEXAMPLE......",
          "Expiration": "2025-08-07T00:58:21-07:00"
        }
      }
      ```

   1. **View detailed API flow** button: Choose this button if you want to see the step-by-step API requests. 
      + `GetId()` API request with your `identityPoolId`. No authentication tokens required for guest access

        ```
        {
          "IdentityPoolId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        }
        ```

        If valid, it finds or creates and returns the user's `IdentityID`. An example response looks like this:

        ```
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        }
        ```
      + `GetCredentialsForIdentity()` with the returned `identityPoolId`.

        ```
        POST GetCredentialsForIdentity
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        }
        ```

        Cognito validates guest access, assumes the unauthenticated role internally with AWS STS, and return temporary AWS credential. (No IAM authentication on this call; role trust must allow `cognito-identity-amazonzaws.com`.)

        ```
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
          "Credentials": {
            "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "SessionToken": "IQoJb3JpZ2luX2VjEEXAMPLE......",
            "Expiration": "2025-08-07T00:58:21-07:00"
          }
        }
        ```

------
#### [ Guest access with basic flow ]

The basic flow provides granular control over the authentication process with separate API requests for identity retrieval and credential generation.

**To test guest access with the basic flow**

1. In the demo application, navigate to **Interactive demo** section

1. Choose the **Guest access** tab.

1. Choose the **Basic flow** tab.

1. Choose **Test guest access**.

1. The app obtains temporary AWS credentials from your identity pools without additional authentication prompts.

1. After successful authentication, you will see the web interface displaying the **Results** panel, and you have two options to explore them.

   1. **View credentials only** button: Choose this button if you want to directly see temporary AWS credentials generated without the API flow details. 

      ```
      {
        "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "Credentials": {
          "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
          "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
          "SessionToken": "IQoJb3JpZ2luX2VjEEXAMPLE......",
          "Expiration": "2025-08-12T13:36:17-07:00"
        }
      }
      ```

   1. **View detailed API flow** button: Choose this button if you want to see the step-by-step API requests. 
      +  `GetId()` API request with your identity pool ID. No authentication tokens required for guest access.

        ```
        POST GetId
        {
          "IdentityPoolId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        }
        ```

        If valid, it finds or creates and returns the user's `IdentityID`. An example response looks like this:

        ```
        {
           "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
        }
        ```
      +  `GetOpenIdToken()` with the returned `IdentityID` and the same `Logins` map

        ```
        POST GetOpenIdToken
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
        }
        ```

        Response:

        ```
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
          "Token": "eyJraWQiOiJFWAMPLE......"
        }
        ```

        **What happens in this step:** Amazon Cognito issues a short-lived OpenID Connect web identity token from cognito-identity.amazonaws.com that represents this `IdentityId`. The token includes OIDC claims that AWS STS evaluates, including aud (your identity pool ID) and amr (authenticated or unauthenticated). Your IAM role's trust policy must require those claims.
      +  `AssumeRoleWithWebIdentity()` - Your app calls AWS STS directly to exchange the Amazon Cognito OpenID token for temporary AWS credentials

        ```
        POST sts:AssumeRoleWithWebIdentity
        {
          "RoleArn": "arn:aws:iam::111122223333:role/Cognito_IdentityPoolUnauth_Role",
          "WebIdentityToken": "eyJraWQiOiJFWAMPLE......"
        }
        ```

        Response:

        ```
        {
          "Credentials": {
            "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "SessionToken": "FwoGZXIvYXdzEEXAMPLE......"
          }
        }
        ```

        **What happens in this step:** Once validated: returns temporary AWS credentials

------

### Use the temporary credentials
<a name="use-temporary-credentials"></a>

These temporary credentials function as standard AWS credentials but with limited permissions defined by your identity pool's unauthenticated IAM role. You can use them with any AWS SDK or AWS CLI. For more information about configuring AWS SDKs with credentials, see [Standardized credentials providers](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html) in the AWS SDKs and Tools Reference Guide.

The examples below are not a complete list, but they show common ways an identity pool's guest feature can improve user experience.

#### Public, read-only content
<a name="public-content"></a>

The following examples configure credentials providers for limited Amazon S3 access as a guest user.

------
#### [ Python ]

```
# Example: Using credentials with boto3
import boto3

# Configure client with temporary credentials
s3_client = boto3.client(
    's3',
    aws_access_key_id='AKIAIOSFODNN7EXAMPLE',
    aws_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
    aws_session_token='IQoJb3JpZ2luX2VjEEXAMPLE......'
)

# Make API requests within IAM role permissions
response = s3_client.list_objects_v2(Bucket='my-public-bucket')

# Access public content
for obj in response.get('Contents', []):
    print(f"File: {obj['Key']}, Size: {obj['Size']} bytes")
```

------
#### [ JavaScript ]

```
// Example: Accessing public content
import { S3Client, GetObjectCommand } from "@aws-sdk/client-s3";

const s3Client = new S3Client({
    region: "us-east-1",
    credentials: {
        accessKeyId: 'AKIAIOSFODNN7EXAMPLE',
        secretAccessKey: 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
        sessionToken: 'IQoJb3JpZ2luX2VjEEXAMPLE......'
    }
});

// Access public images or documents
const response = await s3Client.send(new GetObjectCommand({
    Bucket: 'my-public-content',
    Key: 'product-catalog.pdf'
}));
```

------

### "Try-before-login" features
<a name="try-before-login"></a>

The following examples make use of read-only access to Amazon DynamoDB as a guest user.

------
#### [ Python ]

```
# Example: Limited app functionality for trial users
import boto3

dynamodb = boto3.client(
    'dynamodb',
    aws_access_key_id='AKIAIOSFODNN7EXAMPLE',
    aws_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
    aws_session_token='IQoJb3JpZ2luX2VjEEXAMPLE......'
)

# Allow guest users to view sample data (limited to 5 items)
response = dynamodb.scan(TableName='SampleProducts', Limit=5)
```

------
#### [ JavaScript ]

```
// Example: Limited app functionality for trial users
import { DynamoDBClient, ScanCommand } from "@aws-sdk/client-dynamodb";

const dynamodbClient = new DynamoDBClient({
    region: "us-east-1",
    credentials: {
        accessKeyId: 'AKIAIOSFODNN7EXAMPLE',
        secretAccessKey: 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
        sessionToken: 'IQoJb3JpZ2luX2VjEEXAMPLE......'
    }
});

// Allow guest users to view sample data (limited to 5 items)
const response = await dynamodbClient.send(new ScanCommand({
    TableName: 'SampleProducts',
    Limit: 5
}));
```

------

## Social identity provider authentication
<a name="social-identity-provider-authentication"></a>

This step explores the overall flow for using social identity providers with Amazon Cognito identity pools. Social authentication provides a familiar sign-in experience while maintaining security through federated identity management. You can sign in from a social identity provider (IdP) like Google, Facebook, and Amazon, and then exchange that IdP token for temporary AWS credentials. Twitter and Apple integration is also supported by identity pools, but isn't supported in the example application.

The identity pool itself is not a user directory. It doesn’t store passwords or profile fields. Instead, it trusts external IdPs to authenticate the user and focuses on authorizing that already-authenticated user to directly call AWS services, by vending credentials for IAM roles.

------
#### [ Social identity provider with enhanced flow ]

This section shows how you can use a social identity provider to sign in a user and, using the enhanced flow, exchange the provider token in an Amazon Cognito identity pool for temporary credentials to request AWS resources.

**Use social sign-in with the enhanced flow in the example application**

1. In the demo application, navigate to **Interactive demo** section

1. Choose the **Authenticated access** tab.

1. Choose the **Enhanced flow** tab.

1. Choose a supported social provider you’ve configured, for example **Sign in with Google**, **Sign in with Facebook**, or ** Login with Amazon**.

1. Sign in and consent to share user data with the application.

1. The provider redirects back to the app’s redirect URI

1. The app sends the provider token to your identity pool and retrieves temporary AWS credentials

1. The app displays the **Results** panel in web interface.

   After successful authentication, you will see the web interface displaying the **Results** panel, and you have two options to explore them:

   1. **View credentials only** button: Choose this button if you want to directly see temporary AWS credentials generated without the API flow details. 

      ```
      {
        "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "Credentials": {
          "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
          "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
          "SessionToken": "IQoJb3JpZ2luX2VjEEXAMPLE......",
          "Expiration": "2025-08-12T13:36:17-07:00"
        }
      }
      ```

   1. **View detailed API flow** button: Choose this button if you want to see the step-by-step API requests. 
      +  The app signs in the user with a social IdP and obtains the provider token. Identity pools accept these artifacts from social providers:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-identity-pools-application.html)

        After successful authentication with the social provider, your app receives an OAuth response containing the access token and other authentication details:

        ```
        {
           "access_token": "ya29.A0AS3H6NEXAMPLE......",
           "expires_in": 3599,
           "scope": "openid https://www.examplesocial....",
           "token_type": "Bearer",
           "id_token": "eyJhbGciOiJSUzI1NiIsEXAMPLE......"
        }
        ```
      +  `GetId()` API request with your identity pool ID and a `Logins`map containing your social provider token

        ```
        POST GetId
        {
          "IdentityPoolId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
          "Logins": {
            "accounts.google.com": "eyJhbGciOiJSUzI1NiIsEXAMPLE......"
          }
        }
        ```

        Response:

        ```
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
        }
        ```
      + `GetCredentialsForIdentity()` with the returned `IdentityID` and the same `Logins` map

        ```
        POST GetCredentialsForIdentity
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
          "Logins": {
            "accounts.google.com": "eyJhbGciOiJSUzI1NiIsEXAMPLE......"
          }
        }
        ```

        Response:

        ```
        {
          "Credentials": {
            "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "SessionToken": "IQoJb3JpZ2luX2VjEEXAMPLE......",
            "Expiration": "2025-08-07T00:58:21-07:00"
          },
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
        }
        ```

**What happened**: Amazon Cognito validated the token against the configured provider, chose an IAM role based on your provider configuration, and called AWS STS on your behalf. Your identity pool then returned temporary credentials.

------
#### [ Social identity provider with basic flow ]

This section shows how you can use a social identity provider to sign in a user and, using the basic flow, exchange the provider token in an Amazon Cognito identity pool for temporary credentials to call AWS services. 

**Use social sign-in with the basic flow in the example application**

1. In the demo application, navigate to **Interactive demo** section

1. Choose the **Authenticated access** tab.

1. Choose the **Basic flow** tab.

1. Choose a supported social provider you’ve configured, for example **Sign in with Google**, **Sign in with Facebook**, or ** Login with Amazon**.

1. Sign in and consent to share user data with the application.

1. The provider redirects back to the app’s redirect URI

1. The app sends the provider token to your identity pool and retrieves temporary AWS credentials

1. The app displays the **Results** panel in web interface.

   After successful authentication, you will see the web interface displaying the **Results** panel, and you have two options to explore them:

   1. **View credentials only** button: Choose this button if you want to directly see temporary AWS credentials generated without the API flow details. 

      ```
      {
        "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "Credentials": {
          "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
          "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
          "SessionToken": "IQoJb3JpZ2luX2VjEEXAMPLE......",
          "Expiration": "2025-08-12T13:36:17-07:00"
        }
      }
      ```

   1. **View detailed API flow** button: Choose this button if you want to see the step-by-step API requests. 
      +  The app signs in the user with a social IdP and obtains the provider token. Identity pools accept these artifacts from social providers:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-identity-pools-application.html)

        After successful authentication with the social provider, your app receives an OAuth response containing the access token and other authentication details:

        ```
        {
           "access_token": "ya29.A0AS3H6NEXAMPLE......",
           "expires_in": 3599,
           "scope": "openid https://www.examplesocial....",
           "token_type": "Bearer",
           "id_token": "eyJhbGciOiJSUzI1NiIsEXAMPLE......"
        }
        ```
      +  `GetId()` API request with your identity pool ID and a `Logins` map containing your social provider token

        ```
        POST GetId
        {
          "IdentityPoolId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
          "Logins": {
            "accounts.google.com": "token..."
          }
        }
        ```

        Response:

        ```
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
        }
        ```
      +  `GetOpenIdToken()` with the returned `IdentityID` and the same Logins map

        ```
        POST GetOpenIdToken
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
          "Logins": {
            "accounts.google.com": "token..."
          }
        }
        ```

        Response:

        ```
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
          "Token": "eyJraWQiOiJFWAMPLE......"
        }
        ```
      +  `AssumeRoleWithWebIdentity()` with the OpenID token

        ```
        POST AssumeRoleWithWebIdentity
        {
          "RoleArn": "arn:aws:iam::111122223333:role/Cognito_IdentityPoolAuth_Role",
          "WebIdentityToken": "eyJraWQiOiJFWAMPLE......"
        }
        ```

        Response:

        ```
        {
          "Credentials": {
            "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "SessionToken": "IQoJb3JpZ2luX2VjEEXAMPLE......",
            "Expiration": "2025-08-12T14:36:17-07:00"
          }
        }
        ```

**What happened**: Amazon Cognito validated the token against the configured provider and issued an OpenID token. The application called AWS STS directly to assume an IAM role and receive temporary credentials.

------

### Understand social access
<a name="understand-social-access"></a>
+ Social users receive temporary AWS credentials through Amazon Cognito identity pools after authenticating with their social provider.
+ Each authenticated user gets a unique identity ID that persists across sessions.
+ These credentials are linked to an IAM role specifically designed for authenticated access, providing broader permissions than guest access.
+ Social provider tokens are exchanged for AWS credentials, maintaining user identity and permissions.

## Amazon Cognito user pools authentication
<a name="user-pool-authentication"></a>

This step explores Amazon Cognito authentication with user pool [managed login](cognito-user-pools-managed-login.md) integration. When you link a user pool as an IdP to an identity pool, user pool tokens authorize your identity pool to issue temporary credentials.

------
#### [ User pool authentication with enhanced flow ]

The enhanced flow provides a streamlined approach to obtaining AWS credentials through Amazon Cognito identity pools with a single API request.

**Use Amazon Cognito user pool authentication with the identity pool enhanced flow**

1. In the demo application, navigate to **Interactive demo** section

1. Choose the **Authenticated access** tab.

1. Choose the **Enhanced flow** tab.

1. Choose **Sign in with Amazon Cognito user pools**

1. Complete sign-in with your username and password in managed login.

1. The user pool redirects back to your application redirect URI with an authorization code.

1. The application exchanges the authorization code with your user pool for JSON web tokens.

1. The application exchanges the ID token with your identity pool for temporary AWS credentials

1. The app displays the **Results** panel in web interface

   After successful authentication, you will see the web interface displaying the **Results** panel, and you have two options to explore them:

   1. **View credentials only** button: Choose this button if you want to directly see temporary AWS credentials generated without the API flow details. 

      ```
      {
        "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "Credentials": {
          "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
          "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
          "SessionToken": "IQoJb3JpZ2luX2VjEEXAMPLE......",
          "Expiration": "2025-08-12T13:36:17-07:00"
        }
      }
      ```

   1. **View detailed API flow** button: Choose this button if you want to see the step-by-step API requests. 
      +  The app signs in the user with a Amazon Cognito. After successful authentication with the user pool, your app receives an OAuth 2.0 response containing the ID token (JWT). Identity pools accept JWT ID tokens from user pools using this provider key format:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-identity-pools-application.html)

        After successful authentication with the user pool, your app receives an OAuth 2.0 response containing the ID token (JWT):

        ```
        {
           "id_token": "eyJraWQiOiJFWAMPLE......",
           "token_type": "Bearer",
           "expires_in": 3600
        }
        ```
      +  `GetId()` API request with your `identityPoolId`and a `Logins` map that includes your user-pool provider key mapped to the `id_token`. Amazon Cognito verified the user pool ID token's signature, issuer, expiry, and audience (`aud`) matches one of the app client IDs you registered for this user pool IdP in the identity pool.

        ```
        POST GetId
        {
          "AccountId": "111122223333",
          "IdentityPoolId": "us-east-1:1ac4a76d-1fef-48aa-83af-4224799c0b5c",
          "Logins": {
            "cognito-idp.us-east-1.amazonaws.com/us-east-1_EXAMPLE123": "eyJraWQiOiJFWAMPLE......"
          }
        }
        ```

        If valid, it finds or creates and returns the user's `IdentityID`. An example response looks like this:

        ```
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
        }
        ```
      +  `GetCredentialsForIdentity()` with the returned `identityPoolId`and a=the same `Logins` map with the `id_token`. Amazon Cognito revalidates the user pool ID token's signature, issuer, expiry, and audience (`aud`) matches one of the app client IDs you registered for this user pool IdP in the identity pool.

        ```
        POST GetCredentialsForIdentity
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
          "Logins": {
            "cognito-idp.us-east-1.amazonaws.com/us-east-1_EXAMPLE123": "eyJraWQiOiJFWAMPLE......"
          }
        }
        ```

        If valid, it chooses an IAM role (roles-in-token, rules, or default), calls AWS STS on your behalf, and returns temporary AWS credentials. An example response looks like this:

        ```
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
          "Credentials": {
            "AccessKeyId": "ASIAW7TIP7EJEXAMPLE",
            "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "SessionToken": "IQoJb3JpZ2luX2VjEEXAMPLE......",
            "Expiration": "2025-08-12T14:36:17-07:00"
          }
        }
        ```

------
#### [ User pool authentication with basic flow ]

The basic flow provides granular control over the authentication process with separate API requests for identity retrieval and credential generation.

**Use Amazon Cognito user pool authentication with the identity pool basic flow**

1. In the demo application, navigate to **Interactive demo** section

1. Choose the **Authenticated access** tab.

1. Choose the **Basic flow** tab.

1. Choose **Sign in with Amazon Cognito user pools**

1. Complete sign-in with your username and password in managed login.

1. The user pool redirects back to your application redirect URI with an authorization code.

1. The application exchanges the authorization code with your user pool for JSON web tokens.

1. The application exchanges the ID token with your identity pool for temporary AWS credentials

1. The app displays the **Results** panel in web interface

   After successful authentication, you will see the web interface displaying the **Results** panel, and you have two options to explore them:

   1. **View credentials only** button: Choose this button if you want to directly see temporary AWS credentials generated without the API flow details. 

      ```
      {
        "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "Credentials": {
          "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
          "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
          "SessionToken": "IQoJb3JpZ2luX2VjEEXAMPLE......",
          "Expiration": "2025-08-12T13:36:17-07:00"
        }
      }
      ```

   1. **View detailed API flow** button: Choose this button if you want to see the step-by-step API requests. 
      + The app signs in the user with a Amazon Cognito user pool and obtains ID token (JWT) as the artifact. After successful authentication with the user pool, your app receives an OAuth response containing the ID token (JWT). Identity pools use this token for authentication:

        ```
        {
           "id_token": "eyJraWQiOiJFWAMPLE......",
           "token_type": "Bearer",
           "expires_in": 3600
        }
        ```
      + `GetId()` API request with your identity pool ID and a `Logins` map that includes your user-pool provider key and the ID token as the value. Amazon Cognito verified the user pool ID token's signature, expiry, and audience (aud) matches one of the app client IDs you registered for this user pool IdP in the identity pool.

        ```
        POST GetId
        {
          "AccountId": "111122223333",
          "IdentityPoolId": "us-east-1:1ac4a76d-1fef-48aa-83af-4224799c0b5c",
          "Logins": {
            "cognito-idp.us-east-1.amazonaws.com/us-east-1_EXAMPLE123": "eyJraWQiOiJFWAMPLE......"
          }
        }
        ```

        If valid, it finds or creates and returns the user's `IdentityID`. An example response looks like this:

        ```
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
        }
        ```
      + `GetOpenIdToken()` with the returned `IdentityID` and the same `Logins` map

        ```
        POST GetOpenIdToken
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
          "Logins": {
            "cognito-idp.us-east-1.amazonaws.com/us-east-1_EXAMPLE123": "eyJraWQiOiJFWAMPLE......"
          }
        }
        ```

        Response:

        ```
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
          "Token": "eyJraWQiOiJFWAMPLE......"
        }
        ```

        **What happens in this step:** Amazon Cognito issues a short-lived OpenID Connect web identity token from cognito-identity.amazonaws.com that represents this `IdentityId`. The token includes OIDC claims that AWS STS evaluates, including aud (your identity pool ID) and amr (authenticated or unauthenticated). Your IAM role's trust policy must require those claims.
      + `AssumeRoleWithWebIdentity()` - Your app calls AWS STS directly to exchange the Amazon Cognito OpenID token for temporary AWS credentials

        ```
        POST sts:AssumeRoleWithWebIdentity
        {
          "RoleArn": "arn:aws:iam::111122223333:role/Cognito_IdentityPoolAuth_Role",
          "WebIdentityToken": "eyJraWQiOiJFWAMPLE......",
          "RoleSessionName": "CognitoIdentityCredentials"
        }
        ```

        Response:

        ```
        {
          "Credentials": {
            "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "SessionToken": "FwoGZXIvYXdzEEXAMPLE......",
            "Expiration": "2025-08-12T14:36:17-07:00"
          },
          "AssumedRoleUser": {
            "AssumedRoleId": "AROAW7TIP7EJYEXAMPLE:CognitoIdentityCredentials",
            "Arn": "arn:aws:sts::111122223333:assumed-role/Cognito_IdentityPoolAuth_Role/CognitoIdentityCredentials"
          }
        }
        ```

        **What your demo application did:** Your app sent the OpenID token from `GetOpenIdToken()` to AWS STS, requesting temporary credentials. AWS STS performed validation checks and issued credentials:

------

### Understand user pool access
<a name="understand-user-pool-access"></a>
+ User pool users receive temporary AWS credentials through Amazon Cognito identity pools.
+ These credentials are linked to an IAM role specified in your identity pool configuration.
+ User pool ID tokens are exchanged for AWS credentials through the identity pool.

## SAML authentication
<a name="saml-authentication"></a>

This step explores SAML authentication. Users can sign in with enterprise identity providers that support SAML to access AWS services. The basic flow with SAML isn't supported in the example application.

------
#### [ SAML authentication with enhanced flow ]

This section shows how you can use a SAML identity provider to sign in a user and, using the enhanced flow, exchange the SAML assertion in an Amazon Cognito identity pool for temporary AWS credentials to call AWS services.

**Use SAML authentication with the identity pool enhanced flow**

1. In the demo application, navigate to **Interactive demo** section

1. Choose the **Authenticated access** tab.

1. Choose the **Enhanced flow** tab.

1. Choose **Sign in with SAML provider**

1. Complete sign-in with your enterprise credentials.

1. The user pool redirects back to your application redirect URI with a SAML assertion.

1. The application exchanges the authorization code with your user pool for JSON web tokens.

1. The application exchanges the SAML response with your identity pool for temporary AWS credentials

1. The app displays the **Results** panel in web interface

   After successful authentication, you will see the web interface displaying the **Results** panel, and you have two options to explore them:

   1. **View credentials only** button: Choose this button if you want to directly see temporary AWS credentials generated without the API flow details.

      ```
      {
        "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "Credentials": {
          "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
          "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
          "SessionToken": "IQoJb3JpZ2luX2VjEEXAMPLE......",
          "Expiration": "2025-08-12T13:36:17-07:00"
        }
      }
      ```

   1. **View detailed API flow** button: Choose this button if you want to see the step-by-step API requests.
      +  The app signs in the user with a SAML IdP and obtains the SAML response. Identity pools accept SAML assertions from enterprise providers using the SAML provider ARN as the key:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-identity-pools-application.html)

        After successful authentication with the SAML provider, your app receives a SAML response via HTTP POST to your callback URL:

        ```
        {
          "saml_response": "PD94bWwgdmVyc2lvbj0iMS4wIiBFWAMPLE...",
          "provider_arn": "arn:aws:iam::111122223333:saml-provider/EXAMPLE",
          "status": "Authentication successful"
        }
        ```
      +  `GetId()` API request with your identity pool ID and a `Logins` map containing your SAML provider ARN and assertion

        ```
        POST GetId
        {
          "AccountId": "111122223333",
          "IdentityPoolId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
          "Logins": {
            "arn:aws:iam::111122223333:saml-provider/EXAMPLE": "PD94bWwgdmVyc2lvbj0iMS4wIiBFWAMPLE..."
          }
        }
        ```

        Response:

        ```
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
        }
        ```
      +  `GetCredentialsForIdentity()` with the returned `IdentityID`and the same `Logins` map

        ```
        POST GetCredentialsForIdentity
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
          "Logins": {
            "arn:aws:iam::111122223333:saml-provider/EXAMPLE": "PD94bWwgdmVyc2lvbj0iMS4wIiBFWAMPLE..."
          }
        }
        ```

        Response:

        ```
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
          "Credentials": {
            "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "SessionToken": "IQoJb3JpZ2luX2VjEEXAMPLE......"
          }
        }
        ```

**What happened**: Amazon Cognito validated the SAML assertion against the configured provider, chose an IAM role based on SAML attributes or rules, and called AWS STS on your behalf.

------

### Understand SAML access
<a name="understand-saml-access"></a>
+ Enterprise users receive temporary AWS credentials from Amazon Cognito identity pools after authenticating with their SAML provider.
+ Each authenticated user gets a unique identity ID that persists across sessions.
+ These credentials are linked to an IAM role specifically designed for authenticated access, providing broader permissions than guest access.
+ SAML assertions are exchanged for AWS credentials, maintaining user identity and enterprise attributes.

## OpenID Connect (OIDC) authentication
<a name="oidc-authentication"></a>

This step explores OIDC authentication with enterprise identity providers. Users can sign in through their organization's enterprise identity provider (such as Azure AD, Okta, or Google Workspace) to access AWS services. Continue reading if you are looking for information about integrating standards-based authentication with your AWS resources. After you implement OIDC authentication, you'll learn how to leverage OIDC claims for fine-grained access control.

------
#### [ OIDC authentication with enhanced flow ]

This section shows how you can use an OIDC identity provider to sign in a user and, using the enhanced flow, exchange the OIDC token in an Amazon Cognito identity pool for temporary AWS credentials to call AWS services.

**Use OIDC sign-in with the identity pool enhanced flow**

1. In the demo application, navigate to **Interactive demo** section

1. Choose the **Authenticated access** tab.

1. Choose the **Enhanced flow** tab.

1. Choose **Sign in with OIDC provider**

1. Complete sign-in with your enterprise credentials.

1. The OIDC provider redirects back to the app with an authorization code

1. The application exchanges the authorization code with your user pool for JSON web tokens.

1. The application sends the OIDC token to your identity pool and retrieves temporary AWS credentials.

1. The app displays the **Results** panel in web interface

   After successful authentication, you will see the web interface displaying the **Results** panel, and you have two options to explore them:

   1. **View credentials only** button: Choose this button if you want to directly see temporary AWS credentials generated without the API flow details.

      ```
      {
        "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "Credentials": {
          "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
          "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
          "SessionToken": "IQoJb3JpZ2luX2VjEEXAMPLE......",
          "Expiration": "2025-08-12T13:36:17-07:00"
        }
      }
      ```

   1. **View detailed API flow** button: Choose this button if you want to see the step-by-step API requests.
      +  The app signs in the user with an OIDC IdP and obtains the ID token. Identity pools accept OIDC tokens from enterprise providers:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-identity-pools-application.html)

        After successful authentication with the OIDC provider, your app receives an OAuth 2.0 response containing the tokens:

        ```
        {
          "token_type": "Bearer",
          "expires_in": 3600,
          "access_token": "eyJraWQiOiJFWAMPLE......",
          "scope": "email openid profile",
          "id_token": "eyJraWQiOiJFWAMPLE......"
        }
        ```
      +  `GetId()` API request with your identity pool ID and a `Logins` map containing your OIDC provider token

        ```
        POST GetId
        {
          "AccountId": "111122223333",
          "IdentityPoolId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
          "Logins": {
            "example-provider.com/oauth2/default": "eyJraWQiOiJFWAMPLE......"
          }
        }
        ```

        Response:

        ```
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
        }
        ```
      +  `GetCredentialsForIdentity()` with the returned `IdentityID` and the same Logins map

        ```
        POST GetCredentialsForIdentity
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
          "Logins": {
            "example-provider.com/oauth2/default": "eyJraWQiOiJFWAMPLE......"
          }
        }
        ```

        Response:

        ```
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
          "Credentials": {
            "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "SessionToken": "IQoJb3JpZ2luX2VjEEXAMPLE......"
          }
        }
        ```

**What happened**: Amazon Cognito validated the OIDC token against the configured provider, chose an IAM role (default, claim-based, or rule-mapped) and called AWS STS on your behalf.

------
#### [ OIDC authentication with basic flow ]

This section shows how you can use an OIDC identity provider to sign in a user and, using the basic flow, exchange the OIDC token in an Amazon Cognito identity pool for temporary AWS credentials to call AWS services.

**Use OIDC sign-in with the identity pool basic flow**

1. In the demo application, navigate to **Interactive demo** section

1. Choose the **Authenticated access** tab.

1. Choose the **Basic flow** tab.

1. Choose **Sign in with OIDC provider**

1. Complete sign-in with your enterprise credentials.

1. The OIDC provider redirects back to the app with an authorization code

1. The application exchanges the authorization code with your user pool for JSON web tokens.

1. The application sends the OIDC token to your identity pool and retrieves temporary AWS credentials.

1. The app displays the **Results** panel in web interface

   After successful authentication, you will see the web interface displaying the **Results** panel, and you have two options to explore them:

   1. **View credentials only** button: Choose this button if you want to directly see temporary AWS credentials generated without the API flow details.

      ```
      {
        "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "Credentials": {
          "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
          "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
          "SessionToken": "IQoJb3JpZ2luX2VjEEXAMPLE......",
          "Expiration": "2025-08-12T13:36:17-07:00"
        }
      }
      ```

   1. **View detailed API flow** button: Choose this button if you want to see the step-by-step API requests.
      +  The app signs in the user with an OIDC IdP and obtains the ID token. Identity pools accept OIDC tokens from enterprise providers:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-identity-pools-application.html)

        After successful authentication with the OIDC provider, your app receives an OAuth 2.0 response containing the tokens:

        ```
        {
          "token_type": "Bearer",
          "expires_in": 3600,
          "access_token": "eyJraWQiOiJFWAMPLE......",
          "scope": "openid email profile",
          "id_token": "eyJraWQiOiJFWAMPLE......"
        }
        ```
      +  `GetId()` API request with your identity pool ID and a `Logins`map containing your OIDC provider token

        ```
        POST GetId
        {
          "IdentityPoolId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
          "Logins": {
            "example-provider.com/oauth2/default": "eyJraWQiOiJFWAMPLE......"
          }
        }
        ```

        Response:

        ```
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
        }
        ```
      +  `GetOpenIdToken()` with the returned IdentityID and the same `Logins`map

        ```
        POST GetOpenIdToken
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
          "Logins": {
            "example-provider.com/oauth2/default": "eyJraWQiOiJFWAMPLE......"
          }
        }
        ```

        Response:

        ```
        {
          "IdentityId": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
          "Token": "eyJraWQiOiJFWAMPLE......"
        }
        ```
      +  `AssumeRoleWithWebIdentity()` with the OpenID token

        ```
        POST AssumeRoleWithWebIdentity
        {
          "RoleArn": "arn:aws:iam::111122223333:role/Cognito_IdentityPoolAuth_Role",
          "WebIdentityToken": "eyJraWQiOiJFWAMPLE......"
        }
        ```

        Response:

        ```
        {
          "Credentials": {
            "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "SessionToken": "FwoGZXIvYXdzEEXAMPLE......",
            "Expiration": "2025-08-12T14:36:17-07:00"
          }
        }
        ```

**What happened**: Amazon Cognito validated the OIDC token against the configured provider and returned an OpenID token. The application called AWS STS directly to assume the appropriate IAM role and received short-lived credentials.

------

### Understand OIDC authentication
<a name="understand-oidc-authentication"></a>
+ Standards-based: OIDC is built on OAuth 2.0 and provides standardized identity information.
+ Token validation: ID tokens can be validated for authenticity.
+ Claims-based access: OIDC claims can be used for role mapping and access control.
+ Enterprise integration: Works with popular enterprise identity providers.

## Next steps
<a name="next-steps"></a>

Now that you’ve set up and explored the demo application, you can:
+ Configure additional identity providers you haven’t tested yet
+ Experiment with both enhanced and basic authentication to understand their differences
+ Customize the demo for your own use case
+ Integrate Amazon Cognito Identity Pools into your own applications.
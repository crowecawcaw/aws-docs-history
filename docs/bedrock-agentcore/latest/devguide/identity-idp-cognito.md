# Amazon Cognito

Amazon Cognito can be configured as an identity provider for accessing
AgentCore Gateway and Runtime, or an AgentCore Identity credential provider for outbound resource
access. This allows your agents to authenticate and authorize agent users with Cognito
as the identity provider and authorization server, or your agents to obtain credentials
to access resources authorized by Cognito.

## Inbound

To add Cognito as an identity provider and authorization server for accessing
AgentCore Gateway and Runtime, you must:

- Configure discovery URL from your IDP directory. This helps AgentCore Identity get the
  metadata related to your OAuth authorization server and token verification
  keys.
- Enter valid `clientId` or `aud` claims for the token.
  This helps validate the tokens coming from your IDP and allow access for tokens
  that contain expected claims.

Use the following procedure to create a Cognito user pool as an inbound identity provider
for user authentication with AgentCore Runtime. The following steps will create
a Cognito user pool, a user pool client, add a user, and generate a bearer token for
the user. The token is valid for 60 minutes by default.

###### To create a Cognito user pool as an inbound identity provider for Runtime

authentication

1. Create a file named `setup_cognito.sh` with the following
   content:

###### Note

The following script is only meant as an example. You should customize
the user pool settings and user credentials as needed for your
application. Do not use this script directly in production
environments.

```
#!/bin/bash

# Create User Pool and capture Pool ID directly
export POOL_ID=$(aws cognito-idp create-user-pool \
  --pool-name "MyUserPool" \
  --policies '{"PasswordPolicy":{"MinimumLength":8}}' \
  --region us-east-1 | jq -r '.UserPool.Id')

# Create App Client and capture Client ID directly
export CLIENT_ID=$(aws cognito-idp create-user-pool-client \
  --user-pool-id $POOL_ID \
  --client-name "MyClient" \
  --no-generate-secret \
  --explicit-auth-flows "ALLOW_USER_PASSWORD_AUTH" "ALLOW_REFRESH_TOKEN_AUTH" \
  --region us-east-1 | jq -r '.UserPoolClient.ClientId')

# Create User
aws cognito-idp admin-create-user \
  --user-pool-id $POOL_ID \
  --username "testuser" \
  --temporary-password "${temp-password}" \
  --region us-east-1 \
  --message-action SUPPRESS > /dev/null

# Set Permanent Password
aws cognito-idp admin-set-user-password \
  --user-pool-id $POOL_ID \
  --username "testuser" \
  --password "${permanent-user-password}" \
  --region us-east-1 \
  --permanent > /dev/null

# Authenticate User and capture Access Token
export BEARER_TOKEN=$(aws cognito-idp initiate-auth \
  --client-id "$CLIENT_ID" \
  --auth-flow USER_PASSWORD_AUTH \
  --auth-parameters USERNAME='testuser',PASSWORD='${permanent-user-password}' \
  --region us-east-1 | jq -r '.AuthenticationResult.AccessToken')

# Output the required values
echo "Pool id: $POOL_ID"
echo "Discovery URL: https://cognito-idp.us-east-1.amazonaws.com/$POOL_ID/.well-known/openid-configuration"
echo "Client ID: $CLIENT_ID"
echo "Bearer Token: $BEARER_TOKEN"
```

2. Run the script to create the Cognito resources:

```
source setup_cognito.sh
```

3. Record the output values, which will look similar to:

```
Pool id: us-east-1_poolid
Discovery URL: https://cognito-idp.us-east-1.amazonaws.com/us-east-1_userpoolid/.well-known/openid-configuration
Client ID: clientid
Bearer Token: bearertoken
```

You'll need these values in the next steps.

Use the following procedure to create a Cognito user pool as an inbound identity provider
for machine-to-machine authentication with AgentCore Gateway. The following
steps will create a user pool, resource server, client credentials, and discovery
URL configuration. This setup enables M2M authentication flows for Gateway
access.

###### To create a Cognito user pool as an inbound identity provider for Gateway

authentication

1. Create a user pool:

```
aws cognito-idp create-user-pool \
  --region us-west-2 \
  --pool-name "gateway-user-pool"
```

2. Record the user pool ID from the response or retrieve it using:

```
aws cognito-idp list-user-pools \
  --region us-west-2 \
  --max-results 60
```

3. Create a resource server for the user pool:

```
aws cognito-idp create-resource-server \
  --region us-west-2 \
  --user-pool-id <UserPoolId> \
  --identifier "gateway-resource-server" \
  --name "GatewayResourceServer" \
  --scopes '[{"ScopeName":"read","ScopeDescription":"Read access"}, {"ScopeName":"write","ScopeDescription":"Write access"}]'
```

4. Create a client for the user pool:

```
aws cognito-idp create-user-pool-client \
  --region us-west-2 \
  --user-pool-id <UserPoolId> \
  --client-name "gateway-client" \
  --generate-secret \
  --allowed-o-auth-flows client_credentials \
  --allowed-o-auth-scopes "gateway-resource-server/read" "gateway-resource-server/write" \
  --allowed-o-auth-flows-user-pool-client \
  --supported-identity-providers "COGNITO"
```

Record the client ID and client secret from the response. You'll need
these values to configure the Cognito provider in AgentCore Identity. 5. If needed, create a domain for your user pool:

```
aws cognito-idp create-user-pool-domain \
  --domain <UserPoolIdWithoutUnderscore> \
  --user-pool-id <UserPoolId> \
  --region us-west-2
```

###### Note

Remove any underscore from the `UserPoolId` when creating
the domain. For example, if your user pool ID is "us-west-2_gmSGKKGr9",
use "us-west-2gmSGKKGr9" as the domain. 6. Construct the discovery URL for your Cognito user pool:

```
https://cognito-idp.us-west-2.amazonaws.com/<UserPoolId>/.well-known/openid-configuration
```

7. Configure the Gateway Inbound Auth with the following values:
   1. **Discovery URL**: The URL
      constructed in the previous step
   2. **Allowed clients**: The client ID
      obtained when creating the user pool client

## Outbound

To configure Cognito user pools as an outbound resource provider, use the
following configuration:

```
{
  "name": "Cognito",
  "credentialProviderVendor": "CognitoOauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "your-client-id",
      "clientSecret": "your-client-secret",
      "authorizeEndpoint": "https://{your-cognito-domain}.auth.us-east-1.amazoncognito.com/oauth2/authorize",
      "tokenEndpoint": "https://{your-cognito-domain}.auth.us-east-1.amazoncognito.com/oauth2/token",
      "issuer": "https://cognito-idp.us-east-1.amazonaws.com/{your-user-pool-id}"
    }
  }
}
```

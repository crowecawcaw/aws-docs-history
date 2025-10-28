# Configuring Salesforce connections

To configure a Salesforce connection:

1. In AWS Secrets Manager, create a secret with the following details:
   1. For the JWT_TOKEN grant type - the secret should contain the JWT_TOKEN key with its value.
   2. For the AuthorizationCode grant type:
      1. For an AWS Managed connected app, an empty secret or a secret with some temporary value must be provided.
      2. For a customer managed connected app, the secret should contain the connected app `Consumer Secret` with `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as the key.

   3. Note: You must create a secret for your connection in AWS Glue.

2. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Connection type**, select Salesforce.
   2. Provide the INSTANCE_URL of the Salesforce instance you want to connect to.
   3. Provide the Salesforce environment.
   4. Select the AWS IAM role which AWS Glue can assume and has permissions for following actions:

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "secretsmanager:DescribeSecret",
    "secretsmanager:GetSecretValue",
    "secretsmanager:PutSecretValue",
    "ec2:CreateNetworkInterface",
    "ec2:DescribeNetworkInterfaces",
    "ec2:DeleteNetworkInterface"
    ],
    "Resource": "*"
    }
    ]
   }`

   ```

   5. Select the OAuth2 grant type which you want to use for the connections. The grant type determines how AWS Glue communicates with Salesforce to request access to your data. Your choice affects the requirements that you must meet before you create the connection. You can choose either of these types:
      - **JWT_BEARER Grant Type**: This grant type works well for automation scenarios as it allows a JSON Web Token (JWT) to be created up front with the permissions of a particular user in the Salesforce instance. The creator has control over how long the JWT is valid for. AWS Glue is able to use the JWT to obtain an access token which is used to call Salesforce APIs.

      This flow requires that the user has created a connected app in their Salesforce instance which enables issuing JWT-based access tokens for users.

      For information on creating a connected app for the JWT bearer OAuth flow, see [OAuth 2.0 JWT bearer flow for server-to-server integration](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_jwt_flow.htm "https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_jwt_flow.htm"). To set up the JWT bearer flow with the Salesforce connected app, see [Set up the JWT bearer OAuth flow for Salesforce](salesforce-setup-jwt-bearer-oauth.md "salesforce-setup-jwt-bearer-oauth.md").
      - **AUTHORIZATION_CODE Grant Type**: This grant type is considered a "three-legged" OAuth as it relies on redirecting users to the third-party authorization server to authenticate the user. It is used when creating connections via the AWS Glue console. The user creating a connection may by default rely on an AWS Glue connected app (AWS Glue managed client application) where they do not need to provide any OAuth related information except for their Salesforce instance URL. The AWS Glue console will redirect the user to Salesforce where the user must login and allow AWS Glue the requested permissions to access their Salesforce instance.

      Users may still opt to create their own connected app in Salesforce and provide their own client ID and client secret when creating connections through the AWS Glue console. In this scenario, they will still be redirected to Salesforce to login and authorize AWS Glue to access their resources.

      This grant type results in a refresh token and access token. The access token is short lived, and may be refreshed automatically without user interaction using the refresh token.

      For information on creating a connected app for the Authorization Code OAuth flow, see [Set up the Authorization Code flow for Salesforce](salesforce-setup-authorization-code-flow.md "salesforce-setup-authorization-code-flow.md").

   6. Select the `secretName` which you want to use for this connection in AWS Glue to store the OAuth 2.0 tokens.
   7. Select the network options if you want to use your network.

3. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
4. If providing network options, also grant the IAM role the following permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DeleteNetworkInterface"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Configuring Salesforce connections with the AWS CLI

You can create Salesforce connections using the AWS CLI:

```
aws glue create-connection --connection-input \
"{\"Name\": \"salesforce-conn1\",\"ConnectionType\": \"SALESFORCE\",\"ConnectionProperties\": {\"ROLE_ARN\": \"arn:aws:iam::123456789012:role/glue-role\",\"INSTANCE_URL\": \"https://example.my.salesforce.com\"},\"ValidateCredentials\": true,\"AuthenticationConfiguration\": {\"AuthenticationType\": \"OAUTH2\",\"SecretArn\": \"arn:aws:secretsmanager:us-east-1:123456789012:secret:salesforce-conn1-secret-IAmcdk\",\"OAuth2Properties\": {\"OAuth2GrantType\": \"JWT_BEARER\",\"TokenUrl\": \"https://login.salesforce.com/services/oauth2/token\"}}}" \
--endpoint-url https://glue.us-east-1.amazonaws.com \
--region us-east-1
```

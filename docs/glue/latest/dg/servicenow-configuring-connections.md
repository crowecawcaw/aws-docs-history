# Configuring ServiceNow connections

The grant type determines how AWS Glue communicates with ServiceNow to request access to your data. Your choice affects the requirements that you must meet before you create the connection. ServiceNow supports only the AUTHORIZATION_CODE grant type for OAuth 2.0.

- This grant type is considered "three-legged" OAuth as it relies on redirecting users to a third-party authorization server to authenticate the user. It is used when creating connections via the AWS Glue console. The AWS Glue console will redirect the user to ServiceNow where the user must login and allow AWS Glue the requested permissions to access their ServiceNow instance.
- Users may still opt to create their own connected app in ServiceNow and provide their own client id and client secret when creating connections through the AWS Glue console. In this scenario, they will still be redirected to ServiceNow to login and authorize AWS Glue to access their resources.
- This grant type results in a refresh token and access token. The access token is short lived, and may be refreshed automatically without user interaction using the refresh token.
- For public ServiceNow documentation on creating a connected app for Authorization Code OAuth flow, see [Set up OAuth](https://docs.servicenow.com/bundle/vancouver-platform-security/page/administer/security/task/t_SettingUpOAuth.html "https://docs.servicenow.com/bundle/vancouver-platform-security/page/administer/security/task/t_SettingUpOAuth.html").
  To configure a ServiceNow connection:

1. In AWS Secrets Manager, create a secret with the following details:
   1. For basic authentication, the Secret should contain the connected app Consumer Secret with `USERNAME` and `PASSWORD` as key.
   2. For an authorization code grant type, the Secret should contain the connected app Consumer Secret with `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.
   3. Note: You must create a secret per connection in AWS Glue.

2. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Connection type**, select ServiceNow.
   2. Provide the INSTANCE_URL of the ServiceNow instance you want to connect to.
   3. Select the AWS IAM role which AWS Glue can assume and has permissions for following actions:

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

   4. Select the **Authentication Type** you want to use for this connection in AWS Glue.
      1. Basic Auth: this auth type works well for automation scenarios as it allows to use username and password up front with the permissions of a particular user in the ServiceNow instance. AWS Glue is able to use the username and password to authenticate ServiceNow APIs. Enter the following inputs only in case of Basic Auth: `Username` and `Password`.
      2. OAuth2: enter the following inputs only in case of OAuth2: `ClientId`, `ClientSecret`, `Authorization URL`, `Authorization Token URL`.

   5. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens.
   6. Select the network options if you want to use your network.

3. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.

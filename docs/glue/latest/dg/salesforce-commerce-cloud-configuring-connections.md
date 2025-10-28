# Configuring Salesforce Commerce Cloud connections

Salesforce Commerce Cloud supports CLIENT CREDENTIALS grant type for OAuth2.

- This grant type is considered 2-legged OAuth 2.0 as it is used by clients to obtain an access token outside of the context of a user. AWS Glue
  is able to use the client Id and client secret to authenticate Salesforce Commerce Cloud APIs which are provided by custom services that
  you define.
- Each custom service is owned by an API-Only user which has a set of roles and permissions which authorize the service to perform specific
  actions. An access token is associated with a single custom service.
- This grant type results in an access token which is short lived, and may be renewed by calling identity endpoint.
- For more information on Salesforce Commerce Cloud documentation on generating the Client credentials, see
  [Salesforce documentation](https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization.html "https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization.html") .
  To configure an Salesforce Commerce Cloud connection:

1. In AWS Secrets Manager, create a secret with the following details. It is required to create a secret for
   each connection in AWS Glue.
   1. For customer managed connected app - Secret should contain the connected app Consumer Secret with
      USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET as key.

2. In AWS Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. Under Data Connections, choose **Create connection**.
   2. When selecting a **Data Source**, select Salesforce Commerce Cloud.
   3. Provide your Salesforce Commerce Cloud **Short Code**, **Organization ID**,
      and **Site ID**.
   4. Select the Salesforce Commerce Cloud Domain URL of your Salesforce Commerce Cloud account.
   5. Select the IAM role which AWS Glue can assume and has permissions for following actions:

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

   6. Provide the OAuth scopes - optional, User Managed Client Application ClientId of the Salesforce Commerce Cloud you want to
      connect to.
   7. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens.
   8. Select the network options if you want to use your network.

3. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
4. In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**.

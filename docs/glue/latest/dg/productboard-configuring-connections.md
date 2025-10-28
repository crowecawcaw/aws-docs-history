# Configuring Productboard connections

Productboard supports custom authentication and `OAuth2.0`. For
`OAuth2.0` Productboard supports the `AUTHORIZATION_CODE`
grant type.

- This grant type is considered “three-legged” `OAuth` as it relies
  on redirecting users to the third party authorization server to authenticate the
  user. It is used when creating connections via the AWS Glue Console. The user
  creating a connection may by default rely on a AWS Glue owned connected app where
  they do not need to provide any `OAuth` related information except
  for their Productboard Client ID and Client Secret. The AWS Glue Console will
  redirect the user to Productboard where the user must login and allow AWS Glue the
  requested permissions to access their Productboard instance.
- Users may still opt to create their own connected app in Productboard and
  provide their own Client ID and Client Secret when creating connections through
  the AWS Glue Console. In this scenario, they will still be redirected to
  Productboard to login and authorize AWS Glue to access their resources.
- This grant type results in a refresh token and access token. The access token
  is short lived, and may be refreshed automatically without user interaction
  using the refresh token.
- For public Productboard documentation on creating a connected app for
  `AUTHORIZATION_CODE OAuth` flow, see [How to integrate with Productboard via OAuth2 - developer
  documentation](https://developer.productboard.com/docs/how-to-integrate-with-productboard-via-oauth2-developer-documentation "https://developer.productboard.com/docs/how-to-integrate-with-productboard-via-oauth2-developer-documentation").
  To configure a Productboard connection:

1. In AWS Secrets Manager, create a secret with the following details:
   - For `OAuth` auth – For customer managed connected
     app: Secret should contain the connected app Consumer Secret with
     `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.
   - For `Custom auth` – For customer managed connected
     app: Secret should contain the connected app `JWT token` with
     `access_token` as key.

###### Note

It is a must to create a secret per connection in AWS Glue. 2. In AWS Glue Studio, create a connection under **Data Connections**
by following the steps below:

    1. When selecting a **Data Source**, select
     Productboard.
    2. Select the IAM role for which AWS Glue can assume and has permissions
     for following actions:



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
    3. Select Authentication Type to connect to data source:




    	* For `OAuth` auth – Provide the `Token
    	 URL`, and `User Managed Client Application
    	 ClientId` of the Productboard app.
    4. Select the `secretName` which you want to use for this
     connection in AWS Glue to put the tokens.
    5. Select the network options if you want to use your network.

3. Grant the IAM role associated with your AWS Glue job permission to read
   `secretName`.
4. In your AWS Glue job configuration, provide `connectionName` as an Additional network connection.

# Configuring Google Sheets connections

To configure a Google Sheet connection:

1. In AWS Secrets Manager, create a secret with the following details:
   1. For AuthorizationCode grant type:
      - For customer managed connected app – Secret should contain the
        connected app Consumer Secret with `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.

2. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Data Source**, select Google Sheets.
   2. Provide the Google Sheets environment.
      1. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens.
      2. Select the network options if you want to use your network.

3. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.

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

**AUTHORIZATION_CODE Grant Type**

This grant type is considered “three-legged” OAuth as it relies on redirecting users to the third party authorization server
to authenticate the user. It is used when creating connections via the AWS Glue Console. The AWS Glue Console will redirect the user to Google Sheets
where the user must login and allow AWS Glue the requested permissions to access their Google Sheets instance.

Users may opt to create their own connected app in Google Sheets and provide their own client id and client secret
when creating connections through the AWS Glue Console. In this scenario, they will still be redirected to Google Sheets to
login and authorize AWS Glue to access their resources.

This grant type results in a refresh token and access token. The access token is short lived, and may be refreshed
automatically without user interaction using the refresh token.

For more information, see [public Google Sheets documentation on creating a connected app for Authorization Code OAuth flow](https://developers.google.com/workspace/guides/create-credentials "https://developers.google.com/workspace/guides/create-credentials") .

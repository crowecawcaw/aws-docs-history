# Configuring Instagram Ads connections

Instagram Ads supports the AUTHORIZATION_CODE grant type for OAuth2.

- This grant type is considered three-legged OAuth as it relies on redirecting users to the third-party authorization server to authenticate the user. It is used when creating connections via the AWS Glue console.
- Users may opt to create their own connected app in Instagram Ads and provide their own client ID and client secret when creating connections through the AWS Glue console. In this scenario, they will still be redirected to Instagram Ads to login and authorize AWS Glue to access their resources.
- This grant type results in an access token. An expiring system user token is valid for 60 days from a generated or refreshed date. To create continuity, the developer should refresh the access token within 60 days. Failing to do so results in forfeiting the access token and requires the developer obtain a new one to regain API access. See [Refresh Access Token](https://developers.facebook.com/docs/marketing-api/system-users/install-apps-and-generate-tokens/ "https://developers.facebook.com/docs/marketing-api/system-users/install-apps-and-generate-tokens/").
  To configure a Instagram Ads connection:

1. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:
   1. When selecting a **Connection type**, select Instagram Ads.
   2. Select the AWS IAM role which AWS Glue can assume and has permissions for the following actions:

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

   3. Provide the User Managed Client Application Client ID.
   4. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens. The selected secret needs to have a key `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` with the value being the Client Secret from the connected app.
   5. Select the network options if you want to use your network.

2. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.

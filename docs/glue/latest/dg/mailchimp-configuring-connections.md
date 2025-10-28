# Configuring Mailchimp connections

Mailchimp supports following two types for authentication mechanism:

- Mailchimp supports the `AUTHORIZATION_CODE` grant type.
  - This grant type is considered “three-legged” `OAuth` as it
    relies on redirecting users to the third party authorization server to
    authenticate the user. It is used when creating connections via the
    AWS Glue Console. The user creating a connection may by default rely on a
    AWS Glue owned connected app where they do not need to provide any
    `OAuth` related information except for their Mailchimp
    Client ID and Client Secret. The AWS Glue Console will redirect the user to
    Mailchimp where the user must login and allow AWS Glue the requested
    permissions to access their Mailchimp instance.
  - Users may still opt to create their own connected app in Mailchimp and
    provide their own Client ID and Client Secret when creating connections
    through the AWS Glue Console. In this scenario, they will still be
    redirected to Mailchimp to login and authorize AWS Glue to access their
    resources.
  - For public Mailchimp documentation on creating a connected app for
    `AUTHORIZATION_CODE OAuth` flow, see [Access Data on Behalf of Other Users with OAuth 2](https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/?msockid=141ebf9ffb4d619525c3ad27fad660d6 "https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/?msockid=141ebf9ffb4d619525c3ad27fad660d6") .

- **Custom Auth** – For public Mailchimp
  documentation about generating the required API keys for custom authorization, see
  [About API Keys](https://mailchimp.com/en/help/about-api-keys/?msockid=310fd0fe09d16afe034fc5de08d76b01 "https://mailchimp.com/en/help/about-api-keys/?msockid=310fd0fe09d16afe034fc5de08d76b01").
  To configure a Mailchimp connection:

1. In AWS Secrets Manager, create a secret with the following details:
   - `OAuth` auth – For customer managed connected app:
     Secret should contain the connected app Consumer Secret with
     `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.
   - Custom auth – For customer managed connected app: Secret should
     contain the connected app Consumer Secret with “api_key” as key.

###### Note

It is a must to create a secret per connection in AWS Glue. 2. In AWS Glue Studio, create a connection under **Data Connections**
by following the steps below:

    1. Under **Connections**, select **Create
     connection**.
    2. When selecting a **Data Source**, select
     Mailchimp.
    3. Provide the Mailchimp `instanceUrl`.
    4. Select the IAM role for which AWS Glue can assume and has permissions
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
    5. Select Authentication Type to connect to Mailchimp:




    	* For `OAuth` auth – Provide the Token URL,
    	 User Managed Client Application ClientId of the Mailchimp that
    	 you want to connect to.
    	* For Custom auth – Select Authentication Type CUSTOM to
    	 connect to Mailchimp.
    6. Select the `secretName` which you want to use for this
     connection in AWS Glue to put the tokens.
    7. Select the network options if you want to use your network.

3. Grant the IAM role associated with your AWS Glue job permission to read
   `secretName`.
4. In your AWS Glue job configuration, provide `connectionName` as an Additional network connection.

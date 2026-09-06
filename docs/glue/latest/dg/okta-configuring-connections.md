

# Configuring Okta connections
<a name="okta-configuring-connections"></a>

 Okta supports two types of authentication mechanisms: 
+  OAuth auth: Okta supports the `AUTHORIZATION_CODE` grant type. 
  +  This grant type is considered “three-legged” OAuth as it relies on redirecting users to the third party authorization server to authenticate the user. It is used when creating connections via the AWS Glue Console. The AWS Glue Console will redirect the user to Okta where the user must login and allow AWS Glue the requested permissions to access their Okta instance. 
  +  Users may opt to create their own connected app in Okta and provide their own client ID and client secret when creating connections through the AWS Glue Console. In this scenario, they will still be redirected to Okta to login and authorize AWS Glue to access their resources. 
  +  This grant type results in a refresh token and access token. The access token is short lived, and may be refreshed automatically without user interaction using the refresh token. 
  +  For more information, see [ public Okta documentation on creating a connected app for Authorization Code OAuth flow ](https://developers.google.com/workspace/guides/create-credentials). 
+  Custom auth: 
  +  For public Okta documentation on generating the required API keys for custom authorization, see [ Okta documentation ](https://developer.okta.com/docs/guides/create-an-api-token/main/#create-the-token). 

To configure an Okta connection:

1.  In AWS Secrets Manager, create a secret with the following details. It is required to create a secret for each connection in AWS Glue. 

   1.  For OAuth auth: 
      +  For customer managed connected app – Secret should contain the connected app Consumer Secret with `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key. 

   1.  For Custom auth: 
      +  For customer managed connected app - Secret should contain the connected app Consumer Secret with `OktaApiToken` as key. 

1. In AWS Glue Studio, create a connection under **Data Connections** by following the steps below: 

   1.  Under Connections, choose **Create connection**. 

   1. When selecting a **Data Source**, select Okta.

   1. Provide your Okta subdomain.

   1. Select the Okta Domain URL of your Okta account.

   1.  Select the IAM role which AWS Glue can assume and has permissions for following actions: 

------
#### [ JSON ]

****  

      ```
      {
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
      }
      ```

------

   1.  Select Authentication Type to connect to data source. 

   1.  For OAuth2 authentication type, provide the **User Managed Client Application ClientId** of the Okta app. 

   1.  Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens. 

   1.  Select the network options if you want to use your network. 

1.  Grant the IAM role associated with your AWS Glue job permission to read `secretName`. 

1.  In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**. 
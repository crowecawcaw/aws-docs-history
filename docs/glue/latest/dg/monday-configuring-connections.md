

# Configuring Monday connections
<a name="monday-configuring-connections"></a>

Monday supports following two types for authentication mechanism:

1.  OAuth Auth: Monday supports AUTHORIZATION\_CODE grant type for OAuth2. 
   +  This grant type is considered “three-legged” OAuth as it relies on redirecting users to the third party authorization server to authenticate the user. It is used when creating connections via the AWS Glue Console. The user creating a connection may by default rely on a AWS Glue-owned connected app where they do not need to provide any OAuth related information except for the Monday instanceurl. The AWS Glue Console will redirect the user to Monday where the user must login and allow AWS Glue the requested permissions to access their Monday instance. 
   +  Users should opt to create their own connected app in Monday and provide their own client id and client secret when creating connections through the AWS Glue Console. In this scenario, they will still be redirected to Monday to login and authorize AWS Glue to access their resources. 
   +  This grant type results in a refresh token and access token. The access token is active for one hour, and may be refreshed automatically without user interaction using the refresh token. 
   +  For more information, see [documentation on creating a connected app for AUTHORIZATION\_CODE OAuth flow](https://developers.Monday.com/docs/api/v1/Oauth). 

1.  Custom Auth: 
   +  For public Monday documentation on generating the required API keys for custom authorization, see [ https://developer.monday.com/api-reference/docs/authentication\#api-token-permissions ](https://developer.monday.com/api-reference/docs/authentication#api-token-permissions). 

To configure a Monday connection:

1.  In AWS Secrets Manager, create a secret with the following details. It is required to create a secret for each connection in AWS Glue. 

   1.  For OAuth auth: 
      +  For customer managed connected app - Secret should contain the connected app Consumer Secret with USER\_MANAGED\_CLIENT\_APPLICATION\_CLIENT\_SECRET as key. 

   1.  For Custom auth: 
      +  For customer managed connected app - Secret should contain the connected app Consumer Secret with `personalAccessToken` as key. 

1. In AWS Glue Studio, create a connection under **Data Connections** by following the steps below: 

   1.  Under Data Connections, choose **Create connection**. 

   1. When selecting a **Data Source**, select Monday.

   1. Provide your Monday **instanceURL**.

   1.  Select the IAM role that AWS Glue can assume and has permissions for following actions: 

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

   1.  Select Authentication Type to connect to Monday 
      +  For OAuth auth: Provide the **Token URL** and **User Managed Client Application ClientId ** of the Monday you want to connect to. 
      +  For Custom auth: Select Authentication Type **CUSTOM** to connect to Monday. 

   1.  Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens. 

   1.  Select the network options if you want to use your network. 

1.  Grant the IAM role associated with your AWS Glue job permission to read `secretName`. Choose **Next**. 

1.  In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**. 


# Configuring Pendo connections
<a name="pendo-configuring-connections"></a>

Pendo supports custom authentication.

For public Pendo documentation on generating the required API keys for custom authorization, refer [Authentication – Pendo REST API Documentation](https://engageapi.pendo.io/?bash#getting-started) 

To configure a Pendo connection:

1. In AWS Secrets Manager, create a secret with the following details: 
   + For customer managed connected app - Secret should contain the connected app Consumer Secret with `apiKey` as the key. 
**Note**  
It is a must to create a secret per connection in AWS Glue.

1. In AWS Glue Studio, create a connection under **Data Connections** by following the steps below:

   1. When selecting a **Data Source**, select Pendo.

   1. Provide the `instanceUrl` of the Pendo instance you want to connect to.

   1. Select the IAM role for which AWS Glue can assume and has permissions for following actions: 

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

   1. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens. 

   1.  Select the network options if you want to use your network. 

1. Grant the IAM role associated with your AWS Glue job permission to read `secretName`. 

1. In your AWS Glue job configuration, provide `connectionName` as an Additional network connection.
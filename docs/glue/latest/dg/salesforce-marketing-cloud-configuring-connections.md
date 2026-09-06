

# Configuring Salesforce Marketing Cloud connections
<a name="salesforce-marketing-cloud-configuring-connections"></a>

Salesforce Marketing Cloud supports the CLIENT CREDENTIALS grant type for OAuth2.
+ This grant type is considered 2-legged OAuth 2.0 as it is used by clients to obtain an access token outside of the context of a user. AWS Glue is able to use the client ID and client secret to authenticate the Salesforce Marketing Cloud APIs which are provided by custom services that you define.
+ Each custom service is owned by an API-only user which has a set of roles and permissions which authorize the service to perform specific actions. An access token is associated with a single custom service.
+ This grant type results in an access token which is short lived, and may be renewed by calling an identity endpoint.
+ For public Salesforce Marketing Cloud documentation for OAuth 2.0 with client credentials, see [Set Up Your Development Environment for Enhanced Packages](https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/mc-dev-setup-enhanced.html).

To configure a Salesforce Marketing Cloud connection:

1. In AWS Secrets Manager, create a secret with the following details:

   1. For the customer managed connected app, the Secret should contain the connected app Consumer Secret with `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.

   1. Note: You must create a secret for your connections in AWS Glue.

1. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:

   1. When selecting a **Connection type**, select Salesforce Marketing Cloud.

   1. Provide the `Subdomain Endpoint` of the Salesforce Marketing Cloud you want to connect to.

   1. Select the AWS IAM role which AWS Glue can assume and has permissions for following actions:

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

   1. Select the network options if you want to use your network.

1. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
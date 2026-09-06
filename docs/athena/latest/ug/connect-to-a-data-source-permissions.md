

# Permissions to create and use a data source in Athena
<a name="connect-to-a-data-source-permissions"></a>

## AWS Glue Data Catalog federated connectors without Lambda permissions
<a name="connect-to-a-data-source-permissions-managed"></a>
+ **IAM principal permissions to invoke Athena API for connector management and querying**
  + **Amazon Athena access** – The AmazonAthenaFullAccess managed policy provides full access to Amazon Athena and scoped access to the dependencies needed to enable querying, writing results, and data management. For more information, see [AmazonAthenaFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonAthenaFullAccess.html) in the AWS Managed Policy Reference Guide. 
  + **AWS Glue connection management** – Permissions to create and manage AWS Glue connection objects.

    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "glue:GetConnection",
                    "glue:CreateConnection",
                    "glue:DeleteConnection",
                    "glue:UpdateConnection"
                ],
                "Resource": "*"
            }
        ]
    }
    ```
**Note**  
The example policy uses `"Resource": "*"` for simplicity. For production environments, scope permissions to specific resources where possible.
  + **AWS Lake Formation access** – Permissions to create an AWS Glue Catalog and use fine-grained access control. 

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
            "lakeformation:RegisterResource",
            "iam:ListRoles",
            "glue:CreateCatalog",
            "glue:GetCatalogs",
            "glue:GetCatalog"
          ],
          "Resource": "*"
        }
      ]
    }
    ```

------
+ **Glue Data Catalog IAM role**
  +  This section covers the permissions required for Athena to provision the infrastructure and query your data source. Amazon Athena Federated Query requires the following permissions in the role passed to **Glue Data Catalog IAM Role**. 
**Note**  
When you connect to a data source in a VPC, Athena creates an Elastic Network Interface (ENI) in your account within the specified VPC. The IAM role requires EC2 permissions to create, describe, and delete this network interface.

    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "glue:ManagedConnector",
                    "s3:PutObject",
                    "secretsmanager:DescribeSecret",
                    "secretsmanager:GetSecretValue",
                    "secretsmanager:PutSecretValue",
                    "ec2:CreateNetworkInterface",
                    "ec2:DeleteNetworkInterface",
                    "ec2:DescribeNetworkInterfaces",
                    "ec2:DescribeSubnets",
                    "ec2:DescribeSecurityGroups",
                    "ec2:DescribeVpcs",
                    "dynamodb:DescribeTable",
                    "dynamodb:ListTables",
                    "dynamodb:Scan",
                    "dynamodb:Query",
                    "dynamodb:GetItem",
                    "dynamodb:BatchGetItem"
                ],
                "Resource": "*"
            }
        ]
    }
    ```
**Note**  
The example policy uses `"Resource": "*"` for simplicity. For production environments, scope permissions to specific resources where possible. For example, scope Secrets Manager permissions to specific secret ARNs.  
**Explanation of permissions**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/athena/latest/ug/connect-to-a-data-source-permissions.html)

## AWS Glue Data Catalog federated connectors with Lambda permissions
<a name="connect-to-a-data-source-permissions-lambda"></a>
+ **IAM principal permissions to invoke Athena API for connector management and querying**
  + **Amazon Athena access** – The AmazonAthenaFullAccess managed policy provides full access to Amazon Athena and scoped access to the dependencies needed to enable querying, writing results, and data management. For more information, see [AmazonAthenaFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonAthenaFullAccess.html) in the AWS Managed Policy Reference Guide. 
  + **Connector management permissions** – The following permissions are needed to call the Athena DataCatalog API when using Lambda-based connectors. See [Permissions required to create connector and Athena catalog](athena-catalog-access.md).
  + **AWS Lake Formation access (if using Lake Formation)** – Permissions to create an AWS Glue Catalog and use fine-grained access control. 

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
            "lakeformation:RegisterResource",
            "iam:ListRoles",
            "glue:CreateCatalog",
            "glue:GetCatalogs",
            "glue:GetCatalog"
          ],
          "Resource": "*"
        }
      ]
    }
    ```

------

## Athena data catalog federated connectors permissions
<a name="connect-to-a-data-source-permissions-legacy"></a>
+ **IAM principal permissions to invoke Athena API for connector management and querying**
  + **Amazon Athena access** – The AmazonAthenaFullAccess managed policy provides full access to Amazon Athena and scoped access to the dependencies needed to enable querying, writing results, and data management. For more information, see [AmazonAthenaFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonAthenaFullAccess.html) in the AWS Managed Policy Reference Guide. 
  + **Connector management permissions** – The following permissions are needed to call the Athena DataCatalog API when using Lambda-based connectors. See [Permissions required to create connector and Athena catalog](athena-catalog-access.md).
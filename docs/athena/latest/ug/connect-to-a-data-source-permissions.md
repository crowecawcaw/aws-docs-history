# Permissions to create and use a data source in Athena

## AWS Glue Data Catalog federated connectors without Lambda permissions

- **IAM principal permissions to invoke Athena API for connector management and querying**

  - **Amazon Athena access** – The
    AmazonAthenaFullAccess managed policy provides full access to Amazon Athena and scoped
    access to the dependencies needed to enable querying, writing results, and data
    management. For more information, see [AmazonAthenaFullAccess](../../../aws-managed-policy/latest/reference/AmazonAthenaFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonAthenaFullAccess.md") in the AWS Managed Policy Reference
    Guide.
  - **AWS Glue connection management** –
    Permissions to create and manage AWS Glue connection objects.

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

  ###### Note

  The example policy uses `"Resource": "*"` for simplicity.
  For production environments, scope permissions to specific resources
  where possible.
  - **AWS Lake Formation access** –
    Permissions to create an AWS Glue Catalog and use fine-grained access control.

  JSON

  ```
  `{
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
  }`

  ```

- **Glue Data Catalog IAM role**

  - This section covers the permissions required for Athena to provision the infrastructure
    and query your data source. Amazon Athena Federated Query requires the following permissions in the role
    passed to **Glue Data Catalog IAM Role**.

  ###### Note

  When you connect to a data source in a VPC, Athena creates an Elastic Network
  Interface (ENI) in your account within the specified VPC. The IAM role requires
  EC2 permissions to create, describe, and delete this network interface.

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

  ###### Note

  The example policy uses `"Resource": "*"` for simplicity. For
  production environments, scope permissions to specific resources where possible.
  For example, scope Secrets Manager permissions to specific secret ARNs.

  Explanation of permissions| **Allowed actions** | **Explanation** | **Required** |
  | --- | --- | --- |
  | `<br>"glue:ManagedConnector"<br>` | Allows Athena to invoke the connector. | Required |
  | `<br>"s3:PutObject"<br>` | Allows the connector to write results to the spill bucket. Athena reads results from the spill bucket. | Required |
  | `<br>"secretsmanager:DescribeSecret",<br>"secretsmanager:GetSecretValue",<br>"secretsmanager:PutSecretValue"<br>` | Allows connectors to retrieve database credentials stored in AWS Secrets Manager. | Optional |
  | `<br>"ec2:DescribeSubnets",<br>"ec2:DescribeSecurityGroups",<br>"ec2:DescribeVpcs",<br>"ec2:CreateNetworkInterface",<br>"ec2:DescribeNetworkInterfaces",<br>"ec2:DeleteNetworkInterface"<br>` | Allows Athena to set up networking if the data source is within a VPC. | Optional |
  | `<br>"dynamodb:DescribeTable",<br>"dynamodb:ListTables",<br>"dynamodb:Scan",<br>"dynamodb:Query",<br>"dynamodb:GetItem",<br>"dynamodb:BatchGetItem"<br>` | Allows Athena to query a DynamoDB data source. | Optional |

## AWS Glue Data Catalog federated connectors with Lambda permissions

- **IAM principal permissions to invoke Athena API for connector management and querying**

  - **Amazon Athena access** – The
    AmazonAthenaFullAccess managed policy provides full access to Amazon Athena and scoped
    access to the dependencies needed to enable querying, writing results, and data
    management. For more information, see [AmazonAthenaFullAccess](../../../aws-managed-policy/latest/reference/AmazonAthenaFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonAthenaFullAccess.md") in the AWS Managed Policy Reference
    Guide.
  - **Connector management permissions** – The following permissions are needed to call the Athena DataCatalog API when using
    Lambda-based connectors. See
    [Permissions required to create connector and Athena catalog](athena-catalog-access.md "athena-catalog-access.md").
  - **AWS Lake Formation access (if using Lake Formation)** –
    Permissions to create an AWS Glue Catalog and use fine-grained access control.

  JSON

  ```
  `{
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
  }`

  ```

## Athena data catalog federated connectors permissions

- **IAM principal permissions to invoke Athena API for connector management and querying**

  - **Amazon Athena access** – The
    AmazonAthenaFullAccess managed policy provides full access to Amazon Athena and scoped
    access to the dependencies needed to enable querying, writing results, and data
    management. For more information, see [AmazonAthenaFullAccess](../../../aws-managed-policy/latest/reference/AmazonAthenaFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonAthenaFullAccess.md") in the AWS Managed Policy Reference
    Guide.
  - **Connector management permissions** – The following permissions are needed to call the Athena DataCatalog API when using
    Lambda-based connectors. See
    [Permissions required to create connector and Athena catalog](athena-catalog-access.md "athena-catalog-access.md").

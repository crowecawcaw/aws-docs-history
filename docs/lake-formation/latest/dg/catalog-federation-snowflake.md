# Federate to Snowflake Iceberg Catalog

AWS Glue Data Catalog federates to Snowflake using the OAuth2 credentials of a Snowflake service principal. You can use this federation to connect to Snowflake Horizon and Snowflake Polaris catalogs. This authentication mechanism allows Data Catalog to access the metadata of various objects (such as catalogs, databases, and tables) in your catalog, based on the privileges associated with the service principal. To ensure access to the right objects, it is essential to grant the service principal in Snowflake with the necessary permissions to read metadata of these objects.

## Prerequisites

Before you create a federated catalog in Data Catalog that is governed by Lake Formation, ensure you have the following permissions:

Your IAM principal (user or role) must have the following permissions:

- **Lake Formation permissions** – `lakeformation:RegisterResource`, `lakeformation:DescribeResource`
- **AWS Glue permissions** – `glue:CreateConnection`, `glue:CreateCatalog`, `glue:GetConnection`, `glue:PassConnection`
- **Secrets Manager permissions** – `secretsmanager:CreateSecret`, `secretsmanager:GetSecretValue`
- **IAM permissions** – `iam:CreateRole`, `iam:AttachRolePolicy`, `iam:PassRole`

You must be a Lake Formation data lake administrator or have `CREATE_CATALOG` permission on the Data Catalog

## Create Federated Catalog

1. Sign in to the the console and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. Choose the preferred AWS region in the top-right page section.
3. In the left navigation pane, choose Catalogs.
4. Choose **Create Catalog** to open the **Create Catalog Workflow**.
5. In **Choose data source** step, select Snowflake from the available options.
6. In **Set catalog details** step, you provide three information - catalog details, connection details, and registration details.
7. In **catalog details** container, provide a unique name to your AWS Glue federated catalog and enter the name of the existing Snowflake catalog.
8. In **connections details** container, you can either choose from an existing connection that you have access or provide configuration to create a new connector.
9. New connection configurations include:
   - Connection Name – A unique name of the AWS Glue connection object.
   - Instance URL – The endpoint URL of your existing Snowflake account.
   - Authentication – Specify the authentication configuration that AWS Glue uses to connect to remote catalog server. AWS Glue supports both OAuth2 and Custom authentication.
   - Token URL – Specify the URL of remote catalog's identity provider.
   - OAuth2 Client ID – Specify the Client ID of the OAuth2 credential associated with your remote catalog.
   - Secret – Store and use OAuth2 client secret using AWS Secrets Manager or enter the secret value in textbox. When you enter the secret manually in console, AWS Glue creates the secret on your behalf.
   - Token URL Scope – Specify the OAuth scope for authentication.
   - Catalog Casing Filter – Choose whether to bring lowercase or uppercase objects from your remote catalog to Data Catalog.

10. Create an IAM role that AWS Glue and Lake Formation service principals can use to access secret in AWS Secrets Manager and Amazon S3 locations of remote Iceberg tables respectively. Select the IAM role in the registration dropdown. Refer to step 2 and 3 in following CLI section for IAM policy details.
11. Select Test Connection to test whether your connection properties and IAM role access are configured correctly.
12. Select **Next** to review your settings.
13. Select **Create Catalog** in review page.

14. **Create an AWS Secrets Manager secret**

The AWS Glue connector supports two authentication types - **OAuth2** and **Custom**. When using OAuth2 option, use AWS Secrets Manager to store client secret of the Snowflake service principal. You will later use this secret when creating the AWS Glue Connection. For Custom authentication, use AWS Secrets Manager to store and retrieve the access token.

In the following example, replace `your-snowflake-secret`, `client_secret`, `region` with your own information.

```
aws secretsmanager create-secret \
--name `your-snowflake-secret` \
--description "Snowflake secret" \
--secret-string '{
"USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET": "`client_secret`"
}' \
--region `region`
```

###### Note

`USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` is a reserved keyword that AWS Glue uses to refer to a client secret value in the secret. Use the same keyword when you are creating the secret in Lake Formation console too. 2. **Create an IAM role which gives AWS Glue connection object access to secret created in previous step**

The AWS Glue connection object requires access to the AWS Secrets Manager secret when you use AWS Secrets Manager to store, retrieve, and refresh your OAuth secret token. The AWS Glue connection object also requires access to create, describe, and use the Amazon VPC network interfaces when you use a Amazon VPC endpoint to restrict connectivity to your Snowflake account.

Create an IAM policy and attach it to an IAM role. Add AWS Glue service principal to the trust policy.

In the following example, replace `your-secrets-manager-ARN`, `your-vpc-id`, and `your-subnet-id1` with your own information.

###### Example IAM Policy

```
{
    "Version": "2012-10-17",
    "Statement": [{
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue",
                "secretsmanager:DescribeSecret",
                "secretsmanager:PutSecretValue"
            ],
            "Resource": [
                "`your-secrets-manager-ARN`"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateNetworkInterface",
                "ec2:DeleteNetworkInterface",
                "ec2:DescribeNetworkInterfaces"
            ],
            "Resource": "*",
            "Condition": {
                "ArnEquals": {
                    "ec2:Vpc": "arn:aws:ec2:region:account-id:vpc/`your-vpc-id`",
                    "ec2:Subnet": ["arn:aws:ec2:region:account-id:subnet/`your-subnet-id1`"]
                }
            }
        }
    ]
}
```

###### Example Trust Policy

```
{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": {
            "Service": "glue.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
    }]
}
```

3. **Create an IAM policy that gives Lake Formation read access to catalog's Amazon S3 location**

As the catalog owner of a federated catalog in Data Catalog, you use Lake Formation to grant coarse-grained table access, fine-grained - column-level, row-level, and cell-level - access, and tag-based access to your data teams. Lake Formation uses an IAM role that gives it access to the underlying Amazon S3 locations of your remote Iceberg tables. This access allows Lake Formation to vend scoped access credentials to analytics engines querying remote tables.

Create IAM policy and attach to an IAM role. Add Lake Formation service principal to the role trust policy.

In the following example, replace `amzn-s3-demo-bucketN` and `your-kms-key` with your own information.

###### Example IAM Policy

```
{
    "Version": "2012-10-17",
    "Statement": [{
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket1`/*",
                "arn:aws:s3:::`amzn-s3-demo-bucket2`/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket1`",
                "arn:aws:s3:::`amzn-s3-demo-bucket2`"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:Encrypt"
            ],
            "Resource": [
                "`your-kms-key`"
            ]
        }
    ]
}
```

###### Example Trust Policy

```
{
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "",
        "Effect": "Allow",
        "Principal": {
            "Service": "lakeformation.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
    }]
}
```

###### Note

When you use Lake Formation console to create a federated catalog, the console uses a single IAM role with both policies attached to complete setup. 4. **Create an AWS Glue connection object**

AWS Glue connector supports OAuth2 and Custom authentication methods. Data Catalog connection object supports `CATALOG_CASING_FILTER` configuration that allows you to bring either lowercase or uppercase objects in your remote catalog to Data Catalog.

The following example uses OAuth2 authentication configuration to create an AWS Glue connection. Replace `highlighted sections` with your information.

```
aws glue create-connection \
    --connection-input '{
"Name": "`your-glue-connection-to-snowflake-account`",
"ConnectionType": "SNOWFLAKEICEBERGRESTCATALOG",
"ConnectionProperties": {
    "INSTANCE_URL": "`your-snowflake-account-URL`",
    "ROLE_ARN": "`your-IAM-role-for-secrets-and-VPC-access`",
    "CATALOG_CASING_FILTER": "LOWERCASE_ONLY"
},
"AuthenticationConfiguration": {
    "AuthenticationType": "OAUTH2",
    "OAuth2Properties": {
        "OAuth2GrantType": "CLIENT_CREDENTIALS",
        "TokenUrl": "`your-internal-or-external-token-server-url`",
        "OAuth2ClientApplication": {
            "UserManagedClientApplicationClientId": "`our-client-id`"
        },
        "TokenUrlParametersMap": {
            "scope": "all-apis"
        }
    },
    "SecretArn": "arn:aws:secretsmanager:`your-aws-region`:`your-aws-account-id`:secret:`snowflake-secret`"
}
}'
```

5. **Register AWS Glue connection as a Lake Formation resource**

Using the AWS Glue connection object (created in Step 4) and IAM role (created in Step 3), you can now register the AWS Glue connection object as a Lake Formation managed resource.

Replace `your-glue-connector-arn` and `your-IAM-role-ARN-having-LF-access` with your information.

```
aws lakeformation register-resource \
    --resource-arn `your-glue-connector-arn` \
    --role-arn `your-IAM-role-ARN-having-LF-access` \
    --with-federation \
    --with-privileged-access
```

6. **Create a federated catalog in Data Catalog**

After creating an AWS Glue connection object and registering it with Lake Formation, you can create a federated catalog in the Data Catalog:

Provide the federated catalog a unique name at `your-federated-catalog-name`, reference the catalog in Snowflake at `catalog-name-in-Snowflake`, and input connection name created earlier at `your-glue-connection-name`.

```
aws glue create-catalog \
    --name `your-federated-catalog-name` \
    --catalog-input '{
    "FederatedCatalog": {
        "Identifier": `catalog-name-in-Snowflake`",
        "ConnectionName": `your-glue-connection-name`"
    },
    "CreateTableDefaultPermissions": [],
    "CreateDatabaseDefaultPermissions": []
}'
```

## Considerations when integrating with Snowflake

- When you drop resources (like databases and tables) in Snowflake, Lake Formation does not automatically revoke the permissions granted on that federated resource. To remove the access permissions, you need to explicitly revoke the permissions that were previously granted on the federated resource using Lake Formation.
- When you mount remote catalog with `CATALOG_CASING_FILTER='UPPERCASE_ONLY'` configuration, databases and tables with uppercase identifiers are federated but objects with lowercase identifiers are not.
- You can reuse the same AWS Glue connection to create multiple federated catalogs. Deleting a catalog will not delete the associated connection. To delete a connection, please use AWS CLI `aws glue delete-connection` command and ensure all associated catalogs are deleted first.
- Nested namespaces in Polaris catalog are not supported. That is, catalog federation can access remote Iceberg tables that follow a 3-part notation `catalog.database.table`.

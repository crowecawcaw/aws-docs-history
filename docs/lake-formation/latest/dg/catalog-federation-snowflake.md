

# Federate to Snowflake Iceberg Catalog
<a name="catalog-federation-snowflake"></a>

AWS Glue Data Catalog connects to Snowflake using the OAuth2 credentials of a Snowflake service principal. You can use this feature to connect to Snowflake Horizon and Snowflake Polaris catalogs. AWS Glue Data Catalog requires access to the metadata of various objects (such as catalogs, databases, and tables) in your catalog and uses the privileges associated with the service principal. To ensure access to the right objects, it is essential you configure the service principal in Snowflake with the necessary permissions to read metadata of these objects.

AWS Glue Data Catalog supports two access delegation modes, and you can configure the federated catalog to use credentials vended by either Snowflake (source-vended) or the IAM role that Lake Formation uses (aws-vended). In the former mode, Snowflake Horizon issues temporary Amazon S3 credentials scoped to each table, and AWS Lake Formation passes those credentials to your analytics engine. The IAM role you register with Lake Formation doesn't need access to the Amazon S3 buckets that store your Snowflake tables. For a comparison of the two access delegation modes, see [Access delegation modes](catalog-federation.md#access-delegation-modes).

## Prerequisites
<a name="catalog-federation-snowflake-prerequisites"></a>

Complete these steps in Snowflake and store its access token before you create the federated catalog.

1. **Grant the Snowflake role access to the data**

   Grant the Snowflake role `USAGE` on the database and schema, and `SELECT` on the tables that you want to federate.

1. **Create an access token**

   Create an access token that lets AWS Glue use this role.

1. **(Optional) Store the token in AWS Secrets Manager**

   Store the access credentials in AWS Secrets Manager under the key `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET`. The CLI secret step later in this topic shows the `create-secret` command.

Before you create a federated catalog in Data Catalog that is governed by Lake Formation, ensure you have the following permissions:

Your IAM principal (user or role) must have the following permissions:
+ **Lake Formation permissions** – `lakeformation:RegisterResource`, `lakeformation:DescribeResource`
+ **AWS Glue permissions** – `glue:CreateConnection`, `glue:CreateCatalog`, `glue:GetConnection`, `glue:PassConnection`
+ **Secrets Manager permissions** – `secretsmanager:CreateSecret`, `secretsmanager:GetSecretValue`
+ **IAM permissions** – `iam:CreateRole`, `iam:AttachRolePolicy`, `iam:PassRole`

You must be a Lake Formation data lake administrator or have `CREATE_CATALOG` permission on the Data Catalog

## Create Federated Catalog
<a name="catalog-federation-snowflake-create"></a>

### Using Console
<a name="catalog-federation-snowflake-console"></a>

1. Sign in to the console and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. Choose the preferred AWS Region in the Region selector.

1. In the left navigation pane, choose Catalogs.

1. Choose **Create Catalog** to open the **Create Catalog Workflow**.

1. In **Choose data source** step, select Snowflake Horizon Catalog from the available options.

1. In **Set catalog details** step, you provide three information - catalog details, connection details, and registration details.

1. In **catalog details** container, provide a unique name to your AWS Glue federated catalog and enter the name of the existing Snowflake catalog (the Snowflake database name).

1. In **connections details** container, you can either choose from an existing connection that you have access or provide configuration to create a new connector.

1. New connection configurations include:
   + Connection Name – A unique name of the AWS Glue connection object.
   + Workspace URL – Enter the account root only, in the form `https://<account>.snowflakecomputing.com`. Don't include the `/polaris/api/catalog` path; the console rejects it.
   + Authentication – Specify the authentication configuration that AWS Glue uses to connect to remote catalog server. AWS Glue supports both OAuth2 and Custom authentication.
   + Token URL – Specify `https://<account>.snowflakecomputing.com/polaris/api/catalog/v1/oauth/tokens`.
   + OAuth2 Client ID – Leave this blank. When Snowflake is the OAuth server, don't provide a client ID; the token request authenticates using only the client secret stored in AWS Secrets Manager.
   + Secret – Store and use OAuth2 client secret using AWS Secrets Manager or enter the secret value in textbox. When you enter the secret manually in console, AWS Glue creates the secret on your behalf.
   + Token URL Scope – Specify `session:role:<snowflake-role>`.
   + Catalog Casing Filter – Choose whether to bring lowercase or uppercase objects from your remote catalog to Data Catalog.

1. Under **Access delegation mode**, choose **Vended credential** to use credentials issued by Snowflake. Choose **Registered role** to have Lake Formation issue credentials using your IAM role.

1. In **Register Glue connection with Lake Formation**, choose how to provide the IAM role:
   + **Create and use a default role** – Lake Formation creates the role when you create the catalog. The console shows the role name, `LakeFormationIRC-<connection-name>-<suffix>`, before you create. The role's permissions policy allows `secretsmanager:GetSecretValue`, `secretsmanager:DescribeSecret`, and `secretsmanager:PutSecretValue` on the selected secret only. Its trust policy lets only AWS Glue and Lake Formation in this account and Region assume the role.
   + **Use an existing role** – Choose a role that you created. For the required policies, see step 2 in [Using the AWS CLI](#snowflake-federation-cli), and step 3 if you choose **Registered role**. With **Vended credential**, the role needs access only to the secret (and to the Amazon VPC network interfaces, if you use Amazon VPC). It doesn't need Amazon S3 permissions.

1. (Optional) Choose **Run test** to confirm your connection properties and IAM role access are configured correctly. **Run test** isn't available when you use the default role that Lake Formation creates for you or when you are using Amazon VPC to connect to Snowflake.

1. Select **Next** to review your settings.

1. Select **Create Catalog** in review page.

### Using CLI
<a name="snowflake-federation-cli"></a>

1. <a name="snowflake-step-1"></a>**Create an AWS Secrets Manager secret**

   The AWS Glue connector supports two authentication types - **OAuth2** and **Custom**. When using OAuth2 option, use AWS Secrets Manager to store client secret of the Snowflake service principal. You will later use this secret when creating the AWS Glue Connection. For Custom authentication, use AWS Secrets Manager to store and retrieve the access token.

   In the following example, replace `{{your-snowflake-secret}}`, `{{client_secret}}`, `{{region}}` with your own information.

   ```
   aws secretsmanager create-secret \
   --name {{your-snowflake-secret}} \
   --description "Snowflake secret" \
   --secret-string '{
   "USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET": "{{client_secret}}"
   }' \
   --region {{region}}
   ```
**Note**  
`USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` is a reserved keyword that AWS Glue uses to refer to a client secret value in the secret. Use the same keyword when you are creating the secret in Lake Formation console too.

1. <a name="snowflake-step-2"></a>**Create an IAM role which gives AWS Glue connection object access to secret created in previous step**

   The AWS Glue connection object requires access to the AWS Secrets Manager secret when you use AWS Secrets Manager to store, retrieve, and refresh your OAuth secret token. The AWS Glue connection object also requires access to create, describe, and use the Amazon VPC network interfaces when you use a Amazon VPC endpoint to restrict connectivity to your Snowflake account.

   Create an IAM policy and attach it to an IAM role. Add AWS Glue service principal to the trust policy.

   In the following example, replace `{{your-secrets-manager-ARN}}`, `{{your-vpc-id}}`, and `{{your-subnet-id1}}` with your own information.  
**Example IAM Policy**  

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
                   "{{your-secrets-manager-ARN}}"
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
                       "ec2:Vpc": "arn:aws:ec2:region:account-id:vpc/{{your-vpc-id}}",
                       "ec2:Subnet": ["arn:aws:ec2:region:account-id:subnet/{{your-subnet-id1}}"]
                   }
               }
           }
       ]
   }
   ```  
**Example Trust Policy**  

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

1. <a name="snowflake-step-3"></a>**Create an IAM policy that gives Lake Formation read access to catalog's Amazon S3 location**

   Skip this step if you use vended-credential mode. In that mode, the remote catalog issues the Amazon S3 credentials, so the IAM role doesn't need access to the table data in Amazon S3.

   As the catalog owner of a federated catalog in Data Catalog, you use Lake Formation to grant coarse-grained table access, fine-grained - column-level, row-level, and cell-level - access, and tag-based access to your data teams. Lake Formation uses an IAM role that gives it access to the underlying Amazon S3 locations of your remote Iceberg tables. This access allows Lake Formation to vend scoped access credentials to analytics engines querying remote tables.

   Create IAM policy and attach to an IAM role. Add Lake Formation service principal to the role trust policy.

   In the following example, replace `{{amzn-s3-demo-bucketN}}` and `{{your-kms-key}}` with your own information.  
**Example IAM Policy**  

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [{
               "Effect": "Allow",
               "Action": [
                   "s3:GetObject"
               ],
               "Resource": [
                   "arn:aws:s3:::{{amzn-s3-demo-bucket1}}/*",
                   "arn:aws:s3:::{{amzn-s3-demo-bucket2}}/*"
               ]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "s3:ListBucket"
               ],
               "Resource": [
                   "arn:aws:s3:::{{amzn-s3-demo-bucket1}}",
                   "arn:aws:s3:::{{amzn-s3-demo-bucket2}}"
               ]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "kms:Decrypt",
                   "kms:Encrypt"
               ],
               "Resource": [
                   "{{your-kms-key}}"
               ]
           }
       ]
   }
   ```  
**Example Trust Policy**  

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
**Note**  
When you use Lake Formation console to create a federated catalog, the console uses a single IAM role with both policies attached to complete setup.

1. <a name="snowflake-step-4"></a>**Create an AWS Glue connection object**

   AWS Glue connector supports OAuth2 and Custom authentication methods. Data Catalog connection object supports `CATALOG_CASING_FILTER` configuration that allows you to bring either lowercase or uppercase objects in your remote catalog to Data Catalog.

   The following example uses OAuth2 authentication configuration to create an AWS Glue connection. Replace `{{highlighted sections}}` with your information.

   ```
   aws glue create-connection \
       --connection-input '{
   "Name": "{{your-glue-connection-to-snowflake-account}}",
   "ConnectionType": "SNOWFLAKEICEBERGRESTCATALOG",
   "ConnectionProperties": {
       "INSTANCE_URL": "https://<account>.snowflakecomputing.com",
       "ROLE_ARN": "{{your-IAM-role-for-secrets-and-VPC-access}}",
       "CREDENTIAL_VENDING_MODE": "SOURCE_VENDED",
       "CATALOG_CASING_FILTER": "UPPERCASE_ONLY"
   },
   "AuthenticationConfiguration": {
       "AuthenticationType": "OAUTH2",
       "OAuth2Properties": {
           "OAuth2GrantType": "CLIENT_CREDENTIALS",
           "TokenUrl": "https://<account>.snowflakecomputing.com/polaris/api/catalog/v1/oauth/tokens",
           "TokenUrlParametersMap": {
               "scope": "session:role:<snowflake-role>"
           }
       },
       "SecretArn": "arn:aws:secretsmanager:{{your-aws-region}}:{{your-aws-account-id}}:secret:{{snowflake-secret}}"
   }
   }'
   ```
**Note**  
Omit `OAuth2ClientApplication`. When Snowflake is the OAuth server, the token request authenticates using only the client secret (the programmatic access token) stored in AWS Secrets Manager, without sending a client ID.

1. <a name="snowflake-step-5"></a>**Register AWS Glue connection as a Lake Formation resource**

   Using the AWS Glue connection object (created in Step 4) and IAM role (created in Step 3), you can now register the AWS Glue connection object as a Lake Formation managed resource.

   Replace `{{your-glue-connector-arn}}` and `{{your-IAM-role-ARN-having-LF-access}}` with your information.

   ```
   aws lakeformation register-resource \
       --resource-arn {{your-glue-connector-arn}} \
       --role-arn {{your-IAM-role-ARN-having-LF-access}} \
       --with-federation \
       --with-privileged-access
   ```
**Note**  
Register the connection before you create the catalog. Otherwise, `create-catalog` fails with `The data source … is not registered`.

1. <a name="snowflake-step-6"></a>**Create a federated catalog in Data Catalog**

   After creating an AWS Glue connection object and registering it with Lake Formation, you can create a federated catalog in the Data Catalog:

   Provide a unique name for the federated catalog at {{<your-federated-catalog-name>}}, reference the Snowflake database at {{<catalog-name-in-Snowflake>}}, and enter the connection name you created earlier at {{<your-glue-connection-name>}}.

   ```
   aws glue create-catalog \
     --name {{<your-federated-catalog-name>}} \
     --catalog-input '{
     "FederatedCatalog": {
       "Identifier": "{{<catalog-name-in-Snowflake>}}",
       "ConnectionName": "{{<your-glue-connection-name>}}"
     },
     "CreateTableDefaultPermissions": [],
     "CreateDatabaseDefaultPermissions": []
   }'
   ```

1. <a name="snowflake-step-7"></a>**Grant Lake Formation permissions**

   Catalog-level grants don't carry down to federated databases and tables. Grant `DESCRIBE` on the database, and `SELECT` and `DESCRIBE` on the table wildcard, to each principal that queries the catalog.

1. <a name="snowflake-step-8"></a>**Query the federated catalog**

   Query the federated catalog from your analytics engine. For example, in Amazon Athena:

   ```
   SELECT * FROM "<federated-catalog>"."<schema>"."<table>" LIMIT 10;
   ```

## Considerations when integrating with Snowflake
<a name="snowflake-considerations"></a>
+ When you drop resources (like databases and tables) in Snowflake, Lake Formation does not automatically revoke the permissions granted on that federated resource. To remove the access permissions, you need to explicitly revoke the permissions that were previously granted on the federated resource using Lake Formation.
+ When you mount remote catalog with `CATALOG_CASING_FILTER='UPPERCASE_ONLY'` configuration, databases and tables with uppercase identifiers are federated but objects with lowercase identifiers are not.
+ You can reuse the same AWS Glue connection to create multiple federated catalogs. Deleting a catalog will not delete the associated connection. To delete a connection, please use AWS CLI `aws glue delete-connection` command and ensure all associated catalogs are deleted first.
+ Nested namespaces in Polaris catalog are not supported. That is, catalog federation can access remote Iceberg tables that follow a 3-part notation `catalog.database.table`.
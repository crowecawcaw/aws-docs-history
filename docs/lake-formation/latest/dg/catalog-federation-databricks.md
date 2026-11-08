

# Federate to Databricks Unity Catalog
<a name="catalog-federation-databricks"></a>

AWS Glue Data Catalog federates to Databricks using the OAuth2 credentials of a Databricks service principal. This authentication mechanism allows AWS Glue Data Catalog to access the metadata of various objects (such as catalogs, databases, and tables) in Databricks Unity Catalog, based on the privileges associated with the service principal. To ensure access to the right objects, it is essential to grant the service principal with the necessary permissions in Databricks to read metadata of these objects.

Catalog federation enables discovery and query of Iceberg tables in your Databricks Unity Catalog. To read delta tables, please ensure Iceberg metadata is available for these tables using Uniform. Follow the Databricks tutorial and documentation to create the service principal and associated privileges in your Databricks workspace.

AWS Glue Data Catalog supports two access delegation modes, and you can configure the federated catalog to use credentials vended by either Databricks (source-vended) or the IAM role that Lake Formation uses (aws-vended). In the former mode, Databricks issues temporary Amazon S3 credentials scoped to each table, and AWS Lake Formation passes those credentials to your analytics engine. The IAM role you register with Lake Formation doesn't need access to the Amazon S3 buckets that store your Databricks tables. For a comparison of the two access delegation modes, see [Access delegation modes](catalog-federation.md#access-delegation-modes).

## Prerequisites
<a name="catalog-federation-databricks-prerequisites"></a>

Complete these steps in your Databricks workspace before you create the federated catalog.

1. **Make tables readable as Iceberg**

   Federation reads Iceberg metadata. For Delta tables, turn on Uniform. Column mapping is required for Iceberg compatibility, so set it in the same statement.

1. **Create a service principal and an OAuth secret**

   In the workspace settings, add a service principal, then generate an OAuth secret. Choose the API scopes the secret allows, such as `unity catalog sql`. Refer to the Databricks documentation for valid scope values. Record the application ID (client ID), the secret, and the scopes you chose.

1. **Ensure external data access is configured for the metastore**

1. **Grant Unity Catalog privileges to the service principal**

Before you create a federated catalog in Data Catalog that is governed by Lake Formation, ensure you have the following permissions:

Your IAM principal (user or role) must have the following permissions:
+ **Lake Formation permissions** – `lakeformation:RegisterResource`, `lakeformation:DescribeResource`
+ **AWS Glue permissions** – `glue:CreateConnection`, `glue:CreateCatalog`, `glue:GetConnection`, `glue:PassConnection`
+ **Secrets Manager permissions** – `secretsmanager:CreateSecret`, `secretsmanager:GetSecretValue`
+ **IAM permissions** – `iam:CreateRole`, `iam:AttachRolePolicy`, `iam:PassRole`

You must be a Lake Formation data lake administrator or have `CREATE_CATALOG` permission on the Data Catalog.

## Create a federated catalog
<a name="catalog-federation-databricks-create"></a>

### Using the console
<a name="catalog-federation-databricks-console"></a>

1. Sign in to the console and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. Choose the preferred AWS Region in the Region selector.

1. In the navigation pane, choose **Catalogs**.

1. Choose **Create Catalog** to open the **Create Catalog Workflow**.

1. In the **Choose data source** step, choose Databricks Unity Catalog from the available options.

1. In the **Set catalog details** step, you provide three types of information: catalog details, connection details, and registration details.

1. In the **catalog details** container, provide a unique name for your AWS Glue federated catalog, and enter the name of the existing Databricks catalog.

1. In the **connections details** container, you can either choose an existing connection that you have access to, or provide configuration to create a new connector.

1. New connection configurations include:
   + Connection Name – A unique name of the AWS Glue connection object.
   + Workspace URL – The endpoint URL of your existing Databricks workspace.
   + Authentication – Specify the authentication configuration that AWS Glue uses to connect to the remote catalog server. AWS Glue supports both OAuth2 and Custom authentication.
   + Token URL – Specify the URL of the remote catalog's identity provider.
   + OAuth2 Client ID – Specify the Client ID of the OAuth2 credential associated with your remote catalog.
   + Secret – Store and use the OAuth2 client secret by using AWS Secrets Manager, or enter the secret value in the text box. When you enter the secret manually in the console, AWS Glue creates the secret on your behalf.
   + Token URL Scope – Specify the OAuth scope for authentication.

1. Under **Access delegation mode**, choose **Vended credential** to use credentials issued by Databricks. Choose **Registered role** to have Lake Formation issue credentials using your IAM role.

1. In **Register Glue connection with Lake Formation**, choose how to provide the IAM role:
   + **Create and use a default role** – Lake Formation creates the role when you create the catalog. The console shows the role name, `LakeFormationIRC-<connection-name>-<suffix>`, before you create. The role's permissions policy allows `secretsmanager:GetSecretValue`, `secretsmanager:DescribeSecret`, and `secretsmanager:PutSecretValue` on the selected secret only. Its trust policy lets only AWS Glue and Lake Formation in this account and Region assume the role.
   + **Use an existing role** – Choose a role that you created. For the required policies, see step 2 in [Using the AWS CLI](#catalog-federation-databricks-cli), and step 3 if you choose **Registered role**. With **Vended credential**, the role needs access only to the secret (and to the Amazon VPC network interfaces, if you use Amazon VPC). It doesn't need Amazon S3 permissions.

1. (Optional) Choose **Run test** to confirm your connection properties and IAM role access are configured correctly. A successful test means AWS Glue exchanged the client secret for a token and reached the Databricks Iceberg REST endpoint. **Run test** isn't available when you use the default role that Lake Formation creates for you or when you are using Amazon VPC to connect to Databricks.

1. Choose **Next** to review your settings.

1. Choose **Create Catalog** on the review page. The console creates the AWS Glue connection, registers it with Lake Formation, and creates the federated catalog in a single step.

### Using the AWS CLI
<a name="catalog-federation-databricks-cli"></a>

1. <a name="databricks-step-1"></a>**Create an AWS Secrets Manager secret**

   The AWS Glue connector supports two authentication types: **OAuth2** and **Custom**. When you use the OAuth2 option, use AWS Secrets Manager to store the client secret of the Databricks service principal. You use this secret later when you create the AWS Glue connection. For Custom authentication, use AWS Secrets Manager to store and retrieve the access token.

   In the following example, replace `{{<databricks-secret>}}`, `{{<client_secret>}}`, `{{<region>}}` with your own information.

   ```
   aws secretsmanager create-secret \
   --name {{<databricks-secret>}} \
   --description "Databricks secret" \
   --secret-string '{
   "USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET": "{{<client_secret>}}"
   }' \
   --region {{<region>}}
   ```
**Note**  
`USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` is a reserved keyword that AWS Glue uses to refer to a client secret value in the secret. Use the same keyword when you create the secret in the Lake Formation console. AWS Glue adds and refreshes the OAuth token keys in the secret itself, so you don't need to create placeholder token keys.

1. <a name="databricks-step-2"></a>**Create an IAM role that gives the AWS Glue connection object access to the secret created in the previous step**

   The AWS Glue connection object requires access to the AWS Secrets Manager secret when you use AWS Secrets Manager to store, retrieve, and refresh your OAuth secret token. The AWS Glue connection object also requires access to create, describe, and use the Amazon VPC network interfaces when you use a Amazon VPC endpoint to restrict connectivity to your Databricks workspace.

   Create an IAM policy and attach it to an IAM role. Add both the AWS Glue and Lake Formation service principals to the trust policy, so a single IAM role serves both AWS Glue and Lake Formation. The secret actions shown (`GetSecretValue`, `DescribeSecret`, `PutSecretValue`) are the minimum required, and no secret resource policy or `UpdateSecret` permission is needed.

   In the following example, replace `{{<your-secrets-manager-ARN>}}`, `{{<your-vpc-id>}}`, and `{{<your-subnet-id1>}}` with your own information.  
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
                   "{{<your-secrets-manager-ARN>}}"
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
                       "ec2:Vpc": "arn:aws:ec2:region:account-id:vpc/{{<your-vpc-id>}}",
                       "ec2:Subnet": ["arn:aws:ec2:region:account-id:subnet/{{<your-subnet-id1>}}"]
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
               "Service": [
                   "glue.amazonaws.com",
                   "lakeformation.amazonaws.com"
               ]
           },
           "Action": "sts:AssumeRole"
       }]
   }
   ```

1. <a name="databricks-step-3"></a>Skip this step if you use vended-credential mode. In that mode, the remote catalog issues the Amazon S3 credentials, so the IAM role doesn't need access to the table data in Amazon S3.

   **Create an IAM policy that gives Lake Formation read access to the catalog's Amazon S3 location**

   As the catalog owner of a federated catalog in Data Catalog, you use Lake Formation to grant coarse-grained table access, fine-grained access (column-level, row-level, and cell-level), and tag-based access to your data teams. Lake Formation uses an IAM role that gives it access to the underlying Amazon S3 locations of your remote Iceberg tables. With this access, Lake Formation can vend scoped access credentials to the analytics engines that query remote tables.

   Create an IAM policy and attach it to an IAM role. Add the Lake Formation service principal to the IAM role trust policy.

   In the following example, replace `{{<your-s3-bucket-N>}}` and `{{<your-kms-key>}}` with your own information.  
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
                   "arn:aws:s3:::{{<your-s3-bucket-1>}}/*",
                   "arn:aws:s3:::{{<your-s3-bucket-2>}}/*"
               ]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "s3:ListBucket"
               ],
               "Resource": [
                   "arn:aws:s3:::{{<your-s3-bucket-1>}}",
                   "arn:aws:s3:::{{<your-s3-bucket-2>}}"
               ]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "kms:Decrypt",
                   "kms:Encrypt"
               ],
               "Resource": [
                   "{{<your-kms-key>}}"
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
When you use the Lake Formation console to create a federated catalog, the console uses a single IAM role with both policies attached to complete setup.

1. <a name="databricks-step-4"></a>**Create an AWS Glue connection object**

   Data Catalog supports connectionType: `DATABRICKSICEBERGRESTCATALOG` for connecting Data Catalog to Databricks. This AWS Glue connector supports OAuth2 and Custom authentication methods.

   The following example uses OAuth2 authentication configuration to create an AWS Glue connection. Replace `{{highlighted sections}}` with your information.

   ```
   aws glue create-connection \
       --connection-input '{
   "Name": "{{<your-glue-connection-to-databricks-unity-account>}}",
   "ConnectionType": "DATABRICKSICEBERGRESTCATALOG",
   "ConnectionProperties": {
       "INSTANCE_URL": "https://{{<workspace-host>}}/api/2.1/unity-catalog/iceberg-rest",
       "ROLE_ARN": "{{<your-IAM-role-for-secrets-and-VPC-access>}}",
       "CREDENTIAL_VENDING_MODE": "SOURCE_VENDED"
   },
   "AuthenticationConfiguration": {
       "AuthenticationType": "OAUTH2",
       "OAuth2Properties": {
           "OAuth2GrantType": "CLIENT_CREDENTIALS",
           "TokenUrl": "{{<your-internal-or-external-token-server-url>}}",
           "OAuth2ClientApplication": {
               "UserManagedClientApplicationClientId": "{{<your-client-id>}}"
           },
           "TokenUrlParametersMap": {
               "scope": "{{<scopes-assigned-to-the-secret>}}"
           }
       },
       "SecretArn": "arn:aws:secretsmanager:{{<aws-region>}}:{{<your-aws-account-id>}}:secret:{{<databricks-secret>}}"
   }
   }'
   ```

   The console accepts the workspace root URL and stores it with the `/api/2.1/unity-catalog/iceberg-rest` path appended; in the CLI, pass the full path. The console might also set `CATALOG_CASING_FILTER` (for example, `LOWERCASE_ONLY`).

1. <a name="databricks-step-5"></a>**Register the AWS Glue connection as a Lake Formation resource**

   Using the AWS Glue connection object (created in Step 4) and the IAM role (created in Step 3), you can now register the AWS Glue connection object as a Lake Formation managed resource.

   Replace `{{<your-glue-connector-arn>}}` and `{{<your-IAM-role-ARN-having-LF-access>}}` with your information.

   ```
   aws lakeformation register-resource \
       --resource-arn {{<your-glue-connector-arn>}} \
       --role-arn {{<your-IAM-role-ARN-having-LF-access>}} \
       --with-federation \
       --with-privileged-access
   ```

   The `--with-federation` flag is required. The `--with-privileged-access` flag is optional: per the RegisterResource API reference, it gives the calling principal permission to perform all supported Lake Formation operations on the registered resource. It does not affect how credentials are vended, and the console sets it by default.
**Note**  
Register the connection before you create the catalog. Otherwise, `create-catalog` fails with `The data source … is not registered`.

1. <a name="databricks-step-6"></a>**Create a federated catalog in Data Catalog**

   After creating an AWS Glue connection object and registering it with Lake Formation, you can create a federated catalog in the Data Catalog:

   Provide a unique name for the federated catalog at `{{<your-federated-catalog-name>}}`, reference the catalog in Databricks at `{{"<catalog-name-in-Databricks>}}`, and enter the connection name you created earlier at `{{"<your-glue-connection-name>}}`.

   ```
   aws glue create-catalog \
       --name {{<your-federated-catalog-name>}} \
       --catalog-input '{
       "FederatedCatalog": {
           "Identifier": {{"<catalog-name-in-Databricks>}}",
           "ConnectionName": {{"<your-glue-connection-name>}}"
       },
       "CreateTableDefaultPermissions": [],
       "CreateDatabaseDefaultPermissions": []
   }'
   ```

1. <a name="databricks-step-7"></a>**Grant Lake Formation permissions**

   Catalog-level grants don't carry down to federated databases and tables. Grant `DESCRIBE` on the database, and `SELECT` and `DESCRIBE` on the table wildcard, to each principal that queries the catalog.

1. <a name="databricks-step-8"></a>**Query the federated catalog**

   Query the federated catalog from your analytics engine. For example, in Amazon Athena:

   ```
   SELECT * FROM "<federated-catalog>"."<schema>"."<table>" LIMIT 10;
   ```

## Change the access delegation mode
<a name="catalog-federation-databricks-change-mode"></a>

To switch an existing connection between modes, update the connection property; you don't need to recreate the federated catalog.

```
aws glue get-connection --name <connection-name> --output json > connection.json
# Build ConnectionInput from connection.json with CREDENTIAL_VENDING_MODE set to the new value
aws glue update-connection --name <connection-name> --connection-input file://<updated-connection-input>.json
```

## Considerations when integrating with Databricks
<a name="databricks-considerations"></a>
+ When you drop resources (such as databases and tables) in Databricks, Lake Formation does not automatically revoke the permissions granted on that federated resource. To remove the access permissions, you need to explicitly revoke the permissions that you previously granted on the federated resource by using Lake Formation.
+ You can query Iceberg tables stored in Amazon S3 by using this integration. When you use any other table format or object storage, you can federate metadata in remote catalogs to AWS Glue and list its databases and tables. However, query operations such as `SELECT ColumnFoo from TableBar` fail during the query with the error 'Failed to read Apache Iceberg table. Object storage location is not supported.'
+ You can reuse the same AWS Glue connection to create multiple federated catalogs. Deleting a catalog does not delete the associated connection object. To delete a connection object, use the AWS CLI `aws glue delete-connection` command, and make sure that you delete all associated catalogs first.
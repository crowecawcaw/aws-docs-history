

# Federate to Workday Data Connect

AWS Glue Data Catalog federates to Workday Data Connect using the OAuth2 credentials of a Workday Integration System User (ISU). Workday Data Connect is the zero-copy connector for Workday Data Lake. Workday Data Lake stores Workday data as Apache Iceberg tables and exposes them through an Iceberg REST catalog. With this authentication mechanism, AWS Glue Data Catalog can access the metadata of various objects (such as catalogs, databases, and tables) in your Workday Data Lake. This access is based on the Data Lake access roles assigned to the ISU. To ensure access to the right objects, assign the ISU a Data Lake access role in Workday that includes the tables you want to query.

Workday Data Lake tables are stored in Amazon S3 locations that Workday manages. When you query a federated Workday table, the Workday catalog vends short-lived, table-scoped credentials for the table's data. AWS analytics engines use those credentials to read the Iceberg data files directly. You don't need to grant Lake Formation access to the Amazon S3 locations that Workday manages. Lake Formation governs which databases, tables, and columns each principal in your account can access.

Follow the Workday documentation to set up Workday Data Lake, the ISU, and the API client in your Workday tenant. For more information, see [Get Started with Workday Data Lake](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-data-lake/workday-data-lake.html) in the Workday documentation.

## Prerequisites
<a name="catalog-federation-workday-prerequisites"></a>

Before you create a federated catalog in AWS Glue Data Catalog that is governed by Lake Formation, ensure you have the following permissions and information:

Your IAM principal (user or role) must have the following permissions:
+ **Lake Formation permissions** – `lakeformation:RegisterResource`, `lakeformation:DescribeResource`
+ **AWS Glue permissions** – `glue:CreateConnection`, `glue:CreateCatalog`, `glue:GetConnection`, `glue:PassConnection`
+ **Secrets Manager permissions** – `secretsmanager:CreateSecret`, `secretsmanager:GetSecretValue`
+ **IAM permissions** – `iam:CreateRole`, `iam:AttachRolePolicy`, `iam:PassRole`

You must be a Lake Formation data lake administrator or have `CREATE_CATALOG` permission on the Data Catalog.

You also need the following information from your Workday administrator:
+ **Catalog URL** – The Iceberg REST catalog endpoint of your Workday Data Lake, for example `https://catalog.{{data-center-code}}.myworkday.com`, where {{data-center-code}} is your Workday environment prefix, such as `wd00`.
+ **Token URL** – The OAuth 2.0 token endpoint of the Workday catalog, for example `https://{{host}}/ccx/oauth2/{{tenant}}/token`.
+ **Tenant ID** – The identifier of your Workday tenant.
+ **Client ID** – The client ID of the API client registered for Data Lake. For more information, see [Register API Client for Data Lake (JWT Bearer Grant)](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-data-lake/register-api-client-for-data-lake--jwt-bearer-gran.html?toc=2.2.4) or [Register API Client for Data Lake (Refresh Token Grant)](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-data-lake/register-api-client-for-data-lake--refresh-token-g.html?toc=2.2.5) in the Workday documentation.
+ **ISU user name and private key** – The ISU user name and the RSA private key, in PEM format, matching the x509 certificate registered for the API client. For more information, see [Set Up Integration System Users for Data Lake](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-data-lake/set-up-isus-for-data-lake.html?toc=2.2.3) in the Workday documentation.

## Create Federated Catalog
<a name="catalog-federation-workday-create"></a>

### Using Console
<a name="catalog-federation-workday-console"></a>

1. Sign in to the console and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. Choose the preferred AWS Region in the Region selector.

1. In the left navigation pane, choose Catalogs.

1. Choose **Create a catalog** to open the **Create Catalog Workflow**.

1. In the **Choose data source** step, select Workday Data Connect from the available options.

1. In the **Set catalog details** step, you provide three types of information: catalog details, connection details, and registration details.

1. In the **catalog details** container, provide a unique lowercase name for your AWS Glue federated catalog. For **Catalog name in Workday**, enter the name of the existing catalog in Workday Data Connect, `workday`. Optionally, provide a description.

1. In the **connection details** container, for **Connector object**, you can either **Select existing connection** that you have access to or **Input new connection configuration** to create a new connection.

1. New connection configurations include:
   + Connection name – A unique lowercase name for the AWS Glue connection object. You can't change this name after you create the connection.
   + Workspace URL – The Iceberg REST catalog endpoint of your Workday Data Lake.
   + Tenant ID – The identifier of your Workday tenant.
   + Casing type – Choose whether to bring lowercase or uppercase objects from your remote catalog. Workday Data Lake namespaces and tables use lowercase identifiers.
   + Authentication – For **Grant type**, choose **JWT Bearer** or **Refresh Token**.
   + Token URL – The OAuth 2.0 token endpoint of the Workday catalog.
   + OAuth Client ID – The client ID of the API client registered for Data Lake.
   + Secret name – Choose the AWS Secrets Manager secret that stores your Workday credentials, or choose **Create secret**. For **JWT Bearer**, the secret contains the private key `PRIVATE_KEY_PEM` and the ISU user name `USERNAME`. For **Refresh Token**, the secret contains the client secret `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` and the refresh token `REFRESH_TOKEN`.
   + Token URL parameter map scope – (Optional) The OAuth scope, for example `PRINCIPAL_ROLE:ALL`. Leave this field blank unless your Workday tenant requires a scope.
   + Settings for network configurations – (Optional) The Amazon VPC settings for the connection.

1. For **IAM role**, choose an IAM role that AWS Glue and Lake Formation service principals can use to access the secret, or choose **Create an IAM role**. Refer to step 2 and step 3 in the following CLI section for IAM policy details.
**Note**  
When you register a federated Iceberg catalog in Lake Formation, the registering principal automatically receives permissions to perform all supported Lake Formation operations on the catalog and its objects.

1. Select Test connection to test whether your connection properties and IAM role access are configured correctly.

1. Select **Next** to review your settings.

1. Select **Create catalog** in review page.

### Using CLI
<a name="catalog-federation-workday-cli"></a>

1. <a name="workday-step-1"></a>**Create an AWS Secrets Manager secret**

   The AWS Glue connector supports OAuth2 with two grant types: **JWT bearer** and **refresh token**. For JWT bearer, store the ISU user name and private key. AWS Glue signs a JWT with the private key and exchanges it for an access token at the Workday token URL. For refresh token, store the client secret and refresh token.

   In the following example, replace `{{<workday-secret>}}`, `{{<isu-user-name>}}`, `{{<private-key>}}`, and `{{<region>}}` with your own information.

   ```
   aws secretsmanager create-secret \
   --name {{<workday-secret>}} \
   --description "Workday Data Connect secret" \
   --secret-string '{
   "USERNAME": "{{<isu-user-name>}}",
   "PRIVATE_KEY_PEM": "-----BEGIN PRIVATE KEY-----\n{{<private-key>}}\n-----END PRIVATE KEY-----"
   }' \
   --region {{<region>}}
   ```
**Note**  
`USERNAME` and `PRIVATE_KEY_PEM` are reserved keywords that AWS Glue uses to refer to the ISU user name and private key. For refresh token, use `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` and `REFRESH_TOKEN` instead. Store the private key as a single JSON string, using `\n` escape sequences for the PEM line breaks. After it first connects, AWS Glue adds an `ACCESS_TOKEN` key to the secret.

1. <a name="workday-step-2"></a>**Create an IAM role that gives the AWS Glue connection object access to the secret created in the previous step**

   The AWS Glue connection object requires access to the AWS Secrets Manager secret. The AWS Glue connection object also requires access to create, describe, and use the Amazon VPC network interfaces when you use a Amazon VPC endpoint to restrict connectivity to your Workday tenant.

   Create an IAM policy and attach it to an IAM role. Add the AWS Glue service principal to the trust policy.

   In the following example, replace `{{<your-secrets-manager-ARN>}}`, `{{<your-vpc-id>}}`, `{{<your-subnet-id1>}}`, and `{{<account-id>}}` with your own information.  
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
               "Service": "glue.amazonaws.com"
           },
           "Action": "sts:AssumeRole",
           "Condition": {
               "StringEquals": {
                   "aws:SourceAccount": "{{<account-id>}}"
               }
           }
       }]
   }
   ```

1. <a name="workday-step-3"></a>**Create an IAM role that Lake Formation uses to access the Workday catalog**

   Lake Formation uses this IAM role to retrieve the ISU credentials from AWS Secrets Manager. Unlike other remote Iceberg catalogs, this role does not need Amazon S3 or AWS KMS access, because the Workday catalog vends scoped credentials for the Amazon S3 locations of its tables at query time.

   Create an IAM policy and attach it to an IAM role. Add the Lake Formation service principal to the IAM role trust policy.

   In the following example, replace `{{<your-secrets-manager-ARN>}}` and `{{<account-id>}}` with your own information.  
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
           "Action": "sts:AssumeRole",
           "Condition": {
               "StringEquals": {
                   "aws:SourceAccount": "{{<account-id>}}"
               }
           }
       }]
   }
   ```
**Note**  
When you use the Lake Formation console to create a federated catalog, the console uses a single IAM role with both policies attached to complete setup.

1. <a name="workday-step-4"></a>**Create an AWS Glue connection object**

   Data Catalog supports connectionType: `WORKDAYICEBERGRESTCATALOG` for connecting Data Catalog to Workday Data Connect. This AWS Glue connector supports OAuth2 with the `JWT_BEARER` and `REFRESH_TOKEN` grant types. Set `CREDENTIAL_VENDING_MODE` to `SOURCE_VENDED` so that AWS analytics engines read table data with the credentials that the Workday catalog vends. With the `CATALOG_CASING_FILTER` configuration, you can bring either lowercase or uppercase objects in your remote catalog to the Data Catalog.

   The following example uses JWT bearer authentication configuration to create an AWS Glue connection. Replace `{{highlighted sections}}` with your information.

   ```
   aws glue create-connection \
       --connection-input '{
   "Name": "{{<your-glue-connection-to-workday>}}",
   "ConnectionType": "WORKDAYICEBERGRESTCATALOG",
   "ConnectionProperties": {
       "INSTANCE_URL": "{{<your-workday-catalog-URL>}}",
       "TENANT_ID": "{{<your-workday-tenant-id>}}",
       "ROLE_ARN": "{{<your-IAM-role-for-secret-access>}}",
       "CATALOG_CASING_FILTER": "LOWERCASE_ONLY",
       "CREDENTIAL_VENDING_MODE": "SOURCE_VENDED"
   },
   "AuthenticationConfiguration": {
       "AuthenticationType": "OAUTH2",
       "OAuth2Properties": {
           "OAuth2GrantType": "JWT_BEARER",
           "TokenUrl": "{{<your-workday-token-url>}}",
           "OAuth2ClientApplication": {
               "UserManagedClientApplicationClientId": "{{<your-client-id>}}"
           }
       },
       "SecretArn": "arn:aws:secretsmanager:{{<region>}}:{{<account-id>}}:secret:{{<workday-secret>}}"
   }
   }'
   ```
**Note**  
For refresh token, set `OAuth2GrantType` to `REFRESH_TOKEN` and store the client secret and refresh token in the secret. If your Workday tenant requires an OAuth scope, add `"TokenUrlParametersMap": {"scope": "{{<scope>}}"}` to `OAuth2Properties`, for example `PRINCIPAL_ROLE:ALL`.

1. <a name="workday-step-5"></a>**Register AWS Glue connection as a Lake Formation resource**

   Using the AWS Glue connection object (created in Step 4) and IAM role (created in Step 3), you can now register the AWS Glue connection object as a Lake Formation managed resource.

   Replace `{{<your-glue-connector-arn>}}` and `{{<your-IAM-role-ARN-having-LF-access>}}` with your information.

   ```
   aws lakeformation register-resource \
       --resource-arn {{<your-glue-connector-arn>}} \
       --role-arn {{<your-IAM-role-ARN-having-LF-access>}} \
       --with-federation \
       --with-privileged-access
   ```

1. <a name="workday-step-6"></a>**Create a federated catalog in Data Catalog**

   After creating an AWS Glue connection object and registering it with Lake Formation, you can create a federated catalog in the Data Catalog:

   Provide the federated catalog a unique name at `{{<your-federated-catalog-name>}}`, reference the catalog in Workday with the identifier `workday`, and input the connection name created earlier at `{{<your-glue-connection-name>}}`.

   ```
   aws glue create-catalog \
       --name {{<your-federated-catalog-name>}} \
       --catalog-input '{
       "FederatedCatalog": {
           "Identifier": "workday",
           "ConnectionName": "{{<your-glue-connection-name>}}"
       },
       "CreateTableDefaultPermissions": [],
       "CreateDatabaseDefaultPermissions": []
   }'
   ```

## Considerations when integrating with Workday Data Connect
<a name="workday-considerations"></a>
+ When Workday removes a table from your Data Lake, or you remove a table from the ISU's Data Lake access role, Lake Formation does not automatically revoke the permissions granted on that federated resource. To remove the access, explicitly revoke the permissions that were previously granted using Lake Formation.
+ The databases and tables that appear in the federated catalog depend on the tables in the ISU's Data Lake access role and the tables and columns added to your Data Lake in Workday. Workday enforces access at the table level, and only the columns added to the Data Lake are available. Lake Formation permissions can narrow this access further, but can't grant access beyond it. For more information, see [Configure Data Lake Access Roles](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-data-lake/configure-data-lake-access-roles.html) and [Add Tables and Columns to Data Lake](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-data-lake/add-tables-and-fields-to-data-lake.html?toc=2.2.7) in the Workday documentation.
+ Workday refreshes Data Lake tables from your Workday tenant on a schedule (hourly, daily, or weekly, depending on your subscription and tenant type), so data in the federated catalog can lag behind your Workday tenant. For real-time access, use the Workday Live Data Query connector instead. For more information, see [Connecting to Workday Live Data Query](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-workday.html) in the AWS Glue User Guide.
+ Workday Data Lake namespaces include `workday_core` for Workday business object tables and `join_workday_core` for joiner tables that flatten array relationships into two-column tables. For more information, see [Query Workday Data Lake](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-data-lake/query-workday-data-lake.html?toc=2.2.9) in the Workday documentation.
+ You can reuse the same AWS Glue connection to create multiple federated catalogs. Deleting a catalog does not delete the associated connection object. To delete a connection object, use the AWS CLI `aws glue delete-connection` command and ensure all associated catalogs are deleted first.
+ Nested namespaces are not supported. That is, catalog federation can access remote Iceberg tables that follow a 3-part notation `catalog.database.table`.

## Information to collect from your Workday administrator
<a name="catalog-federation-workday-info-to-collect"></a>

Collect the following information from your Workday administrator before you create the connection. The information that you need depends on the OAuth 2.0 grant type, either JWT bearer or refresh token.


**Information to collect from your Workday administrator**  

| Value | Description | Example | 
| --- | --- | --- | 
| Catalog URL | The Iceberg REST catalog endpoint of your Workday Data Lake. The {{data-center-code}} is your Workday environment prefix, such as wd00. | https://catalog.{{data-center-code}}.myworkday.com | 
| Token URL | The OAuth 2.0 token endpoint of the Workday catalog. | https://{{host}}/ccx/oauth2/{{tenant}}/token | 
| Tenant ID | The identifier of your Workday tenant. | aws\_tenant1 | 
| Client ID | The client ID of the API client registered for Data Lake. | MThmMWI3YWEtZDZjMS00MzRmLTliZWBeMzg4ZjI2NmI1MjFl4 | 
| ISU user name | The user name of the ISU. Required for the JWT bearer grant type (stored in the secret as USERNAME). | demo-isu | 
| Private key | The RSA private key, in PEM format, that matches the x509 certificate registered for the API client. Required for the JWT bearer grant type (stored in the secret as PRIVATE\_KEY\_PEM). | -----BEGIN PRIVATE KEY----- … -----END PRIVATE KEY----- | 
| Client secret | The client secret of the API client registered for Data Lake. Required for the refresh token grant type (stored in the secret as USER\_MANAGED\_CLIENT\_APPLICATION\_CLIENT\_SECRET). | yego9m0c...hniqtw | 
| Refresh token | The refresh token of the API client registered for Data Lake. Required for the refresh token grant type (stored in the secret as REFRESH\_TOKEN). | nmdjc98r2j...4e6fqz9swlc | 
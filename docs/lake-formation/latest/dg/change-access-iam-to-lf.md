

# Enable Lake Formation with S3 Tables integration with Data Catalog
<a name="change-access-iam-to-lf"></a>

This section describes the workflow to migrate access control from IAM privileges to IAM with AWS Lake Formation grants for Amazon S3 Tables integrated with the AWS Glue Data Catalog.

**Important**  
Enabling AWS Lake Formation access control will revoke all existing IAM-based access to your S3 Tables resources. After completing Step 1, users and roles that previously accessed data through IAM permissions will immediately lose access. You must grant Lake Formation permissions in Step 2 before users can query data again. Plan this migration during a maintenance window and coordinate with your data team.

## Prerequisites
<a name="w2aac13c29b7b7"></a>

For read/write access to S3 Tables, in addition to Lake Formation permissions, principals also need the `lakeformation:GetDataAccess` IAM permission. With this permission, Lake Formation grants the request for temporary credentials to access the data.

## Using AWS CLI
<a name="w2aac13c29b7b9"></a>

1. **Step 1: Register bucket with Lake Formation using IAM role**

   Register the S3 Tables resource with Lake Formation.
**Note**  
If you have an existing role, ensure hybrid access is false.

   ```
   aws lakeformation register-resource \
     --resource-arn "arn:aws:s3tables:us-east-1:{{AWSAccountID}}:bucket/*" \
     --role-arn "arn:aws:iam::{{AWSAccountID}}:role/service-role/{{LFAccessRole}}" \
     --with-federation
   ```

1. **Step 2: Update AWS Glue catalog to enable Lake Formation access control**

   Update the catalog with empty `CreateDatabaseDefaultPermissions` and `CreateTableDefaultPermissions` (set to `[]`). This ensures that databases and tables in the catalog are managed using Lake Formation grants instead of IAM-based default permissions.

   ```
   aws glue update-catalog \
     --catalog-id "s3tablescatalog" \
     --catalog-input '{
       "FederatedCatalog": {
           "Identifier": "arn:aws:s3tables:us-east-1:{{AWSAccountID}}:bucket/*",
           "ConnectionName": "aws:s3tables"
       },
       "CreateDatabaseDefaultPermissions": [],
       "CreateTableDefaultPermissions": [],
       "AllowFullTableExternalDataAccess": "True"
     }'
   ```

1. **Step 3: Grant Lake Formation permissions to your data team**

   Grant Lake Formation permissions to the principals (roles, users, or groups) that need access. For example, to grant full-table read access to a role:

   ```
   aws lakeformation grant-permissions \
     --principal DataLakePrincipalIdentifier=arn:aws:iam::{{AWSAccountID}}:role/{{DataTeamRole}} \
     --resource '{
       "Table": {
           "CatalogId": "{{AWSAccountID}}",
           "DatabaseName": "s3tablescatalog/{{table-bucket-name}}/{{namespace}}",
           "TableWildcard": {}
       }
     }' \
     --permissions "SELECT" "DESCRIBE"
   ```

   Repeat for each principal and resource combination as needed.
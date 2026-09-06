

# Change access control from AWS Lake Formation to IAM
<a name="change-access-lf-to-iam"></a>

This section describes the workflow to change access control from AWS Lake Formation grants to IAM privileges for Amazon S3 Tables integrated with the AWS Glue Data Catalog.

**Important**  
Changing access control from AWS Lake Formation grants to IAM will revoke all existing Lake Formation-based access to your S3 Tables resources. After completing Step 2, users and roles that previously accessed data through Lake Formation grants will immediately lose access. You must grant IAM access in Step 1 before updating the catalog. Plan this migration during a maintenance window and coordinate with your data team.

**Important**  
Fine-grained access controls, such as column-level access and data cell filters, with Data Catalog objects are available when using AWS Lake Formation only. Before proceeding to migrate access controls from AWS Lake Formation to IAM, audit your existing Lake Formation grants using `aws lakeformation list-permissions` and determine whether equivalent IAM policies can provide the access your users need. Any principal that relied on fine-grained Lake Formation grants will require full table-level IAM access after migrating access control.

## Prerequisites
<a name="w2aac13c29b9b9"></a>

Before you begin, ensure the following:
+ You have identified all Lake Formation grants currently in effect for the resources being migrated. Run `aws lakeformation list-permissions --resource-type TABLE` to review them.
+ You have prepared IAM policies that provide equivalent access for all affected principals.
+ The IAM role registered with Lake Formation still has `lakeformation:GetDataAccess` (needed during the hybrid transition period).

## Using AWS CLI
<a name="w2aac13c29b9c11"></a>

1. **Step 1: Grant IAM permissions to principals**

   Attach IAM policies to the users or roles that need access. The policy must include both AWS Glue metadata permissions and S3 Tables data permissions.
**Note**  
The following example policy only provides read access.

   ```
   aws iam put-user-policy \
     --user-name {{GlueIAMAccessUser}} \
     --policy-name {{S3TablesIAMAccessPolicy}} \
     --policy-document '{
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "GlueMetadataAccess",
               "Effect": "Allow",
               "Action": [
                   "glue:GetCatalog",
                   "glue:GetDatabase",
                   "glue:GetTable"
               ],
               "Resource": [
                   "arn:aws:glue:us-east-1:{{AWSAccountID}}:catalog/s3tablescatalog",
                   "arn:aws:glue:us-east-1:{{AWSAccountID}}:database/s3tablescatalog/{{table-bucket-name}}/{{namespace}}",
                   "arn:aws:glue:us-east-1:{{AWSAccountID}}:table/s3tablescatalog/{{table-bucket-name}}/{{namespace}}/*"
               ]
           },
           {
               "Sid": "S3TablesDataAccess",
               "Effect": "Allow",
               "Action": [
                   "s3tables:GetTableBucket",
                   "s3tables:GetTable",
                   "s3tables:GetTableMetadataLocation",
                   "s3tables:GetTableData"
               ],
               "Resource": [
                   "arn:aws:s3tables:us-east-1:{{AWSAccountID}}:bucket/{{table-bucket-name}}",
                   "arn:aws:s3tables:us-east-1:{{AWSAccountID}}:bucket/{{table-bucket-name}}/table/*"
               ]
           }
       ]
     }'
   ```

   Verify that all affected users and roles can access the expected tables using their IAM credentials before proceeding.

1. **Step 2: Update the catalog to restore IAM default permissions**

   Update the catalog so that `CreateDatabaseDefaultPermissions` and `CreateTableDefaultPermissions` grant `ALL` to `IAM_ALLOWED_PRINCIPALS`. Set `OverwriteChildResourcePermissionsWithDefault` to `Accept` so the change propagates to all existing child resources, not just newly created ones.

   ```
   aws glue update-catalog \
     --catalog-id "s3tablescatalog" \
     --catalog-input '{
       "FederatedCatalog": {
           "Identifier": "arn:aws:s3tables:us-east-1:{{AWSAccountID}}:bucket/*",
           "ConnectionName": "aws:s3tables"
       },
       "CreateDatabaseDefaultPermissions": [{
           "Principal": {"DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS"},
           "Permissions": ["ALL"]
       }],
       "CreateTableDefaultPermissions": [{
           "Principal": {"DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS"},
           "Permissions": ["ALL"]
       }],
       "OverwriteChildResourcePermissionsWithDefault": "Accept"
     }'
   ```

1. **Step 3: Deregister the resource from Lake Formation**

   Once you have confirmed that all access is working through IAM policies and no principals depend on Lake Formation grants, you can deregister the resource from Lake Formation to complete the migration.

   ```
   aws lakeformation deregister-resource \
     --resource-arn "arn:aws:s3tables:us-east-1:{{AWSAccountID}}:bucket/*"
   ```
**Note**  
After deregistering the resource, remove `lakeformation:GetDataAccess` from IAM principals that no longer need it.

No `revoke-permissions` step is required.


# Enabling Amazon S3 Tables integration
<a name="enable-s3-tables-catalog-integration"></a>

You can create Amazon S3 table buckets using Amazon S3 console, and integrate it with AWS analytics services. For more information, see [Using Amazon S3 Tables with AWS analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html). 

 In AWS Lake Formation, you can enable Amazon S3 Tables integration with AWS Glue Data Catalog and AWS Lake Formation using the Lake Formation console or use AWS CLI. 

## To integrate Amazon S3 Tables with the Data Catalog and Lake Formation (console)
<a name="w2aac13c27c23b7b1"></a>

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. In the navigation pane, choose **Catalogs** under **Data Catalog**.

1. Choose **Enable S3 Table integration** on the **Catalogs** page.   
![The enable S3 table integration option on the catalogs page.](http://docs.aws.amazon.com/lake-formation/latest/dg/images/enable-s3-table-integration.png)

1.  Choose an IAM role with the required permissions for Lake Formation to assume to vend credentials to the analytical query engines. For the permissions required for the role to accessing data, see [step3-permissions](s3tables-catalog-prerequisites.md#step3-permissions) in the prerequisites section.   
![The enable S3 integration screen with IAM role.](http://docs.aws.amazon.com/lake-formation/latest/dg/images/enable-s3-table-catalog.png)

1.  Select **Allow external engines to access data in Amazon S3 locations with full table access** option. When you enable full table access for third-party engines, Lake Formation returns credentials to the third-party engine directly without performing IAM session tag validation. This means you cannot apply Lake Formation fine-grained access controls to the tables being accessed. 

1. Choose **Enable**. The new catalog for S3 Tables is added to the catalog list. When you enable the S3 tables catalog integration, the service registers the data location of the S3 table bucket with Lake Formation.

1. Choose the catalog to view catalog objects and grant permissions to other principals.   
![The S3 Table Catalog](http://docs.aws.amazon.com/lake-formation/latest/dg/images/s3-table-catalog.png)

   To create multi-level catalogs, see the [Creating a table bucket ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-create.html) section in the Amazon Simple Storage Service User Guide.

## To integrate Amazon S3 tables with the Data Catalog and Lake Formation (CLI)
<a name="w2aac13c27c23b7b3"></a>

Following the prerequisites section, create an IAM service role that allows Lake Formation to access your table resources.

1. Create a file called `Role-Trust-Policy.json` that contains the following trust policy:

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
         {
           "Sid": "LakeFormationDataAccessPolicy",
           "Effect": "Allow",
           "Principal": {
             "Service": "lakeformation.amazonaws.com"
           },
           "Action": [
               "sts:AssumeRole",
               "sts:SetContext",
               "sts:SetSourceIdentity"
           ],
           "Condition": {
             "StringEquals": {
               "aws:SourceAccount": "{{111122223333}}"
             }
           }
         }
       ]
   }
   ```

1. Create the IAM service role by using the following command:

   ```
   aws iam create-role \
     --role-name {{S3TablesRoleForLakeFormation}} \
     --assume-role-policy-document file://Role-Trust-Policy.json
   ```

1. Create a file called `LF-GluePolicy.json` that contains the following policy:

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "LakeFormationPermissionsForS3ListTableBucket",
               "Effect": "Allow",
               "Action": [
                   "s3tables:ListTableBuckets"
               ],
               "Resource": [
                   "*"
               ]
           },
           {
               "Sid": "LakeFormationDataAccessPermissionsForS3TableBucket",
               "Effect": "Allow",
               "Action": [
                   "s3tables:CreateTableBucket",
                   "s3tables:GetTableBucket",
                   "s3tables:CreateNamespace",
                   "s3tables:GetNamespace",
                   "s3tables:ListNamespaces",
                   "s3tables:DeleteNamespace",
                   "s3tables:DeleteTableBucket",
                   "s3tables:CreateTable",
                   "s3tables:DeleteTable",
                   "s3tables:GetTable",
                   "s3tables:ListTables",
                   "s3tables:RenameTable",
                   "s3tables:UpdateTableMetadataLocation",
                   "s3tables:GetTableMetadataLocation",
                   "s3tables:GetTableData",
                   "s3tables:PutTableData"
               ],
               "Resource": [
                   "arn:aws:s3tables:us-east-1:{{111122223333}}:bucket/*"
               ]
           }
       ]
   }
   ```

1. Attach the policy to the role by using the following command:

   ```
   aws iam put-role-policy \
     --role-name {{S3TablesRoleForLakeFormation}} \
     --policy-name {{LakeFormationDataAccessPermissionsForS3TableBucket}} \
     --policy-document file://LF-GluePolicy.json
   ```

1. Create a file called `input.json` that contains the following:

   ```
   {
       "ResourceArn": "arn:aws:s3tables:us-east-1:{{111122223333}}:bucket/*",
       "WithFederation": true,
       "RoleArn": "arn:aws:iam::{{111122223333}}:role/{{S3TablesRoleForLakeFormation}}"
   }
   ```

1. Register table buckets with Lake Formation by using the following command:

   ```
   aws lakeformation register-resource \
     --region us-east-1 \
     --with-privileged-access \
     --cli-input-json file://input.json
   ```

1. Create a file called `catalog.json` that contains the following catalog:

   ```
   {
      "Name": "s3tablescatalog",
      "CatalogInput": {
         "FederatedCatalog": {
             "Identifier": "arn:aws:s3tables:us-east-1:{{111122223333}}:bucket/*",
             "ConnectionName": "aws:s3tables"
          },
          "CreateDatabaseDefaultPermissions": [],
          "CreateTableDefaultPermissions": [],
          "AllowFullTableExternalDataAccess": "True"
      }
   }
   ```

1. Create the `s3tablescatalog` catalog by using the following command. Creating this catalog populates the AWS Glue Data Catalog with objects corresponding to table buckets, namespaces, and tables.

   ```
   aws glue create-catalog \
     --region us-east-1 \
     --cli-input-json file://catalog.json
   ```

1. Verify that the `s3tablescatalog` catalog was added in AWS Glue by using the following command:

   ```
   aws glue get-catalog --catalog-id s3tablescatalog
   ```
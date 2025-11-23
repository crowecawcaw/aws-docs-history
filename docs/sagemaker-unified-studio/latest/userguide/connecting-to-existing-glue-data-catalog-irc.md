# Working with an existing AWS Glue Data Catalog IRC

This document outlines the procedure for onboarding existing AWS Glue IRC federated catalogs managed by AWS Lake Formation into an Amazon SageMaker Unified Studio domain. Successful onboarding requires granting appropriate permissions granted to the Studio role within AWS Lake Formation by the Datalake admin.

## IAM based domain

### Prerequisites

- Amazon SageMaker Unified Studio deployed with IAM-based domain mode
- Existing AWS Glue federated catalog managed by AWS Lake Formation
- Data Lake Administrator credentials

### Step by Step Instructions

###### Step 1: Retrieve the Project Execution Role

1. Access your Amazon SageMaker Unified Studio project
2. Locate and copy the project execution role ARN

###### Step 2: Configure Lake Formation Permissions

1. Sign in to the AWS Management Console using Data Lake Administrator credentials
2. Navigate to AWS Lake Formation and grant Permissions (Select One Option):

Option 1: Full Catalog Access (Recommended for Admin project)

Grant the execution role super_user permissions on the federated catalog. The execution role receives complete access to discover and query all databases and tables within the federated catalog.

Option 2: Granular Access Control (Recommended for non-Admin project)

Apply least-privilege permissions by granting specific access levels:

    1. Catalog Level: Grant DESCRIBE permission on the catalog to the execution role
    2. Database Level: Grant DESCRIBE permission on the target database(s) to the execution role
    3. Table Level: Grant SELECT and DESCRIBE permissions on the target table(s) to the execution role

###### Step 3 : Query federated resource from Unified Studio

1. Use Query Editor:
   1. Now you can see the federated catalogs discoverable under Query Editor and query them as well.

2. Use Data notebook
   1. To use Data notebook to query you can navigate to the notebooks tab in the left navigation panel.
   2. Create notebook and you can now run select on federated catalog
   3. For Athena(SQL) you can run the query as shown below

   ```
   SELECT * FROM "smus_lfuc_poc"."lfuc"."customer" LIMIT 100
   ```

   4. For Athena(spark), add the following config to enable federated catalog querying.

   ```
   SET `spark.sql.catalog.<catalog_name>`=`org.apache.iceberg.spark.SparkCatalog`;
   SET `spark.sql.catalog.<catalog_name>.catalog-impl`=`org.apache.iceberg.aws.glue.GlueCatalog`;
   SET `spark.sql.catalog.<catalog_name>.glue.id`=`<account_id>:<federated_catalog_name>`;
   SET `spark.sql.catalog.<catalog_name>.glue.lakeformation-enabled` = `true`;
   SET `spark.sql.catalog.<catalog_name>.glue.account-id` = `<accountid>`;
   SET `spark.sql.catalog.<catalog_name>.client.region` = `<region>`;
   ```

   5. Query the catalog by running the following:

   ```
   select * from <fderated_catalog_name>.<database_name>.<table_name>
   ```

## Identity Center based domain

### Prerequisites

- Amazon SageMaker Unified Studio deployed with IDC-based domain mode
- Existing AWS Glue federated catalog managed by AWS Lake Formation
- Data Lake Administrator credentials

### Step by Step Instructions

###### Step 1: Retrieve the Project IAM Role

1. Access your Amazon SageMaker Unified Studio project
2. Locate and copy the project IAM role ARN

###### Step 2: Configure Lake Formation Permissions

1. Sign in to the AWS Management Console using Data Lake Administrator credentials
2. Navigate to AWS Lake Formation and grant Permissions (Select One Option):

Option 1: Full Catalog Access

Grant the project role super_user permissions on the federated catalog. The execution role receives complete access to discover and query all databases and tables within the federated catalog.

Option 2: Granular Access Control

Apply least-privilege permissions by granting specific access levels:

    1. Catalog Level: Grant DESCRIBE permission on the catalog to the project role
    2. Database Level: Grant DESCRIBE permission on the target database(s) to the project role
    3. Table Level: Grant SELECT and DESCRIBE permissions on the target table(s) to the project role

###### Step 3 : Query federated resource from Unified Studio

- Login into studio and access as Idc used and access the the federated resource from the explorer. You can select resource and query with Athena and Amazon Redshift.

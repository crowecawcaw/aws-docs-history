

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Query Amazon S3 Tables from Amazon Redshift
<a name="querying-s3Tables"></a>

Amazon Redshift integrates with Amazon S3 table buckets, so you can access S3 table resources using Amazon Redshift. Whether you are just getting started or managing thousands of tables in your Iceberg environment, table buckets simplify data lake management at any scale. For more information, see [Table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets.html).

This topic describes how to get started with Amazon S3 Tables and Redshift and access S3 Tables objects using Amazon Redshift.

## Prerequisites
<a name="querying-s3Tables-prerequisites"></a>

Before querying S3 Tables from Amazon Redshift, you must integrate S3 Tables with AWS Glue Data Catalog. For instructions, see [Integrating Amazon S3 Tables with AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/glue-federation-s3tables.html).

After S3 Tables is integrated with AWS Glue Data Catalog, IAM principals with the required S3 Tables and AWS Glue IAM permissions can discover S3 Tables through the AWS Glue Data Catalog.

**Note**  
Method 3 (Auto-mounted awsdatacatalog) has additional prerequisites. See [Method 3: Auto-mounted awsdatacatalog](#querying-s3Tables-method3) for details.

## Query S3 Tables from Amazon Redshift
<a name="querying-s3Tables-steps"></a>

To get started with querying S3 Tables, follow these steps:
+ Step 1: Create an IAM role for Amazon Redshift
+ Step 2: Attach an IAM role to your Amazon Redshift cluster
+ Step 3: Query S3 Tables from Amazon Redshift

### Step 1: Create an IAM role for Amazon Redshift
<a name="querying-s3Tables-step1"></a>

Your cluster needs authorization to access the external S3 Tables catalog in AWS Glue. To provide that authorization, Amazon Redshift uses an IAM role that is attached to your cluster. Create an IAM role with the following policy permissions.

**Note**  
In the policy and examples below, replace `us-west-2` with your AWS Region and `111122223333` with your AWS account ID.

**To create a policy:**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. Choose the **JSON** tab.

1. Paste in the following JSON policy document:

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "GlueDataCatalogPermissions",
         "Effect": "Allow",
         "Action": [
           "glue:GetCatalog",
           "glue:GetDatabase",
           "glue:GetTable",
           "glue:GetTables",
           "glue:UpdateTable",
           "glue:DeleteTable"
         ],
         "Resource": [
           "arn:aws:glue:us-west-2:111122223333:catalog",
           "arn:aws:glue:us-west-2:111122223333:catalog/s3tablescatalog",
           "arn:aws:glue:us-west-2:111122223333:catalog/s3tablescatalog/*",
           "arn:aws:glue:us-west-2:111122223333:database/s3tablescatalog/*/*",
           "arn:aws:glue:us-west-2:111122223333:table/s3tablescatalog/*/*/*",
           "arn:aws:glue:us-west-2:111122223333:database/*",
           "arn:aws:glue:us-west-2:111122223333:table/*/*"
         ]
       },
       {
         "Sid": "S3TablesDataAccessPermissions",
         "Effect": "Allow",
         "Action": [
           "s3tables:GetTableBucket",
           "s3tables:GetNamespace",
           "s3tables:GetTable",
           "s3tables:GetTableMetadataLocation",
           "s3tables:GetTableData",
           "s3tables:ListTableBuckets",
           "s3tables:CreateTable",
           "s3tables:PutTableData",
           "s3tables:UpdateTableMetadataLocation",
           "s3tables:ListNamespaces",
           "s3tables:ListTables",
           "s3tables:DeleteTable"
         ],
         "Resource": [
           "arn:aws:s3tables:us-west-2:111122223333:bucket/*",
           "arn:aws:s3tables:us-west-2:111122223333:bucket/*/table/*"
         ]
       }
     ]
   }
   ```

1. Choose **Review policy**.

1. On the **Review policy** page, enter `GlueCatalogS3Tables_Policy` for **Name**. Optionally, enter a description. Review the policy summary, then choose **Create policy**.

**To create an IAM role for Amazon Redshift:**

1. Open the [IAM console](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**.

1. Choose **Create role**.

1. Choose **AWS service** as the trusted entity, then choose **Redshift** as the use case.

1. Under **Use case for other AWS services**, choose **Redshift - Customizable**, then choose **Next**.

1. On the **Add permissions** page, attach the `GlueCatalogS3Tables_Policy` policy you created above. Choose **Next**.

1. For **Role name**, enter a name for your role, for example `RedshiftS3TablesRole`.

1. Review the information, then choose **Create role**.

1. In the navigation pane, choose **Roles**. Choose the name of your new role to view the summary, then copy the **Role ARN** to your clipboard. You will use this ARN when creating external schemas for S3 Tables namespaces.

**Note**  
Scope down to specific resources by replacing the wildcard with exact Amazon Resource Names (ARNs).

### Step 2: Attach an IAM role to your Amazon Redshift cluster
<a name="querying-s3Tables-step2"></a>

Associate the IAM role you configured in Step 1 with your Amazon Redshift cluster.

**Using the AWS Management Console:**

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Clusters**, then choose the cluster that you want to update.

1. For **Actions**, choose **Manage IAM roles** to display the current list of IAM roles associated with the cluster.

1. On the **Manage IAM roles** page, choose the IAM role to add, then choose **Add IAM role**.

1. Choose **Done** to save your changes.

**Using the AWS CLI:**

Run the following command to associate an IAM role with an existing cluster or namespace. Replace `my-redshift-cluster` or `my-redshift-namespace` with your cluster identifier or namespace and `111122223333` with your AWS account ID.

```
aws redshift modify-cluster-iam-roles \
    --cluster-identifier my-redshift-cluster \
    --add-iam-roles arn:aws:iam::111122223333:role/RedshiftS3TablesRole

-- for serverless
aws redshift-serverless update-namespace \
    --namespace-name my-redshift-namespace \
    --iam-roles "arn:aws:iam::111122223333:role/RedshiftS3TablesRole"
```

For more information, see [Associating IAM roles with clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/copy-unload-iam-role.html) in the *Amazon Redshift Management Guide*.

### Step 3: Query S3 Tables from Amazon Redshift
<a name="querying-s3Tables-step3"></a>

When you integrate S3 Tables with AWS Glue Data Catalog, the service creates a federated catalog structure that maps S3 Tables resources to AWS Glue catalog objects:
+ An S3 table bucket becomes a **catalog** in the AWS Glue Data Catalog.
+ An S3 namespace becomes a **AWS Glue database**.
+ An S3 table becomes a **AWS Glue table object**.

The integration creates the following hierarchy:
+ **Federated catalog:**`s3tablescatalog` (automatically created)
+ **Child catalogs:** Each S3 table bucket becomes a child catalog under `s3tablescatalog`.
+ **Databases:** Each S3 namespace within a table bucket becomes a database.
+ **Tables:** Each S3 table within a namespace becomes a table.

For example, if you have an S3 table bucket named `analytics-bucket` with a namespace `sales` containing a table `transactions`, the full path in the AWS Glue Data Catalog would be: `s3tablescatalog/analytics-bucket/sales/transactions`.

**Create a resource link**

Before using any of the three query methods below, you must create a resource link in AWS Glue Data Catalog. Resource links allow Amazon Redshift to reference S3 Tables databases through the standard catalog.

*Using the AWS Glue console:*

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1. In the navigation pane, choose **Databases**.

1. Choose **Create**, then choose **Resource link**.

1. On the **Create resource link** page, provide the following information:
   + **Resource link name:** Enter a name for the resource link (for example, `sales_resource_link`).
   + **Shared database:** Enter the S3 Tables database path (for example, `s3tablescatalog/analytics-bucket/sales`).
   + **Shared database owner:** Enter your AWS account ID.
   + **Shared database's catalog ID:** Enter the catalog ID in the format `<account-id>:s3tablescatalog/<bucket-name>`.

1. Choose **Create**.

*Using the AWS CLI:*

```
aws glue create-database \
  --region us-west-2 \
  --cli-input-json '{
        "CatalogId": "111122223333",
        "DatabaseInput": {
            "Name": "sales_resource_link",
            "TargetDatabase": {
                "CatalogId": "111122223333:s3tablescatalog/analytics-bucket",
                "DatabaseName": "sales"
            }
        }
  }'
```

This command creates a resource link named `sales_resource_link` in your default AWS Glue Data Catalog that points to the `sales` database in the S3 table bucket `analytics-bucket`.

After resource links are created, Amazon Redshift provides three methods to query S3 Tables. Choose the method that best fits your use case.

**Note**  
To create a resource link at the database level, the Redshift Administrator must have the `AWS Glue:CreateDatabase` permission on the default catalog and the database being created.

#### Method 1: CREATE EXTERNAL SCHEMA
<a name="querying-s3Tables-method1"></a>

Use `CREATE EXTERNAL SCHEMA` to create an external schema that references your S3 Tables database. This method provides explicit control over schema naming and configuration.

For complete syntax details, see [CREATE EXTERNAL SCHEMA](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_EXTERNAL_SCHEMA.html) in the *Amazon Redshift Database Developer Guide*.

**Example**

Use the database name and catalog ID from Step 3. Replace `111122223333` with your AWS account ID.

```
CREATE EXTERNAL SCHEMA s3tables_schema
FROM DATA CATALOG DATABASE 'sales_resource_link'
IAM_ROLE 'arn:aws:iam::111122223333:role/RedshiftS3TablesRole'
REGION 'us-west-2'
CATALOG_ID '111122223333';

SELECT * FROM s3tables_schema.transactions;
```

#### Method 2: CREATE DATABASE FROM ARN
<a name="querying-s3Tables-method2"></a>

Use `CREATE DATABASE` with the `FROM ARN` clause to create a federated database that directly references your AWS Glue resource link. This method automatically maps the AWS Glue database to a Redshift database.

For complete syntax details, see [CREATE DATABASE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_DATABASE.html) in the *Amazon Redshift Database Developer Guide*.

**Example**

Replace `111122223333` with your AWS account ID.

```
CREATE DATABASE s3tables_db
FROM ARN 'arn:aws:glue:us-west-2:111122223333:database/sales_resource_link'
WITH DATA CATALOG SCHEMA analytics_schema
IAM_ROLE 'arn:aws:iam::111122223333:role/RedshiftS3TablesRole';

SELECT * FROM s3tables_db.analytics_schema.transactions;
```

#### Method 3: Auto-mounted awsdatacatalog
<a name="querying-s3Tables-method3"></a>

Amazon Redshift can automatically mount AWS Glue Data Catalog databases, including S3 Tables resource links, through the `awsdatacatalog` database. This method requires federated access to Spectrum (FAS) to be enabled on your cluster.

**Prerequisites**

To use the auto-mounted `awsdatacatalog` database, you must enable federated access to Spectrum. This allows Amazon Redshift to use federated identity credentials to access AWS Glue Data Catalog and external data sources.

To enable federated access to Spectrum:

1. Connect to your Redshift cluster using an IAM identity with the following permissions:
   + `redshift:GetClusterCredentialsWithIAM` (for provisioned clusters) or `redshift-serverless:GetCredentials` (for Serverless)
   + `AmazonS3ReadOnlyAccess`
   + `AWSGlueConsoleFullAccess`
   + S3 Tables permissions (as defined in Step 1)

1. When you connect with an IAM identity, Amazon Redshift automatically creates a database user prefixed with `IAM:` (for users) or `IAMR:` (for roles).

1. As a cluster administrator, grant the federated user permissions to access the external schema. Replace `my_user` with your IAM role or user name:

   ```
   GRANT ALL ON SCHEMA awsdatacatalog TO "IAMR:my_user";
   ```

For detailed instructions on setting up federated access, see [Using a federated identity to manage Amazon Redshift access to local resources and Amazon Redshift Spectrum external tables](https://docs.aws.amazon.com/redshift/latest/mgmt/authorization-fas-spectrum.html) in the *Amazon Redshift Management Guide*.

**Query S3 Tables**

After federated access is configured, verify the mounted schemas and query your S3 Tables.

Verify mounted schemas:

```
SHOW SCHEMAS FROM DATABASE awsdatacatalog;
```

Query S3 Tables using the resource link name from Step 3:

```
SELECT * FROM awsdatacatalog.sales_resource_link.transactions;
```
# Registering an Amazon S3 table bucket in another AWS account

You can register individual Amazon S3 table buckets (ARN
format:`arn:aws:s3tables:us-east-1:`account-id`:bucket/`bucket-name``)
from one AWS account with Lake Formation in another account. For example, you can register a table
bucket from account A in account B's Lake Formation.

## Prerequisites

Before beginning the cross-account bucket registration:

- Create a table bucket in account A.
- Create an IAM role in account B with appropriate permissions for bucket
  registration.

For more information about the permissions required to register a table bucket with Lake Formation, see [Prerequisites for integrating Amazon S3 tables catalog with the Data Catalog and Lake Formation](s3tables-catalog-prerequisites.md "s3tables-catalog-prerequisites.md") .

- Register the table bucket in the account where you are going to create the S3 table catalog.
- For cross-account access, the role specified when registering the table bucket must
  be an in-account role with appropriate permissions to access the cross-account bucket.
  The role needs necessary S3 Tables IAM actions to access bucket resources.

## Cross-account table bucket registration

In the following procedures, account A is the resource owning account, and account B is
where the table bucket will be registered for managing access permissions.

1. Sign in to the AWS Management Console in account A.

Open the Amazon S3 console at
[https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/"). 2. Create a table bucket. For more information, see [Creating a table
bucket](../../../AmazonS3/latest/userguide/s3-tables-buckets-create.md "../../../AmazonS3/latest/userguide/s3-tables-buckets-create.md") in the Amazon S3 User Guide. 3. Register the table bucket in account B.

Use the AWS CLI to register the table bucket from account A with Lake Formation in account
B.

```
aws lakeformation register-resource \
--resource-arn 'arn:aws:s3tables:us-east-1:account-A-id:bucket/single-bucket-name' \
--role-arn arn:aws:iam::account-B-id:role/role-name \
--region us-east-1
```

Replace account-A-id, single-bucket-name, account-B-id, and role-name with your
specific values. 4. Next, create a catalog for the table bucket in account B.

Create a catalog using the AWS CLI.

```
aws glue create-catalog --region us-east-1 \
--cli-input-json \
'{
   "Name": "catalog-name",
   "CatalogInput" : {
      "FederatedCatalog": {
         "Identifier": "arn:aws:s3tables:us-east-1:account A:bucket/single-bucket-name",
         "ConnectionName": "aws:s3tables"
      },
      "CreateDatabaseDefaultPermissions": [],
      "CreateTableDefaultPermissions": []
   }
}'
```

Replace catalog-name, account-A-id, and bucket-name with your specific values.

The following CLI example shows how to view the details of the catalog.

```

aws glue get-catalog \
  --catalog-id account-id:catalog-name \
  --region us-east-1
```

5. Next, create databases and tables in newly created catalog in account B.

Create a database.

```
aws glue create-database \
  --region us-east-1 \
  --catalog-id "account-B-id:catalog-name" \
  --database-input \
'{
  "Name": "database-name"
}'
```

Create a table.

```
aws glue create-table \
  --database-name database-name \
  --catalog-id account-B-id:catalog-name\
  --region us-east-1 \
  --table-input \
  '{
        "Name": "table-name",
        "Parameters": {
            "format": "ICEBERG"
        },
        "StorageDescriptor": {
           "Columns": [
        {"Name": "x", "Type": "int", "Parameters": {"required": "true"}}
          ]
        }
}'
```

Replace database-name, account-B-id, catalog-name, and table-name with your specific
values. 6. The following examples show how to view the objects in the catalog.

View database details.

```
aws glue get-database \
  --name database-name \
  --catalog-id account-B-id:catalog-name \
  --region us-east-1
```

View table details.

```
aws glue get-table \
  --name table-name \
  --database-name database-name \
  --catalog-id account-B-id:catalog-name \
  --region us-east-1
```

Replace database-name, account-B-id, catalog-name, and table-name with your specific values.

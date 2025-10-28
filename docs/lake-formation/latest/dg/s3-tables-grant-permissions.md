# Granting permissions

After integrating your S3 tables with AWS Lake Formation, you can grant permissions on the S3
tables catalog and the catalog objects (table buckets, databases, tables) to other IAM roles and users in your account. Lake Formation
permissions allows you to define access controls at table, column, and row-level granularity
for users of integrated analytical engines such as Amazon Redshift Spectrum and Athena.

You can grant permissions by using either the named resource method or the Lake Formation tag-based access control (LF-TBAC) method.
Before granting permissions using LF-Tags and LF-Tag expressions, you must define them and assing them to Data Catalog objects.

For more information, see [Managing LF-Tags for metadata access control](managing-tags.md "managing-tags.md").

You can share databases and tables with external AWS accounts by granting Lake
Formation permissions to the external accounts. Users can then run queries and jobs that join
and query tables across multiple accounts. When you share a catalog resource with another
account, principals in that account can operate on that resource as if the resource were in
their Data Catalog.

When you share databases and tables with external accounts, the **Super user**
permission is not available.

For detailed instructions about granting permissions, see the [Managing Lake Formation permissions](managing-permissions.md "managing-permissions.md") section.

## AWS CLI example for granting permissions on an Amazon S3 Table

```
aws lakeformation grant-permissions \
--cli-input-json \
'{
    "Principal": {
        "DataLakePrincipalIdentifier":"arn:aws:iam::`111122223333`:role/`DataAnalystRole`"
    },
    "Resource": {
        "Table": {
            "CatalogId":"`111122223333`:`s3tablescatalog`/`amzn-s3-demo-bucket1`",
            "DatabaseName":"`S3 table bucket namespace <example_namespace>`",
            "Name":"`S3 table bucket table name <example_table>`"
        }
    },
    "Permissions": [
        "SELECT"
    ]
}'

```

The following are the parameters to include in the command:

- DataLakePrincipalIdentifier – IAM user, role, or group ARN to grant permissions
- CatalogId – 12-digit AWS account ID that owns the Data Catalog
- DatabaseName – Name of the Amazon S3 table bucket name space
- Name – Amazon S3 table bucket table name
- Permissions – Permissions to grant. Options include: SELECT, INSERT, DELETE, DESCRIBE, ALTER, DROP, ALLL, and SUPER

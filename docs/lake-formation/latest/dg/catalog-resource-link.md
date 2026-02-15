# Accessing a shared federated catalog

AWS Lake Formation cross-account capabilities allow users to securely share distributed data lakes across multiple AWS accounts, AWS organizations,
or directly with IAM principals in another account providing fine-grained access to the metadata and underlying data.

Lake Formation uses the AWS Resource Access Manager (AWS RAM) service to facilitate resource sharing. When you share a
catalog resource with another account, AWS RAM sends an invitation to the grantee account to
accept or reject the resource grant.

Integrated analytical services such as Amazon Athena and Redshift Spectrum require resource links to be
able to include shared resources in queries. Principals need to create a resource link in
their AWS Glue Data Catalog to a shared resource from another AWS account. For more information
about resource links, see [How
resource links work in Lake Formation](resource-links-about.md "resource-links-about.md").

A _Catalog link container_ is a Data Catalog object, which references a
local or cross-account federated database-level catalog from other AWS accounts. You can
also create database links and table links within a catalog link container. When you create a
database link or a table link, you must specify a target resource that resides under the same
target Amazon Redshift database-level catalog (Amazon Redshift database).

To create a catalog link container, you need the Lake Formation `CREATE_CATALOG` or
the `glue:CreateCatalog` permission.

You must have **Cross account version settings** version 4 or higher for sharing databases or tables in the federated catalog across AWS accounts.

## Creating a catalog link container to a

cross-account federated catalog

You can create a catalog link container that points to a Redshift database-level
federated catalog in any AWS Region by using the AWS Lake Formation console, AWS Glue
`CreateCatalog` API, or AWS Command Line Interface (AWS CLI).

###### To create a catalog link container to a shared catalog (console)

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"). Sign in as a principal who
   has the Lake Formation `CREATE_CATALOG` permission.
2. In the navigation pane, choose **Catalogs**, and then choose
   **Create catalog**.
3. On the **Set catalog details** page, provide the following information:

**Name**

Enter a name that adheres to the same rules as a catalog name. The name can be the
same as the target shared catalog.

**Type**

Choose **Catalog link container** as the type of catalog.

**Source**

Choose `Redshift`.

**Target Redshift catalog**

Select a Redshift database-level federated catalog or choose a local (owned)
catalog from the list.

The list contains all the catalogs shared with your account. Note the catalog
owner account ID is listed with each catalog. If you don't see a catalog that you
know was shared with your account, check the following:

    * If you aren't a data lake administrator, check that the data lake
     administrator granted you Lake Formation permissions on the catalog.
    * If you are a data lake administrator, and your account is not in the same
     AWS organization as the granting account, ensure that you have accepted the
     AWS Resource Access Manager (AWS RAM) resource share invitation for the catalog. For more information,
     see [Accepting a resource share invitation from AWS RAM](accepting-ram-invite.md "accepting-ram-invite.md").

###### Note

When creating a catalog link container through the console, the
**Target Redshift Catalog** dropdown might display `No
 matches` when attempting to select a cross-account Redshift catalog.
Despite this display, you can manually enter the target ARN of the Amazon Redshift
federated database-level catalog (Amazon Redshift database) in the input field, and the
form will still work correctly. For example:
`arn:aws:glue:us-east-1:123456789012:catalog/federated-catalog-redshift/dev`.

This behavior occurs because the console can only search for potential candidates within the currently signed-in account.
The dropdown is intended as an auto-complete feature, but you can still manually input ARNs for cross-account access. 4. To enable Apache Iceberg query engines to read and write to Amazon Redshift namespaces, AWS Glue creates
a managed Amazon Redshift cluster with the compute and storage resources required to
perform read and write operations without impacting Amazon Redshift data warehouse
workloads. You need to provide an IAM role with the permissions required
to transfer data to and from the Amazon S3 bucket. 5. Choose **Next**. 6. (Optional) Choose **Add permissions** to grant permissions to other principals.

However, granting permissions on a catalog link container doesn't grant permissions on the
target (linked) catalog. You must grant permissions on the target catalog
separately for the catalog link to be visible in Athena. 7. Next, review the catalog link container details and choose **Create catalog**.

You can then view the link container name under the **Catalogs**
page.

Now, you can create database links and table links in the catalog link container to enable access from query engines.

###### Create a catalog link container CLI example

- In the following example, the `TargetRedshiftCatalog` object specifies the arn of the Amazon Redshift federated database-level catalog (Amazon Redshift database).
  The `DataLakeAccess` must be enabled when you create the catalog link container.

```
aws glue create-catalog \
  --cli-input-json
    '{
        "Name": "linkcontainer",
        "CatalogInput": {
            "TargetRedshiftCatalog": {
               "CatalogArn": "arn:aws:us-east-1:123456789012:catalog/nscatalog/dev"
             },
            "CatalogProperties": {
              "DataLakeAccessProperties" : {
                "DataLakeAccess" : true,
                "DataTransferRole" : "arn:aws:iam::111122223333:role/DataTransferRole"
             }
           }
        }
    }'

```

## Creating resource links under the catalog link container

You can create resource links to databases and tables links under a catalog link container.
When you create database resource links or table resource links, you must specify a target resource that resides under the same target Amazon Redshift database-level catalog (Amazon Redshift database) that the link container points to.

You can create a resource link to a shared Amazon Redshift database or a table by using the AWS Lake Formation console, API, or
AWS Command Line Interface (AWS CLI).

- For detailed instructions, see [Creating a resource link to a shared Data Catalog
  database](create-resource-link-database.md "create-resource-link-database.md").

Following is a AWS CLI example to create a database resource link under a catalog link container.

```
aws glue create-database \
  --cli-input-json \
    '{
        "CatalogId": "111122223333:linkcontainer",
        "DatabaseInput": {
            "Name": "dblink",
             "TargetDatabase": {
               "CatalogId": "123456789012:nscatalog/dev",
                "DatabaseName": "schema1"
             }
        }
    }'

```

- To create a table resource link under a catalog link container, you need to first create a AWS Glue database in the local AWS Glue Data Catalog to contain the table resource link.

For more information on creating resource links to shared tables, see [Creating a resource link to a shared Data Catalog
table](create-resource-link-table.md "create-resource-link-table.md").

    + Create a database to contain the table resource link example



    ```
    aws glue create-database \
      --cli-input-json \
          '{
              "CatalogId": "111122223333:linkcontainer",
              "DatabaseInput": {
                  "Name": "db1",
                  "Description": "creating parent database for table link"
              }
          }'

    ```
    + Create table resource link example



    ```
    aws glue create-table \
      --cli-input-json \
        '{
            "CatalogId": "111122223333:linkcontainer",
             "DatabaseName": "db1",
            "TableInput": {
                "Name": "tablelink",
                "TargetTable": {
                    "CatalogId": "123456789012:nscatalog/dev",
                   "DatabaseName": "schema1",
                    "Name": "table1"
                 }
            }
        }'

    ```

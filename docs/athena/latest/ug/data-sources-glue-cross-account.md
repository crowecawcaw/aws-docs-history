# Register a Data Catalog from another

account

You can use Athena's cross-account AWS Glue catalog feature to register an AWS Glue catalog from
an account other than your own. After you configure the required IAM permissions for AWS Glue
and register the catalog as an Athena `DataCatalog` resource, you can use Athena to
run cross-account queries. For information about configuring the required permissions, see
[Configure cross-account
access to AWS Glue data catalogs](security-iam-cross-account-glue-catalog-access.md "security-iam-cross-account-glue-catalog-access.md").

The following procedure shows you how to use the Athena to configure an AWS Glue Data Catalog in an
Amazon Web Services account other than your own as a data source.

## Register from console

1. Follow the steps in [Configure cross-account
   access to AWS Glue data catalogs](security-iam-cross-account-glue-catalog-access.md "security-iam-cross-account-glue-catalog-access.md") to ensure that
   you have permissions to query the data catalog in the other account.
2. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
3. If the console navigation pane is not visible, choose the expansion menu
   on the left.

![Choose the expansion menu.](images/nav-pane-expansion.png) 4. Choose **Data sources and catalogs**. 5. On the upper right, choose **Create data source**. 6. On the **Choose a data source** page, for **Data
sources**, choose **S3 - AWS Glue Data Catalog**, and then
choose **Next**. 7. On the **Enter data source details** page, in the
**AWS Glue Data Catalog** section, for **Choose an
AWS Glue Data Catalog**, choose **AWS Glue Data Catalog in another
account**. 8. For **Data source details**, enter the following
information:

    * **Data source name** – Enter the name that you
     want to use in your SQL queries to refer to the data catalog in the other
     account.
    * **Description** – (Optional) Enter a description
     of the data catalog in the other account.
    * **Catalog ID** – Enter the 12-digit Amazon Web Services
     account ID of the account to which the data catalog belongs. The Amazon Web Services
     account ID is the catalog ID.

9. (Optional) For **Tags**, enter key-value pairs that you want to
   associate with the data source. For more information about tags, see [Tag Athena resources](tags.md "tags.md").
10. Choose **Next**.
11. On the **Review and create** page, review the information that
    you provided, and then choose **Create data source**. The
    **Data source details** page lists the databases and tags for
    the data catalog that you registered.
12. Choose **Data sources and catalogs**. The data catalog that you registered is
    listed in the **Data source name** column.
13. To view or edit information about the data catalog, choose the catalog, and then
    choose **Actions**, **Edit**.
14. To delete the new data catalog, choose the catalog, and then choose
    **Actions**, **Delete**.

## Register using API operations

1. The following `CreateDataCatalog` request body registers an AWS Glue catalog
   for cross-account access:

```
# Example CreateDataCatalog request to register a cross-account Glue catalog:
{
    "Description": "`Cross-account Glue catalog`",
    "Name": "`ownerCatalog`",
    "Parameters": {"catalog-id" : "`<catalogid>`"  # Owner's account ID
    },
    "Type": "GLUE"
}
```

2. The following sample code uses a Java client to create the `DataCatalog`
   object.

```
# Sample code to create the DataCatalog through Java client
CreateDataCatalogRequest request = new CreateDataCatalogRequest()
    .withName("`ownerCatalog`")
    .withType(DataCatalogType.GLUE)
    .withParameters(ImmutableMap.of("catalog-id", "`<catalogid>`"));

athenaClient.createDataCatalog(request);
```

After these steps, the borrower should see
`ownerCatalog` when it calls the [ListDataCatalogs](../APIReference/API_ListDataCatalogs.md "../APIReference/API_ListDataCatalogs.md") API operation.

## Register using AWS CLI

Use the followig example CLI command to register an AWS Glue Data Catalog from another account

```
aws athena create-data-catalog \
  --name cross_account_catalog \
  --type GLUE \
  --description "`Cross Account Catalog`" \
  --parameters catalog-id=`<catalogid>`
```

For more information, see [Query
cross-account AWS Glue Data Catalogs using Amazon Athena](https://aws.amazon.com/blogs/big-data/query-cross-account-aws-glue-data-catalogs-using-amazon-athena/ "https://aws.amazon.com/blogs/big-data/query-cross-account-aws-glue-data-catalogs-using-amazon-athena/") in the _AWS Big Data
Blog_.

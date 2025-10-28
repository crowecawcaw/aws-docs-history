# Updating a federated catalog

You can update a Amazon Redshift federated catalog in the Data Catalog using the Lake Formation console, the AWS CLI or the [UpdateCatalog](../../../glue/latest/webapi/API_UpdateCatalog.md "../../../glue/latest/webapi/API_UpdateCatalog.md") API operation.

AWS Management Console
Follow these steps to update your federated catalog using Lake Formation console.

1. Sign in to the AWS Management Console, and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. In the left navigation pane, choose **Catalogs** under **Data Catalog**.
3. On the **Catalogs** page, choose the Amazon Redshift federated catalog you want to update.
4. Under **Actions**, choose **Edit**.
5. On the **Set Catalog details** screen, under the **Access from
   engines** section, choose **Access this catalog from Iceberg
   compatible engines**. Checking this option will enable data lake access
   for Apache Iceberg compatible query engines.
6. Next, create a new IAM role or choose an existing IAM role that has the policy that grants permissions to perform data transfer to and from the Amazon S3 bucket.

For more information on permissions, see [Prerequisites for managing Amazon Redshift namespaces in the AWS Glue Data Catalog](redshift-ns-prereqs.md "redshift-ns-prereqs.md"). 7. By default, your data in the Amazon Redshift cluster is encrypted using an
AWS managed key. If you choose to encrypt data using a customer managed key,
either create a KMS key or choose an existing key that has the permissions defined
in the [Prerequisites for managing Amazon Redshift namespaces in the AWS Glue Data Catalog](redshift-ns-prereqs.md "redshift-ns-prereqs.md") section. 8. Choose **Save**.

Upon successful completion, the **Catalog details** page shows
the managed workgroup name with the status as "Success".

AWS CLI
The following is an example of the `update-catalog` CLI input with the data lake access disabled by
setting the `DataLakeAacess` parameter value as `false`.

```
aws glue update-catalog  --cli-input-json \
'{
    "Name": "nscatalog",
    "CatalogInput": {
        "Description": "Redshift published catalog",
        "CreateDatabaseDefaultPermissions" : [],
        "CreateTableDefaultPermissions": [],
        "FederatedCatalog": {
            "Identifier": "arn:aws:redshift:us-east-1:123456789012:datashare:11524d7f-f56d-45fe-83f7-d7bb0a4d6d71/ds_internal_namespace",
            "ConnectionName": "aws:redshift"
        },
        "CatalogProperties": {
          "DataLakeAccessProperties" : {
            "DataLakeAccess" : false
        }
       }
    }
}'
```

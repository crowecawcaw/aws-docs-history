# Create an Amazon SageMaker Unified Studio data source for

AWS Glue in the project catalog

In Amazon SageMaker Unified Studio, you can create an AWS Glue Data Catalog data source in order to import technical
metadata of database tables from AWS Glue. To add a data source for the AWS Glue Data Catalog, the
source database must already exist in AWS Glue. Your Amazon SageMaker Unified Studio project’s IAM role also
needs certain permissions to be able to create a data source, as described in the
section [Configure
Lake Formation permissions for Amazon SageMaker Unified Studio](lake-formation-permissions-for-amazon-sagemaker-unified-studio.md "lake-formation-permissions-for-amazon-sagemaker-unified-studio.md").

When you create and run an AWS Glue data source, you add assets from the source AWS Glue
database to your Amazon SageMaker Unified Studio project's inventory. You can run your AWS Glue data sources on a
set schedule or on demand to create or update your assets' technical metadata. During
the data source runs, you can optionally choose to publish your assets to the Amazon SageMaker Unified Studio
catalog and thus make them discoverable by all domain users. You can also publish your
project inventory assets after editing their business metadata. Domain users can search
for and discover your published assets, and request subscriptions to these assets.

###### Note

Adding a data source in the project catalog makes it possible to publish that data
into the Amazon SageMaker Catalog. To add a data source for analyzing and editing within
your project, use the **Data** page of your project. Data that you
add to your connect to on the **Data** page can also be published
to the Amazon SageMaker Catalog. For more information, see [The lakehouse architecture of Amazon SageMaker](lakehouse.md "lakehouse.md").

###### To create an AWS Glue data source

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Choose **Select project** from the top navigation pane and
   select the project to which you want to add the data source.
3. Choose **Data sources** from the left navigation pane under
   **Project catalog**.
4. Choose **Create data source**.
5. Configure the following fields:
   - **Name** – The data source name.
   - **Description** – The data source
     description.

6. Under **Data source type**, choose
   **AWS Glue**.
7. (Optional) Under **Connection**, select **Import data
   lineage** if you want to import lineage for the data sources that
   use the connection.
8. Under **Data selection**, provide an AWS Glue database and
   provide a catalog, database names, and criteria for tables. For example, if you
   choose **Include** and enter `*corporate`, the
   database will include all source tables that end with the word
   `corporate`.

You can either choose an AWS Glue catalog from the dropdown or type a catalog
name. The dropdown includes the default AWS Glue catalog for the connection
account.

You can add multiple include and exclude rules for tables. You can also add
multiple databases using the **Add another database**
button. 9. Choose **Next**. 10. For **Publishing settings**, choose whether assets are
immediately discoverable in the Amazon SageMaker Catalog. If you only add them to the
inventory, you can choose subscription terms later and then publish them to the
Amazon SageMaker Catalog. 11. For **Metadata generation methods**, choose whether to
automatically generate metadata for assets as they're imported from the
source. 12. Under **Data quality**, you can choose to **Enable
data quality for this data source**. If you do this, Amazon SageMaker Unified Studio
imports your existing AWS Glue data quality output into your Amazon SageMaker Unified Studio catalog. By
default, Amazon SageMaker Unified Studio imports the latest existing 100 quality reports with no
expiration date from AWS Glue.

Data quality metrics in Amazon SageMaker Unified Studio help you understand the completeness and
accuracy of your data sources. Amazon SageMaker Unified Studio pulls these data quality metrics from
AWS Glue in order to provide context during a point in time, for example, during a
business data catalog search. Data users can see how data quality metrics change
over time for their subscribed assets. Data producers can ingest AWS Glue data
quality scores on a schedule. The Amazon SageMaker Unified Studio business data catalog can also
display data quality metrics from third-party systems through data quality APIs. 13. (Optional) For **Metadata forms**, add forms to define the
metadata that is collected and saved when the assets are imported into
Amazon SageMaker Unified Studio. For more information, see [Create a metadata form in Amazon SageMaker Unified Studio](create-metadata-form.md "create-metadata-form.md"). 14. Choose **Next**. 15. For **Run preference**, choose when to run the data
source.

    * **Run on a schedule** – Specify the dates and
     time to run the data source.
    * **Run on demand** – You can manually initiate
     data source runs.

16. Choose **Next**.
17. Review your data source configuration and choose
    **Create**.
    You can also create a Amazon SageMaker Unified Studio data source for Amazon Redshift by invoking the
    `CreateDataSource` API action or the `create-data-source` CLI
    action:

```

aws datazone create-data-source --cli-input-json file://create-sagemaker-datasource-example.json

```

Sample payload (create-sagemaker-datasource-example.json per example above) to create
an Amazon Sagemaker data sources in an Amazon DataZone domain:

```

{
  "name": "my-data-source",
  "projectIdentifier": "project123",
  "type": "GLUE",
  "description": "Description of the datasource",
  "environmentIdentifier": "environment123",
  "configuration": {
    "glueRunConfiguration": {
        "autoImportDataQualityResult": "True",
        "relationalFilterConfigurations": [{
            "databaseName": "my_database",
            "filterExpressions": [{
                "expression": "*",
                "type": "INCLUDE"
            }]
        }]
    }
  },
  "recommendation": {
    "enableBusinessNameGeneration": "True"
  },
  "enableSetting": "ENABLED",
  "schedule": {
    "timezone": "UTC",
    "schedule": "cron(7 22 * * ? *)"
  },
  "publishOnImport": "True",
  "assetFormsInput": [
    {
      "formName": "AssetCommonDetailsForm"
      "typeIdentifier": "amazon.datazone.AssetCommonDetailsFormType",
      "typeRevision": "3",
      "content": "form-content",
      "renderingConfig": {
        "collapse": "True""
      }
    }
  ],
  "clientToken": "123456"
}

```

Sample payload (create-sagemaker-datasource-example.json per example above) to create
an Amazon Sagemaker data sources in an Amazon SageMaker unified domain:

```

{
  "name": "my-data-source",
  "projectIdentifier": "project123",
  "type": "GLUE",
  "description": "Description of the datasource",
  "connectionIdentifier": "connection123",
  "configuration": {
    "glueRunConfiguration": {
        "catalogName": "my_catalog",
        "autoImportDataQualityResult": "True",
        "relationalFilterConfigurations": [{
            "databaseName": "my_database",
            "filterExpressions": [{
                "expression": "*",
                "type": "INCLUDE"
            }]
        }]
    }
  },
  "recommendation": {
    "enableBusinessNameGeneration": "True"
  },
  "enableSetting": "ENABLED",
  "schedule": {
    "timezone": "UTC",
    "schedule": "cron(7 22 * * ? *)"
  },
  "publishOnImport": "True",
  "assetFormsInput": [
    {
      "formName": "AssetCommonDetailsForm"
      "typeIdentifier": "amazon.datazone.AssetCommonDetailsFormType",
      "typeRevision": "3",
      "content": "form-content"
    }
  ],
  "clientToken": "123456"
}

```

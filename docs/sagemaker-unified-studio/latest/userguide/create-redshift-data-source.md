# Create an Amazon SageMaker Unified Studio data source for

Amazon Redshift in the project catalog

In Amazon SageMaker Unified Studio, you can create an Amazon Redshift data source in order to import technical
metadata of database tables and views from the Amazon Redshift data warehouse. To add a
Amazon SageMaker Unified Studio data source for Amazon Redshift, the source data warehouse must already exist in the
Amazon Redshift.

When you create and run an Amazon Redshift data source, you add assets from the source
Amazon Redshift data warehouse to your Amazon SageMaker Unified Studio project's inventory. You can run your Amazon Redshift
data sources on a set schedule or on demand to create or update your assets' technical
metadata. During the data source runs, you can optionally choose to publish your project
inventory assets to the Amazon SageMaker Unified Studio catalog and thus make them discoverable by all domain
users. You can also publish your inventory assets after editing their business metadata.
Domain users can search for and discover your published assets and request subscriptions
to these assets.

###### Note

Adding a data source in the project catalog makes it possible to publish that data
into the Amazon SageMaker Catalog. To add a data source for analyzing and editing within
your project, use the **Data** page of your project. Data that you
add to your connect to on the **Data** page can also be published
to the Amazon SageMaker Catalog. For more information, see [The lakehouse architecture of Amazon SageMaker](lakehouse.md "lakehouse.md").

###### To add an Amazon Redshift data source

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
   **Amazon Redshift**.
7. Under **Connection**, select a connection for your data
   source. The connection cannot be changed after the data source is
   created.
8. Under **Data selection**, provide an Amazon Redshift database schema
   name and enter your table or view selection criteria. For example, if you choose
   **Include** and enter `*corporate`, the asset
   will include all source tables that end with the word
   `corporate`.

You can add multiple include rules. You can also add another schema using the
**Add another schema** button. 9. Choose **Next**. 10. For **Publishing settings**, choose whether assets are
immediately discoverable in Amazon SageMaker Catalog. If you only add them to the
inventory, you can choose subscription terms later and then publish them to the
Amazon SageMaker Catalog. 11. For **Metadata generation methods**, choose whether to
automatically generate metadata for assets as they're published and updated from
the source. 12. (Optional) For **Metadata forms**, add forms to define the
metadata that is collected and saved when the assets are imported into
Amazon SageMaker Unified Studio. For more information, see [Create a metadata form in Amazon SageMaker Unified Studio](create-metadata-form.md "create-metadata-form.md"). 13. Choose **Next**. 14. For **Run preference**, choose when to run the data
source.

    * **Run on a schedule** – Specify the dates and
     time to run the data source.
    * **Run on demand** – You can manually initiate
     data source runs.

15. Choose **Next**.
16. Review your data source configuration and choose
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
  "type": "REDSHIFT",
  "description": "Description of the datasource",
  "environmentIdentifier": "environment123",
  "configuration": {
    "redshiftRunConfiguration": {
        "dataAccessRole": "arn:aws:iam::123456789012:role/my-data-access-role",
        "redshiftCredentialConfiguration": {
                "secretManagerArn": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-secret"
            },
        "redshiftStorage": {
            "redshiftClusterSource": {
                "clusterName": "my-redshift-cluster"
            }
        },
        "relationalFilterConfigurations": [{
            "databaseName": "my_database",
            "filterExpressions": [{
                "expression": "*",
                "type": "INCLUDE"
            }],
            "schemaName": "my_schema"
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

Sample payload (create-sagemaker-datasource-example.json per example above) to create
an Amazon Sagemaker data sources in an Amazon SageMaker unified domain:

```

{
  "name": "my-data-source",
  "projectIdentifier": "project123",
  "type": "REDSHIFT",
  "description": "Description of the datasource",
  "connectionIdentifier": "connection123",
  "configuration": {
    "redshiftRunConfiguration": {
        "dataAccessRole": "arn:aws:iam::123456789012:role/my-data-access-role",
        "redshiftCredentialConfiguration": {
                "secretManagerArn": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-secret"
            },
        "redshiftStorage": {
            "redshiftClusterSource": {
                "clusterName": "my-redshift-cluster"
            }
        },
        "relationalFilterConfigurations": [{
            "databaseName": "my_database",
            "filterExpressions": [{
                "expression": "*",
                "type": "INCLUDE"
            }],
            "schemaName": "my_schema"
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

# Amazon Redshift Managed Storage for the lakehouse architecture of Amazon SageMaker

You can manage Amazon Redshift tables in the lakehouse architecture of Amazon SageMaker by creating a Amazon Redshift managed catalog in the
AWS Glue Data Catalog (Data Catalog). With lakehouse architecture integration, you can access Amazon Redshift tables stored in the
Amazon Redshift managed storage (RMS) through Apache Iceberg REST APIs. The lakehouse architecture uses Data Catalog as the
technical catalog. The Data Catalog functions as the centralized metadata repository, storing
table schemas, partitioning information, and other metadata required for query planning and
execution. AWS Lake Formation provides fine-grained access to Redshift tables stored in RMS. You can
query and analyze Amazon Redshift data alongside your data lake assets.

## Amazon Redshift managed storage overview

Amazon Redshift Managed Storage provides the following benefits for your lakehouse architecture:

- **Unified data access** - Query Amazon Redshift tables directly from your lakehouse environment using familiar SQL interfaces
- **No data movement** - Access Amazon Redshift data in place without ETL processes or data duplication
- **Consistent governance** - Apply unified access controls and data governance policies across data warehouse and data lake
- **Performance optimization** - Leverage Amazon Redshift's columnar storage and query optimization for analytical workloads

## Creating Amazon Redshift managed catalog in the AWS Glue Data Catalog

You can create a Amazon Redshift managed catalog in the AWS Glue Data Catalog with RMS storage. This
catalog will contain the Amazon Redshift tables and databases that are accessible from open source
engines to serve to business intelligence (BI) applications.

You can get started by creating an AWS Glue
managed catalog using the `glue:CreateCatalog` API or the AWS Lake Formation console by setting
the catalog type as `Managed` and `Catalog source` as **Redshift.** This step does the following:

- Creates a catalog in the Data Catalog
- Registers the catalog as a Lake Formation data location
- creates an Amazon Redshift managed serverless-workgroup
- Links Amazon Redshift serverless workgroup and Data Catalog using a datashare object

###### To create a federated catalog (CLI)

- The following example shows how to create a federated catalog.

```
aws glue create-catalog --cli-input-json file://input.json

{
    "Name": `"CatalogName"`,
    "CatalogInput": {
      "Description": `"Redshift published Catalog"`,
      "CreateDatabaseDefaultPermissions" : [],
      "CreateTableDefaultPermissions": [],
      "CatalogProperties": {
        "DataLakeAccessProperties" : {
          "DataLakeAccess" : "true",
          "DataTransferRole" : `"DTR arn"`,
          "KMSKey": `"kms key arn"`,  // Optional
          "CatalogType": "aws:redshift"
        }
      }
    }
}

```

Glue get-catalog response

```
aws glue get-catalog \
  --catalog-id `account-id`:`catalog-name` \
  --region `us-east-1`

Response:
{
    "Catalog": {
        "Name": "CatalogName",
        "Description": "Glue Catalog for Redshift z-etl use case",
        "CreateDatabaseDefaultPermissions" : [],
        "CreateTableDefaultPermissions": [],
         "CatalogProperties": {
          "DataLakeAccessProperties" : {
            "DataLakeAccess": "true",
            "DataTransferRole": "DTR arn",
            "KMSKey": "kms key arn",
            "ManagedWorkgroupName": "MWG name",
            "ManagedWorkgroupStatus": "MWG status",
            "RedshiftDatabaseName": "RS db name",
            "NamespaceArn": "namespace key arn",
            "CatalogType": "aws:redshift"
         }
       }
    }
```

## Accessing Amazon Redshift data

Once RMS integration is established, you can access Amazon Redshift data through multiple interfaces:

- **SQL queries** - Use Amazon Athena or other SQL engines to query Amazon Redshift tables alongside Amazon S3 data
- **Data discovery** - Browse Amazon Redshift schemas and tables through the lakehouse data catalog
- **Cross-source joins** - Perform federated queries that join Amazon Redshift data with data lake sources
- **ML workflows** - Access Amazon Redshift data directly in Amazon SageMaker Unified Studio for machine learning model training and inference

## Best practices

Follow these best practices when working with Amazon Redshift Managed Storage:

- **Security** - Use IAM roles for authentication and implement least-privilege access principles
- **Performance** - Optimize queries by using appropriate filters and leveraging the distribution of Amazon Redshift and sort keys
- **Cost management** - Monitor query patterns and optimize Amazon Redshift cluster sizing based on usage
- **Data governance** - Apply consistent data classification and access policies across warehouse and lake

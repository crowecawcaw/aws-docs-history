# Bringing your data into the AWS Glue Data Catalog

You can create federated catalogs in the AWS Glue Data Catalog (Data Catalog) and unify data across Amazon S3 data lakes and Amazon Redshift data warehouses. You can also
integrate data from your operational databases such as Amazon DynamoDB, and third-party data sources such as PostgreSQL, Google BigQuery, MySQL, among others.
The Data Catalog provides a centralized metadata repository that
makes managing and discovering data across disparate systems easier.

The Data Catalog integrates with over 30 external data sources through federated connectors.
With this integration, you can query data from these external sources without having to build
data pipelines to ingest the data into AWS first.

After cataloging the external data, you can use AWS Lake Formation to centrally manage data access
permissions in the Data Catalog. Data lake administrators can grant fine-grained access permissions
to other IAM principals (users or roles) within the same account or across accounts using tag-based access control (LF-Tags) and named resources methods.

By using LF-Tags data administrators can logically organize resources based on attributes such as
domain and sensitivity level, simplifying permission management while ensuring
consistent access controls across analytics and machine learning services including Athena, Amazon EMR, AWS Glue or Redshift Spectrum.

The Data Catalog provides the following methods to manage data and permissions on external
datasets and external metastores:

- **Bring data in Amazon Redshift data warehouses into the AWS Glue Data Catalog**
  – Register an existing [Amazon Redshift](../../../redshift/index.md "../../../redshift/index.md") namespace or a cluster with the Data Catalog, and create a multi-level federated
  catalog in the Data Catalog.

You can access your data using any query engine compatible with Apache Iceberg REST
catalog OpenAPI specification, such as Amazon EMR Serverless, and Amazon Athena.

- **Federate into the Data Catalog from external data sources**
  – Connect the Data Catalog to external data sources using AWS Glue connections, and create
  federated catalogs to centrally manage access permissions on datasets using Lake Formation. No
  migration of metadata into the Data Catalog is necessary.
- **Integrate Amazon S3 Table buckets with Data Catalog (Preview)**
  – You can publish and catalog Amazon S3 Tables as Data Catalog objects and register the catalog
  as a Lake Formation data location from Lake Formation console or using AWS Glue API operations.
- **Create catalogs to manage Amazon Redshift tables in the Data Catalog**
  – You might not have an Amazon Redshift producer cluster or an Amazon Redshift datashare available today,
  but want to create and manage Amazon Redshift tables using Data Catalog. You can get started by creating an
  AWS Glue managed catalog using the `glue:CreateCatalog` API operation or the
  AWS Lake Formation console by setting the catalog type as `Managed` and `Catalog
source` as **Redshift.**
- **Publish Amazon Redshift datashares with Data Catalog** – Publish
  [Amazon Redshift](../../../redshift/index.md "../../../redshift/index.md") datashares to Data Catalog,
  and use Lake Formation to centrally manage data access of datashares and restrict user access.

You can query your data using Amazon Redshift Spectrum.

- **Connect Data Catalog to external Hive metastores** – Connect the
  Data Catalog to external metastores to manage access permissions on datasets in Amazon S3 using Lake Formation.
  No migration of metadata into the Data Catalog is necessary.
- **Integrate Lake Formation with AWS Data Exchange** – Lake Formation
  supports licensing access to your data through AWS Data Exchange. If you want to license your Lake Formation
  data, see [What
  is AWS Data Exchange](../../../data-exchange/latest/userguide/what-is.md "../../../data-exchange/latest/userguide/what-is.md") in the _AWS Data Exchange User Guide_.

###### Topics

- [Bringing Amazon Redshift data into the
  AWS Glue Data Catalog](managing-namespaces-datacatalog.md "managing-namespaces-datacatalog.md")
- [Federating into external data sources in the
  AWS Glue Data Catalog](federated-catalog-data-connection.md "federated-catalog-data-connection.md")
- [Creating an Amazon S3 Tables catalog in the AWS Glue Data Catalog](create-s3-tables-catalog.md "create-s3-tables-catalog.md")
- [Creating an Amazon Redshift managed catalog in the AWS Glue Data Catalog](create-rms-catalog.md "create-rms-catalog.md")
- [Managing permissions for data in an Amazon Redshift datashare](data-sharing-redshift.md "data-sharing-redshift.md")
- [Managing permissions on datasets that use external
  metastores](data-sharing-hms.md "data-sharing-hms.md")

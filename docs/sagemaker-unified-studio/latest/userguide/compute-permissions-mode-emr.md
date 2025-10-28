# Configuring permission mode for EMR Serverless in Amazon SageMaker Unified Studio

Permission mode is a configuration available to Spark compute resources such as Glue ETL or
EMR Serverless. It configures Spark to access different types of data based on the permissions
configured for that data. There are two configuration options for permission mode:

- Compatibility mode. This is a configuration for data managed using full-table access,
  meaning the compute engine can access all rows and columns in the data.
  Choosing this option enables your compute to work with data assets from AWS and from external systems.
- Fine-grained mode. This is a configuration for data managed using fine-grained access controls,
  meaning the compute engine can only access specific rows and columns from the full dataset.
  Choosing this option enables your Glue ETL
  to work with data asset subscriptions from Amazon SageMaker Catalog.
  You configure permission mode in EMR Serverless computes in Amazon SageMaker Unified Studio when you add a new
  EMR Serverless compute resource in your project. For more information, see [Adding a new EMR Serverless application](adding-new-emr-serverless.md "adding-new-emr-serverless.md").

###### Note

You cannot modify the permission mode after the EMR Serverless compute resource is created.
Instead, you can create another EMR Serverless compute resource with a different permission mode.

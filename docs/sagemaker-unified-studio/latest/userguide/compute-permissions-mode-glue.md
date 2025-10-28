# Configuring permission mode for Glue ETL in Amazon SageMaker Unified Studio

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
  To configure permission mode for Glue ETL in Amazon SageMaker Unified Studio, complete the following steps:

1.  Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
    using your SSO or AWS credentials.
2.  Navigate to a project.
3.  Navigate to the Visual ETL tool by using the dropdown **Build** menu and
    selecting **Visual ETL flows**.
4.  Navigate to a flow by creating one or selecting the flow from the list.
5.  From the dropdown menu next to the **Run** button,
    choose a compute connection type that aligns with your data access preference.

        * Select **project.spark.fineGrained** to configure permission mode to
         support fine-grained access control. Choosing this option configures your Visual ETL flow
         to work with data asset subscriptions from Amazon SageMaker Catalog.
        * Select **project.spark.compatibility** to configure permission mode
         to be compatible with general access control.
         Choosing this option configures your Visual ETL flow to work with data assets that you
         connect to from your project.

    You can then run the Visual ETL flow with data that aligns with your selected compute connection.

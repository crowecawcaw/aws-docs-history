# SQL extension features and usage

This section details the various features of the JupyterLab SQL extension in Studio,
and provides instructions on how to use them. Before you can use the SQL extension to access
and query data from your JupyterLab notebooks, an administrator must first configure the
connection to your data sources. For information on how administrators can create connections to
data sources, see [SQL extension data source
connections](sagemaker-sql-extension-datasources-connection.md "sagemaker-sql-extension-datasources-connection.md").

###### Note

To use the SQL extension, your JupyterLab application must run on a [SageMaker AI
distribution](https://github.com/aws/sagemaker-distribution/blob/main/README.md "https://github.com/aws/sagemaker-distribution/blob/main/README.md") image version 1.6 or higher. These SageMaker images have the extension
pre-installed.

The extension provides two components to help you access, discover, query, and analyze data
from pre-configured data sources.

- Use the _user interface_ of the SQL extension to
  discover and explore your data sources. The UI capabilities can be further divided into the
  following subcategories.
  - With the **data exploration** UI element, you can
    browse your data sources and explore their tables, columns, and metadata. For details on
    the data exploration features of the SQL extension, see [Browse data using SQL extension](sagemaker-sql-extension-features-data-discovery.md "sagemaker-sql-extension-features-data-discovery.md").
  - The **connection caching** element caches connections
    for quick access. For details on connection caching in the SQL extension, see [SQL extension
    connection caching](sagemaker-sql-extension-features-connection-caching.md "sagemaker-sql-extension-features-connection-caching.md").

- Use the _SQL Editor and Executor_ to write, edit, and
  run SQL queries against connected data sources.
  - With the **SQL editor** element, you can write,
    format, and validate SQL statements within the notebooks of your JupyterLab application
    in Studio. For details on the SQL editor features, see [SQL editor features of the
    JupyterLab SQL extension](sagemaker-sql-extension-features-editor.md "sagemaker-sql-extension-features-editor.md").
  - With the **SQL execution** element, you can run your
    SQL queries and visualize their results from the notebooks of your JupyterLab
    application in Studio. For details on the SQL execution capabilities, see [SQL execution features of the
    JupyterLab SQL extension](sagemaker-sql-extension-features-sql-execution.md "sagemaker-sql-extension-features-sql-execution.md").

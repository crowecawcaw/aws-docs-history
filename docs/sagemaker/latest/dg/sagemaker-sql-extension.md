# Data preparation with SQL in Studio

Amazon SageMaker Studio provides a built-in SQL extension. This extension allows data scientists
to perform tasks such as sampling, exploratory analysis, and feature engineering directly within
their JupyterLab notebooks. It leverages AWS Glue connections to maintain a
centralized data source catalog. The catalog stores metadata about various data sources. Through
this SQL environment, data scientists can browse data catalogs, explore their data, author
complex SQL queries, and further process the results in Python.

This section walks through configuring the SQL extension in Studio. It describes the
capabilities enabled by this SQL integration and provides instructions for running SQL queries
in JupyterLab notebooks.

To enable SQL data analysis, administrators must first configure AWS Glue connections to the
relevant data sources. These connections allow data scientists to seamlessly access authorized
datasets from within JupyterLab.

In addition to the administrator-configured AWS Glue connections, the SQL extension allows
individual data scientists to create their own data source connections. These user-created
connections can be managed independently and scoped to the user's profile through tag-based
access control policies. This dual-level connection model - with both administrator-configured
and user-created connections - provides data scientists with broader access to the data they
need for their analysis and modeling tasks. Users can set up the necessary connections to their
own data sources within the JupyterLab environment user interface (UI), without relying solely
on the centralized connections established by the administrator.

###### Important

The user-defined connections creation capability is available as a set of standalone
libraries in PyPI. To use this functionality, you need to install the following libraries in
your JupyterLab environment:

- [amazon-sagemaker-sql-editor](https://pypi.org/project/amazon-sagemaker-sql-editor/ "https://pypi.org/project/amazon-sagemaker-sql-editor/")
- [amazon-sagemaker-sql-execution](https://pypi.org/project/amazon-sagemaker-sql-execution/ "https://pypi.org/project/amazon-sagemaker-sql-execution/")
- [amazon-sagemaker-sql-magic](https://pypi.org/project/amazon-sagemaker-sql-magic/ "https://pypi.org/project/amazon-sagemaker-sql-magic/")
  You can install these libraries by running the following commands in your JupyterLab
  terminal:

```
pip install amazon-sagemaker-sql-editor>=0.1.13
pip install amazon-sagemaker-sql-execution>=0.1.6
pip install amazon-sagemaker-sql-magic>=0.1.3
```

After installing the libraries, you will need to restart the JupyterLab server for the
changes to take effect.

```
restart-jupyter-server
```

With access set up, JupyterLab users can:

- View and browse pre-configured data sources.
- Search, filter, and inspect database information elements such as tables, schemas, and
  columns.
- Auto-generate the connection parameters to a data source.
- Create complex SQL queries using the syntax-highlighting, auto-completion, and SQL
  formatting features of the extension's SQL editor.
- Run SQL statements from JupyterLab notebook cells.
- Retrieve the results of SQL queries as pandas DataFrames for further
  processing, visualization, and other machine learning tasks.
  You can access the extension by choosing the SQL extension icon (
  ![Icon of the SQL extension feature in JupyterLab.](images/studio/sqlexplorer/sqlexplorer-icon.png)
  ) in the left navigation pane of your JupyterLab application in
  Studio. Hovering over the icon displays its _Data
  Discovery_ tool tip.

###### Important

- The JupyterLab image in SageMaker Studio contains the SQL extension by default,
  starting with [SageMaker AI
  Distribution](https://github.com/aws/sagemaker-distribution "https://github.com/aws/sagemaker-distribution") 1.6. The extension works with Python and SparkMagic kernels
  only.
- The extension's user interface for exploring connections and data is only available in
  JupyterLab within Studio. It is compatible with [Amazon Redshift](https://aws.amazon.com/redshift/ "https://aws.amazon.com/redshift/"), [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/"), and [Snowflake](https://www.snowflake.com/en/ "https://www.snowflake.com/en/").

- If you are an administrator looking to create generic connections to data sources for
  the SQL extension, follow these steps:
  1.  Enable the network communication between your Studio domain and the data
      sources to which you want to connect. To learn about the networking requirements, see
      [Configure network access between Studio and data sources (for administrators)](sagemaker-sql-extension-networking.md "sagemaker-sql-extension-networking.md").
  2.  Check connection properties and instructions to create a secret for your data source
      in [Create secrets for database
      access credentials in Secrets Manager](sagemaker-sql-extension-glue-connection-secrets.md "sagemaker-sql-extension-glue-connection-secrets.md").
  3.  Create the AWS Glue connections to your data sources in [Create AWS Glue connections
      (for administrators)](sagemaker-sql-extension-datasources-glue-connection.md "sagemaker-sql-extension-datasources-glue-connection.md").
  4.  Grant the execution role of your SageMaker domain or user profiles the required
      permissions in [Set up the IAM
      permissions to access the data sources (for administrators)](sagemaker-sql-extension-datasources-connection-permissions.md "sagemaker-sql-extension-datasources-connection-permissions.md").

- If you are a data scientist looking to create your own connections to data sources for
  the SQL extension, follow these steps:
  1.  Have your administrator:
      - Enable the network communication between your Studio domain and the
        data sources to which you want to connect. To learn about the networking
        requirements, see [Configure network access between Studio and data sources (for administrators)](sagemaker-sql-extension-networking.md "sagemaker-sql-extension-networking.md").
      - Grant the execution role of your SageMaker domain or user profiles the required
        permissions in [Set up the IAM
        permissions to access the data sources (for administrators)](sagemaker-sql-extension-datasources-connection-permissions.md "sagemaker-sql-extension-datasources-connection-permissions.md").

      ###### Note

      Administrators can restrict user access to connections created within the
      JupyterLab application by configuring [tag-based access control](sagemaker-sql-extension-datasources-connection-permissions.md#user-defined-connections-permissions "sagemaker-sql-extension-datasources-connection-permissions.md#user-defined-connections-permissions")
      in the execution role.

  2.  Check connection properties and instructions to create a secret for your data source
      in [Create secrets for database
      access credentials in Secrets Manager](sagemaker-sql-extension-glue-connection-secrets.md "sagemaker-sql-extension-glue-connection-secrets.md").
  3.  Create your connection in JupyterLab UI using the instructions in [Create
      user-defined AWS Glue connections](sagemaker-sql-extension-datasources-glue-connection-user-defined.md "sagemaker-sql-extension-datasources-glue-connection-user-defined.md").

- If you are a data scientist looking to browse and query your data sources using the
  SQL extension, ensure that you or your administrator have set up the connections to your
  data sources first. Then, follow these steps:
  1.  Create a private space to launch your JupyterLab application in Studio using
      the SageMaker distribution image version 1.6 or higher.
  2.  If you are a user of the SageMaker distribution image version 1.6, load the
      SQL extension in a JupyterLab notebook by running `%load_ext
amazon_sagemaker_sql_magic` in a notebook cell.

  For users of SageMaker distribution image versions 1.7 and later, no action is needed,
  the SQL extension loads automatically. 3. Familiarize with the capabilities of the SQL extension in [SQL extension features and usage](sagemaker-sql-extension-features.md "sagemaker-sql-extension-features.md").

###### Topics

- [Quickstart: Query data in
  Amazon S3](studio-sqlexplorer-athena-s3-quickstart.md "studio-sqlexplorer-athena-s3-quickstart.md")
- [SQL extension features and usage](sagemaker-sql-extension-features.md "sagemaker-sql-extension-features.md")
- [Configure network access between Studio and data sources (for administrators)](sagemaker-sql-extension-networking.md "sagemaker-sql-extension-networking.md")
- [SQL extension data source
  connections](sagemaker-sql-extension-datasources-connection.md "sagemaker-sql-extension-datasources-connection.md")
- [Frequently asked questions](sagemaker-sql-extension-faqs.md "sagemaker-sql-extension-faqs.md")
- [Connection parameters](sagemaker-sql-extension-connection-properties.md "sagemaker-sql-extension-connection-properties.md")

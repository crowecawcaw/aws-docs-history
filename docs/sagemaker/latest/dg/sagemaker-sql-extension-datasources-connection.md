# SQL extension data source

connections

Before using the SQL extension in JupyterLab notebooks, administrators or users must
create AWS Glue connections to their data sources. The SQL extension allows connecting to data
sources such as Amazon Redshift Amazon Athena, or Snowflake.

To set up the connections, administrators must first ensure their network configuration
allows communication between Studio and the data sources and then grant the necessary IAM
permissions to allow Studio to access the data sources. For information on how
administrators can set up the networking, see [Configure network access between Studio and data sources (for administrators)](sagemaker-sql-extension-networking.md "sagemaker-sql-extension-networking.md"). For information on what policies must be setup, see [Set up the IAM
permissions to access the data sources (for administrators)](sagemaker-sql-extension-datasources-connection-permissions.md "sagemaker-sql-extension-datasources-connection-permissions.md"). Once the connections
are set up, data scientists can use the SQL extension in their JupyterLab notebooks to browse
and query the connected data sources.

###### Note

We recommend storing your database access credentials as a secret in Secrets Manager. To learn
about how to create secrets for storing Amazon Redshift or Snowflake access credentials, see [Create secrets for database
access credentials in Secrets Manager](sagemaker-sql-extension-glue-connection-secrets.md "sagemaker-sql-extension-glue-connection-secrets.md").

This section explains how to set up an AWS Glue connection and lists the IAM permissions
required for the Studio JupyterLab application to access the data through the connection.

###### Note

[Amazon SageMaker Assets](sm-assets.md "sm-assets.md") integrates [Amazon DataZone](../../../datazone/latest/userguide/what-is-datazone.md "../../../datazone/latest/userguide/what-is-datazone.md") with Studio.
It includes a SageMaker AI blueprint for administrators to create Studio environments from
Amazon DataZone projects within an Amazon DataZone domain.

Users of a JupyterLab application launched from a Studio domain created with the
blueprint can automatically access AWS Glue connections to data assets in their Amazon DataZone
catalog when using the SQL extension. This allows querying those data sources without
manually setting up connections.

###### Topics

- [Create secrets for database
  access credentials in Secrets Manager](sagemaker-sql-extension-glue-connection-secrets.md "sagemaker-sql-extension-glue-connection-secrets.md")
- [Create AWS Glue connections
  (for administrators)](sagemaker-sql-extension-datasources-glue-connection.md "sagemaker-sql-extension-datasources-glue-connection.md")
- [Create
  user-defined AWS Glue connections](sagemaker-sql-extension-datasources-glue-connection-user-defined.md "sagemaker-sql-extension-datasources-glue-connection-user-defined.md")
- [Set up the IAM
  permissions to access the data sources (for administrators)](sagemaker-sql-extension-datasources-connection-permissions.md "sagemaker-sql-extension-datasources-connection-permissions.md")

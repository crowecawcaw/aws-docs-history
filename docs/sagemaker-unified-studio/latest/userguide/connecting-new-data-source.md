# Connecting to a new data source

## Domain and project VPC

configuration

Data sources Amazon DocumentDB, Amazon Redshift, Aurora MySQL, Aurora PostgreSQL, Azure SQL,
PostgreSQL, Oracle, Microsoft SQL Server require your project to be configured with a VPC
[Step 1](../adminguide/configure-vpc-networking-iam-based-domains.md "../adminguide/configure-vpc-networking-iam-based-domains.md"), [Step 2](../adminguide/update-individual-projects-vpc.md "../adminguide/update-individual-projects-vpc.md"). You might need to contact administrator to complete that
configuration.

###### To connect to a new data source

1. In the navigation pane, choose **Connections**.
2. Choose **Create connection**.
3. Select the connection type in the gallery that opens.
4. For **Name** enter a descriptive name for your connection.
5. Configure the connection parameters based on your selected connection type.
   1. You can select [SSL connection](#ssl-connection "#ssl-connection")
      for supported data sources.

6. Configure the authentication details. You can either enter
   **Username** and **Password** directly in the
   connection details, or use a secret in AWS Secrets Manager that stores the
   credentials. You might need to contact your administrator to create a new secret for the
   connection.
7. Choose **Create connection**.
8. If all validations pass, a new connection will be created.
   Your connection will appear under **Data section** in the navigation
   pane. In that section, select **Connections** to see the list of all
   available connections. From there you can see connection details such as
   **Name**, **Connection type**, and
   **Authorization mode**. You can also check the connection status.

## SSL connection

You can configure SSL connection for Amazon DocumentDB, Amazon Redshift, Aurora MySQL, Aurora
PostgreSQL, Azure SQL, Microsoft SQL Server, MySQL, Oracle, and PostgreSQL connection
types.

SSL connection enables encrypted communication between Amazon SageMaker Unified Studio
and your data source. When enabled, all data transmitted between your notebooks and the
database is encrypted using SSL/TLS protocols, protecting sensitive information in
transit. This setting is recommended for production environments and required when
connecting to databases that enforce SSL connections.

To enable SSL connection select Enforce SSL checkbox when configuring connection
properties.

###### Note

Enabling SSL may slightly increase connection latency due to the encryption
overhead.

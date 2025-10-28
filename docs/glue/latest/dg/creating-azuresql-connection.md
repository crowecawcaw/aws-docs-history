# Creating a Azure SQL connection

To connect to Azure SQL from AWS Glue, you will need to create and store your Azure SQL credentials
in a AWS Secrets Manager secret, then associate that secret with a Azure SQL AWS Glue connection.

###### To configure a connection to Azure SQL:

1.  In AWS Secrets Manager, create a secret using your Azure SQL credentials.
    To create a secret in Secrets Manager, follow the tutorial available in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the AWS Secrets Manager documentation.
    After creating the secret, keep the Secret name, `secretName` for the next step.
    - When selecting **Key/value pairs**, create a pair for
      the key `user` with the value `azuresqlUsername`.
    - When selecting **Key/value pairs**, create a pair for
      the key `password` with the value `azuresqlPassword`.

2.  In the AWS Glue console, create a connection by following the steps in [Adding an AWS Glue connection](console-connections.md "console-connections.md").
    After creating the connection, keep the connection name, `connectionName`, for future use in AWS Glue.
    - When selecting a **Connection type**, select Azure SQL.
    - When providing **Azure SQL URL**, provide a JDBC endpoint URL.

    The URL must be in the following format:
    `jdbc:sqlserver://`databaseServerName`:`databasePort`;databaseName=`azuresqlDBname`;`.

    AWS Glue requires the following URL properties:

        + `databaseName` – A default database in Azure SQL to connect to.

    For more information about JDBC URLs for Azure SQL Managed Instances, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?view=azuresqldb-mi-current "https://learn.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?view=azuresqldb-mi-current").
    - When selecting an **AWS Secret**, provide `secretName`.

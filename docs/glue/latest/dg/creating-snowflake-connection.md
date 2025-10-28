# Creating a Snowflake connection

###### Note

Unified connections (connection v2) standardize all connections to use `USERNAME`, `PASSWORD` keys for
basic auth credentials.
You can still create a v1 connection via API with secrets containing `sfUser`, `sfPassword`.

When adding a **Data source - Snowflake** node in AWS Glue Studio, you can choose
an existing AWS Glue Snowflake connection or create a new connection. You must choose a `SNOWFLAKE`
type connection and not a `JDBC` type connection configured to connect to Snowflake. Follow the following
procedure to create a AWS Glue Snowflake connection:

###### To create a Snowflake connection

1. In Snowflake, generate a user, `snowflakeUser` and password, `snowflakePassword`.
2. Determine which Snowflake warehouse this user will interact with,
   `snowflakeWarehouse`. Either set it as the `DEFAULT_WAREHOUSE` for
   `snowflakeUser` in Snowflake or remember it for the next step.
3. In AWS Secrets Manager, create a secret using your Snowflake credentials.
   To create a secret in Secrets Manager, follow the tutorial available in
   [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md#create_secret_cli "../../../secretsmanager/latest/userguide/create_secret.md#create_secret_cli") in the AWS Secrets Manager documentation.
   After creating the secret, keep the Secret name, `secretName` for the next step.
   - When selecting **Key/value pairs**, create a pair for
     `snowflakeUser` with the key `sfUser`.
   - When selecting **Key/value pairs**, create a pair for
     `snowflakePassword` with the key `sfPassword`.
   - When selecting **Key/value pairs**, create a pair for
     `snowflakeWarehouse` with the key `sfWarehouse`. This
     is not needed if a default is set in Snowflake.

4. In the AWS Glue Data Catalog, create a connection by following the steps in [Adding an AWS Glue connection](console-connections.md "console-connections.md"). After creating
   the connection, keep the connection name, `connectionName`, for the next
   step.
   - When selecting a **Connection type**, select Snowflake.
   - When selecting **Snowflake URL**, provide the hostname of your Snowflake
     instance. The URL will use a hostname in the form
     ``account_identifier`.snowflakecomputing.com`.
   - When selecting an **AWS Secret**, provide
     `secretName`.

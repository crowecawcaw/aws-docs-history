# Secrets

Retrieve the secret (username, password, other connection-related metadata)
for the connection using the following property.

```

snowflake_connection: Connection = proj.connection("project.snowflake")
secret = snowflake_connection.secret

```

Secrets can be a dictionary containing credentials or a single string
depending on the connection type.

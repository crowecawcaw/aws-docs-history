# Connections

You can retrieve a list of connections for a project, or you can retrieve a single
connection by providing its name.

```

proj_connections: List[Connection] = proj.connections
proj_redshift_conn = proj.connection("my_redshift_connection_name")

```

Each `Connection` object has several properties that can provide
information about the connection.

```

proj_redshift_conn.name
proj_redshift_conn.id
proj_redshift_conn.physical_endpoints[0].host
proj_redshift_conn.iam_role

```

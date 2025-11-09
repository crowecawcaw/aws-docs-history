# Transportable databases function reference

The `transport.import_from_server` function transports a PostgreSQL
database by importing it from a source DB instance to a destination DB instance. It does
this by using a physical database connection transport mechanism.

Before starting the transport, this function verifies that the source and the destination
DB instances are the same version and are compatible for the migration. It also confirms that the destination
DB instance has enough space for the source.

**Syntax**

```
transport.import_from_server(
   host text,
   port int,
   username text,
   password text,
   database text,
   local_password text,
   dry_run bool
)
```

**Return Value**

None.

**Parameters**

You can find descriptions of the `transport.import_from_server` function
parameters in the following table.

| Parameter        | Description                                                                                                                                                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `host`           | The endpoint of the source DB instance.                                                                                                                                                                                                                                              |
| `port`           | An integer representing the port of the source DB instance.<br>PostgreSQL DB instances often use port 5432.                                                                                                                                                                          |
| `username`       | The user of the source DB instance. This user must be a member of<br>the `rds_superuser` role.                                                                                                                                                                                       |
| `password`       | The user password of the source DB instance.                                                                                                                                                                                                                                         |
| `database`       | The name of the database in the source DB instance to<br>transport.                                                                                                                                                                                                                  |
| `local_password` | The local password of the current user for the destination DB<br>instance. This user must be a member of the<br>`rds_superuser` role.                                                                                                                                                |
| `dry_run`        | An optional Boolean value specifying whether to perform a dry<br>run. The default is `false`, which means the transport<br>proceeds.To confirm compatibility between the source and<br>destination DB instances without performing the actual transport, set<br>`dry_run` to `true`. |

**Example**

For an example, see [Transporting a PostgreSQL database to the destination from the source](PostgreSQL.TransportableDB.md "PostgreSQL.TransportableDB.md").

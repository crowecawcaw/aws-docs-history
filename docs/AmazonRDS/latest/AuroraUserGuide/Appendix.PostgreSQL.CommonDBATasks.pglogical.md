# Parameter reference

for the pglogical extension

In the table you can find parameters associated with the `pglogical` extension.
Parameters such as `pglogical.conflict_log_level` and
`pglogical.conflict_resolution` are used to handle update conflicts. Conflicts
can emerge when changes are made locally to the same tables that are subscribed to changes
from the publisher. Conflicts can also occur during various scenarios, such as two-way
replication or when multiple subscribers are replicating from the same publisher. For more
information, see [PostgreSQL bi-directional replication using pglogical](https://aws.amazon.com/blogs/database/postgresql-bi-directional-replication-using-pglogical/ "https://aws.amazon.com/blogs/database/postgresql-bi-directional-replication-using-pglogical/").

| Parameter                          | Description                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pglogical.batch_inserts            | Batch inserts if possible. Not set by default. Change to '1' to turn on,<br>'0' to turn off.                                                                                                                                                                                                                                                |
| pglogical.conflict_log_level       | Sets the log level to use for logging resolved conflicts. Supported string<br>values are debug5, debug4, debug3, debug2, debug1, info, notice, warning, error,<br>log, fatal, panic.                                                                                                                                                        |
| pglogical.conflict_resolution      | Sets method to use to resolve conflicts when conflicts are resolvable.<br>Supported string values are error, apply_remote, keep_local, last_update_wins,<br>first_update_wins.                                                                                                                                                              |
| pglogical.extra_connection_options | Connection options to add to all peer node connections.                                                                                                                                                                                                                                                                                     |
| pglogical.synchronous_commit       | pglogical specific synchronous commit value                                                                                                                                                                                                                                                                                                 |
| pglogical.use_spi                  | Use SPI (server programming interface) instead of low-level API to apply<br>changes. Set to '1' to turn on, '0' to turn off. For more information about SPI, see<br>[Server Programming<br>Interface](https://www.postgresql.org/docs/current/spi.html "https://www.postgresql.org/docs/current/spi.html") in the PostgreSQL documentation. |

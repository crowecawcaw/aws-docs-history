

# Parameter reference for the pglogical extension
<a name="Appendix.PostgreSQL.CommonDBATasks.pglogical.reference"></a>

In the table you can find parameters associated with the `pglogical` extension. Parameters such as `pglogical.conflict_log_level` and `pglogical.conflict_resolution` are used to handle update conflicts. Conflicts can emerge when changes are made locally to the same tables that are subscribed to changes from the publisher. Conflicts can also occur during various scenarios, such as two-way replication or when multiple subscribers are replicating from the same publisher. For more information, see [ PostgreSQL bi-directional replication using pglogical](https://aws.amazon.com/blogs/database/postgresql-bi-directional-replication-using-pglogical/). 


| Parameter | Description | 
| --- | --- | 
| pglogical.batch\_inserts | Batch inserts if possible. Not set by default. Change to '1' to turn on, '0' to turn off. | 
| pglogical.conflict\_log\_level | Sets the log level to use for logging resolved conflicts. Supported string values are debug5, debug4, debug3, debug2, debug1, info, notice, warning, error, log, fatal, panic. | 
| pglogical.conflict\_resolution | Sets method to use to resolve conflicts when conflicts are resolvable. Supported string values are error, apply\_remote, keep\_local, last\_update\_wins, first\_update\_wins. | 
| pglogical.extra\_connection\_options | Connection options to add to all peer node connections. | 
| pglogical.synchronous\_commit | pglogical specific synchronous commit value | 
| pglogical.use\_spi | Use SPI (server programming interface) instead of low-level API to apply changes. Set to '1' to turn on, '0' to turn off. For more information about SPI, see [Server Programming Interface](https://www.postgresql.org/docs/current/spi.html) in the PostgreSQL documentation.  | 
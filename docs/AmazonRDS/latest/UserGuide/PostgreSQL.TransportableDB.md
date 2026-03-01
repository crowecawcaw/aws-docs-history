# Transporting a PostgreSQL database to the destination from the source

After you complete the process described in [Setting up to transport a PostgreSQL database](PostgreSQL.TransportableDB.md "PostgreSQL.TransportableDB.md"), you can start the transport. To
do so, run the `transport.import_from_server` function on the destination
DB instance. In the syntax following you can find the function parameters.

```
SELECT transport.import_from_server(
   '`source-db-instance-endpoint`',
    `source-db-instance-port`,
   '`source-db-instance-user`',
   '`source-user-password`',
   '`source-database-name`',
   '`destination-user-password`',
   false);

```

The `false` value shown in the example tells the function that this is not a dry run. To
test your transport setup, you can specify `true` for the `dry_run` option when
you call the function, as shown following:

```
`postgres=>` `SELECT transport.import_from_server(
 'docs-lab-source-db.666666666666`aws-region`.rds.amazonaws.com', 5432,
 'postgres', '********', 'labdb', '******', true);`
`INFO: Starting dry-run of import of database "labdb".
INFO: Created connections to remote database (took 0.03 seconds).
INFO: Checked remote cluster compatibility (took 0.05 seconds).
INFO: Dry-run complete (took 0.08 seconds total).
 import_from_server
--------------------

(1 row)`
```

The INFO lines are output because the `pg_transport.timing` parameter
is set to its default value, `true`. Set the `dry_run` to `false`
when you run the command and the source database is imported to the destination, as shown
following:

```
INFO:  Starting import of database "labdb".
INFO:  Created connections to remote database        (took 0.02 seconds).
INFO:  Marked remote database as read only           (took 0.13 seconds).
INFO:  Checked remote cluster compatibility          (took 0.03 seconds).
INFO:  Signaled creation of PITR blackout window     (took 2.01 seconds).
INFO:  Applied remote database schema pre-data       (took 0.50 seconds).
INFO:  Created connections to local cluster          (took 0.01 seconds).
INFO:  Locked down destination database              (took 0.00 seconds).
INFO:  Completed transfer of database files          (took 0.24 seconds).
INFO:  Completed clean up                            (took 1.02 seconds).
INFO:  Physical transport complete              (took 3.97 seconds total).
import_from_server
--------------------
(1 row)
```

This function requires that you provide database user passwords. Thus, we recommend
that you change the passwords of the user roles you used after transport is complete.
Or, you can use SQL bind variables to create temporary user roles. Use these temporary
roles for the transport and then discard the roles afterwards.

If your transport isn't successful, you might see an error message similar to the following:

```
pg_transport.num_workers=8 25% of files transported failed to download file data
```

The "failed to download file data" error message indicates that the number of worker processes isn't set correctly
for the size of the database. You might need to increase or decrease the value set for `pg_transport.num_workers`.
Each failure reports the percentage of completion, so you can see the impact of your changes. For example, changing the setting
from 8 to 4 in one case resulted in the following:

```
pg_transport.num_workers=4 75% of files transported failed to download file data
```

Keep in mind that the `max_worker_processes` parameter is also
taken into account during the transport process. In other words, you might need to modify both `pg_transport.num_workers`
and `max_worker_processes` to successfully transport the database. The example shown finally worked when
the `pg_transport.num_workers` was set to 2:

```
pg_transport.num_workers=2 100% of files transported
```

For more information about the `transport.import_from_server` function and its
parameters, see [Transportable databases function reference](PostgreSQL.TransportableDB.transport.md "PostgreSQL.TransportableDB.transport.md").

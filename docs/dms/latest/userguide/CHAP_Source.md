# Using Microsoft Azure Database for PostgreSQL flexible server as a source for AWS DMS

With AWS DMS, you can use Microsoft Azure Database for PostgreSQL flexible server as a source in much the same way as you do PostgreSQL.

For information about versions of Microsoft Azure Database for PostgreSQL flexible server that AWS DMS supports as a source, see
[Sources for AWS DMS](CHAP_Introduction.md "CHAP_Introduction.md").

## Setting up Microsoft Azure for PostgreSQL flexible server for logical replication and decoding

You can use logical replication and decoding features in Microsoft Azure Database for
PostgreSQL flexible server during database migration.

For logical decoding, DMS uses either the `test_decoding` or `pglogical`
plugin. If the `pglogical`
plugin is available on a source PostgreSQL database, DMS creates a replication slot using
`pglogical`,
otherwise the `test_decoding` plugin is used.

To configure your Microsoft Azure for PostgreSQL flexible server as a source endpoint
for DMS, perform the following steps:

1. Open the Server Parameters page on the portal.
2. Set the `wal_level` server parameter to `LOGICAL`.
3. If you want to use the `pglogical` extension, set the
   `shared_preload_libraries` and `azure.extensions` parameters to
   `pglogical`.
4. Set the `max_replication_slots` parameter to the maximum number of
   DMS tasks that you plan to run concurrently. In Microsoft Azure, the default value for
   this parameter is 10. This parameter's maximum value depends on the available memory
   of your PostgreSQL instance, allowing for between 2 and 8 replication slots per GB of memory.
5. Set the `max_wal_senders` parameter to a value greater than 1.
   The `max_wal_senders` parameter sets the number of concurrent tasks that can
   run. The default value is 10.
6. Set the `max_worker_processes` parameter value to at least 16.
   Otherwise, you may see errors such as the following:

```
WARNING: out of background worker slots.
```

7. Save the changes. Restart the server to apply the changes.
8. Confirm that your PostgreSQL instance allows network traffic from your
   connecting resource.
9. Grant an existing user replication permissions, or create a new user with
   replication permissions, using the following commands.
   - Grant an existing user replication permissions using the following command:

   ```
   ALTER USER `<existing_user>` WITH REPLICATION;
   ```

   - Create a new user with replication permissions using the following command:

   ```
   CREATE USER aws_dms_user PASSWORD 'aws_dms_user_password';
   GRANT azure_pg_admin to aws_dms_user;
   ALTER ROLE aws_dms_user REPLICATION LOGIN;
   ```

For more information about logical replication with PostgreSQL, see the following topics:

- [Enabling change data capture (CDC)
  using logical replication](CHAP_Source.md#CHAP_Source.PostgreSQL.Security "CHAP_Source.md#CHAP_Source.PostgreSQL.Security")
- [Using native CDC start points to set up
  a CDC load of a PostgreSQL source](CHAP_Source.md#CHAP_Source.PostgreSQL.v10 "CHAP_Source.md#CHAP_Source.PostgreSQL.v10")
- [Logical replication and logical decoding in Azure Database for PostgreSQL - Flexible Server](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-logical "https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-logical") in the
  [Azure Database for PostgreSQL documentation](https://learn.microsoft.com/en-us/azure/postgresql/ "https://learn.microsoft.com/en-us/azure/postgresql/").

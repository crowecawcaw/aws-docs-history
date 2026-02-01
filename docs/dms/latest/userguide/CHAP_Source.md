# Using Google Cloud for PostgreSQL as a source

for AWS DMS

With AWS DMS, you can use Google Cloud for PostgreSQL as a source in much the same way as you do self-managed PostgreSQL databases.

For information about versions of GCP PostgreSQL that AWS DMS supports as a source, see
[Sources for AWS DMS](CHAP_Introduction.md "CHAP_Introduction.md").

For more information, see [Using a PostgreSQL database as an AWS DMS
source](CHAP_Source.md "CHAP_Source.md").

## Set up Google Cloud for PostgreSQL for logical replication and decoding

You can use logical replication and decoding features in Google Cloud SQL for PostgreSQL during database migration.

For logical decoding, DMS uses one of the following plugins:

- `test_decoding`
- `pglogical`

If the `pglogical` plugin is available on a source PostgreSQL database, DMS creates a replication slot using `pglogical`,
otherwise the `test_decoding` plugin is used.

Note the following about using logical decoding with AWS DMS:

1. With Google Cloud SQL for PostgreSQL, enable logical decoding by
   setting the `cloudsql.logical_decoding` flag to `on`.
2. To enable `pglogical`, set the `cloudsql.enable_pglogical`
   flag to `on`, and restart the database.
3. To use logical decoding features, you create a PostgreSQL user with the
   `REPLICATION` attribute. When you are using the `pglogical`
   extension, the user must have the `cloudsqlsuperuser` role. To create
   a user with the `cloudsqlsuperuser` role, do the following:

```
CREATE USER new_aws_dms_user WITH REPLICATION
IN ROLE cloudsqlsuperuser LOGIN PASSWORD 'new_aws_dms_user_password';
```

To set this attribue on an existing user, do the following:

```
ALTER USER existing_user WITH REPLICATION;
```

4. Set the `max_replication_slots` parameter to the maximum number of
   DMS tasks that you plan to run concurrently. In Google Cloud SQL, the default value for
   this parameter is 10. This parameter's maximum value depends on the available memory
   of your PostgreSQL instance, allowing for between 2 and 8 replication slots per GB of memory.

For more information about logical replication with PostgreSQL, see the following topics:

- [Enabling change data capture (CDC)
  using logical replication](CHAP_Source.md#CHAP_Source.PostgreSQL.Security "CHAP_Source.md#CHAP_Source.PostgreSQL.Security")
- [Using native CDC start points to set up
  a CDC load of a PostgreSQL source](CHAP_Source.md#CHAP_Source.PostgreSQL.v10 "CHAP_Source.md#CHAP_Source.PostgreSQL.v10")
- [Set up logical replication and decoding](https://cloud.google.com/sql/docs/postgres/replication/configure-logical-replication "https://cloud.google.com/sql/docs/postgres/replication/configure-logical-replication") in the
  [Cloud SQL for PostgreSQL documentation](https://cloud.google.com/sql/docs/postgres "https://cloud.google.com/sql/docs/postgres").

#

Tablespaces for RDS for PostgreSQL

RDS for PostgreSQL supports tablespaces for compatibility. Because all storage is on a
single logical volume, you can't use tablespaces for I/O splitting or
isolation. Our benchmarks and experience indicate that a single logical volume is
the best setup for most use cases.

To create and use tablespaces with your RDS for PostgreSQL DB instance requires the
`rds_superuser` role. Your RDS for PostgreSQL DB instance's main user
account (default name, `postgres`) is a member of this role. For more
information, see [Understanding PostgreSQL roles and
permissions](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md").

If you specify a file name when you create a tablespace, the path prefix is
`/rdsdbdata/db/base/tablespace`. The following example places
tablespace files in `/rdsdbdata/db/base/tablespace/data`. This example
assumes that a `dbadmin` user (role) exists and that it's been
granted the `rds_superuser` role needed to work with tablespaces.

```
`postgres=>` `CREATE TABLESPACE act_data
 OWNER dbadmin
 LOCATION '/data';`
`CREATE TABLESPACE`
```

To learn more about PostgreSQL tablespaces, see [Tablespaces](https://www.postgresql.org/docs/current/manage-ag-tablespaces.html "https://www.postgresql.org/docs/current/manage-ag-tablespaces.html") in the PostgreSQL documentation.

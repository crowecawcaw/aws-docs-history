# RDS version numbers in RDS for MySQL

RDS version numbers use either the
``major`.`minor`.`patch``
or the
``major`.`minor`.`patch.YYYYMMDD``
naming scheme. Amazon RDS Extended Support versions use the `minor-RDS.YYYYMMDD`
minor version naming scheme.

An RDS patch version includes important bug fixes added to a minor version after its
release. An RDS date version (`YYYYMMDD`) is a security patch.
A security patch doesn't include any fixes that might change the engine's behavior. For
information about RDS Extended Support version numbering, see [Amazon RDS Extended Support version naming](extended-support-versions.md#extended-support-naming "extended-support-versions.md#extended-support-naming").

You can find out the RDS version number of your RDS for MySQL database with the following
SQL query:

```
`mysql>` `select mysql.rds_version();`
```

For example, querying an RDS for MySQL 8.0.34 database returns the following
output:

```
`+---------------------+
| mysql.rds_version() |
+---------------------+
| 8.0.34.R2.20231201 |
+---------------------+
1 row in set (0.01 sec)`
```

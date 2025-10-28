# RDS version numbers in RDS for MariaDB

RDS version numbers use either the
``major`.`minor`.`patch``
or the
``major`.`minor`.`patch.YYYYMMDD``
naming scheme. An RDS patch version includes important bug fixes added to a minor
version after its release. An RDS date version (`YYMMDD`) is a
security patch. A security patch doesn't include any fixes that might change the
engine's behavior.

To identify the Amazon RDS version number of your database, you must first create the
`rds_tools` extension by using the following command:

```
CREATE EXTENSION rds_tools;
```

You can find out the RDS version number of your RDS for MariaDB database with the
following SQL query:

```
`mysql>` `select mysql.rds_version();`
```

For example, querying an RDS for MariaDB 10.6.14 database returns the following
output:

````
`+---------------------+
| mysql.rds_version() | +---------------------+
| 10.6.14.R2.20231201 | +---------------------+ 1 row in set (0.01 sec)` ```
````

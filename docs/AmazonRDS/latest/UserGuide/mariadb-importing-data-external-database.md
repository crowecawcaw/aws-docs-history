# Importing data from an external

MariaDB database to an Amazon RDS for MariaDB DB instance

You can import data from an existing MariaDB database to an RDS for MariaDB DB instance. You do
so by copying the database with [mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html "https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html") or [mariadb-dump](https://mariadb.com/kb/en/mariadb-dump/ "https://mariadb.com/kb/en/mariadb-dump/"), and piping the
database directly into the RDS for MariaDB DB instance. The `mysqldump` or
`mariadb-dump` command line utility is commonly used to make backups and
transfer data from one MariaDB server to another. It's included with MariaDB client
software.

Starting with MariaDB 11.0.1, you must use `mariadb-dump` instead of
`mysqldump`.

A typical `mysqldump` command to move data from an external database to an
Amazon RDS DB instance looks similar to the following example. Replace values with your own
information. For MariaDB 11.0.1 and higher versions, replace `mysqldump` with
`mariadb-dump`.

```
mysqldump -u `local_user` \
    --databases `database_name` \
    --single-transaction \
    --compress \
    --order-by-primary  \
    --routines=0 \
    --triggers=0 \
    --events=0 \
    -p`local_password` | mariadb -u `RDS_user` \
        --port=`port_number` \
        --host=`host_name` \
        -p`RDS_password`
```

###### Important

Make sure not to leave a space between the `-p` option and the entered
password.

As a security best practice, specify credentials other than the prompts shown in this
example.

Make sure that you're aware of the following recommendations and considerations:

- Exclude the following schemas from the dump file:

      + `sys`
      + `performance_schema`
      + `information_schema`

  The `mysqldump` and `mariadb-dump` utility excludes these
  schemas by default.

- If you need to migrate users and privileges, consider using a tool that generates
  the data control language (DCL) for recreating them, such as the [pt-show-grants](https://www.percona.com/doc/percona-toolkit/LATEST/pt-show-grants.html "https://www.percona.com/doc/percona-toolkit/LATEST/pt-show-grants.html") utility.
- To perform the import, make sure the user doing so has access to the DB instance.
  For more information, see [Controlling access with security
  groups](Overview.md "Overview.md").
  The parameters used are as follows:

- `-u `local_user``– Use to specify a
user name. In the first usage of this parameter, specify the name of a user account
on the local MariaDB database that you identify with the`--databases`
  parameter.
- `--databases `database_name`` – Use to
  specify the name of the database on the local MariaDB instance that you want to
  import into Amazon RDS.
- `--single-transaction` – Use to ensure that all of the data
  loaded from the local database is consistent with a single point in time. If there
  are other processes changing the data while `mysqldump` or
  `mariadb-dump` is reading it, using this parameter helps maintain
  data integrity.
- `--compress` – Use to reduce network bandwidth consumption by
  compressing the data from the local database before sending it to Amazon RDS.
- `--order-by-primary` – Use to reduce load time by sorting each
  table's data by its primary key.
- `--routines` – Use if routines such as stored procedures or
  functions exist in the database that you are copying. Set the parameter to
  `0`, which excludes the routines during the import process. Then
  later manually recreate the routines in the Amazon RDS database.
- `--triggers` – Use if triggers exist in the database that you
  are copying. Set the parameter to `0`, which excludes the triggers during
  the import process. Then later manually recreate the triggers in the Amazon RDS
  database.
- `--events` – Use if events exist in the database that you are
  copying. Set the parameter to `0`, which excludes the events during the
  import process. Then later manually recreate the events in the Amazon RDS database.
- `-p`local_password``– Use to specify a
password. In the first usage of this parameter, specify the password for the user
account that you identify with the first`-u` parameter.
- `-u `RDS_user``– Use to specify a user
name. In the second usage of this parameter, specify the name of a user account on
the default database for the MariaDB DB instance that you identify with the`--host` parameter.
- `--port `port_number`` – Use to specify
  the port for your MariaDB DB instance. By default, this is 3306 unless you changed
  the value when creating the DB instance.
- `--host `host_name``– Use to specify
the Domain Name System (DNS) name from the Amazon RDS DB instance endpoint, for example,`myinstance.123456789012.us-east-1.rds.amazonaws.com`. You can find
  the endpoint value in the DB instance details in the Amazon RDS console.
- `-p`RDS_password``– Use to specify a
 password. In the second usage of this parameter, you specify the password for the
 user account identified by the second`-u`parameter.
Make sure to create any stored procedures, triggers, functions, or events manually in your
 Amazon RDS database. If you have any of these objects in the database that you are copying, then
 exclude them when you run`mysqldump`or`mariadb-dump`. To do so,
 include the following parameters with your `mysqldump`or
`mariadb-dump` command:

- `--routines=0`
- `--triggers=0`
- `--events=0`
  **Example**

The following example copies the `world` sample database on the local host to
an RDS for MariaDB DB instance. Replace values with your own information.

For Linux, macOS, or Unix:

```
sudo mariadb-dump -u `local_user` \
    --databases `world` \
    --single-transaction \
    --compress \
    --order-by-primary  \
    --routines=0 \
    --triggers=0 \
    --events=0 \
    -p`local_password` | mariadb -u `rds_user` \
        --port=`3306` \
        --host=`my_instance.123456789012.us-east-1.rds.amazonaws.com` \
        -p`RDS_password`
```

For Windows:

Run the following command in a command prompt that has been opened by right-clicking
**Command Prompt** on the Windows programs menu and choosing
**Run as administrator**. Replace values with your own information.

```
mariadb-dump -u `local_user` ^
    --databases `world` ^
    --single-transaction ^
    --compress ^
    --order-by-primary  ^
    --routines=0 ^
    --triggers=0 ^
    --events=0 ^
    -p`local_password` | mariadb -u `RDS_user` ^
        --port=`3306` ^
        --host=`my_instance.123456789012.us-east-1.rds.amazonaws.com` ^
        -p`RDS_password`
```

###### Note

As a security best practice, specify credentials other than the prompts shown in the
example.

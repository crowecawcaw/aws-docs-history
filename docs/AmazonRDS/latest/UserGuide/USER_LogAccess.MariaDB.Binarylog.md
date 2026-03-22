# Accessing MariaDB binary logs

You can use the mysqlbinlog utility to download binary logs in text format from MariaDB DB
instances. The binary log is downloaded to your local computer. For more information
about using the mysqlbinlog utility, go to [Using
mysqlbinlog](http://mariadb.com/kb/en/mariadb/using-mysqlbinlog/ "http://mariadb.com/kb/en/mariadb/using-mysqlbinlog/") in the MariaDB documentation.

To run the mysqlbinlog utility against an Amazon RDS instance, use the following options:

- Specify the `--read-from-remote-server` option.
- `--host`: Specify the DNS name from the endpoint of the instance.
- `--port`: Specify the port used by the instance.
- `--user`: Specify a MariaDB user that has been granted the
  replication slave permission.
- `--password`: Specify the password for the user, or
  omit a password value so the utility prompts you for a password.
- `--result-file`: Specify the local file that receives
  the output.
- Specify the names of one or more binary log files. To get a list of the available logs,
  use the SQL command SHOW BINARY LOGS.
  For more information about mysqlbinlog options, go to [mysqlbinlog options](http://mariadb.com/kb/en/mariadb/mysqlbinlog-options/ "http://mariadb.com/kb/en/mariadb/mysqlbinlog-options/") in the MariaDB documentation.

The following is an example:

For Linux, macOS, or Unix:

```
mysqlbinlog \
    --read-from-remote-server \
    --host=mariadbinstance1.1234abcd.region.rds.amazonaws.com \
    --port=3306  \
    --user ReplUser \
    --password <password> \
    --result-file=/tmp/binlog.txt
```

For Windows:

```
mysqlbinlog ^
    --read-from-remote-server ^
    --host=mariadbinstance1.1234abcd.region.rds.amazonaws.com ^
    --port=3306  ^
    --user ReplUser ^
    --password <password> ^
    --result-file=/tmp/binlog.txt
```

Amazon RDS normally purges a binary log as soon as possible. However, the binary log must still
be available on the instance to be accessed by mysqlbinlog. To specify the number of
hours for RDS to retain binary logs, use the `mysql.rds_set_configuration`
stored procedure. Specify a period with enough time for you to download the logs. After
you set the retention period, monitor storage usage for the DB instance to ensure that
the retained binary logs don't take up too much storage.

The following example sets the retention period to 1 day.

```
call mysql.rds_set_configuration('binlog retention hours', 24);
```

To display the current setting, use the `mysql.rds_show_configuration` stored
procedure.

```
call mysql.rds_show_configuration;
```

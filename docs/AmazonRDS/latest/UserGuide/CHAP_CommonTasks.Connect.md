# Finding the connection information for an Amazon RDS DB instance

The connection information for a DB instance includes its endpoint, port, and a valid
database user, such as the master user. For example, for a MySQL DB instance, suppose
that the endpoint value is `mydb.123456789012.us-east-1.rds.amazonaws.com`.
In this case, the port value is `3306`, and the database user is
`admin`. Given this information, you specify the following values in a
connection string:

- For host or host name or DNS name, specify
  `mydb.123456789012.us-east-1.rds.amazonaws.com`.
- For port, specify `3306`.
- For user, specify `admin`.
  The endpoint is unique for each DB instance, and the values of the port and user can
  vary. The following list shows the most common port for each DB engine:

- Db2 – 50000
- MariaDB – 3306
- Microsoft SQL Server – 1433
- MySQL – 3306
- Oracle – 1521
- PostgreSQL – 5432
  To connect to a DB instance, use any client for a DB engine. For example, you might
  use the mysql utility to connect to a MariaDB or MySQL DB instance. You might use
  Microsoft SQL Server Management Studio to connect to a SQL Server DB instance. You might
  use Oracle SQL Developer to connect to an Oracle DB instance. Similarly, you might use
  the psql command line utility to connect to a PostgreSQL DB instance.

To find the connection information for a DB instance, use the AWS Management Console. You can also
use the AWS Command Line Interface (AWS CLI) [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") command or the RDS API [DescribeDBInstances](../APIReference/API_DescribeDBInstances.md "../APIReference/API_DescribeDBInstances.md")
operation.

###### To find the connection information for a DB instance in the AWS Management Console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases** to display a list of your DB instances.
3. Choose the name of the DB instance to display its details.
4. On the **Connectivity & security** tab, copy the endpoint.
   Also, note the port number. You need both the endpoint and the port number
   to connect to the DB instance.

![The endpoint and port of a DB instance](images/endpoint-port.png) 5. If you need to find the master user name, choose the
**Configuration** tab and view the **Master
username** value.
To find the connection information for a DB instance by using the AWS CLI, call the
[describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") command. In the call, query for the DB
instance ID, endpoint, port, and master user name.

For Linux, macOS, or Unix:

```
aws rds describe-db-instances \
  --query "*[].[DBInstanceIdentifier,Endpoint.Address,Endpoint.Port,MasterUsername]"
```

For Windows:

```
aws rds describe-db-instances ^
  --query "*[].[DBInstanceIdentifier,Endpoint.Address,Endpoint.Port,MasterUsername]"
```

Your output should be similar to the following.

```
[
    [
        "mydb",
        "mydb.123456789012.us-east-1.rds.amazonaws.com",
        3306,
        "admin"
    ],
    [
        "myoracledb",
        "myoracledb.123456789012.us-east-1.rds.amazonaws.com",
        1521,
        "dbadmin"
    ],
    [
        "mypostgresqldb",
        "mypostgresqldb.123456789012.us-east-1.rds.amazonaws.com",
        5432,
        "postgresadmin"
    ]
]
```

To find the connection information for a DB instance by using the Amazon RDS API, call
the [DescribeDBInstances](../APIReference/API_DescribeDBInstances.md "../APIReference/API_DescribeDBInstances.md") operation. In the output, find the values for
the endpoint address, endpoint port, and master user name.

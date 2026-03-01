# Finding the endpoint of your Amazon RDS for Db2 DB instance

Each Amazon RDS DB instance has an endpoint, and each endpoint has the DNS name and port number
for the DB instance. To connect to your Amazon RDS for Db2 DB instance with a SQL client
application, you need the DNS name and port number for your DB instance.

You can find the endpoint for a DB instance by using the AWS Management Console or the AWS CLI.

###### To find the endpoint of an RDS for Db2 DB instance

1.  Sign in to the AWS Management Console and open the Amazon RDS console at
    [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2.  In the upper-right corner of the console, choose the AWS Region of your
    DB instance.
3.  Find the DNS name and port number for your RDS for Db2 DB Instance.

        1. Choose **Databases** to display a list of your DB
         instances.
        2. Choose the RDS for Db2 DB instance name to display the instance
         details.
        3. On the **Connectivity & security** tab, copy
         the endpoint. Also, note the port number. You need both the endpoint
         and the port number to connect to the DB instance.



        ![The Connectivity and security tab for a DB instance that shows the endpoint and port.](images/db2-connectivity-security.png)

    To find the endpoint of an RDS for Db2 DB instance, run the [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") command. In the following
    example, replace `database-1` with the name of your DB
    instance.

For Linux, macOS, or Unix:

```
aws rds describe-db-instances \
    --db-instance-identifier `database-1` \
    --query 'DBInstances[].{DBInstanceIdentifier:DBInstanceIdentifier,DBName:DBName,Endpoint:Endpoint}' \
    --output json
```

For Windows:

```
aws rds describe-db-instances ^
    --db-instance-identifier `database-1` ^
    --query 'DBInstances[].{DBInstanceIdentifier:DBInstanceIdentifier,DBName:DBName,Endpoint:Endpoint}' ^
    --output json
```

This command produces output similar to the following example. The
`Address` line in the output contains the DNS name.

```
[
    {
        "DBInstanceIdentifier": "database-1",
        "DBName": "DB2DB",
        "Endpoint": {
            "Address": "database-1.123456789012.us-east-2.amazonaws.com",
            "Port": 50000,
            "HostedZoneId": "Z2OC4A7DETW6VH"
        }
    }
]
```



# Connecting to a DB instance running the PostgreSQL database engine
<a name="USER_ConnectToPostgreSQLInstance"></a>

After Amazon RDS provisions your DB instance, you can use any standard SQL client application to connect to the instance. Before you can connect, the DB instance must be available and accessible. Whether you can connect to the instance from outside the VPC depends on how you created the Amazon RDS DB instance: 
+ If you created your DB instance as *public*, devices and Amazon EC2 instances outside the VPC can connect to your database. 
+ If you created your DB instance as *private*, only Amazon EC2 instances and devices inside the Amazon VPC can connect to your database. 

To check whether your DB instance is public or private, use the AWS Management Console to view the **Connectivity & security** tab for your instance. Under **Security**, you can find the "Publicly accessible" value, with No for private, Yes for public. 

To learn more about different Amazon RDS and Amazon VPC configurations and how they affect accessibility, see [Scenarios for accessing a DB instance in a VPC](USER_VPC.Scenarios.md). 

**Contents**
+ [Installing the psql client](#install-psql)
+ [Finding the connection information for an RDS for PostgreSQL DB instance](#postgresql-endpoint)
+ [Using pgAdmin to connect to a RDS for PostgreSQL DB instance](USER_ConnectToPostgreSQLInstance.pgAdmin.md)
+ [Using psql to connect to your RDS for PostgreSQL DB instance](USER_ConnectToPostgreSQLInstance.psql.md)
+ [Connecting to RDS for PostgreSQL with the Amazon Web Services (AWS) JDBC Driver](PostgreSQL.Connecting.JDBCDriver.md)
+ [Connecting to RDS for PostgreSQL with the Amazon Web Services (AWS) Python Driver](PostgreSQL.Connecting.PythonDriver.md)
+ [Troubleshooting connections to your RDS for PostgreSQL instance](USER_ConnectToPostgreSQLInstance.Troubleshooting.md)
  + [Error – FATAL: database {{name}} does not exist](USER_ConnectToPostgreSQLInstance.Troubleshooting.md#USER_ConnectToPostgreSQLInstance.Troubleshooting-DBname)
  + [Error – Could not connect to server: Connection timed out](USER_ConnectToPostgreSQLInstance.Troubleshooting.md#USER_ConnectToPostgreSQLInstance.Troubleshooting-timeout)
  + [Errors with security group access rules](USER_ConnectToPostgreSQLInstance.Troubleshooting.md#USER_ConnectToPostgreSQLInstance.Troubleshooting-AccessRules)

## Installing the psql client
<a name="install-psql"></a>

To connect to your DB instance from an EC2 instance, you can install a PostgreSQL client on the EC2 instance. To install the latest version of the psql client on Amazon Linux 2023, run the following command: 

```
sudo dnf install postgresql{{<version number>}}
```

To install the latest version of the psql client on Amazon Linux 2, run the following command:

```
sudo yum install -y postgresql
```

To install the latest version of the psql client on Ubuntu, run the following command:

```
sudo apt install -y postgresql-client
```

## Finding the connection information for an RDS for PostgreSQL DB instance
<a name="postgresql-endpoint"></a>

If the DB instance is available and accessible, you can connect by providing the following information to the SQL client application: 
+ The DB instance endpoint, which serves as the host name (DNS name) for the instance.
+ The port on which the DB instance is listening. For PostgreSQL, the default port is 5432. 
+ The user name and password for the DB instance. The default 'master username' for PostgreSQL is `postgres`. 
+ The name and password of the database (DB name). 

 You can obtain these details by using the AWS Management Console, the AWS CLI [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) command, or the Amazon RDS API [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) operation. 

**To find the endpoint, port number, and DB name using the AWS Management Console**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Open the RDS console and then choose **Databases** to display a list of your DB instances. 

1. Choose the PostgreSQL DB instance name to display its details. 

1. On the **Connectivity & security** tab, copy the endpoint. Also, note the port number. You need both the endpoint and the port number to connect to the DB instance.   
![Obtain the endpoint from the RDS Console.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/PostgreSQL-endpoint.png)

1. On the **Configuration** tab, note the DB name. If you created a database when you created the RDS for PostgreSQL instance, you see the name listed under DB name. If you didn't create a database, the DB name displays a dash (‐).  
![Obtain the DB name from the RDS Console.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/PostgreSQL-db-name.png)

Following are two ways to connect to a PostgreSQL DB instance. The first example uses pgAdmin, a popular open-source administration and development tool for PostgreSQL. The second example uses psql, a command line utility that is part of a PostgreSQL installation. 
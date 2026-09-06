

# Connecting to your Microsoft SQL Server DB instance
<a name="USER_ConnectToMicrosoftSQLServerInstance"></a>

After Amazon RDS provisions your DB instance, you can use any standard SQL client application to connect to the DB instance. In this topic, you connect to your DB instance by using either Microsoft SQL Server Management Studio (SSMS) or SQL Workbench/J.

For an example that walks you through the process of creating and connecting to a sample DB instance, see [Creating and connecting to a Microsoft SQL Server DB instance](CHAP_GettingStarted.CreatingConnecting.SQLServer.md). 

## Before you connect
<a name="sqlserver-before-connect"></a>

Before you can connect to your DB instance, it has to be available and accessible.

1. Make sure that its status is `available`. You can check this on the details page for your instance in the AWS Management Console or by using the [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) AWS CLI command.  
![Check that the DB instance is available.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/sqlserver-available.png)

1. Make sure that it is accessible to your source. Depending on your scenario, it might not need to be publicly accessible. For more information, see [Amazon VPC and Amazon RDS](USER_VPC.md).

1. Make sure that the inbound rules of your VPC security group allow access to your DB instance. For more information, see [Can't connect to Amazon RDS DB instance](CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting).

## Finding the DB instance endpoint and port number
<a name="sqlserver-endpoint"></a>

You need both the endpoint and the port number to connect to the DB instance.

**To find the endpoint and port**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the Amazon RDS console, choose the AWS Region of your DB instance.

1. Find the Domain Name System (DNS) name (endpoint) and port number for your DB instance:

   1. Open the RDS console and choose **Databases** to display a list of your DB instances.

   1. Choose the SQL Server DB instance name to display its details.

   1. On the **Connectivity & security** tab, copy the endpoint.  
![Locate DB instance endpoint and port.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/SQL-Connect-Endpoint.png)

   1. Note the port number.
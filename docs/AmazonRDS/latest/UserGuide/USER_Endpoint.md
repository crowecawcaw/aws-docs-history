

# Finding the endpoint of your RDS for Oracle DB instance

Each Amazon RDS DB instance has an endpoint, and each endpoint has the DNS name and port number for the DB instance. To connect to your DB instance using a SQL client application, you need the DNS name and port number for your DB instance. 

You can find the endpoint for a DB instance using the Amazon RDS console or the AWS CLI.

**Note**  
If your DB instance runs Oracle Database Enterprise Edition, it also has a Primary Endpoint. The Primary Endpoint is a DNS name that points to the current primary DB instance in a replica configuration. When you connect through it, you don't need to change your connection string after a switchover. For more information, see [Using the Primary Endpoint for Amazon RDS for Oracle](oracle-primary-endpoint.md).

## Console
<a name="USER_Endpoint.Console"></a>

**To find the endpoint using the console**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the console, choose the AWS Region of your DB instance. 

1. Find the DNS name and port number for your DB instance. 

   1. Choose **Databases** to display a list of your DB instances. 

   1. Choose the Oracle DB instance name to display the instance details. 

   1. On the **Connectivity & security** tab, for **Connect using**, choose **Endpoints**.

   1. Under **Endpoint & port**, copy the endpoint. Also, note the port number. You need both the endpoint and the port number to connect to the DB instance.  
![The Endpoint and Port of a DB instance under Endpoint & port on the Connectivity & security tab.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/OracleConnect1.png)

## AWS CLI
<a name="USER_Endpoint.CLI"></a>

To find the endpoint of an Oracle DB instance by using the AWS CLI, call the [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) command. 

**Example To find the endpoint using the AWS CLI**  

```sql
1. aws rds describe-db-instances
```
Search for `Endpoint` in the output to find the DNS name and port number for your DB instance. The `Address` line in the output contains the DNS name. The following is an example of the JSON endpoint output.  

```
"Endpoint": {
    "HostedZoneId": "Z1PVIF0B656C1W",
    "Port": 1521,
    "Address": "myinstance.123456789012.us-west-2.rds.amazonaws.com"
},
```

**Note**  
The output might contain information for multiple DB instances.
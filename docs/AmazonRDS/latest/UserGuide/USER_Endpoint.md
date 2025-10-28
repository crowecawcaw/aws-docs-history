# Finding the endpoint of your RDS for Oracle DB instance

Each Amazon RDS DB instance has an endpoint, and each endpoint has the DNS name and port number
for the DB instance. To connect to your DB instance using a SQL client application, you need the DNS
name and port number for your DB instance.

You can find the endpoint for a DB instance using the Amazon RDS console or the AWS CLI.

###### Note

If you are using Kerberos authentication, see [Connecting to Oracle with Kerberos authentication](oracle-kerberos-connecting.md "oracle-kerberos-connecting.md").

## Console

###### To find the endpoint using the console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the upper-right corner of the console, choose the AWS Region of your DB instance.
3. Find the DNS name and port number for your DB instance.
   1. Choose **Databases** to display a list of your DB instances.
   2. Choose the Oracle DB instance name to display the instance details.
   3. On the **Connectivity & security** tab, copy the endpoint. Also, note
      the port number. You need both the endpoint and the port number to connect to the DB
      instance.

   ![Locate DB instance endpoint and port](images/OracleConnect1.png)

## AWS CLI

To find the endpoint of an Oracle DB instance by using the AWS CLI, call the [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") command.

###### Example To find the endpoint using the AWS CLI

```
aws rds describe-db-instances
```

Search for `Endpoint` in the output to find the DNS name and port number for your DB
instance. The `Address` line in the output contains the DNS name. The following is an example
of the JSON endpoint output.

```
"Endpoint": {
    "HostedZoneId": "Z1PVIF0B656C1W",
    "Port": 3306,
    "Address": "myinstance.123456789012.us-west-2.rds.amazonaws.com"
},
```

###### Note

The output might contain information for multiple DB instances.

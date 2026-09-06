

# Using the Amazon RDS console to retrieve connection information
<a name="connecting-console"></a>

Before you can connect to your Amazon RDS DB instance, you need to gather the connection details, including the endpoint, port, and other required settings. The AWS Management Console provides an easy way to retrieve this information. The following sections walk you through how to find the endpoint and port, along with additional connection details, so you can connect to your DB instance.

**Topics**
+ [Locating the endpoint and port](#connecting-endpoint)
+ [Locating other connection details](#connecting-details)
+ [Next steps](#connecting-console-next-steps)

## Locating the endpoint and port
<a name="connecting-endpoint"></a>

To connect to your DB instance, you first need the instance endpoint and port number. Follow these steps to find them in the AWS Management Console.

**To locate the endpoint and port**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the left navigation pane, choose **Databases**.

1. Select the DB instance that you want to connect to from the list of available instances.

1. In the **Connectivity & security** section, find the **Endpoint** and **Port** settings.
   + The **Endpoint** is the DNS address for your DB instance. You use this as part of the connection string when you connect with a database client.
   + The **Port** is the communication port used by the database engine (for example, 3306 for MySQL or 5432 for PostgreSQL).

     The following image shows these fields in the console:  
![Endpoint and port section showing database endpoint URL and port 3306.](http://docs.aws.amazon.com/AmazonRDS/latest/gettingstartedguide/images/endpoint-port.png)

These are the primary details that you need to initiate a connection to your DB instance.

## Locating other connection details
<a name="connecting-details"></a>

In addition to the endpoint and port, you might need other connection details depending on your specific use case and database engine. You can find the following additional information in the **Connectivity & security** section and in the **Configuration** section.
+ **VPC and subnet group** – The Virtual Private Cloud (VPC) and subnet group details help you understand the network environment your DB instance resides in. If you need to configure security groups or modify network settings, this information is essential.
+ **Security groups** – Security groups control access to your DB instance. You can view the security groups associated with your DB instance here, which help you make sure that the appropriate inbound and outbound rules are in place for a successful connection.
+ **DB parameter group** – If you need to adjust database settings, such as timeouts or query limits, the DB parameter group associated with your instance provides the necessary configuration options.

## Next steps
<a name="connecting-console-next-steps"></a>

Once you have the required connection details, including the instance endpoint and port, you can use them to connect to the DB instance.

**Next step: **[Connecting to an Amazon RDS DB instance using a database client](connecting-client.md)
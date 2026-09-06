

# Connect using the Amazon DocumentDB ODBC driver
<a name="connect-odbc"></a>

The ODBC driver for Amazon DocumentDB provides an SQL-relational interface for developers and enables connectivity from BI tools such as Power BI Desktop and Microsoft Excel.

For more detailed information, refer to the [Amazon DocumentDB ODBC Driver documentation on GitHub](https://github.com/aws/amazon-documentdb-jdbc-driver/blob/develop/src/markdown/index.md).

**Topics**
+ [Getting started](#connect-odbc-get-started)
+ [Setting up the Amazon DocumentDB ODBC driver in Windows](connect-odbc-setup-windows.md)
+ [Connect to Amazon DocumentDB from Microsoft Excel](connect-odbc-excel.md)
+ [Connect to Amazon DocumentDB from Microsoft Power BI Desktop](connect-odbc-power-bi.md)
+ [Automatic schema generation](connect-odbc-schema.md)
+ [SQL support and limitations](connect-odbc-sql-support.md)
+ [Troubleshooting](connect-odbc-troubleshooting.md)

## Getting started
<a name="connect-odbc-get-started"></a>

**Step 1. Create Amazon DocumentDB Clusters**  
If you don't already have an Amazon DocumentDB cluster, there are a number of ways to get started.  
Amazon DocumentDB is a Virtual Private Cloud (VPC)-only service. If you are connecting from a local machine outside the cluster's VPC, you need to create an SSH connection to an Amazon EC2 instance. For more information, see [Connect using Amazon EC2](connect-ec2.md). For more information on SSH tunneling, see [Using an SSH Tunnel to Connect to Amazon DocumentDB](https://github.com/aws/amazon-documentdb-odbc-driver/blob/develop/src/markdown/setup/setup.md#using-an-ssh-tunnel-to-connect-to-amazon-documentdb).

**Step 2. JRE or JDK Installation**  
Depending on your BI application, you may need to ensure a 64-bit JRE or JDK installation version 8 or later installed on your computer. You can download the Java SE Runtime Environment 8 [here](https://www.oracle.com/ca-en/java/technologies/downloads/#java8).

**Step 3. Download the Amazon DocumentDB ODBC Driver**  
Download the Amazon DocumentDB ODBC driver [here](https://github.com/aws/amazon-documentdb-odbc-driver/releases). Choose the proper installer (for example, documentdb-odbc-1.0.0.msi). Follow the installation guide.

**Step 4. Using an SSH Tunnel to Connect to Amazon DocumentDB**  
Amazon DocumentDB clusters are deployed within an Amazon Virtual Private Cloud (Amazon VPC). They can be accessed directly by Amazon EC2 instances or other AWS services that are deployed in the same Amazon VPC. Additionally, Amazon DocumentDB can be accessed by Amazon EC2 instances or other AWS services in different VPCs in the same AWS Region or other Regions via VPC peering.  
However, suppose that your use case requires that you (or your application) access your Amazon DocumentDB resources from outside the cluster's VPC. This will be the case for most users not running their application on a VM in the same VPC as the Amazon DocumentDB cluster. When connecting from outside the VPC, you can use SSH tunneling (also known as port forwarding) to access your Amazon DocumentDB resources.  
To create an SSH tunnel, you need an Amazon EC2 instance running in the same Amazon VPC as your Amazon DocumentDB cluster. You can either use an existing EC2 instance in the same VPC as your cluster or create one. You can set up an SSH tunnel to the Amazon DocumentDB cluster `sample-cluster.node.us-east-1.docdb.amazonaws.com` by running the following command on your local computer:  

```
ssh -i "ec2Access.pem" -L 27017:sample-cluster.node.us-east-1.docdb.amazonaws.com:27017 ubuntu@ec2-34-229-221-164.compute-1.amazonaws.com -N
```
The `-L` flag is used for forwarding a local port. This is a prerequisite for connecting to any BI tool running on a client outside your VPC. Once you run the step above you can move on to the next steps for the BI tool of your choice.  
For further information on SSH tunneling, refer to the documentation on [Using an SSH Tunnel to Connect to Amazon DocumentDB](https://github.com/aws/amazon-documentdb-odbc-driver/blob/develop/src/markdown/setup/setup.md#using-an-ssh-tunnel-to-connect-to-amazon-documentdb).
# Connect using the Amazon DocumentDB JDBC driver

The JDBC driver for Amazon DocumentDB provides an SQL-relational interface for developers and
enables connectivity from BI tools such as Tableau and DbVisualizer.

For more detailed information, refer to the [Amazon DocumentDB JDBC Driver documentation on GitHub](https://github.com/aws/amazon-documentdb-jdbc-driver/blob/develop/src/markdown/index.md "https://github.com/aws/amazon-documentdb-jdbc-driver/blob/develop/src/markdown/index.md").

###### Topics

- [Getting started](#connect-jdbc-gettingstarted "#connect-jdbc-gettingstarted")
- [Connect to Amazon DocumentDB from Tableau Desktop](connect-jdbc-tableau.md "connect-jdbc-tableau.md")
- [Connect to Amazon DocumentDB from DbVisualizer](connect-jdbc-DbVisualizer.md "connect-jdbc-DbVisualizer.md")
- [JDBC automatic schema generation](connect-jdbc-autoschemagen.md "connect-jdbc-autoschemagen.md")
- [SQL support and limitations](connect-jdbc-sqlandlimits.md "connect-jdbc-sqlandlimits.md")
- [Troubleshooting](connect-jdbc-troubleshooting.md "connect-jdbc-troubleshooting.md")

## Getting started

**Step 1. Create Amazon DocumentDB Cluster**

If you do not have an Amazon DocumentDB cluster created, then create one using the
instructions in the [Getting Started](get-started-guide.md "get-started-guide.md") section of the Amazon DocumentDB Developer Guide.

###### Note

Amazon DocumentDB is a Virtual Private Cloud (VPC) only service. If you are
connecting from a local machine, outside the cluster's VPC, you will
need to create an SSH connection to an Amazon EC2 instance. In this
case, launch your cluster using the instructions in [Connect with EC2](connect-ec2.md "connect-ec2.md"). See [Using an SSH Tunnel to Connect to Amazon DocumentDB](https://github.com/aws/amazon-documentdb-jdbc-driver/blob/develop/src/markdown/setup/setup.md#using-an-ssh-tunnel-to-connect-to-amazon-documentdb "https://github.com/aws/amazon-documentdb-jdbc-driver/blob/develop/src/markdown/setup/setup.md#using-an-ssh-tunnel-to-connect-to-amazon-documentdb") for more
information on SSH tunneling and when you might need it.

**Step 2. JRE or JDK Installation**

Depending on your BI application, you may need to ensure a 64-bit JRE or
JDK installation version 8 or later is installed on your computer. You can
download the Java SE Runtime Environment 8 [here](https://www.oracle.com/ca-en/java/technologies/javase-jre8-downloads.html "https://www.oracle.com/ca-en/java/technologies/javase-jre8-downloads.html").

**Step 3. Download the DocumentDB JDBC Driver**

Download the DocumentDB JDBC driver from [here](https://github.com/aws/amazon-documentdb-jdbc-driver/releases "https://github.com/aws/amazon-documentdb-jdbc-driver/releases"). The driver is packaged as a single JAR file (e.g.
documentdb-jdbc-1.0.0-all.jar).

**Step 4. Using an SSH Tunnel to Connect to Amazon DocumentDB**

Amazon DocumentDB (with MongoDB compatibility) clusters are deployed within an
Amazon Virtual Private Cloud (Amazon VPC). They can be accessed directly by
Amazon EC2 instances or other AWS services that are deployed in the same
Amazon VPC. Additionally, Amazon DocumentDB can be accessed by EC2a instances or other
AWS services in different VPCs in the same AWS Region or other Regions via
VPC peering.

You can use SSH tunneling (also known as port forwarding) to access your
Amazon DocumentDB resources, from outside the cluster's VPC. This will be the case for
most users not running their application on a VM in the same VPC as the
DocumentDB cluster.

To create an SSH tunnel, you need an Amazon EC2 instance running in the
same Amazon VPC as your Amazon DocumentDB cluster. You can either use an existing EC2
instance in the same VPC as your cluster or create one. You can set up an
SSH tunnel to the Amazon DocumentDB cluster
`sample-cluster.node.us-east-1.docdb.amazonaws.com` by
running the following command on your local computer.

```
ssh -i "ec2Access.pem" -L 27017:sample-cluster.node.us-east-1.docdb.amazonaws.com:27017 ubuntu@ec2-34-229-221-164.compute-1.amazonaws.com -N

```

The -L flag is used for forwarding a local port. This is a prerequisite
for connecting to any BI tool running on a client outside your VPC. Once you
run the step above you can move on to the next steps for the BI tool of your
choice.

For further information on SSH tunneling , please refer to the
documentation on [Using an SSH tunnel to connect to Amazon DocumentDB](https://github.com/aws/amazon-documentdb-jdbc-driver/blob/develop/src/markdown/setup/setup.md#using-an-ssh-tunnel-to-connect-to-amazon-documentdb "https://github.com/aws/amazon-documentdb-jdbc-driver/blob/develop/src/markdown/setup/setup.md#using-an-ssh-tunnel-to-connect-to-amazon-documentdb ").

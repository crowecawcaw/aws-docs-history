

# Prerequisites for using Amazon Redshift to analyze messages
<a name="firehose-redshift-prereqs"></a>

Before you begin, make sure you've addressed all prerequisites in [Prerequisites for subscribing Firehose delivery streams to Amazon SNS topics](prereqs-kinesis-data-firehose.md). You also need a SQL query tool. Amazon Redshift doesn't provide or install any SQL client tools or libraries. You must install one that you can use to access the Amazon Redshift clusters that contain your Amazon SNS notifications. This tutorial uses [SQL Workbench/J](http://www.sql-workbench.net/), a free, DBMS-independent, cross-platform SQL query tool.

**To install SQL Workbench/J**

1. Review the [SQL Workbench/J software license](http://www.sql-workbench.net/manual/license.html#license-restrictions).

1. From the [SQL Workbench/J website](http://www.sql-workbench.net/), download the appropriate package for your operating system.

1. Use the [Installing and starting SQL Workbench/J](http://www.sql-workbench.net/manual/install.html) instructions to install SQL Workbench/J.

1. From [Configure a JDBC Connection](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html), download an Amazon Redshift JDBC driver. This driver lets SQL Workbench/J connect to your cluster.
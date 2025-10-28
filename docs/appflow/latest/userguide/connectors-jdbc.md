# JDBC connector for Amazon AppFlow

Java Database Connectivity (JDBC) is a Java API that developers use to connect
their applications to relational databases. JDBC is included in the Java Standard
Edition from Oracle. You can use Amazon AppFlow to transfer data from a databases by a creating a
JDBC connection. Then you can transfer the data to other databases, AWS services,
or other supported applications.

## Amazon AppFlow support for JDBC

Amazon AppFlow supports JDBC as follows.

**Supported as a data source?**

Yes. You can use Amazon AppFlow to transfer data from databases through the JDBC
API.

**Supported as a data destination?**

Yes. You can use Amazon AppFlow to transfer data to databases through the JDBC
API.

## Before you begin

Before you can use Amazon AppFlow to transfer data to or from a database using the
JDBC connector, you must have one or more databases that support and are enabled
for JDBC API access. For more information about installing the JDBC driver, see the
JDBC documentation for your version of Java, such as the [JDBC Getting
Started](https://docs.oracle.com/javase/tutorial/jdbc/basics/gettingstarted.html "https://docs.oracle.com/javase/tutorial/jdbc/basics/gettingstarted.html") documentation in the Oracle Java SE 8 Documentation.

From your database settings, note the endpoint name and port. You provide these values,
along with your database user name and password, to Amazon AppFlow when you connect to your
database.

## Connecting Amazon AppFlow to a database through

JDBC

To connect Amazon AppFlow to your database through the JDBC API, provide details from
your database settings so that Amazon AppFlow can access your data.

###### To connect through JDBC

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **JDBC**.
4. Choose **Create connection**.
5. In the **Connect to JDBC** window, enter the following
   information:
   - **driver** — Choose **mysql** or
     **postgresql** depending on the type of database where you want to
     connect.
   - **hostname** — The hostname associated with the database that
     you're connecting to.
   - **port** — The port that is activated for JDBC
     access to the database.
   - **username** — The user name for a user that has access to the
     database.
   - **password** — The password associated with the user
     name.
   - **database** — The name of the database where you want to
     connect.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses JDBC as the data source, you can select this connection.

## Transferring data to or from a database through

JDBC

To transfer data to or from a database through the JDBC API, create an Amazon AppFlow flow, and
choose JDBC as the data source or the data destination. For the steps to create a
flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the a flow that uses the JDBC connector as a source or
destination, you set the following options:

- **connection** – The Amazon AppFlow JDBC connection that you
  created.
- **API Version** – The supported JDBC API
  version.
- **object** – Typically, the database schema.
- **subobject** – Typically, the name of the database table that you
  want to transfer data to or from.

## Supported destinations

When you create a flow that uses JDBC as the data source, you can set the
destination to any of the following connectors:

- [Amazon Lookout for Metrics](lookout.md "lookout.md")
- [Amazon Redshift](redshift.md "redshift.md")
- [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md "connectors-amazon-rds-postgres-sql.md")
- [Amazon S3](s3.md "s3.md")
- JDBC
- [Marketo](marketo.md "marketo.md")
- [Salesforce](salesforce.md "salesforce.md")
- [SAP OData](sapodata.md "sapodata.md")
- [Snowflake](snowflake.md "snowflake.md")
- [Upsolver](upsolver.md "upsolver.md")
- [Zendesk](zendesk.md "zendesk.md")

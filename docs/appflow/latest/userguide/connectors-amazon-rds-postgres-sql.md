# Amazon RDS for PostgreSQL connector for Amazon AppFlow

Amazon Relational Database Service (Amazon RDS) helps you set up and manage relational databases in the AWS Cloud. With
Amazon RDS for PostgreSQL, you can set up Amazon RDS databases that run the PostgreSQL open source database
system. If you use Amazon RDS for PostgreSQL, you can also use Amazon AppFlow to populate your databases with
data that you transfer from certain AWS services or other supported applications.

## Amazon AppFlow support for Amazon RDS for PostgreSQL

Amazon AppFlow supports Amazon RDS for PostgreSQL as follows.

**Supported as a data source?**
No. You can't use Amazon AppFlow to transfer data from Amazon RDS for PostgreSQL.

**Supported as a data destination?**
Yes. You can use Amazon AppFlow to transfer data to Amazon RDS for PostgreSQL.

## Before you begin

Before you can use Amazon AppFlow to transfer data to Amazon RDS for PostgreSQL, you must have one or more
Amazon RDS databases where you've set the engine to PostreSQL. For the steps to create such a
database, see [Creating a PostgreSQL DB instance](../../../AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.md#CHAP_GettingStarted.Creating.PostgreSQL "../../../AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.md#CHAP_GettingStarted.Creating.PostgreSQL") in the _Amazon RDS User Guide_.

From your database settings, note the endpoint name and port. You provide these values,
along with your database user name and password, to Amazon AppFlow when you connect to your
database.

## Connecting Amazon AppFlow to your Amazon RDS for PostgreSQL database

To connect Amazon AppFlow to your Amazon RDS for PostgreSQL database, provide details from your database
settings.

###### To connect to Amazon RDS for PostgreSQL

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Amazon RDS for PostgreSQL**.
4. Choose **Create connection**.
5. In the **Connect to Amazon RDS for PostgreSQL** window, enter the following
   information:
   - **driver** – Choose **postgresql**.
   - **hostname** – The endpoint name of the destination DB
     instance.
   - **port** – The DB instance port number.
   - **username** – The name of the DB instance master user.
   - **password** – The DB instance password.
   - **database** – The DB instance name.

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
**Connections** table. When you create a flow that uses Amazon RDS for PostgreSQL as
the data destination, you can select this connection.

## Transferring data to Amazon RDS for PostgreSQL with a flow

To transfer data to Amazon RDS for PostgreSQL, create an Amazon AppFlow flow, and choose Amazon RDS for PostgreSQL
as the data destination. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

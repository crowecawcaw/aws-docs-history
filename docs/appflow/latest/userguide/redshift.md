# Amazon Redshift connector for Amazon AppFlow

Amazon Redshift is a data warehouse service in AWS. If you use Amazon Redshift, you can also use Amazon AppFlow to
transfer data from supported sources into your Amazon Redshift databases. When you connect Amazon AppFlow to Amazon Redshift
with the recommended settings, Amazon AppFlow transfers your data with the Amazon Redshift Data API.

For more information about Amazon Redshift, see the [Amazon Redshift Management Guide](../../../redshift/latest/mgmt/welcome.md "../../../redshift/latest/mgmt/welcome.md").

## Amazon AppFlow support for Amazon Redshift

Amazon AppFlow supports Amazon Redshift as follows.

**Supported as a data source?**
No. You can't use Amazon AppFlow to transfer data from Amazon Redshift.

**Supported as a data destination?**
Yes. You can use Amazon AppFlow to transfer data to Amazon Redshift.

## Before you begin

Before you can use Amazon AppFlow to transfer data to Amazon Redshift, you must meet these requirements:

- You have an Amazon Redshift database. If you are new to Amazon Redshift, see the [Amazon Redshift Getting Started Guide](../../../redshift/latest/gsg.md "../../../redshift/latest/gsg.md") to learn about
  basic concepts and tasks. You specify your database in the Amazon Redshift connection settings in
  Amazon AppFlow.
- **Recommended**: You have an AWS Identity and Access Management (IAM) role that
  authorizes Amazon AppFlow to access your database through the Amazon Redshift Data API. You need this role to
  configure an Amazon Redshift connection with the recommended settings. For more information, and for
  the polices that you attach to this role, see [Allow Amazon AppFlow to access Amazon Redshift databases with the Data API](security_iam_service-role-policies.md#access-redshift "security_iam_service-role-policies.md#access-redshift").
- You have an Amazon S3 bucket that Amazon AppFlow can use as an intermediate destination when it
  transfers data to Amazon Redshift. You specify this bucket in the connection settings. For the steps
  to create a bucket, see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in
  the _Amazon S3 User Guide_.
- You have an IAM role that grants Amazon Redshift read-only access to Amazon S3. You specify this
  role in the connection settings, and you associate it with your Amazon Redshift cluster. For more
  information, and for the polices that you attach to this role, see [Allow Amazon Redshift to access your Amazon AppFlow data in Amazon S3](security_iam_service-role-policies.md#redshift-access-s3 "security_iam_service-role-policies.md#redshift-access-s3").
- In IAM, you’re authorized with the required pass role permissions below.

### Required pass role permissions

Before you can create an Amazon Redshift connection, you must have certain IAM permissions
assigned to you as an AWS user. These permissions must allow you pass IAM roles to
Amazon AppFlow and Amazon Redshift, as shown by the following example IAM policy:

Before you use this example policy, replace the variable elements with the required
values:

- `account-id` – Your AWS account ID.
- `appflow-redshift-access-role-name` – The name of the role that
  authorizes Amazon AppFlow to access your Amazon Redshift database.
- `region` – The code of the AWS Region where you use Amazon AppFlow. For
  example, the code for the US East (N. Virginia) Region is `us-east-1`. For the
  AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md") in the
  _AWS General Reference_.
- `redshift-s3-access-role-name` – The name of the role that grants
  Amazon Redshift read-only access to Amazon S3.

## Connecting Amazon AppFlow to your Amazon Redshift database

To connect Amazon AppFlow to your Amazon Redshift database, provide the required database
details, S3 bucket, and IAM roles. If you haven't yet created the required resources, see
the preceding section, [Before you begin](#redshift-prereqs "#redshift-prereqs").

###### To create an Amazon Redshift connection

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Amazon Redshift**.
4. Choose **Create connection**.
5. For **Data warehouse type**, choose whether to connect to
   **Amazon Redshift Serverless** or an **Amazon Redshift cluster**.
6. If you chose to connect to Amazon Redshift Serverless, enter the following information:
   - **Workgroup name** – The name of your Amazon Redshift
     workgroup.
   - **Database name** – The name of the Amazon Redshift database that
     stores the data that you transfer with Amazon AppFlow.
   - **Bucket details** – The Amazon S3 bucket where Amazon AppFlow writes
     your data as an intermediate destination. Amazon Redshift gets your data from this bucket.
   - **IAM role for Amazon S3 access** – The IAM role that
     authorizes Amazon Redshift to get and decrypt the data from the S3 bucket.
   - **IAM role for Amazon Redshift Data API access** — The IAM role
     that authorizes Amazon AppFlow to access your database through the Amazon Redshift Data API.

###### Note

After you create a connection to Amazon Redshift Serverless, you must also grant the required
access privileges to your database user. For more information, see [Granting access privileges to the database user (required for Amazon Redshift Serverless)](#grant-access "#grant-access"). 7. If you chose to connect to an Amazon Redshift cluster, do one of the following:

    * **Recommended:** Choose **Data API**
     to connect through the Amazon Redshift Data API. This option is recommended because Amazon AppFlow can
     use the Data API to connect to public and private Amazon Redshift clusters. Enter the following
     information:




    	+ **Cluster identifier** – The unique identifier of your
    	 Amazon Redshift cluster.
    	+ **Database name** – The name of the Amazon Redshift database that
    	 stores the data that you transfer with Amazon AppFlow.
    	+ **Bucket details** – The Amazon S3 bucket where Amazon AppFlow
    	 writes your data as an intermediate destination. Amazon Redshift gets your data from this
    	 bucket.
    	+ **IAM role for Amazon S3 access** – The IAM role that
    	 authorizes Amazon Redshift to get and decrypt the data from the S3 bucket.
    	+ **IAM role for Amazon Redshift Data API access** – The IAM
    	 role that authorizes Amazon AppFlow to access your database through the Amazon Redshift Data
    	 API.
    	+ **Amazon Redshift database user name** – The user name that you
    	 use to authenticate with your Amazon Redshift database.
    * **Not recommended:** Choose **JDBC
     URL** to connect through a Java Database Connectivity (JDBC) URL. For
     information about the settings for this option, see the [Guidance for connections that use JDBC URLs](#jdbc-guidance "#jdbc-guidance") section that follows.###### Warning

We don't recommend that you choose the **JDBC URL** option because
Amazon AppFlow can't use JDBC URLs to connect to private Amazon Redshift clusters. Amazon AppFlow will discontinue
support for JDBC URLs in the near future. We strongly recommend that you configure your
connection with the Data API instead. 8. Optionally, under **Data encryption**, choose **Customize
encryption settings (advanced)** if you want to encrypt your data with a customer
managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 9. For **Connection name**, enter a name for your connection. 10. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow that uses Amazon Redshift
as the data destination, you can select this connection.

## Granting access privileges to the database user (required for Amazon Redshift Serverless)

After you connect Amazon AppFlow to Amazon Redshift Serverless, you must also grant access privileges to a
database user account. Amazon AppFlow uses this account to access your database. Until you grant the
access privileges, Amazon AppFlow can't access your database, and it can't run flows that transfer
data to the database.

###### Note

This action is necessary only if you created a connection to Amazon Redshift Serverless. It isn't
necessary if you chose to connect to an Amazon Redshift cluster.

You grant the access privileges to a database user that Amazon Redshift creates for you when you
create the connection in Amazon AppFlow. Amazon Redshift names this user
`IAMR:`data-api-access-role``. In that name,
 `data-api-access-role` is the name of the IAM role that authorizes access to
your database through the Amazon Redshift Data API. If you already created the connection in the Amazon AppFlow
console, you provided that role for the **IAM role for Amazon Redshift Data API
access** field.

Amazon Redshift maps this role to the database user. After you grant the access privileges, Amazon Redshift
allows the database user to access your data with the permissions that you assigned to the
role.

###### To grant the access privileges

- Use your SQL client to run the Amazon Redshift SQL command `GRANT`.

For example, you can run this command to permit the user to access all of the tables
in a specific schema:

```
GRANT ALL ON ALL TABLES IN SCHEMA `schema-name` TO "IAMR:`data-api-access-role`"
```

To apply the privileges more restrictively, you can run this command to permit the
user to access a specific table in a specific schema:

```
GRANT ALL ON TABLE `table-name` IN SCHEMA `schema-name` TO "IAMR:`data-api-access-role`"
```

These examples grant `ALL` privileges because the user must be able to read the
schema and write data to the cluster.

For more information about the `GRANT` SQL command, see [GRANT](../../../redshift/latest/dg/r_GRANT.md "../../../redshift/latest/dg/r_GRANT.md") in the _Amazon Redshift Database Developer Guide_.

The following information applies only to Amazon Redshift connections that are configured with JDBC
URLs. We don't recommend these types of connections because Amazon AppFlow will discontinue support
for JDBC URLs in the near future. You can refer to this section to manage existing
connections that use JDBC URLs. However, for any new Amazon Redshift connections that you create, you
should configure them with the Data API instead.

### JDBC requirements

You must provide Amazon AppFlow with the following:

- The user name and password of your Amazon Redshift user account.
- The JDBC URL of your Amazon Redshift cluster. For more information, see [Finding
  your cluster connection string](../../../redshift/latest/mgmt/configuring-connections.md#connecting-connection-string "../../../redshift/latest/mgmt/configuring-connections.md#connecting-connection-string") in the _Amazon Redshift Management Guide_.

You must also do the following:

- Ensure that you enter a correct JDBC connector and password when configuring your
  Redshift connections. An incorrect JDBC connector or password can return an
  **`'[Amazon](500310)'`** error.
- Ensure that your cluster is publicly accessible by going to the AWS Management
  Console, navigating to the Amazon Redshift console and choose CLUSTERS. Then, select
  the cluster that you want to modify and choose **Actions > Modify Publicly >
  Enable**. Save your changes.

If you still can't connect to the cluster from the internet or a different
network, go to the Amazon Redshift console and select the cluster that you want to
modify. Under **Properties**, choose **Network and
security settings**. Choose the link next to VPC security group to open
the Amazon Elastic Compute Cloud (Amazon EC2) console. On the Inbound Rules tab, make
sure that your IP address and the port of your Amazon Redshift cluster are allowed.
The default port for Amazon Redshift is 5439, but your port might be different.

- Ensure that your Amazon Redshift cluster is accessible from Amazon AppFlow IP address ranges in
  your Region.

### JDBC settings

- **JDBC URL** — The JDBC URL of the Amazon Redshift cluster where you
  want to connect.
- **Bucket details** — The Amazon S3 bucket where Amazon AppFlow writes
  your data as an intermediate destination. Amazon Redshift gets your data from this bucket.
- **IAM role for Amazon S3 access** — The IAM role that
  authorizes Amazon Redshift to get and decrypt the data from the S3 bucket.
- **Amazon Redshift database user name** — The user name that you use
  to authenticate with your Amazon Redshift database.
- **Amazon Redshift database password** — The password you use to
  authenticate with your Amazon Redshift database.

### Notes

- The default port for Amazon Redshift is 5439, but your port might be different. To find the
  Amazon AppFlow IP CIDR block for your region, see [AWS IP address ranges](../../../general/latest/gr/aws-ip-ranges.md "../../../general/latest/gr/aws-ip-ranges.md") in the
  _Amazon Web Services General Reference_.
- Amazon AppFlow currently supports the insert action when transferring data into Amazon Redshift,
  but not the update or upsert action.

### Related resources

- [Finding
  your cluster connection string](../../../redshift/latest/mgmt/configuring-connections.md#connecting-connection-string "../../../redshift/latest/mgmt/configuring-connections.md#connecting-connection-string") in the
  _Amazon Redshift Management Guide_
- [How to make a private Redshift cluster publicly accessible](https://aws.amazon.com/premiumsupport/knowledge-center/redshift-cluster-private-public/ "https://aws.amazon.com/premiumsupport/knowledge-center/redshift-cluster-private-public/")
  in the AWS Knowledge Center
- [Workaround to extract Salesforce data using Amazon AppFlow and upsert it to Amazon Redshift
  tables hosted on private subnet using data APIs](https://github.com/aws-samples/amazon-appflow/blob/master/sf-appflow-upsert-redshift-lambda/README.md "https://github.com/aws-samples/amazon-appflow/blob/master/sf-appflow-upsert-redshift-lambda/README.md") in the Amazon AppFlow GitHub
  Page

## Transferring data to Amazon Redshift with a flow

To transfer data to Amazon Redshift, create an Amazon AppFlow flow, and choose Amazon Redshift
as the data destination. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").



# Creating data providers in AWS Database Migration Service
<a name="data-providers-create"></a>

You can create data providers and use them in AWS DMS migration projects. Your data provider can be a self-managed engine running on-premises or on an Amazon EC2 instance. Also, your data provider can be a fully managed engine, such as Amazon Relational Database Service (Amazon RDS) or Amazon Aurora.

For each database, you can create a single data provider. You can use a single data provider in multiple migration projects.

Before creating a migration project, make sure that you have created at least two data providers. One of your data providers must be on an AWS service. You can't use AWS DMS to convert your schemas or migrate your data to an on-premises database.

The following procedure shows you how to create data providers in the AWS DMS console wizard.

**To create a data provider**

1. Sign in to the AWS Management Console, then open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/).

1. Choose **Data providers**. The **Data providers** page opens.

1. Choose **Create data provider**. The following table describes the settings.



<table>
<thead>
  <tr><th>Option</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><b>Configuration</b></td><td>Choose whether to enter the information about your data provider manually or to use the Amazon RDS DB instance.</td></tr>
  <tr><td><b>Name</b></td><td>Enter a name for your data provider. Make sure that you use a unique name for your data provider so that you can easily identify it.</td></tr>
  <tr><td><b>Engine type</b></td><td>Choose the type of the database engine for your data provider.</td></tr>
  <tr><td><b>Virtual Mode</b></td><td>Select <b>Virtual Mode</b> to use schema conversion without connecting to a database. For more information, see <a href="virtual-data-provider.md">Virtual mode for offline source and virtual target</a></td></tr>
  <tr><td><b>Server name</b></td><td>Enter the Domain Name Service (DNS) name or IP address of your database server. The server name for a data provider used for a homogeneous replication must start with an alphanumeric character, and can only contain alphanumeric characters, hyphens (-), periods (.), or underscores (_).</td></tr>
  <tr><td><b>Port</b></td><td>Enter the port used to connect to your database server.</td></tr>
  <tr><td><b>Service ID (SID) or service name</b></td><td>Enter the Oracle System ID (SID). To find the Oracle SID, submit the following query to your Oracle database:<pre>SELECT sys_context('userenv','instance_name') AS SID FROM dual;</pre></td></tr>
  <tr><td><b>Database name</b></td><td>Enter the name of the database for this data provider. The database name for a data provider used for a homogeneous replication can be up to 63 characters and can't contain spaces.</td></tr>
  <tr><td><b>Secure Socket Layer (SSL) mode</b></td><td>Choose an SSL mode if you want to turn on connection encryption for this data provider. Depending on the mode that you select, you might need to provide certificate and server certificate information. For further details, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.SSL">Using SSL with AWS Database Migration Service</a>.</td></tr>
  <tr><td><b>Authentication mode</b></td><td>For a MongoDB source, the authentication mode that AWS DMS uses to authenticate the endpoint connection.</td></tr>
  <tr><td><b>Authentication source</b></td><td>For a MongoDB source, the name of the MongoDB database to use to validate your credentials for authentication.</td></tr>
  <tr><td><b>Authentication mechanism</b></td><td>For a MongoDB source, the authentication method that MongoDB uses to encrypt the password.</td></tr>
</tbody>
</table>


1. Choose **Create data provider**.

After you create a data provider, make sure that you add database connection credentials in AWS Secrets Manager.
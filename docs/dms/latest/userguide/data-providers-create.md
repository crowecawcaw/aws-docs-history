# Creating data providers in AWS Database Migration Service

You can create data providers and use them in AWS DMS migration projects. Your data
provider can be a self-managed engine running on-premises or on an Amazon EC2 instance. Also,
your data provider can be a fully managed engine, such as Amazon Relational Database Service (Amazon RDS) or Amazon Aurora.

For each database, you can create a single data provider. You can use a single data provider
in multiple migration projects.

Before creating a migration project, make sure that you have created at least two data
providers. One of your data providers must be on an AWS service. You can't use
AWS DMS to convert your schemas or migrate your data to an on-premises database.

The following procedure shows you how to create data providers in the AWS DMS console
wizard.

###### To create a data provider

1. Sign in to the AWS Management Console, then open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Data providers**. The **Data providers** page
   opens.
3. Choose **Create data provider**. The following table describes the settings.

| Option                               | Action                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Configuration**                    | Choose whether to enter the information about your data<br>provider manually or to use the Amazon RDS DB instance.                                                                                                                                                                                                                                                   |
| **Name**                             | Enter a name for your data provider. Make sure that you<br>use a unique name for your data provider so that you can<br>easily identify it.                                                                                                                                                                                                                           |
| **Engine type**                      | Choose the type of the database engine for your data provider.                                                                                                                                                                                                                                                                                                       |
| **Server name**                      | Enter the Domain Name Service (DNS) name or IP address of your database server.<br>The server name for a data provider<br>used for a homogeneous replication must start with an alphanumeric character,<br>and can only contain alphanumeric characters, hyphens (-), periods (.), or underscores (\_).                                                              |
| **Port**                             | Enter the port used to connect to your database server.                                                                                                                                                                                                                                                                                                              |
| **Service ID (SID) or service name** | Enter the Oracle System ID (SID). To find the Oracle SID, submit the following<br>query to your Oracle database:<br>`<br>SELECT sys_context('userenv','instance_name') AS SID FROM dual;<br>`                                                                                                                                                                        |
| **Database name**                    | Enter the name of the database for this data provider. The database name for a data provider<br>used for a homogeneous replication can be up to 63 characters and can't contain spaces.                                                                                                                                                                              |
| **Secure Socket Layer (SSL) mode**   | Choose an SSL mode if you want to turn on connection<br>encryption for this data provider. Depending on the mode that you<br>select, you might need to provide certificate and server<br>certificate information. For further details, see [Using SSL with AWS Database Migration Service](CHAP_Security.md#CHAP_Security.SSL "CHAP_Security.md#CHAP_Security.SSL"). |
| **Authentication mode**              | For a MongoDB source, the authentication mode that AWS DMS<br>uses to authenticate the endpoint connection.                                                                                                                                                                                                                                                          |
| **Authentication source**            | For a MongoDB source, the name of the MongoDB database to use to validate your<br>credentials for authentication.                                                                                                                                                                                                                                                    |
| **Authentication mechanism**         | For a MongoDB source, the authentication method that MongoDB uses to<br>encrypt the password.                                                                                                                                                                                                                                                                        |

4. Choose **Create data provider**.
   After you create a data provider, make sure that you add database connection credentials in AWS Secrets Manager.

# AWS Glue connection

properties

This topic includes information about properties for AWS Glue connections.

###### Topics

- [Required connection
  properties](#connection-properties-required "#connection-properties-required")
- [AWS Glue JDBC connection
  properties](#connection-properties-jdbc "#connection-properties-jdbc")
- [AWS Glue MongoDB and MongoDB Atlas connection
  properties](#connection-properties-mongodb "#connection-properties-mongodb")
- [Salesforce connection
  properties](#connection-properties-salesforce "#connection-properties-salesforce")
- [Snowflake connection](#connection-properties-snowflake "#connection-properties-snowflake")
- [Vertica connection](#connection-properties-vertica "#connection-properties-vertica")
- [SAP HANA connection](#connection-properties-saphana "#connection-properties-saphana")
- [Azure SQL connection](#connection-properties-azuresql "#connection-properties-azuresql")
- [Teradata Vantage connection](#connection-properties-teradata "#connection-properties-teradata")
- [OpenSearch Service connection](#connection-properties-opensearch "#connection-properties-opensearch")
- [Azure Cosmos connection](#connection-properties-azurecosmos "#connection-properties-azurecosmos")
- [AWS Glue SSL connection
  properties](#connection-properties-SSL "#connection-properties-SSL")
- [Apache Kafka connection
  properties for client authentication](#connection-properties-authentication "#connection-properties-authentication")
- [Google BigQuery connection](#connection-properties-bigquery "#connection-properties-bigquery")
- [Vertica connection](#connection-properties-vertica "#connection-properties-vertica")

## Required connection

properties

When you define a connection on the AWS Glue console, you must provide
values for the following properties:

**Connection name**

Enter a unique name for your connection.

**Connection type**

Choose **JDBC** or one of the specific connection
types.

For details about the JDBC connection type, see [AWS Glue JDBC connection
properties](#connection-properties-jdbc "#connection-properties-jdbc")

Choose **Network** to connect to a data source within
an Amazon Virtual Private Cloud environment (Amazon VPC)).

Depending on the type that you choose, the AWS Glue
console displays other required fields. For example, if you choose
**Amazon RDS**, you must then choose the database
engine.

**Require SSL connection**

When you select this option, AWS Glue must verify that the
connection to the data store is connected over a trusted Secure Sockets
Layer (SSL).

For more information, including additional options that are available
when you select this option, see [AWS Glue SSL connection
properties](#connection-properties-SSL "#connection-properties-SSL").

**Select MSK cluster (Amazon managed streaming for Apache
Kafka (MSK) only)**

Specifies an MSK cluster from another AWS account.

**Kafka bootstrap server URLs (Kafka only)**

Specifies a comma-separated list of bootstrap server URLs. Include the
port number. For example:
b-1.vpc-test-2.o4q88o.c6.kafka.us-east-1.amazonaws.com:9094,
b-2.vpc-test-2.o4q88o.c6.kafka.us-east-1.amazonaws.com:9094,
b-3.vpc-test-2.o4q88o.c6.kafka.us-east-1.amazonaws.com:9094

## AWS Glue JDBC connection

properties

AWS Glue Studio now creates unified connections for MySQL, Oracle, PostgresSQL, Redshift, and SQL Server data sources, which requires
additional steps for accessing Secrets Manager and VPC resources, which may incur extra costs. You can access these
connections in AWS Glue Studio by choosing the connection name for the respective connection.

For more information, see [Considerations](using-connectors-unified-connections.md#using-connectors-unified-connections-considerations "using-connectors-unified-connections.md#using-connectors-unified-connections-considerations").

AWS Glue can connect to the following data stores through a JDBC
connection:

- Amazon Redshift
- Amazon Aurora
- Microsoft SQL Server
- MySQL
- Oracle
- PostgreSQL
- Snowflake, when using AWS Glue crawlers.
- Aurora (supported if the native JDBC driver is being used. Not all driver features can be leveraged)
- Amazon RDS for MariaDB

###### Important

Currently, an ETL job can use JDBC connections within only one subnet. If you
have multiple data stores in a job, they must be on the same subnet, or accessible from the subnet.

If you choose to bring in your own JDBC driver versions for AWS Glue crawlers, your crawlers will consume resources in AWS Glue
jobs and Amazon S3 to ensure your provided drivers are run in your environment. The additional usage of resources will be reflected in your account.
Additionally, providing your own JDBC driver does not mean that the crawler is able to leverage all of the driver’s features.
Drivers are limited to the properties described in
[Defining connections in the Data Catalog](glue-connections.md "glue-connections.md").

The following are additional properties for the JDBC connection type.

**JDBC URL**

Enter the URL for your JDBC data store. For most database engines, this
field is in the following format. In this format, replace
`protocol`,
`host`, `port`, and
`db_name` with your own information.

`jdbc:`protocol`://`host`:`port`/`db_name``

Depending on the database engine, a different JDBC URL format might be
required. This format can have slightly different use of the colon (:)
and slash (/) or different keywords to specify databases.

For JDBC to connect to the data store, a `db_name` in the
data store is required. The `db_name` is used to establish a
network connection with the supplied `username` and
`password`. When connected, AWS Glue can
access other databases in the data store to run a crawler or run an ETL
job.

The following JDBC URL examples show the syntax for several database
engines.

- To connect to an Amazon Redshift cluster data store with a
  `dev` database:

`jdbc:redshift://xxx.us-east-1.redshift.amazonaws.com:8192/dev`

- To connect to an Amazon RDS for MySQL data store with an
  `employee` database:

`jdbc:mysql://xxx-cluster.cluster-xxx.us-east-1.rds.amazonaws.com:3306/employee`

- To connect to an Amazon RDS for PostgreSQL data store with an
  `employee` database:

`jdbc:postgresql://xxx-cluster.cluster-xxx.us-east-1.rds.amazonaws.com:5432/employee`

- To connect to an Amazon RDS for Oracle data store with an
  `employee` service name:

`jdbc:oracle:thin://@xxx-cluster.cluster-xxx.us-east-1.rds.amazonaws.com:1521/employee`

The syntax for Amazon RDS for Oracle can follow the following
patterns. In these patterns, replace
`host`,
`port`,
`service_name`, and
`SID` with your own
information.

    + `jdbc:oracle:thin://@`host`:`port`/`service_name``
    + `jdbc:oracle:thin://@`host`:`port`:`SID``

- To connect to an Amazon RDS for Microsoft SQL Server data store
  with an `employee` database:

`jdbc:sqlserver://xxx-cluster.cluster-xxx.us-east-1.rds.amazonaws.com:1433;databaseName=employee`

The syntax for Amazon RDS for SQL Server can follow the following
patterns. In these patterns, replace
`server_name`,
`port`, and
`db_name` with your own
information.

    + `jdbc:sqlserver://`server_name`:`port`;database=`db_name``
    + `jdbc:sqlserver://`server_name`:`port`;databaseName=`db_name``

- To connect to an Amazon Aurora PostgreSQL instance
  of the `employee` database, specify the endpoint for
  the database instance, the port, and the database name:

`jdbc:postgresql://employee_instance_1.`xxxxxxxxxxxx`.us-east-2.rds.amazonaws.com:5432/employee`

- To connect to an Amazon RDS for MariaDB data store with an
  `employee` database, specify the endpoint for the
  database instance, the port, and the database name:

`jdbc:mysql://`xxx`-cluster.cluster-`xxx`.`aws-region`.rds.amazonaws.com:3306/employee`

- ###### Warning

Snowflake JDBC connections are supported only by AWS Glue crawlers. When using
the Snowflake connector in AWS Glue jobs, use the Snowflake connection
type.

To connect to a Snowflake instance of the `sample` database, specify the endpoint for the snowflake instance, the user, the database name, and the role name. You can optionally add the `warehouse` parameter.

`jdbc:snowflake://`account_name`.snowflakecomputing.com/?user=`user_name`&db=sample&role=`role_name`&warehouse=`warehouse_name``

###### Important

For Snowflake connections over JDBC, the order of parameters in the URL is enforced and must be ordered as
`user`, `db`, `role_name`, and `warehouse`.

- To connect to a Snowflake instance of the `sample` database with AWS private link, specify the snowflake JDBC URL as follows:

`jdbc:snowflake://`account_name`.`region`.privatelink.snowflakecomputing.com/?user=`user_name`&db=sample&role=`role_name`&warehouse=`warehouse_name``

**Username**

###### Note

We recommend that you use an AWS secret to store connection
credentials instead of supplying your user name and password
directly. For more information, see [Storing connection credentials
in AWS Secrets Manager](connection-properties-secrets-manager.md "connection-properties-secrets-manager.md").

Provide a user name that has permission to access the JDBC data store.

**Password**

Enter the password for the user name that has access permission to the
JDBC data store.

**Port**

Enter the port used in the JDBC URL to connect to an Amazon RDS Oracle
instance. This field is only shown when **Require SSL
connection** is selected for an Amazon RDS Oracle
instance.

**VPC**

Choose the name of the virtual private cloud (VPC) that contains your
data store. The AWS Glue console lists all VPCs for the
current Region.

###### Important

When working over a JDBC connection which is hosted off of AWS, such as with data from Snowflake,
your VPC should have a NAT gateway which splits traffic into public and private subnets. The
public subnet is used for connection to the external source, and the internal subnet is used for
processing by AWS Glue. For information on configuring your Amazon VPC for external connections, read
[Connect to the internet or other networks using NAT devices](../../../vpc/latest/userguide/vpc-nat.md "../../../vpc/latest/userguide/vpc-nat.md")
and [Setting up Amazon VPC for JDBC connections to Amazon RDS data stores from
AWS Glue](setup-vpc-for-glue-access.md "setup-vpc-for-glue-access.md").

**Subnet**

Choose the subnet within the VPC that contains your data store. The
AWS Glue console lists all subnets for the data store in
your VPC.

**Security groups**

Choose the security groups that are associated with your data store.
AWS Glue requires one or more security groups with an
inbound source rule that allows AWS Glue to connect. The
AWS Glue console lists all security groups that are
granted inbound access to your VPC. AWS Glue associates
these security groups with the elastic network interface that is
attached to your VPC subnet.

**JDBC Driver Class name - optional**

Provide the custom JDBC driver class name:

- Postgres – org.postgresql.Driver
- MySQL – com.mysql.jdbc.Driver, com.mysql.cj.jdbc.Driver
- Redshift – com.amazon.redshift.jdbc.Driver, com.amazon.redshift.jdbc42.Driver
- Oracle – oracle.jdbc.driver.OracleDriver
- SQL Server – com.microsoft.sqlserver.jdbc.SQLServerDriver

**JDBC Driver S3 Path - optional**

Provide the Amazon S3 location to the custom JDBC driver. This is an absolute path to a .jar file. If you want to provide
your own JDBC drivers to connect to your data souces for your crawler-supported databases,
you can specify values for parameters

`customJdbcDriverS3Path` and `customJdbcDriverClassName`.
Using a JDBC driver supplied by a customer is
limited to the required [Required connection
properties](#connection-properties-required "#connection-properties-required").

## AWS Glue MongoDB and MongoDB Atlas connection

properties

The following are additional properties for the MongoDB or MongoDB Atlas connection type.

**MongoDB URL**

Enter the URL for your MongoDB or MongoDB Atlas data store:

- For MongoDB: mongodb://host:port/database. The host can be a hostname, IP address, or UNIX domain socket. If the connection string doesn't specify a port, it uses the default MongoDB port, 27017.
- For MongoDB Atlas: mongodb+srv://server.example.com/database. The host can be a hostname that follows corresponds to a DNS SRV record. The SRV format does not require a port and will use the default MongoDB port, 27017.

**Username**

###### Note

We recommend that you use an AWS secret to store connection
credentials instead of supplying your user name and password
directly. For more information, see [Storing connection credentials
in AWS Secrets Manager](connection-properties-secrets-manager.md "connection-properties-secrets-manager.md").

Provide a user name that has permission to access the JDBC data store.

**Password**

Enter the password for the user name that has access permission to the
MongoDB or MongoDB Atlas data store.

## Salesforce connection

properties

The following are additional properties for the Salesforce connection type.

- `ENTITY_NAME`(String) - (Required) Used for Read/Write. The name of your Object in Salesforce.
- `API_VERSION`(String) - (Required) Used for Read/Write. Salesforce Rest API version you want to use.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.
- `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
- `PARTITION_FIELD`(String) - Used for Read. Field to be used to partition query.
- `LOWER_BOUND`(String)- Used for Read. An inclusive lower bound value of the chosen partition field.
- `UPPER_BOUND`(String) - Used for Read. An exclusive upper bound value of the chosen partition field.
- `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read.
- `IMPORT_DELETED_RECORDS`(String) - Default: FALSE. Used for read. To get the delete records while querying.
- `WRITE_OPERATION`(String) - Default: INSERT. Used for write. Value should be INSERT, UPDATE, UPSERT, DELETE.
- `ID_FIELD_NAMES`(String) - Default : null. Used only for UPSERT.

## Snowflake connection

The following properties are used to set up a Snowflake connection used in AWS Glue ETL jobs.
When crawling Snowflake, use a JDBC connection.

**Snowflake URL**

The URL of your Snowflake endpoint. For more information about Snowflake endpoint URLs, see
[Connecting to
Your Accounts](https://docs.snowflake.com/en/user-guide/organizations-connect "https://docs.snowflake.com/en/user-guide/organizations-connect") in the Snowflake documentation.

**AWS Secret**
The **Secret name** of a secret in AWS Secrets Manager. AWS Glue will connect to
Snowflake using the `sfUser` and `sfPassword` keys of your secret.

**Snowflake role (optional)**
A Snowflake security role AWS Glue will use when connecting.

Use the following properties when configuring a connection to a Snowflake endpoint hosted in Amazon VPC using AWS PrivateLink.

**VPC**

Choose the name of the virtual private cloud (VPC) that contains your
data store. The AWS Glue console lists all VPCs for the
current Region.

**Subnet**

Choose the subnet within the VPC that contains your data store. The
AWS Glue console lists all subnets for the data store in
your VPC.

**Security groups**

Choose the security groups that are associated with your data store.
AWS Glue requires one or more security groups with an
inbound source rule that allows AWS Glue to connect. The
AWS Glue console lists all security groups that are
granted inbound access to your VPC. AWS Glue associates
these security groups with the elastic network interface that is
attached to your VPC subnet.

## Vertica connection

Use the following properties to set up a Vertica connection for AWS Glue ETL jobs.

**Vertica Host**
The hostname of your Vertica installation.

**Vertica Port**
The port your Vertica installation is available through.

**AWS Secret**
The **Secret name** of a secret in AWS Secrets Manager. AWS Glue will connect to
Vertica using the keys of your secret.

Use the following properties when configuring a connection to a Vertica endpoint hosted in Amazon VPC.

**VPC**

Choose the name of the virtual private cloud (VPC) that contains your
data store. The AWS Glue console lists all VPCs for the
current Region.

**Subnet**

Choose the subnet within the VPC that contains your data store. The
AWS Glue console lists all subnets for the data store in
your VPC.

**Security groups**

Choose the security groups that are associated with your data store.
AWS Glue requires one or more security groups with an
inbound source rule that allows AWS Glue to connect. The
AWS Glue console lists all security groups that are
granted inbound access to your VPC. AWS Glue associates
these security groups with the elastic network interface that is
attached to your VPC subnet.

## SAP HANA connection

Use the following properties to set up a SAP HANA connection for AWS Glue ETL jobs.

**SAP HANA URL**
A SAP JDBC URL.

SAP HANA JDBC URLs are in the form `jdbc:sap://`saphanaHostname`:`saphanaPort`/?`databaseName`=`saphanaDBname`,`ParameterName`=`ParameterValue``

AWS Glue requires the following JDBC URL parameters:

- `databaseName` – A default database in SAP HANA to connect to.

**AWS Secret**
The **Secret name** of a secret in AWS Secrets Manager. AWS Glue will connect to
SAP HANA using the keys of your secret.

Use the following properties when configuring a connection to a SAP HANA endpoint hosted in Amazon VPC:

**VPC**

Choose the name of the virtual private cloud (VPC) that contains your
data store. The AWS Glue console lists all VPCs for the
current Region.

**Subnet**

Choose the subnet within the VPC that contains your data store. The
AWS Glue console lists all subnets for the data store in
your VPC.

**Security groups**

Choose the security groups that are associated with your data store.
AWS Glue requires one or more security groups with an
inbound source rule that allows AWS Glue to connect. The
AWS Glue console lists all security groups that are
granted inbound access to your VPC. AWS Glue associates
these security groups with the elastic network interface that is
attached to your VPC subnet.

## Azure SQL connection

Use the following properties to set up a Azure SQL connection for AWS Glue ETL jobs.

**Azure SQL URL**
The JDBC URL of an Azure SQL endpoint.

The URL must be in the following format:
`jdbc:sqlserver://`databaseServerName`:`databasePort`;databaseName=`azuresqlDBname`;`.

AWS Glue requires the following URL properties:

- `databaseName` – A default database in Azure SQL to connect to.

For more information about JDBC URLs for Azure SQL Managed Instances, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?view=azuresqldb-mi-current "https://learn.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?view=azuresqldb-mi-current").

**AWS Secret**
The **Secret name** of a secret in AWS Secrets Manager. AWS Glue will connect to
Azure SQL using the keys of your secret.

## Teradata Vantage connection

Use the following properties to set up a Teradata Vantage connection for AWS Glue ETL jobs.

**Teradata URL**
To connect to a Teradata instance specify the hostname for the database instance and relevant Teradata parameters:

`jdbc:teradata://`teradataHostname`/`ParameterName`=`ParameterValue`,`ParameterName`=`ParameterValue``.

AWS Glue supports the following JDBC URL parameters:

- `DATABASE_NAME` – A default database in Teradata to connect to.
- `DBS_PORT` – Specifies the Teradata port, if nonstandard.

**AWS Secret**
The **Secret name** of a secret in AWS Secrets Manager. AWS Glue will connect to
Teradata Vantage using the keys of your secret.

Use the following properties when configuring a connection to a Teradata Vantage endpoint hosted in Amazon VPC:

**VPC**

Choose the name of the virtual private cloud (VPC) that contains your
data store. The AWS Glue console lists all VPCs for the
current Region.

**Subnet**

Choose the subnet within the VPC that contains your data store. The
AWS Glue console lists all subnets for the data store in
your VPC.

**Security groups**

Choose the security groups that are associated with your data store.
AWS Glue requires one or more security groups with an
inbound source rule that allows AWS Glue to connect. The
AWS Glue console lists all security groups that are
granted inbound access to your VPC. AWS Glue associates
these security groups with the elastic network interface that is
attached to your VPC subnet.

## OpenSearch Service connection

Use the following properties to set up a OpenSearch Service connection for AWS Glue ETL jobs.

**Domain endpoint**
An Amazon OpenSearch Service domain endpoint will have the following default form,
https://search-`domainName`-`unstructuredIdContent`.`region`.es.amazonaws.com.
For more information on identifying your domain endpoint, see [Creating and managing
Amazon OpenSearch Service domains](../../../opensearch-service/latest/developerguide/createupdatedomains.md "../../../opensearch-service/latest/developerguide/createupdatedomains.md") in the Amazon OpenSearch Service documentation.

**Port**
The port open on the endpoint.

**AWS Secret**
The **Secret name** of a secret in AWS Secrets Manager. AWS Glue will connect to
OpenSearch Service using the keys of your secret.

Use the following properties when configuring a connection to a OpenSearch Service endpoint hosted in Amazon VPC:

**VPC**

Choose the name of the virtual private cloud (VPC) that contains your
data store. The AWS Glue console lists all VPCs for the
current Region.

**Subnet**

Choose the subnet within the VPC that contains your data store. The
AWS Glue console lists all subnets for the data store in
your VPC.

**Security groups**

Choose the security groups that are associated with your data store.
AWS Glue requires one or more security groups with an
inbound source rule that allows AWS Glue to connect. The
AWS Glue console lists all security groups that are
granted inbound access to your VPC. AWS Glue associates
these security groups with the elastic network interface that is
attached to your VPC subnet.

## Azure Cosmos connection

Use the following properties to set up a Azure Cosmos connection for AWS Glue ETL jobs.

**Azure Cosmos DB Account Endpoint URI**

The endpoint used to connect to Azure Cosmos. For more information, see [the Azure documentation](https://learn.microsoft.com/en-us/rest/api/cosmos-db/cosmosdb-resource-uri-syntax-for-rest "https://learn.microsoft.com/en-us/rest/api/cosmos-db/cosmosdb-resource-uri-syntax-for-rest").

**AWS Secret**
The **Secret name** of a secret in AWS Secrets Manager. AWS Glue will connect to
Azure Cosmos using the keys of your secret.

## AWS Glue SSL connection

properties

The following are details about the **Require SSL connection**
property.

If you do not require SSL connection, AWS Glue ignores failures when
it uses SSL to encrypt a connection to the data store. See the documentation for
your data store for configuration instructions. When you select this option, the job
run, crawler, or ETL statements in a development endpoint fail when
AWS Glue cannot connect.

###### Note

Snowflake supports an SSL connection by default, so this property is not applicable for Snowflake.

This option is validated on the AWS Glue client side. For JDBC
connections, AWS Glue only connects over SSL with certificate and host
name validation. SSL connection support is available for:

- Oracle Database
- Microsoft SQL Server
- PostgreSQL
- Amazon Redshift
- MySQL (Amazon RDS instances only)
- Amazon Aurora MySQL (Amazon RDS instances only)
- Amazon Aurora PostgreSQL (Amazon RDS instances only)
- Kafka, which includes Amazon Managed Streaming for Apache Kafka
- MongoDB

###### Note

To enable an **Amazon RDS Oracle** data store to use
**Require SSL connection**, you must create and attach an
option group to the Oracle instance.

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Add an **Option group** to the Amazon RDS Oracle instance.
   For more information about how to add an option group on the Amazon RDS
   console, see [Creating an Option Group](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create")
3. Add an **Option** to the option group for
   **SSL**. The **Port** you specify
   for SSL is later used when you create an AWS Glue JDBC
   connection URL for the Amazon RDS Oracle instance. For more information about
   how to add an option on the Amazon RDS console, see [Adding an Option to an Option Group](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption") in the
   _Amazon RDS User Guide_. For more information about
   the Oracle SSL option, see [Oracle
   SSL](../../../AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.md "../../../AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.md") in the _Amazon RDS User Guide_.
4. On the AWS Glue console, create a connection to the Amazon RDS
   Oracle instance. In the connection definition, select **Require
   SSL connection**. When requested, enter the
   **Port** that you used in the Amazon RDS Oracle SSL
   option.

The following additional optional properties are available when **Require
SSL connection** is selected for a connection:

**Custom JDBC certificate in S3**

If you have a certificate that you are currently using for SSL
communication with your on-premises or cloud databases, you can use that
certificate for SSL connections to AWS Glue data sources or
targets. Enter an Amazon Simple Storage Service (Amazon S3) location that contains a custom root
certificate. AWS Glue uses this certificate to establish an
SSL connection to the database. AWS Glue handles only X.509
certificates. The certificate must be DER-encoded and supplied in base64
encoding PEM format.

If this field is left blank, the default certificate is used.

**Custom JDBC certificate string**

Enter certificate information specific to your JDBC database. This
string is used for domain matching or distinguished name (DN) matching.
For Oracle Database, this string maps to the
`SSL_SERVER_CERT_DN` parameter in the security section of
the `tnsnames.ora` file. For Microsoft SQL Server,
this string is used as `hostNameInCertificate`.

The following is an example for the Oracle Database
`SSL_SERVER_CERT_DN` parameter.

```
cn=sales,cn=OracleContext,dc=us,dc=example,dc=com
```

**Kafka private CA certificate
location**

If you have a certificate that you are currently using for SSL
communication with your Kafka data store, you can use that certificate
with your AWS Glue connection. This option is required for
Kafka data stores, and optional for Amazon Managed Streaming for Apache Kafka data stores.
Enter an Amazon Simple Storage Service (Amazon S3) location that contains a custom root
certificate. AWS Glue uses this certificate to establish an
SSL connection to the Kafka data store. AWS Glue handles
only X.509 certificates. The certificate must be DER-encoded and
supplied in base64 encoding PEM format.

**Skip certificate validation**

Select the **Skip certificate validation** check box
to skip validation of the custom certificate by AWS Glue. If
you choose to validate, AWS Glue validates the signature
algorithm and subject public key algorithm for the certificate. If the
certificate fails validation, any ETL job or crawler that uses the
connection fails.

The only permitted signature algorithms are SHA256withRSA,
SHA384withRSA, or SHA512withRSA. For the subject public key algorithm,
the key length must be at least 2048.

**Kafka client keystore location**

The Amazon S3 location of the client keystore file for Kafka client side
authentication. Path must be in the form
s3://bucket/prefix/filename.jks. It must end with the file name and .jks
extension.

**Kafka client keystore password
(optional)**

The password to access the provided keystore.

**Kafka client key password
(optional)**

A keystore can consist of multiple keys, so this is the password to
access the client key to be used with the Kafka server side key.

## Apache Kafka connection

properties for client authentication

AWS Glue supports the Simple Authentication and Security Layer (SASL)
framework for authentication when you create an Apache Kafka connection. The SASL
framework supports various mechanisms of authentication, and AWS Glue
offers the SCRAM (user name and password), GSSAPI (Kerberos protocol), and PLAIN protocols.

Use AWS Glue Studio to configure one of the following client authentication methods. For
more information, see [Creating
connections for connectors](../ug/connectors-chapter.md#creating-connections "../ug/connectors-chapter.md#creating-connections") in the AWS Glue Studio user guide.

- None - No authentication. This is useful if creating a connection for
  testing purposes.
- SASL/SCRAM-SHA-512 - Choosing this authentication method will allow you to
  specify authentication credentials. There are two options available:
  - Use AWS Secrets Manager (recommended) - if you select this
    option, you can store your user name and password in AWS Secrets
    Manager and let AWS Glue access them when needed.
    Specify the secret that stores the SSL or SASL authentication
    credentials. For more information, see [Storing connection credentials
    in AWS Secrets Manager](connection-properties-secrets-manager.md "connection-properties-secrets-manager.md").
  - Provide a user name and password directly.

- SASL/GSSAPI (Kerberos) - if you select this option, you can select the
  location of the keytab file, krb5.conf file and enter the Kerberos principal
  name and Kerberos service name. The locations for the keytab file and
  krb5.conf file must be in an Amazon S3 location. Since MSK does not yet support
  SASL/GSSAPI, this option is only available for customer managed Apache Kafka
  clusters. For more information, see [MIT Kerberos Documentation: Keytab](https://web.mit.edu/kerberos/krb5-latest/doc/basic/keytab_def.html "https://web.mit.edu/kerberos/krb5-latest/doc/basic/keytab_def.html") .
- SASL/PLAIN - choose this authentication method to specify authentication credentials. There are two options available:
  - Use AWS Secrets Manager (recommended) - if you select this option, you can store your credentials in AWS Secrets Manager and let AWS Glue access the information when needed. Specify the secret that stores the SSL or SASL authentication credentials.
  - Provide username and password directly.

- SSL Client Authentication - if you select this option, you can you can
  select the location of the Kafka client keystore by browsing Amazon S3.
  Optionally, you can enter the Kafka client keystore password and Kafka
  client key password.

## Google BigQuery connection

The following properties are used to set up a Google BigQuery connection used in AWS Glue ETL jobs. For more
information, see [BigQuery connections](aws-glue-programming-etl-connect-bigquery-home.md "aws-glue-programming-etl-connect-bigquery-home.md").

AWS Secret

The **Secret name** of a secret in AWS Secrets Manager. AWS Glue ETL jobs will connect
to Google BigQuery using the `credentials` key of your secret.

## Vertica connection

The following properties are used to set up a Vertica connection used in AWS Glue ETL jobs. For more
information, see [Vertica connections](aws-glue-programming-etl-connect-vertica-home.md "aws-glue-programming-etl-connect-vertica-home.md").

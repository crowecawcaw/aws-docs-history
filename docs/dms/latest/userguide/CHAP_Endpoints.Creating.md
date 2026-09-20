

# Creating source and target endpoints
<a name="CHAP_Endpoints.Creating"></a>

You can create source and target endpoints when you create your replication instance or you can create endpoints after your replication instance is created. The source and target data stores can be on an Amazon Elastic Compute Cloud (Amazon EC2) instance, an Amazon Relational Database Service (Amazon RDS) DB instance, or an on-premises database. (Note that one of your endpoints must be on an AWS service. You can't use AWS DMS to migrate from an on-premises database to another on-premises database.)

The following procedure assumes that you have chosen the AWS DMS console wizard. Note that you can also do this step by selecting **Endpoints** from the AWS DMS console's navigation pane and then selecting **Create endpoint**. When using the console wizard, you create both the source and target endpoints on the same page. When not using the console wizard, you create each endpoint separately.

**To specify source or target database endpoints using the AWS console**

1. On the **Connect source and target database endpoints** page, specify your connection information for the source or target database. The following table describes the settings.


<table>
<thead>
  <tr><th>Configuration options </th><th>Configuration settings </th></tr>
</thead>
<tbody>
  <tr><td><b>Endpoint type</b></td><td>Choose whether this endpoint is the source or target endpoint.</td></tr>
  <tr><td><b>Select RDS DB Instance</b></td><td>Choose this option if the endpoint is an Amazon RDS database instance. </td></tr>
  <tr><td> <b>Endpoint identifier</b> </td><td>Type the name you want to use to identify the endpoint. You might want to include in the name the type of endpoint, such as <b>oracle-source</b> or <b>PostgreSQL-target</b>. The name must be unique for all replication instances.</td></tr>
  <tr><td><b>Descriptive Amazon Resource Name (ARN) - <i>optional</i></b></td><td>Provide a name to override the default DMS ARN. This setting is optional.</td></tr>
  <tr><td><b>Source engine</b> and <b>Target engine</b></td><td>Choose the type of database engine that is the endpoint.</td></tr>
  <tr><td> <b>Access to endpoint database</b> </td><td>Choose the option you want to use to specify endpoint database credentials:<ul><li> <a href="#ChooseAWSSecretsManager">**Choose AWS Secrets Manager**</a> – Use secrets defined in AWS Secrets Manager to secretly provide your credentials as shown following. For more information on creating these secrets and the secret access roles that enable AWS DMS to access them, see <a href="security_iam_secretsmanager.md">Using secrets to access AWS Database Migration Service endpoints</a>. </li><li> <a href="#ProvideAccessInformationManually">**Provide access information manually**</a> – Use clear-text credentials that you enter directly as shown following. </li><li> <a href="CHAP_Endpoints.Creating.IAMRDS.md">**IAM authentication**</a> – IAM as the authentication type instead of username and password for your Amazon RDS database instance. </li></ul></td></tr>
  <tr><td><b>Choose AWS Secrets Manager</b></td><td>Set the following secret credentials.</td></tr>
  <tr><td><b>Secret ID</b></td><td>Type the full Amazon Resource Name (ARN), partial ARN, or friendly name of a secret that you have created in the AWS Secrets Manager for endpoint database access.</td></tr>
  <tr><td><b>IAM role </b></td><td>Type the ARN of a secret access role that you have created in IAM to provide AWS DMS access on your behalf to the secret identified by <b>Secret ID</b>. For information about creating a secret access role, see <a href="security_iam_secretsmanager.md">Using secrets to access AWS Database Migration Service endpoints</a>.</td></tr>
  <tr><td><b>Secret ID for Oracle automatic storage management (ASM)</b></td><td>(For Oracle source endpoints using Oracle ASM only) Type the full Amazon Resource Name (ARN), partial ARN, or friendly name of a secret that you have created in the AWS Secrets Manager for Oracle ASM access. This secret is typically created to access Oracle ASM on the same server as the secret identified by <b>Secret ID</b>.</td></tr>
  <tr><td><b>IAM role for Oracle ASM</b></td><td>(For Oracle source endpoints using Oracle ASM only) Type the ARN of a secret access role that you have created in IAM to provide AWS DMS access on your behalf to the secret identified by <b>Secret ID for Oracle automatic storage management (ASM)</b>.</td></tr>
  <tr><td><b>Provide access information manually</b></td><td>Set the following clear-text credentials.</td></tr>
  <tr><td> <b>Server name</b> </td><td>Type the server name. For an on-premises database, this can be the IP address or the public hostname. For an Amazon RDS DB instance, this can be the endpoint (also called the DNS name) for the DB instance, such as <b>mysqlsrvinst.abcd12345678.us-west-2.rds.amazonaws.com</b>.</td></tr>
  <tr><td> <b>Port</b> </td><td>Type the port used by the database.</td></tr>
  <tr><td> <b>Secure Socket Layer (SSL) mode</b> </td><td>Choose an SSL mode if you want to enable connection encryption for this endpoint. Depending on the mode you select, you might be asked to provide certificate and server certificate information.</td></tr>
  <tr><td> <b>User name</b> </td><td>Type the user name with the permissions required to allow data migration. For information on the permissions required, see the security section for the source or target database engine in this user guide.</td></tr>
  <tr><td> <b>Password</b> </td><td>Type the password for the account with the required permissions. Passwords for AWS DMS source and target endpoints have character restrictions, depending on the database engine. For more information, see the following table.</td></tr>
  <tr><td> <b>Database name</b> </td><td>For certain database engines, the name of the database you want to use as the endpoint database.</td></tr>
</tbody>
</table>


   The following table lists the unsupported characters in endpoint passwords and secret manager secrets for the listed database engines. If you want to use commas (,) in your endpoint passwords, use the Secrets Manager support provided in AWS DMS to authenticate access to your AWS DMS instances. For more information, see [Using secrets to access AWS Database Migration Service endpoints](security_iam_secretsmanager.md).


<table>
<thead>
  <tr><th>For this database engine</th><th>The following characters are unsupported in an endpoint password and secret manager secrets</th></tr>
</thead>
<tbody>
  <tr><td>All</td><td><code>{ }</code></td></tr>
  <tr><td>Microsoft Azure, as a source only</td><td><code>;</code></td></tr>
  <tr><td>Microsoft SQL Server</td><td><code>, ;</code></td></tr>
  <tr><td>MySQL-compatible, including MySQL, MariaDB, and Amazon Aurora MySQL</td><td><code>;</code></td></tr>
  <tr><td>Oracle</td><td><code>,</code></td></tr>
  <tr><td>PostgreSQL, Amazon Aurora PostgreSQL-Compatible Edition, and Amazon Aurora Serverless as a target only for Aurora PostgreSQL-Compatible Edition</td><td><code>; + %</code></td></tr>
  <tr><td>Amazon Redshift, as a target only</td><td><code>, ;</code></td></tr>
</tbody>
</table>


1. Choose **Endpoint settings** and **AWS KMS key ** if you need them. You can test the endpoint connection by choosing **Run test**. The following table describes the settings.


<table>
<thead>
  <tr><th>Configuration options</th><th>Configuration settings </th></tr>
</thead>
<tbody>
  <tr><td> <b>Endpoint settings</b> </td><td>Select any additional connection parameters here. For more information about endpoint settings, see the documentation section for your <b>Source engine</b> or <b>Target engine</b> (specified in step 1).<br />For an Oracle source endpoint that uses Oracle ASM, if you choose <b>Provide access information manually</b> in step 1, you might also need to type in endpoint setting to specify Oracle ASM user credentials. For more information on these Oracle ASM endpoint settings, see <a href="CHAP_Source.Oracle.md#CHAP_Source.Oracle.CDC">Using Oracle LogMiner or AWS DMS Binary Reader for CDC</a>. If you specify the same connection attribute in both <b>Endpoint settings</b> and <b>Extra connection attributes</b>, the value in <b>Endpoint settings</b> takes precedence. </td></tr>
  <tr><td> <b>AWS KMS key</b> </td><td>Choose the encryption key to use to encrypt replication storage and connection information. If you choose <b>(Default) aws/dms</b>, the default AWS Key Management Service (AWS KMS) key associated with your account and AWS Region is used. For more information on using the encryption key, see <a href="CHAP_Security.md#CHAP_Security.EncryptionKey">Setting an encryption key and specifying AWS KMS permissions</a>.</td></tr>
  <tr><td> <b>Test endpoint connection (optional)</b> </td><td>Add the VPC and replication instance name. To test the connection, choose <b>Run test</b>.</td></tr>
</tbody>
</table>

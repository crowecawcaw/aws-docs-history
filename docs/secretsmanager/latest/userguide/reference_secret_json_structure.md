# JSON structure of AWS Secrets Manager secrets

You can store any text or binary in a Secrets Manager secret up to the maximum size of 65,536 Bytes.

If you use [Rotation by Lambda function](rotate-secrets_lambda.md "rotate-secrets_lambda.md"), a secret must contain specific JSON fields that the rotation function expects. For example, for a secret that contains database credentials, the rotation function connects to the database to update credentials, so the secret must contain the database connection information.

If you use the console to edit rotation for a database secret, the secret must contain specific JSON key-value pairs that identify the database. Secrets Manager uses these fields to query the database to find the correct VPC to store a rotation function in.

JSON key names are case-sensitive.

###### Topics

- [Amazon RDS and Aurora credentials](#reference_secret_json_structure_rds "#reference_secret_json_structure_rds")
- [Amazon Redshift credentials](#reference_secret_json_structure_RS "#reference_secret_json_structure_RS")
- [Amazon Redshift Serverless credentials](#reference_secret_json_structure_RSServerless "#reference_secret_json_structure_RSServerless")
- [Amazon DocumentDB credentials](#reference_secret_json_structure_docdb "#reference_secret_json_structure_docdb")
- [Amazon Timestream for InfluxDB secret structure](#reference_secret_json_structure_TIME "#reference_secret_json_structure_TIME")
- [Amazon ElastiCache credentials](#reference_secret_json_structure_ELC "#reference_secret_json_structure_ELC")
- [Active Directory credentials](#reference_secret_json_structure_AD "#reference_secret_json_structure_AD")

## Amazon RDS and Aurora credentials

To use the [rotation function templates provided by Secrets Manager](reference_available-rotation-templates.md#RDS_rotation_templates "reference_available-rotation-templates.md#RDS_rotation_templates"), use the following JSON structure. You can add more key/value pairs, for example to contain connection information for replica databases in other Regions.

DB2
For Amazon RDS Db2 instances, because users can't change their own passwords, you must provide admin credentials in a separate secret.

```
{
  "engine": "db2",
  "host": "`<instance host name/resolvable DNS name>`",
  "username": "`<username>`",
  "password": "`<password>`",
  "dbname": "`<database name. If not specified, defaults to None>`",
  "port": `<TCP port number. If not specified, defaults to 3306>`,
  "masterarn": "`<ARN of the elevated secret>`",
  "dbInstanceIdentifier": `<optional: ID of the instance. Alternately, use dbClusterIdentifier. Required for configuring rotation in the console.>`",
  "dbClusterIdentifier": `<optional: ID of the cluster. Alternately, use dbInstanceIdentifier. Required for configuring rotation in the console.>`"
}
```

MariaDB

```
{
  "engine": "mariadb",
  "host": "`<instance host name/resolvable DNS name>`",
  "username": "`<username>`",
  "password": "`<password>`",
  "dbname": "`<database name. If not specified, defaults to None>`",
  "port": `<TCP port number. If not specified, defaults to 3306>`,
  "masterarn": "`<optional: ARN of the elevated secret. Required for the Rotation strategy: alternating users.>`",
  "dbInstanceIdentifier": `<optional: ID of the instance. Alternately, use dbClusterIdentifier. Required for configuring rotation in the console.>`",
  "dbClusterIdentifier": `<optional: ID of the cluster. Alternately, use dbInstanceIdentifier. Required for configuring rotation in the console.>`"
}
```

MySQL

```
{
  "engine": "mysql",
  "host": "`<instance host name/resolvable DNS name>`",
  "username": "`<username>`",
  "password": "`<password>`",
  "dbname": "`<database name. If not specified, defaults to None>`",
  "port": `<TCP port number. If not specified, defaults to 3306>`,
  "masterarn": "`<optional: ARN of the elevated secret. Required for the Rotation strategy: alternating users.>`",
  "dbInstanceIdentifier": `<optional: ID of the instance. Alternately, use dbClusterIdentifier. Required for configuring rotation in the console.>`",
  "dbClusterIdentifier": `<optional: ID of the cluster. Alternately, use dbInstanceIdentifier. Required for configuring rotation in the console.>`"
}
```

Oracle

```
{
  "engine": "oracle",
  "host": "`<instance host name/resolvable DNS name>`",
  "username": "`<username>`",
  "password": "`<password>`",
  "dbname": "`<database name>`",
  "port": `<TCP port number. If not specified, defaults to 1521>`,
  "masterarn": "`<optional: ARN of the elevated secret. Required for the Rotation strategy: alternating users.>`",
  "dbInstanceIdentifier": `<optional: ID of the instance. Alternately, use dbClusterIdentifier. Required for configuring rotation in the console.>`",
  "dbClusterIdentifier": `<optional: ID of the cluster. Alternately, use dbInstanceIdentifier. Required for configuring rotation in the console.>`"
}
```

Postgres

```
{
  "engine": "postgres",
  "host": "`<instance host name/resolvable DNS name>`",
  "username": "`<username>`",
  "password": "`<password>`",
  "dbname": "`<database name. If not specified, defaults to 'postgres'>`",
  "port": `<TCP port number. If not specified, defaults to 5432>`,
  "masterarn": "`<optional: ARN of the elevated secret. Required for the Rotation strategy: alternating users.>`",
  "dbInstanceIdentifier": `<optional: ID of the instance. Alternately, use dbClusterIdentifier. Required for configuring rotation in the console.>`",
  "dbClusterIdentifier": `<optional: ID of the cluster. Alternately, use dbInstanceIdentifier. Required for configuring rotation in the console.>`"
}
```

SQLServer

```
{
  "engine": "sqlserver",
  "host": "`<instance host name/resolvable DNS name>`",
  "username": "`<username>`",
  "password": "`<password>`",
  "dbname": "`<database name. If not specified, defaults to 'master'>`",
  "port": `<TCP port number. If not specified, defaults to 1433>`,
  "masterarn": "`<optional: ARN of the elevated secret. Required for the Rotation strategy: alternating users.>`",
  "dbInstanceIdentifier": `<optional: ID of the instance. Alternately, use dbClusterIdentifier. Required for configuring rotation in the console.>`",
  "dbClusterIdentifier": `<optional: ID of the cluster.Alternately, use dbInstanceIdentifier. Required for configuring rotation in the console.>`"
}
```

## Amazon Redshift credentials

To use the [rotation function templates provided by Secrets Manager](reference_available-rotation-templates.md#template-redshift "reference_available-rotation-templates.md#template-redshift"), use the following JSON structure. You can add more key/value pairs, for example to contain connection information for replica databases in other Regions.

```
{
  "engine": "redshift",
  "host": "`<instance host name/resolvable DNS name>`",
  "username": "`<username>`",
  "password": "`<password>`",
  "dbname": "`<database name. If not specified, defaults to None>`",
  "dbClusterIdentifier": "`<optional: database ID. Required for configuring rotation in the console.>`"
  "port": `<optional: TCP port number. If not specified, defaults to 5439>`
  "masterarn": "`<optional: ARN of the elevated secret. Required for the Rotation strategy: alternating users.>`"
}
```

## Amazon Redshift Serverless credentials

To use the [rotation function templates provided by Secrets Manager](reference_available-rotation-templates.md#template-redshift "reference_available-rotation-templates.md#template-redshift"), use the following JSON structure. You can add more key/value pairs, for example to contain connection information for replica databases in other Regions.

```
{
  "engine": "redshift",
  "host": "`<instance host name/resolvable DNS name>`",
  "username": "`<username>`",
  "password": "`<password>`",
  "dbname": "`<database name. If not specified, defaults to None>`",
  "namespaceName": "`<optional: namespace name, Required for configuring rotation in the console.>` "
  "port": `<optional: TCP port number. If not specified, defaults to 5439>`
  "masterarn": "`<optional: ARN of the elevated secret. Required for the Rotation strategy: alternating users.>`"
}
```

## Amazon DocumentDB credentials

To use the [rotation function templates provided by Secrets Manager](reference_available-rotation-templates.md#NON-RDS_rotation_templates "reference_available-rotation-templates.md#NON-RDS_rotation_templates"), use the following JSON structure. You can add more key/value pairs, for example to contain connection information for replica databases in other Regions.

```
{
  "engine": "mongo",
  "host": "`<instance host name/resolvable DNS name>`",
  "username": "`<username>`",
  "password": "`<password>`",
  "dbname": "`<database name. If not specified, defaults to None>`",
  "port": `<TCP port number. If not specified, defaults to 27017>`,
  "ssl": `<true|false. If not specified, defaults to false>`,
  "masterarn": "`<optional: ARN of the elevated secret. Required for the Rotation strategy: alternating users.>`",
  "dbClusterIdentifier": "`<optional: database cluster ID. Alternately, use dbInstanceIdentifier. Required for configuring rotation in the console.>`"
  "dbInstanceIdentifier": "`<optional: database instance ID. Alternately, use dbClusterIdentifier. Required for configuring rotation in the console.>`"
}
```

## Amazon Timestream for InfluxDB secret structure

To rotate Timestream secrets, you can use the [Amazon Timestream for InfluxDB](reference_available-rotation-templates.md#template-TimeStream "reference_available-rotation-templates.md#template-TimeStream") rotation templates.

For more information, see [How Amazon Timestream for InfluxDB uses secrets](../../../timestream/latest/developerguide/timestream-for-influx-security-db-secrets.md "../../../timestream/latest/developerguide/timestream-for-influx-security-db-secrets.md") in the _Amazon Timestream Developer Guide_.

The Timestream secrets must be in the correct JSON structure to be able to use the rotation templates. For more information, see [What's in the secret](../../../timestream/latest/developerguide/timestream-for-influx-security-db-secrets.md#timestream-for-influx-security-db-secrets-definition "../../../timestream/latest/developerguide/timestream-for-influx-security-db-secrets.md#timestream-for-influx-security-db-secrets-definition") in the _Amazon Timestream Developer Guide_.

## Amazon ElastiCache credentials

The following example shows the JSON structure for a secret that stores ElastiCache credentials.

```
{
  "password": "`<password>`",
  "username": "`<username>`"
  "user_arn": "`ARN of the Amazon EC2 user`"
}
```

For more information, see [Automatically rotating passwords for users](../../../AmazonElastiCache/latest/red-ug/User-Secrets-Manager.md "../../../AmazonElastiCache/latest/red-ug/User-Secrets-Manager.md") in the _Amazon ElastiCache User Guide_.

## Active Directory credentials

AWS Directory Service uses secrets to store Active Directory credentials. For more information, see [Seamlessly join an Amazon EC2 Linux instance to your Managed AD Active Directory](../../../directoryservice/latest/admin-guide/seamlessly_join_linux_instance.md "../../../directoryservice/latest/admin-guide/seamlessly_join_linux_instance.md") in the _AWS Directory Service Administration Guide_. Seamless domain join requires the key names in the following examples. If you don't use seamless domain join, you can change the names of the keys in the secret using environment variables as described in the rotation function template code.

To rotate Active Directory secrets, you can use the [Active Directory rotation templates](reference_available-rotation-templates.md#template-AD "reference_available-rotation-templates.md#template-AD").

Active Directory credential

```
{
  "awsSeamlessDomainUsername": "`<username>`",
  "awsSeamlessDomainPassword": "`<password>`"
}
```

If you want to rotate the secret, you include the domain directory ID.

```
{
  "awsSeamlessDomainDirectoryId": "`d-12345abc6e`",
  "awsSeamlessDomainUsername": "`<username>`",
  "awsSeamlessDomainPassword": "`<password>`"
}
```

If the secret is used in conjunction with a secret that contains a keytab, you include the keytab secret ARNs.

```
{
  "awsSeamlessDomainDirectoryId": "`d-12345abc6e`",
  "awsSeamlessDomainUsername": "`<username>`",
  "awsSeamlessDomainPassword": "`<password>`",
  "directoryServiceSecretVersion": `1`,
  "schemaVersion": "`1.0`",
  "keytabArns": [
    "`<ARN of child keytab secret 1>`,
    "`<ARN of child keytab secret 2>`,
    "`<ARN of child keytab secret 3>`,
  ],
  "lastModifiedDateTime": "`2021-07-19 17:06:58`"
}
```

Active Directory keytab
For information about using keytab files to authenticate to Active Directory accounts on Amazon EC2, see [Deploying and configuring Active Directory authentication with SQL Server 2017 on Amazon Linux 2](https://aws.amazon.com/blogs/database/deploying-and-configuring-active-directory-authentication-with-sql-server-2017-on-amazon-linux-2/ "https://aws.amazon.com/blogs/database/deploying-and-configuring-active-directory-authentication-with-sql-server-2017-on-amazon-linux-2/").

```
{
  "awsSeamlessDomainDirectoryId": "`d-12345abc6e`",
  "schemaVersion": "`1.0`",
  "name": "`< name>`",
  "principals": [
    "`aduser@MY.EXAMPLE.COM`",
    "`MSSQLSvc/test:1433@MY.EXAMPLE.COM`"
  ],
  "keytabContents": "`<keytab>`",
  "parentSecretArn": "`<ARN of parent secret>`",
  "lastModifiedDateTime": "`2021-07-19 17:06:58`"
  "version": `1`
}
```

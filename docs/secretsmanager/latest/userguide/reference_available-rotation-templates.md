

# AWS Secrets Manager rotation function templates
<a name="reference_available-rotation-templates"></a>

AWS Secrets Manager provides a set of rotation function templates that help automate the secure management of credentials for various database systems and services. The templates are ready-to-use Lambda functions that implement best practices for credential rotation, helping you maintain your security posture without manual intervention.

The templates support two primary rotation strategies:
+ *Single-user rotation* which updates the credentials for a single user.
+ *Alternating-users rotation* which maintains two separate users to help eliminate downtime during credential changes.

Secrets Manager also provides a generic template that serves as a starting point for any type of secret.

To use the templates, see:
+ [Automatic rotation for database secrets (console)](rotate-secrets_turn-on-for-db.md)
+ [Automatic rotation for non-database secrets (console)](rotate-secrets_turn-on-for-other.md)

To write your own rotation function, see [Write a rotation function](rotate-secrets_lambda-functions.md).

**Contents**
+ [Amazon RDS and Amazon Aurora](#RDS_rotation_templates)
  + [Amazon RDS Db2 single user](#sar-template-db2-singleuser)
  + [Amazon RDS Db2 alternating users](#sar-template-db2-multiuser)
  + [Amazon RDS MariaDB single user](#sar-template-mariadb-singleuser)
  + [Amazon RDS MariaDB alternating users](#sar-template-mariadb-multiuser)
  + [Amazon RDS and Amazon Aurora MySQL single user](#sar-template-mysql-singleuser)
  + [Amazon RDS and Amazon Aurora MySQL alternating users](#sar-template-mysql-multiuser)
  + [Amazon RDS Oracle single user](#sar-template-oracle-singleuser)
  + [Amazon RDS Oracle alternating users](#sar-template-oracle-multiuser)
  + [Amazon RDS and Amazon Aurora PostgreSQL single user](#sar-template-postgre-singleuser)
  + [Amazon RDS and Amazon Aurora PostgreSQL alternating users](#sar-template-postgre-multiuser)
  + [Amazon RDS Microsoft SQLServer single user](#sar-template-sqlserver-singleuser)
  + [Amazon RDS Microsoft SQLServer alternating users](#sar-template-sqlserver-multiuser)
+ [Amazon DocumentDB (with MongoDB compatibility)](#NON-RDS_rotation_templates)
  + [Amazon DocumentDB single user](#sar-template-mongodb-singleuser)
  + [Amazon DocumentDB alternating users](#sar-template-mongodb-multiuser)
+ [Amazon Redshift](#template-redshift)
  + [Amazon Redshift single user](#sar-template-redshift-singleuser)
  + [Amazon Redshift alternating users](#sar-template-redshift-multiuser)
+ [Amazon Timestream for InfluxDB](#template-TimeStream)
  + [Amazon Timestream for InfluxDB single user](#template-TimeStream-singleuser)
  + [Amazon Timestream for InfluxDB alternating users](#template-TimeStream-multiuser)
+ [Amazon ElastiCache](#template-ELC)
+ [Active Directory](#template-AD)
  + [Active Directory credentials](#template-AD-password)
  + [Active Directory keytab](#template-AD-keytab)
+ [Other types of secrets](#OTHER_rotation_templates)

## Amazon RDS and Amazon Aurora
<a name="RDS_rotation_templates"></a>

### Amazon RDS Db2 single user
<a name="sar-template-db2-singleuser"></a>
+ **Template name:** SecretsManagerRDSDb2RotationSingleUser
+ **Rotation strategy:** [Rotation strategy: single user](rotation-strategy.md#rotating-secrets-one-user-one-password).
+ **`SecretString` structure:** [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds).
+ **Source code: **[https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSDb2RotationSingleUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSDb2RotationSingleUser/lambda_function.py)
+ **Dependency: **[python-ibmdb 3.2.8](https://github.com/ibmdb/python-ibmdb)

### Amazon RDS Db2 alternating users
<a name="sar-template-db2-multiuser"></a>
+ **Template name:** SecretsManagerRDSDb2RotationMultiUser
+ **Rotation strategy:** [Rotation strategy: alternating users](rotation-strategy.md#rotating-secrets-two-users).
+ **`SecretString` structure:** [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds).
+ **Source code:** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSDb2RotationMultiUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSDb2RotationMultiUser/lambda_function.py)
+ **Dependency: **[python-ibmdb 3.2.8](https://github.com/ibmdb/python-ibmdb)

### Amazon RDS MariaDB single user
<a name="sar-template-mariadb-singleuser"></a>
+ **Template name:** SecretsManagerRDSMariaDBRotationSingleUser
+ **Rotation strategy:** [Rotation strategy: single user](rotation-strategy.md#rotating-secrets-one-user-one-password).
+ **`SecretString` structure:** [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds).
+ **Source code: **[https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMariaDBRotationSingleUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMariaDBRotationSingleUser/lambda_function.py)
+ **Dependency: **[PyMySQL 1.1.1](https://github.com/PyMySQL/PyMySQL). If you use sha256 password for authentication, PyMySQL[rsa]. For information about using packages with compiled code in a Lambda runtime, see [How do I add Python packages with compiled binaries to my deployment package and make the package compatible with Lambda?](https://repost.aws/knowledge-center/lambda-python-package-compatible) in *AWS Knowledge Center*.

### Amazon RDS MariaDB alternating users
<a name="sar-template-mariadb-multiuser"></a>
+ **Template name:** SecretsManagerRDSMariaDBRotationMultiUser
+ **Rotation strategy:** [Rotation strategy: alternating users](rotation-strategy.md#rotating-secrets-two-users).
+ **`SecretString` structure:** [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds).
+ **Source code:** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMariaDBRotationMultiUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMariaDBRotationMultiUser/lambda_function.py)
+ **Dependency: **[PyMySQL 1.1.1](https://github.com/PyMySQL/PyMySQL). If you use sha256 password for authentication, PyMySQL[rsa]. For information about using packages with compiled code in a Lambda runtime, see [How do I add Python packages with compiled binaries to my deployment package and make the package compatible with Lambda?](https://repost.aws/knowledge-center/lambda-python-package-compatible) in *AWS Knowledge Center*.

### Amazon RDS and Amazon Aurora MySQL single user
<a name="sar-template-mysql-singleuser"></a>
+ **Template name:** SecretsManagerRDSMySQLRotationSingleUser
+ **Rotation strategy:** [Rotation strategy: single user](rotation-strategy.md#rotating-secrets-one-user-one-password).
+ **Expected `SecretString` structure:** [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds).
+ **Source code:** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMySQLRotationSingleUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMySQLRotationSingleUser/lambda_function.py)
+ **Dependency: **[PyMySQL 1.1.1](https://github.com/PyMySQL/PyMySQL). If you use sha256 password for authentication, PyMySQL[rsa]. For information about using packages with compiled code in a Lambda runtime, see [How do I add Python packages with compiled binaries to my deployment package and make the package compatible with Lambda?](https://repost.aws/knowledge-center/lambda-python-package-compatible) in *AWS Knowledge Center*.

### Amazon RDS and Amazon Aurora MySQL alternating users
<a name="sar-template-mysql-multiuser"></a>
+ **Template name:** SecretsManagerRDSMySQLRotationMultiUser
+ **Rotation strategy:** [Rotation strategy: alternating users](rotation-strategy.md#rotating-secrets-two-users).
+ **Expected `SecretString` structure:** [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds).
+ **Source code: ** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMySQLRotationMultiUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMySQLRotationMultiUser/lambda_function.py)
+ **Dependency: **[PyMySQL 1.1.1](https://github.com/PyMySQL/PyMySQL). If you use sha256 password for authentication, PyMySQL[rsa]. For information about using packages with compiled code in a Lambda runtime, see [How do I add Python packages with compiled binaries to my deployment package and make the package compatible with Lambda?](https://repost.aws/knowledge-center/lambda-python-package-compatible) in *AWS Knowledge Center*.

### Amazon RDS Oracle single user
<a name="sar-template-oracle-singleuser"></a>
+ **Template name:** SecretsManagerRDSOracleRotationSingleUser
+ **Rotation strategy:** [Rotation strategy: single user](rotation-strategy.md#rotating-secrets-one-user-one-password).
+ **Expected `SecretString` structure:** [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds).
+ **Source code: **[https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSOracleRotationSingleUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSOracleRotationSingleUser/lambda_function.py)
+ **Dependency: **[python-oracledb 2.4.1](https://github.com/oracle/python-oracledb)

### Amazon RDS Oracle alternating users
<a name="sar-template-oracle-multiuser"></a>
+ **Template name:** SecretsManagerRDSOracleRotationMultiUser
+ **Rotation strategy:** [Rotation strategy: alternating users](rotation-strategy.md#rotating-secrets-two-users).
+ **Expected `SecretString` structure:** [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds).
+ **Source code: **[https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSOracleRotationMultiUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSOracleRotationMultiUser/lambda_function.py)
+ **Dependency: **[python-oracledb 2.4.1](https://github.com/oracle/python-oracledb)

### Amazon RDS and Amazon Aurora PostgreSQL single user
<a name="sar-template-postgre-singleuser"></a>
+ **Template name:** SecretsManagerRDSPostgreSQLRotationSingleUser
+ **Rotation strategy:** [Rotation strategy: single user](rotation-strategy.md#rotating-secrets-one-user-one-password).
+ **Expected `SecretString` structure:** [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds).
+ **Source code: **[https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSPostgreSQLRotationSingleUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSPostgreSQLRotationSingleUser/lambda_function.py)
+ **Dependency: **[PyGreSQL 6.1.0](https://github.com/PyGreSQL/PyGreSQL)

### Amazon RDS and Amazon Aurora PostgreSQL alternating users
<a name="sar-template-postgre-multiuser"></a>
+ **Template name:** SecretsManagerRDSPostgreSQLRotationMultiUser
+ **Rotation strategy:** [Rotation strategy: alternating users](rotation-strategy.md#rotating-secrets-two-users).
+ **Expected `SecretString` structure:** [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds).
+ **Source code: **[https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSPostgreSQLRotationMultiUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSPostgreSQLRotationMultiUser/lambda_function.py)
+ **Dependency: **[PyGreSQL 6.1.0](https://github.com/PyGreSQL/PyGreSQL)

### Amazon RDS Microsoft SQLServer single user
<a name="sar-template-sqlserver-singleuser"></a>
+ **Template name:** SecretsManagerRDSSQLServerRotationSingleUser
+ **Rotation strategy:** [Rotation strategy: single user](rotation-strategy.md#rotating-secrets-one-user-one-password).
+ **Expected `SecretString` structure:** [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds).
+ **Source code: **[https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSSQLServerRotationSingleUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSSQLServerRotationSingleUser/lambda_function.py)
+ **Dependency: **[Pymssql 2.3.11](https://github.com/Pymssql/Pymssql)

### Amazon RDS Microsoft SQLServer alternating users
<a name="sar-template-sqlserver-multiuser"></a>
+ **Template name:** SecretsManagerRDSSQLServerRotationMultiUser
+ **Rotation strategy:** [Rotation strategy: alternating users](rotation-strategy.md#rotating-secrets-two-users).
+ **Expected `SecretString` structure:** [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds).
+ **Source code: **[https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSSQLServerRotationMultiUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSSQLServerRotationMultiUser/lambda_function.py)
+ **Dependency: **[Pymssql 2.3.11](https://github.com/Pymssql/Pymssql)

## Amazon DocumentDB (with MongoDB compatibility)
<a name="NON-RDS_rotation_templates"></a>

### Amazon DocumentDB single user
<a name="sar-template-mongodb-singleuser"></a>
+ **Template name:** SecretsManagerMongoDBRotationSingleUser
+ **Rotation strategy:** [Rotation strategy: single user](rotation-strategy.md#rotating-secrets-one-user-one-password).
+ **Expected `SecretString` structure:** [Amazon DocumentDB credentials](reference_secret_json_structure.md#reference_secret_json_structure_docdb).
+ **Source code:** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerMongoDBRotationSingleUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerMongoDBRotationSingleUser/lambda_function.py)
+ **Dependency: **[PyMongo 4.7.3](https://github.com/mongodb/mongo-python-driver)

### Amazon DocumentDB alternating users
<a name="sar-template-mongodb-multiuser"></a>
+ **Template name:** SecretsManagerMongoDBRotationMultiUser
+ **Rotation strategy:** [Rotation strategy: alternating users](rotation-strategy.md#rotating-secrets-two-users).
+ **Expected `SecretString` structure:** [Amazon DocumentDB credentials](reference_secret_json_structure.md#reference_secret_json_structure_docdb).
+ **Source code: ** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerMongoDBRotationMultiUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerMongoDBRotationMultiUser/lambda_function.py)
+ **Dependency: **[PyMongo 4.7.3](https://github.com/mongodb/mongo-python-driver)

## Amazon Redshift
<a name="template-redshift"></a>

### Amazon Redshift single user
<a name="sar-template-redshift-singleuser"></a>
+ **Template name:** SecretsManagerRedshiftRotationSingleUser
+ **Rotation strategy:** [Rotation strategy: single user](rotation-strategy.md#rotating-secrets-one-user-one-password).
+ **Expected `SecretString` structure:** [Amazon Redshift credentials](reference_secret_json_structure.md#reference_secret_json_structure_RS).
+ **Source code: ** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRedshiftRotationSingleUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRedshiftRotationSingleUser/lambda_function.py)
+ **Dependency: **[redshift-connector 2.1.13](https://github.com/aws/amazon-redshift-python-driver)

### Amazon Redshift alternating users
<a name="sar-template-redshift-multiuser"></a>
+ **Template name:** SecretsManagerRedshiftRotationMultiUser
+ **Rotation strategy:** [Rotation strategy: alternating users](rotation-strategy.md#rotating-secrets-two-users).
+ **Expected `SecretString` structure:** [Amazon Redshift credentials](reference_secret_json_structure.md#reference_secret_json_structure_RS).
+ **Source code: ** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRedshiftRotationMultiUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRedshiftRotationMultiUser/lambda_function.py)
+ **Dependency: **[redshift-connector 2.1.13](https://github.com/aws/amazon-redshift-python-driver)

## Amazon Timestream for InfluxDB
<a name="template-TimeStream"></a>

To use these templates, see [How Amazon Timestream for InfluxDB uses secrets](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influx-security-db-secrets.html) in the *Amazon Timestream Developer Guide*.

### Amazon Timestream for InfluxDB single user
<a name="template-TimeStream-singleuser"></a>
+ **Template name:** SecretsManagerInfluxDBRotationSingleUser
+ **Expected `SecretString` structure:** [Amazon Timestream for InfluxDB secret structure](reference_secret_json_structure.md#reference_secret_json_structure_TIME).
+ **Source code: ** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerInfluxDBRotationSingleUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerInfluxDBRotationSingleUser/lambda_function.py)
+ **Dependency: **InfluxDB 2.0 python client

### Amazon Timestream for InfluxDB alternating users
<a name="template-TimeStream-multiuser"></a>
+ **Template name:** SecretsManagerInfluxDBRotationMultiUser
+ **Expected `SecretString` structure:** [Amazon Timestream for InfluxDB secret structure](reference_secret_json_structure.md#reference_secret_json_structure_TIME).
+ **Source code: ** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerInfluxDBRotationMultiUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerInfluxDBRotationMultiUser/lambda_function.py)
+ **Dependency: **InfluxDB 2.0 python client

## Amazon ElastiCache
<a name="template-ELC"></a>

To use this template, see [Automatically rotating passwords for users](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/User-Secrets-Manager.html) in the *Amazon ElastiCache User Guide*.
+ **Template name:** SecretsManagerElasticacheUserRotation
+ **Expected `SecretString` structure:** [Amazon ElastiCache credentials](reference_secret_json_structure.md#reference_secret_json_structure_ELC).
+ **Source code: ** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerElasticacheUserRotation/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerElasticacheUserRotation/lambda_function.py)

## Active Directory
<a name="template-AD"></a>

### Active Directory credentials
<a name="template-AD-password"></a>
+ **Template name:** SecretsManagerActiveDirectoryRotationSingleUser
+ **Expected `SecretString` structure:** [Active Directory credentials](reference_secret_json_structure.md#reference_secret_json_structure_AD).
+ **Source code: ** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerActiveDirectoryRotationSingleUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerActiveDirectoryRotationSingleUser/lambda_function.py)

### Active Directory keytab
<a name="template-AD-keytab"></a>
+ **Template name:** SecretsManagerActiveDirectoryAndKeytabRotationSingleUser
+ **Expected `SecretString` structure:** [Active Directory credentials](reference_secret_json_structure.md#reference_secret_json_structure_AD).
+ **Source code: ** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerActiveDirectoryAndKeytabRotationSingleUser/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerActiveDirectoryAndKeytabRotationSingleUser/lambda_function.py)
+ **Dependencies:** msktutil

## Other types of secrets
<a name="OTHER_rotation_templates"></a>

Secrets Manager provides this template as a starting point for you to create a rotation function for any type of secret.
+ **Template name:** SecretsManagerRotationTemplate
+ **Source code: ** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRotationTemplate/lambda\_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRotationTemplate/lambda_function.py)
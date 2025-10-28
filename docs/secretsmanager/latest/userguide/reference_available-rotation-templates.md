# AWS Secrets Manager rotation function

templates

AWS Secrets Manager provides a set of rotation function templates that help automate the secure
management of credentials for various database systems and services. The templates are
ready-to-use Lambda functions that implement best practices for credential rotation, helping you
maintain your security posture without manual intervention.

The templates support two primary rotation strategies:

- _Single-user rotation_ which updates the credentials for a single
  user.
- _Alternating-users rotation_ which maintains two separate users to
  help eliminate downtime during credential changes.
  Secrets Manager also provides a generic template that serves as a starting point for any type of
  secret.

To use the templates, see:

- [Automatic rotation for database secrets (console)](rotate-secrets_turn-on-for-db.md "rotate-secrets_turn-on-for-db.md")
- [Automatic rotation for
  non-database secrets (console)](rotate-secrets_turn-on-for-other.md "rotate-secrets_turn-on-for-other.md")
  To write your own rotation function, see [Write a rotation function](rotate-secrets_lambda-functions.md "rotate-secrets_lambda-functions.md").

###### Templates

- [Amazon RDS and Amazon Aurora](reference_available-rotation-templates.md#RDS_rotation_templates "reference_available-rotation-templates.md#RDS_rotation_templates")
  - [Amazon RDS Db2 single user](reference_available-rotation-templates.md#sar-template-db2-singleuser "reference_available-rotation-templates.md#sar-template-db2-singleuser")
  - [Amazon RDS Db2 alternating users](reference_available-rotation-templates.md#sar-template-db2-multiuser "reference_available-rotation-templates.md#sar-template-db2-multiuser")
  - [Amazon RDS MariaDB single user](reference_available-rotation-templates.md#sar-template-mariadb-singleuser "reference_available-rotation-templates.md#sar-template-mariadb-singleuser")
  - [Amazon RDS MariaDB alternating users](reference_available-rotation-templates.md#sar-template-mariadb-multiuser "reference_available-rotation-templates.md#sar-template-mariadb-multiuser")
  - [Amazon RDS and Amazon Aurora MySQL single
    user](reference_available-rotation-templates.md#sar-template-mysql-singleuser "reference_available-rotation-templates.md#sar-template-mysql-singleuser")
  - [Amazon RDS and Amazon Aurora MySQL alternating
    users](reference_available-rotation-templates.md#sar-template-mysql-multiuser "reference_available-rotation-templates.md#sar-template-mysql-multiuser")
  - [Amazon RDS Oracle single user](reference_available-rotation-templates.md#sar-template-oracle-singleuser "reference_available-rotation-templates.md#sar-template-oracle-singleuser")
  - [Amazon RDS Oracle alternating users](reference_available-rotation-templates.md#sar-template-oracle-multiuser "reference_available-rotation-templates.md#sar-template-oracle-multiuser")
  - [Amazon RDS and Amazon Aurora PostgreSQL single
    user](reference_available-rotation-templates.md#sar-template-postgre-singleuser "reference_available-rotation-templates.md#sar-template-postgre-singleuser")
  - [Amazon RDS and Amazon Aurora PostgreSQL alternating
    users](reference_available-rotation-templates.md#sar-template-postgre-multiuser "reference_available-rotation-templates.md#sar-template-postgre-multiuser")
  - [Amazon RDS Microsoft SQLServer single
    user](reference_available-rotation-templates.md#sar-template-sqlserver-singleuser "reference_available-rotation-templates.md#sar-template-sqlserver-singleuser")
  - [Amazon RDS Microsoft SQLServer alternating
    users](reference_available-rotation-templates.md#sar-template-sqlserver-multiuser "reference_available-rotation-templates.md#sar-template-sqlserver-multiuser")

- [Amazon DocumentDB (with MongoDB compatibility)](reference_available-rotation-templates.md#NON-RDS_rotation_templates "reference_available-rotation-templates.md#NON-RDS_rotation_templates")
  - [Amazon DocumentDB single user](reference_available-rotation-templates.md#sar-template-mongodb-singleuser "reference_available-rotation-templates.md#sar-template-mongodb-singleuser")
  - [Amazon DocumentDB alternating users](reference_available-rotation-templates.md#sar-template-mongodb-multiuser "reference_available-rotation-templates.md#sar-template-mongodb-multiuser")

- [Amazon Redshift](reference_available-rotation-templates.md#template-redshift "reference_available-rotation-templates.md#template-redshift")
  - [Amazon Redshift single user](reference_available-rotation-templates.md#sar-template-redshift-singleuser "reference_available-rotation-templates.md#sar-template-redshift-singleuser")
  - [Amazon Redshift alternating users](reference_available-rotation-templates.md#sar-template-redshift-multiuser "reference_available-rotation-templates.md#sar-template-redshift-multiuser")

- [Amazon Timestream for InfluxDB](reference_available-rotation-templates.md#template-TimeStream "reference_available-rotation-templates.md#template-TimeStream")
  - [Amazon Timestream for InfluxDB single user](reference_available-rotation-templates.md#template-TimeStream-singleuser "reference_available-rotation-templates.md#template-TimeStream-singleuser")
  - [Amazon Timestream for InfluxDB alternating
    users](reference_available-rotation-templates.md#template-TimeStream-multiuser "reference_available-rotation-templates.md#template-TimeStream-multiuser")

- [Amazon ElastiCache](reference_available-rotation-templates.md#template-ELC "reference_available-rotation-templates.md#template-ELC")
- [Active Directory](reference_available-rotation-templates.md#template-AD "reference_available-rotation-templates.md#template-AD")
  - [Active Directory credentials](reference_available-rotation-templates.md#template-AD-password "reference_available-rotation-templates.md#template-AD-password")
  - [Active Directory keytab](reference_available-rotation-templates.md#template-AD-keytab "reference_available-rotation-templates.md#template-AD-keytab")

- [Other types of secrets](reference_available-rotation-templates.md#OTHER_rotation_templates "reference_available-rotation-templates.md#OTHER_rotation_templates")

## Amazon RDS and Amazon Aurora

### Amazon RDS Db2 single user

- **Template name:**
  SecretsManagerRDSDb2RotationSingleUser
- **Rotation strategy:**
  [Rotation strategy: single user](rotation-strategy.md#rotating-secrets-one-user-one-password "rotation-strategy.md#rotating-secrets-one-user-one-password").
- **`SecretString` structure:**
  [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds "reference_secret_json_structure.md#reference_secret_json_structure_rds").
- **Source code:** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSDb2RotationSingleUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSDb2RotationSingleUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSDb2RotationSingleUser/lambda_function.py")
- **Dependency:** [python-ibmdb](https://github.com/ibmdb/python-ibmdb "https://github.com/ibmdb/python-ibmdb")

### Amazon RDS Db2 alternating users

- **Template name:**
  SecretsManagerRDSDb2RotationMultiUser
- **Rotation strategy:**
  [Rotation strategy: alternating users](rotation-strategy.md#rotating-secrets-two-users "rotation-strategy.md#rotating-secrets-two-users").
- **`SecretString` structure:**
  [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds "reference_secret_json_structure.md#reference_secret_json_structure_rds").
- **Source code:**
  [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSDb2RotationMultiUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSDb2RotationMultiUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSDb2RotationMultiUser/lambda_function.py")
- **Dependency:** [python-ibmdb](https://github.com/ibmdb/python-ibmdb "https://github.com/ibmdb/python-ibmdb")

### Amazon RDS MariaDB single user

- **Template name:**
  SecretsManagerRDSMariaDBRotationSingleUser
- **Rotation strategy:**
  [Rotation strategy: single user](rotation-strategy.md#rotating-secrets-one-user-one-password "rotation-strategy.md#rotating-secrets-one-user-one-password").
- **`SecretString` structure:**
  [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds "reference_secret_json_structure.md#reference_secret_json_structure_rds").
- **Source code:** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMariaDBRotationSingleUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMariaDBRotationSingleUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMariaDBRotationSingleUser/lambda_function.py")
- **Dependency:** PyMySQL 1.0.2. If you use sha256
  password for authentication, PyMySQL[rsa]. For information about using packages with
  compiled code in a Lambda runtime, see [How do I
  add Python packages with compiled binaries to my deployment package and make the
  package compatible with Lambda?](https://repost.aws/knowledge-center/lambda-python-package-compatible "https://repost.aws/knowledge-center/lambda-python-package-compatible") in _AWS Knowledge
  Center_.

### Amazon RDS MariaDB alternating users

- **Template name:**
  SecretsManagerRDSMariaDBRotationMultiUser
- **Rotation strategy:**
  [Rotation strategy: alternating users](rotation-strategy.md#rotating-secrets-two-users "rotation-strategy.md#rotating-secrets-two-users").
- **`SecretString` structure:**
  [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds "reference_secret_json_structure.md#reference_secret_json_structure_rds").
- **Source code:**
  [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMariaDBRotationMultiUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMariaDBRotationMultiUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMariaDBRotationMultiUser/lambda_function.py")
- **Dependency:** PyMySQL 1.0.2. If you use sha256
  password for authentication, PyMySQL[rsa]. For information about using packages with
  compiled code in a Lambda runtime, see [How do I
  add Python packages with compiled binaries to my deployment package and make the
  package compatible with Lambda?](https://repost.aws/knowledge-center/lambda-python-package-compatible "https://repost.aws/knowledge-center/lambda-python-package-compatible") in _AWS Knowledge
  Center_.

### Amazon RDS and Amazon Aurora MySQL single

user

- **Template name:**
  SecretsManagerRDSMySQLRotationSingleUser
- **Rotation strategy:**
  [Rotation strategy: single user](rotation-strategy.md#rotating-secrets-one-user-one-password "rotation-strategy.md#rotating-secrets-one-user-one-password").
- **Expected `SecretString` structure:**
  [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds "reference_secret_json_structure.md#reference_secret_json_structure_rds").
- **Source code:**
  [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMySQLRotationSingleUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMySQLRotationSingleUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMySQLRotationSingleUser/lambda_function.py")
- **Dependency:** PyMySQL 1.0.2. If you use sha256
  password for authentication, PyMySQL[rsa]. For information about using packages with
  compiled code in a Lambda runtime, see [How do I
  add Python packages with compiled binaries to my deployment package and make the
  package compatible with Lambda?](https://repost.aws/knowledge-center/lambda-python-package-compatible "https://repost.aws/knowledge-center/lambda-python-package-compatible") in _AWS Knowledge
  Center_.

### Amazon RDS and Amazon Aurora MySQL alternating

users

- **Template name:**
  SecretsManagerRDSMySQLRotationMultiUser
- **Rotation strategy:**
  [Rotation strategy: alternating users](rotation-strategy.md#rotating-secrets-two-users "rotation-strategy.md#rotating-secrets-two-users").
- **Expected `SecretString` structure:**
  [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds "reference_secret_json_structure.md#reference_secret_json_structure_rds").
- **Source code:**
  [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMySQLRotationMultiUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMySQLRotationMultiUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSMySQLRotationMultiUser/lambda_function.py")
- **Dependency:** PyMySQL 1.0.2. If you use sha256
  password for authentication, PyMySQL[rsa]. For information about using packages with
  compiled code in a Lambda runtime, see [How do I
  add Python packages with compiled binaries to my deployment package and make the
  package compatible with Lambda?](https://repost.aws/knowledge-center/lambda-python-package-compatible "https://repost.aws/knowledge-center/lambda-python-package-compatible") in _AWS Knowledge
  Center_.

### Amazon RDS Oracle single user

- **Template name:**
  SecretsManagerRDSOracleRotationSingleUser
- **Rotation strategy:**
  [Rotation strategy: single user](rotation-strategy.md#rotating-secrets-one-user-one-password "rotation-strategy.md#rotating-secrets-one-user-one-password").
- **Expected `SecretString` structure:**
  [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds "reference_secret_json_structure.md#reference_secret_json_structure_rds").
- **Source code:** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSOracleRotationSingleUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSOracleRotationSingleUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSOracleRotationSingleUser/lambda_function.py")
- **Dependency:** [python-oracledb 2.4.1](https://github.com/oracle/python-oracledb "https://github.com/oracle/python-oracledb")

### Amazon RDS Oracle alternating users

- **Template name:**
  SecretsManagerRDSOracleRotationMultiUser
- **Rotation strategy:**
  [Rotation strategy: alternating users](rotation-strategy.md#rotating-secrets-two-users "rotation-strategy.md#rotating-secrets-two-users").
- **Expected `SecretString` structure:**
  [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds "reference_secret_json_structure.md#reference_secret_json_structure_rds").
- **Source code:** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSOracleRotationMultiUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSOracleRotationMultiUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSOracleRotationMultiUser/lambda_function.py")
- **Dependency:** [python-oracledb 2.4.1](https://github.com/oracle/python-oracledb "https://github.com/oracle/python-oracledb")

### Amazon RDS and Amazon Aurora PostgreSQL single

user

- **Template name:**
  SecretsManagerRDSPostgreSQLRotationSingleUser
- **Rotation strategy:**
  [Rotation strategy: single user](rotation-strategy.md#rotating-secrets-one-user-one-password "rotation-strategy.md#rotating-secrets-one-user-one-password").
- **Expected `SecretString` structure:**
  [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds "reference_secret_json_structure.md#reference_secret_json_structure_rds").
- **Source code:** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSPostgreSQLRotationSingleUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSPostgreSQLRotationSingleUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSPostgreSQLRotationSingleUser/lambda_function.py")
- **Dependency:** PyGreSQL 5.2.5

### Amazon RDS and Amazon Aurora PostgreSQL alternating

users

- **Template name:**
  SecretsManagerRDSPostgreSQLRotationMultiUser
- **Rotation strategy:**
  [Rotation strategy: alternating users](rotation-strategy.md#rotating-secrets-two-users "rotation-strategy.md#rotating-secrets-two-users").
- **Expected `SecretString` structure:**
  [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds "reference_secret_json_structure.md#reference_secret_json_structure_rds").
- **Source code:** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSPostgreSQLRotationMultiUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSPostgreSQLRotationMultiUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSPostgreSQLRotationMultiUser/lambda_function.py")
- **Dependency:** PyGreSQL 5.2.5

### Amazon RDS Microsoft SQLServer single

user

- **Template name:**
  SecretsManagerRDSSQLServerRotationSingleUser
- **Rotation strategy:**
  [Rotation strategy: single user](rotation-strategy.md#rotating-secrets-one-user-one-password "rotation-strategy.md#rotating-secrets-one-user-one-password").
- **Expected `SecretString` structure:**
  [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds "reference_secret_json_structure.md#reference_secret_json_structure_rds").
- **Source code:** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSSQLServerRotationSingleUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSSQLServerRotationSingleUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSSQLServerRotationSingleUser/lambda_function.py")
- **Dependency:** Pymssql 2.2.2

### Amazon RDS Microsoft SQLServer alternating

users

- **Template name:**
  SecretsManagerRDSSQLServerRotationMultiUser
- **Rotation strategy:**
  [Rotation strategy: alternating users](rotation-strategy.md#rotating-secrets-two-users "rotation-strategy.md#rotating-secrets-two-users").
- **Expected `SecretString` structure:**
  [Amazon RDS and Aurora credentials](reference_secret_json_structure.md#reference_secret_json_structure_rds "reference_secret_json_structure.md#reference_secret_json_structure_rds").
- **Source code:** [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSSQLServerRotationMultiUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSSQLServerRotationMultiUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRDSSQLServerRotationMultiUser/lambda_function.py")
- **Dependency:** Pymssql 2.2.2

## Amazon DocumentDB (with MongoDB compatibility)

### Amazon DocumentDB single user

- **Template name:**
  SecretsManagerMongoDBRotationSingleUser
- **Rotation strategy:**
  [Rotation strategy: single user](rotation-strategy.md#rotating-secrets-one-user-one-password "rotation-strategy.md#rotating-secrets-one-user-one-password").
- **Expected `SecretString` structure:**
  [Amazon DocumentDB credentials](reference_secret_json_structure.md#reference_secret_json_structure_docdb "reference_secret_json_structure.md#reference_secret_json_structure_docdb").
- **Source code:**
  [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerMongoDBRotationSingleUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerMongoDBRotationSingleUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerMongoDBRotationSingleUser/lambda_function.py")
- **Dependency:** PyMongo 4.2.0

### Amazon DocumentDB alternating users

- **Template name:**
  SecretsManagerMongoDBRotationMultiUser
- **Rotation strategy:**
  [Rotation strategy: alternating users](rotation-strategy.md#rotating-secrets-two-users "rotation-strategy.md#rotating-secrets-two-users").
- **Expected `SecretString` structure:**
  [Amazon DocumentDB credentials](reference_secret_json_structure.md#reference_secret_json_structure_docdb "reference_secret_json_structure.md#reference_secret_json_structure_docdb").
- **Source code:**
  [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerMongoDBRotationMultiUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerMongoDBRotationMultiUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerMongoDBRotationMultiUser/lambda_function.py")
- **Dependency:** PyMongo 4.2.0

## Amazon Redshift

### Amazon Redshift single user

- **Template name:**
  SecretsManagerRedshiftRotationSingleUser
- **Rotation strategy:**
  [Rotation strategy: single user](rotation-strategy.md#rotating-secrets-one-user-one-password "rotation-strategy.md#rotating-secrets-one-user-one-password").
- **Expected `SecretString` structure:**
  [Amazon Redshift credentials](reference_secret_json_structure.md#reference_secret_json_structure_RS "reference_secret_json_structure.md#reference_secret_json_structure_RS").
- **Source code:**
  [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRedshiftRotationSingleUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRedshiftRotationSingleUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRedshiftRotationSingleUser/lambda_function.py")
- **Dependency:** PyGreSQL 5.2.5

### Amazon Redshift alternating users

- **Template name:**
  SecretsManagerRedshiftRotationMultiUser
- **Rotation strategy:**
  [Rotation strategy: alternating users](rotation-strategy.md#rotating-secrets-two-users "rotation-strategy.md#rotating-secrets-two-users").
- **Expected `SecretString` structure:**
  [Amazon Redshift credentials](reference_secret_json_structure.md#reference_secret_json_structure_RS "reference_secret_json_structure.md#reference_secret_json_structure_RS").
- **Source code:**
  [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRedshiftRotationMultiUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRedshiftRotationMultiUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRedshiftRotationMultiUser/lambda_function.py")
- **Dependency:** PyGreSQL 5.2.5

## Amazon Timestream for InfluxDB

To use these templates, see [How
Amazon Timestream for InfluxDB uses secrets](../../../timestream/latest/developerguide/timestream-for-influx-security-db-secrets.md "../../../timestream/latest/developerguide/timestream-for-influx-security-db-secrets.md") in the _Amazon Timestream Developer
Guide_.

### Amazon Timestream for InfluxDB single user

- **Template name:**
  SecretsManagerInfluxDBRotationSingleUser
- **Expected `SecretString` structure:**
  [Amazon Timestream for InfluxDB secret structure](reference_secret_json_structure.md#reference_secret_json_structure_TIME "reference_secret_json_structure.md#reference_secret_json_structure_TIME").
- **Source code:**
  [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerInfluxDBRotationSingleUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerInfluxDBRotationSingleUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerInfluxDBRotationSingleUser/lambda_function.py")
- **Dependency:** InfluxDB 2.0 python client

### Amazon Timestream for InfluxDB alternating

users

- **Template name:**
  SecretsManagerInfluxDBRotationMultiUser
- **Expected `SecretString` structure:**
  [Amazon Timestream for InfluxDB secret structure](reference_secret_json_structure.md#reference_secret_json_structure_TIME "reference_secret_json_structure.md#reference_secret_json_structure_TIME").
- **Source code:**
  [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerInfluxDBRotationMultiUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerInfluxDBRotationMultiUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerInfluxDBRotationMultiUser/lambda_function.py")
- **Dependency:** InfluxDB 2.0 python client

## Amazon ElastiCache

To use this template, see [Automatically rotating
passwords for users](../../../AmazonElastiCache/latest/red-ug/User-Secrets-Manager.md "../../../AmazonElastiCache/latest/red-ug/User-Secrets-Manager.md") in the _Amazon ElastiCache User Guide_.

- **Template name:**
  SecretsManagerElasticacheUserRotation
- **Expected `SecretString` structure:**
  [Amazon ElastiCache credentials](reference_secret_json_structure.md#reference_secret_json_structure_ELC "reference_secret_json_structure.md#reference_secret_json_structure_ELC").
- **Source code:**
  [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerElasticacheUserRotation/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerElasticacheUserRotation/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerElasticacheUserRotation/lambda_function.py")

## Active Directory

### Active Directory credentials

- **Template name:**
  SecretsManagerActiveDirectoryRotationSingleUser
- **Expected `SecretString` structure:**
  [Active Directory credentials](reference_secret_json_structure.md#reference_secret_json_structure_AD "reference_secret_json_structure.md#reference_secret_json_structure_AD").
- **Source code:**
  [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerActiveDirectoryRotationSingleUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerActiveDirectoryRotationSingleUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerActiveDirectoryRotationSingleUser/lambda_function.py")

### Active Directory keytab

- **Template name:**
  SecretsManagerActiveDirectoryAndKeytabRotationSingleUser
- **Expected `SecretString` structure:**
  [Active Directory credentials](reference_secret_json_structure.md#reference_secret_json_structure_AD "reference_secret_json_structure.md#reference_secret_json_structure_AD").
- **Source code:**
  [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerActiveDirectoryAndKeytabRotationSingleUser/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerActiveDirectoryAndKeytabRotationSingleUser/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerActiveDirectoryAndKeytabRotationSingleUser/lambda_function.py")
- **Dependencies:** msktutil

## Other types of secrets

Secrets Manager provides this template as a starting point for you to create a rotation function for
any type of secret.

- **Template name:** SecretsManagerRotationTemplate
- **Source code:**
  [https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRotationTemplate/lambda_function.py](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRotationTemplate/lambda_function.py "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas/tree/master/SecretsManagerRotationTemplate/lambda_function.py")

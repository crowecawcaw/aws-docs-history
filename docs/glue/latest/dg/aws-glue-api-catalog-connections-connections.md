# Connection API

The Connection API describes AWS Glue connection data types,
and the API for creating, deleting, updating, and listing connections.

## Data types

- [Connection structure](#aws-glue-api-catalog-connections-connections-Connection "#aws-glue-api-catalog-connections-connections-Connection")
- [ConnectionInput structure](#aws-glue-api-catalog-connections-connections-ConnectionInput "#aws-glue-api-catalog-connections-connections-ConnectionInput")
- [TestConnectionInput structure](#aws-glue-api-catalog-connections-connections-TestConnectionInput "#aws-glue-api-catalog-connections-connections-TestConnectionInput")
- [PhysicalConnectionRequirements structure](#aws-glue-api-catalog-connections-connections-PhysicalConnectionRequirements "#aws-glue-api-catalog-connections-connections-PhysicalConnectionRequirements")
- [GetConnectionsFilter structure](#aws-glue-api-catalog-connections-connections-GetConnectionsFilter "#aws-glue-api-catalog-connections-connections-GetConnectionsFilter")
- [AuthenticationConfiguration structure](#aws-glue-api-catalog-connections-connections-AuthenticationConfiguration "#aws-glue-api-catalog-connections-connections-AuthenticationConfiguration")
- [AuthenticationConfigurationInput structure](#aws-glue-api-catalog-connections-connections-AuthenticationConfigurationInput "#aws-glue-api-catalog-connections-connections-AuthenticationConfigurationInput")
- [OAuth2Properties structure](#aws-glue-api-catalog-connections-connections-OAuth2Properties "#aws-glue-api-catalog-connections-connections-OAuth2Properties")
- [OAuth2PropertiesInput structure](#aws-glue-api-catalog-connections-connections-OAuth2PropertiesInput "#aws-glue-api-catalog-connections-connections-OAuth2PropertiesInput")
- [OAuth2ClientApplication structure](#aws-glue-api-catalog-connections-connections-OAuth2ClientApplication "#aws-glue-api-catalog-connections-connections-OAuth2ClientApplication")
- [AuthorizationCodeProperties structure](#aws-glue-api-catalog-connections-connections-AuthorizationCodeProperties "#aws-glue-api-catalog-connections-connections-AuthorizationCodeProperties")
- [BasicAuthenticationCredentials structure](#aws-glue-api-catalog-connections-connections-BasicAuthenticationCredentials "#aws-glue-api-catalog-connections-connections-BasicAuthenticationCredentials")
- [OAuth2Credentials structure](#aws-glue-api-catalog-connections-connections-OAuth2Credentials "#aws-glue-api-catalog-connections-connections-OAuth2Credentials")

## Connection structure

Defines a connection to a data source.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the connection definition.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

The description of the connection.

- `ConnectionType` – UTF-8 string (valid values: `JDBC` | `SFTP` | `MONGODB` | `KAFKA` | `NETWORK` | `MARKETPLACE` | `CUSTOM` | `SALESFORCE` | `VIEW_VALIDATION_REDSHIFT` | `VIEW_VALIDATION_ATHENA` | `GOOGLEADS` | `GOOGLESHEETS` | `GOOGLEANALYTICS4` | `SERVICENOW` | `MARKETO` | `SAPODATA` | `ZENDESK` | `JIRACLOUD` | `NETSUITEERP` | `HUBSPOT` | `FACEBOOKADS` | `INSTAGRAMADS` | `ZOHOCRM` | `SALESFORCEPARDOT` | `SALESFORCEMARKETINGCLOUD` | `ADOBEANALYTICS` | `SLACK` | `LINKEDIN` | `MIXPANEL` | `ASANA` | `STRIPE` | `SMARTSHEET` | `DATADOG` | `WOOCOMMERCE` | `INTERCOM` | `SNAPCHATADS` | `PAYPAL` | `QUICKBOOKS` | `FACEBOOKPAGEINSIGHTS` | `FRESHDESK` | `TWILIO` | `DOCUSIGNMONITOR` | `FRESHSALES` | `ZOOM` | `GOOGLESEARCHCONSOLE` | `SALESFORCECOMMERCECLOUD` | `SAPCONCUR` | `DYNATRACE` | `MICROSOFTDYNAMIC365FINANCEANDOPS` | `MICROSOFTTEAMS` | `BLACKBAUDRAISEREDGENXT` | `MAILCHIMP` | `GITLAB` | `PENDO` | `PRODUCTBOARD` | `CIRCLECI` | `PIPEDIVE` | `SENDGRID` | `AZURECOSMOS` | `AZURESQL` | `BIGQUERY` | `BLACKBAUD` | `CLOUDERAHIVE` | `CLOUDERAIMPALA` | `CLOUDWATCH` | `CLOUDWATCHMETRICS` | `CMDB` | `DATALAKEGEN2` | `DB2` | `DB2AS400` | `DOCUMENTDB` | `DOMO` | `DYNAMODB` | `GOOGLECLOUDSTORAGE` | `HBASE` | `KUSTOMER` | `MICROSOFTDYNAMICS365CRM` | `MONDAY` | `MYSQL` | `OKTA` | `OPENSEARCH` | `ORACLE` | `PIPEDRIVE` | `POSTGRESQL` | `SAPHANA` | `SQLSERVER` | `SYNAPSE` | `TERADATA` | `TERADATANOS` | `TIMESTREAM` | `TPCDS` | `VERTICA`).

The type of the connection. Currently, SFTP is not supported.

- `MatchCriteria` – An array of UTF-8 strings, not more than 10 strings.

A list of criteria that can be used in selecting this connection.

- `ConnectionProperties` – A map array of key-value pairs, not more than 100 pairs.

Each key is a UTF-8 string (valid values: `HOST` | `PORT` | `USERNAME="USER_NAME"` | `PASSWORD` | `ENCRYPTED_PASSWORD` | `JDBC_DRIVER_JAR_URI` | `JDBC_DRIVER_CLASS_NAME` | `JDBC_ENGINE` | `JDBC_ENGINE_VERSION` | `CONFIG_FILES` | `INSTANCE_ID` | `JDBC_CONNECTION_URL` | `JDBC_ENFORCE_SSL` | `CUSTOM_JDBC_CERT` | `SKIP_CUSTOM_JDBC_CERT_VALIDATION` | `CUSTOM_JDBC_CERT_STRING` | `CONNECTION_URL` | `KAFKA_BOOTSTRAP_SERVERS` | `KAFKA_SSL_ENABLED` | `KAFKA_CUSTOM_CERT` | `KAFKA_SKIP_CUSTOM_CERT_VALIDATION` | `KAFKA_CLIENT_KEYSTORE` | `KAFKA_CLIENT_KEYSTORE_PASSWORD` | `KAFKA_CLIENT_KEY_PASSWORD` | `ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD` | `ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD` | `KAFKA_SASL_MECHANISM` | `KAFKA_SASL_PLAIN_USERNAME` | `KAFKA_SASL_PLAIN_PASSWORD` | `ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD` | `KAFKA_SASL_SCRAM_USERNAME` | `KAFKA_SASL_SCRAM_PASSWORD` | `KAFKA_SASL_SCRAM_SECRETS_ARN` | `ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD` | `KAFKA_SASL_GSSAPI_KEYTAB` | `KAFKA_SASL_GSSAPI_KRB5_CONF` | `KAFKA_SASL_GSSAPI_SERVICE` | `KAFKA_SASL_GSSAPI_PRINCIPAL` | `SECRET_ID` | `CONNECTOR_URL` | `CONNECTOR_TYPE` | `CONNECTOR_CLASS_NAME` | `ENDPOINT` | `ENDPOINT_TYPE` | `ROLE_ARN` | `REGION` | `WORKGROUP_NAME` | `CLUSTER_IDENTIFIER` | `DATABASE`).

Each value is a Value string, not less than 1 or more than 1024 bytes long.

These key-value pairs define parameters for the connection when using
the version 1 Connection schema:

    + `HOST` - The host URI: either the fully qualified domain name
     (FQDN) or the IPv4 address of the database host.
    + `PORT` - The port number, between 1024 and 65535, of the port
     on which the database host is listening for database connections.
    + `USER_NAME` - The name under which to log in to the database.
     The value string for `USER_NAME` is "`USERNAME`".
    + `PASSWORD` - A password, if one is used, for the user name.
    + `ENCRYPTED_PASSWORD` - When you enable connection password
     protection by setting `ConnectionPasswordEncryption` in the
     Data Catalog encryption settings, this field stores the encrypted password.
    + `JDBC_DRIVER_JAR_URI` - The Amazon Simple Storage Service
     (Amazon S3) path of the JAR file that contains the JDBC driver to use.
    + `JDBC_DRIVER_CLASS_NAME` - The class name of the JDBC driver
     to use.
    + `JDBC_ENGINE` - The name of the JDBC engine to use.
    + `JDBC_ENGINE_VERSION` - The version of the JDBC engine to
     use.
    + `CONFIG_FILES` - (Reserved for future use.)
    + `INSTANCE_ID` - The instance ID to use.
    + `JDBC_CONNECTION_URL` - The URL for connecting to a JDBC
     data source.
    + `JDBC_ENFORCE_SSL` - A case-insensitive Boolean string
     (true, false) specifying whether Secure Sockets Layer (SSL) with hostname matching
     is enforced for the JDBC connection on the client. The default is false.
    + `CUSTOM_JDBC_CERT` - An Amazon S3 location specifying the
     customer's root certificate. AWS Glue uses this root certificate
     to validate the customer's certificate when connecting to the customer database.
     AWS Glue only handles X.509 certificates. The certificate provided
     must be DER-encoded and supplied in Base64 encoding PEM format.
    + `SKIP_CUSTOM_JDBC_CERT_VALIDATION` - By default, this
     is `false`. AWS Glue validates the Signature algorithm
     and Subject Public Key Algorithm for the customer certificate. The only permitted
     algorithms for the Signature algorithm are SHA256withRSA, SHA384withRSA or
     SHA512withRSA. For the Subject Public Key Algorithm, the key length must be at
     least 2048. You can set the value of this property to `true` to skip
     AWS Glue's validation of the customer certificate.
    + `CUSTOM_JDBC_CERT_STRING` - A custom JDBC certificate
     string which is used for domain match or distinguished name match to prevent a
     man-in-the-middle attack. In Oracle database, this is used as the `SSL_SERVER_CERT_DN`;
     in Microsoft SQL Server, this is used as the `hostNameInCertificate`.
    + `CONNECTION_URL` - The URL for connecting to a general (non-JDBC)
     data source.
    + `SECRET_ID` - The secret ID used for the secret manager of
     credentials.
    + `CONNECTOR_URL` - The connector URL for a MARKETPLACE or
     CUSTOM connection.
    + `CONNECTOR_TYPE` - The connector type for a MARKETPLACE
     or CUSTOM connection.
    + `CONNECTOR_CLASS_NAME` - The connector class name for a
     MARKETPLACE or CUSTOM connection.
    + `KAFKA_BOOTSTRAP_SERVERS` - A comma-separated list of
     host and port pairs that are the addresses of the Apache Kafka brokers in a Kafka
     cluster to which a Kafka client will connect to and bootstrap itself.
    + `KAFKA_SSL_ENABLED` - Whether to enable or disable SSL on
     an Apache Kafka connection. Default value is "true".
    + `KAFKA_CUSTOM_CERT` - The Amazon S3 URL for the private CA
     cert file (.pem format). The default is an empty string.
    + `KAFKA_SKIP_CUSTOM_CERT_VALIDATION` - Whether to skip
     the validation of the CA cert file or not. AWS Glue validates for three
     algorithms: SHA256withRSA, SHA384withRSA and SHA512withRSA. Default value
     is "false".
    + `KAFKA_CLIENT_KEYSTORE` - The Amazon S3 location of the
     client keystore file for Kafka client side authentication (Optional).
    + `KAFKA_CLIENT_KEYSTORE_PASSWORD` - The password to access
     the provided keystore (Optional).
    + `KAFKA_CLIENT_KEY_PASSWORD` - A keystore can consist of
     multiple keys, so this is the password to access the client key to be used with the
     Kafka server side key (Optional).
    + `ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD` - The encrypted
     version of the Kafka client keystore password (if the user has the AWS Glue encrypt passwords setting selected).
    + `ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD` - The encrypted
     version of the Kafka client key password (if the user has the AWS Glue encrypt passwords setting selected).
    + `KAFKA_SASL_MECHANISM` - `"SCRAM-SHA-512"`,
     `"GSSAPI"`, `"AWS_MSK_IAM"`, or `"PLAIN"`.
     These are the supported [SASL
     Mechanisms](https://www.iana.org/assignments/sasl-mechanisms/sasl-mechanisms.xhtml "https://www.iana.org/assignments/sasl-mechanisms/sasl-mechanisms.xhtml").
    + `KAFKA_SASL_PLAIN_USERNAME` - A plaintext username used
     to authenticate with the "PLAIN" mechanism.
    + `KAFKA_SASL_PLAIN_PASSWORD` - A plaintext password used
     to authenticate with the "PLAIN" mechanism.
    + `ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD` - The encrypted
     version of the Kafka SASL PLAIN password (if the user has the AWS Glue encrypt passwords setting selected).
    + `KAFKA_SASL_SCRAM_USERNAME` - A plaintext username used
     to authenticate with the "SCRAM-SHA-512" mechanism.
    + `KAFKA_SASL_SCRAM_PASSWORD` - A plaintext password used
     to authenticate with the "SCRAM-SHA-512" mechanism.
    + `ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD` - The encrypted
     version of the Kafka SASL SCRAM password (if the user has the AWS Glue encrypt passwords setting selected).
    + `KAFKA_SASL_SCRAM_SECRETS_ARN` - The Amazon Resource
     Name of a secret in AWS Secrets Manager.
    + `KAFKA_SASL_GSSAPI_KEYTAB` - The S3 location of a Kerberos
     `keytab` file. A keytab stores long-term keys for one or more principals.
     For more information, see [MIT
     Kerberos Documentation: Keytab](https://web.mit.edu/kerberos/krb5-latest/doc/basic/keytab_def.html "https://web.mit.edu/kerberos/krb5-latest/doc/basic/keytab_def.html").
    + `KAFKA_SASL_GSSAPI_KRB5_CONF` - The S3 location of a Kerberos
     `krb5.conf` file. A krb5.conf stores Kerberos configuration information,
     such as the location of the KDC server. For more information, see [MIT
     Kerberos Documentation: krb5.conf](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html "https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html").
    + `KAFKA_SASL_GSSAPI_SERVICE` - The Kerberos service name,
     as set with `sasl.kerberos.service.name` in your [Kafka
     Configuration](https://kafka.apache.org/documentation/#brokerconfigs_sasl.kerberos.service.name "https://kafka.apache.org/documentation/#brokerconfigs_sasl.kerberos.service.name").
    + `KAFKA_SASL_GSSAPI_PRINCIPAL` - The name of the Kerberos
     princial used by AWS Glue. For more information, see [Kafka
     Documentation: Configuring Kafka Brokers](https://kafka.apache.org/documentation/#security_sasl_kerberos_clientconfig "https://kafka.apache.org/documentation/#security_sasl_kerberos_clientconfig").
    + `ROLE_ARN` - The role to be used for running queries.
    + `REGION` - The AWS Region where queries will
     be run.
    + `WORKGROUP_NAME` - The name of an Amazon Redshift serverless
     workgroup or Amazon Athena workgroup in which queries will run.
    + `CLUSTER_IDENTIFIER` - The cluster identifier of an Amazon
     Redshift cluster in which queries will run.
    + `DATABASE` - The Amazon Redshift database that you are connecting
     to.

- `SparkProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not less than 1 or more than 2048 bytes long.

Connection properties specific to the Spark compute environment.

- `AthenaProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not less than 1 or more than 2048 bytes long.

Connection properties specific to the Athena compute environment.

- `PythonProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not less than 1 or more than 2048 bytes long.

Connection properties specific to the Python compute environment.

- `PhysicalConnectionRequirements` – A [PhysicalConnectionRequirements](#aws-glue-api-catalog-connections-connections-PhysicalConnectionRequirements "#aws-glue-api-catalog-connections-connections-PhysicalConnectionRequirements") object.

The physical connection requirements, such as virtual private cloud
(VPC) and `SecurityGroup`, that are needed to make this connection
successfully.

- `CreationTime` – Timestamp.

The timestamp of the time that this connection definition was created.

- `LastUpdatedTime` – Timestamp.

The timestamp of the last time the connection definition was updated.

- `LastUpdatedBy` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The user, group, or role that last updated this connection definition.

- `Status` – UTF-8 string (valid values: `READY` | `IN_PROGRESS` | `FAILED`).

The status of the connection. Can be one of: `READY`, `IN_PROGRESS`,
or `FAILED`.

- `StatusReason` – UTF-8 string, not less than 1 or more than 16384 bytes long.

The reason for the connection status.

- `LastConnectionValidationTime` – Timestamp.

A timestamp of the time this connection was last validated.

- `AuthenticationConfiguration` – An [AuthenticationConfiguration](#aws-glue-api-catalog-connections-connections-AuthenticationConfiguration "#aws-glue-api-catalog-connections-connections-AuthenticationConfiguration") object.

The authentication properties of the connection.

- `ConnectionSchemaVersion` – Number (integer), not less than 1 or more than 2.

The version of the connection schema for this connection. Version 2 supports
properties for specific compute environments.

- `CompatibleComputeEnvironments` – An array of UTF-8 strings.

A list of compute environments compatible with the connection.

## ConnectionInput structure

A structure that is used to specify a connection to create or update.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the connection.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

The description of the connection.

- `ConnectionType` – _Required:_ UTF-8 string (valid values: `JDBC` | `SFTP` | `MONGODB` | `KAFKA` | `NETWORK` | `MARKETPLACE` | `CUSTOM` | `SALESFORCE` | `VIEW_VALIDATION_REDSHIFT` | `VIEW_VALIDATION_ATHENA` | `GOOGLEADS` | `GOOGLESHEETS` | `GOOGLEANALYTICS4` | `SERVICENOW` | `MARKETO` | `SAPODATA` | `ZENDESK` | `JIRACLOUD` | `NETSUITEERP` | `HUBSPOT` | `FACEBOOKADS` | `INSTAGRAMADS` | `ZOHOCRM` | `SALESFORCEPARDOT` | `SALESFORCEMARKETINGCLOUD` | `ADOBEANALYTICS` | `SLACK` | `LINKEDIN` | `MIXPANEL` | `ASANA` | `STRIPE` | `SMARTSHEET` | `DATADOG` | `WOOCOMMERCE` | `INTERCOM` | `SNAPCHATADS` | `PAYPAL` | `QUICKBOOKS` | `FACEBOOKPAGEINSIGHTS` | `FRESHDESK` | `TWILIO` | `DOCUSIGNMONITOR` | `FRESHSALES` | `ZOOM` | `GOOGLESEARCHCONSOLE` | `SALESFORCECOMMERCECLOUD` | `SAPCONCUR` | `DYNATRACE` | `MICROSOFTDYNAMIC365FINANCEANDOPS` | `MICROSOFTTEAMS` | `BLACKBAUDRAISEREDGENXT` | `MAILCHIMP` | `GITLAB` | `PENDO` | `PRODUCTBOARD` | `CIRCLECI` | `PIPEDIVE` | `SENDGRID` | `AZURECOSMOS` | `AZURESQL` | `BIGQUERY` | `BLACKBAUD` | `CLOUDERAHIVE` | `CLOUDERAIMPALA` | `CLOUDWATCH` | `CLOUDWATCHMETRICS` | `CMDB` | `DATALAKEGEN2` | `DB2` | `DB2AS400` | `DOCUMENTDB` | `DOMO` | `DYNAMODB` | `GOOGLECLOUDSTORAGE` | `HBASE` | `KUSTOMER` | `MICROSOFTDYNAMICS365CRM` | `MONDAY` | `MYSQL` | `OKTA` | `OPENSEARCH` | `ORACLE` | `PIPEDRIVE` | `POSTGRESQL` | `SAPHANA` | `SQLSERVER` | `SYNAPSE` | `TERADATA` | `TERADATANOS` | `TIMESTREAM` | `TPCDS` | `VERTICA`).

The type of the connection. Currently, these types are supported:

    + `JDBC` - Designates a connection to a database through Java
     Database Connectivity (JDBC).


    `JDBC` Connections use the following ConnectionParameters.




    	- Required: All of (`HOST`, `PORT`, `JDBC_ENGINE`)
    	 or `JDBC_CONNECTION_URL`.
    	- Required: All of (`USERNAME`, `PASSWORD`)
    	 or `SECRET_ID`.
    	- Optional: `JDBC_ENFORCE_SSL`, `CUSTOM_JDBC_CERT`,
    	 `CUSTOM_JDBC_CERT_STRING`, `SKIP_CUSTOM_JDBC_CERT_VALIDATION`.
    	 These parameters are used to configure SSL with JDBC.
    + `KAFKA` - Designates a connection to an Apache Kafka streaming
     platform.


    `KAFKA` Connections use the following ConnectionParameters.




    	- Required: `KAFKA_BOOTSTRAP_SERVERS`.
    	- Optional: `KAFKA_SSL_ENABLED`, `KAFKA_CUSTOM_CERT`,
    	 `KAFKA_SKIP_CUSTOM_CERT_VALIDATION`. These parameters are
    	 used to configure SSL with `KAFKA`.
    	- Optional: `KAFKA_CLIENT_KEYSTORE`, `KAFKA_CLIENT_KEYSTORE_PASSWORD`,
    	 `KAFKA_CLIENT_KEY_PASSWORD`, `ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD`,
    	 `ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD`. These parameters are
    	 used to configure TLS client configuration with SSL in `KAFKA`.
    	- Optional: `KAFKA_SASL_MECHANISM`. Can be specified as
    	 `SCRAM-SHA-512`, `GSSAPI`, or `AWS_MSK_IAM`.
    	- Optional: `KAFKA_SASL_SCRAM_USERNAME`, `KAFKA_SASL_SCRAM_PASSWORD`,
    	 `ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD`. These parameters are
    	 used to configure SASL/SCRAM-SHA-512 authentication with `KAFKA`.
    	- Optional: `KAFKA_SASL_GSSAPI_KEYTAB`, `KAFKA_SASL_GSSAPI_KRB5_CONF`,
    	 `KAFKA_SASL_GSSAPI_SERVICE`, `KAFKA_SASL_GSSAPI_PRINCIPAL`.
    	 These parameters are used to configure SASL/GSSAPI authentication with `KAFKA`.
    + `MONGODB` - Designates a connection to a MongoDB document
     database.


    `MONGODB` Connections use the following ConnectionParameters.




    	- Required: `CONNECTION_URL`.
    	- Required: All of (`USERNAME`, `PASSWORD`)
    	 or `SECRET_ID`.
    + `VIEW_VALIDATION_REDSHIFT` - Designates a connection
     used for view validation by Amazon Redshift.
    + `VIEW_VALIDATION_ATHENA` - Designates a connection used
     for view validation by Amazon Athena.
    + `NETWORK` - Designates a network connection to a data source
     within an Amazon Virtual Private Cloud environment (Amazon VPC).


    `NETWORK` Connections do not require ConnectionParameters.
     Instead, provide a PhysicalConnectionRequirements.
    + `MARKETPLACE` - Uses configuration settings contained
     in a connector purchased from AWS Marketplace to read from and write to data
     stores that are not natively supported by AWS Glue.


    `MARKETPLACE` Connections use the following ConnectionParameters.




    	- Required: `CONNECTOR_TYPE`, `CONNECTOR_URL`,
    	 `CONNECTOR_CLASS_NAME`, `CONNECTION_URL`.
    	- Required for `JDBC` `CONNECTOR_TYPE` connections:
    	 All of (`USERNAME`, `PASSWORD`) or `SECRET_ID`.
    + `CUSTOM` - Uses configuration settings contained in a custom
     connector to read from and write to data stores that are not natively supported
     by AWS Glue.

For more information on the connection parameters needed for a particular
connector, see the documentation for the connector in [Adding an AWS Glue connection](console-connections.md "console-connections.md")in the AWS Glue User Guide.

`SFTP` is not supported.

For more information about how optional ConnectionProperties are used
to configure features in AWS Glue, consult [AWS Glue connection
properties](connection-defining.md "connection-defining.md").

For more information about how optional ConnectionProperties are used
to configure features in AWS Glue Studio, consult [Using connectors and connections](../ug/connectors-chapter.md "../ug/connectors-chapter.md").

- `MatchCriteria` – An array of UTF-8 strings, not more than 10 strings.

A list of criteria that can be used in selecting this connection.

- `ConnectionProperties` – _Required:_ A map array of key-value pairs, not more than 100 pairs.

Each key is a UTF-8 string (valid values: `HOST` | `PORT` | `USERNAME="USER_NAME"` | `PASSWORD` | `ENCRYPTED_PASSWORD` | `JDBC_DRIVER_JAR_URI` | `JDBC_DRIVER_CLASS_NAME` | `JDBC_ENGINE` | `JDBC_ENGINE_VERSION` | `CONFIG_FILES` | `INSTANCE_ID` | `JDBC_CONNECTION_URL` | `JDBC_ENFORCE_SSL` | `CUSTOM_JDBC_CERT` | `SKIP_CUSTOM_JDBC_CERT_VALIDATION` | `CUSTOM_JDBC_CERT_STRING` | `CONNECTION_URL` | `KAFKA_BOOTSTRAP_SERVERS` | `KAFKA_SSL_ENABLED` | `KAFKA_CUSTOM_CERT` | `KAFKA_SKIP_CUSTOM_CERT_VALIDATION` | `KAFKA_CLIENT_KEYSTORE` | `KAFKA_CLIENT_KEYSTORE_PASSWORD` | `KAFKA_CLIENT_KEY_PASSWORD` | `ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD` | `ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD` | `KAFKA_SASL_MECHANISM` | `KAFKA_SASL_PLAIN_USERNAME` | `KAFKA_SASL_PLAIN_PASSWORD` | `ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD` | `KAFKA_SASL_SCRAM_USERNAME` | `KAFKA_SASL_SCRAM_PASSWORD` | `KAFKA_SASL_SCRAM_SECRETS_ARN` | `ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD` | `KAFKA_SASL_GSSAPI_KEYTAB` | `KAFKA_SASL_GSSAPI_KRB5_CONF` | `KAFKA_SASL_GSSAPI_SERVICE` | `KAFKA_SASL_GSSAPI_PRINCIPAL` | `SECRET_ID` | `CONNECTOR_URL` | `CONNECTOR_TYPE` | `CONNECTOR_CLASS_NAME` | `ENDPOINT` | `ENDPOINT_TYPE` | `ROLE_ARN` | `REGION` | `WORKGROUP_NAME` | `CLUSTER_IDENTIFIER` | `DATABASE`).

Each value is a Value string, not less than 1 or more than 1024 bytes long.

These key-value pairs define parameters for the connection.

- `SparkProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not less than 1 or more than 2048 bytes long.

Connection properties specific to the Spark compute environment.

- `AthenaProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not less than 1 or more than 2048 bytes long.

Connection properties specific to the Athena compute environment.

- `PythonProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not less than 1 or more than 2048 bytes long.

Connection properties specific to the Python compute environment.

- `PhysicalConnectionRequirements` – A [PhysicalConnectionRequirements](#aws-glue-api-catalog-connections-connections-PhysicalConnectionRequirements "#aws-glue-api-catalog-connections-connections-PhysicalConnectionRequirements") object.

The physical connection requirements, such as virtual private cloud
(VPC) and `SecurityGroup`, that are needed to successfully make
this connection.

- `AuthenticationConfiguration` – An [AuthenticationConfigurationInput](#aws-glue-api-catalog-connections-connections-AuthenticationConfigurationInput "#aws-glue-api-catalog-connections-connections-AuthenticationConfigurationInput") object.

The authentication properties of the connection.

- `ValidateCredentials` – Boolean.

A flag to validate the credentials during create connection. Default
is true.

- `ValidateForComputeEnvironments` – An array of UTF-8 strings.

The compute environments that the specified connection properties are
validated against.

## TestConnectionInput structure

A structure that is used to specify testing a connection to a service.

###### Fields

- `ConnectionType` – _Required:_ UTF-8 string (valid values: `JDBC` | `SFTP` | `MONGODB` | `KAFKA` | `NETWORK` | `MARKETPLACE` | `CUSTOM` | `SALESFORCE` | `VIEW_VALIDATION_REDSHIFT` | `VIEW_VALIDATION_ATHENA` | `GOOGLEADS` | `GOOGLESHEETS` | `GOOGLEANALYTICS4` | `SERVICENOW` | `MARKETO` | `SAPODATA` | `ZENDESK` | `JIRACLOUD` | `NETSUITEERP` | `HUBSPOT` | `FACEBOOKADS` | `INSTAGRAMADS` | `ZOHOCRM` | `SALESFORCEPARDOT` | `SALESFORCEMARKETINGCLOUD` | `ADOBEANALYTICS` | `SLACK` | `LINKEDIN` | `MIXPANEL` | `ASANA` | `STRIPE` | `SMARTSHEET` | `DATADOG` | `WOOCOMMERCE` | `INTERCOM` | `SNAPCHATADS` | `PAYPAL` | `QUICKBOOKS` | `FACEBOOKPAGEINSIGHTS` | `FRESHDESK` | `TWILIO` | `DOCUSIGNMONITOR` | `FRESHSALES` | `ZOOM` | `GOOGLESEARCHCONSOLE` | `SALESFORCECOMMERCECLOUD` | `SAPCONCUR` | `DYNATRACE` | `MICROSOFTDYNAMIC365FINANCEANDOPS` | `MICROSOFTTEAMS` | `BLACKBAUDRAISEREDGENXT` | `MAILCHIMP` | `GITLAB` | `PENDO` | `PRODUCTBOARD` | `CIRCLECI` | `PIPEDIVE` | `SENDGRID` | `AZURECOSMOS` | `AZURESQL` | `BIGQUERY` | `BLACKBAUD` | `CLOUDERAHIVE` | `CLOUDERAIMPALA` | `CLOUDWATCH` | `CLOUDWATCHMETRICS` | `CMDB` | `DATALAKEGEN2` | `DB2` | `DB2AS400` | `DOCUMENTDB` | `DOMO` | `DYNAMODB` | `GOOGLECLOUDSTORAGE` | `HBASE` | `KUSTOMER` | `MICROSOFTDYNAMICS365CRM` | `MONDAY` | `MYSQL` | `OKTA` | `OPENSEARCH` | `ORACLE` | `PIPEDRIVE` | `POSTGRESQL` | `SAPHANA` | `SQLSERVER` | `SYNAPSE` | `TERADATA` | `TERADATANOS` | `TIMESTREAM` | `TPCDS` | `VERTICA`).

The type of connection to test. This operation is only available for the
`JDBC` or `SALESFORCE` connection types.

- `ConnectionProperties` – _Required:_ A map array of key-value pairs, not more than 100 pairs.

Each key is a UTF-8 string (valid values: `HOST` | `PORT` | `USERNAME="USER_NAME"` | `PASSWORD` | `ENCRYPTED_PASSWORD` | `JDBC_DRIVER_JAR_URI` | `JDBC_DRIVER_CLASS_NAME` | `JDBC_ENGINE` | `JDBC_ENGINE_VERSION` | `CONFIG_FILES` | `INSTANCE_ID` | `JDBC_CONNECTION_URL` | `JDBC_ENFORCE_SSL` | `CUSTOM_JDBC_CERT` | `SKIP_CUSTOM_JDBC_CERT_VALIDATION` | `CUSTOM_JDBC_CERT_STRING` | `CONNECTION_URL` | `KAFKA_BOOTSTRAP_SERVERS` | `KAFKA_SSL_ENABLED` | `KAFKA_CUSTOM_CERT` | `KAFKA_SKIP_CUSTOM_CERT_VALIDATION` | `KAFKA_CLIENT_KEYSTORE` | `KAFKA_CLIENT_KEYSTORE_PASSWORD` | `KAFKA_CLIENT_KEY_PASSWORD` | `ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD` | `ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD` | `KAFKA_SASL_MECHANISM` | `KAFKA_SASL_PLAIN_USERNAME` | `KAFKA_SASL_PLAIN_PASSWORD` | `ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD` | `KAFKA_SASL_SCRAM_USERNAME` | `KAFKA_SASL_SCRAM_PASSWORD` | `KAFKA_SASL_SCRAM_SECRETS_ARN` | `ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD` | `KAFKA_SASL_GSSAPI_KEYTAB` | `KAFKA_SASL_GSSAPI_KRB5_CONF` | `KAFKA_SASL_GSSAPI_SERVICE` | `KAFKA_SASL_GSSAPI_PRINCIPAL` | `SECRET_ID` | `CONNECTOR_URL` | `CONNECTOR_TYPE` | `CONNECTOR_CLASS_NAME` | `ENDPOINT` | `ENDPOINT_TYPE` | `ROLE_ARN` | `REGION` | `WORKGROUP_NAME` | `CLUSTER_IDENTIFIER` | `DATABASE`).

Each value is a Value string, not less than 1 or more than 1024 bytes long.

The key-value pairs that define parameters for the connection.

JDBC connections use the following connection properties:

    + Required: All of (`HOST`, `PORT`, `JDBC_ENGINE`)
     or `JDBC_CONNECTION_URL`.
    + Required: All of (`USERNAME`, `PASSWORD`)
     or `SECRET_ID`.
    + Optional: `JDBC_ENFORCE_SSL`, `CUSTOM_JDBC_CERT`,
     `CUSTOM_JDBC_CERT_STRING`, `SKIP_CUSTOM_JDBC_CERT_VALIDATION`.
     These parameters are used to configure SSL with JDBC.

SALESFORCE connections require the `AuthenticationConfiguration`
member to be configured.

- `AuthenticationConfiguration` – An [AuthenticationConfigurationInput](#aws-glue-api-catalog-connections-connections-AuthenticationConfigurationInput "#aws-glue-api-catalog-connections-connections-AuthenticationConfigurationInput") object.

A structure containing the authentication configuration in the TestConnection
request. Required for a connection to Salesforce using OAuth authentication.

## PhysicalConnectionRequirements structure

The OAuth client app in GetConnection response.

###### Fields

- `SubnetId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The subnet ID used by the connection.

- `SecurityGroupIdList` – An array of UTF-8 strings, not more than 50 strings.

The security group ID list used by the connection.

- `AvailabilityZone` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The connection's Availability Zone.

## GetConnectionsFilter structure

Filters the connection definitions that are returned by the `GetConnections`
API operation.

###### Fields

- `MatchCriteria` – An array of UTF-8 strings, not more than 10 strings.

A criteria string that must match the criteria recorded in the connection
definition for that connection definition to be returned.

- `ConnectionType` – UTF-8 string (valid values: `JDBC` | `SFTP` | `MONGODB` | `KAFKA` | `NETWORK` | `MARKETPLACE` | `CUSTOM` | `SALESFORCE` | `VIEW_VALIDATION_REDSHIFT` | `VIEW_VALIDATION_ATHENA` | `GOOGLEADS` | `GOOGLESHEETS` | `GOOGLEANALYTICS4` | `SERVICENOW` | `MARKETO` | `SAPODATA` | `ZENDESK` | `JIRACLOUD` | `NETSUITEERP` | `HUBSPOT` | `FACEBOOKADS` | `INSTAGRAMADS` | `ZOHOCRM` | `SALESFORCEPARDOT` | `SALESFORCEMARKETINGCLOUD` | `ADOBEANALYTICS` | `SLACK` | `LINKEDIN` | `MIXPANEL` | `ASANA` | `STRIPE` | `SMARTSHEET` | `DATADOG` | `WOOCOMMERCE` | `INTERCOM` | `SNAPCHATADS` | `PAYPAL` | `QUICKBOOKS` | `FACEBOOKPAGEINSIGHTS` | `FRESHDESK` | `TWILIO` | `DOCUSIGNMONITOR` | `FRESHSALES` | `ZOOM` | `GOOGLESEARCHCONSOLE` | `SALESFORCECOMMERCECLOUD` | `SAPCONCUR` | `DYNATRACE` | `MICROSOFTDYNAMIC365FINANCEANDOPS` | `MICROSOFTTEAMS` | `BLACKBAUDRAISEREDGENXT` | `MAILCHIMP` | `GITLAB` | `PENDO` | `PRODUCTBOARD` | `CIRCLECI` | `PIPEDIVE` | `SENDGRID` | `AZURECOSMOS` | `AZURESQL` | `BIGQUERY` | `BLACKBAUD` | `CLOUDERAHIVE` | `CLOUDERAIMPALA` | `CLOUDWATCH` | `CLOUDWATCHMETRICS` | `CMDB` | `DATALAKEGEN2` | `DB2` | `DB2AS400` | `DOCUMENTDB` | `DOMO` | `DYNAMODB` | `GOOGLECLOUDSTORAGE` | `HBASE` | `KUSTOMER` | `MICROSOFTDYNAMICS365CRM` | `MONDAY` | `MYSQL` | `OKTA` | `OPENSEARCH` | `ORACLE` | `PIPEDRIVE` | `POSTGRESQL` | `SAPHANA` | `SQLSERVER` | `SYNAPSE` | `TERADATA` | `TERADATANOS` | `TIMESTREAM` | `TPCDS` | `VERTICA`).

The type of connections to return. Currently, SFTP is not supported.

- `ConnectionSchemaVersion` – Number (integer), not less than 1 or more than 2.

Denotes if the connection was created with schema version 1 or 2.

## AuthenticationConfiguration structure

A structure containing the authentication configuration.

###### Fields

- `AuthenticationType` – UTF-8 string (valid values: `BASIC` | `OAUTH2` | `CUSTOM` | `IAM`).

A structure containing the authentication configuration.

- `SecretArn` – UTF-8 string, matching the [Custom string pattern #36](aws-glue-api-common.md#regex_36 "aws-glue-api-common.md#regex_36").

The secret manager ARN to store credentials.

- `KmsKeyArn` – UTF-8 string, matching the [Custom string pattern #42](aws-glue-api-common.md#regex_42 "aws-glue-api-common.md#regex_42").

The Amazon Resource Name (ARN) of the KMS key used to encrypt sensitive
authentication information. This key is used to protect credentials and other
sensitive data stored within the authentication configuration.

- `OAuth2Properties` – An [OAuth2Properties](#aws-glue-api-catalog-connections-connections-OAuth2Properties "#aws-glue-api-catalog-connections-connections-OAuth2Properties") object.

The properties for OAuth2 authentication.

## AuthenticationConfigurationInput structure

A structure containing the authentication configuration in the CreateConnection
request.

###### Fields

- `AuthenticationType` – UTF-8 string (valid values: `BASIC` | `OAUTH2` | `CUSTOM` | `IAM`).

A structure containing the authentication configuration in the CreateConnection
request.

- `OAuth2Properties` – An [OAuth2PropertiesInput](#aws-glue-api-catalog-connections-connections-OAuth2PropertiesInput "#aws-glue-api-catalog-connections-connections-OAuth2PropertiesInput") object.

The properties for OAuth2 authentication in the CreateConnection request.

- `SecretArn` – UTF-8 string, matching the [Custom string pattern #36](aws-glue-api-common.md#regex_36 "aws-glue-api-common.md#regex_36").

The secret manager ARN to store credentials in the CreateConnection request.

- `KmsKeyArn` – UTF-8 string, matching the [Custom string pattern #42](aws-glue-api-common.md#regex_42 "aws-glue-api-common.md#regex_42").

The ARN of the KMS key used to encrypt the connection. Only taken an as input
in the request and stored in the Secret Manager.

- `BasicAuthenticationCredentials` – A [BasicAuthenticationCredentials](#aws-glue-api-catalog-connections-connections-BasicAuthenticationCredentials "#aws-glue-api-catalog-connections-connections-BasicAuthenticationCredentials") object.

The credentials used when the authentication type is basic authentication.

- `CustomAuthenticationCredentials` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not less than 1 or more than 2048 bytes long.

The credentials used when the authentication type is custom authentication.

## OAuth2Properties structure

A structure containing properties for OAuth2 authentication.

###### Fields

- `OAuth2GrantType` – UTF-8 string (valid values: `AUTHORIZATION_CODE` | `CLIENT_CREDENTIALS` | `JWT_BEARER`).

The OAuth2 grant type. For example, `AUTHORIZATION_CODE`,
`JWT_BEARER`, or `CLIENT_CREDENTIALS`.

- `OAuth2ClientApplication` – An [OAuth2ClientApplication](#aws-glue-api-catalog-connections-connections-OAuth2ClientApplication "#aws-glue-api-catalog-connections-connections-OAuth2ClientApplication") object.

The client application type. For example, AWS_MANAGED or USER_MANAGED.

- `TokenUrl` – UTF-8 string, not more than 256 bytes long, matching the [Custom string pattern #40](aws-glue-api-common.md#regex_40 "aws-glue-api-common.md#regex_40").

The URL of the provider's authentication server, to exchange an authorization
code for an access token.

- `TokenUrlParametersMap` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not less than 1 or more than 512 bytes long.

A map of parameters that are added to the token `GET` request.

## OAuth2PropertiesInput structure

A structure containing properties for OAuth2 in the CreateConnection
request.

###### Fields

- `OAuth2GrantType` – UTF-8 string (valid values: `AUTHORIZATION_CODE` | `CLIENT_CREDENTIALS` | `JWT_BEARER`).

The OAuth2 grant type in the CreateConnection request. For example, `AUTHORIZATION_CODE`,
`JWT_BEARER`, or `CLIENT_CREDENTIALS`.

- `OAuth2ClientApplication` – An [OAuth2ClientApplication](#aws-glue-api-catalog-connections-connections-OAuth2ClientApplication "#aws-glue-api-catalog-connections-connections-OAuth2ClientApplication") object.

The client application type in the CreateConnection request. For example,
`AWS_MANAGED` or `USER_MANAGED`.

- `TokenUrl` – UTF-8 string, not more than 256 bytes long, matching the [Custom string pattern #40](aws-glue-api-common.md#regex_40 "aws-glue-api-common.md#regex_40").

The URL of the provider's authentication server, to exchange an authorization
code for an access token.

- `TokenUrlParametersMap` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not less than 1 or more than 512 bytes long.

A map of parameters that are added to the token `GET` request.

- `AuthorizationCodeProperties` – An [AuthorizationCodeProperties](#aws-glue-api-catalog-connections-connections-AuthorizationCodeProperties "#aws-glue-api-catalog-connections-connections-AuthorizationCodeProperties") object.

The set of properties required for the the OAuth2 `AUTHORIZATION_CODE`
grant type.

- `OAuth2Credentials` – An [OAuth2Credentials](#aws-glue-api-catalog-connections-connections-OAuth2Credentials "#aws-glue-api-catalog-connections-connections-OAuth2Credentials") object.

The credentials used when the authentication type is OAuth2 authentication.

## OAuth2ClientApplication structure

The OAuth2 client app used for the connection.

###### Fields

- `UserManagedClientApplicationClientId` – UTF-8 string, not more than 2048 bytes long, matching the [Custom string pattern #37](aws-glue-api-common.md#regex_37 "aws-glue-api-common.md#regex_37").

The client application clientID if the ClientAppType is `USER_MANAGED`.

- `AWSManagedClientApplicationReference` – UTF-8 string, not more than 2048 bytes long, matching the [Custom string pattern #37](aws-glue-api-common.md#regex_37 "aws-glue-api-common.md#regex_37").

The reference to the SaaS-side client app that is AWS managed.

## AuthorizationCodeProperties structure

The set of properties required for the the OAuth2 `AUTHORIZATION_CODE`
grant type workflow.

###### Fields

- `AuthorizationCode` – UTF-8 string, not less than 1 or more than 4096 bytes long, matching the [Custom string pattern #37](aws-glue-api-common.md#regex_37 "aws-glue-api-common.md#regex_37").

An authorization code to be used in the third leg of the `AUTHORIZATION_CODE`
grant workflow. This is a single-use code which becomes invalid once exchanged
for an access token, thus it is acceptable to have this value as a request parameter.

- `RedirectUri` – UTF-8 string, not more than 512 bytes long, matching the [Custom string pattern #41](aws-glue-api-common.md#regex_41 "aws-glue-api-common.md#regex_41").

The redirect URI where the user gets redirected to by authorization server
when issuing an authorization code. The URI is subsequently used when the authorization
code is exchanged for an access token.

## BasicAuthenticationCredentials structure

For supplying basic auth credentials when not providing a `SecretArn`
value.

###### Fields

- `Username` – UTF-8 string, not more than 512 bytes long, matching the [Custom string pattern #37](aws-glue-api-common.md#regex_37 "aws-glue-api-common.md#regex_37").

The username to connect to the data source.

- `Password` – UTF-8 string, not more than 512 bytes long, matching the [Custom string pattern #33](aws-glue-api-common.md#regex_33 "aws-glue-api-common.md#regex_33").

The password to connect to the data source.

## OAuth2Credentials structure

The credentials used when the authentication type is OAuth2 authentication.

###### Fields

- `UserManagedClientApplicationClientSecret` – UTF-8 string, not more than 512 bytes long, matching the [Custom string pattern #38](aws-glue-api-common.md#regex_38 "aws-glue-api-common.md#regex_38").

The client application client secret if the client application is user
managed.

- `AccessToken` – UTF-8 string, not more than 4096 bytes long, matching the [Custom string pattern #38](aws-glue-api-common.md#regex_38 "aws-glue-api-common.md#regex_38").

The access token used when the authentication type is OAuth2.

- `RefreshToken` – UTF-8 string, not more than 4096 bytes long, matching the [Custom string pattern #38](aws-glue-api-common.md#regex_38 "aws-glue-api-common.md#regex_38").

The refresh token used when the authentication type is OAuth2.

- `JwtToken` – UTF-8 string, not more than 8000 bytes long, matching the [Custom string pattern #39](aws-glue-api-common.md#regex_39 "aws-glue-api-common.md#regex_39").

The JSON Web Token (JWT) used when the authentication type is OAuth2.

## Operations

- [CreateConnection action (Python: create_connection)](#aws-glue-api-catalog-connections-connections-CreateConnection "#aws-glue-api-catalog-connections-connections-CreateConnection")
- [DeleteConnection action (Python: delete_connection)](#aws-glue-api-catalog-connections-connections-DeleteConnection "#aws-glue-api-catalog-connections-connections-DeleteConnection")
- [GetConnection action (Python: get_connection)](#aws-glue-api-catalog-connections-connections-GetConnection "#aws-glue-api-catalog-connections-connections-GetConnection")
- [GetConnections action (Python: get_connections)](#aws-glue-api-catalog-connections-connections-GetConnections "#aws-glue-api-catalog-connections-connections-GetConnections")
- [UpdateConnection action (Python: update_connection)](#aws-glue-api-catalog-connections-connections-UpdateConnection "#aws-glue-api-catalog-connections-connections-UpdateConnection")
- [TestConnection action (Python: test_connection)](#aws-glue-api-catalog-connections-connections-TestConnection "#aws-glue-api-catalog-connections-connections-TestConnection")
- [BatchDeleteConnection action (Python: batch_delete_connection)](#aws-glue-api-catalog-connections-connections-BatchDeleteConnection "#aws-glue-api-catalog-connections-connections-BatchDeleteConnection")

## CreateConnection action (Python: create_connection)

Creates a connection definition in the Data Catalog.

Connections used for creating federated resources require the IAM `glue:PassConnection`
permission.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which to create the connection. If none is provided,
the AWS account ID is used by default.

- `ConnectionInput` – _Required:_ A [ConnectionInput](#aws-glue-api-catalog-connections-connections-ConnectionInput "#aws-glue-api-catalog-connections-connections-ConnectionInput") object.

A `ConnectionInput` object defining the connection to create.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

The tags you assign to the connection.

###### Response

- `CreateConnectionStatus` – UTF-8 string (valid values: `READY` | `IN_PROGRESS` | `FAILED`).

The status of the connection creation request. The request can take some
time for certain authentication types, for example when creating an OAuth connection
with token exchange over VPC.

###### Errors

- `AlreadyExistsException`
- `InvalidInputException`
- `OperationTimeoutException`
- `ResourceNumberLimitExceededException`
- `GlueEncryptionException`

## DeleteConnection action (Python: delete_connection)

Deletes a connection from the Data Catalog.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which the connection resides. If none is provided,
the AWS account ID is used by default.

- `ConnectionName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the connection to delete.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `OperationTimeoutException`

## GetConnection action (Python: get_connection)

Retrieves a connection definition from the Data Catalog.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which the connection resides. If none is provided,
the AWS account ID is used by default.

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the connection definition to retrieve.

- `HidePassword` – Boolean.

Allows you to retrieve the connection metadata without returning the
password. For instance, the AWS Glue console uses this flag to retrieve
the connection, and does not display the password. Set this parameter when the
caller might not have permission to use the AWS KMS key to decrypt
the password, but it does have permission to access the rest of the connection
properties.

- `ApplyOverrideForComputeEnvironment` – UTF-8 string (valid values: `SPARK` | `ATHENA` | `PYTHON`).

For connections that may be used in multiple services, specifies returning
properties for the specified compute environment.

###### Response

- `Connection` – A [Connection](#aws-glue-api-catalog-connections-connections-Connection "#aws-glue-api-catalog-connections-connections-Connection") object.

The requested connection definition.

###### Errors

- `EntityNotFoundException`
- `OperationTimeoutException`
- `InvalidInputException`
- `GlueEncryptionException`

## GetConnections action (Python: get_connections)

Retrieves a list of connection definitions from the Data Catalog.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which the connections reside. If none is provided,
the AWS account ID is used by default.

- `Filter` – A [GetConnectionsFilter](#aws-glue-api-catalog-connections-connections-GetConnectionsFilter "#aws-glue-api-catalog-connections-connections-GetConnectionsFilter") object.

A filter that controls which connections are returned.

- `HidePassword` – Boolean.

Allows you to retrieve the connection metadata without returning the
password. For instance, the AWS Glue console uses this flag to retrieve
the connection, and does not display the password. Set this parameter when the
caller might not have permission to use the AWS KMS key to decrypt
the password, but it does have permission to access the rest of the connection
properties.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation call.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum number of connections to return in one response.

###### Response

- `ConnectionList` – An array of [Connection](#aws-glue-api-catalog-connections-connections-Connection "#aws-glue-api-catalog-connections-connections-Connection") objects.

A list of requested connection definitions.

- `NextToken` – UTF-8 string.

A continuation token, if the list of connections returned does not include
the last of the filtered connections.

###### Errors

- `EntityNotFoundException`
- `OperationTimeoutException`
- `InvalidInputException`
- `GlueEncryptionException`

## UpdateConnection action (Python: update_connection)

Updates a connection definition in the Data Catalog.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which the connection resides. If none is provided,
the AWS account ID is used by default.

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the connection definition to update.

- `ConnectionInput` – _Required:_ A [ConnectionInput](#aws-glue-api-catalog-connections-connections-ConnectionInput "#aws-glue-api-catalog-connections-connections-ConnectionInput") object.

A `ConnectionInput` object that redefines the connection
in question.

###### Response

- _No Response parameters._

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `OperationTimeoutException`
- `InvalidInputException`
- `GlueEncryptionException`

## TestConnection action (Python: test_connection)

Tests a connection to a service to validate the service credentials that
you provide.

You can either provide an existing connection name or a `TestConnectionInput`
for testing a non-existing connection input. Providing both at the same time
will cause an error.

If the action is successful, the service sends back an HTTP 200 response.

###### Request

- `ConnectionName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Optional. The name of the connection to test. If only name is provided,
the operation will get the connection and use that for testing.

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The catalog ID where the connection resides.

- `TestConnectionInput` – A [TestConnectionInput](#aws-glue-api-catalog-connections-connections-TestConnectionInput "#aws-glue-api-catalog-connections-connections-TestConnectionInput") object.

A structure that is used to specify testing a connection to a service.

###### Response

- _No Response parameters._

###### Errors

- `InvalidInputException`
- `OperationTimeoutException`
- `ResourceNumberLimitExceededException`
- `GlueEncryptionException`
- `FederationSourceException`
- `AccessDeniedException`
- `EntityNotFoundException`
- `ConflictException`
- `InternalServiceException`

## BatchDeleteConnection action (Python: batch_delete_connection)

Deletes a list of connection definitions from the Data Catalog.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which the connections reside. If none is provided,
the AWS account ID is used by default.

- `ConnectionNameList` – _Required:_ An array of UTF-8 strings, not more than 25 strings.

A list of names of the connections to delete.

###### Response

- `Succeeded` – An array of UTF-8 strings.

A list of names of the connection definitions that were successfully deleted.

- `Errors` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a An [ErrorDetail](aws-glue-api-common.md#aws-glue-api-common-ErrorDetail "aws-glue-api-common.md#aws-glue-api-common-ErrorDetail") object.

A map of the names of connections that were not successfully deleted to
error details.

###### Errors

- `InternalServiceException`
- `OperationTimeoutException`

# Connection Types API

The Connection Type API describes AWS Glue APIs related to
describing connection types.

## Connection management APIs

- [DescribeConnectionType action (Python: describe_connection_type)](#aws-glue-api-catalog-connections-connections-type-DescribeConnectionType "#aws-glue-api-catalog-connections-connections-type-DescribeConnectionType")
- [ListConnectionTypes action (Python: list_connection_types)](#aws-glue-api-catalog-connections-connections-type-ListConnectionTypes "#aws-glue-api-catalog-connections-connections-type-ListConnectionTypes")
- [ConnectionTypeBrief structure](#aws-glue-api-catalog-connections-connections-type-ConnectionTypeBrief "#aws-glue-api-catalog-connections-connections-type-ConnectionTypeBrief")
- [ConnectionTypeVariant structure](#aws-glue-api-catalog-connections-connections-type-ConnectionTypeVariant "#aws-glue-api-catalog-connections-connections-type-ConnectionTypeVariant")

## DescribeConnectionType action (Python: describe_connection_type)

The `DescribeConnectionType` API provides full details
of the supported options for a given connection type in AWS Glue.

###### Request

- `ConnectionType` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the connection type to be described.

###### Response

- `ConnectionType` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the connection type.

- `Description` – UTF-8 string, not more than 1024 bytes long.

A description of the connection type.

- `Capabilities` – A [Capabilities](#aws-glue-api-catalog-connections-connections-type-Capabilities "#aws-glue-api-catalog-connections-connections-type-Capabilities") object.

The supported authentication types, data interface types (compute environments),
and data operations of the connector.

- `ConnectionProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property "#aws-glue-api-catalog-connections-connections-type-Property") object.

Connection properties which are common across compute environments.

- `ConnectionOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property "#aws-glue-api-catalog-connections-connections-type-Property") object.

Returns properties that can be set when creating a connection in the `ConnectionInput.ConnectionProperties`.
`ConnectionOptions` defines parameters that can be set in a Spark
ETL script in the connection options map passed to a dataframe.

- `AuthenticationConfiguration` – An [AuthConfiguration](#aws-glue-api-catalog-connections-connections-type-AuthConfiguration "#aws-glue-api-catalog-connections-connections-type-AuthConfiguration") object.

The type of authentication used for the connection.

- `ComputeEnvironmentConfigurations` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a A [ComputeEnvironmentConfiguration](#aws-glue-api-catalog-connections-connections-type-ComputeEnvironmentConfiguration "#aws-glue-api-catalog-connections-connections-type-ComputeEnvironmentConfiguration") object.

The compute environments that are supported by the connection.

- `PhysicalConnectionRequirements` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property "#aws-glue-api-catalog-connections-connections-type-Property") object.

Physical requirements for a connection, such as VPC, Subnet and Security
Group specifications.

- `AthenaConnectionProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property "#aws-glue-api-catalog-connections-connections-type-Property") object.

Connection properties specific to the Athena compute environment.

- `PythonConnectionProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property "#aws-glue-api-catalog-connections-connections-type-Property") object.

Connection properties specific to the Python compute environment.

- `SparkConnectionProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property "#aws-glue-api-catalog-connections-connections-type-Property") object.

Connection properties specific to the Spark compute environment.

###### Errors

- `ValidationException`
- `InvalidInputException`
- `InternalServiceException`

## ListConnectionTypes action (Python: list_connection_types)

The `ListConnectionTypes` API provides a discovery mechanism
to learn available connection types in AWS Glue. The response contains
a list of connection types with high-level details of what is supported for each
connection type. The connection types listed are the set of supported options
for the `ConnectionType` value in the `CreateConnection`
API.

###### Request

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum number of results to return.

- `NextToken` – UTF-8 string, not less than 1 or more than 2048 bytes long, matching the [Custom string pattern #11](aws-glue-api-common.md#regex_11 "aws-glue-api-common.md#regex_11").

A continuation token, if this is a continuation call.

###### Response

- `ConnectionTypes` – An array of [ConnectionTypeBrief](#aws-glue-api-catalog-connections-connections-type-ConnectionTypeBrief "#aws-glue-api-catalog-connections-connections-type-ConnectionTypeBrief") objects.

A list of `ConnectionTypeBrief` objects containing brief
information about the supported connection types.

- `NextToken` – UTF-8 string, not less than 1 or more than 2048 bytes long, matching the [Custom string pattern #11](aws-glue-api-common.md#regex_11 "aws-glue-api-common.md#regex_11").

A continuation token, if the current list segment is not the last.

###### Errors

- `InternalServiceException`

## ConnectionTypeBrief structure

Brief information about a supported connection type returned by the `ListConnectionTypes`
API.

###### Fields

- `ConnectionType` – UTF-8 string (valid values: `JDBC` | `SFTP` | `MONGODB` | `KAFKA` | `NETWORK` | `MARKETPLACE` | `CUSTOM` | `SALESFORCE` | `VIEW_VALIDATION_REDSHIFT` | `VIEW_VALIDATION_ATHENA` | `GOOGLEADS` | `GOOGLESHEETS` | `GOOGLEANALYTICS4` | `SERVICENOW` | `MARKETO` | `SAPODATA` | `ZENDESK` | `JIRACLOUD` | `NETSUITEERP` | `HUBSPOT` | `FACEBOOKADS` | `INSTAGRAMADS` | `ZOHOCRM` | `SALESFORCEPARDOT` | `SALESFORCEMARKETINGCLOUD` | `ADOBEANALYTICS` | `SLACK` | `LINKEDIN` | `MIXPANEL` | `ASANA` | `STRIPE` | `SMARTSHEET` | `DATADOG` | `WOOCOMMERCE` | `INTERCOM` | `SNAPCHATADS` | `PAYPAL` | `QUICKBOOKS` | `FACEBOOKPAGEINSIGHTS` | `FRESHDESK` | `TWILIO` | `DOCUSIGNMONITOR` | `FRESHSALES` | `ZOOM` | `GOOGLESEARCHCONSOLE` | `SALESFORCECOMMERCECLOUD` | `SAPCONCUR` | `DYNATRACE` | `MICROSOFTDYNAMIC365FINANCEANDOPS` | `MICROSOFTTEAMS` | `BLACKBAUDRAISEREDGENXT` | `MAILCHIMP` | `GITLAB` | `PENDO` | `PRODUCTBOARD` | `CIRCLECI` | `PIPEDIVE` | `SENDGRID` | `AZURECOSMOS` | `AZURESQL` | `BIGQUERY` | `BLACKBAUD` | `CLOUDERAHIVE` | `CLOUDERAIMPALA` | `CLOUDWATCH` | `CLOUDWATCHMETRICS` | `CMDB` | `DATALAKEGEN2` | `DB2` | `DB2AS400` | `DOCUMENTDB` | `DOMO` | `DYNAMODB` | `GOOGLECLOUDSTORAGE` | `HBASE` | `KUSTOMER` | `MICROSOFTDYNAMICS365CRM` | `MONDAY` | `MYSQL` | `OKTA` | `OPENSEARCH` | `ORACLE` | `PIPEDRIVE` | `POSTGRESQL` | `SAPHANA` | `SQLSERVER` | `SYNAPSE` | `TERADATA` | `TERADATANOS` | `TIMESTREAM` | `TPCDS` | `VERTICA`).

The name of the connection type.

- `DisplayName` – UTF-8 string, not less than 1 or more than 128 bytes long.

The human-readable name for the connection type that is displayed in the
AWS Glue console.

- `Vendor` – UTF-8 string, not less than 1 or more than 128 bytes long.

The name of the vendor or provider that created or maintains this connection
type.

- `Description` – UTF-8 string, not more than 1024 bytes long.

A description of the connection type.

- `Categories` – .

A list of categories that this connection type belongs to. Categories
help users filter and find appropriate connection types based on their use cases.

- `Capabilities` – A [Capabilities](#aws-glue-api-catalog-connections-connections-type-Capabilities "#aws-glue-api-catalog-connections-connections-type-Capabilities") object.

The supported authentication types, data interface types (compute environments),
and data operations of the connector.

- `LogoUrl` – UTF-8 string.

The URL of the logo associated with a connection type.

- `ConnectionTypeVariants` – An array of [ConnectionTypeVariant](#aws-glue-api-catalog-connections-connections-type-ConnectionTypeVariant "#aws-glue-api-catalog-connections-connections-type-ConnectionTypeVariant") objects.

A list of variants available for this connection type. Different variants
may provide specialized configurations for specific use cases or implementations
of the same general connection type.

## ConnectionTypeVariant structure

Represents a variant of a connection type in AWS Glue Data Catalog.
Connection type variants provide specific configurations and behaviors for
different implementations of the same general connection type.

###### Fields

- `ConnectionTypeVariantName` – UTF-8 string, not less than 1 or more than 128 bytes long.

The unique identifier for the connection type variant. This name is used
internally to identify the specific variant of a connection type.

- `DisplayName` – UTF-8 string, not less than 1 or more than 128 bytes long.

The human-readable name for the connection type variant that is displayed
in the AWS Glue console.

- `Description` – UTF-8 string, not more than 1024 bytes long.

A detailed description of the connection type variant, including its
purpose, use cases, and any specific configuration requirements.

- `LogoUrl` – UTF-8 string.

The URL of the logo associated with a connection type variant.

## datatypes

- [Validation structure](#aws-glue-api-catalog-connections-connections-type-Validation "#aws-glue-api-catalog-connections-connections-type-Validation")
- [AuthConfiguration structure](#aws-glue-api-catalog-connections-connections-type-AuthConfiguration "#aws-glue-api-catalog-connections-connections-type-AuthConfiguration")
- [Capabilities structure](#aws-glue-api-catalog-connections-connections-type-Capabilities "#aws-glue-api-catalog-connections-connections-type-Capabilities")
- [Property structure](#aws-glue-api-catalog-connections-connections-type-Property "#aws-glue-api-catalog-connections-connections-type-Property")
- [AllowedValue structure](#aws-glue-api-catalog-connections-connections-type-AllowedValue "#aws-glue-api-catalog-connections-connections-type-AllowedValue")
- [ComputeEnvironmentConfiguration structure](#aws-glue-api-catalog-connections-connections-type-ComputeEnvironmentConfiguration "#aws-glue-api-catalog-connections-connections-type-ComputeEnvironmentConfiguration")

## Validation structure

Defines how a validation is performed on a connection property.

###### Fields

- `ValidationType` – _Required:_ UTF-8 string (valid values: `REGEX` | `RANGE`).

The type of validation to be performed, such as `REGEX`.

- `Patterns` – .

A list of patterns that apply to the validation.

- `Description` – _Required:_ UTF-8 string, not less than 1 or more than 1024 bytes long.

A description for the validation.

- `MaxLength` – Number (integer).

A maximum length for a string connection property.

- `Maximum` – Number (integer).

A maximum value when specifying a `RANGE` type of validation.

- `Minimum` – Number (integer).

A minimum value when specifying a `RANGE` type of validation.

## AuthConfiguration structure

The authentication configuration for a connection returned by the `DescribeConnectionType`
API.

###### Fields

- `AuthenticationType` – _Required:_ A [Property](#aws-glue-api-catalog-connections-connections-type-Property "#aws-glue-api-catalog-connections-connections-type-Property") object.

The type of authentication for a connection.

- `SecretArn` – A [Property](#aws-glue-api-catalog-connections-connections-type-Property "#aws-glue-api-catalog-connections-connections-type-Property") object.

The Amazon Resource Name (ARN) for the Secrets Manager.

- `OAuth2Properties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property "#aws-glue-api-catalog-connections-connections-type-Property") object.

A map of key-value pairs for the OAuth2 properties. Each value is a a `Property`
object.

- `BasicAuthenticationProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property "#aws-glue-api-catalog-connections-connections-type-Property") object.

A map of key-value pairs for the OAuth2 properties. Each value is a a `Property`
object.

- `CustomAuthenticationProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property "#aws-glue-api-catalog-connections-connections-type-Property") object.

A map of key-value pairs for the custom authentication properties. Each
value is a a `Property` object.

## Capabilities structure

Specifies the supported authentication types returned by the `DescribeConnectionType`
API.

###### Fields

- `SupportedAuthenticationTypes` – _Required:_ An array of UTF-8 strings.

A list of supported authentication types.

- `SupportedDataOperations` – _Required:_ An array of UTF-8 strings.

A list of supported data operations.

- `SupportedComputeEnvironments` – _Required:_ An array of UTF-8 strings.

A list of supported compute environments.

## Property structure

An object that defines a connection type for a compute environment.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The name of the property.

- `Description` – _Required:_ UTF-8 string, not more than 1024 bytes long.

A description of the property.

- `Required` – _Required:_ Boolean.

Indicates whether the property is required.

- `PropertyTypes` – _Required:_ An array of UTF-8 strings.

Describes the type of property.

- `AllowedValues` – An array of [AllowedValue](#aws-glue-api-catalog-connections-connections-type-AllowedValue "#aws-glue-api-catalog-connections-connections-type-AllowedValue") objects.

A list of `AllowedValue` objects representing the values
allowed for the property.

- `DataOperationScopes` – An array of UTF-8 strings.

Indicates which data operations are applicable to the property.

## AllowedValue structure

An object representing a value allowed for a property.

###### Fields

- `Description` – UTF-8 string, not more than 1024 bytes long.

A description of the allowed value.

- `Value` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The value allowed for the property.

## ComputeEnvironmentConfiguration structure

An object containing configuration for a compute environment (such as
Spark, Python or Athena) returned by the `DescribeConnectionType`
API.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

A name for the compute environment configuration.

- `Description` – _Required:_ UTF-8 string, not more than 1024 bytes long.

A description of the compute environment.

- `ComputeEnvironment` – _Required:_ UTF-8 string (valid values: `SPARK` | `ATHENA` | `PYTHON`).

The type of compute environment.

- `SupportedAuthenticationTypes` – _Required:_ An array of UTF-8 strings.

The supported authentication types for the compute environment.

- `ConnectionOptions` – _Required:_ A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property "#aws-glue-api-catalog-connections-connections-type-Property") object.

The parameters used as connection options for the compute environment.

- `ConnectionPropertyNameOverrides` – _Required:_ A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not less than 1 or more than 128 bytes long.

The connection property name overrides for the compute environment.

- `ConnectionOptionNameOverrides` – _Required:_ A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not less than 1 or more than 128 bytes long.

The connection option name overrides for the compute environment.

- `ConnectionPropertiesRequiredOverrides` – _Required:_ .

The connection properties that are required as overrides for the compute
environment.

- `PhysicalConnectionPropertiesRequired` – Boolean.

Indicates whether `PhysicalConnectionProperties` are
required for the compute environment.

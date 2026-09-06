

# Connection Type API
<a name="aws-glue-api-catalog-connections-connections-type"></a>

The Connection Type API describes AWS Glue API to register, describe, delete and list connection types.

## Connection management APIs
<a name="aws-glue-api-catalog-connections-connections-type-connection-management"></a>
+ [RegisterConnectionType action (Python: register\_connection\_type)](#aws-glue-api-catalog-connections-connections-type-RegisterConnectionType)
+ [DeleteConnectionType action (Python: delete\_connection\_type)](#aws-glue-api-catalog-connections-connections-type-DeleteConnectionType)
+ [DescribeConnectionType action (Python: describe\_connection\_type)](#aws-glue-api-catalog-connections-connections-type-DescribeConnectionType)
+ [ListConnectionTypes action (Python: list\_connection\_types)](#aws-glue-api-catalog-connections-connections-type-ListConnectionTypes)
+ [ConnectionTypeBrief structure](#aws-glue-api-catalog-connections-connections-type-ConnectionTypeBrief)
+ [ConnectionTypeVariant structure](#aws-glue-api-catalog-connections-connections-type-ConnectionTypeVariant)

## RegisterConnectionType action (Python: register\_connection\_type)
<a name="aws-glue-api-catalog-connections-connections-type-RegisterConnectionType"></a>

Registers a custom connection type in AWS Glue based on the configuration provided. This operation enables customers to configure custom connectors for any data source with REST-based APIs, eliminating the need for building custom Lambda connectors.

The registered connection type stores details about how requests and responses are interpreted by REST sources, including connection properties, authentication configuration, and REST configuration with entity definitions. Once registered, customers can create connections using this connection type and work with them the same way as natively supported AWS Glue connectors.

Supports multiple authentication types including Basic, OAuth2 (Client Credentials, JWT Bearer, Authorization Code), and Custom Auth configurations.

**Request**
+ `ConnectionType` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the connection type. Must be between 1 and 255 characters and must be prefixed with "REST-" to indicate it is a REST-based connector.
+ `IntegrationType` – *Required:* UTF-8 string (valid values: `REST`).

  The integration type for the connection. Currently only "REST" protocol is supported.
+ `Description` – UTF-8 string, not more than 1024 bytes long.

  A description of the connection type. Can be up to 2048 characters and provides details about the purpose and functionality of the connection type.
+ `ConnectionProperties` – *Required:* A [ConnectionPropertiesConfiguration](#aws-glue-api-catalog-connections-connections-type-ConnectionPropertiesConfiguration) object.

  Defines the base URL and additional request parameters needed during connection creation for this connection type.
+ `ConnectorAuthenticationConfiguration` – *Required:* A [ConnectorAuthenticationConfiguration](#aws-glue-api-catalog-connections-connections-type-ConnectorAuthenticationConfiguration) object.

  Defines the supported authentication types and required properties for this connection type, including Basic, OAuth2, and Custom authentication methods.
+ `RestConfiguration` – *Required:* A [RestConfiguration](#aws-glue-api-catalog-connections-connections-type-RestConfiguration) object.

  Defines the HTTP request and response configuration, validation endpoint, and entity configurations for REST API interactions.
+ `Tags` – A map array of key-value pairs, not more than 50 pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

  Each value is a UTF-8 string, not more than 256 bytes long.

  The tags you assign to the connection type.

**Response**

Contains the Amazon Resource Name (ARN) of the newly registered connection type.
+ `ConnectionTypeArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #47](aws-glue-api-common.md#regex_47).

  The Amazon Resource Name (ARN) of the registered connection type. This unique identifier can be used to reference the connection type in other AWS Glue operations.

**Errors**
+ `AlreadyExistsException`
+ `InvalidInputException`
+ `OperationTimeoutException`
+ `ResourceNumberLimitExceededException`
+ `InternalServiceException`

## DeleteConnectionType action (Python: delete\_connection\_type)
<a name="aws-glue-api-catalog-connections-connections-type-DeleteConnectionType"></a>

Deletes a custom connection type in AWS Glue.

The connection type must exist and be registered before it can be deleted. This operation supports cleanup of connection type resources and helps maintain proper lifecycle management of custom connection types.

**Request**
+ `ConnectionType` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the connection type to delete. Must reference an existing registered connection type.

**Response**
+ *No Response parameters.*

**Errors**
+ `EntityNotFoundException`
+ `InvalidInputException`
+ `OperationTimeoutException`
+ `InternalServiceException`
+ `AccessDeniedException`

## DescribeConnectionType action (Python: describe\_connection\_type)
<a name="aws-glue-api-catalog-connections-connections-type-DescribeConnectionType"></a>

The `DescribeConnectionType` API provides full details of the supported options for a given connection type in AWS Glue. The response includes authentication configuration details that show supported authentication types and properties, and RestConfiguration for custom REST-based connection types registered via `RegisterConnectionType`.

See also: `ListConnectionTypes`, `RegisterConnectionType`, `DeleteConnectionType`

**Request**
+ `ConnectionType` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the connection type to be described.

**Response**
+ `ConnectionType` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the connection type.
+ `Description` – UTF-8 string, not more than 1024 bytes long.

  A description of the connection type.
+ `Capabilities` – A [Capabilities](#aws-glue-api-catalog-connections-connections-type-Capabilities) object.

  The supported authentication types, data interface types (compute environments), and data operations of the connector.
+ `ConnectionProperties` – A map array of key-value pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

  Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property) object.

  Connection properties which are common across compute environments.
+ `ConnectionOptions` – A map array of key-value pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

  Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property) object.

  Returns properties that can be set when creating a connection in the `ConnectionInput.ConnectionProperties`. `ConnectionOptions` defines parameters that can be set in a Spark ETL script in the connection options map passed to a dataframe.
+ `AuthenticationConfiguration` – An [AuthConfiguration](#aws-glue-api-catalog-connections-connections-type-AuthConfiguration) object.

  The type of authentication used for the connection.
+ `ComputeEnvironmentConfigurations` – A map array of key-value pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

  Each value is a A [ComputeEnvironmentConfiguration](#aws-glue-api-catalog-connections-connections-type-ComputeEnvironmentConfiguration) object.

  The compute environments that are supported by the connection.
+ `PhysicalConnectionRequirements` – A map array of key-value pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

  Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property) object.

  Physical requirements for a connection, such as VPC, Subnet and Security Group specifications.
+ `AthenaConnectionProperties` – A map array of key-value pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

  Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property) object.

  Connection properties specific to the Athena compute environment.
+ `PythonConnectionProperties` – A map array of key-value pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

  Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property) object.

  Connection properties specific to the Python compute environment.
+ `SparkConnectionProperties` – A map array of key-value pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

  Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property) object.

  Connection properties specific to the Spark compute environment.
+ `RestConfiguration` – A [RestConfiguration](#aws-glue-api-catalog-connections-connections-type-RestConfiguration) object.

  HTTP request and response configuration, validation endpoint, and entity configurations for REST based data source.

**Errors**
+ `ValidationException`
+ `InvalidInputException`
+ `InternalServiceException`

## ListConnectionTypes action (Python: list\_connection\_types)
<a name="aws-glue-api-catalog-connections-connections-type-ListConnectionTypes"></a>

The `ListConnectionTypes` API provides a discovery mechanism to learn available connection types in AWS Glue. The response contains a list of connection types with high-level details of what is supported for each connection type, including both built-in connection types and custom connection types registered via `RegisterConnectionType`. The connection types listed are the set of supported options for the `ConnectionType` value in the `CreateConnection` API.

See also: `DescribeConnectionType`, `RegisterConnectionType`, `DeleteConnectionType`

**Request**
+ `MaxResults` – Number (integer), not less than 1 or more than 1000.

  The maximum number of results to return.
+ `NextToken` – UTF-8 string, not less than 1 or more than 2048 bytes long, matching the [Custom string pattern #11](aws-glue-api-common.md#regex_11).

  A continuation token, if this is a continuation call.

**Response**
+ `ConnectionTypes` – An array of [ConnectionTypeBrief](#aws-glue-api-catalog-connections-connections-type-ConnectionTypeBrief) objects.

  A list of `ConnectionTypeBrief` objects containing brief information about the supported connection types.
+ `NextToken` – UTF-8 string, not less than 1 or more than 2048 bytes long, matching the [Custom string pattern #11](aws-glue-api-common.md#regex_11).

  A continuation token, if the current list segment is not the last.

**Errors**
+ `InternalServiceException`

## ConnectionTypeBrief structure
<a name="aws-glue-api-catalog-connections-connections-type-ConnectionTypeBrief"></a>

Brief information about a supported connection type returned by the `ListConnectionTypes` API.

**Fields**
+ `ConnectionType` – UTF-8 string (valid values: `JDBC` \| `SFTP` \| `MONGODB` \| `KAFKA` \| `NETWORK` \| `MARKETPLACE` \| `CUSTOM` \| `SALESFORCE` \| `VIEW_VALIDATION_REDSHIFT` \| `VIEW_VALIDATION_ATHENA` \| `GOOGLEADS` \| `GOOGLESHEETS` \| `GOOGLEANALYTICS4` \| `SERVICENOW` \| `MARKETO` \| `SAPODATA` \| `ZENDESK` \| `JIRACLOUD` \| `NETSUITEERP` \| `HUBSPOT` \| `FACEBOOKADS` \| `INSTAGRAMADS` \| `ZOHOCRM` \| `SALESFORCEPARDOT` \| `SALESFORCEMARKETINGCLOUD` \| `ADOBEANALYTICS` \| `SLACK` \| `LINKEDIN` \| `MIXPANEL` \| `ASANA` \| `STRIPE` \| `SMARTSHEET` \| `DATADOG` \| `WOOCOMMERCE` \| `INTERCOM` \| `SNAPCHATADS` \| `PAYPAL` \| `QUICKBOOKS` \| `FACEBOOKPAGEINSIGHTS` \| `FRESHDESK` \| `TWILIO` \| `DOCUSIGNMONITOR` \| `FRESHSALES` \| `ZOOM` \| `GOOGLESEARCHCONSOLE` \| `SALESFORCECOMMERCECLOUD` \| `SAPCONCUR` \| `DYNATRACE` \| `MICROSOFTDYNAMIC365FINANCEANDOPS` \| `MICROSOFTTEAMS` \| `BLACKBAUDRAISEREDGENXT` \| `MAILCHIMP` \| `GITLAB` \| `PENDO` \| `PRODUCTBOARD` \| `CIRCLECI` \| `PIPEDIVE` \| `SENDGRID` \| `AZURECOSMOS` \| `AZURESQL` \| `BIGQUERY` \| `BLACKBAUD` \| `CLOUDERAHIVE` \| `CLOUDERAIMPALA` \| `CLOUDWATCH` \| `CLOUDWATCHMETRICS` \| `CMDB` \| `DATALAKEGEN2` \| `DB2` \| `DB2AS400` \| `DOCUMENTDB` \| `DOMO` \| `DYNAMODB` \| `GOOGLECLOUDSTORAGE` \| `HBASE` \| `KUSTOMER` \| `MICROSOFTDYNAMICS365CRM` \| `MONDAY` \| `MYSQL` \| `OKTA` \| `OPENSEARCH` \| `ORACLE` \| `PIPEDRIVE` \| `POSTGRESQL` \| `SAPHANA` \| `SQLSERVER` \| `SYNAPSE` \| `TERADATA` \| `TERADATANOS` \| `TIMESTREAM` \| `TPCDS` \| `VERTICA`).

  The name of the connection type.
+ `DisplayName` – UTF-8 string, not less than 1 or more than 128 bytes long.

  The human-readable name for the connection type that is displayed in the AWS Glue console.
+ `Vendor` – UTF-8 string, not less than 1 or more than 128 bytes long.

  The name of the vendor or provider that created or maintains this connection type.
+ `Description` – UTF-8 string, not more than 1024 bytes long.

  A description of the connection type.
+ `Categories` – An array of UTF-8 strings.

  A list of categories that this connection type belongs to. Categories help users filter and find appropriate connection types based on their use cases.
+ `Capabilities` – A [Capabilities](#aws-glue-api-catalog-connections-connections-type-Capabilities) object.

  The supported authentication types, data interface types (compute environments), and data operations of the connector.
+ `LogoUrl` – UTF-8 string.

  The URL of the logo associated with a connection type.
+ `ConnectionTypeVariants` – An array of [ConnectionTypeVariant](#aws-glue-api-catalog-connections-connections-type-ConnectionTypeVariant) objects.

  A list of variants available for this connection type. Different variants may provide specialized configurations for specific use cases or implementations of the same general connection type.

## ConnectionTypeVariant structure
<a name="aws-glue-api-catalog-connections-connections-type-ConnectionTypeVariant"></a>

Represents a variant of a connection type in AWS Glue. Connection type variants provide specific configurations and behaviors for different implementations of the same general connection type.

**Fields**
+ `ConnectionTypeVariantName` – UTF-8 string, not less than 1 or more than 128 bytes long.

  The unique identifier for the connection type variant. This name is used internally to identify the specific variant of a connection type. 
+ `DisplayName` – UTF-8 string, not less than 1 or more than 128 bytes long.

  The human-readable name for the connection type variant that is displayed in the AWS Glue console.
+ `Description` – UTF-8 string, not more than 1024 bytes long.

  A detailed description of the connection type variant, including its purpose, use cases, and any specific configuration requirements.
+ `LogoUrl` – UTF-8 string.

  The URL of the logo associated with a connection type variant.

## datatypes
<a name="aws-glue-api-catalog-connections-connections-type-connection-types"></a>
+ [Validation structure](#aws-glue-api-catalog-connections-connections-type-Validation)
+ [AuthConfiguration structure](#aws-glue-api-catalog-connections-connections-type-AuthConfiguration)
+ [Capabilities structure](#aws-glue-api-catalog-connections-connections-type-Capabilities)
+ [Property structure](#aws-glue-api-catalog-connections-connections-type-Property)
+ [AllowedValue structure](#aws-glue-api-catalog-connections-connections-type-AllowedValue)
+ [ComputeEnvironmentConfiguration structure](#aws-glue-api-catalog-connections-connections-type-ComputeEnvironmentConfiguration)

## Validation structure
<a name="aws-glue-api-catalog-connections-connections-type-Validation"></a>

Defines how a validation is performed on a connection property.

**Fields**
+ `ValidationType` – *Required:* UTF-8 string (valid values: `REGEX` \| `RANGE`).

  The type of validation to be performed, such as `REGEX`.
+ `Patterns` – An array of UTF-8 strings.

  A list of patterns that apply to the validation.
+ `Description` – *Required:* UTF-8 string, not less than 1 or more than 1024 bytes long.

  A description for the validation.
+ `MaxLength` – Number (integer).

  A maximum length for a string connection property.
+ `Maximum` – Number (integer).

  A maximum value when specifying a `RANGE` type of validation.
+ `Minimum` – Number (integer).

  A minimum value when specifying a `RANGE` type of validation.

## AuthConfiguration structure
<a name="aws-glue-api-catalog-connections-connections-type-AuthConfiguration"></a>

The authentication configuration for a connection returned by the `DescribeConnectionType` API.

**Fields**
+ `AuthenticationType` – *Required:* A [Property](#aws-glue-api-catalog-connections-connections-type-Property) object.

  The type of authentication for a connection.
+ `SecretArn` – A [Property](#aws-glue-api-catalog-connections-connections-type-Property) object.

  The Amazon Resource Name (ARN) for the Secrets Manager.
+ `OAuth2Properties` – A map array of key-value pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

  Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property) object.

  A map of key-value pairs for the OAuth2 properties. Each value is a a `Property` object.
+ `BasicAuthenticationProperties` – A map array of key-value pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

  Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property) object.

  A map of key-value pairs for the OAuth2 properties. Each value is a a `Property` object.
+ `CustomAuthenticationProperties` – A map array of key-value pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

  Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property) object.

  A map of key-value pairs for the custom authentication properties. Each value is a a `Property` object.

## Capabilities structure
<a name="aws-glue-api-catalog-connections-connections-type-Capabilities"></a>

Specifies the supported authentication types returned by the `DescribeConnectionType` API.

**Fields**
+ `SupportedAuthenticationTypes` – *Required:* An array of UTF-8 strings.

  A list of supported authentication types.
+ `SupportedDataOperations` – *Required:* An array of UTF-8 strings.

  A list of supported data operations.
+ `SupportedComputeEnvironments` – *Required:* An array of UTF-8 strings.

  A list of supported compute environments.

## Property structure
<a name="aws-glue-api-catalog-connections-connections-type-Property"></a>

An object that defines a connection type for a compute environment.

**Fields**
+ `Name` – *Required:* UTF-8 string, not less than 1 or more than 128 bytes long.

  The name of the property.
+ `Description` – *Required:* UTF-8 string, not more than 1024 bytes long.

  A description of the property.
+ `Required` – *Required:* Boolean.

  Indicates whether the property is required.
+ `DefaultValue` – UTF-8 string.

  The default value for the property.
+ `PropertyTypes` – *Required:* An array of UTF-8 strings.

  Describes the type of property.
+ `AllowedValues` – An array of [AllowedValue](#aws-glue-api-catalog-connections-connections-type-AllowedValue) objects.

  A list of `AllowedValue` objects representing the values allowed for the property.
+ `DataOperationScopes` – An array of UTF-8 strings.

  Indicates which data operations are applicable to the property.
+ `KeyOverride` – UTF-8 string.

  A key name to use when sending this property in API requests, if different from the display name.
+ `PropertyLocation` – UTF-8 string (valid values: `HEADER` \| `BODY` \| `QUERY_PARAM` \| `PATH`).

  Specifies where this property should be included in REST requests, such as in headers, query parameters, or request body.

## AllowedValue structure
<a name="aws-glue-api-catalog-connections-connections-type-AllowedValue"></a>

An object representing a value allowed for a property.

**Fields**
+ `Description` – UTF-8 string, not more than 1024 bytes long.

  A description of the allowed value.
+ `Value` – *Required:* UTF-8 string, not less than 1 or more than 128 bytes long.

  The value allowed for the property.

## ComputeEnvironmentConfiguration structure
<a name="aws-glue-api-catalog-connections-connections-type-ComputeEnvironmentConfiguration"></a>

An object containing configuration for a compute environment (such as Spark, Python or Athena) returned by the `DescribeConnectionType` API.

**Fields**
+ `Name` – *Required:* UTF-8 string, not less than 1 or more than 128 bytes long.

  A name for the compute environment configuration.
+ `Description` – *Required:* UTF-8 string, not more than 1024 bytes long.

  A description of the compute environment.
+ `ComputeEnvironment` – *Required:* UTF-8 string (valid values: `SPARK` \| `ATHENA` \| `PYTHON`).

  The type of compute environment.
+ `SupportedAuthenticationTypes` – *Required:* An array of UTF-8 strings.

  The supported authentication types for the compute environment.
+ `ConnectionOptions` – *Required:* A map array of key-value pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

  Each value is a A [Property](#aws-glue-api-catalog-connections-connections-type-Property) object.

  The parameters used as connection options for the compute environment.
+ `ConnectionPropertyNameOverrides` – *Required:* A map array of key-value pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

  Each value is a UTF-8 string, not less than 1 or more than 128 bytes long.

  The connection property name overrides for the compute environment.
+ `ConnectionOptionNameOverrides` – *Required:* A map array of key-value pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

  Each value is a UTF-8 string, not less than 1 or more than 128 bytes long.

  The connection option name overrides for the compute environment.
+ `ConnectionPropertiesRequiredOverrides` – *Required:* An array of UTF-8 strings.

  The connection properties that are required as overrides for the compute environment.
+ `PhysicalConnectionPropertiesRequired` – Boolean.

  Indicates whether `PhysicalConnectionProperties` are required for the compute environment.

## Custom connector data types
<a name="aws-glue-api-catalog-connections-connections-type-connector-types"></a>
+ [ConnectionPropertiesConfiguration structure](#aws-glue-api-catalog-connections-connections-type-ConnectionPropertiesConfiguration)
+ [ConnectorAuthenticationConfiguration structure](#aws-glue-api-catalog-connections-connections-type-ConnectorAuthenticationConfiguration)
+ [ConnectorProperty structure](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty)
+ [RestConfiguration structure](#aws-glue-api-catalog-connections-connections-type-RestConfiguration)
+ [SourceConfiguration structure](#aws-glue-api-catalog-connections-connections-type-SourceConfiguration)
+ [EntityConfiguration structure](#aws-glue-api-catalog-connections-connections-type-EntityConfiguration)
+ [ResponseConfiguration structure](#aws-glue-api-catalog-connections-connections-type-ResponseConfiguration)
+ [ResponseExtractionMapping structure](#aws-glue-api-catalog-connections-connections-type-ResponseExtractionMapping)
+ [PaginationConfiguration structure](#aws-glue-api-catalog-connections-connections-type-PaginationConfiguration)
+ [CursorConfiguration structure](#aws-glue-api-catalog-connections-connections-type-CursorConfiguration)
+ [OffsetConfiguration structure](#aws-glue-api-catalog-connections-connections-type-OffsetConfiguration)
+ [ExtractedParameter structure](#aws-glue-api-catalog-connections-connections-type-ExtractedParameter)
+ [FieldDefinition structure](#aws-glue-api-catalog-connections-connections-type-FieldDefinition)
+ [ConnectorOAuth2Properties structure](#aws-glue-api-catalog-connections-connections-type-ConnectorOAuth2Properties)
+ [ClientCredentialsProperties structure](#aws-glue-api-catalog-connections-connections-type-ClientCredentialsProperties)
+ [JWTBearerProperties structure](#aws-glue-api-catalog-connections-connections-type-JWTBearerProperties)
+ [ConnectorAuthorizationCodeProperties structure](#aws-glue-api-catalog-connections-connections-type-ConnectorAuthorizationCodeProperties)
+ [BasicAuthenticationProperties structure](#aws-glue-api-catalog-connections-connections-type-BasicAuthenticationProperties)
+ [CustomAuthenticationProperties structure](#aws-glue-api-catalog-connections-connections-type-CustomAuthenticationProperties)
+ [FilterConfiguration structure](#aws-glue-api-catalog-connections-connections-type-FilterConfiguration)
+ [FilterOverrides structure](#aws-glue-api-catalog-connections-connections-type-FilterOverrides)
+ [BetweenConfiguration structure](#aws-glue-api-catalog-connections-connections-type-BetweenConfiguration)
+ [FilterStringConfiguration structure](#aws-glue-api-catalog-connections-connections-type-FilterStringConfiguration)

## ConnectionPropertiesConfiguration structure
<a name="aws-glue-api-catalog-connections-connections-type-ConnectionPropertiesConfiguration"></a>

Configuration that defines the base URL and additional request parameters needed during connection creation.

**Fields**
+ `Url` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The base instance URL for the endpoint that this connection type will connect to.
+ `AdditionalRequestParameters` – An array of [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) objects.

  Key-value pairs of additional request parameters that may be needed during connection creation, such as API versions or service-specific configuration options.

## ConnectorAuthenticationConfiguration structure
<a name="aws-glue-api-catalog-connections-connections-type-ConnectorAuthenticationConfiguration"></a>

Configuration that defines the supported authentication types and required properties for the connection type.

**Fields**
+ `AuthenticationTypes` – *Required:* An array of UTF-8 strings.

  A list of authentication types supported by this connection type, such as Basic, OAuth2, or Custom authentication methods.

## ConnectorProperty structure
<a name="aws-glue-api-catalog-connections-connections-type-ConnectorProperty"></a>

Defines a property configuration for connection types, default values, and where the property should be used in requests.

**Fields**
+ `Name` – *Required:* UTF-8 string, not less than 1 or more than 128 bytes long.

  The name of the property.
+ `KeyOverride` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #15](aws-glue-api-common.md#regex_15).

  A key name to use when sending this property in API requests, if different from the display name.
+ `Required` – *Required:* Boolean.

  Indicates whether the property is required.
+ `DefaultValue` – UTF-8 string.

  The default value for the property.
+ `AllowedValues` – An array of UTF-8 strings.

  A list of `AllowedValue` objects representing the values allowed for the property.
+ `PropertyLocation` – UTF-8 string (valid values: `HEADER` \| `BODY` \| `QUERY_PARAM` \| `PATH`).

  Specifies where this property should be included in REST requests, such as in headers, query parameters, or request body.
+ `PropertyType` – *Required:* UTF-8 string (valid values: `USER_INPUT` \| `SECRET` \| `READ_ONLY` \| `UNUSED` \| `SECRET_OR_USER_INPUT`).

  The data type of this property
+ `Format` – UTF-8 string.

  A format template for the property value that defines how the value should be formatted before sending it in API requests. Use `{value}` as a placeholder for the actual property value (for example, `SSWS {value}`).

## RestConfiguration structure
<a name="aws-glue-api-catalog-connections-connections-type-RestConfiguration"></a>

Configuration that defines HTTP request and response handling, validation endpoints, and entity configurations for REST API interactions.

**Fields**
+ `GlobalSourceConfiguration` – A [SourceConfiguration](#aws-glue-api-catalog-connections-connections-type-SourceConfiguration) object.

  Global configuration settings that apply to all REST API requests for this connection type, including common request methods, paths, and parameters.
+ `ValidationEndpointConfiguration` – A [SourceConfiguration](#aws-glue-api-catalog-connections-connections-type-SourceConfiguration) object.

  Configuration for the endpoint used to validate connection credentials and test connectivity during connection creation.
+ `EntityConfigurations` – A map array of key-value pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #12](aws-glue-api-common.md#regex_12).

  Each value is a An [EntityConfiguration](#aws-glue-api-catalog-connections-connections-type-EntityConfiguration) object.

  A map of entity configurations that define how to interact with different data entities available through the REST API, including their schemas and access patterns.

## SourceConfiguration structure
<a name="aws-glue-api-catalog-connections-connections-type-SourceConfiguration"></a>

Configuration that defines how to make requests to endpoints, including request methods, paths, parameters, and response handling.

**Fields**
+ `RequestMethod` – UTF-8 string (valid values: `GET` \| `POST`).

  The HTTP method to use for requests to this endpoint, such as GET, POST.
+ `RequestPath` – UTF-8 string, not less than 1 or more than 512 bytes long, matching the [Custom string pattern #14](aws-glue-api-common.md#regex_14).

  The URL path for the REST endpoint, which may include parameter placeholders that will be replaced with actual values during requests.
+ `RequestParameters` – An array of [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) objects.

  Configuration for request parameters that should be included in API calls, such as query parameters, headers, or body content.
+ `ResponseConfiguration` – A [ResponseConfiguration](#aws-glue-api-catalog-connections-connections-type-ResponseConfiguration) object.

  Configuration that defines how to parse and extract data from API responses, including success and error handling.
+ `PaginationConfiguration` – A [PaginationConfiguration](#aws-glue-api-catalog-connections-connections-type-PaginationConfiguration) object.

  Configuration for handling paginated responses from the REST API, supporting both cursor-based and offset-based pagination strategies.
+ `FilterConfiguration` – A [FilterConfiguration](#aws-glue-api-catalog-connections-connections-type-FilterConfiguration) object.

  Configuration for applying filter pushdown to REST API requests, defining how filter predicates are translated into query parameters or filter strings.

## EntityConfiguration structure
<a name="aws-glue-api-catalog-connections-connections-type-EntityConfiguration"></a>

Configuration that defines how to interact with a specific data entity through the REST API, including its access patterns and schema definition.

**Fields**
+ `SourceConfiguration` – A [SourceConfiguration](#aws-glue-api-catalog-connections-connections-type-SourceConfiguration) object.

  The source configuration that defines how to make requests to access this entity's data through the REST API.
+ `Schema` – A map array of key-value pairs.

  Each key is a UTF-8 string, at least 1 byte long.

  Each value is a A [FieldDefinition](#aws-glue-api-catalog-connections-connections-type-FieldDefinition) object.

  The schema definition for this entity, including field names, types, and other metadata that describes the structure of the data.

## ResponseConfiguration structure
<a name="aws-glue-api-catalog-connections-connections-type-ResponseConfiguration"></a>

Configuration that defines how to parse JSON responses from REST API calls, including paths to result data and error information.

**Fields**
+ `ResultPath` – *Required:* UTF-8 string, not less than 1 or more than 512 bytes long, matching the [Custom string pattern #10](aws-glue-api-common.md#regex_10).

  The JSON path expression that identifies where the actual result data is located within the API response.
+ `ErrorPath` – UTF-8 string, not less than 1 or more than 512 bytes long, matching the [Custom string pattern #10](aws-glue-api-common.md#regex_10).

  The JSON path expression that identifies where error information is located within API responses when requests fail.

## ResponseExtractionMapping structure
<a name="aws-glue-api-catalog-connections-connections-type-ResponseExtractionMapping"></a>

Configuration that defines how to extract values from HTTP response content or headers for use in subsequent requests or parameter mapping.

**Fields**
+ `ContentPath` – UTF-8 string, not less than 1 or more than 512 bytes long, matching the [Custom string pattern #10](aws-glue-api-common.md#regex_10).

  A JSON path expression that specifies how to extract a value from the response body content.
+ `HeaderKey` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #15](aws-glue-api-common.md#regex_15).

  The name of an HTTP response header from which to extract the value.

## PaginationConfiguration structure
<a name="aws-glue-api-catalog-connections-connections-type-PaginationConfiguration"></a>

Configuration that defines how to handle paginated responses from REST APIs, supporting different pagination strategies used by various services.

**Fields**
+ `CursorConfiguration` – A [CursorConfiguration](#aws-glue-api-catalog-connections-connections-type-CursorConfiguration) object.

  Configuration for cursor-based pagination, where the API provides a cursor or token to retrieve the next page of results.
+ `OffsetConfiguration` – An [OffsetConfiguration](#aws-glue-api-catalog-connections-connections-type-OffsetConfiguration) object.

  Configuration for offset-based pagination, where the API uses numeric offsets and limits to control which results are returned.

## CursorConfiguration structure
<a name="aws-glue-api-catalog-connections-connections-type-CursorConfiguration"></a>

Cursor-based pagination configuration that defines how to handle pagination using cursor tokens or next page identifiers.

**Fields**
+ `NextPage` – *Required:* An [ExtractedParameter](#aws-glue-api-catalog-connections-connections-type-ExtractedParameter) object.

  The parameter name or JSON path that contains the cursor or token for retrieving the next page of results.
+ `LimitParameter` – An [ExtractedParameter](#aws-glue-api-catalog-connections-connections-type-ExtractedParameter) object.

  The parameter name used to specify the maximum number of results to return per page.

## OffsetConfiguration structure
<a name="aws-glue-api-catalog-connections-connections-type-OffsetConfiguration"></a>

Offset-based pagination configuration that defines how to handle pagination using numeric offsets and limits.

**Fields**
+ `OffsetParameter` – *Required:* An [ExtractedParameter](#aws-glue-api-catalog-connections-connections-type-ExtractedParameter) object.

  The parameter name used to specify the starting position or offset for retrieving results.
+ `LimitParameter` – *Required:* An [ExtractedParameter](#aws-glue-api-catalog-connections-connections-type-ExtractedParameter) object.

  The parameter name used to specify the maximum number of results to return per page.

## ExtractedParameter structure
<a name="aws-glue-api-catalog-connections-connections-type-ExtractedParameter"></a>

Parameter extraction configuration that defines how to extract and map values from API responses to request parameters.

**Fields**
+ `Key` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #15](aws-glue-api-common.md#regex_15).

  The parameter key name that will be used in subsequent requests.
+ `DefaultValue` – UTF-8 string, not less than 1 or more than 1024 bytes long, matching the [Custom string pattern #16](aws-glue-api-common.md#regex_16).

  The default value to use if the parameter cannot be extracted from the response.
+ `PropertyLocation` – UTF-8 string (valid values: `HEADER` \| `BODY` \| `QUERY_PARAM` \| `PATH`).

  Specifies where this extracted parameter should be placed in subsequent requests, such as in headers, query parameters, or request body.
+ `Value` – A [ResponseExtractionMapping](#aws-glue-api-catalog-connections-connections-type-ResponseExtractionMapping) object.

  The JSON path or extraction mapping that defines how to extract the parameter value from API responses.

## FieldDefinition structure
<a name="aws-glue-api-catalog-connections-connections-type-FieldDefinition"></a>

Defines a field in an entity schema for REST connector data sources, specifying the field name and data type.

**Fields**
+ `Name` – *Required:* UTF-8 string.

  The name of the field in the entity schema.
+ `FieldDataType` – *Required:* UTF-8 string (valid values: `INT` \| `SMALLINT` \| `BIGINT` \| `FLOAT` \| `LONG` \| `DATE` \| `BOOLEAN` \| `MAP` \| `ARRAY` \| `STRING` \| `TIMESTAMP` \| `DECIMAL` \| `BYTE` \| `SHORT` \| `DOUBLE` \| `STRUCT` \| `BINARY` \| `UNION`).

  The data type of the field.
+ `ResponseDateFormat` – UTF-8 string.

  The format pattern for parsing date values from API responses. Required when the API uses a non-ISO-8601 format. Accepts Java `DateTimeFormatter` patterns (for example, `EEE, d MMM yyyy HH:mm:ss Z`), `EPOCH_SECONDS` for Unix epoch seconds, or `EPOCH_MILLIS` for Unix epoch milliseconds.
+ `IsPartitionable` – Boolean.

  Indicates whether this field can be used for partitioning queries to the data source.
+ `IsNullable` – Boolean.

  Indicates whether this field can contain null values.
+ `IsQueryable` – Boolean.

  Indicates whether this field can be used in filter predicates when querying data.
+ `IsOrderable` – Boolean.

  Indicates whether this field can be used for ordering results.
+ `FilterOverrides` – A [FilterOverrides](#aws-glue-api-catalog-connections-connections-type-FilterOverrides) object.

  Per-field overrides for filter behavior, allowing customization of how filters are applied to this specific field.

## ConnectorOAuth2Properties structure
<a name="aws-glue-api-catalog-connections-connections-type-ConnectorOAuth2Properties"></a>

OAuth2 configuration container that defines the authentication properties and flow-specific configurations for OAuth2-based connections.

**Fields**
+ `OAuth2GrantType` – *Required:* UTF-8 string (valid values: `CLIENT_CREDENTIALS` \| `JWT_BEARER` \| `AUTHORIZATION_CODE`).

  The OAuth2 grant type to use for authentication, such as CLIENT\_CREDENTIALS, JWT\_BEARER, or AUTHORIZATION\_CODE.
+ `ClientCredentialsProperties` – A [ClientCredentialsProperties](#aws-glue-api-catalog-connections-connections-type-ClientCredentialsProperties) object.

  Configuration properties specific to the OAuth2 Client Credentials grant type flow.
+ `JWTBearerProperties` – A [JWTBearerProperties](#aws-glue-api-catalog-connections-connections-type-JWTBearerProperties) object.

  Configuration properties specific to the OAuth2 JWT Bearer grant type flow.
+ `AuthorizationCodeProperties` – A [ConnectorAuthorizationCodeProperties](#aws-glue-api-catalog-connections-connections-type-ConnectorAuthorizationCodeProperties) object.

  Configuration properties specific to the OAuth2 Authorization Code grant type flow.

## ClientCredentialsProperties structure
<a name="aws-glue-api-catalog-connections-connections-type-ClientCredentialsProperties"></a>

OAuth2 client credentials configuration that defines the properties needed for the Client Credentials grant type flow.

**Fields**
+ `TokenUrl` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The token endpoint URL where the client will request access tokens using client credentials.
+ `RequestMethod` – UTF-8 string (valid values: `GET` \| `POST`).

  The HTTP method to use when making token requests, typically POST.
+ `ContentType` – UTF-8 string (valid values: `APPLICATION_JSON` \| `URL_ENCODED`).

  The content type to use for token requests, such as application/x-www-form-urlencoded or application/json.
+ `ClientId` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The OAuth2 client identifier provided by the authorization server.
+ `ClientSecret` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The OAuth2 client secret provided by the authorization server.
+ `Scope` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The OAuth2 scope that defines the level of access requested for the client credentials flow.
+ `TokenUrlParameters` – An array of [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) objects.

  Additional parameters to include in token URL requests as key-value pairs.

## JWTBearerProperties structure
<a name="aws-glue-api-catalog-connections-connections-type-JWTBearerProperties"></a>

JWT bearer token configuration that defines the properties needed for the JWT Bearer grant type flow.

**Fields**
+ `TokenUrl` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The token endpoint URL where the JWT bearer token will be exchanged for an access token.
+ `RequestMethod` – UTF-8 string (valid values: `GET` \| `POST`).

  The HTTP method to use when making JWT bearer token requests, typically POST.
+ `ContentType` – UTF-8 string (valid values: `APPLICATION_JSON` \| `URL_ENCODED`).

  The content type to use for JWT bearer token requests, such as application/x-www-form-urlencoded or application/json.
+ `JwtToken` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The JWT token to be used in the bearer token grant flow for authentication.
+ `TokenUrlParameters` – An array of [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) objects.

  Additional parameters to include in token URL requests as key-value pairs.

## ConnectorAuthorizationCodeProperties structure
<a name="aws-glue-api-catalog-connections-connections-type-ConnectorAuthorizationCodeProperties"></a>

OAuth2 authorization code configuration that defines the properties needed for the Authorization Code grant type flow.

**Fields**
+ `AuthorizationCodeUrl` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The authorization endpoint URL where users will be redirected to grant authorization.
+ `AuthorizationCode` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The authorization code received from the authorization server after user consent.
+ `RedirectUri` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The redirect URI that must match the URI registered with the authorization server.
+ `TokenUrl` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The token endpoint URL where the authorization code will be exchanged for an access token.
+ `RequestMethod` – UTF-8 string (valid values: `GET` \| `POST`).

  The HTTP method to use when making token exchange requests, typically POST.
+ `ContentType` – UTF-8 string (valid values: `APPLICATION_JSON` \| `URL_ENCODED`).

  The content type to use for token exchange requests, such as application/x-www-form-urlencoded or application/json.
+ `ClientId` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The OAuth2 client identifier provided by the authorization server.
+ `ClientSecret` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The OAuth2 client secret provided by the authorization server.
+ `Scope` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The OAuth2 scope that defines the level of access requested for the authorization code flow.
+ `Prompt` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The OAuth2 prompt parameter that controls the authorization server's behavior during user authentication.
+ `TokenUrlParameters` – An array of [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) objects.

  Additional parameters to include in token URL requests as key-value pairs.

## BasicAuthenticationProperties structure
<a name="aws-glue-api-catalog-connections-connections-type-BasicAuthenticationProperties"></a>

Basic authentication configuration that defines the username and password properties for HTTP Basic authentication.

**Fields**
+ `Username` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The username property name to use for Basic authentication credentials.
+ `Password` – A [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) object.

  The password property name to use for Basic authentication credentials.

## CustomAuthenticationProperties structure
<a name="aws-glue-api-catalog-connections-connections-type-CustomAuthenticationProperties"></a>

Custom authentication configuration that allows for flexible authentication mechanisms beyond standard Basic and OAuth2 flows.

**Fields**
+ `AuthenticationParameters` – *Required:* An array of [ConnectorProperty](#aws-glue-api-catalog-connections-connections-type-ConnectorProperty) objects.

  A map of custom authentication parameters that define the specific authentication mechanism and required properties.

## FilterConfiguration structure
<a name="aws-glue-api-catalog-connections-connections-type-FilterConfiguration"></a>

Configuration that defines how filter predicates are applied to REST API requests, supporting both query parameter and filter string strategies.

**Fields**
+ `FilterMode` – *Required:* UTF-8 string (valid values: `QUERY_PARAMS` \| `FILTER_STRING`).

  The strategy for applying filters to requests. Use `QUERY_PARAMS` to pass filters as individual query parameters, or `FILTER_STRING` to construct a single filter expression string.
+ `OperatorMappings` – A map array of key-value pairs.

  Each key is a UTF-8 string.

  Each value is a UTF-8 string.

  A map of logical filter operators to their API-specific string representations. Supported operator keys are: `EQUAL_TO`, `NOT_EQUAL_TO`, `LESS_THAN`, `GREATER_THAN`, `LESS_THAN_OR_EQUAL_TO`, `GREATER_THAN_OR_EQUAL_TO`, `CONTAINS`, `BETWEEN`, `AND`, and `OR`.
+ `DateTimeFormat` – UTF-8 string.

  The global date and time format for filter expressions. Accepts Java `DateTimeFormatter` patterns (for example, `EEE, d MMM yyyy HH:mm:ss Z`), `EPOCH_SECONDS` for Unix epoch seconds, or `EPOCH_MILLIS` for Unix epoch milliseconds. If not specified, values are passed as-is in ISO-8601 format.
+ `StripQuotes` – Boolean.

  Indicates whether surrounding double quotes should be stripped from filter values before processing.
+ `BetweenConfiguration` – A [BetweenConfiguration](#aws-glue-api-catalog-connections-connections-type-BetweenConfiguration) object.

  Configuration for handling BETWEEN range filter operations.
+ `FilterStringConfiguration` – A [FilterStringConfiguration](#aws-glue-api-catalog-connections-connections-type-FilterStringConfiguration) object.

  Configuration for constructing filter expressions when `FilterMode` is set to `FILTER_STRING`.

## FilterOverrides structure
<a name="aws-glue-api-catalog-connections-connections-type-FilterOverrides"></a>

Configuration that defines per-field overrides for filter behavior, allowing individual fields to customize how filter operations are applied.

**Fields**
+ `FieldName` – UTF-8 string.

  An override for the field name to use in filter expressions, if different from the schema field name.
+ `OperatorMappings` – A map array of key-value pairs.

  Each key is a UTF-8 string.

  Each value is a UTF-8 string.

  A map of logical filter operators to their field-specific API representations, overriding the global operator mappings. Supported operator keys are: `EQUAL_TO`, `NOT_EQUAL_TO`, `LESS_THAN`, `GREATER_THAN`, `LESS_THAN_OR_EQUAL_TO`, `GREATER_THAN_OR_EQUAL_TO`, `CONTAINS`, `BETWEEN`, `AND`, and `OR`.
+ `BetweenConfiguration` – A [BetweenConfiguration](#aws-glue-api-catalog-connections-connections-type-BetweenConfiguration) object.

  Field-specific configuration for handling BETWEEN range filter operations.
+ `DateTimeFormat` – UTF-8 string.

  The date and time format for filter expressions on this field, overriding the global `DateTimeFormat`. Accepts Java `DateTimeFormatter` patterns (for example, `EEE, d MMM yyyy HH:mm:ss Z`), `EPOCH_SECONDS` for Unix epoch seconds, or `EPOCH_MILLIS` for Unix epoch milliseconds.

## BetweenConfiguration structure
<a name="aws-glue-api-catalog-connections-connections-type-BetweenConfiguration"></a>

Configuration that defines how BETWEEN range filter operations are translated into REST API request parameters.

**Fields**
+ `LowBoundKey` – UTF-8 string.

  The parameter name used for the lower bound value in a BETWEEN filter operation.
+ `HighBoundKey` – UTF-8 string.

  The parameter name used for the upper bound value in a BETWEEN filter operation.
+ `Template` – UTF-8 string.

  A template string for constructing the BETWEEN filter expression.

## FilterStringConfiguration structure
<a name="aws-glue-api-catalog-connections-connections-type-FilterStringConfiguration"></a>

Configuration for constructing filter expression strings when using the `FILTER_STRING` filter mode.

**Fields**
+ `QueryParameterName` – *Required:* UTF-8 string.

  The query parameter name used to send the constructed filter expression string in API requests.
+ `QuoteStringValues` – Boolean.

  Indicates whether string and date values should be wrapped with a quote character in the filter expression.
+ `QuoteCharacter` – UTF-8 string.

  The character used to quote values when `QuoteStringValues` is true. Defaults to double quotes if not specified.
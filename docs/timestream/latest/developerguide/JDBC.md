For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Connection properties

The Timestream for LiveAnalytics JDBC driver supports the following options:

###### Topics

- [Basic authentication
  options](#JDBC.connection-properties.basic-auth "#JDBC.connection-properties.basic-auth")
- [Standard client info
  option](#JDBC.connection-properties.standard-client "#JDBC.connection-properties.standard-client")
- [Driver configuration
  option](#JDBC.connection-properties.driver-config "#JDBC.connection-properties.driver-config")
- [SDK option](#JDBC.connection-properties.sdk-options "#JDBC.connection-properties.sdk-options")
- [Endpoint configuration
  option](#JDBC.connection-properties.endpoint-config "#JDBC.connection-properties.endpoint-config")
- [Credential provider
  options](#JDBC.connection-properties.cred-providers "#JDBC.connection-properties.cred-providers")
- [SAML-based authentication options
  for Okta](#JDBC.connection-properties.okta "#JDBC.connection-properties.okta")
- [SAML-based authentication
  options for Azure AD](#JDBC.connection-properties.azure-ad "#JDBC.connection-properties.azure-ad")

###### Note

If none of the properties are provided, the Timestream for LiveAnalytics JDBC driver will use the
default credentials chain to load the credentials.

###### Note

All property keys are case-sensitive.

## Basic authentication

options

The following table describes the available Basic Authentication options.

| Option          | Description                                                                                                  | Default |
| --------------- | ------------------------------------------------------------------------------------------------------------ | ------- |
| AccessKeyId     | The AWS user access key id.                                                                                  | NONE    |
| SecretAccessKey | The AWS user secret access key.                                                                              | NONE    |
| SessionToken    | The temporary session token required to access a database with<br>multi-factor authentication (MFA) enabled. | NONE    |

## Standard client info

option

The following table describes the Standard Client Info Option.

| Option          | Description                                                                                                                                                                                         | Default                                      |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| ApplicationName | The name of the application currently utilizing the<br>connection. `ApplicationName` is used for debugging<br>purposes and will not be communicated to the Timestream for LiveAnalytics<br>service. | The application name detected by the driver. |

## Driver configuration

option

The following table describes the Driver Configuration Option.

| Option                          | Description                                                                                                                                                                                                   | Default   |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| EnableMetaDataPreparedStatement | Enables Timestream for LiveAnalytics JDBC driver to return metadata for<br>`PreparedStatements`, but this will incur an<br>additional cost with Timestream for LiveAnalytics when retrieving the<br>metadata. | FALSE     |
| Region                          | The database's region.                                                                                                                                                                                        | us-east-1 |

## SDK option

The following table describes the SDK Option.

| Option              | Description                                                                                                                                                                                       | Default |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| RequestTimeout      | The time in milliseconds the AWS SDK will wait for a query<br>request before timing out. Non-positive value disables request<br>timeout.                                                          | 0       |
| SocketTimeout       | The time in milliseconds the AWS SDK will wait for data to be<br>transferred over an open connection before timing out. Value<br>must be non-negative. A value of `0` disables socket<br>timeout. | 50000   |
| MaxRetryCountClient | The maximum number of retry attempts for retryable errors with<br>5XX error codes in the SDK. The value must be<br>non-negative.                                                                  | NONE    |
| MaxConnections      | The maximum number of allowed concurrently opened HTTP<br>connections to the Timestream for LiveAnalytics service. The value must be<br>positive.                                                 | 50      |

## Endpoint configuration

option

The following table describes the Endpoint Configuration Option.

| Option   | Description                                                | Default |
| -------- | ---------------------------------------------------------- | ------- |
| Endpoint | The endpoint for the Timestream for LiveAnalytics service. | NONE    |

## Credential provider

options

The following table describes the available Credential Provider options.

| Option                      | Description                                                                                                                                                                                                             | Default |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| AwsCredentialsProviderClass | One of `PropertiesFileCredentialsProvider` or<br>`InstanceProfileCredentialsProvider` to use for<br>authentication.                                                                                                     | NONE    |
| CustomCredentialsFilePath   | The path to a properties file containing AWS security<br>credentials `accessKey` and `secretKey`.<br>This is only required if<br>`AwsCredentialsProviderClass` is specified as<br>`PropertiesFileCredentialsProvider` . | NONE    |

## SAML-based authentication options

for Okta

The following table describes the available SAML-based authentication options for
Okta.

| Option            | Description                                                                                                                                                                                                                                                         | Default |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| IdpName           | The Identity Provider (Idp) name to use for SAML-based<br>authentication. One of `Okta` or `AzureAD`.                                                                                                                                                               | NONE    |
| IdpHost           | The host name of the specified Idp.                                                                                                                                                                                                                                 | NONE    |
| IdpUserName       | The user name for the specified Idp account.                                                                                                                                                                                                                        | NONE    |
| IdpPassword       | The password for the specified Idp account.                                                                                                                                                                                                                         | NONE    |
| OktaApplicationID | The unique Okta-provided ID associated with the Timestream for LiveAnalytics<br>application. `AppId` can be found in the<br>`entityID` field provided in the application<br>metadata. Consider the following example: `entityID =<br>http://www.okta.com//IdpAppID` | NONE    |
| RoleARN           | The Amazon Resource Name (ARN) of the role that the caller is<br>assuming.                                                                                                                                                                                          | NONE    |
| IdpARN            | The Amazon Resource Name (ARN) of the SAML provider in IAM<br>that describes the Idp.                                                                                                                                                                               | NONE    |

## SAML-based authentication

options for Azure AD

The following table describes the available SAML-based authentication options for
Azure AD.

| Option           | Description                                                                                                    | Default |
| ---------------- | -------------------------------------------------------------------------------------------------------------- | ------- |
| IdpName          | The Identity Provider (Idp) name to use for SAML-based<br>authentication. One of `Okta` or `AzureAD`<br>.      | NONE    |
| IdpHost          | The host name of the specified Idp.                                                                            | NONE    |
| IdpUserName      | The user name for the specified Idp account.                                                                   | NONE    |
| IdpPassword      | The password for the specified Idp account.                                                                    | NONE    |
| AADApplicationID | The unique id of the registered application on Azure<br>AD.                                                    | NONE    |
| AADClientSecret  | The client secret associated with the registered application<br>on Azure AD used to authorize fetching tokens. | NONE    |
| AADTenant        | The Azure AD Tenant ID.                                                                                        | NONE    |
| IdpARN           | The Amazon Resource Name (ARN) of the SAML provider in IAM<br>that describes the Idp.                          | NONE    |

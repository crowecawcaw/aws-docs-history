For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# JDBC URL examples

This section describes how to create a JDBC connection URL, and provides examples. To
specify the [optional connection
properties](JDBC.md "JDBC.md"), use the following URL format:

```
jdbc:timestream://PropertyName1=value1;PropertyName2=value2...
```

###### Note

All connection properties are optional. All property keys are
case-sensitive.

Below are some examples of JDBC connection URLs.

_Example with basic authentication options and region:_

```
jdbc:timestream://AccessKeyId=<myAccessKeyId>;SecretAccessKey=<mySecretAccessKey>;SessionToken=<mySessionToken>;Region=us-east-1
```

_Example with client info, region and SDK options:_

```
jdbc:timestream://ApplicationName=MyApp;Region=us-east-1;MaxRetryCountClient=10;MaxConnections=5000;RequestTimeout=20000
```

_Connect using the default credential provider chain with AWS credential set in
environment variables:_

```
jdbc:timestream
```

_Connect using the default credential provider chain with AWS credential set in
the connection URL:_

```
jdbc:timestream://AccessKeyId=<myAccessKeyId>;SecretAccessKey=<mySecretAccessKey>;SessionToken=<mySessionToken>
```

_Connect using the PropertiesFileCredentialsProvider as the authentication
method:_

```
jdbc:timestream://AwsCredentialsProviderClass=PropertiesFileCredentialsProvider;CustomCredentialsFilePath=<path to properties file>
```

_Connect using the InstanceProfileCredentialsProvider as the authentication
method:_

```
jdbc:timestream://AwsCredentialsProviderClass=InstanceProfileCredentialsProvider
```

_Connect using the Okta credentials as the authentication method:_

```
jdbc:timestream://IdpName=Okta;IdpHost=<host>;IdpUserName=<name>;IdpPassword=<password>;OktaApplicationID=<id>;RoleARN=<roleARN>;IdpARN=<IdpARN>
```

_Connect using the Azure AD credentials as the authentication method:_

```
jdbc:timestream://IdpName=AzureAD;IdpUserName=<name>;IdpPassword=<password>;AADApplicationID=<id>;AADClientSecret=<secret>;AADTenant=<tenantID>;IdpARN=<IdpARN>
```

_Connect with a specific endpoint:_

```
jdbc:timestream://Endpoint=abc.us-east-1.amazonaws.com;Region=us-east-1
```

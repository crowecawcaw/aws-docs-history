For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Connection string examples for the Timestream for LiveAnalytics ODBC driver

## Example of connecting to the ODBC driver with IAM credentials

```
Driver={Amazon Timestream ODBC Driver};Auth=IAM;AccessKeyId=``(your access key ID)``;secretKey=`(your secret key)`;SessionToken=(your session token);Region=`us-east-2`;
```

## Example of connecting to the ODBC driver with a profile

```
Driver={Amazon Timestream ODBC Driver};ProfileName=`(the profile name)`;region=us-west-2;
```

The driver will attempt to connect using the credentials provided in `~/.aws/credentials`,
or if a file is specified in the environment variable `AWS_SHARED_CREDENTIALS_FILE`, using
the credentials in that file.

## Example of connecting to the ODBC driver with Okta

```
driver={Amazon Timestream ODBC Driver};auth=okta;region=us-west-2;idPHost=`(your host at Okta)`;idPUsername=`(your user name)`;idPPassword=`(your password)`;OktaApplicationID=`(your Okta AppId)`;roleARN=`(your role ARN)`;idPARN=`(your Idp ARN)`;
```

## Example of connecting to the ODBC driver with Azure Active Directory (AAD)

```
driver={Amazon Timestream ODBC Driver};auth=aad;region=us-west-2;idPUsername=`(your user name)`;idPPassword=`(your password)`;aadApplicationID=`(your AAD AppId)`;aadClientSecret=`(your AAD client secret)`;aadTenant=`(your AAD tenant)`;roleARN=`(your role ARN)`;idPARN=`(your idP ARN)`;
```

## Example of connecting to the ODBC driver with a specified endpoint and a log level of 2 (WARNING)

```
Driver={Amazon Timestream ODBC Driver};Auth=IAM;AccessKeyId=`(your access key ID)`;secretKey=`(your secret key)`;EndpointOverride=ingest.timestream.us-west-2.amazonaws.com;Region=us-east-2;LogLevel=2;
```

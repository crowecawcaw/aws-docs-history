# Connection string examples for the AWS IoT SiteWise ODBC driver

## Example of connecting to the ODBC driver with IAM credentials

```
Driver={AWS IoT SiteWise ODBC Driver};Auth=`IAM`;AccessKeyId=``(your access key ID)``;SecretKey=`(your secret key)`;SessionToken=`(your session token)`;Region=`us-east-1`;
```

## Example of connecting to the ODBC driver with a profile

```
Driver={AWS IoT SiteWise ODBC Driver};ProfileName=`(the profile name)`;region=`us-east-1`;
```

The driver will attempt to connect using the credentials provided in `~/.aws/credentials`,
or if a file is specified in the environment variable `AWS_SHARED_CREDENTIALS_FILE`, using
the credentials in that file.

## Example of connecting to the ODBC driver with Okta

```
Driver={AWS IoT SiteWise ODBC Driver};Auth=`OKTA`;region=`us-east-1`;idPHost=`(your host at Okta)`;idPUsername=`(your user name)`;idPPassword=`(your password)`;OktaApplicationID=`(your Okta AppId)`;roleARN=`(your role ARN)`;idPARN=`(your Idp ARN)`;
```

## Example of connecting to the ODBC driver with Azure Active Directory (AAD)

```
Driver={AWS IoT SiteWise ODBC Driver};Auth=`AAD`;region=`us-east-1`;idPUsername=`(your user name)`;idPPassword=`(your password)`;aadApplicationID=`(your AAD AppId)`;aadClientSecret=`(your AAD client secret)`;aadTenant=`(your AAD tenant)`;roleARN=`(your role ARN)`;idPARN=`(your idP ARN)`;
```

## Example of connecting to the ODBC driver with a specified endpoint and a log level of 2 (WARNING)

```
Driver={AWS IoT SiteWise ODBC Driver};Auth=`IAM`;AccessKeyId=`(your access key ID)`;SecretKey=`(your secret key)`;EndpointOverride=`iotsitewise.us-east-1.amazonaws.com`;Region=`us-east-1`;LogLevel=`2`;
```

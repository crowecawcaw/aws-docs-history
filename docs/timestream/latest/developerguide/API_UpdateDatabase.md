For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# UpdateDatabase

Modifies the AWS KMS key for an existing database. While updating the database, you must specify the
database name and the identifier of the new AWS KMS key to be used (`KmsKeyId`). If there are
any concurrent `UpdateDatabase` requests, first writer wins.

See [code
sample](code-samples.md "code-samples.md") for details.

## Request Syntax

```
{
   "DatabaseName": "`string`",
   "KmsKeyId": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[DatabaseName](#API_UpdateDatabase_RequestSyntax "#API_UpdateDatabase_RequestSyntax")**

The name of the database.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 256.

Required: Yes

**[KmsKeyId](#API_UpdateDatabase_RequestSyntax "#API_UpdateDatabase_RequestSyntax")**

The identifier of the new AWS KMS key (`KmsKeyId`) to be used to encrypt the data stored
in the database. If the `KmsKeyId` currently registered with the database is the same as the
`KmsKeyId` in the request, there will not be any update.

You can specify the `KmsKeyId` using any of the following:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias ARN: `arn:aws:kms:us-east-1:111122223333:alias/ExampleAlias`

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: Yes

## Response Syntax

```
{
   "Database": {
      "Arn": "***string***",
      "CreationTime": ***number***,
      "DatabaseName": "***string***",
      "KmsKeyId": "***string***",
      "LastUpdatedTime": ***number***,
      "TableCount": ***number***
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Database](#API_UpdateDatabase_ResponseSyntax "#API_UpdateDatabase_ResponseSyntax")**

A top-level container for a table. Databases and tables are the fundamental management concepts in Amazon
Timestream. All tables in a database are encrypted with the same AWS KMS key.

Type: [Database](API_Database.md "API_Database.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You are not authorized to perform this action.

HTTP Status Code: 400

**InternalServerException**

Timestream was unable to fully process this request because of an internal server error.

HTTP Status Code: 500

**InvalidEndpointException**

The requested endpoint was not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its
status might not be ACTIVE.

HTTP Status Code: 400

**ServiceQuotaExceededException**

The instance quota of resource exceeded for this account.

HTTP Status Code: 400

**ThrottlingException**

Too many requests were made by a user and they exceeded the service quotas. The request was throttled.

HTTP Status Code: 400

**ValidationException**

An invalid or malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-write-2018-11-01/UpdateDatabase.md "../../../goto/cli2/timestream-write-2018-11-01/UpdateDatabase.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/timestream-write-2018-11-01/UpdateDatabase.md "../../../goto/DotNetSDKV3/timestream-write-2018-11-01/UpdateDatabase.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/UpdateDatabase.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/UpdateDatabase.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-write-2018-11-01/UpdateDatabase.md "../../../goto/SdkForGoV2/timestream-write-2018-11-01/UpdateDatabase.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/UpdateDatabase.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/UpdateDatabase.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-write-2018-11-01/UpdateDatabase.md "../../../goto/SdkForJavaScriptV3/timestream-write-2018-11-01/UpdateDatabase.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-write-2018-11-01/UpdateDatabase.md "../../../goto/SdkForKotlin/timestream-write-2018-11-01/UpdateDatabase.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-write-2018-11-01/UpdateDatabase.md "../../../goto/SdkForPHPV3/timestream-write-2018-11-01/UpdateDatabase.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-write-2018-11-01/UpdateDatabase.md "../../../goto/boto3/timestream-write-2018-11-01/UpdateDatabase.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/UpdateDatabase.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/UpdateDatabase.md")

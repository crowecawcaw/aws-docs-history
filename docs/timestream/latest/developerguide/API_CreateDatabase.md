For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# CreateDatabase

Creates a new Timestream database. If the AWS KMS key is not specified, the database will be
encrypted with a Timestream managed AWS KMS key located in your account. For more information,
see [AWS
managed keys](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk"). [Service
quotas apply](ts-limits.md "ts-limits.md"). For details, see [code sample](code-samples.md "code-samples.md").

## Request Syntax

```
{
   "DatabaseName": "`string`",
   "KmsKeyId": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[DatabaseName](#API_CreateDatabase_RequestSyntax "#API_CreateDatabase_RequestSyntax")**

The name of the Timestream database.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**[KmsKeyId](#API_CreateDatabase_RequestSyntax "#API_CreateDatabase_RequestSyntax")**

The AWS KMS key for the database. If the AWS KMS key is not specified, the database will
be encrypted with a Timestream managed AWS KMS key located in your account. For more information,
see [AWS
managed keys](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: No

**[Tags](#API_CreateDatabase_RequestSyntax "#API_CreateDatabase_RequestSyntax")**

A list of key-value pairs to label the table.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

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

**[Database](#API_CreateDatabase_ResponseSyntax "#API_CreateDatabase_ResponseSyntax")**

The newly created Timestream database.

Type: [Database](API_Database.md "API_Database.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You are not authorized to perform this action.

HTTP Status Code: 400

**ConflictException**

Timestream was unable to process this request because it contains resource that already exists.

HTTP Status Code: 400

**InternalServerException**

Timestream was unable to fully process this request because of an internal server error.

HTTP Status Code: 500

**InvalidEndpointException**

The requested endpoint was not valid.

HTTP Status Code: 400

**InvalidEndpointException**

The requested endpoint was not valid.

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

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-write-2018-11-01/CreateDatabase.md "../../../goto/cli2/timestream-write-2018-11-01/CreateDatabase.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/timestream-write-2018-11-01/CreateDatabase.md "../../../goto/DotNetSDKV3/timestream-write-2018-11-01/CreateDatabase.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/CreateDatabase.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/CreateDatabase.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-write-2018-11-01/CreateDatabase.md "../../../goto/SdkForGoV2/timestream-write-2018-11-01/CreateDatabase.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/CreateDatabase.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/CreateDatabase.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-write-2018-11-01/CreateDatabase.md "../../../goto/SdkForJavaScriptV3/timestream-write-2018-11-01/CreateDatabase.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-write-2018-11-01/CreateDatabase.md "../../../goto/SdkForKotlin/timestream-write-2018-11-01/CreateDatabase.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-write-2018-11-01/CreateDatabase.md "../../../goto/SdkForPHPV3/timestream-write-2018-11-01/CreateDatabase.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-write-2018-11-01/CreateDatabase.md "../../../goto/boto3/timestream-write-2018-11-01/CreateDatabase.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/CreateDatabase.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/CreateDatabase.md")

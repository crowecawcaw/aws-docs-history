For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# DeleteTable

Deletes a given Timestream table. This is an irreversible operation. After a Timestream
database table is deleted, the time-series data stored in the table cannot be recovered.

###### Note

Due to the nature of distributed retries, the operation can return either success or a
ResourceNotFoundException. Clients should consider them equivalent.

See [code
sample](code-samples.md "code-samples.md") for details.

## Request Syntax

```
{
   "DatabaseName": "`string`",
   "TableName": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[DatabaseName](#API_DeleteTable_RequestSyntax "#API_DeleteTable_RequestSyntax")**

The name of the database where the Timestream database is to be deleted.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 256.

Required: Yes

**[TableName](#API_DeleteTable_RequestSyntax "#API_DeleteTable_RequestSyntax")**

The name of the Timestream table to be deleted.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 256.

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

**ThrottlingException**

Too many requests were made by a user and they exceeded the service quotas. The request was throttled.

HTTP Status Code: 400

**ValidationException**

An invalid or malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-write-2018-11-01/DeleteTable.md "../../../goto/cli2/timestream-write-2018-11-01/DeleteTable.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/timestream-write-2018-11-01/DeleteTable.md "../../../goto/DotNetSDKV4/timestream-write-2018-11-01/DeleteTable.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/DeleteTable.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/DeleteTable.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-write-2018-11-01/DeleteTable.md "../../../goto/SdkForGoV2/timestream-write-2018-11-01/DeleteTable.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/DeleteTable.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/DeleteTable.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-write-2018-11-01/DeleteTable.md "../../../goto/SdkForJavaScriptV3/timestream-write-2018-11-01/DeleteTable.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-write-2018-11-01/DeleteTable.md "../../../goto/SdkForKotlin/timestream-write-2018-11-01/DeleteTable.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-write-2018-11-01/DeleteTable.md "../../../goto/SdkForPHPV3/timestream-write-2018-11-01/DeleteTable.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-write-2018-11-01/DeleteTable.md "../../../goto/boto3/timestream-write-2018-11-01/DeleteTable.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/DeleteTable.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/DeleteTable.md")

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# CreateTable

Adds a new table to an existing database in your account. In an AWS account, table names must be
at least unique within each Region if they are in the same database. You might have identical table names in the same
Region if the tables are in separate databases. While creating the table, you must specify the table name, database
name, and the retention properties. [Service quotas apply](ts-limits.md "ts-limits.md"). See [code sample](code-samples.md "code-samples.md") for details.

## Request Syntax

```
{
   "DatabaseName": "`string`",
   "MagneticStoreWriteProperties": {
      "EnableMagneticStoreWrites": `boolean`,
      "MagneticStoreRejectedDataLocation": {
         "S3Configuration": {
            "BucketName": "`string`",
            "EncryptionOption": "`string`",
            "KmsKeyId": "`string`",
            "ObjectKeyPrefix": "`string`"
         }
      }
   },
   "RetentionProperties": {
      "MagneticStoreRetentionPeriodInDays": `number`,
      "MemoryStoreRetentionPeriodInHours": `number`
   },
   "Schema": {
      "CompositePartitionKey": [
         {
            "EnforcementInRecord": "`string`",
            "Name": "`string`",
            "Type": "`string`"
         }
      ]
   },
   "TableName": "`string`",
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

**[DatabaseName](#API_CreateTable_RequestSyntax "#API_CreateTable_RequestSyntax")**

The name of the Timestream database.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**[MagneticStoreWriteProperties](#API_CreateTable_RequestSyntax "#API_CreateTable_RequestSyntax")**

Contains properties to set on the table when enabling magnetic store writes.

Type: [MagneticStoreWriteProperties](API_MagneticStoreWriteProperties.md "API_MagneticStoreWriteProperties.md") object

Required: No

**[RetentionProperties](#API_CreateTable_RequestSyntax "#API_CreateTable_RequestSyntax")**

The duration for which your time-series data must be stored in the memory store and the magnetic store.

Type: [RetentionProperties](API_RetentionProperties.md "API_RetentionProperties.md") object

Required: No

**[Schema](#API_CreateTable_RequestSyntax "#API_CreateTable_RequestSyntax")**

The schema of the table.

Type: [Schema](API_Schema.md "API_Schema.md") object

Required: No

**[TableName](#API_CreateTable_RequestSyntax "#API_CreateTable_RequestSyntax")**

The name of the Timestream table.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**[Tags](#API_CreateTable_RequestSyntax "#API_CreateTable_RequestSyntax")**

A list of key-value pairs to label the table.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "Table": {
      "Arn": "***string***",
      "CreationTime": ***number***,
      "DatabaseName": "***string***",
      "LastUpdatedTime": ***number***,
      "MagneticStoreWriteProperties": {
         "EnableMagneticStoreWrites": ***boolean***,
         "MagneticStoreRejectedDataLocation": {
            "S3Configuration": {
               "BucketName": "***string***",
               "EncryptionOption": "***string***",
               "KmsKeyId": "***string***",
               "ObjectKeyPrefix": "***string***"
            }
         }
      },
      "RetentionProperties": {
         "MagneticStoreRetentionPeriodInDays": ***number***,
         "MemoryStoreRetentionPeriodInHours": ***number***
      },
      "Schema": {
         "CompositePartitionKey": [
            {
               "EnforcementInRecord": "***string***",
               "Name": "***string***",
               "Type": "***string***"
            }
         ]
      },
      "TableName": "***string***",
      "TableStatus": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Table](#API_CreateTable_ResponseSyntax "#API_CreateTable_ResponseSyntax")**

The newly created Timestream table.

Type: [Table](API_Table.md "API_Table.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-write-2018-11-01/CreateTable.md "../../../goto/cli2/timestream-write-2018-11-01/CreateTable.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/timestream-write-2018-11-01/CreateTable.md "../../../goto/DotNetSDKV4/timestream-write-2018-11-01/CreateTable.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/CreateTable.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/CreateTable.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-write-2018-11-01/CreateTable.md "../../../goto/SdkForGoV2/timestream-write-2018-11-01/CreateTable.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/CreateTable.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/CreateTable.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-write-2018-11-01/CreateTable.md "../../../goto/SdkForJavaScriptV3/timestream-write-2018-11-01/CreateTable.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-write-2018-11-01/CreateTable.md "../../../goto/SdkForKotlin/timestream-write-2018-11-01/CreateTable.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-write-2018-11-01/CreateTable.md "../../../goto/SdkForPHPV3/timestream-write-2018-11-01/CreateTable.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-write-2018-11-01/CreateTable.md "../../../goto/boto3/timestream-write-2018-11-01/CreateTable.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/CreateTable.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/CreateTable.md")

AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# DescribeMigrationTask

Retrieves a list of all attributes associated with a specific migration task.

## Request Syntax

```
{
   "MigrationTaskName": "`string`",
   "ProgressUpdateStream": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[MigrationTaskName](#API_DescribeMigrationTask_RequestSyntax "#API_DescribeMigrationTask_RequestSyntax")**

The identifier given to the MigrationTask. _Do not store personal data in this
field._

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[^:|]+`

Required: Yes

**[ProgressUpdateStream](#API_DescribeMigrationTask_RequestSyntax "#API_DescribeMigrationTask_RequestSyntax")**

The name of the ProgressUpdateStream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[^/:|\000-\037]+`

Required: Yes

## Response Syntax

```
{
   "MigrationTask": {
      "MigrationTaskName": "***string***",
      "ProgressUpdateStream": "***string***",
      "ResourceAttributeList": [
         {
            "Type": "***string***",
            "Value": "***string***"
         }
      ],
      "Task": {
         "ProgressPercent": ***number***,
         "Status": "***string***",
         "StatusDetail": "***string***"
      },
      "UpdateDateTime": ***number***
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[MigrationTask](#API_DescribeMigrationTask_ResponseSyntax "#API_DescribeMigrationTask_ResponseSyntax")**

Object encapsulating information about the migration task.

Type: [MigrationTask](API_MigrationTask.md "API_MigrationTask.md") object

## Errors

**AccessDeniedException**

You do not have sufficient access to perform this action.

HTTP Status Code: 400

**HomeRegionNotSetException**

The home region is not set. Set the home region to continue.

HTTP Status Code: 400

**InternalServerError**

Exception raised when an internal, configuration, or dependency error is
encountered.

HTTP Status Code: 500

**InvalidInputException**

Exception raised when the provided input violates a policy constraint or is entered in
the wrong format or data type.

HTTP Status Code: 400

**ResourceNotFoundException**

Exception raised when the request references a resource (Application Discovery Service
configuration, update stream, migration task, etc.) that does not exist in Application
Discovery Service (Application Discovery Service) or in Migration Hub's repository.

HTTP Status Code: 400

**ServiceUnavailableException**

Exception raised when there is an internal, configuration, or dependency error
encountered.

HTTP Status Code: 500

**ThrottlingException**

The request was denied due to request throttling.

**Message**

A message that provides information about the exception.

**RetryAfterSeconds**

The number of seconds the caller should wait before retrying.

HTTP Status Code: 400

## Examples

### Describe a migration task by listing all associated attributes

The following example lists all of the attributes associated with the values
passed to the required parameters of `MigrationTaskName` and
`ProgressUpdateStream`.

#### Sample Request

```

{
    "ProgressUpdateStream": "SMS",
    "MigrationTaskName": "sms-12de3cf1a"
}
```

#### Sample Response

```

{
    "MigrationTask": {
        "ProgressUpdateStream": "SMS",
        "Task": {
            "Status": "IN_PROGRESS",
            "StatusDetail": "Migration: Copying image data",
            "ProgressPercent": 77
        },
        "UpdateDateTime": 1493750385.0,
        "MigrationTaskName": "sms-12de3cf1a"
    }
}

```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md "../../../goto/cli2/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md "../../../goto/DotNetSDKV3/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md "../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md "../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md "../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md "../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md")
- [AWS SDK for Python](../../../goto/boto3/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md "../../../goto/boto3/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/DescribeMigrationTask.md")

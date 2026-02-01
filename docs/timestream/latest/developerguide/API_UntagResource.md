For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# UntagResource

Removes the association of tags from a Timestream resource.

## Request Syntax

```
{
   "ResourceARN": "`string`",
   "TagKeys": [ "`string`" ]
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[ResourceARN](#API_UntagResource_RequestSyntax "#API_UntagResource_RequestSyntax")**

The Timestream resource that the tags will be removed from. This value is an Amazon Resource Name
(ARN).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Required: Yes

**[TagKeys](#API_UntagResource_RequestSyntax "#API_UntagResource_RequestSyntax")**

A list of tags keys. Existing tags of the resource whose keys are members of this list will be removed from the
Timestream resource.

Type: Array of strings

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Length Constraints: Minimum length of 1. Maximum length of 128.

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

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

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-write-2018-11-01/UntagResource.md "../../../goto/cli2/timestream-write-2018-11-01/UntagResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/timestream-write-2018-11-01/UntagResource.md "../../../goto/DotNetSDKV4/timestream-write-2018-11-01/UntagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/UntagResource.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/UntagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-write-2018-11-01/UntagResource.md "../../../goto/SdkForGoV2/timestream-write-2018-11-01/UntagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/UntagResource.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/UntagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-write-2018-11-01/UntagResource.md "../../../goto/SdkForJavaScriptV3/timestream-write-2018-11-01/UntagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-write-2018-11-01/UntagResource.md "../../../goto/SdkForKotlin/timestream-write-2018-11-01/UntagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-write-2018-11-01/UntagResource.md "../../../goto/SdkForPHPV3/timestream-write-2018-11-01/UntagResource.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-write-2018-11-01/UntagResource.md "../../../goto/boto3/timestream-write-2018-11-01/UntagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/UntagResource.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/UntagResource.md")

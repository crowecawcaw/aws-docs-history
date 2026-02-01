After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# ListTagsForResource

Retrieves the list of key-value tags assigned to the application. For more
information, see [Using Tagging](how-tagging.md "how-tagging.md").

## Request Syntax

```
{
   "ResourceARN": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ResourceARN](#API_ListTagsForResource_RequestSyntax "#API_ListTagsForResource_RequestSyntax")**

The ARN of the application for which to retrieve tags.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:.*`

Required: Yes

## Response Syntax

```
{
   "Tags": [
      {
         "Key": "***string***",
         "Value": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Tags](#API_ListTagsForResource_ResponseSyntax "#API_ListTagsForResource_ResponseSyntax")**

The key-value tags assigned to the application.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 1 item. Maximum number of 200 items.

## Errors

**ConcurrentModificationException**

Exception thrown as a result of concurrent modification to an application. For
example, two individuals attempting to edit the same application at the same
time.

**message**

HTTP Status Code: 400

**InvalidArgumentException**

Specified input parameter value is invalid.

**message**

HTTP Status Code: 400

**ResourceNotFoundException**

Specified application can't be found.

**message**

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisanalytics-2015-08-14/ListTagsForResource.md "../../../goto/cli2/kinesisanalytics-2015-08-14/ListTagsForResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisanalytics-2015-08-14/ListTagsForResource.md "../../../goto/DotNetSDKV4/kinesisanalytics-2015-08-14/ListTagsForResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/ListTagsForResource.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/ListTagsForResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/ListTagsForResource.md "../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/ListTagsForResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/ListTagsForResource.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/ListTagsForResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/ListTagsForResource.md "../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/ListTagsForResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/ListTagsForResource.md "../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/ListTagsForResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/ListTagsForResource.md "../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/ListTagsForResource.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisanalytics-2015-08-14/ListTagsForResource.md "../../../goto/boto3/kinesisanalytics-2015-08-14/ListTagsForResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/ListTagsForResource.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/ListTagsForResource.md")

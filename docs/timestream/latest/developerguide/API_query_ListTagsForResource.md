For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# ListTagsForResource

List all tags on a Timestream query resource.

## Request Syntax

```
{
   "MaxResults": `number`,
   "NextToken": "`string`",
   "ResourceARN": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[MaxResults](#API_query_ListTagsForResource_RequestSyntax "#API_query_ListTagsForResource_RequestSyntax")**

The maximum number of tags to return.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 200.

Required: No

**[NextToken](#API_query_ListTagsForResource_RequestSyntax "#API_query_ListTagsForResource_RequestSyntax")**

A pagination token to resume pagination.

Type: String

Required: No

**[ResourceARN](#API_query_ListTagsForResource_RequestSyntax "#API_query_ListTagsForResource_RequestSyntax")**

The Timestream resource with tags to be listed. This value is an Amazon Resource Name
(ARN).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: Yes

## Response Syntax

```
{
   "NextToken": "***string***",
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

**[NextToken](#API_query_ListTagsForResource_ResponseSyntax "#API_query_ListTagsForResource_ResponseSyntax")**

A pagination token to resume pagination with a subsequent call to
`ListTagsForResourceResponse`.

Type: String

**[Tags](#API_query_ListTagsForResource_ResponseSyntax "#API_query_ListTagsForResource_ResponseSyntax")**

The tags currently associated with the Timestream resource.

Type: Array of [Tag](API_query_Tag.md "API_query_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidEndpointException**

The requested endpoint is invalid.

HTTP Status Code: 400

**ResourceNotFoundException**

The requested resource could not be found.

**ScheduledQueryArn**

The ARN of the scheduled query.

HTTP Status Code: 400

**ThrottlingException**

The request was throttled due to excessive requests.

HTTP Status Code: 400

**ValidationException**

Invalid or malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-query-2018-11-01/ListTagsForResource.md "../../../goto/cli2/timestream-query-2018-11-01/ListTagsForResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/timestream-query-2018-11-01/ListTagsForResource.md "../../../goto/DotNetSDKV3/timestream-query-2018-11-01/ListTagsForResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/ListTagsForResource.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/ListTagsForResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-query-2018-11-01/ListTagsForResource.md "../../../goto/SdkForGoV2/timestream-query-2018-11-01/ListTagsForResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ListTagsForResource.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ListTagsForResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/ListTagsForResource.md "../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/ListTagsForResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-query-2018-11-01/ListTagsForResource.md "../../../goto/SdkForKotlin/timestream-query-2018-11-01/ListTagsForResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-query-2018-11-01/ListTagsForResource.md "../../../goto/SdkForPHPV3/timestream-query-2018-11-01/ListTagsForResource.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-query-2018-11-01/ListTagsForResource.md "../../../goto/boto3/timestream-query-2018-11-01/ListTagsForResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ListTagsForResource.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ListTagsForResource.md")

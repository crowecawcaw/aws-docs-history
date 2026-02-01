# ListAdapters

Lists all adapters that match the specified filtration criteria.

## Request Syntax

```
{
   "AfterCreationTime": `number`,
   "BeforeCreationTime": `number`,
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AfterCreationTime](#API_ListAdapters_RequestSyntax "#API_ListAdapters_RequestSyntax")**

Specifies the lower bound for the ListAdapters operation.
Ensures ListAdapters returns only adapters created after the specified creation time.

Type: Timestamp

Required: No

**[BeforeCreationTime](#API_ListAdapters_RequestSyntax "#API_ListAdapters_RequestSyntax")**

Specifies the upper bound for the ListAdapters operation.
Ensures ListAdapters returns only adapters created before the specified creation time.

Type: Timestamp

Required: No

**[MaxResults](#API_ListAdapters_RequestSyntax "#API_ListAdapters_RequestSyntax")**

The maximum number of results to return when listing adapters.

Type: Integer

Valid Range: Minimum value of 1.

Required: No

**[NextToken](#API_ListAdapters_RequestSyntax "#API_ListAdapters_RequestSyntax")**

Identifies the next page of results to return when listing adapters.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `.*\S.*`

Required: No

## Response Syntax

```
{
   "Adapters": [
      {
         "AdapterId": "***string***",
         "AdapterName": "***string***",
         "CreationTime": ***number***,
         "FeatureTypes": [ "***string***" ]
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Adapters](#API_ListAdapters_ResponseSyntax "#API_ListAdapters_ResponseSyntax")**

A list of adapters that matches the filtering criteria specified when calling ListAdapters.

Type: Array of [AdapterOverview](API_AdapterOverview.md "API_AdapterOverview.md") objects

**[NextToken](#API_ListAdapters_ResponseSyntax "#API_ListAdapters_ResponseSyntax")**

Identifies the next page of results to return when listing adapters.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `.*\S.*`

## Errors

**AccessDeniedException**

You aren't authorized to perform the action. Use the Amazon Resource Name (ARN)
of an authorized user or IAM role to perform the operation.

HTTP Status Code: 400

**InternalServerError**

Amazon Textract experienced a service issue. Try your call again.

HTTP Status Code: 500

**InvalidParameterException**

An input parameter violated a constraint. For example, in synchronous operations,
an `InvalidParameterException` exception occurs
when neither of the `S3Object` or `Bytes` values are supplied in the `Document`
request parameter.
Validate your parameter before calling the API operation again.

HTTP Status Code: 400

**ProvisionedThroughputExceededException**

The number of requests exceeded your throughput limit. If you want to increase this limit,
contact Amazon Textract.

HTTP Status Code: 400

**ThrottlingException**

Amazon Textract is temporarily unable to process the request. Try your call again.

HTTP Status Code: 500

**ValidationException**

Indicates that a request was not valid. Check request for proper formatting.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/textract-2018-06-27/ListAdapters.md "../../../goto/cli2/textract-2018-06-27/ListAdapters.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/textract-2018-06-27/ListAdapters.md "../../../goto/DotNetSDKV4/textract-2018-06-27/ListAdapters.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/ListAdapters.md "../../../goto/SdkForCpp/textract-2018-06-27/ListAdapters.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/textract-2018-06-27/ListAdapters.md "../../../goto/SdkForGoV2/textract-2018-06-27/ListAdapters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/ListAdapters.md "../../../goto/SdkForJavaV2/textract-2018-06-27/ListAdapters.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/textract-2018-06-27/ListAdapters.md "../../../goto/SdkForJavaScriptV3/textract-2018-06-27/ListAdapters.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/textract-2018-06-27/ListAdapters.md "../../../goto/SdkForKotlin/textract-2018-06-27/ListAdapters.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/textract-2018-06-27/ListAdapters.md "../../../goto/SdkForPHPV3/textract-2018-06-27/ListAdapters.md")
- [AWS SDK for Python](../../../goto/boto3/textract-2018-06-27/ListAdapters.md "../../../goto/boto3/textract-2018-06-27/ListAdapters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/ListAdapters.md "../../../goto/SdkForRubyV3/textract-2018-06-27/ListAdapters.md")

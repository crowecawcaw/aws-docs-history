# ListAdapterVersions

List all version of an adapter that meet the specified filtration criteria.

## Request Syntax

```
{
   "AdapterId": "`string`",
   "AfterCreationTime": `number`,
   "BeforeCreationTime": `number`,
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AdapterId](#API_ListAdapterVersions_RequestSyntax "#API_ListAdapterVersions_RequestSyntax")**

A string containing a unique ID for the adapter to match for when listing adapter versions.

Type: String

Length Constraints: Minimum length of 12. Maximum length of 1011.

Required: No

**[AfterCreationTime](#API_ListAdapterVersions_RequestSyntax "#API_ListAdapterVersions_RequestSyntax")**

Specifies the lower bound for the ListAdapterVersions operation.
Ensures ListAdapterVersions returns only adapter versions created after the specified creation time.

Type: Timestamp

Required: No

**[BeforeCreationTime](#API_ListAdapterVersions_RequestSyntax "#API_ListAdapterVersions_RequestSyntax")**

Specifies the upper bound for the ListAdapterVersions operation.
Ensures ListAdapterVersions returns only adapter versions created after the specified creation time.

Type: Timestamp

Required: No

**[MaxResults](#API_ListAdapterVersions_RequestSyntax "#API_ListAdapterVersions_RequestSyntax")**

The maximum number of results to return when listing adapter versions.

Type: Integer

Valid Range: Minimum value of 1.

Required: No

**[NextToken](#API_ListAdapterVersions_RequestSyntax "#API_ListAdapterVersions_RequestSyntax")**

Identifies the next page of results to return when listing adapter versions.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `.*\S.*`

Required: No

## Response Syntax

```
{
   "AdapterVersions": [
      {
         "AdapterId": "***string***",
         "AdapterVersion": "***string***",
         "CreationTime": ***number***,
         "FeatureTypes": [ "***string***" ],
         "Status": "***string***",
         "StatusMessage": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AdapterVersions](#API_ListAdapterVersions_ResponseSyntax "#API_ListAdapterVersions_ResponseSyntax")**

Adapter versions that match the filtering criteria specified when calling ListAdapters.

Type: Array of [AdapterVersionOverview](API_AdapterVersionOverview.md "API_AdapterVersionOverview.md") objects

**[NextToken](#API_ListAdapterVersions_ResponseSyntax "#API_ListAdapterVersions_ResponseSyntax")**

Identifies the next page of results to return when listing adapter versions.

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

**ResourceNotFoundException**

Returned when an operation tried to access a nonexistent resource.

HTTP Status Code: 400

**ThrottlingException**

Amazon Textract is temporarily unable to process the request. Try your call again.

HTTP Status Code: 500

**ValidationException**

Indicates that a request was not valid. Check request for proper formatting.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/textract-2018-06-27/ListAdapterVersions.md "../../../goto/cli2/textract-2018-06-27/ListAdapterVersions.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/textract-2018-06-27/ListAdapterVersions.md "../../../goto/DotNetSDKV3/textract-2018-06-27/ListAdapterVersions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/ListAdapterVersions.md "../../../goto/SdkForCpp/textract-2018-06-27/ListAdapterVersions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/textract-2018-06-27/ListAdapterVersions.md "../../../goto/SdkForGoV2/textract-2018-06-27/ListAdapterVersions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/ListAdapterVersions.md "../../../goto/SdkForJavaV2/textract-2018-06-27/ListAdapterVersions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/textract-2018-06-27/ListAdapterVersions.md "../../../goto/SdkForJavaScriptV3/textract-2018-06-27/ListAdapterVersions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/textract-2018-06-27/ListAdapterVersions.md "../../../goto/SdkForKotlin/textract-2018-06-27/ListAdapterVersions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/textract-2018-06-27/ListAdapterVersions.md "../../../goto/SdkForPHPV3/textract-2018-06-27/ListAdapterVersions.md")
- [AWS SDK for Python](../../../goto/boto3/textract-2018-06-27/ListAdapterVersions.md "../../../goto/boto3/textract-2018-06-27/ListAdapterVersions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/ListAdapterVersions.md "../../../goto/SdkForRubyV3/textract-2018-06-27/ListAdapterVersions.md")

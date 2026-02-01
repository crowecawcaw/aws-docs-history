On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# ListLabels

Provides a list of labels.

## Request Syntax

```
{
   "Equipment": "`string`",
   "FaultCode": "`string`",
   "IntervalEndTime": `number`,
   "IntervalStartTime": `number`,
   "LabelGroupName": "`string`",
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[Equipment](#API_ListLabels_RequestSyntax "#API_ListLabels_RequestSyntax")**

Lists the labels that pertain to a particular piece of equipment.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `[\P{M}\p{M}]{1,200}`

Required: No

**[FaultCode](#API_ListLabels_RequestSyntax "#API_ListLabels_RequestSyntax")**

Returns labels with a particular fault code.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[\P{M}\p{M}]{1,100}`

Required: No

**[IntervalEndTime](#API_ListLabels_RequestSyntax "#API_ListLabels_RequestSyntax")**

Returns all labels with a start time earlier than the end time given.

Type: Timestamp

Required: No

**[IntervalStartTime](#API_ListLabels_RequestSyntax "#API_ListLabels_RequestSyntax")**

Returns all the labels with a end time equal to or later than the start time given.

Type: Timestamp

Required: No

**[LabelGroupName](#API_ListLabels_RequestSyntax "#API_ListLabels_RequestSyntax")**

Returns the name of the label group.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

**[MaxResults](#API_ListLabels_RequestSyntax "#API_ListLabels_RequestSyntax")**

Specifies the maximum number of labels to list.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 500.

Required: No

**[NextToken](#API_ListLabels_RequestSyntax "#API_ListLabels_RequestSyntax")**

An opaque pagination token indicating where to continue the listing of label groups.

Type: String

Length Constraints: Maximum length of 8192.

Pattern: `\p{ASCII}{0,8192}`

Required: No

## Response Syntax

```
{
   "LabelSummaries": [
      {
         "CreatedAt": ***number***,
         "EndTime": ***number***,
         "Equipment": "***string***",
         "FaultCode": "***string***",
         "LabelGroupArn": "***string***",
         "LabelGroupName": "***string***",
         "LabelId": "***string***",
         "Rating": "***string***",
         "StartTime": ***number***
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[LabelSummaries](#API_ListLabels_ResponseSyntax "#API_ListLabels_ResponseSyntax")**

A summary of the items in the label group.

###### Note

If you don't supply the `LabelGroupName` request parameter, or if you supply
the name of a label group that doesn't exist, `ListLabels` returns an empty array in
`LabelSummaries`.

Type: Array of [LabelSummary](API_LabelSummary.md "API_LabelSummary.md") objects

**[NextToken](#API_ListLabels_ResponseSyntax "#API_ListLabels_ResponseSyntax")**

An opaque pagination token indicating where to continue the listing of datasets.

Type: String

Length Constraints: Maximum length of 8192.

Pattern: `\p{ASCII}{0,8192}`

## Errors

**AccessDeniedException**

The request could not be completed because you do not have access to the resource.

HTTP Status Code: 400

**InternalServerException**

Processing of the request has failed because of an unknown error, exception or failure.

HTTP Status Code: 500

**ThrottlingException**

The request was denied due to request throttling.

HTTP Status Code: 400

**ValidationException**

The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related AWS
service that's being utilized.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/ListLabels.md "../../../goto/cli2/lookoutequipment-2020-12-15/ListLabels.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/ListLabels.md "../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/ListLabels.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ListLabels.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ListLabels.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/ListLabels.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/ListLabels.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListLabels.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListLabels.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListLabels.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListLabels.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/ListLabels.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/ListLabels.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListLabels.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListLabels.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/ListLabels.md "../../../goto/boto3/lookoutequipment-2020-12-15/ListLabels.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListLabels.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListLabels.md")

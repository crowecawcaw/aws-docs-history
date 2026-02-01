On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# DescribeLabel

Returns the name of the label.

## Request Syntax

```
{
   "LabelGroupName": "`string`",
   "LabelId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[LabelGroupName](#API_DescribeLabel_RequestSyntax "#API_DescribeLabel_RequestSyntax")**

Returns the name of the group containing the label.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

**[LabelId](#API_DescribeLabel_RequestSyntax "#API_DescribeLabel_RequestSyntax")**

Returns the ID of the label.

Type: String

Length Constraints: Maximum length of 32.

Pattern: `[A-Fa-f0-9]{0,32}`

Required: Yes

## Response Syntax

```
{
   "CreatedAt": ***number***,
   "EndTime": ***number***,
   "Equipment": "***string***",
   "FaultCode": "***string***",
   "LabelGroupArn": "***string***",
   "LabelGroupName": "***string***",
   "LabelId": "***string***",
   "Notes": "***string***",
   "Rating": "***string***",
   "StartTime": ***number***
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreatedAt](#API_DescribeLabel_ResponseSyntax "#API_DescribeLabel_ResponseSyntax")**

The time at which the label was created.

Type: Timestamp

**[EndTime](#API_DescribeLabel_ResponseSyntax "#API_DescribeLabel_ResponseSyntax")**

The end time of the requested label.

Type: Timestamp

**[Equipment](#API_DescribeLabel_ResponseSyntax "#API_DescribeLabel_ResponseSyntax")**

Indicates that a label pertains to a particular piece of equipment.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `[\P{M}\p{M}]{1,200}`

**[FaultCode](#API_DescribeLabel_ResponseSyntax "#API_DescribeLabel_ResponseSyntax")**

Indicates the type of anomaly associated with the label.

Data in this field will be retained for service usage. Follow best practices for the
security of your data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[\P{M}\p{M}]{1,100}`

**[LabelGroupArn](#API_DescribeLabel_ResponseSyntax "#API_DescribeLabel_ResponseSyntax")**

The Amazon Resource Name (ARN) of the requested label group.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:label-group\/.+`

**[LabelGroupName](#API_DescribeLabel_ResponseSyntax "#API_DescribeLabel_ResponseSyntax")**

The name of the requested label group.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

**[LabelId](#API_DescribeLabel_ResponseSyntax "#API_DescribeLabel_ResponseSyntax")**

The ID of the requested label.

Type: String

Length Constraints: Maximum length of 32.

Pattern: `[A-Fa-f0-9]{0,32}`

**[Notes](#API_DescribeLabel_ResponseSyntax "#API_DescribeLabel_ResponseSyntax")**

Metadata providing additional information about the label.

Data in this field will be retained for service usage. Follow best practices for the
security of your data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2560.

Pattern: `[\P{M}\p{M}]{1,2560}`

**[Rating](#API_DescribeLabel_ResponseSyntax "#API_DescribeLabel_ResponseSyntax")**

Indicates whether a labeled event represents an anomaly.

Type: String

Valid Values: `ANOMALY | NO_ANOMALY | NEUTRAL`

**[StartTime](#API_DescribeLabel_ResponseSyntax "#API_DescribeLabel_ResponseSyntax")**

The start time of the requested label.

Type: Timestamp

## Errors

**AccessDeniedException**

The request could not be completed because you do not have access to the resource.

HTTP Status Code: 400

**InternalServerException**

Processing of the request has failed because of an unknown error, exception or failure.

HTTP Status Code: 500

**ResourceNotFoundException**

The resource requested could not be found. Verify the resource ID and retry your
request.

HTTP Status Code: 400

**ThrottlingException**

The request was denied due to request throttling.

HTTP Status Code: 400

**ValidationException**

The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related AWS
service that's being utilized.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/DescribeLabel.md "../../../goto/cli2/lookoutequipment-2020-12-15/DescribeLabel.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/DescribeLabel.md "../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/DescribeLabel.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/DescribeLabel.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/DescribeLabel.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/DescribeLabel.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/DescribeLabel.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/DescribeLabel.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/DescribeLabel.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DescribeLabel.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DescribeLabel.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/DescribeLabel.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/DescribeLabel.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/DescribeLabel.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/DescribeLabel.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/DescribeLabel.md "../../../goto/boto3/lookoutequipment-2020-12-15/DescribeLabel.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/DescribeLabel.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/DescribeLabel.md")

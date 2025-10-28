On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# CreateLabel

Creates a label for an event.

## Request Syntax

```
{
   "ClientToken": "`string`",
   "EndTime": `number`,
   "Equipment": "`string`",
   "FaultCode": "`string`",
   "LabelGroupName": "`string`",
   "Notes": "`string`",
   "Rating": "`string`",
   "StartTime": `number`
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ClientToken](#API_CreateLabel_RequestSyntax "#API_CreateLabel_RequestSyntax")**

A unique identifier for the request to create a label. If you do not set the client
request token, Lookout for Equipment generates one.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `\p{ASCII}{1,256}`

Required: Yes

**[EndTime](#API_CreateLabel_RequestSyntax "#API_CreateLabel_RequestSyntax")**

The end time of the labeled event.

Type: Timestamp

Required: Yes

**[Equipment](#API_CreateLabel_RequestSyntax "#API_CreateLabel_RequestSyntax")**

Indicates that a label pertains to a particular piece of equipment.

Data in this field will be retained for service usage. Follow best practices for the
security of your data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `[\P{M}\p{M}]{1,200}`

Required: No

**[FaultCode](#API_CreateLabel_RequestSyntax "#API_CreateLabel_RequestSyntax")**

Provides additional information about the label. The fault code must be defined in the
FaultCodes attribute of the label group.

Data in this field will be retained for service usage. Follow best practices for the
security of your data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[\P{M}\p{M}]{1,100}`

Required: No

**[LabelGroupName](#API_CreateLabel_RequestSyntax "#API_CreateLabel_RequestSyntax")**

The name of a group of labels.

Data in this field will be retained for service usage. Follow best practices for the
security of your data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

**[Notes](#API_CreateLabel_RequestSyntax "#API_CreateLabel_RequestSyntax")**

Metadata providing additional information about the label.

Data in this field will be retained for service usage. Follow best practices for the
security of your data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2560.

Pattern: `[\P{M}\p{M}]{1,2560}`

Required: No

**[Rating](#API_CreateLabel_RequestSyntax "#API_CreateLabel_RequestSyntax")**

Indicates whether a labeled event represents an anomaly.

Type: String

Valid Values: `ANOMALY | NO_ANOMALY | NEUTRAL`

Required: Yes

**[StartTime](#API_CreateLabel_RequestSyntax "#API_CreateLabel_RequestSyntax")**

The start time of the labeled event.

Type: Timestamp

Required: Yes

## Response Syntax

```
{
   "LabelId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[LabelId](#API_CreateLabel_ResponseSyntax "#API_CreateLabel_ResponseSyntax")**

The ID of the label that you have created.

Type: String

Length Constraints: Maximum length of 32.

Pattern: `[A-Fa-f0-9]{0,32}`

## Errors

**AccessDeniedException**

The request could not be completed because you do not have access to the resource.

HTTP Status Code: 400

**ConflictException**

The request could not be completed due to a conflict with the current state of the
target resource.

HTTP Status Code: 400

**InternalServerException**

Processing of the request has failed because of an unknown error, exception or failure.

HTTP Status Code: 500

**ResourceNotFoundException**

The resource requested could not be found. Verify the resource ID and retry your
request.

HTTP Status Code: 400

**ServiceQuotaExceededException**

Resource limitations have been exceeded.

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

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/CreateLabel.md "../../../goto/cli2/lookoutequipment-2020-12-15/CreateLabel.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/CreateLabel.md "../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/CreateLabel.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/CreateLabel.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/CreateLabel.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/CreateLabel.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/CreateLabel.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/CreateLabel.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/CreateLabel.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/CreateLabel.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/CreateLabel.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/CreateLabel.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/CreateLabel.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/CreateLabel.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/CreateLabel.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/CreateLabel.md "../../../goto/boto3/lookoutequipment-2020-12-15/CreateLabel.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/CreateLabel.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/CreateLabel.md")

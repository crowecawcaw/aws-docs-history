On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# CreateLabelGroup

Creates a group of labels.

## Request Syntax

```
{
   "ClientToken": "`string`",
   "FaultCodes": [ "`string`" ],
   "LabelGroupName": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ClientToken](#API_CreateLabelGroup_RequestSyntax "#API_CreateLabelGroup_RequestSyntax")**

A unique identifier for the request to create a label group. If you do not set the
client request token, Lookout for Equipment generates one.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `\p{ASCII}{1,256}`

Required: Yes

**[FaultCodes](#API_CreateLabelGroup_RequestSyntax "#API_CreateLabelGroup_RequestSyntax")**

The acceptable fault codes (indicating the type of anomaly associated with the label)
that can be used with this label group.

Data in this field will be retained for service usage. Follow best practices for the
security of your data.

Type: Array of strings

Array Members: Minimum number of 0 items. Maximum number of 50 items.

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[\P{M}\p{M}]{1,100}`

Required: No

**[LabelGroupName](#API_CreateLabelGroup_RequestSyntax "#API_CreateLabelGroup_RequestSyntax")**

Names a group of labels.

Data in this field will be retained for service usage. Follow best practices for the
security of your data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

**[Tags](#API_CreateLabelGroup_RequestSyntax "#API_CreateLabelGroup_RequestSyntax")**

Tags that provide metadata about the label group you are creating.

Data in this field will be retained for service usage. Follow best practices for the
security of your data.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "LabelGroupArn": "***string***",
   "LabelGroupName": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[LabelGroupArn](#API_CreateLabelGroup_ResponseSyntax "#API_CreateLabelGroup_ResponseSyntax")**

The Amazon Resource Name (ARN) of the label group that you have created.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:label-group\/.+`

**[LabelGroupName](#API_CreateLabelGroup_ResponseSyntax "#API_CreateLabelGroup_ResponseSyntax")**

The name of the label group that you have created. Data in this field will be retained
for service usage. Follow best practices for the security of your data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

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

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/CreateLabelGroup.md "../../../goto/cli2/lookoutequipment-2020-12-15/CreateLabelGroup.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/CreateLabelGroup.md "../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/CreateLabelGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/CreateLabelGroup.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/CreateLabelGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/CreateLabelGroup.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/CreateLabelGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/CreateLabelGroup.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/CreateLabelGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/CreateLabelGroup.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/CreateLabelGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/CreateLabelGroup.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/CreateLabelGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/CreateLabelGroup.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/CreateLabelGroup.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/CreateLabelGroup.md "../../../goto/boto3/lookoutequipment-2020-12-15/CreateLabelGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/CreateLabelGroup.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/CreateLabelGroup.md")

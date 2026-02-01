# DisassociateAttributeGroup

Disassociates an attribute group from an application to remove the extra attributes contained in the attribute group from the application's metadata. This operation reverts `AssociateAttributeGroup`.

## Request Syntax

```
DELETE /applications/`application`/attribute-groups/`attributeGroup` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[application](#API_app-registry_DisassociateAttributeGroup_RequestSyntax "#API_app-registry_DisassociateAttributeGroup_RequestSyntax")**

The name, ID, or ARN
of the application.

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`

Required: Yes

**[attributeGroup](#API_app-registry_DisassociateAttributeGroup_RequestSyntax "#API_app-registry_DisassociateAttributeGroup_RequestSyntax")**

The name, ID, or ARN
of the attribute group
that holds the attributes
to describe the application.

Length Constraints: Minimum length of 1. Maximum length of 512.

Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+)`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationArn": "***string***",
   "attributeGroupArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[applicationArn](#API_app-registry_DisassociateAttributeGroup_ResponseSyntax "#API_app-registry_DisassociateAttributeGroup_ResponseSyntax")**

The Amazon resource name (ARN) that specifies the application.

Type: String

Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`

**[attributeGroupArn](#API_app-registry_DisassociateAttributeGroup_ResponseSyntax "#API_app-registry_DisassociateAttributeGroup_ResponseSyntax")**

The Amazon resource name (ARN) that specifies the attribute group.

Type: String

Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+`

## Errors

**InternalServerException**

The service is experiencing internal problems.

HTTP Status Code: 500

**ResourceNotFoundException**

The specified resource does not exist.

HTTP Status Code: 404

**ValidationException**

The request has invalid or missing parameters.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md "../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup.md")

# DeleteAttributeGroup

Deletes an attribute group, specified either by its attribute group ID, name, or ARN.

## Request Syntax

```
DELETE /attribute-groups/`attributeGroup` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[attributeGroup](#API_app-registry_DeleteAttributeGroup_RequestSyntax "#API_app-registry_DeleteAttributeGroup_RequestSyntax")**

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
   "attributeGroup": {
      "arn": "***string***",
      "createdBy": "***string***",
      "creationTime": "***string***",
      "description": "***string***",
      "id": "***string***",
      "lastUpdateTime": "***string***",
      "name": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[attributeGroup](#API_app-registry_DeleteAttributeGroup_ResponseSyntax "#API_app-registry_DeleteAttributeGroup_ResponseSyntax")**

Information about the deleted attribute group.

Type: [AttributeGroupSummary](API_app-registry_AttributeGroupSummary.md "API_app-registry_AttributeGroupSummary.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md "../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/DeleteAttributeGroup.md")

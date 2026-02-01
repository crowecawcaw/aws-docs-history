# UpdateAttributeGroup

Updates an existing attribute group with new details.

## Request Syntax

```
PATCH /attribute-groups/`attributeGroup` HTTP/1.1
Content-type: application/json

{
   "attributes": "`string`",
   "description": "`string`",
   "name": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[attributeGroup](#API_app-registry_UpdateAttributeGroup_RequestSyntax "#API_app-registry_UpdateAttributeGroup_RequestSyntax")**

The name, ID, or ARN
of the attribute group
that holds the attributes
to describe the application.

Length Constraints: Minimum length of 1. Maximum length of 512.

Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+)`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[attributes](#API_app-registry_UpdateAttributeGroup_RequestSyntax "#API_app-registry_UpdateAttributeGroup_RequestSyntax")**

A JSON string in the form of nested key-value pairs that represent the attributes in the group and describes an application and its components.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 8000.

Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`

Required: No

**[description](#API_app-registry_UpdateAttributeGroup_RequestSyntax "#API_app-registry_UpdateAttributeGroup_RequestSyntax")**

The description of the attribute group that the user provides.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

**[name](#API_app-registry_UpdateAttributeGroup_RequestSyntax "#API_app-registry_UpdateAttributeGroup_RequestSyntax")**

Deprecated: The new name of the attribute group. The name must be unique in the region in which you are
updating the attribute group. Please do not use this field as we have stopped supporting name updates.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[-.\w]+`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "attributeGroup": {
      "arn": "***string***",
      "creationTime": "***string***",
      "description": "***string***",
      "id": "***string***",
      "lastUpdateTime": "***string***",
      "name": "***string***",
      "tags": {
         "***string***" : "***string***"
      }
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[attributeGroup](#API_app-registry_UpdateAttributeGroup_ResponseSyntax "#API_app-registry_UpdateAttributeGroup_ResponseSyntax")**

The updated information of the attribute group.

Type: [AttributeGroup](API_app-registry_AttributeGroup.md "API_app-registry_AttributeGroup.md") object

## Errors

**ConflictException**

There was a conflict when processing the request (for example, a resource with the given
name already exists within the account).

HTTP Status Code: 409

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

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md "../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup.md")

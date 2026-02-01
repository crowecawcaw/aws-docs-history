# CreateAttributeGroup

Creates a new attribute group as a container for user-defined attributes. This feature
enables users to have full control over their cloud application's metadata in a rich
machine-readable format to facilitate integration with automated workflows and third-party
tools.

## Request Syntax

```
POST /attribute-groups HTTP/1.1
Content-type: application/json

{
   "attributes": "`string`",
   "clientToken": "`string`",
   "description": "`string`",
   "name": "`string`",
   "tags": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[attributes](#API_app-registry_CreateAttributeGroup_RequestSyntax "#API_app-registry_CreateAttributeGroup_RequestSyntax")**

A JSON string in the form of nested key-value pairs that represent the attributes in the group and describes an application and its components.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 8000.

Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`

Required: Yes

**[clientToken](#API_app-registry_CreateAttributeGroup_RequestSyntax "#API_app-registry_CreateAttributeGroup_RequestSyntax")**

A unique identifier that you provide to ensure idempotency. If you retry a request that
completed successfully using the same client token and the same parameters, the retry succeeds
without performing any further actions. If you retry a successful request using the same
client token, but one or more of the parameters are different, the retry fails.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

Required: Yes

**[description](#API_app-registry_CreateAttributeGroup_RequestSyntax "#API_app-registry_CreateAttributeGroup_RequestSyntax")**

The description of the attribute group that the user provides.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

**[name](#API_app-registry_CreateAttributeGroup_RequestSyntax "#API_app-registry_CreateAttributeGroup_RequestSyntax")**

The name of the attribute group.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[-.\w]+`

Required: Yes

**[tags](#API_app-registry_CreateAttributeGroup_RequestSyntax "#API_app-registry_CreateAttributeGroup_RequestSyntax")**

Key-value pairs you can use to associate with the attribute group.

Type: String to string map

Map Entries: Minimum number of 0 items. Maximum number of 50 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`

Value Length Constraints: Maximum length of 256.

Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`

Required: No

## Response Syntax

```
HTTP/1.1 201
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

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

**[attributeGroup](#API_app-registry_CreateAttributeGroup_ResponseSyntax "#API_app-registry_CreateAttributeGroup_ResponseSyntax")**

Information about the attribute group.

Type: [AttributeGroup](API_app-registry_AttributeGroup.md "API_app-registry_AttributeGroup.md") object

## Errors

**ConflictException**

There was a conflict when processing the request (for example, a resource with the given
name already exists within the account).

HTTP Status Code: 409

**InternalServerException**

The service is experiencing internal problems.

HTTP Status Code: 500

**ServiceQuotaExceededException**

The maximum number
of resources per account
has been reached.

HTTP Status Code: 402

**ValidationException**

The request has invalid or missing parameters.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md "../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/CreateAttributeGroup.md")

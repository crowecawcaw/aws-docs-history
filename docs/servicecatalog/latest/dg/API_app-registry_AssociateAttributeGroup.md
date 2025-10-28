# AssociateAttributeGroup

Associates an attribute group with an application to augment the application's metadata
with the group's attributes. This feature enables applications to be described with
user-defined details that are machine-readable, such as third-party integrations.

## Request Syntax

```
PUT /applications/`application`/attribute-groups/`attributeGroup` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[application](#API_app-registry_AssociateAttributeGroup_RequestSyntax "#API_app-registry_AssociateAttributeGroup_RequestSyntax")**

The name, ID, or ARN
of the application.

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`

Required: Yes

**[attributeGroup](#API_app-registry_AssociateAttributeGroup_RequestSyntax "#API_app-registry_AssociateAttributeGroup_RequestSyntax")**

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

**[applicationArn](#API_app-registry_AssociateAttributeGroup_ResponseSyntax "#API_app-registry_AssociateAttributeGroup_ResponseSyntax")**

The Amazon resource name (ARN) of the application that was augmented with attributes.

Type: String

Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`

**[attributeGroupArn](#API_app-registry_AssociateAttributeGroup_ResponseSyntax "#API_app-registry_AssociateAttributeGroup_ResponseSyntax")**

The Amazon resource name (ARN) of the attribute group that contains the application's new attributes.

Type: String

Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+`

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

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md "../../../goto/DotNetSDKV3/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup.md")

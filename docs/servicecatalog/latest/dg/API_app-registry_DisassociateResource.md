# DisassociateResource

Disassociates a resource from application.
Both the resource and the application can be specified either by ID or name.

**Minimum permissions**

You must have the following permissions to remove a resource that's been associated with an application using the `APPLY_APPLICATION_TAG` option for [AssociateResource](API_app-registry_AssociateResource.md "API_app-registry_AssociateResource.md").

- `tag:GetResources`
- `tag:UntagResources`

You must also have the following permissions if you don't use the `AWSServiceCatalogAppRegistryFullAccess` policy.
For more information, see [AWSServiceCatalogAppRegistryFullAccess](../arguide/full.md "../arguide/full.md") in the AppRegistry Administrator Guide.

- `resource-groups:DisassociateResource`
- `cloudformation:UpdateStack`
- `cloudformation:DescribeStacks`

###### Note

In addition, you must have the tagging permission defined by the AWS service that creates the resource.
For more information, see [UntagResources](../../../resourcegroupstagging/latest/APIReference/API_UntTagResources.md "../../../resourcegroupstagging/latest/APIReference/API_UntTagResources.md") in the _Resource Groups Tagging API Reference_.

## Request Syntax

```
DELETE /applications/`application`/resources/`resourceType`/`resource` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[application](#API_app-registry_DisassociateResource_RequestSyntax "#API_app-registry_DisassociateResource_RequestSyntax")**

The name or ID of the application.

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`

Required: Yes

**[resource](#API_app-registry_DisassociateResource_RequestSyntax "#API_app-registry_DisassociateResource_RequestSyntax")**

The name or ID of the resource.

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `\S+`

Required: Yes

**[resourceType](#API_app-registry_DisassociateResource_RequestSyntax "#API_app-registry_DisassociateResource_RequestSyntax")**

The type of the resource that is being disassociated.

Valid Values: `CFN_STACK | RESOURCE_TAG_VALUE`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationArn": "***string***",
   "resourceArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[applicationArn](#API_app-registry_DisassociateResource_ResponseSyntax "#API_app-registry_DisassociateResource_ResponseSyntax")**

The Amazon resource name (ARN) that specifies the application.

Type: String

Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`

**[resourceArn](#API_app-registry_DisassociateResource_ResponseSyntax "#API_app-registry_DisassociateResource_ResponseSyntax")**

The Amazon resource name (ARN) that specifies the resource.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

## Errors

**InternalServerException**

The service is experiencing internal problems.

HTTP Status Code: 500

**ResourceNotFoundException**

The specified resource does not exist.

HTTP Status Code: 404

**ThrottlingException**

The maximum number
of API requests
has been exceeded.

**message**

A message associated with the Throttling exception.

**serviceCode**

The originating service code.

HTTP Status Code: 429

**ValidationException**

The request has invalid or missing parameters.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/DisassociateResource.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/DisassociateResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/DisassociateResource.md "../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/DisassociateResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/DisassociateResource.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/DisassociateResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/DisassociateResource.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/DisassociateResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/DisassociateResource.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/DisassociateResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/DisassociateResource.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/DisassociateResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/DisassociateResource.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/DisassociateResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/DisassociateResource.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/DisassociateResource.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/DisassociateResource.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/DisassociateResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/DisassociateResource.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/DisassociateResource.md")

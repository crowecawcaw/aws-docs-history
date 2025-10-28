# AssociateResource

Associates a resource with an application.
The resource can be specified by its ARN or name.
The application can be specified by ARN, ID, or name.

**Minimum permissions**

You must have the following permissions to associate a resource using the `OPTIONS` parameter set to `APPLY_APPLICATION_TAG`.

- `tag:GetResources`
- `tag:TagResources`

You must also have these additional permissions if you don't use the `AWSServiceCatalogAppRegistryFullAccess` policy.
For more information, see [AWSServiceCatalogAppRegistryFullAccess](../arguide/full.md "../arguide/full.md") in the AppRegistry Administrator Guide.

- `resource-groups:AssociateResource`
- `cloudformation:UpdateStack`
- `cloudformation:DescribeStacks`

###### Note

In addition, you must have the tagging permission defined by the AWS service that creates the resource.
For more information, see [TagResources](../../../resourcegroupstagging/latest/APIReference/API_TagResources.md "../../../resourcegroupstagging/latest/APIReference/API_TagResources.md") in the _Resource Groups Tagging API Reference_.

## Request Syntax

```
PUT /applications/`application`/resources/`resourceType`/`resource` HTTP/1.1
Content-type: application/json

{
   "options": [ "`string`" ]
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[application](#API_app-registry_AssociateResource_RequestSyntax "#API_app-registry_AssociateResource_RequestSyntax")**

The name, ID, or ARN
of the application.

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`

Required: Yes

**[resource](#API_app-registry_AssociateResource_RequestSyntax "#API_app-registry_AssociateResource_RequestSyntax")**

The name or ID of the resource of which the application will be associated.

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `\S+`

Required: Yes

**[resourceType](#API_app-registry_AssociateResource_RequestSyntax "#API_app-registry_AssociateResource_RequestSyntax")**

The type of resource of which the application will be associated.

Valid Values: `CFN_STACK | RESOURCE_TAG_VALUE`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[options](#API_app-registry_AssociateResource_RequestSyntax "#API_app-registry_AssociateResource_RequestSyntax")**

Determines whether an application tag is applied or skipped.

Type: Array of strings

Valid Values: `APPLY_APPLICATION_TAG | SKIP_APPLICATION_TAG`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationArn": "***string***",
   "options": [ "***string***" ],
   "resourceArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[applicationArn](#API_app-registry_AssociateResource_ResponseSyntax "#API_app-registry_AssociateResource_ResponseSyntax")**

The Amazon resource name (ARN) of the application that was augmented with attributes.

Type: String

Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`

**[options](#API_app-registry_AssociateResource_ResponseSyntax "#API_app-registry_AssociateResource_ResponseSyntax")**

Determines whether an application tag is applied or skipped.

Type: Array of strings

Valid Values: `APPLY_APPLICATION_TAG | SKIP_APPLICATION_TAG`

**[resourceArn](#API_app-registry_AssociateResource_ResponseSyntax "#API_app-registry_AssociateResource_ResponseSyntax")**

The Amazon resource name (ARN) that specifies the resource.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

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

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/AssociateResource.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/AssociateResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/AWS242AppRegistry-2020-06-24/AssociateResource.md "../../../goto/DotNetSDKV3/AWS242AppRegistry-2020-06-24/AssociateResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/AssociateResource.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/AssociateResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/AssociateResource.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/AssociateResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/AssociateResource.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/AssociateResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/AssociateResource.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/AssociateResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/AssociateResource.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/AssociateResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/AssociateResource.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/AssociateResource.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/AssociateResource.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/AssociateResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/AssociateResource.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/AssociateResource.md")

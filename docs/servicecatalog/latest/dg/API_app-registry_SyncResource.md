# SyncResource

Syncs the resource with current AppRegistry records.

Specifically, the resource’s AppRegistry system tags sync with its associated application. We remove the resource's AppRegistry system tags if it does not associate with the application. The caller must have permissions to read and update the resource.

## Request Syntax

```
POST /sync/`resourceType`/`resource` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[resource](#API_app-registry_SyncResource_RequestSyntax "#API_app-registry_SyncResource_RequestSyntax")**

An entity you can work with and specify with a name or ID. Examples include an Amazon EC2 instance, an AWS CloudFormation stack, or an Amazon S3 bucket.

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `\S+`

Required: Yes

**[resourceType](#API_app-registry_SyncResource_RequestSyntax "#API_app-registry_SyncResource_RequestSyntax")**

The type of resource of which the application will be associated.

Valid Values: `CFN_STACK | RESOURCE_TAG_VALUE`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "actionTaken": "***string***",
   "applicationArn": "***string***",
   "resourceArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[actionTaken](#API_app-registry_SyncResource_ResponseSyntax "#API_app-registry_SyncResource_ResponseSyntax")**

The results of the output if an application is associated with an ARN value, which could be `syncStarted` or None.

Type: String

Valid Values: `START_SYNC | NO_ACTION`

**[applicationArn](#API_app-registry_SyncResource_ResponseSyntax "#API_app-registry_SyncResource_ResponseSyntax")**

The Amazon resource name (ARN) that specifies the application.

Type: String

Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`

**[resourceArn](#API_app-registry_SyncResource_ResponseSyntax "#API_app-registry_SyncResource_ResponseSyntax")**

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

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/SyncResource.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/SyncResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/SyncResource.md "../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/SyncResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/SyncResource.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/SyncResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/SyncResource.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/SyncResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/SyncResource.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/SyncResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/SyncResource.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/SyncResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/SyncResource.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/SyncResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/SyncResource.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/SyncResource.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/SyncResource.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/SyncResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/SyncResource.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/SyncResource.md")

# CreateProject

Creates a new DataBrew project.

## Request Syntax

```
POST /projects HTTP/1.1
Content-type: application/json

{
   "DatasetName": "`string`",
   "Name": "`string`",
   "RecipeName": "`string`",
   "RoleArn": "`string`",
   "Sample": {
      "Size": `number`,
      "Type": "`string`"
   },
   "Tags": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[DatasetName](#API_CreateProject_RequestSyntax "#API_CreateProject_RequestSyntax")**

The name of an existing dataset to associate this project with.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**[Name](#API_CreateProject_RequestSyntax "#API_CreateProject_RequestSyntax")**

A unique name for the new project. Valid characters are alphanumeric (A-Z, a-z, 0-9),
hyphen (-), period (.), and space.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**[RecipeName](#API_CreateProject_RequestSyntax "#API_CreateProject_RequestSyntax")**

The name of an existing recipe to associate with the project.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**[RoleArn](#API_CreateProject_RequestSyntax "#API_CreateProject_RequestSyntax")**

The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role to
be assumed for this request.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: Yes

**[Sample](#API_CreateProject_RequestSyntax "#API_CreateProject_RequestSyntax")**

Represents the sample size and sampling type for DataBrew to use for interactive data
analysis.

Type: [Sample](API_Sample.md "API_Sample.md") object

Required: No

**[Tags](#API_CreateProject_RequestSyntax "#API_CreateProject_RequestSyntax")**

Metadata tags to apply to this project.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Name](#API_CreateProject_ResponseSyntax "#API_CreateProject_ResponseSyntax")**

The name of the project that you created.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ConflictException**

Updating or deleting a resource can cause an inconsistent state.

HTTP Status Code: 409

**InternalServerException**

An internal service failure occurred.

HTTP Status Code: 500

**ServiceQuotaExceededException**

A service quota is exceeded.

HTTP Status Code: 402

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/CreateProject.md "../../../goto/cli2/databrew-2017-07-25/CreateProject.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/databrew-2017-07-25/CreateProject.md "../../../goto/DotNetSDKV3/databrew-2017-07-25/CreateProject.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/CreateProject.md "../../../goto/SdkForCpp/databrew-2017-07-25/CreateProject.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/CreateProject.md "../../../goto/SdkForGoV2/databrew-2017-07-25/CreateProject.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/CreateProject.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/CreateProject.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/CreateProject.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/CreateProject.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/CreateProject.md "../../../goto/SdkForKotlin/databrew-2017-07-25/CreateProject.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/CreateProject.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/CreateProject.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/CreateProject.md "../../../goto/boto3/databrew-2017-07-25/CreateProject.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/CreateProject.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/CreateProject.md")

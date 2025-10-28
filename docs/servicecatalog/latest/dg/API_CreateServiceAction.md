# CreateServiceAction

Creates a self-service action.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "Definition": {
      "`string`" : "`string`"
   },
   "DefinitionType": "`string`",
   "Description": "`string`",
   "IdempotencyToken": "`string`",
   "Name": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_CreateServiceAction_RequestSyntax "#API_CreateServiceAction_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[Definition](#API_CreateServiceAction_RequestSyntax "#API_CreateServiceAction_RequestSyntax")**

The self-service action definition. Can be one of the following:

Name

The name of the AWS Systems Manager document (SSM document). For example, `AWS-RestartEC2Instance`.

If you are using a shared SSM document, you must provide the ARN instead of the name.

Version

The AWS Systems Manager automation document version. For example, `"Version": "1"`

AssumeRole

The Amazon Resource Name (ARN) of the role that performs the self-service actions on your behalf. For example, `"AssumeRole": "arn:aws:iam::12345678910:role/ActionRole"`.

To reuse the provisioned product launch role, set to `"AssumeRole": "LAUNCH_ROLE"`.

Parameters

The list of parameters in JSON format.

For example: `[{\"Name\":\"InstanceId\",\"Type\":\"TARGET\"}]` or `[{\"Name\":\"InstanceId\",\"Type\":\"TEXT_VALUE\"}]`.

Type: String to string map

Map Entries: Maximum number of 100 items.

Valid Keys: `Name | Version | AssumeRole | Parameters`

Value Length Constraints: Minimum length of 1. Maximum length of 1024.

Required: Yes

**[DefinitionType](#API_CreateServiceAction_RequestSyntax "#API_CreateServiceAction_RequestSyntax")**

The service action definition type. For example, `SSM_AUTOMATION`.

Type: String

Valid Values: `SSM_AUTOMATION`

Required: Yes

**[Description](#API_CreateServiceAction_RequestSyntax "#API_CreateServiceAction_RequestSyntax")**

The self-service action description.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

**[IdempotencyToken](#API_CreateServiceAction_RequestSyntax "#API_CreateServiceAction_RequestSyntax")**

A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token,
the same response is returned for each repeated request.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

Required: Yes

**[Name](#API_CreateServiceAction_RequestSyntax "#API_CreateServiceAction_RequestSyntax")**

The self-service action name.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `^[a-zA-Z0-9_\-.]*`

Required: Yes

## Response Syntax

```
{
   "ServiceActionDetail": {
      "Definition": {
         "***string***" : "***string***"
      },
      "ServiceActionSummary": {
         "DefinitionType": "***string***",
         "Description": "***string***",
         "Id": "***string***",
         "Name": "***string***"
      }
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ServiceActionDetail](#API_CreateServiceAction_ResponseSyntax "#API_CreateServiceAction_ResponseSyntax")**

An object containing information about the self-service action.

Type: [ServiceActionDetail](API_ServiceActionDetail.md "API_ServiceActionDetail.md") object

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**LimitExceededException**

The current limits of the service would have been exceeded by this operation. Decrease your
resource use or increase your service limits and retry the operation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/CreateServiceAction.md "../../../goto/cli2/servicecatalog-2015-12-10/CreateServiceAction.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/CreateServiceAction.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/CreateServiceAction.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/CreateServiceAction.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/CreateServiceAction.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/CreateServiceAction.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/CreateServiceAction.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/CreateServiceAction.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/CreateServiceAction.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/CreateServiceAction.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/CreateServiceAction.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/CreateServiceAction.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/CreateServiceAction.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/CreateServiceAction.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/CreateServiceAction.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/CreateServiceAction.md "../../../goto/boto3/servicecatalog-2015-12-10/CreateServiceAction.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/CreateServiceAction.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/CreateServiceAction.md")

# Applications applicationId Templates templateId

## URI

`/applications/`applicationId`/templates/`templateId``

## HTTP methods

### GET

**Operation ID:** `GetCloudFormationTemplate`

Gets the specified AWS CloudFormation template.

| Path parameters | Name   | Type | Required                                                                                                                                   | Description |
| --------------- | ------ | ---- | ------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| `applicationId` | String | True | The Amazon Resource Name (ARN) of the application.                                                                                         |
| `templateId`    | String | True | The UUID returned by CreateCloudFormationTemplate.Pattern: [0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12} |

| Responses | Status code                    | Response model                                                                                 | Description |
| --------- | ------------------------------ | ---------------------------------------------------------------------------------------------- | ----------- |
| `200`     | `TemplateDetails`              | Success                                                                                        |
| `400`     | `BadRequestException`          | One of the parameters in the request is invalid.                                               |
| `403`     | `ForbiddenException`           | The client is not authenticated.                                                               |
| `404`     | `NotFoundException`            | The resource (for example, an access policy statement) specified in the request doesn't exist. |
| `429`     | `TooManyRequestsException`     | The client is sending more than the allowed number of requests per unit of time.               |
| `500`     | `InternalServerErrorException` | The AWS Serverless Application Repository service encountered an internal error.               |

### OPTIONS

| Path parameters | Name   | Type | Required                                                                                                                                   | Description |
| --------------- | ------ | ---- | ------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| `applicationId` | String | True | The Amazon Resource Name (ARN) of the application.                                                                                         |
| `templateId`    | String | True | The UUID returned by CreateCloudFormationTemplate.Pattern: [0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12} |

| Responses | Status code | Response model | Description |
| --------- | ----------- | -------------- | ----------- |
| `200`     | None        | 200 response   |

## Schemas

### Response bodies

```
{
  "templateId": "string",
  "templateUrl": "string",
  "applicationId": "string",
  "semanticVersion": "string",
  "status": enum,
  "creationTime": "string",
  "expirationTime": "string"
}
```

```
{
  "message": "string",
  "errorCode": "string"
}
```

```
{
  "message": "string",
  "errorCode": "string"
}
```

```
{
  "message": "string",
  "errorCode": "string"
}
```

```
{
  "message": "string",
  "errorCode": "string"
}
```

```
{
  "message": "string",
  "errorCode": "string"
}
```

## Properties

### BadRequestException

One of the parameters in the request is invalid.

| Property    | Type   | Required | Description                                      |
| ----------- | ------ | -------- | ------------------------------------------------ |
| `errorCode` | string | False    | 400                                              |
| `message`   | string | False    | One of the parameters in the request is invalid. |

### ForbiddenException

The client is not authenticated.

| Property    | Type   | Required | Description                      |
| ----------- | ------ | -------- | -------------------------------- |
| `errorCode` | string | False    | 403                              |
| `message`   | string | False    | The client is not authenticated. |

### InternalServerErrorException

The AWS Serverless Application Repository service encountered an internal error.

| Property    | Type   | Required | Description                                                                      |
| ----------- | ------ | -------- | -------------------------------------------------------------------------------- |
| `errorCode` | string | False    | 500                                                                              |
| `message`   | string | False    | The AWS Serverless Application Repository service encountered an internal error. |

### NotFoundException

The resource (for example, an access policy statement) specified in the request doesn't exist.

| Property    | Type   | Required | Description                                                                                    |
| ----------- | ------ | -------- | ---------------------------------------------------------------------------------------------- |
| `errorCode` | string | False    | 404                                                                                            |
| `message`   | string | False    | The resource (for example, an access policy statement) specified in the request doesn't exist. |

### TemplateDetails

Details of the template.

| Property          | Type                     | Required | Description                                                                                                                                |
| ----------------- | ------------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---- | -------------------------------------------------------------------- | ------ | -------- |
| `applicationId`   | string                   | True     | The application Amazon Resource Name (ARN).                                                                                                |
| `creationTime`    | string                   | True     | The date and time this resource was created.                                                                                               |
| `expirationTime`  | string                   | True     | The date and time this template expires. Templates expire 1 hour after creation.                                                           |
| `semanticVersion` | string                   | True     | The semantic version of the application:<br>[https://semver.org/](https://semver.org/ "https://semver.org/")                               |
| `status`          | stringValues: `PREPARING | ACTIVE   | EXPIRED`                                                                                                                                   | True | Status of the template creation workflow.Possible values: `PREPARING | ACTIVE | EXPIRED` |
| `templateId`      | string                   | True     | The UUID returned by CreateCloudFormationTemplate.Pattern: [0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12} |
| `templateUrl`     | string                   | True     | A link to the template that can be used to deploy the application using AWS CloudFormation.                                                |

### TooManyRequestsException

The client is sending more than the allowed number of requests per unit of time.

| Property    | Type   | Required | Description                                                                      |
| ----------- | ------ | -------- | -------------------------------------------------------------------------------- |
| `errorCode` | string | False    | 429                                                                              |
| `message`   | string | False    | The client is sending more than the allowed number of requests per unit of time. |

## See also

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetCloudFormationTemplate

- [AWS Command Line Interface V2](../../../goto/cli2/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md "../../../goto/cli2/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md "../../../goto/DotNetSDKV3/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md "../../../goto/SdkForCpp/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md "../../../goto/SdkForGoV2/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md "../../../goto/SdkForJavaV2/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md "../../../goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md "../../../goto/SdkForKotlin/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md "../../../goto/SdkForPHPV3/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md")
- [AWS SDK for Python](../../../goto/boto3/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md "../../../goto/boto3/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md "../../../goto/SdkForRubyV3/serverlessrepo-2017-09-08/GetCloudFormationTemplate.md")

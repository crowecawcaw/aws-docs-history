# Applications applicationId Policy

## URI

`/applications/`applicationId`/policy`

## HTTP methods

### GET

**Operation ID:** `GetApplicationPolicy`

Retrieves the policy for the application.

| Path parameters | Name   | Type | Required                                           | Description |
| --------------- | ------ | ---- | -------------------------------------------------- | ----------- |
| `applicationId` | String | True | The Amazon Resource Name (ARN) of the application. |

| Responses | Status code                    | Response model                                                                                 | Description |
| --------- | ------------------------------ | ---------------------------------------------------------------------------------------------- | ----------- |
| `200`     | `ApplicationPolicy`            | Success                                                                                        |
| `400`     | `BadRequestException`          | One of the parameters in the request is invalid.                                               |
| `403`     | `ForbiddenException`           | The client is not authenticated.                                                               |
| `404`     | `NotFoundException`            | The resource (for example, an access policy statement) specified in the request doesn't exist. |
| `429`     | `TooManyRequestsException`     | The client is sending more than the allowed number of requests per unit of time.               |
| `500`     | `InternalServerErrorException` | The AWS Serverless Application Repository service encountered an internal error.               |

### PUT

**Operation ID:** `PutApplicationPolicy`

Sets the permission policy for an application. For the list of actions supported for this operation, see
[Application
Permissions](access-control-resource-based.md#application-permissions "access-control-resource-based.md#application-permissions") .

| Path parameters | Name   | Type | Required                                           | Description |
| --------------- | ------ | ---- | -------------------------------------------------- | ----------- |
| `applicationId` | String | True | The Amazon Resource Name (ARN) of the application. |

| Responses | Status code                    | Response model                                                                                 | Description |
| --------- | ------------------------------ | ---------------------------------------------------------------------------------------------- | ----------- |
| `200`     | `ApplicationPolicy`            | Success                                                                                        |
| `400`     | `BadRequestException`          | One of the parameters in the request is invalid.                                               |
| `403`     | `ForbiddenException`           | The client is not authenticated.                                                               |
| `404`     | `NotFoundException`            | The resource (for example, an access policy statement) specified in the request doesn't exist. |
| `429`     | `TooManyRequestsException`     | The client is sending more than the allowed number of requests per unit of time.               |
| `500`     | `InternalServerErrorException` | The AWS Serverless Application Repository service encountered an internal error.               |

### OPTIONS

| Path parameters | Name   | Type | Required                                           | Description |
| --------------- | ------ | ---- | -------------------------------------------------- | ----------- |
| `applicationId` | String | True | The Amazon Resource Name (ARN) of the application. |

| Responses | Status code | Response model | Description |
| --------- | ----------- | -------------- | ----------- |
| `200`     | None        | 200 response   |

## Schemas

### Request bodies

```
{
  "statements": [
    {
      "statementId": "string",
      "principals": [
        "string"
      ],
      "actions": [
        "string"
      ],
      "principalOrgIDs": [
        "string"
      ]
    }
  ]
}
```

### Response bodies

```
{
  "statements": [
    {
      "statementId": "string",
      "principals": [
        "string"
      ],
      "actions": [
        "string"
      ],
      "principalOrgIDs": [
        "string"
      ]
    }
  ]
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

### ApplicationPolicy

Policy statements applied to the application.

| Property     | Type                                     | Required | Description                                               |
| ------------ | ---------------------------------------- | -------- | --------------------------------------------------------- |
| `statements` | Array of type ApplicationPolicyStatement | True     | An array of policy statements applied to the application. |

### ApplicationPolicyStatement

Policy statement applied to the application.

| Property          | Type                 | Required | Description                                                                                                                                                                                                  |
| ----------------- | -------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `actions`         | Array of type string | True     | For the list of actions supported for this operation, see [Application<br>Permissions](access-control-resource-based.md#application-permissions "access-control-resource-based.md#application-permissions"). |
| `principalOrgIDs` | Array of type string | False    | The AWS Organizations ID to share the application with.                                                                                                                                                      |
| `principals`      | Array of type string | True     | An array of AWS account IDs to share the application with, or \<br>• to make the application<br>public.                                                                                                      |
| `statementId`     | string               | False    | A unique ID for the statement.                                                                                                                                                                               |

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

### TooManyRequestsException

The client is sending more than the allowed number of requests per unit of time.

| Property    | Type   | Required | Description                                                                      |
| ----------- | ------ | -------- | -------------------------------------------------------------------------------- |
| `errorCode` | string | False    | 429                                                                              |
| `message`   | string | False    | The client is sending more than the allowed number of requests per unit of time. |

## See also

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetApplicationPolicy

- [AWS Command Line Interface V2](../../../goto/cli2/serverlessrepo-2017-09-08/GetApplicationPolicy.md "../../../goto/cli2/serverlessrepo-2017-09-08/GetApplicationPolicy.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/serverlessrepo-2017-09-08/GetApplicationPolicy.md "../../../goto/DotNetSDKV4/serverlessrepo-2017-09-08/GetApplicationPolicy.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/serverlessrepo-2017-09-08/GetApplicationPolicy.md "../../../goto/SdkForCpp/serverlessrepo-2017-09-08/GetApplicationPolicy.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/serverlessrepo-2017-09-08/GetApplicationPolicy.md "../../../goto/SdkForGoV2/serverlessrepo-2017-09-08/GetApplicationPolicy.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/serverlessrepo-2017-09-08/GetApplicationPolicy.md "../../../goto/SdkForJavaV2/serverlessrepo-2017-09-08/GetApplicationPolicy.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/GetApplicationPolicy.md "../../../goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/GetApplicationPolicy.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/serverlessrepo-2017-09-08/GetApplicationPolicy.md "../../../goto/SdkForKotlin/serverlessrepo-2017-09-08/GetApplicationPolicy.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/serverlessrepo-2017-09-08/GetApplicationPolicy.md "../../../goto/SdkForPHPV3/serverlessrepo-2017-09-08/GetApplicationPolicy.md")
- [AWS SDK for Python](../../../goto/boto3/serverlessrepo-2017-09-08/GetApplicationPolicy.md "../../../goto/boto3/serverlessrepo-2017-09-08/GetApplicationPolicy.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/serverlessrepo-2017-09-08/GetApplicationPolicy.md "../../../goto/SdkForRubyV3/serverlessrepo-2017-09-08/GetApplicationPolicy.md")

### PutApplicationPolicy

- [AWS Command Line Interface V2](../../../goto/cli2/serverlessrepo-2017-09-08/PutApplicationPolicy.md "../../../goto/cli2/serverlessrepo-2017-09-08/PutApplicationPolicy.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/serverlessrepo-2017-09-08/PutApplicationPolicy.md "../../../goto/DotNetSDKV4/serverlessrepo-2017-09-08/PutApplicationPolicy.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/serverlessrepo-2017-09-08/PutApplicationPolicy.md "../../../goto/SdkForCpp/serverlessrepo-2017-09-08/PutApplicationPolicy.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/serverlessrepo-2017-09-08/PutApplicationPolicy.md "../../../goto/SdkForGoV2/serverlessrepo-2017-09-08/PutApplicationPolicy.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/serverlessrepo-2017-09-08/PutApplicationPolicy.md "../../../goto/SdkForJavaV2/serverlessrepo-2017-09-08/PutApplicationPolicy.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/PutApplicationPolicy.md "../../../goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/PutApplicationPolicy.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/serverlessrepo-2017-09-08/PutApplicationPolicy.md "../../../goto/SdkForKotlin/serverlessrepo-2017-09-08/PutApplicationPolicy.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/serverlessrepo-2017-09-08/PutApplicationPolicy.md "../../../goto/SdkForPHPV3/serverlessrepo-2017-09-08/PutApplicationPolicy.md")
- [AWS SDK for Python](../../../goto/boto3/serverlessrepo-2017-09-08/PutApplicationPolicy.md "../../../goto/boto3/serverlessrepo-2017-09-08/PutApplicationPolicy.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/serverlessrepo-2017-09-08/PutApplicationPolicy.md "../../../goto/SdkForRubyV3/serverlessrepo-2017-09-08/PutApplicationPolicy.md")

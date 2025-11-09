# Applications applicationId Unshare

## URI

`/applications/`applicationId`/unshare`

## HTTP methods

### POST

**Operation ID:** `UnshareApplication`

Unshares an application from an AWS Organization.

This operation can be called only from the organization's management account.

| Path parameters | Name   | Type | Required                                           | Description |
| --------------- | ------ | ---- | -------------------------------------------------- | ----------- |
| `applicationId` | String | True | The Amazon Resource Name (ARN) of the application. |

| Responses | Status code                    | Response model                                                                                 | Description |
| --------- | ------------------------------ | ---------------------------------------------------------------------------------------------- | ----------- |
| `204`     | None                           | Success                                                                                        |
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
  "organizationId": "string"
}
```

### Response bodies

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

### TooManyRequestsException

The client is sending more than the allowed number of requests per unit of time.

| Property    | Type   | Required | Description                                                                      |
| ----------- | ------ | -------- | -------------------------------------------------------------------------------- |
| `errorCode` | string | False    | 429                                                                              |
| `message`   | string | False    | The client is sending more than the allowed number of requests per unit of time. |

### UnshareApplicationInput

Unshare application request.

| Property         | Type   | Required | Description                                               |
| ---------------- | ------ | -------- | --------------------------------------------------------- |
| `organizationId` | string | True     | The AWS Organizations ID to unshare the application from. |

## See also

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UnshareApplication

- [AWS Command Line Interface V2](../../../goto/cli2/serverlessrepo-2017-09-08/UnshareApplication.md "../../../goto/cli2/serverlessrepo-2017-09-08/UnshareApplication.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/serverlessrepo-2017-09-08/UnshareApplication.md "../../../goto/DotNetSDKV3/serverlessrepo-2017-09-08/UnshareApplication.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/serverlessrepo-2017-09-08/UnshareApplication.md "../../../goto/SdkForCpp/serverlessrepo-2017-09-08/UnshareApplication.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/serverlessrepo-2017-09-08/UnshareApplication.md "../../../goto/SdkForGoV2/serverlessrepo-2017-09-08/UnshareApplication.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/serverlessrepo-2017-09-08/UnshareApplication.md "../../../goto/SdkForJavaV2/serverlessrepo-2017-09-08/UnshareApplication.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/UnshareApplication.md "../../../goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/UnshareApplication.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/serverlessrepo-2017-09-08/UnshareApplication.md "../../../goto/SdkForKotlin/serverlessrepo-2017-09-08/UnshareApplication.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/serverlessrepo-2017-09-08/UnshareApplication.md "../../../goto/SdkForPHPV3/serverlessrepo-2017-09-08/UnshareApplication.md")
- [AWS SDK for Python](../../../goto/boto3/serverlessrepo-2017-09-08/UnshareApplication.md "../../../goto/boto3/serverlessrepo-2017-09-08/UnshareApplication.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/serverlessrepo-2017-09-08/UnshareApplication.md "../../../goto/SdkForRubyV3/serverlessrepo-2017-09-08/UnshareApplication.md")

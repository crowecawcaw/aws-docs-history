# DescribeConnectorOperation

Returns information about the specified connector's operations.

## Request Syntax

```
GET /v1/connectorOperations/`connectorOperationArn` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[connectorOperationArn](#API_DescribeConnectorOperation_RequestSyntax "#API_DescribeConnectorOperation_RequestSyntax")**

ARN of the connector operation to be described.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "connectorArn": "***string***",
   "connectorOperationArn": "***string***",
   "connectorOperationState": "***string***",
   "connectorOperationType": "***string***",
   "creationTime": "***string***",
   "endTime": "***string***",
   "errorInfo": {
      "code": "***string***",
      "message": "***string***"
   },
   "operationSteps": [
      {
         "stepState": "***string***",
         "stepType": "***string***"
      }
   ],
   "originConnectorConfiguration": {
      "***string***" : "***string***"
   },
   "originWorkerSetting": {
      "capacity": {
         "autoScaling": {
            "maxWorkerCount": ***number***,
            "mcuCount": ***number***,
            "minWorkerCount": ***number***,
            "scaleInPolicy": {
               "cpuUtilizationPercentage": ***number***
            },
            "scaleOutPolicy": {
               "cpuUtilizationPercentage": ***number***
            }
         },
         "provisionedCapacity": {
            "mcuCount": ***number***,
            "workerCount": ***number***
         }
      }
   },
   "targetConnectorConfiguration": {
      "***string***" : "***string***"
   },
   "targetWorkerSetting": {
      "capacity": {
         "autoScaling": {
            "maxWorkerCount": ***number***,
            "mcuCount": ***number***,
            "minWorkerCount": ***number***,
            "scaleInPolicy": {
               "cpuUtilizationPercentage": ***number***
            },
            "scaleOutPolicy": {
               "cpuUtilizationPercentage": ***number***
            }
         },
         "provisionedCapacity": {
            "mcuCount": ***number***,
            "workerCount": ***number***
         }
      }
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[connectorArn](#API_DescribeConnectorOperation_ResponseSyntax "#API_DescribeConnectorOperation_ResponseSyntax")**

The Amazon Resource Name (ARN) of the connector.

Type: String

**[connectorOperationArn](#API_DescribeConnectorOperation_ResponseSyntax "#API_DescribeConnectorOperation_ResponseSyntax")**

The Amazon Resource Name (ARN) of the connector operation.

Type: String

**[connectorOperationState](#API_DescribeConnectorOperation_ResponseSyntax "#API_DescribeConnectorOperation_ResponseSyntax")**

The state of the connector operation.

Type: String

Valid Values: `PENDING | UPDATE_IN_PROGRESS | UPDATE_COMPLETE | UPDATE_FAILED | ROLLBACK_IN_PROGRESS | ROLLBACK_FAILED | ROLLBACK_COMPLETE`

**[connectorOperationType](#API_DescribeConnectorOperation_ResponseSyntax "#API_DescribeConnectorOperation_ResponseSyntax")**

The type of connector operation performed.

Type: String

Valid Values: `UPDATE_WORKER_SETTING | UPDATE_CONNECTOR_CONFIGURATION | ISOLATE_CONNECTOR | RESTORE_CONNECTOR`

**[creationTime](#API_DescribeConnectorOperation_ResponseSyntax "#API_DescribeConnectorOperation_ResponseSyntax")**

The time when the operation was created.

Type: Timestamp

**[endTime](#API_DescribeConnectorOperation_ResponseSyntax "#API_DescribeConnectorOperation_ResponseSyntax")**

The time when the operation ended.

Type: Timestamp

**[errorInfo](#API_DescribeConnectorOperation_ResponseSyntax "#API_DescribeConnectorOperation_ResponseSyntax")**

Details about the state of a resource.

Type: [StateDescription](API_StateDescription.md "API_StateDescription.md") object

**[operationSteps](#API_DescribeConnectorOperation_ResponseSyntax "#API_DescribeConnectorOperation_ResponseSyntax")**

The array of operation steps taken.

Type: Array of [ConnectorOperationStep](API_ConnectorOperationStep.md "API_ConnectorOperationStep.md") objects

**[originConnectorConfiguration](#API_DescribeConnectorOperation_ResponseSyntax "#API_DescribeConnectorOperation_ResponseSyntax")**

The origin connector configuration.

Type: String to string map

**[originWorkerSetting](#API_DescribeConnectorOperation_ResponseSyntax "#API_DescribeConnectorOperation_ResponseSyntax")**

The origin worker setting.

Type: [WorkerSetting](API_WorkerSetting.md "API_WorkerSetting.md") object

**[targetConnectorConfiguration](#API_DescribeConnectorOperation_ResponseSyntax "#API_DescribeConnectorOperation_ResponseSyntax")**

The target connector configuration.

Type: String to string map

**[targetWorkerSetting](#API_DescribeConnectorOperation_ResponseSyntax "#API_DescribeConnectorOperation_ResponseSyntax")**

The target worker setting.

Type: [WorkerSetting](API_WorkerSetting.md "API_WorkerSetting.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**BadRequestException**

HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then
retry it.

HTTP Status Code: 400

**ForbiddenException**

HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your
request.

HTTP Status Code: 403

**InternalServerErrorException**

HTTP Status Code 500: Unexpected internal server error. Retrying your request might
resolve the issue.

HTTP Status Code: 500

**NotFoundException**

HTTP Status Code 404: Resource not found due to incorrect input. Correct your request
and then retry it.

HTTP Status Code: 404

**ServiceUnavailableException**

HTTP Status Code 503: Service Unavailable. Retrying your request in some time might
resolve the issue.

HTTP Status Code: 503

**TooManyRequestsException**

HTTP Status Code 429: Limit exceeded. Resource limit reached.

HTTP Status Code: 429

**UnauthorizedException**

HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be
validated.

HTTP Status Code: 401

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kafkaconnect-2021-09-14/DescribeConnectorOperation.md "../../../goto/cli2/kafkaconnect-2021-09-14/DescribeConnectorOperation.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/kafkaconnect-2021-09-14/DescribeConnectorOperation.md "../../../goto/DotNetSDKV3/kafkaconnect-2021-09-14/DescribeConnectorOperation.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kafkaconnect-2021-09-14/DescribeConnectorOperation.md "../../../goto/SdkForCpp/kafkaconnect-2021-09-14/DescribeConnectorOperation.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kafkaconnect-2021-09-14/DescribeConnectorOperation.md "../../../goto/SdkForGoV2/kafkaconnect-2021-09-14/DescribeConnectorOperation.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/DescribeConnectorOperation.md "../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/DescribeConnectorOperation.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/DescribeConnectorOperation.md "../../../goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/DescribeConnectorOperation.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kafkaconnect-2021-09-14/DescribeConnectorOperation.md "../../../goto/SdkForKotlin/kafkaconnect-2021-09-14/DescribeConnectorOperation.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kafkaconnect-2021-09-14/DescribeConnectorOperation.md "../../../goto/SdkForPHPV3/kafkaconnect-2021-09-14/DescribeConnectorOperation.md")
- [AWS SDK for Python](../../../goto/boto3/kafkaconnect-2021-09-14/DescribeConnectorOperation.md "../../../goto/boto3/kafkaconnect-2021-09-14/DescribeConnectorOperation.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/DescribeConnectorOperation.md "../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/DescribeConnectorOperation.md")

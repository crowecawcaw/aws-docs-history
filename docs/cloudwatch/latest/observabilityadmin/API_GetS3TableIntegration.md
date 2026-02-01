# GetS3TableIntegration

Retrieves information about a specific S3 Table integration, including its configuration,
status, and metadata.

## Request Syntax

```
POST /GetS3TableIntegration HTTP/1.1
Content-type: application/json

{
   "Arn": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[Arn](#API_GetS3TableIntegration_RequestSyntax "#API_GetS3TableIntegration_RequestSyntax")**

The Amazon Resource Name (ARN) of the S3 Table integration to retrieve.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "***string***",
   "CreatedTimeStamp": ***number***,
   "DestinationTableBucketArn": "***string***",
   "Encryption": {
      "KmsKeyArn": "***string***",
      "SseAlgorithm": "***string***"
   },
   "RoleArn": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Arn](#API_GetS3TableIntegration_ResponseSyntax "#API_GetS3TableIntegration_ResponseSyntax")**

The Amazon Resource Name (ARN) of the S3 Table integration.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`

**[CreatedTimeStamp](#API_GetS3TableIntegration_ResponseSyntax "#API_GetS3TableIntegration_ResponseSyntax")**

The timestamp when the S3 Table integration was created.

Type: Long

**[DestinationTableBucketArn](#API_GetS3TableIntegration_ResponseSyntax "#API_GetS3TableIntegration_ResponseSyntax")**

The Amazon Resource Name (ARN) of the S3 bucket used as the destination for the table
data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`

**[Encryption](#API_GetS3TableIntegration_ResponseSyntax "#API_GetS3TableIntegration_ResponseSyntax")**

The encryption configuration for the S3 Table integration.

Type: [Encryption](API_Encryption.md "API_Encryption.md") object

**[RoleArn](#API_GetS3TableIntegration_ResponseSyntax "#API_GetS3TableIntegration_ResponseSyntax")**

The Amazon Resource Name (ARN) of the IAM role used by the S3 Table integration.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`

**[Status](#API_GetS3TableIntegration_ResponseSyntax "#API_GetS3TableIntegration_ResponseSyntax")**

The current status of the S3 Table integration.

Type: String

Valid Values: `ACTIVE | DELETING`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

Indicates you don't have permissions to perform the requested operation. The user or role
that is making the request must have at least one IAM permissions policy attached that grants
the required permissions. For more information, see [Access management for AWS resources](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the
IAM user guide.

**amznErrorType**

The name of the exception.

HTTP Status Code: 400

**InternalServerException**

Indicates the request has failed to process because of an unknown server error,
exception, or failure.

**amznErrorType**

The name of the exception.

**retryAfterSeconds**

The number of seconds to wait before retrying the request.

HTTP Status Code: 500

**ResourceNotFoundException**

The specified resource (such as a telemetry rule) could not be found.

**ResourceId**

The identifier of the resource which could not be found.

**ResourceType**

The type of the resource which could not be found.

HTTP Status Code: 404

**TooManyRequestsException**

The request throughput limit was exceeded.

HTTP Status Code: 429

**ValidationException**

Indicates input validation failed. Check your request parameters and retry the request.

**Errors**

The errors in the input which caused the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/observabilityadmin-2018-05-10/GetS3TableIntegration.md "../../../goto/cli2/observabilityadmin-2018-05-10/GetS3TableIntegration.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/observabilityadmin-2018-05-10/GetS3TableIntegration.md "../../../goto/DotNetSDKV4/observabilityadmin-2018-05-10/GetS3TableIntegration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/GetS3TableIntegration.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/GetS3TableIntegration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/GetS3TableIntegration.md "../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/GetS3TableIntegration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/GetS3TableIntegration.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/GetS3TableIntegration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/GetS3TableIntegration.md "../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/GetS3TableIntegration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/GetS3TableIntegration.md "../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/GetS3TableIntegration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/GetS3TableIntegration.md "../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/GetS3TableIntegration.md")
- [AWS SDK for Python](../../../goto/boto3/observabilityadmin-2018-05-10/GetS3TableIntegration.md "../../../goto/boto3/observabilityadmin-2018-05-10/GetS3TableIntegration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/GetS3TableIntegration.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/GetS3TableIntegration.md")

# GetTelemetryEvaluationStatusForOrganization

This returns the onboarding status of the telemetry configuration feature for the
organization. It can only be called by a Management Account of an AWS Organization or an
assigned Delegated Admin Account of Amazon CloudWatch telemetry config.

## Request Syntax

```
POST /GetTelemetryEvaluationStatusForOrganization HTTP/1.1

```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "FailureReason": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[FailureReason](#API_GetTelemetryEvaluationStatusForOrganization_ResponseSyntax "#API_GetTelemetryEvaluationStatusForOrganization_ResponseSyntax")**

This field describes the reason for the failure status. The field will only be populated
if `Status` is `FAILED_START` or `FAILED_STOP`.

Type: String

**[Status](#API_GetTelemetryEvaluationStatusForOrganization_ResponseSyntax "#API_GetTelemetryEvaluationStatusForOrganization_ResponseSyntax")**

The onboarding status of the telemetry config feature for the organization.

Type: String

Valid Values: `NOT_STARTED | STARTING | FAILED_START | RUNNING | STOPPING | FAILED_STOP | STOPPED`

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

HTTP Status Code: 500

**TooManyRequestsException**

The request throughput limit was exceeded.

HTTP Status Code: 429

**ValidationException**

Indicates input validation failed. Check your request parameters and retry the request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md "../../../goto/cli2/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md "../../../goto/DotNetSDKV3/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md "../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md "../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md "../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md "../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md")
- [AWS SDK for Python](../../../goto/boto3/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md "../../../goto/boto3/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatusForOrganization.md")

# StartTelemetryEvaluationForOrganization

This actions begins onboarding the organization and all member accounts to the telemetry
config feature.

## Request Syntax

```
POST /StartTelemetryEvaluationForOrganization HTTP/1.1
Content-type: application/json

{
   "AllRegions": `boolean`,
   "Regions": [ "`string`" ]
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[AllRegions](#API_StartTelemetryEvaluationForOrganization_RequestSyntax "#API_StartTelemetryEvaluationForOrganization_RequestSyntax")**

If set to `true`, telemetry evaluation for the organization starts in all
AWS Regions where Amazon CloudWatch Observability Admin is available in the current partition. The
current region becomes the home region for managing multi-region evaluation for the
organization. When new regions become available, evaluation automatically expands to include
them. Mutually exclusive with `Regions`.

Type: Boolean

Required: No

**[Regions](#API_StartTelemetryEvaluationForOrganization_RequestSyntax "#API_StartTelemetryEvaluationForOrganization_RequestSyntax")**

An optional list of AWS Regions to include in multi-region telemetry evaluation for the
organization. The current region is always implicitly included and must not be specified in
this list. When provided, telemetry evaluation starts in the current region and propagates to
all specified regions for the organization. Mutually exclusive with `AllRegions`.
If neither `Regions` nor `AllRegions` is provided, the operation
applies only to the current region.

Type: Array of strings

Array Members: Minimum number of 1 item.

Length Constraints: Minimum length of 1.

Required: No

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md "CommonErrors.md").

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

- [AWS Command Line Interface V2](../../../goto/cli2/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md "../../../goto/cli2/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md "../../../goto/DotNetSDKV4/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md "../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md "../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md "../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md "../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md")
- [AWS SDK for Python](../../../goto/boto3/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md "../../../goto/boto3/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/StartTelemetryEvaluationForOrganization.md")

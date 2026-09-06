

# GetTelemetryEvaluationStatus
<a name="API_GetTelemetryEvaluationStatus"></a>

 Returns the current onboarding status of the telemetry config feature, including the status of the feature and reason the feature failed to start or stop. 

## Request Syntax
<a name="API_GetTelemetryEvaluationStatus_RequestSyntax"></a>

```
POST /GetTelemetryEvaluationStatus HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTelemetryEvaluationStatus_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetTelemetryEvaluationStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTelemetryEvaluationStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "FailureReason": "string",
   "HomeRegion": "string",
   "RegionStatuses": [ 
      { 
         "FailureReason": "string",
         "Region": "string",
         "RuleArn": "string",
         "Status": "string"
      }
   ],
   "Status": "string"
}
```

## Response Elements
<a name="API_GetTelemetryEvaluationStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailureReason](#API_GetTelemetryEvaluationStatus_ResponseSyntax) **   <a name="cwoa-GetTelemetryEvaluationStatus-response-FailureReason"></a>
 Describes the reason for the failure status. The field will only be populated if `Status` is `FAILED_START` or `FAILED_STOP`.   
Type: String

 ** [HomeRegion](#API_GetTelemetryEvaluationStatus_ResponseSyntax) **   <a name="cwoa-GetTelemetryEvaluationStatus-response-HomeRegion"></a>
 The AWS Region that is designated as the home region for multi-region telemetry evaluation. The home region is the single management point for all multi-region operations on this account. This field is only present when multi-region telemetry evaluation is active.   
Type: String  
Length Constraints: Minimum length of 1.

 ** [RegionStatuses](#API_GetTelemetryEvaluationStatus_ResponseSyntax) **   <a name="cwoa-GetTelemetryEvaluationStatus-response-RegionStatuses"></a>
 A list of per-region telemetry evaluation statuses. Each entry indicates the evaluation status for a specific spoke region included in the multi-region configuration. This field is only present when multi-region telemetry evaluation is active.   
Type: Array of [RegionStatus](API_RegionStatus.md) objects

 ** [Status](#API_GetTelemetryEvaluationStatus_ResponseSyntax) **   <a name="cwoa-GetTelemetryEvaluationStatus-response-Status"></a>
 The onboarding status of the telemetry config feature.   
Type: String  
Valid Values: `NOT_STARTED | STARTING | FAILED_START | RUNNING | STOPPING | FAILED_STOP | STOPPED` 

## Errors
<a name="API_GetTelemetryEvaluationStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
 Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access management for AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the IAM user guide.     
 ** amznErrorType **   
 The name of the exception. 
HTTP Status Code: 400

 ** InternalServerException **   
 Indicates the request has failed to process because of an unknown server error, exception, or failure.     
 ** amznErrorType **   
 The name of the exception.   
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** TooManyRequestsException **   
 The request throughput limit was exceeded.   
HTTP Status Code: 429

## See Also
<a name="API_GetTelemetryEvaluationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatus) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatus) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatus) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatus) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatus) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatus) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatus) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/GetTelemetryEvaluationStatus) 
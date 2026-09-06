

# UpdateTelemetryPipeline
<a name="API_UpdateTelemetryPipeline"></a>

Updates the configuration of an existing telemetry pipeline.

**Note**  
The following attributes cannot be updated after pipeline creation:  
 **Pipeline name** - The pipeline name is immutable
 **Pipeline ARN** - The ARN is automatically generated and cannot be changed
 **Source type** - Once a pipeline is created with a specific source type (such as S3, CloudWatch Logs, GitHub, or third-party sources), it cannot be changed to a different source type
Processors can be added, removed, or modified. However, some processors are not supported for third-party pipelines and cannot be added through updates.

 **Source-Specific Update Rules** 

CloudWatch Logs Sources (Vended and Custom)  
 **Updatable:** `sts_role_arn`   
 **Fixed:** `data_source_name`, `data_source_type`, sink (must remain `@original`)

S3 Sources (Crowdstrike, Zscaler, SentinelOne, Custom)  
 **Updatable:** All SQS configuration parameters, `sts_role_arn`, codec settings, compression type, bucket ownership settings, sink log group  
 **Fixed:** `notification_type`, `aws.region` 

GitHub Audit Logs  
 **Updatable:** All AWS Secrets Manager attributes, `scope` (can switch between ORGANIZATION/ENTERPRISE), `organization` or `enterprise` name, `range`, authentication credentials (PAT or GitHub App)

Microsoft Sources (Entra ID, Office365, Windows)  
 **Updatable:** All AWS Secrets Manager attributes, `tenant_id`, `workspace_id` (Windows only), OAuth2 credentials (`client_id`, `client_secret`)

Okta Sources (SSO, Auth0)  
 **Updatable:** All AWS Secrets Manager attributes, `domain`, `range`, OAuth2 credentials (`client_id`, `client_secret`)

Palo Alto Networks  
 **Updatable:** All AWS Secrets Manager attributes, `hostname`, basic authentication credentials (`username`, `password`)

ServiceNow CMDB  
 **Updatable:** All AWS Secrets Manager attributes, `instance_url`, `range`, OAuth2 credentials (`client_id`, `client_secret`)

Wiz CNAPP  
 **Updatable:** All AWS Secrets Manager attributes, `region`, `range`, OAuth2 credentials (`client_id`, `client_secret`)

## Request Syntax
<a name="API_UpdateTelemetryPipeline_RequestSyntax"></a>

```
POST /UpdateTelemetryPipeline HTTP/1.1
Content-type: application/json

{
   "Configuration": { 
      "Body": "{{string}}"
   },
   "PipelineIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateTelemetryPipeline_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateTelemetryPipeline_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Configuration](#API_UpdateTelemetryPipeline_RequestSyntax) **   <a name="cwoa-UpdateTelemetryPipeline-request-Configuration"></a>
The new configuration for the telemetry pipeline, including updated sources, processors, and destinations.  
Type: [TelemetryPipelineConfiguration](API_TelemetryPipelineConfiguration.md) object  
Required: Yes

 ** [PipelineIdentifier](#API_UpdateTelemetryPipeline_RequestSyntax) **   <a name="cwoa-UpdateTelemetryPipeline-request-PipelineIdentifier"></a>
The ARN of the telemetry pipeline to update.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Required: Yes

## Response Syntax
<a name="API_UpdateTelemetryPipeline_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateTelemetryPipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateTelemetryPipeline_Errors"></a>

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

 ** ResourceNotFoundException **   
 The specified resource (such as a telemetry rule) could not be found.     
 ** ResourceId **   
 The identifier of the resource which could not be found.   
 ** ResourceType **   
 The type of the resource which could not be found. 
HTTP Status Code: 404

 ** TooManyRequestsException **   
 The request throughput limit was exceeded.   
HTTP Status Code: 429

 ** ValidationException **   
 Indicates input validation failed. Check your request parameters and retry the request.     
 ** Errors **   
 The errors in the input which caused the exception. 
HTTP Status Code: 400

## See Also
<a name="API_UpdateTelemetryPipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/UpdateTelemetryPipeline) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/UpdateTelemetryPipeline) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/UpdateTelemetryPipeline) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/UpdateTelemetryPipeline) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/UpdateTelemetryPipeline) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/UpdateTelemetryPipeline) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/UpdateTelemetryPipeline) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/UpdateTelemetryPipeline) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/UpdateTelemetryPipeline) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/UpdateTelemetryPipeline) 
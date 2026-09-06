

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# ListInferenceExecutions
<a name="API_ListInferenceExecutions"></a>

 Lists all inference executions that have been performed by the specified inference scheduler. 

## Request Syntax
<a name="API_ListInferenceExecutions_RequestSyntax"></a>

```
{
   "DataEndTimeBefore": {{number}},
   "DataStartTimeAfter": {{number}},
   "InferenceSchedulerName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_ListInferenceExecutions_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DataEndTimeBefore](#API_ListInferenceExecutions_RequestSyntax) **   <a name="LookoutForEquipment-ListInferenceExecutions-request-DataEndTimeBefore"></a>
The time reference in the inferenced dataset before which Amazon Lookout for Equipment stopped the inference execution.   
Type: Timestamp  
Required: No

 ** [DataStartTimeAfter](#API_ListInferenceExecutions_RequestSyntax) **   <a name="LookoutForEquipment-ListInferenceExecutions-request-DataStartTimeAfter"></a>
The time reference in the inferenced dataset after which Amazon Lookout for Equipment started the inference execution.   
Type: Timestamp  
Required: No

 ** [InferenceSchedulerName](#API_ListInferenceExecutions_RequestSyntax) **   <a name="LookoutForEquipment-ListInferenceExecutions-request-InferenceSchedulerName"></a>
The name of the inference scheduler for the inference execution listed.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: Yes

 ** [MaxResults](#API_ListInferenceExecutions_RequestSyntax) **   <a name="LookoutForEquipment-ListInferenceExecutions-request-MaxResults"></a>
Specifies the maximum number of inference executions to list.   
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 500.  
Required: No

 ** [NextToken](#API_ListInferenceExecutions_RequestSyntax) **   <a name="LookoutForEquipment-ListInferenceExecutions-request-NextToken"></a>
An opaque pagination token indicating where to continue the listing of inference executions.  
Type: String  
Length Constraints: Maximum length of 8192.  
Pattern: `\p{ASCII}{0,8192}`   
Required: No

 ** [Status](#API_ListInferenceExecutions_RequestSyntax) **   <a name="LookoutForEquipment-ListInferenceExecutions-request-Status"></a>
The status of the inference execution.   
Type: String  
Valid Values: `IN_PROGRESS | SUCCESS | FAILED`   
Required: No

## Response Syntax
<a name="API_ListInferenceExecutions_ResponseSyntax"></a>

```
{
   "InferenceExecutionSummaries": [ 
      { 
         "CustomerResultObject": { 
            "Bucket": "string",
            "Key": "string"
         },
         "DataEndTime": number,
         "DataInputConfiguration": { 
            "InferenceInputNameConfiguration": { 
               "ComponentTimestampDelimiter": "string",
               "TimestampFormat": "string"
            },
            "InputTimeZoneOffset": "string",
            "S3InputConfiguration": { 
               "Bucket": "string",
               "Prefix": "string"
            }
         },
         "DataOutputConfiguration": { 
            "KmsKeyId": "string",
            "S3OutputConfiguration": { 
               "Bucket": "string",
               "Prefix": "string"
            }
         },
         "DataStartTime": number,
         "FailedReason": "string",
         "InferenceSchedulerArn": "string",
         "InferenceSchedulerName": "string",
         "ModelArn": "string",
         "ModelName": "string",
         "ModelVersion": number,
         "ModelVersionArn": "string",
         "ScheduledStartTime": number,
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListInferenceExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InferenceExecutionSummaries](#API_ListInferenceExecutions_ResponseSyntax) **   <a name="LookoutForEquipment-ListInferenceExecutions-response-InferenceExecutionSummaries"></a>
Provides an array of information about the individual inference executions returned from the `ListInferenceExecutions` operation, including model used, inference scheduler, data configuration, and so on.   
If you don't supply the `InferenceSchedulerName` request parameter, or if you supply the name of an inference scheduler that doesn't exist, `ListInferenceExecutions` returns an empty array in `InferenceExecutionSummaries`.
Type: Array of [InferenceExecutionSummary](API_InferenceExecutionSummary.md) objects

 ** [NextToken](#API_ListInferenceExecutions_ResponseSyntax) **   <a name="LookoutForEquipment-ListInferenceExecutions-response-NextToken"></a>
 An opaque pagination token indicating where to continue the listing of inference executions.   
Type: String  
Length Constraints: Maximum length of 8192.  
Pattern: `\p{ASCII}{0,8192}` 

## Errors
<a name="API_ListInferenceExecutions_Errors"></a>

 ** AccessDeniedException **   
The request could not be completed because you do not have access to the resource.   
HTTP Status Code: 400

 ** InternalServerException **   
 Processing of the request has failed because of an unknown error, exception or failure.   
HTTP Status Code: 500

 ** ResourceNotFoundException **   
 The resource requested could not be found. Verify the resource ID and retry your request.   
HTTP Status Code: 400

 ** ThrottlingException **   
The request was denied due to request throttling.  
HTTP Status Code: 400

 ** ValidationException **   
 The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related AWS service that's being utilized.   
HTTP Status Code: 400

## See Also
<a name="API_ListInferenceExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lookoutequipment-2020-12-15/ListInferenceExecutions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lookoutequipment-2020-12-15/ListInferenceExecutions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/ListInferenceExecutions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lookoutequipment-2020-12-15/ListInferenceExecutions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListInferenceExecutions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListInferenceExecutions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lookoutequipment-2020-12-15/ListInferenceExecutions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListInferenceExecutions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lookoutequipment-2020-12-15/ListInferenceExecutions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListInferenceExecutions) 


 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# ListRetrainingSchedulers
<a name="API_ListRetrainingSchedulers"></a>

Lists all retraining schedulers in your account, filtering by model name prefix and status. 

## Request Syntax
<a name="API_ListRetrainingSchedulers_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "ModelNameBeginsWith": "{{string}}",
   "NextToken": "{{string}}",
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRetrainingSchedulers_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListRetrainingSchedulers_RequestSyntax) **   <a name="LookoutForEquipment-ListRetrainingSchedulers-request-MaxResults"></a>
Specifies the maximum number of retraining schedulers to list.   
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 500.  
Required: No

 ** [ModelNameBeginsWith](#API_ListRetrainingSchedulers_RequestSyntax) **   <a name="LookoutForEquipment-ListRetrainingSchedulers-request-ModelNameBeginsWith"></a>
Specify this field to only list retraining schedulers whose machine learning models begin with the value you specify.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: No

 ** [NextToken](#API_ListRetrainingSchedulers_RequestSyntax) **   <a name="LookoutForEquipment-ListRetrainingSchedulers-request-NextToken"></a>
If the number of results exceeds the maximum, a pagination token is returned. Use the token in the request to show the next page of retraining schedulers.  
Type: String  
Length Constraints: Maximum length of 8192.  
Pattern: `\p{ASCII}{0,8192}`   
Required: No

 ** [Status](#API_ListRetrainingSchedulers_RequestSyntax) **   <a name="LookoutForEquipment-ListRetrainingSchedulers-request-Status"></a>
Specify this field to only list retraining schedulers whose status matches the value you specify.   
Type: String  
Valid Values: `PENDING | RUNNING | STOPPING | STOPPED`   
Required: No

## Response Syntax
<a name="API_ListRetrainingSchedulers_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RetrainingSchedulerSummaries": [ 
      { 
         "LookbackWindow": "string",
         "ModelArn": "string",
         "ModelName": "string",
         "RetrainingFrequency": "string",
         "RetrainingStartDate": number,
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRetrainingSchedulers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRetrainingSchedulers_ResponseSyntax) **   <a name="LookoutForEquipment-ListRetrainingSchedulers-response-NextToken"></a>
If the number of results exceeds the maximum, this pagination token is returned. Use this token in the request to show the next page of retraining schedulers.  
Type: String  
Length Constraints: Maximum length of 8192.  
Pattern: `\p{ASCII}{0,8192}` 

 ** [RetrainingSchedulerSummaries](#API_ListRetrainingSchedulers_ResponseSyntax) **   <a name="LookoutForEquipment-ListRetrainingSchedulers-response-RetrainingSchedulerSummaries"></a>
Provides information on the specified retraining scheduler, including the model name, model ARN, status, and start date.   
Type: Array of [RetrainingSchedulerSummary](API_RetrainingSchedulerSummary.md) objects

## Errors
<a name="API_ListRetrainingSchedulers_Errors"></a>

 ** AccessDeniedException **   
The request could not be completed because you do not have access to the resource.   
HTTP Status Code: 400

 ** InternalServerException **   
 Processing of the request has failed because of an unknown error, exception or failure.   
HTTP Status Code: 500

 ** ThrottlingException **   
The request was denied due to request throttling.  
HTTP Status Code: 400

 ** ValidationException **   
 The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related AWS service that's being utilized.   
HTTP Status Code: 400

## See Also
<a name="API_ListRetrainingSchedulers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lookoutequipment-2020-12-15/ListRetrainingSchedulers) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lookoutequipment-2020-12-15/ListRetrainingSchedulers) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/ListRetrainingSchedulers) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lookoutequipment-2020-12-15/ListRetrainingSchedulers) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListRetrainingSchedulers) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListRetrainingSchedulers) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lookoutequipment-2020-12-15/ListRetrainingSchedulers) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListRetrainingSchedulers) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lookoutequipment-2020-12-15/ListRetrainingSchedulers) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListRetrainingSchedulers) 


 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# ListModels
<a name="API_ListModels"></a>

Generates a list of all models in the account, including model name and ARN, dataset, and status. 

## Request Syntax
<a name="API_ListModels_RequestSyntax"></a>

```
{
   "DatasetNameBeginsWith": "{{string}}",
   "MaxResults": {{number}},
   "ModelNameBeginsWith": "{{string}}",
   "NextToken": "{{string}}",
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_ListModels_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DatasetNameBeginsWith](#API_ListModels_RequestSyntax) **   <a name="LookoutForEquipment-ListModels-request-DatasetNameBeginsWith"></a>
The beginning of the name of the dataset of the machine learning models to be listed.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: No

 ** [MaxResults](#API_ListModels_RequestSyntax) **   <a name="LookoutForEquipment-ListModels-request-MaxResults"></a>
 Specifies the maximum number of machine learning models to list.   
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 500.  
Required: No

 ** [ModelNameBeginsWith](#API_ListModels_RequestSyntax) **   <a name="LookoutForEquipment-ListModels-request-ModelNameBeginsWith"></a>
The beginning of the name of the machine learning models being listed.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: No

 ** [NextToken](#API_ListModels_RequestSyntax) **   <a name="LookoutForEquipment-ListModels-request-NextToken"></a>
 An opaque pagination token indicating where to continue the listing of machine learning models.   
Type: String  
Length Constraints: Maximum length of 8192.  
Pattern: `\p{ASCII}{0,8192}`   
Required: No

 ** [Status](#API_ListModels_RequestSyntax) **   <a name="LookoutForEquipment-ListModels-request-Status"></a>
The status of the machine learning model.   
Type: String  
Valid Values: `IN_PROGRESS | SUCCESS | FAILED | IMPORT_IN_PROGRESS`   
Required: No

## Response Syntax
<a name="API_ListModels_ResponseSyntax"></a>

```
{
   "ModelSummaries": [ 
      { 
         "ActiveModelVersion": number,
         "ActiveModelVersionArn": "string",
         "CreatedAt": number,
         "DatasetArn": "string",
         "DatasetName": "string",
         "LatestScheduledRetrainingModelVersion": number,
         "LatestScheduledRetrainingStartTime": number,
         "LatestScheduledRetrainingStatus": "string",
         "ModelArn": "string",
         "ModelDiagnosticsOutputConfiguration": { 
            "KmsKeyId": "string",
            "S3OutputConfiguration": { 
               "Bucket": "string",
               "Prefix": "string"
            }
         },
         "ModelName": "string",
         "ModelQuality": "string",
         "NextScheduledRetrainingStartDate": number,
         "RetrainingSchedulerStatus": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListModels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelSummaries](#API_ListModels_ResponseSyntax) **   <a name="LookoutForEquipment-ListModels-response-ModelSummaries"></a>
Provides information on the specified model, including created time, model and dataset ARNs, and status.   
Type: Array of [ModelSummary](API_ModelSummary.md) objects

 ** [NextToken](#API_ListModels_ResponseSyntax) **   <a name="LookoutForEquipment-ListModels-response-NextToken"></a>
 An opaque pagination token indicating where to continue the listing of machine learning models.   
Type: String  
Length Constraints: Maximum length of 8192.  
Pattern: `\p{ASCII}{0,8192}` 

## Errors
<a name="API_ListModels_Errors"></a>

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
<a name="API_ListModels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lookoutequipment-2020-12-15/ListModels) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lookoutequipment-2020-12-15/ListModels) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/ListModels) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lookoutequipment-2020-12-15/ListModels) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListModels) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListModels) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lookoutequipment-2020-12-15/ListModels) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListModels) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lookoutequipment-2020-12-15/ListModels) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListModels) 
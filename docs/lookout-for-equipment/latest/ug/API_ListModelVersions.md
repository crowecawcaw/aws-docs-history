

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# ListModelVersions
<a name="API_ListModelVersions"></a>

Generates a list of all model versions for a given model, including the model version, model version ARN, and status. To list a subset of versions, use the `MaxModelVersion` and `MinModelVersion` fields.

## Request Syntax
<a name="API_ListModelVersions_RequestSyntax"></a>

```
{
   "CreatedAtEndTime": {{number}},
   "CreatedAtStartTime": {{number}},
   "MaxModelVersion": {{number}},
   "MaxResults": {{number}},
   "MinModelVersion": {{number}},
   "ModelName": "{{string}}",
   "NextToken": "{{string}}",
   "SourceType": "{{string}}",
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_ListModelVersions_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [CreatedAtEndTime](#API_ListModelVersions_RequestSyntax) **   <a name="LookoutForEquipment-ListModelVersions-request-CreatedAtEndTime"></a>
Filter results to return all the model versions created before this time.  
Type: Timestamp  
Required: No

 ** [CreatedAtStartTime](#API_ListModelVersions_RequestSyntax) **   <a name="LookoutForEquipment-ListModelVersions-request-CreatedAtStartTime"></a>
Filter results to return all the model versions created after this time.  
Type: Timestamp  
Required: No

 ** [MaxModelVersion](#API_ListModelVersions_RequestSyntax) **   <a name="LookoutForEquipment-ListModelVersions-request-MaxModelVersion"></a>
Specifies the highest version of the model to return in the list.  
Type: Long  
Valid Range: Minimum value of 1.  
Required: No

 ** [MaxResults](#API_ListModelVersions_RequestSyntax) **   <a name="LookoutForEquipment-ListModelVersions-request-MaxResults"></a>
Specifies the maximum number of machine learning model versions to list.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 500.  
Required: No

 ** [MinModelVersion](#API_ListModelVersions_RequestSyntax) **   <a name="LookoutForEquipment-ListModelVersions-request-MinModelVersion"></a>
Specifies the lowest version of the model to return in the list.  
Type: Long  
Valid Range: Minimum value of 1.  
Required: No

 ** [ModelName](#API_ListModelVersions_RequestSyntax) **   <a name="LookoutForEquipment-ListModelVersions-request-ModelName"></a>
Then name of the machine learning model for which the model versions are to be listed.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: Yes

 ** [NextToken](#API_ListModelVersions_RequestSyntax) **   <a name="LookoutForEquipment-ListModelVersions-request-NextToken"></a>
If the total number of results exceeds the limit that the response can display, the response returns an opaque pagination token indicating where to continue the listing of machine learning model versions. Use this token in the `NextToken` field in the request to list the next page of results.  
Type: String  
Length Constraints: Maximum length of 8192.  
Pattern: `\p{ASCII}{0,8192}`   
Required: No

 ** [SourceType](#API_ListModelVersions_RequestSyntax) **   <a name="LookoutForEquipment-ListModelVersions-request-SourceType"></a>
Filter the results based on the way the model version was generated.  
Type: String  
Valid Values: `TRAINING | RETRAINING | IMPORT`   
Required: No

 ** [Status](#API_ListModelVersions_RequestSyntax) **   <a name="LookoutForEquipment-ListModelVersions-request-Status"></a>
Filter the results based on the current status of the model version.  
Type: String  
Valid Values: `IN_PROGRESS | SUCCESS | FAILED | IMPORT_IN_PROGRESS | CANCELED`   
Required: No

## Response Syntax
<a name="API_ListModelVersions_ResponseSyntax"></a>

```
{
   "ModelVersionSummaries": [ 
      { 
         "CreatedAt": number,
         "ModelArn": "string",
         "ModelName": "string",
         "ModelQuality": "string",
         "ModelVersion": number,
         "ModelVersionArn": "string",
         "SourceType": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListModelVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelVersionSummaries](#API_ListModelVersions_ResponseSyntax) **   <a name="LookoutForEquipment-ListModelVersions-response-ModelVersionSummaries"></a>
Provides information on the specified model version, including the created time, model and dataset ARNs, and status.  
If you don't supply the `ModelName` request parameter, or if you supply the name of a model that doesn't exist, `ListModelVersions` returns an empty array in `ModelVersionSummaries`. 
Type: Array of [ModelVersionSummary](API_ModelVersionSummary.md) objects

 ** [NextToken](#API_ListModelVersions_ResponseSyntax) **   <a name="LookoutForEquipment-ListModelVersions-response-NextToken"></a>
If the total number of results exceeds the limit that the response can display, the response returns an opaque pagination token indicating where to continue the listing of machine learning model versions. Use this token in the `NextToken` field in the request to list the next page of results.  
Type: String  
Length Constraints: Maximum length of 8192.  
Pattern: `\p{ASCII}{0,8192}` 

## Errors
<a name="API_ListModelVersions_Errors"></a>

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
<a name="API_ListModelVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lookoutequipment-2020-12-15/ListModelVersions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lookoutequipment-2020-12-15/ListModelVersions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/ListModelVersions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lookoutequipment-2020-12-15/ListModelVersions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListModelVersions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListModelVersions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lookoutequipment-2020-12-15/ListModelVersions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListModelVersions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lookoutequipment-2020-12-15/ListModelVersions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListModelVersions) 
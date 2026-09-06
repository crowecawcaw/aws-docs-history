

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# ListDatasets
<a name="API_ListDatasets"></a>

Lists all datasets currently available in your account, filtering on the dataset name. 

## Request Syntax
<a name="API_ListDatasets_RequestSyntax"></a>

```
{
   "DatasetNameBeginsWith": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDatasets_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DatasetNameBeginsWith](#API_ListDatasets_RequestSyntax) **   <a name="LookoutForEquipment-ListDatasets-request-DatasetNameBeginsWith"></a>
The beginning of the name of the datasets to be listed.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: No

 ** [MaxResults](#API_ListDatasets_RequestSyntax) **   <a name="LookoutForEquipment-ListDatasets-request-MaxResults"></a>
 Specifies the maximum number of datasets to list.   
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 500.  
Required: No

 ** [NextToken](#API_ListDatasets_RequestSyntax) **   <a name="LookoutForEquipment-ListDatasets-request-NextToken"></a>
 An opaque pagination token indicating where to continue the listing of datasets.   
Type: String  
Length Constraints: Maximum length of 8192.  
Pattern: `\p{ASCII}{0,8192}`   
Required: No

## Response Syntax
<a name="API_ListDatasets_ResponseSyntax"></a>

```
{
   "DatasetSummaries": [ 
      { 
         "CreatedAt": number,
         "DatasetArn": "string",
         "DatasetName": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDatasets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DatasetSummaries](#API_ListDatasets_ResponseSyntax) **   <a name="LookoutForEquipment-ListDatasets-response-DatasetSummaries"></a>
Provides information about the specified dataset, including creation time, dataset ARN, and status.   
Type: Array of [DatasetSummary](API_DatasetSummary.md) objects

 ** [NextToken](#API_ListDatasets_ResponseSyntax) **   <a name="LookoutForEquipment-ListDatasets-response-NextToken"></a>
 An opaque pagination token indicating where to continue the listing of datasets.   
Type: String  
Length Constraints: Maximum length of 8192.  
Pattern: `\p{ASCII}{0,8192}` 

## Errors
<a name="API_ListDatasets_Errors"></a>

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
<a name="API_ListDatasets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lookoutequipment-2020-12-15/ListDatasets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lookoutequipment-2020-12-15/ListDatasets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/ListDatasets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lookoutequipment-2020-12-15/ListDatasets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListDatasets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListDatasets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lookoutequipment-2020-12-15/ListDatasets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListDatasets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lookoutequipment-2020-12-15/ListDatasets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListDatasets) 
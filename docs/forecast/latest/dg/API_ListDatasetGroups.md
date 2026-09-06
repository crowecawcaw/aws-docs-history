

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# ListDatasetGroups
<a name="API_ListDatasetGroups"></a>

Returns a list of dataset groups created using the [CreateDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html) operation. For each dataset group, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). You can retrieve the complete set of properties by using the dataset group ARN with the [DescribeDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetGroup.html) operation.

**Important**  
Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/) 

## Request Syntax
<a name="API_ListDatasetGroups_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDatasetGroups_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListDatasetGroups_RequestSyntax) **   <a name="forecast-ListDatasetGroups-request-MaxResults"></a>
The number of items to return in the response.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListDatasetGroups_RequestSyntax) **   <a name="forecast-ListDatasetGroups-request-NextToken"></a>
If the result of the previous request was truncated, the response includes a `NextToken`. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 3000.  
Pattern: `.+`   
Required: No

## Response Syntax
<a name="API_ListDatasetGroups_ResponseSyntax"></a>

```
{
   "DatasetGroups": [ 
      { 
         "CreationTime": number,
         "DatasetGroupArn": "string",
         "DatasetGroupName": "string",
         "LastModificationTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDatasetGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DatasetGroups](#API_ListDatasetGroups_ResponseSyntax) **   <a name="forecast-ListDatasetGroups-response-DatasetGroups"></a>
An array of objects that summarize each dataset group's properties.  
Type: Array of [DatasetGroupSummary](API_DatasetGroupSummary.md) objects

 ** [NextToken](#API_ListDatasetGroups_ResponseSyntax) **   <a name="forecast-ListDatasetGroups-response-NextToken"></a>
If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of results, use the token in the next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 3000.  
Pattern: `.+` 

## Errors
<a name="API_ListDatasetGroups_Errors"></a>

 ** InvalidNextTokenException **   
The token is not valid. Tokens expire after 24 hours.  
HTTP Status Code: 400

## See Also
<a name="API_ListDatasetGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecast-2018-06-26/ListDatasetGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecast-2018-06-26/ListDatasetGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/ListDatasetGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecast-2018-06-26/ListDatasetGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/ListDatasetGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecast-2018-06-26/ListDatasetGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecast-2018-06-26/ListDatasetGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecast-2018-06-26/ListDatasetGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecast-2018-06-26/ListDatasetGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/ListDatasetGroups) 
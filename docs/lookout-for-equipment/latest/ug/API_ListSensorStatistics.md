

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# ListSensorStatistics
<a name="API_ListSensorStatistics"></a>

 Lists statistics about the data collected for each of the sensors that have been successfully ingested in the particular dataset. Can also be used to retreive Sensor Statistics for a previous ingestion job. 

## Request Syntax
<a name="API_ListSensorStatistics_RequestSyntax"></a>

```
{
   "DatasetName": "{{string}}",
   "IngestionJobId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSensorStatistics_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DatasetName](#API_ListSensorStatistics_RequestSyntax) **   <a name="LookoutForEquipment-ListSensorStatistics-request-DatasetName"></a>
 The name of the dataset associated with the list of Sensor Statistics.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: Yes

 ** [IngestionJobId](#API_ListSensorStatistics_RequestSyntax) **   <a name="LookoutForEquipment-ListSensorStatistics-request-IngestionJobId"></a>
 The ingestion job id associated with the list of Sensor Statistics. To get sensor statistics for a particular ingestion job id, both dataset name and ingestion job id must be submitted as inputs.   
Type: String  
Length Constraints: Maximum length of 32.  
Pattern: `[A-Fa-f0-9]{0,32}`   
Required: No

 ** [MaxResults](#API_ListSensorStatistics_RequestSyntax) **   <a name="LookoutForEquipment-ListSensorStatistics-request-MaxResults"></a>
Specifies the maximum number of sensors for which to retrieve statistics.   
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 500.  
Required: No

 ** [NextToken](#API_ListSensorStatistics_RequestSyntax) **   <a name="LookoutForEquipment-ListSensorStatistics-request-NextToken"></a>
An opaque pagination token indicating where to continue the listing of sensor statistics.   
Type: String  
Length Constraints: Maximum length of 8192.  
Pattern: `\p{ASCII}{0,8192}`   
Required: No

## Response Syntax
<a name="API_ListSensorStatistics_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SensorStatisticsSummaries": [ 
      { 
         "CategoricalValues": { 
            "NumberOfCategory": number,
            "Status": "string"
         },
         "ComponentName": "string",
         "DataEndTime": number,
         "DataExists": boolean,
         "DataStartTime": number,
         "DuplicateTimestamps": { 
            "Count": number,
            "Percentage": number
         },
         "InvalidDateEntries": { 
            "Count": number,
            "Percentage": number
         },
         "InvalidValues": { 
            "Count": number,
            "Percentage": number
         },
         "LargeTimestampGaps": { 
            "MaxTimestampGapInDays": number,
            "NumberOfLargeTimestampGaps": number,
            "Status": "string"
         },
         "MissingValues": { 
            "Count": number,
            "Percentage": number
         },
         "MonotonicValues": { 
            "Monotonicity": "string",
            "Status": "string"
         },
         "MultipleOperatingModes": { 
            "Status": "string"
         },
         "SensorName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSensorStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSensorStatistics_ResponseSyntax) **   <a name="LookoutForEquipment-ListSensorStatistics-response-NextToken"></a>
An opaque pagination token indicating where to continue the listing of sensor statistics.   
Type: String  
Length Constraints: Maximum length of 8192.  
Pattern: `\p{ASCII}{0,8192}` 

 ** [SensorStatisticsSummaries](#API_ListSensorStatistics_ResponseSyntax) **   <a name="LookoutForEquipment-ListSensorStatistics-response-SensorStatisticsSummaries"></a>
Provides ingestion-based statistics regarding the specified sensor with respect to various validation types, such as whether data exists, the number and percentage of missing values, and the number and percentage of duplicate timestamps.   
Type: Array of [SensorStatisticsSummary](API_SensorStatisticsSummary.md) objects

## Errors
<a name="API_ListSensorStatistics_Errors"></a>

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
<a name="API_ListSensorStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lookoutequipment-2020-12-15/ListSensorStatistics) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lookoutequipment-2020-12-15/ListSensorStatistics) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/ListSensorStatistics) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lookoutequipment-2020-12-15/ListSensorStatistics) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListSensorStatistics) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListSensorStatistics) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lookoutequipment-2020-12-15/ListSensorStatistics) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListSensorStatistics) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lookoutequipment-2020-12-15/ListSensorStatistics) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListSensorStatistics) 
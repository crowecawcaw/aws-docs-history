

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# DescribeDataIngestionJob
<a name="API_DescribeDataIngestionJob"></a>

Provides information on a specific data ingestion job such as creation time, dataset ARN, and status.

## Request Syntax
<a name="API_DescribeDataIngestionJob_RequestSyntax"></a>

```
{
   "JobId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDataIngestionJob_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [JobId](#API_DescribeDataIngestionJob_RequestSyntax) **   <a name="LookoutForEquipment-DescribeDataIngestionJob-request-JobId"></a>
The job ID of the data ingestion job.   
Type: String  
Length Constraints: Maximum length of 32.  
Pattern: `[A-Fa-f0-9]{0,32}`   
Required: Yes

## Response Syntax
<a name="API_DescribeDataIngestionJob_ResponseSyntax"></a>

```
{
   "CreatedAt": number,
   "DataEndTime": number,
   "DataQualitySummary": { 
      "DuplicateTimestamps": { 
         "TotalNumberOfDuplicateTimestamps": number
      },
      "InsufficientSensorData": { 
         "MissingCompleteSensorData": { 
            "AffectedSensorCount": number
         },
         "SensorsWithShortDateRange": { 
            "AffectedSensorCount": number
         }
      },
      "InvalidSensorData": { 
         "AffectedSensorCount": number,
         "TotalNumberOfInvalidValues": number
      },
      "MissingSensorData": { 
         "AffectedSensorCount": number,
         "TotalNumberOfMissingValues": number
      },
      "UnsupportedTimestamps": { 
         "TotalNumberOfUnsupportedTimestamps": number
      }
   },
   "DatasetArn": "string",
   "DataStartTime": number,
   "FailedReason": "string",
   "IngestedDataSize": number,
   "IngestedFilesSummary": { 
      "DiscardedFiles": [ 
         { 
            "Bucket": "string",
            "Key": "string"
         }
      ],
      "IngestedNumberOfFiles": number,
      "TotalNumberOfFiles": number
   },
   "IngestionInputConfiguration": { 
      "S3InputConfiguration": { 
         "Bucket": "string",
         "KeyPattern": "string",
         "Prefix": "string"
      }
   },
   "JobId": "string",
   "RoleArn": "string",
   "SourceDatasetArn": "string",
   "Status": "string",
   "StatusDetail": "string"
}
```

## Response Elements
<a name="API_DescribeDataIngestionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_DescribeDataIngestionJob_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataIngestionJob-response-CreatedAt"></a>
The time at which the data ingestion job was created.   
Type: Timestamp

 ** [DataEndTime](#API_DescribeDataIngestionJob_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataIngestionJob-response-DataEndTime"></a>
 Indicates the latest timestamp corresponding to data that was successfully ingested during this specific ingestion job.   
Type: Timestamp

 ** [DataQualitySummary](#API_DescribeDataIngestionJob_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataIngestionJob-response-DataQualitySummary"></a>
 Gives statistics about a completed ingestion job. These statistics primarily relate to quantifying incorrect data such as MissingCompleteSensorData, MissingSensorData, UnsupportedDateFormats, InsufficientSensorData, and DuplicateTimeStamps.   
Type: [DataQualitySummary](API_DataQualitySummary.md) object

 ** [DatasetArn](#API_DescribeDataIngestionJob_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataIngestionJob-response-DatasetArn"></a>
The Amazon Resource Name (ARN) of the dataset being used in the data ingestion job.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:dataset\/[0-9a-zA-Z_-]{1,200}\/.+` 

 ** [DataStartTime](#API_DescribeDataIngestionJob_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataIngestionJob-response-DataStartTime"></a>
 Indicates the earliest timestamp corresponding to data that was successfully ingested during this specific ingestion job.   
Type: Timestamp

 ** [FailedReason](#API_DescribeDataIngestionJob_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataIngestionJob-response-FailedReason"></a>
Specifies the reason for failure when a data ingestion job has failed.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5000.  
Pattern: `[\P{M}\p{M}]{1,5000}` 

 ** [IngestedDataSize](#API_DescribeDataIngestionJob_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataIngestionJob-response-IngestedDataSize"></a>
 Indicates the size of the ingested dataset.   
Type: Long  
Valid Range: Minimum value of 0.

 ** [IngestedFilesSummary](#API_DescribeDataIngestionJob_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataIngestionJob-response-IngestedFilesSummary"></a>
Gives statistics about how many files have been ingested, and which files have not been ingested, for a particular ingestion job.  
Type: [IngestedFilesSummary](API_IngestedFilesSummary.md) object

 ** [IngestionInputConfiguration](#API_DescribeDataIngestionJob_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataIngestionJob-response-IngestionInputConfiguration"></a>
Specifies the S3 location configuration for the data input for the data ingestion job.   
Type: [IngestionInputConfiguration](API_IngestionInputConfiguration.md) object

 ** [JobId](#API_DescribeDataIngestionJob_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataIngestionJob-response-JobId"></a>
Indicates the job ID of the data ingestion job.   
Type: String  
Length Constraints: Maximum length of 32.  
Pattern: `[A-Fa-f0-9]{0,32}` 

 ** [RoleArn](#API_DescribeDataIngestionJob_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataIngestionJob-response-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role with permission to access the data source being ingested.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+` 

 ** [SourceDatasetArn](#API_DescribeDataIngestionJob_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataIngestionJob-response-SourceDatasetArn"></a>
The Amazon Resource Name (ARN) of the source dataset from which the data used for the data ingestion job was imported from.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:dataset\/[0-9a-zA-Z_-]{1,200}\/.+` 

 ** [Status](#API_DescribeDataIngestionJob_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataIngestionJob-response-Status"></a>
Indicates the status of the `DataIngestionJob` operation.   
Type: String  
Valid Values: `IN_PROGRESS | SUCCESS | FAILED | IMPORT_IN_PROGRESS` 

 ** [StatusDetail](#API_DescribeDataIngestionJob_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataIngestionJob-response-StatusDetail"></a>
 Provides details about status of the ingestion job that is currently in progress.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5000.  
Pattern: `[\P{M}\p{M}]{1,5000}` 

## Errors
<a name="API_DescribeDataIngestionJob_Errors"></a>

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
<a name="API_DescribeDataIngestionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lookoutequipment-2020-12-15/DescribeDataIngestionJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lookoutequipment-2020-12-15/DescribeDataIngestionJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/DescribeDataIngestionJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lookoutequipment-2020-12-15/DescribeDataIngestionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/DescribeDataIngestionJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DescribeDataIngestionJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lookoutequipment-2020-12-15/DescribeDataIngestionJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lookoutequipment-2020-12-15/DescribeDataIngestionJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lookoutequipment-2020-12-15/DescribeDataIngestionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/DescribeDataIngestionJob) 


 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# DescribeDataset
<a name="API_DescribeDataset"></a>

Provides a JSON description of the data in each time series dataset, including names, column names, and data types.

## Request Syntax
<a name="API_DescribeDataset_RequestSyntax"></a>

```
{
   "DatasetName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDataset_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DatasetName](#API_DescribeDataset_RequestSyntax) **   <a name="LookoutForEquipment-DescribeDataset-request-DatasetName"></a>
The name of the dataset to be described.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: Yes

## Response Syntax
<a name="API_DescribeDataset_ResponseSyntax"></a>

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
   "DatasetName": "string",
   "DataStartTime": number,
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
   "LastUpdatedAt": number,
   "RoleArn": "string",
   "Schema": "string",
   "ServerSideKmsKeyId": "string",
   "SourceDatasetArn": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_DescribeDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_DescribeDataset_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataset-response-CreatedAt"></a>
Specifies the time the dataset was created in Lookout for Equipment.   
Type: Timestamp

 ** [DataEndTime](#API_DescribeDataset_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataset-response-DataEndTime"></a>
 Indicates the latest timestamp corresponding to data that was successfully ingested during the most recent ingestion of this particular dataset.   
Type: Timestamp

 ** [DataQualitySummary](#API_DescribeDataset_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataset-response-DataQualitySummary"></a>
 Gives statistics associated with the given dataset for the latest successful associated ingestion job id. These statistics primarily relate to quantifying incorrect data such as MissingCompleteSensorData, MissingSensorData, UnsupportedDateFormats, InsufficientSensorData, and DuplicateTimeStamps.   
Type: [DataQualitySummary](API_DataQualitySummary.md) object

 ** [DatasetArn](#API_DescribeDataset_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataset-response-DatasetArn"></a>
The Amazon Resource Name (ARN) of the dataset being described.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:dataset\/[0-9a-zA-Z_-]{1,200}\/.+` 

 ** [DatasetName](#API_DescribeDataset_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataset-response-DatasetName"></a>
The name of the dataset being described.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$` 

 ** [DataStartTime](#API_DescribeDataset_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataset-response-DataStartTime"></a>
 Indicates the earliest timestamp corresponding to data that was successfully ingested during the most recent ingestion of this particular dataset.   
Type: Timestamp

 ** [IngestedFilesSummary](#API_DescribeDataset_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataset-response-IngestedFilesSummary"></a>
IngestedFilesSummary associated with the given dataset for the latest successful associated ingestion job id.   
Type: [IngestedFilesSummary](API_IngestedFilesSummary.md) object

 ** [IngestionInputConfiguration](#API_DescribeDataset_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataset-response-IngestionInputConfiguration"></a>
Specifies the S3 location configuration for the data input for the data ingestion job.   
Type: [IngestionInputConfiguration](API_IngestionInputConfiguration.md) object

 ** [LastUpdatedAt](#API_DescribeDataset_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataset-response-LastUpdatedAt"></a>
Specifies the time the dataset was last updated, if it was.   
Type: Timestamp

 ** [RoleArn](#API_DescribeDataset_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataset-response-RoleArn"></a>
 The Amazon Resource Name (ARN) of the IAM role that you are using for this the data ingestion job.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+` 

 ** [Schema](#API_DescribeDataset_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataset-response-Schema"></a>
A JSON description of the data that is in each time series dataset, including names, column names, and data types.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000000.

 ** [ServerSideKmsKeyId](#API_DescribeDataset_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataset-response-ServerSideKmsKeyId"></a>
Provides the identifier of the AWS KMS key used to encrypt dataset data by Amazon Lookout for Equipment.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `arn:aws[a-z\-]*:kms:[a-z0-9\-]*:\d{12}:[\w\-\/]+` 

 ** [SourceDatasetArn](#API_DescribeDataset_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataset-response-SourceDatasetArn"></a>
The Amazon Resource Name (ARN) of the source dataset from which the current data being described was imported from.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:dataset\/[0-9a-zA-Z_-]{1,200}\/.+` 

 ** [Status](#API_DescribeDataset_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeDataset-response-Status"></a>
Indicates the status of the dataset.   
Type: String  
Valid Values: `CREATED | INGESTION_IN_PROGRESS | ACTIVE | IMPORT_IN_PROGRESS` 

## Errors
<a name="API_DescribeDataset_Errors"></a>

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
<a name="API_DescribeDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lookoutequipment-2020-12-15/DescribeDataset) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lookoutequipment-2020-12-15/DescribeDataset) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/DescribeDataset) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lookoutequipment-2020-12-15/DescribeDataset) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/DescribeDataset) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DescribeDataset) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lookoutequipment-2020-12-15/DescribeDataset) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lookoutequipment-2020-12-15/DescribeDataset) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lookoutequipment-2020-12-15/DescribeDataset) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/DescribeDataset) 
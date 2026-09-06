

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# CreateDatasetImportJob
<a name="API_CreateDatasetImportJob"></a>

Imports your training data to an Amazon Forecast dataset. You provide the location of your training data in an Amazon Simple Storage Service (Amazon S3) bucket and the Amazon Resource Name (ARN) of the dataset that you want to import the data to.

**Important**  
Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/) 

You must specify a [DataSource](https://docs.aws.amazon.com/forecast/latest/dg/API_DataSource.html) object that includes an AWS Identity and Access Management (IAM) role that Amazon Forecast can assume to access the data, as Amazon Forecast makes a copy of your data and processes it in an internal AWS system. For more information, see [Set up permissions](https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-iam-roles.html).

The training data must be in CSV or Parquet format. The delimiter must be a comma (,).

You can specify the path to a specific file, the S3 bucket, or to a folder in the S3 bucket. For the latter two cases, Amazon Forecast imports all files up to the limit of 10,000 files.

Because dataset imports are not aggregated, your most recent dataset import is the one that is used when training a predictor or generating a forecast. Make sure that your most recent dataset import contains all of the data you want to model off of, and not just the new data collected since the previous import.

To get a list of all your dataset import jobs, filtered by specified criteria, use the [ListDatasetImportJobs](https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasetImportJobs.html) operation.

## Request Syntax
<a name="API_CreateDatasetImportJob_RequestSyntax"></a>

```
{
   "DatasetArn": "{{string}}",
   "DatasetImportJobName": "{{string}}",
   "DataSource": { 
      "S3Config": { 
         "KMSKeyArn": "{{string}}",
         "Path": "{{string}}",
         "RoleArn": "{{string}}"
      }
   },
   "Format": "{{string}}",
   "GeolocationFormat": "{{string}}",
   "ImportMode": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TimestampFormat": "{{string}}",
   "TimeZone": "{{string}}",
   "UseGeolocationForTimeZone": {{boolean}}
}
```

## Request Parameters
<a name="API_CreateDatasetImportJob_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DatasetArn](#API_CreateDatasetImportJob_RequestSyntax) **   <a name="forecast-CreateDatasetImportJob-request-DatasetArn"></a>
The Amazon Resource Name (ARN) of the Amazon Forecast dataset that you want to import data to.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: Yes

 ** [DatasetImportJobName](#API_CreateDatasetImportJob_RequestSyntax) **   <a name="forecast-CreateDatasetImportJob-request-DatasetImportJobName"></a>
The name for the dataset import job. We recommend including the current timestamp in the name, for example, `20190721DatasetImport`. This can help you avoid getting a `ResourceAlreadyExistsException` exception.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`   
Required: Yes

 ** [DataSource](#API_CreateDatasetImportJob_RequestSyntax) **   <a name="forecast-CreateDatasetImportJob-request-DataSource"></a>
The location of the training data to import and an AWS Identity and Access Management (IAM) role that Amazon Forecast can assume to access the data. The training data must be stored in an Amazon S3 bucket.  
If encryption is used, `DataSource` must include an AWS Key Management Service (KMS) key and the IAM role must allow Amazon Forecast permission to access the key. The KMS key and IAM role must match those specified in the `EncryptionConfig` parameter of the [CreateDataset](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html) operation.  
Type: [DataSource](API_DataSource.md) object  
Required: Yes

 ** [Format](#API_CreateDatasetImportJob_RequestSyntax) **   <a name="forecast-CreateDatasetImportJob-request-Format"></a>
The format of the imported data, CSV or PARQUET. The default value is CSV.  
Type: String  
Length Constraints: Maximum length of 7.  
Pattern: `^CSV|PARQUET$`   
Required: No

 ** [GeolocationFormat](#API_CreateDatasetImportJob_RequestSyntax) **   <a name="forecast-CreateDatasetImportJob-request-GeolocationFormat"></a>
The format of the geolocation attribute. The geolocation attribute can be formatted in one of two ways:  
+  `LAT_LONG` - the latitude and longitude in decimal format (Example: 47.61\_-122.33).
+  `CC_POSTALCODE` (US Only) - the country code (US), followed by the 5-digit ZIP code (Example: US\_98121).
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `^[a-zA-Z0-9_]+$`   
Required: No

 ** [ImportMode](#API_CreateDatasetImportJob_RequestSyntax) **   <a name="forecast-CreateDatasetImportJob-request-ImportMode"></a>
Specifies whether the dataset import job is a `FULL` or `INCREMENTAL` import. A `FULL` dataset import replaces all of the existing data with the newly imported data. An `INCREMENTAL` import appends the imported data to the existing data.  
Type: String  
Valid Values: `FULL | INCREMENTAL`   
Required: No

 ** [Tags](#API_CreateDatasetImportJob_RequestSyntax) **   <a name="forecast-CreateDatasetImportJob-request-Tags"></a>
The optional metadata that you apply to the dataset import job to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.  
The following basic restrictions apply to tags:  
+ Maximum number of tags per resource - 50.
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8.
+ Maximum value length - 256 Unicode characters in UTF-8.
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has `aws` as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of `aws` do not count against your tags per resource limit.
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

 ** [TimestampFormat](#API_CreateDatasetImportJob_RequestSyntax) **   <a name="forecast-CreateDatasetImportJob-request-TimestampFormat"></a>
The format of timestamps in the dataset. The format that you specify depends on the `DataFrequency` specified when the dataset was created. The following formats are supported  
+ "yyyy-MM-dd"

  For the following data frequencies: Y, M, W, and D
+ "yyyy-MM-dd HH:mm:ss"

  For the following data frequencies: H, 30min, 15min, and 1min; and optionally, for: Y, M, W, and D
If the format isn't specified, Amazon Forecast expects the format to be "yyyy-MM-dd HH:mm:ss".  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `^[a-zA-Z0-9\-\:\.\,\'\s]+$`   
Required: No

 ** [TimeZone](#API_CreateDatasetImportJob_RequestSyntax) **   <a name="forecast-CreateDatasetImportJob-request-TimeZone"></a>
A single time zone for every item in your dataset. This option is ideal for datasets with all timestamps within a single time zone, or if all timestamps are normalized to a single time zone.   
Refer to the [Joda-Time API](http://joda-time.sourceforge.net/timezones.html) for a complete list of valid time zone names.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `^[a-zA-Z0-9\/\+\-\_]+$`   
Required: No

 ** [UseGeolocationForTimeZone](#API_CreateDatasetImportJob_RequestSyntax) **   <a name="forecast-CreateDatasetImportJob-request-UseGeolocationForTimeZone"></a>
Automatically derive time zone information from the geolocation attribute. This option is ideal for datasets that contain timestamps in multiple time zones and those timestamps are expressed in local time.  
Type: Boolean  
Required: No

## Response Syntax
<a name="API_CreateDatasetImportJob_ResponseSyntax"></a>

```
{
   "DatasetImportJobArn": "string"
}
```

## Response Elements
<a name="API_CreateDatasetImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DatasetImportJobArn](#API_CreateDatasetImportJob_ResponseSyntax) **   <a name="forecast-CreateDatasetImportJob-response-DatasetImportJobArn"></a>
The Amazon Resource Name (ARN) of the dataset import job.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+` 

## Errors
<a name="API_CreateDatasetImportJob_Errors"></a>

 ** InvalidInputException **   
We can't process the request because it includes an invalid value or a value that exceeds the valid range.  
HTTP Status Code: 400

 ** LimitExceededException **   
The limit on the number of resources per account has been exceeded.  
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **   
There is already a resource with this name. Try again with a different name.  
HTTP Status Code: 400

 ** ResourceInUseException **   
The specified resource is in use.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.  
HTTP Status Code: 400

## See Also
<a name="API_CreateDatasetImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecast-2018-06-26/CreateDatasetImportJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecast-2018-06-26/CreateDatasetImportJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/CreateDatasetImportJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecast-2018-06-26/CreateDatasetImportJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/CreateDatasetImportJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecast-2018-06-26/CreateDatasetImportJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecast-2018-06-26/CreateDatasetImportJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecast-2018-06-26/CreateDatasetImportJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecast-2018-06-26/CreateDatasetImportJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/CreateDatasetImportJob) 
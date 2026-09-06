

# CreateDataDeletionJob
<a name="API_CreateDataDeletionJob"></a>

Creates a batch job that deletes all references to specific users from an Amazon Personalize dataset group in batches. You specify the users to delete in a CSV file of userIds in an Amazon S3 bucket. After a job completes, Amazon Personalize no longer trains on the users’ data and no longer considers the users when generating user segments. For more information about creating a data deletion job, see [Deleting users](https://docs.aws.amazon.com/personalize/latest/dg/delete-records.html).
+ Your input file must be a CSV file with a single USER\_ID column that lists the users IDs. For more information about preparing the CSV file, see [Preparing your data deletion file and uploading it to Amazon S3](https://docs.aws.amazon.com/personalize/latest/dg/prepare-deletion-input-file.html).
+ To give Amazon Personalize permission to access your input CSV file of userIds, you must specify an IAM service role that has permission to read from the data source. This role needs `GetObject` and `ListBucket` permissions for the bucket and its content. These permissions are the same as importing data. For information on granting access to your Amazon S3 bucket, see [Giving Amazon Personalize Access to Amazon S3 Resources](https://docs.aws.amazon.com/personalize/latest/dg/granting-personalize-s3-access.html). 

 After you create a job, it can take up to a day to delete all references to the users from datasets and models. Until the job completes, Amazon Personalize continues to use the data when training. And if you use a User Segmentation recipe, the users might appear in user segments. 

 **Status** 

A data deletion job can have one of the following statuses:
+ PENDING > IN\_PROGRESS > COMPLETED -or- FAILED

To get the status of the data deletion job, call [DescribeDataDeletionJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataDeletionJob.html) API operation and specify the Amazon Resource Name (ARN) of the job. If the status is FAILED, the response includes a `failureReason` key, which describes why the job failed.

**Related APIs**
+  [ListDataDeletionJobs](https://docs.aws.amazon.com/personalize/latest/dg/API_ListDataDeletionJobs.html) 
+  [DescribeDataDeletionJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataDeletionJob.html) 

## Request Syntax
<a name="API_CreateDataDeletionJob_RequestSyntax"></a>

```
{
   "datasetGroupArn": "{{string}}",
   "dataSource": { 
      "dataLocation": "{{string}}"
   },
   "jobName": "{{string}}",
   "roleArn": "{{string}}",
   "tags": [ 
      { 
         "tagKey": "{{string}}",
         "tagValue": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateDataDeletionJob_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [datasetGroupArn](#API_CreateDataDeletionJob_RequestSyntax) **   <a name="personalize-CreateDataDeletionJob-request-datasetGroupArn"></a>
The Amazon Resource Name (ARN) of the dataset group that has the datasets you want to delete records from.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: Yes

 ** [dataSource](#API_CreateDataDeletionJob_RequestSyntax) **   <a name="personalize-CreateDataDeletionJob-request-dataSource"></a>
The Amazon S3 bucket that contains the list of userIds of the users to delete.  
Type: [DataSource](API_DataSource.md) object  
Required: Yes

 ** [jobName](#API_CreateDataDeletionJob_RequestSyntax) **   <a name="personalize-CreateDataDeletionJob-request-jobName"></a>
The name for the data deletion job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`   
Required: Yes

 ** [roleArn](#API_CreateDataDeletionJob_RequestSyntax) **   <a name="personalize-CreateDataDeletionJob-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that has permissions to read from the Amazon S3 data source.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`   
Required: Yes

 ** [tags](#API_CreateDataDeletionJob_RequestSyntax) **   <a name="personalize-CreateDataDeletionJob-request-tags"></a>
A list of [tags](https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html) to apply to the data deletion job.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateDataDeletionJob_ResponseSyntax"></a>

```
{
   "dataDeletionJobArn": "string"
}
```

## Response Elements
<a name="API_CreateDataDeletionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataDeletionJobArn](#API_CreateDataDeletionJob_ResponseSyntax) **   <a name="personalize-CreateDataDeletionJob-response-dataDeletionJobArn"></a>
The Amazon Resource Name (ARN) of the data deletion job.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+` 

## Errors
<a name="API_CreateDataDeletionJob_Errors"></a>

 ** InvalidInputException **   
Provide a valid value for the field or parameter.  
HTTP Status Code: 400

 ** LimitExceededException **   
The limit on the number of requests per second has been exceeded.  
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **   
The specified resource already exists.  
HTTP Status Code: 400

 ** ResourceInUseException **   
The specified resource is in use.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Could not find the specified resource.  
HTTP Status Code: 400

 ** TooManyTagsException **   
You have exceeded the maximum number of tags you can apply to this resource.   
HTTP Status Code: 400

## See Also
<a name="API_CreateDataDeletionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/personalize-2018-05-22/CreateDataDeletionJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/personalize-2018-05-22/CreateDataDeletionJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/CreateDataDeletionJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/personalize-2018-05-22/CreateDataDeletionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/CreateDataDeletionJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateDataDeletionJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/personalize-2018-05-22/CreateDataDeletionJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/personalize-2018-05-22/CreateDataDeletionJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/personalize-2018-05-22/CreateDataDeletionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/CreateDataDeletionJob) 
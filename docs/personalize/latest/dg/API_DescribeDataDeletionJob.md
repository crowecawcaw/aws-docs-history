

# DescribeDataDeletionJob
<a name="API_DescribeDataDeletionJob"></a>

Describes the data deletion job created by [CreateDataDeletionJob](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataDeletionJob.html), including the job status.

## Request Syntax
<a name="API_DescribeDataDeletionJob_RequestSyntax"></a>

```
{
   "dataDeletionJobArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDataDeletionJob_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [dataDeletionJobArn](#API_DescribeDataDeletionJob_RequestSyntax) **   <a name="personalize-DescribeDataDeletionJob-request-dataDeletionJobArn"></a>
The Amazon Resource Name (ARN) of the data deletion job.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: Yes

## Response Syntax
<a name="API_DescribeDataDeletionJob_ResponseSyntax"></a>

```
{
   "dataDeletionJob": { 
      "creationDateTime": number,
      "dataDeletionJobArn": "string",
      "datasetGroupArn": "string",
      "dataSource": { 
         "dataLocation": "string"
      },
      "failureReason": "string",
      "jobName": "string",
      "lastUpdatedDateTime": number,
      "numDeleted": number,
      "roleArn": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_DescribeDataDeletionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataDeletionJob](#API_DescribeDataDeletionJob_ResponseSyntax) **   <a name="personalize-DescribeDataDeletionJob-response-dataDeletionJob"></a>
Information about the data deletion job, including the status.  
The status is one of the following values:  
+ PENDING
+ IN\_PROGRESS
+ COMPLETED
+ FAILED
Type: [DataDeletionJob](API_DataDeletionJob.md) object

## Errors
<a name="API_DescribeDataDeletionJob_Errors"></a>

 ** InvalidInputException **   
Provide a valid value for the field or parameter.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Could not find the specified resource.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeDataDeletionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/personalize-2018-05-22/DescribeDataDeletionJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/personalize-2018-05-22/DescribeDataDeletionJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/DescribeDataDeletionJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/personalize-2018-05-22/DescribeDataDeletionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/DescribeDataDeletionJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeDataDeletionJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/personalize-2018-05-22/DescribeDataDeletionJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/personalize-2018-05-22/DescribeDataDeletionJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/personalize-2018-05-22/DescribeDataDeletionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/DescribeDataDeletionJob) 
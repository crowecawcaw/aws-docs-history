# ListJobs

Lists current S3 Batch Operations jobs as well as the jobs that have ended within the last 90
 days for the AWS account making the request. For more information, see [S3 Batch Operations](../userguide/batch-ops.md "../userguide/batch-ops.md") in the *Amazon S3 User Guide*.



Permissions

To use the `ListJobs` operation, you must have permission to perform
 the `s3:ListJobs` action.



Related actions include:


* [CreateJob](API_control_CreateJob.md "API_control_CreateJob.md")
* [DescribeJob](API_control_DescribeJob.md "API_control_DescribeJob.md")
* [UpdateJobPriority](API_control_UpdateJobPriority.md "API_control_UpdateJobPriority.md")
* [UpdateJobStatus](API_control_UpdateJobStatus.md "API_control_UpdateJobStatus.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/jobs?jobStatuses=`JobStatuses`&maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[jobStatuses](#API_control_ListJobs_RequestSyntax "#API_control_ListJobs_RequestSyntax")**


The `List Jobs` request returns jobs that match the statuses listed in this
 element.


Valid Values: `Active | Cancelled | Cancelling | Complete | Completing | Failed | Failing | New | Paused | Pausing | Preparing | Ready | Suspended`





**[maxResults](#API_control_ListJobs_RequestSyntax "#API_control_ListJobs_RequestSyntax")**


The maximum number of jobs that Amazon S3 will include in the `List Jobs`
 response. If there are more jobs than this number, the response will include a pagination
 token in the `NextToken` field to enable you to retrieve the next page of
 results.


Valid Range: Minimum value of 0. Maximum value of 1000.




**[nextToken](#API_control_ListJobs_RequestSyntax "#API_control_ListJobs_RequestSyntax")**


A pagination token to request the next page of results. Use the token that Amazon S3 returned
 in the `NextToken` element of the `ListJobsResult` from the previous
 `List Jobs` request.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `^[A-Za-z0-9\+\:\/\=\?\#-_]+$`





**[x-amz-account-id](#API_control_ListJobs_RequestSyntax "#API_control_ListJobs_RequestSyntax")**


The AWS account ID associated with the S3 Batch Operations job.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[ListJobsResult](#AmazonS3-control_ListJobs-response-ListJobsResult "#AmazonS3-control_ListJobs-response-ListJobsResult")>
   <[NextToken](#AmazonS3-control_ListJobs-response-NextToken "#AmazonS3-control_ListJobs-response-NextToken")>***string***</[NextToken](#AmazonS3-control_ListJobs-response-NextToken "#AmazonS3-control_ListJobs-response-NextToken")>
   <[Jobs](#AmazonS3-control_ListJobs-response-Jobs "#AmazonS3-control_ListJobs-response-Jobs")>
      <JobListDescriptor>
         <[CreationTime](API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-CreationTime "API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-CreationTime")>***timestamp***</[CreationTime](API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-CreationTime "API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-CreationTime")>
         <[Description](API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-Description "API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-Description")>***string***</[Description](API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-Description "API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-Description")>
         <[JobId](API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-JobId "API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-JobId")>***string***</[JobId](API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-JobId "API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-JobId")>
         <[Operation](API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-Operation "API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-Operation")>***string***</[Operation](API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-Operation "API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-Operation")>
         <[Priority](API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-Priority "API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-Priority")>***integer***</[Priority](API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-Priority "API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-Priority")>
         <[ProgressSummary](API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-ProgressSummary "API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-ProgressSummary")>
            <[NumberOfTasksFailed](API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-NumberOfTasksFailed "API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-NumberOfTasksFailed")>***long***</[NumberOfTasksFailed](API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-NumberOfTasksFailed "API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-NumberOfTasksFailed")>
            <[NumberOfTasksSucceeded](API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-NumberOfTasksSucceeded "API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-NumberOfTasksSucceeded")>***long***</[NumberOfTasksSucceeded](API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-NumberOfTasksSucceeded "API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-NumberOfTasksSucceeded")>
            <[Timers](API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-Timers "API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-Timers")>
               <[ElapsedTimeInActiveSeconds](API_control_JobTimers.md#AmazonS3-Type-control_JobTimers-ElapsedTimeInActiveSeconds "API_control_JobTimers.md#AmazonS3-Type-control_JobTimers-ElapsedTimeInActiveSeconds")>***long***</[ElapsedTimeInActiveSeconds](API_control_JobTimers.md#AmazonS3-Type-control_JobTimers-ElapsedTimeInActiveSeconds "API_control_JobTimers.md#AmazonS3-Type-control_JobTimers-ElapsedTimeInActiveSeconds")>
            </[Timers](API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-Timers "API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-Timers")>
            <[TotalNumberOfTasks](API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-TotalNumberOfTasks "API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-TotalNumberOfTasks")>***long***</[TotalNumberOfTasks](API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-TotalNumberOfTasks "API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-TotalNumberOfTasks")>
         </[ProgressSummary](API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-ProgressSummary "API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-ProgressSummary")>
         <[Status](API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-Status "API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-Status")>***string***</[Status](API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-Status "API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-Status")>
         <[TerminationDate](API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-TerminationDate "API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-TerminationDate")>***timestamp***</[TerminationDate](API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-TerminationDate "API_control_JobListDescriptor.md#AmazonS3-Type-control_JobListDescriptor-TerminationDate")>
      </JobListDescriptor>
   </[Jobs](#AmazonS3-control_ListJobs-response-Jobs "#AmazonS3-control_ListJobs-response-Jobs")>
</[ListJobsResult](#AmazonS3-control_ListJobs-response-ListJobsResult "#AmazonS3-control_ListJobs-response-ListJobsResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ListJobsResult](#API_control_ListJobs_ResponseSyntax "#API_control_ListJobs_ResponseSyntax")**


Root level tag for the ListJobsResult parameters.


Required: Yes




**[Jobs](#API_control_ListJobs_ResponseSyntax "#API_control_ListJobs_ResponseSyntax")**


The list of current jobs and jobs that have ended within the last 30 days.


Type: Array of [JobListDescriptor](API_control_JobListDescriptor.md "API_control_JobListDescriptor.md") data types




**[NextToken](#API_control_ListJobs_ResponseSyntax "#API_control_ListJobs_ResponseSyntax")**


If the `List Jobs` request produced more than the maximum number of results,
 you can pass this value into a subsequent `List Jobs` request in order to
 retrieve the next page of results.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `^[A-Za-z0-9\+\:\/\=\?\#-_]+$`





## Errors





**InternalServiceException** 



HTTP Status Code: 500




**InvalidNextTokenException** 



HTTP Status Code: 400




**InvalidRequestException** 



HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListJobs "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListJobs")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/ListJobs "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/ListJobs")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListJobs "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListJobs")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListJobs "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListJobs")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListJobs "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListJobs")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListJobs "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListJobs")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListJobs "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListJobs")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListJobs "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListJobs")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListJobs "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListJobs")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListJobs "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListJobs")

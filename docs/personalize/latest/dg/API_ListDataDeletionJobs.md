

# ListDataDeletionJobs
<a name="API_ListDataDeletionJobs"></a>

Returns a list of data deletion jobs for a dataset group ordered by creation time, with the most recent first. When a dataset group is not specified, all the data deletion jobs associated with the account are listed. The response provides the properties for each job, including the Amazon Resource Name (ARN). For more information on data deletion jobs, see [Deleting users](https://docs.aws.amazon.com/personalize/latest/dg/delete-records.html).

## Request Syntax
<a name="API_ListDataDeletionJobs_RequestSyntax"></a>

```
{
   "datasetGroupArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDataDeletionJobs_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [datasetGroupArn](#API_ListDataDeletionJobs_RequestSyntax) **   <a name="personalize-ListDataDeletionJobs-request-datasetGroupArn"></a>
The Amazon Resource Name (ARN) of the dataset group to list data deletion jobs for.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** [maxResults](#API_ListDataDeletionJobs_RequestSyntax) **   <a name="personalize-ListDataDeletionJobs-request-maxResults"></a>
The maximum number of data deletion jobs to return.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListDataDeletionJobs_RequestSyntax) **   <a name="personalize-ListDataDeletionJobs-request-nextToken"></a>
A token returned from the previous call to `ListDataDeletionJobs` for getting the next set of jobs (if they exist).  
Type: String  
Length Constraints: Maximum length of 1500.  
Pattern: `\p{ASCII}{0,1500}`   
Required: No

## Response Syntax
<a name="API_ListDataDeletionJobs_ResponseSyntax"></a>

```
{
   "dataDeletionJobs": [ 
      { 
         "creationDateTime": number,
         "dataDeletionJobArn": "string",
         "datasetGroupArn": "string",
         "failureReason": "string",
         "jobName": "string",
         "lastUpdatedDateTime": number,
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDataDeletionJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataDeletionJobs](#API_ListDataDeletionJobs_ResponseSyntax) **   <a name="personalize-ListDataDeletionJobs-response-dataDeletionJobs"></a>
The list of data deletion jobs.  
Type: Array of [DataDeletionJobSummary](API_DataDeletionJobSummary.md) objects  
Array Members: Maximum number of 100 items.

 ** [nextToken](#API_ListDataDeletionJobs_ResponseSyntax) **   <a name="personalize-ListDataDeletionJobs-response-nextToken"></a>
A token for getting the next set of data deletion jobs (if they exist).  
Type: String  
Length Constraints: Maximum length of 1500.  
Pattern: `\p{ASCII}{0,1500}` 

## Errors
<a name="API_ListDataDeletionJobs_Errors"></a>

 ** InvalidInputException **   
Provide a valid value for the field or parameter.  
HTTP Status Code: 400

 ** InvalidNextTokenException **   
The token is not valid.  
HTTP Status Code: 400

## See Also
<a name="API_ListDataDeletionJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/personalize-2018-05-22/ListDataDeletionJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/personalize-2018-05-22/ListDataDeletionJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/ListDataDeletionJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/personalize-2018-05-22/ListDataDeletionJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/ListDataDeletionJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/personalize-2018-05-22/ListDataDeletionJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/personalize-2018-05-22/ListDataDeletionJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/personalize-2018-05-22/ListDataDeletionJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/personalize-2018-05-22/ListDataDeletionJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/ListDataDeletionJobs) 
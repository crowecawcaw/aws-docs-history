# GetTableMaintenanceJobStatus

Gets the status of a maintenance job for a table. For more information, see [S3 Tables maintenance](../userguide/s3-tables-maintenance.md "../userguide/s3-tables-maintenance.md") in the *Amazon Simple Storage Service User Guide*.



Permissions

You must have the `s3tables:GetTableMaintenanceJobStatus` permission to use this operation. 




## Request Syntax



```
GET /tables/`tableBucketARN`/`namespace`/`name`/maintenance-job-status HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_s3Buckets_GetTableMaintenanceJobStatus_RequestSyntax "#API_s3Buckets_GetTableMaintenanceJobStatus_RequestSyntax")**


The name of the table containing the maintenance job status you want to check.


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[0-9a-z_]*`



Required: Yes




**[namespace](#API_s3Buckets_GetTableMaintenanceJobStatus_RequestSyntax "#API_s3Buckets_GetTableMaintenanceJobStatus_RequestSyntax")**


The name of the namespace the table is associated with.
 
 


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[0-9a-z_]*`



Required: Yes




**[tableBucketARN](#API_s3Buckets_GetTableMaintenanceJobStatus_RequestSyntax "#API_s3Buckets_GetTableMaintenanceJobStatus_RequestSyntax")**


The Amazon Resource Name (ARN) of the table bucket.


Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[status](#AmazonS3-s3Buckets_GetTableMaintenanceJobStatus-response-status "#AmazonS3-s3Buckets_GetTableMaintenanceJobStatus-response-status")": { 
      "***string***" : { 
         "[failureMessage](API_s3Buckets_TableMaintenanceJobStatusValue.md#AmazonS3-Type-s3Buckets_TableMaintenanceJobStatusValue-failureMessage "API_s3Buckets_TableMaintenanceJobStatusValue.md#AmazonS3-Type-s3Buckets_TableMaintenanceJobStatusValue-failureMessage")": "***string***",
         "[lastRunTimestamp](API_s3Buckets_TableMaintenanceJobStatusValue.md#AmazonS3-Type-s3Buckets_TableMaintenanceJobStatusValue-lastRunTimestamp "API_s3Buckets_TableMaintenanceJobStatusValue.md#AmazonS3-Type-s3Buckets_TableMaintenanceJobStatusValue-lastRunTimestamp")": "***string***",
         "[status](API_s3Buckets_TableMaintenanceJobStatusValue.md#AmazonS3-Type-s3Buckets_TableMaintenanceJobStatusValue-status "API_s3Buckets_TableMaintenanceJobStatusValue.md#AmazonS3-Type-s3Buckets_TableMaintenanceJobStatusValue-status")": "***string***"
      }
   },
   "[tableARN](#AmazonS3-s3Buckets_GetTableMaintenanceJobStatus-response-tableARN "#AmazonS3-s3Buckets_GetTableMaintenanceJobStatus-response-tableARN")": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[status](#API_s3Buckets_GetTableMaintenanceJobStatus_ResponseSyntax "#API_s3Buckets_GetTableMaintenanceJobStatus_ResponseSyntax")**


The status of the maintenance job.


Type: String to [TableMaintenanceJobStatusValue](API_s3Buckets_TableMaintenanceJobStatusValue.md "API_s3Buckets_TableMaintenanceJobStatusValue.md") object map


Valid Keys: `icebergCompaction | icebergSnapshotManagement | icebergUnreferencedFileRemoval`





**[tableARN](#API_s3Buckets_GetTableMaintenanceJobStatus_ResponseSyntax "#API_s3Buckets_GetTableMaintenanceJobStatus_ResponseSyntax")**


The Amazon Resource Name (ARN) of the table.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`





## Errors





**BadRequestException** 


The request is invalid or malformed.


HTTP Status Code: 400




**ConflictException** 


The request failed because there is a conflict with a previous write. You can retry the
 request.


HTTP Status Code: 409




**ForbiddenException** 


The caller isn't authorized to make the request.


HTTP Status Code: 403




**InternalServerErrorException** 


The request failed due to an internal server error.


HTTP Status Code: 500




**NotFoundException** 


The request was rejected because the specified resource could not be found.


HTTP Status Code: 404




**TooManyRequestsException** 


The limit on the number of requests per second was exceeded.


HTTP Status Code: 429




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/GetTableMaintenanceJobStatus "https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/GetTableMaintenanceJobStatus")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/GetTableMaintenanceJobStatus "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/GetTableMaintenanceJobStatus")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/GetTableMaintenanceJobStatus "https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/GetTableMaintenanceJobStatus")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/GetTableMaintenanceJobStatus "https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/GetTableMaintenanceJobStatus")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/GetTableMaintenanceJobStatus "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/GetTableMaintenanceJobStatus")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/GetTableMaintenanceJobStatus "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/GetTableMaintenanceJobStatus")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/GetTableMaintenanceJobStatus "https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/GetTableMaintenanceJobStatus")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/GetTableMaintenanceJobStatus "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/GetTableMaintenanceJobStatus")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/GetTableMaintenanceJobStatus "https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/GetTableMaintenanceJobStatus")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/GetTableMaintenanceJobStatus "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/GetTableMaintenanceJobStatus")

# PutTableBucketMaintenanceConfiguration

Creates a new maintenance configuration or replaces an existing maintenance configuration
 for a table bucket. For more information, see [Amazon S3 table bucket maintenance](../userguide/s3-table-buckets-maintenance.md "../userguide/s3-table-buckets-maintenance.md") in the *Amazon Simple Storage Service User Guide*.



Permissions

You must have the `s3tables:PutTableBucketMaintenanceConfiguration` permission to use this operation. 




## Request Syntax



```
PUT /buckets/`tableBucketARN`/maintenance/`type` HTTP/1.1
Content-type: application/json

{
   "[value](#AmazonS3-s3Buckets_PutTableBucketMaintenanceConfiguration-request-value "#AmazonS3-s3Buckets_PutTableBucketMaintenanceConfiguration-request-value")": { 
      "[settings](API_s3Buckets_TableBucketMaintenanceConfigurationValue.md#AmazonS3-Type-s3Buckets_TableBucketMaintenanceConfigurationValue-settings "API_s3Buckets_TableBucketMaintenanceConfigurationValue.md#AmazonS3-Type-s3Buckets_TableBucketMaintenanceConfigurationValue-settings")": { ... },
      "[status](API_s3Buckets_TableBucketMaintenanceConfigurationValue.md#AmazonS3-Type-s3Buckets_TableBucketMaintenanceConfigurationValue-status "API_s3Buckets_TableBucketMaintenanceConfigurationValue.md#AmazonS3-Type-s3Buckets_TableBucketMaintenanceConfigurationValue-status")": "`string`"
   }
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[tableBucketARN](#API_s3Buckets_PutTableBucketMaintenanceConfiguration_RequestSyntax "#API_s3Buckets_PutTableBucketMaintenanceConfiguration_RequestSyntax")**


The Amazon Resource Name (ARN) of the table bucket associated with the maintenance
 configuration.


Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`



Required: Yes




**[type](#API_s3Buckets_PutTableBucketMaintenanceConfiguration_RequestSyntax "#API_s3Buckets_PutTableBucketMaintenanceConfiguration_RequestSyntax")**


The type of the maintenance configuration.


Valid Values: `icebergUnreferencedFileRemoval`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[value](#API_s3Buckets_PutTableBucketMaintenanceConfiguration_RequestSyntax "#API_s3Buckets_PutTableBucketMaintenanceConfiguration_RequestSyntax")**


Defines the values of the maintenance configuration for the table bucket.


Type: [TableBucketMaintenanceConfigurationValue](API_s3Buckets_TableBucketMaintenanceConfigurationValue.md "API_s3Buckets_TableBucketMaintenanceConfigurationValue.md") object


Required: Yes




## Response Syntax



```
HTTP/1.1 204

```

## Response Elements


If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration "https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration "https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/PutTableBucketMaintenanceConfiguration")

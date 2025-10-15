# GetTableMaintenanceConfiguration

Gets details about the maintenance configuration of a table. For more information, see [S3 Tables maintenance](../userguide/s3-tables-maintenance.md "../userguide/s3-tables-maintenance.md") in the *Amazon Simple Storage Service User Guide*.



Permissions


* You must have the `s3tables:GetTableMaintenanceConfiguration` permission to use this operation.
* You must have the `s3tables:GetTableData` permission to use set the compaction strategy to `sort` or `zorder`.



## Request Syntax



```
GET /tables/`tableBucketARN`/`namespace`/`name`/maintenance HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_s3Buckets_GetTableMaintenanceConfiguration_RequestSyntax "#API_s3Buckets_GetTableMaintenanceConfiguration_RequestSyntax")**


The name of the table.


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[0-9a-z_]*`



Required: Yes




**[namespace](#API_s3Buckets_GetTableMaintenanceConfiguration_RequestSyntax "#API_s3Buckets_GetTableMaintenanceConfiguration_RequestSyntax")**


The namespace associated with the table.


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[0-9a-z_]*`



Required: Yes




**[tableBucketARN](#API_s3Buckets_GetTableMaintenanceConfiguration_RequestSyntax "#API_s3Buckets_GetTableMaintenanceConfiguration_RequestSyntax")**


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
   "[configuration](#AmazonS3-s3Buckets_GetTableMaintenanceConfiguration-response-configuration "#AmazonS3-s3Buckets_GetTableMaintenanceConfiguration-response-configuration")": { 
      "***string***" : { 
         "[settings](API_s3Buckets_TableMaintenanceConfigurationValue.md#AmazonS3-Type-s3Buckets_TableMaintenanceConfigurationValue-settings "API_s3Buckets_TableMaintenanceConfigurationValue.md#AmazonS3-Type-s3Buckets_TableMaintenanceConfigurationValue-settings")": { ... },
         "[status](API_s3Buckets_TableMaintenanceConfigurationValue.md#AmazonS3-Type-s3Buckets_TableMaintenanceConfigurationValue-status "API_s3Buckets_TableMaintenanceConfigurationValue.md#AmazonS3-Type-s3Buckets_TableMaintenanceConfigurationValue-status")": "***string***"
      }
   },
   "[tableARN](#AmazonS3-s3Buckets_GetTableMaintenanceConfiguration-response-tableARN "#AmazonS3-s3Buckets_GetTableMaintenanceConfiguration-response-tableARN")": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[configuration](#API_s3Buckets_GetTableMaintenanceConfiguration_ResponseSyntax "#API_s3Buckets_GetTableMaintenanceConfiguration_ResponseSyntax")**


Details about the maintenance configuration for the table bucket.


Type: String to [TableMaintenanceConfigurationValue](API_s3Buckets_TableMaintenanceConfigurationValue.md "API_s3Buckets_TableMaintenanceConfigurationValue.md") object map


Valid Keys: `icebergCompaction | icebergSnapshotManagement`





**[tableARN](#API_s3Buckets_GetTableMaintenanceConfiguration_ResponseSyntax "#API_s3Buckets_GetTableMaintenanceConfiguration_ResponseSyntax")**


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/GetTableMaintenanceConfiguration "https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/GetTableMaintenanceConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/GetTableMaintenanceConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/GetTableMaintenanceConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/GetTableMaintenanceConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/GetTableMaintenanceConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/GetTableMaintenanceConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/GetTableMaintenanceConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/GetTableMaintenanceConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/GetTableMaintenanceConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/GetTableMaintenanceConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/GetTableMaintenanceConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/GetTableMaintenanceConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/GetTableMaintenanceConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/GetTableMaintenanceConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/GetTableMaintenanceConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/GetTableMaintenanceConfiguration "https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/GetTableMaintenanceConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/GetTableMaintenanceConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/GetTableMaintenanceConfiguration")

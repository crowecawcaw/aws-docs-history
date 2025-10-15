# PutTablePolicy

Creates a new table policy or replaces an existing table policy for a table. For more information, see [Adding a table policy](../userguide/s3-tables-table-policy.md#table-policy-add "../userguide/s3-tables-table-policy.md#table-policy-add") in the *Amazon Simple Storage Service User Guide*.
 



Permissions

You must have the `s3tables:PutTablePolicy` permission to use this operation. 




## Request Syntax



```
PUT /tables/`tableBucketARN`/`namespace`/`name`/policy HTTP/1.1
Content-type: application/json

{
   "[resourcePolicy](#AmazonS3-s3Buckets_PutTablePolicy-request-resourcePolicy "#AmazonS3-s3Buckets_PutTablePolicy-request-resourcePolicy")": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_s3Buckets_PutTablePolicy_RequestSyntax "#API_s3Buckets_PutTablePolicy_RequestSyntax")**


The name of the table.


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[0-9a-z_]*`



Required: Yes




**[namespace](#API_s3Buckets_PutTablePolicy_RequestSyntax "#API_s3Buckets_PutTablePolicy_RequestSyntax")**


The namespace associated with the table.


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[0-9a-z_]*`



Required: Yes




**[tableBucketARN](#API_s3Buckets_PutTablePolicy_RequestSyntax "#API_s3Buckets_PutTablePolicy_RequestSyntax")**


The Amazon Resource Name (ARN) of the table bucket that contains the table.


Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[resourcePolicy](#API_s3Buckets_PutTablePolicy_RequestSyntax "#API_s3Buckets_PutTablePolicy_RequestSyntax")**


The `JSON` that defines the policy.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 20480.


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/PutTablePolicy "https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/PutTablePolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/PutTablePolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/PutTablePolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/PutTablePolicy "https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/PutTablePolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/PutTablePolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/PutTablePolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/PutTablePolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/PutTablePolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/PutTablePolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/PutTablePolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/PutTablePolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/PutTablePolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/PutTablePolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/PutTablePolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/PutTablePolicy "https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/PutTablePolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/PutTablePolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/PutTablePolicy")

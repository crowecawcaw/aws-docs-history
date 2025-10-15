# DeleteBucketReplication

###### Note

This operation deletes an Amazon S3 on Outposts bucket's replication configuration. To
 delete an S3 bucket's replication configuration, see [DeleteBucketReplication](API_DeleteBucketReplication.md "API_DeleteBucketReplication.md") in the *Amazon S3 API Reference*. 

Deletes the replication configuration from the specified S3 on Outposts bucket.

To use this operation, you must have permissions to perform the
 `s3-outposts:PutReplicationConfiguration` action. The Outposts bucket owner
 has this permission by default and can grant it to others. For more information about
 permissions, see [Setting up IAM with
 S3 on Outposts](../userguide/S3OutpostsIAM.md "../userguide/S3OutpostsIAM.md") and [Managing access to
 S3 on Outposts buckets](../userguide/S3OutpostsBucketPolicy.md "../userguide/S3OutpostsBucketPolicy.md") in the *Amazon S3 User Guide*.

###### Note

It can take a while to propagate `PUT` or `DELETE` requests for
 a replication configuration to all S3 on Outposts systems. Therefore, the replication
 configuration that's returned by a `GET` request soon after a
 `PUT` or `DELETE` request might return a more recent result
 than what's on the Outpost. If an Outpost is offline, the delay in updating the
 replication configuration on that Outpost can be significant.

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](API_control_DeleteBucketReplication.md#API_control_DeleteBucketReplication_Examples "API_control_DeleteBucketReplication.md#API_control_DeleteBucketReplication_Examples") section.

For information about S3 replication on Outposts configuration, see [Replicating objects for S3 on Outposts](../userguide/S3OutpostsReplication.md "../userguide/S3OutpostsReplication.md") in the
 *Amazon S3 User Guide*.

The following operations are related to `DeleteBucketReplication`:


* [PutBucketReplication](API_control_PutBucketReplication.md "API_control_PutBucketReplication.md")
* [GetBucketReplication](API_control_GetBucketReplication.md "API_control_GetBucketReplication.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /v20180820/bucket/`name`/replication HTTP/1.1
Host: `Bucket`.s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_DeleteBucketReplication_RequestSyntax "#API_control_DeleteBucketReplication_RequestSyntax")**


Specifies the S3 on Outposts bucket to delete the replication configuration for.


For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.


For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded. 


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**[x-amz-account-id](#API_control_DeleteBucketReplication_RequestSyntax "#API_control_DeleteBucketReplication_RequestSyntax")**


The AWS account ID of the Outposts bucket to delete the replication configuration
 for.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Sample Request


The following `DELETE` request deletes the `replication`
 subresource from the specified S3 on Outposts bucket. This request removes the
 replication configuration that is set for the bucket. 



```

DELETE /v20180820/bucket/example-outpost-bucket/replication HTTP/1.1
Host: s3-outposts.<Region>.amazonaws.com 
x-amz-outpost-id: op-01ac5d28a6a232904
x-amz-account-id:example-account-id
               
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteBucketReplication "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteBucketReplication")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DeleteBucketReplication "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DeleteBucketReplication")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteBucketReplication "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteBucketReplication")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteBucketReplication "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteBucketReplication")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteBucketReplication "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteBucketReplication")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteBucketReplication "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteBucketReplication")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteBucketReplication "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteBucketReplication")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteBucketReplication "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteBucketReplication")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteBucketReplication "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteBucketReplication")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteBucketReplication "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteBucketReplication")

# DeleteBucketMetricsConfiguration

###### Note

This operation is not supported for directory buckets.

Deletes a metrics configuration for the Amazon CloudWatch request metrics (specified by the metrics
 configuration ID) from the bucket. Note that this doesn't include the daily storage metrics.

 To use this operation, you must have permissions to perform the
 `s3:PutMetricsConfiguration` action. The bucket owner has this permission by default. The
 bucket owner can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Managing Access Permissions to Your Amazon S3
 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md").

For information about CloudWatch request metrics for Amazon S3, see [Monitoring Metrics with Amazon CloudWatch](https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html"). 

The following operations are related to `DeleteBucketMetricsConfiguration`:


* [GetBucketMetricsConfiguration](API_GetBucketMetricsConfiguration.md "API_GetBucketMetricsConfiguration.md")
* [PutBucketMetricsConfiguration](API_PutBucketMetricsConfiguration.md "API_PutBucketMetricsConfiguration.md")
* [ListBucketMetricsConfigurations](API_ListBucketMetricsConfigurations.md "API_ListBucketMetricsConfigurations.md")
* [Monitoring
 Metrics with Amazon CloudWatch](https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /?metrics&id=`Id` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_DeleteBucketMetricsConfiguration_RequestSyntax "#API_DeleteBucketMetricsConfiguration_RequestSyntax")**


The name of the bucket containing the metrics configuration to delete.


Required: Yes




**[id](#API_DeleteBucketMetricsConfiguration_RequestSyntax "#API_DeleteBucketMetricsConfiguration_RequestSyntax")**


The ID used to identify the metrics configuration. The ID has a 64 character limit and can only
 contain letters, numbers, periods, dashes, and underscores.


Required: Yes




**[x-amz-expected-bucket-owner](#API_DeleteBucketMetricsConfiguration_RequestSyntax "#API_DeleteBucketMetricsConfiguration_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 204

```

## Response Elements


If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.


## Examples


### Sample Request


Delete the metric configuration with a specified ID, which disables the CloudWatch metrics with
 the `ExampleMetrics` value for the `FilterId` dimension. 



```

            DELETE /?metrics&id=ExampleMetrics HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            x-amz-date: Thu, 15 Nov 2016 00:17:21 GMT
            Authorization: signatureValue
         
```

### Sample Response


Delete the metric configuration with a specified ID, which disables the CloudWatch metrics with
 the `ExampleMetrics` value for the `FilterId` dimension. 



```

            HTTP/1.1 204 No Content
            x-amz-id-2: ITnGT1y4REXAMPLEPi4hklTXouTf0hccUjo0iCPEXAMPLEutBj3M7fPGlWO2SEWp
            x-amz-request-id: 51991EXAMPLE5321
            Date: Thu, 15 Nov 2016 00:17:22 GMT
            Server: AmazonS3
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteBucketMetricsConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteBucketMetricsConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketMetricsConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteBucketMetricsConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketMetricsConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteBucketMetricsConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteBucketMetricsConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteBucketMetricsConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketMetricsConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteBucketMetricsConfiguration")

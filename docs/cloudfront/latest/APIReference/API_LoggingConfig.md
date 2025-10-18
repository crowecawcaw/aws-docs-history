# LoggingConfig

A complex type that specifies whether access logs are written for the distribution.

###### Note

If you already enabled standard logging (legacy) and you want to enable standard logging
 (v2) to send your access logs to Amazon S3, we recommend that you specify a
 *different* Amazon S3 bucket or use a *separate
 path* in the same bucket (for example, use a log prefix or
 partitioning). This helps you keep track of which log files are associated with
 which logging subscription and prevents log files from overwriting each other. For
 more information, see [Standard logging (access logs)](../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md "../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md") in the
 *Amazon CloudFront Developer Guide*.


## Contents





**Bucket** 


The Amazon S3 bucket to store the access logs in, for example,
 `amzn-s3-demo-bucket.s3.amazonaws.com`.


Type: String


Required: No




**Enabled** 


Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don't want to
 enable logging when you create a distribution or if you want to disable logging for an
 existing distribution, specify `false` for `Enabled`, and specify
 empty `Bucket` and `Prefix` elements. If you specify
 `false` for `Enabled` but you specify values for
 `Bucket` and `prefix`, the values are automatically
 deleted.


Type: Boolean


Required: No




**IncludeCookies** 


Specifies whether you want CloudFront to include cookies in access logs, specify
 `true` for `IncludeCookies`. If you choose to include cookies
 in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for
 this distribution. If you don't want to include cookies when you create a distribution
 or if you want to disable include cookies for an existing distribution, specify
 `false` for `IncludeCookies`.


Type: Boolean


Required: No




**Prefix** 


An optional string that you want CloudFront to prefix to the access log
 `filenames` for this distribution, for example, `myprefix/`.
 If you want to enable logging, but you don't want to specify a prefix, you still must
 include an empty `Prefix` element in the `Logging` element.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/LoggingConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/LoggingConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/LoggingConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/LoggingConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/LoggingConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/LoggingConfig")

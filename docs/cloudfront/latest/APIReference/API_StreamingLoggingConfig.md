# StreamingLoggingConfig

A complex type that controls whether access logs are written for this streaming
 distribution.


## Contents





**Bucket** 


The Amazon S3 bucket to store the access logs in, for example,
 `amzn-s3-demo-bucket.s3.amazonaws.com`.


Type: String


Required: Yes




**Enabled** 


Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don't
 want to enable logging when you create a streaming distribution or if you want to
 disable logging for an existing streaming distribution, specify `false` for
 `Enabled`, and specify `empty Bucket` and `Prefix`
 elements. If you specify `false` for `Enabled` but you specify
 values for `Bucket` and `Prefix`, the values are automatically
 deleted.


Type: Boolean


Required: Yes




**Prefix** 


An optional string that you want CloudFront to prefix to the access log filenames for this
 streaming distribution, for example, `myprefix/`. If you want to enable
 logging, but you don't want to specify a prefix, you still must include an empty
 `Prefix` element in the `Logging` element.


Type: String


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/StreamingLoggingConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/StreamingLoggingConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/StreamingLoggingConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/StreamingLoggingConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/StreamingLoggingConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/StreamingLoggingConfig")

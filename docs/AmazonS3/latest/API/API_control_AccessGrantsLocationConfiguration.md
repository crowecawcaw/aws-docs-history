# AccessGrantsLocationConfiguration

The configuration options of the S3 Access Grants location. It contains the
 `S3SubPrefix` field. The grant scope, the data to which you are granting
 access, is the result of appending the `Subprefix` field to the scope of the
 registered location.


## Contents





**S3SubPrefix** 


The `S3SubPrefix` is appended to the location scope creating the grant scope.
 Use this field to narrow the scope of the grant to a subset of the location scope. This
 field is required if the location scope is the default location `s3://` because
 you cannot create a grant for all of your S3 data in the Region and must narrow the scope.
 For example, if the location scope is the default location `s3://`, the
 `S3SubPrefx` can be a <bucket-name>/\*, so the full grant scope path
 would be `s3://<bucket-name>/*`. Or the `S3SubPrefx` can be
 `<bucket-name>/<prefix-name>*`, so the full grant scope path
 would be or `s3://<bucket-name>/<prefix-name>*`.


If the `S3SubPrefix` includes a prefix, append the wildcard character
 `*` after the prefix to indicate that you want to include all object key
 names in the bucket that start with that prefix. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2000.


Pattern: `^.+$`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/AccessGrantsLocationConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/AccessGrantsLocationConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/AccessGrantsLocationConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/AccessGrantsLocationConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/AccessGrantsLocationConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/AccessGrantsLocationConfiguration")

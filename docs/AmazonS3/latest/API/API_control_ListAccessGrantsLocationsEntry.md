# ListAccessGrantsLocationsEntry

A container for information about the registered location.


## Contents





**AccessGrantsLocationArn** 


The Amazon Resource Name (ARN) of the registered location. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/location/[a-zA-Z0-9\-]+`



Required: No




**AccessGrantsLocationId** 


The ID of the registered location to which you are granting access. S3 Access Grants assigns this
 ID when you register the location. S3 Access Grants assigns the ID `default` to the
 default location `s3://` and assigns an auto-generated ID to other locations
 that you register. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-]+`



Required: No




**CreatedAt** 


The date and time when you registered the location. 


Type: Timestamp


Required: No




**IAMRoleArn** 


The Amazon Resource Name (ARN) of the IAM role for the registered location. S3 Access Grants
 assumes this role to manage access to the registered location. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `arn:[^:]+:iam::\d{12}:role/.*`



Required: No




**LocationScope** 


The S3 path to the location that you are registering. The location scope can be the
 default S3 location `s3://`, the S3 path to a bucket
 `s3://<bucket>`, or the S3 path to a bucket and prefix
 `s3://<bucket>/<prefix>`. A prefix in S3 is a string of
 characters at the beginning of an object key name used to organize the objects that you
 store in your S3 buckets. For example, object key names that start with the
 `engineering/` prefix or object key names that start with the
 `marketing/campaigns/` prefix.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2000.


Pattern: `^.+$`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessGrantsLocationsEntry "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessGrantsLocationsEntry")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessGrantsLocationsEntry "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessGrantsLocationsEntry")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessGrantsLocationsEntry "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessGrantsLocationsEntry")

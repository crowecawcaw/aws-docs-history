# Grantee

The user, group, or role to which you are granting access. You can grant access to an
 IAM user or role. If you have added your corporate directory to AWS IAM Identity
 Center and associated your Identity Center instance with your S3 Access Grants instance, the grantee
 can also be a corporate directory user or group.


## Contents





**GranteeIdentifier** 


The unique identifier of the `Grantee`. If the grantee type is
 `IAM`, the identifier is the IAM Amazon Resource Name (ARN) of the user
 or role. If the grantee type is a directory user or group, the identifier is 128-bit
 universally unique identifier (UUID) in the format
 `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`. You can obtain this UUID from your
 AWS IAM Identity Center instance.


Type: String


Required: No




**GranteeType** 


The type of the grantee to which access has been granted. It can be one of the following
 values:



* `IAM` - An IAM user or role.
* `DIRECTORY_USER` - Your corporate directory user. You can use
 this option if you have added your corporate identity directory to IAM Identity
 Center and associated the IAM Identity Center instance with your S3 Access Grants
 instance.
* `DIRECTORY_GROUP` - Your corporate directory group. You can use
 this option if you have added your corporate identity directory to IAM Identity
 Center and associated the IAM Identity Center instance with your S3 Access Grants
 instance.

Type: String


Valid Values: `DIRECTORY_USER | DIRECTORY_GROUP | IAM`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/Grantee "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/Grantee")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/Grantee "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/Grantee")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/Grantee "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/Grantee")

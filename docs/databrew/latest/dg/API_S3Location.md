# S3Location

Represents an Amazon S3 location (bucket name, bucket owner, and object key) where DataBrew can read
input data, or write output from a job.

## Contents

###### Note

In the following list, the required parameters are described first.

**Bucket**

The Amazon S3 bucket name.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 63.

Required: Yes

**BucketOwner**

The AWS account ID of the bucket owner.

Type: String

Length Constraints: Fixed length of 12.

Pattern: `^[0-9]{12}$`

Required: No

**Key**

The unique name of the object in the bucket.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1280.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/S3Location.md "../../../goto/SdkForCpp/databrew-2017-07-25/S3Location.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/S3Location.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/S3Location.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/S3Location.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/S3Location.md")

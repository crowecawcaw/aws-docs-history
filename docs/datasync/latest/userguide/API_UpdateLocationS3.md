# UpdateLocationS3

Modifies the following configuration parameters of the Amazon S3 transfer location
that you're using with AWS DataSync.

###### Important

Before you begin, make sure that you read the following topics:

- [Storage
  class considerations with Amazon S3 locations](create-s3-location.md#using-storage-classes "create-s3-location.md#using-storage-classes")
- [Evaluating S3 request costs when using DataSync](create-s3-location.md#create-s3-location-s3-requests "create-s3-location.md#create-s3-location-s3-requests")

## Request Syntax

```
{
   "LocationArn": "`string`",
   "S3Config": {
      "BucketAccessRoleArn": "`string`"
   },
   "S3StorageClass": "`string`",
   "Subdirectory": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[LocationArn](#API_UpdateLocationS3_RequestSyntax "#API_UpdateLocationS3_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the Amazon S3 transfer location that
you're updating.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

**[S3Config](#API_UpdateLocationS3_RequestSyntax "#API_UpdateLocationS3_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that DataSync uses to access your S3 bucket.

For more information, see [Providing
DataSync access to S3 buckets](create-s3-location.md#create-s3-location-access "create-s3-location.md#create-s3-location-access").

Type: [S3Config](API_S3Config.md "API_S3Config.md") object

Required: No

**[S3StorageClass](#API_UpdateLocationS3_RequestSyntax "#API_UpdateLocationS3_RequestSyntax")**

Specifies the storage class that you want your objects to use when Amazon S3 is a
transfer destination.

For buckets in AWS Regions, the storage class defaults to
`STANDARD`. For buckets on AWS Outposts, the storage class defaults to
`OUTPOSTS`.

For more information, see [Storage class
considerations with Amazon S3 transfers](create-s3-location.md#using-storage-classes "create-s3-location.md#using-storage-classes").

Type: String

Valid Values: `STANDARD | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | GLACIER | DEEP_ARCHIVE | OUTPOSTS | GLACIER_INSTANT_RETRIEVAL`

Required: No

**[Subdirectory](#API_UpdateLocationS3_RequestSyntax "#API_UpdateLocationS3_RequestSyntax")**

Specifies a prefix in the S3 bucket that DataSync reads from or writes to
(depending on whether the bucket is a source or destination location).

###### Note

DataSync can't transfer objects with a prefix that begins with a slash (`/`)
or includes `//`, `/./`, or `/../` patterns. For
example:

- `/photos`
- `photos//2006/January`
- `photos/./2006/February`
- `photos/../2006/March`

Type: String

Length Constraints: Maximum length of 4096.

Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]*$`

Required: No

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception is thrown when an error occurs in the AWS DataSync
service.

HTTP Status Code: 500

**InvalidRequestException**

This exception is thrown when the client submits a malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/UpdateLocationS3.md "../../../goto/cli2/datasync-2018-11-09/UpdateLocationS3.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateLocationS3.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateLocationS3.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationS3.md "../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationS3.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationS3.md "../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationS3.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationS3.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationS3.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationS3.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationS3.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationS3.md "../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationS3.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationS3.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationS3.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/UpdateLocationS3.md "../../../goto/boto3/datasync-2018-11-09/UpdateLocationS3.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationS3.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationS3.md")

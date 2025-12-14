# DescribeLocationS3

Provides details about how an AWS DataSync transfer location for an S3 bucket
is configured.

## Request Syntax

```
{
   "LocationArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[LocationArn](#API_DescribeLocationS3_RequestSyntax "#API_DescribeLocationS3_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the Amazon S3 location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

## Response Syntax

```
{
   "AgentArns": [ "***string***" ],
   "CreationTime": ***number***,
   "LocationArn": "***string***",
   "LocationUri": "***string***",
   "S3Config": {
      "BucketAccessRoleArn": "***string***"
   },
   "S3StorageClass": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AgentArns](#API_DescribeLocationS3_ResponseSyntax "#API_DescribeLocationS3_ResponseSyntax")**

The ARNs of the DataSync agents deployed on your Outpost when using working with
Amazon S3 on Outposts.

For more information, see [Deploy your DataSync agent
on AWS Outposts](deploy-agents.md#outposts-agent "deploy-agents.md#outposts-agent").

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 8 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

**[CreationTime](#API_DescribeLocationS3_ResponseSyntax "#API_DescribeLocationS3_ResponseSyntax")**

The time that the Amazon S3 location was created.

Type: Timestamp

**[LocationArn](#API_DescribeLocationS3_ResponseSyntax "#API_DescribeLocationS3_ResponseSyntax")**

The ARN of the Amazon S3 location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

**[LocationUri](#API_DescribeLocationS3_ResponseSyntax "#API_DescribeLocationS3_ResponseSyntax")**

The URL of the Amazon S3 location that was described.

Type: String

Length Constraints: Maximum length of 4360.

Pattern: `^(efs|nfs|s3|smb|hdfs|fsx[a-z0-9-]+)://[a-zA-Z0-9.:/\-]+$`

**[S3Config](#API_DescribeLocationS3_ResponseSyntax "#API_DescribeLocationS3_ResponseSyntax")**

Specifies the Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that DataSync uses to access your S3 bucket.

For more information, see [Providing
DataSync access to S3 buckets](create-s3-location.md#create-s3-location-access "create-s3-location.md#create-s3-location-access").

Type: [S3Config](API_S3Config.md "API_S3Config.md") object

**[S3StorageClass](#API_DescribeLocationS3_ResponseSyntax "#API_DescribeLocationS3_ResponseSyntax")**

When Amazon S3 is a destination location, this is the storage class that you chose
for your objects.

Some storage classes have behaviors that can affect your Amazon S3 storage costs.
For more information, see [Storage class
considerations with Amazon S3 transfers](create-s3-location.md#using-storage-classes "create-s3-location.md#using-storage-classes").

Type: String

Valid Values: `STANDARD | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | GLACIER | DEEP_ARCHIVE | OUTPOSTS | GLACIER_INSTANT_RETRIEVAL`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception is thrown when an error occurs in the AWS DataSync
service.

HTTP Status Code: 500

**InvalidRequestException**

This exception is thrown when the client submits a malformed request.

HTTP Status Code: 400

## Examples

### Example

The following example returns information about the Amazon S3 location
specified in the sample request.

#### Sample Request

```
{
  "LocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50s3"
}
```

### Example

This example illustrates one usage of DescribeLocationS3.

#### Sample Response

```
{
   "CreationTime": 1532660733.39,
   "LocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50s3",
   "LocationUri": "s3://amzn-s3-demo-bucket",
   "S3Config": {
      "BucketAccessRoleArn": "arn:aws:iam::111222333444:role/amzn-s3-demo-bucket-access-role",
   }
    "S3StorageClass": "STANDARD"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/DescribeLocationS3.md "../../../goto/cli2/datasync-2018-11-09/DescribeLocationS3.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeLocationS3.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeLocationS3.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationS3.md "../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationS3.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationS3.md "../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationS3.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationS3.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationS3.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationS3.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationS3.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationS3.md "../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationS3.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationS3.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationS3.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/DescribeLocationS3.md "../../../goto/boto3/datasync-2018-11-09/DescribeLocationS3.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationS3.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationS3.md")

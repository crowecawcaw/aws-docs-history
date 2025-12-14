# ReportDestinationS3

Specifies the Amazon S3 bucket where DataSync uploads your [task
report](task-reports.md "task-reports.md").

## Contents

**BucketAccessRoleArn**

Specifies the Amazon Resource Name (ARN) of the IAM policy that allows
DataSync to upload a task report to your S3 bucket. For more information, see
[Allowing
DataSync to upload a task report to an Amazon S3 bucket](task-reports.md "task-reports.md").

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$`

Required: Yes

**S3BucketArn**

Specifies the ARN of the S3 bucket where DataSync uploads your report.

Type: String

Length Constraints: Maximum length of 268.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):s3:[a-z\-0-9]*:[0-9]{12}:accesspoint[/:][a-zA-Z0-9\-.]{1,63}$|^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):s3-outposts:[a-z\-0-9]+:[0-9]{12}:outpost[/:][a-zA-Z0-9\-]{1,63}[/:]accesspoint[/:][a-zA-Z0-9\-]{1,63}$|^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):s3:::[a-zA-Z0-9.\-_]{1,255}$`

Required: Yes

**Subdirectory**

Specifies a bucket prefix for your report.

Type: String

Length Constraints: Maximum length of 4096.

Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]*$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/ReportDestinationS3.md "../../../goto/SdkForCpp/datasync-2018-11-09/ReportDestinationS3.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/ReportDestinationS3.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/ReportDestinationS3.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/ReportDestinationS3.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/ReportDestinationS3.md")

# `AWS-ConfigureS3BucketLogging`

**Description**

Enable logging on an Amazon Simple Storage Service (Amazon S3) bucket.

###### Important

Note the following important information regarding the Email Grantee ACL for
the Amazon S3 [PutBucketLogging](../../../AmazonS3/latest/API/API_PutBucketLogging.md "../../../AmazonS3/latest/API/API_PutBucketLogging.md")
API, which is used by this runbook:

End of support notice: Beginning October 1, 2025, Amazon S3 will discontinue
support for creating new Email Grantee Access Control Lists (ACL). Email Grantee
ACLs created prior to this date will continue to work and remain accessible
through the AWS Management Console, AWS CLI (CLI), SDKs, and REST API. However, you will no
longer be able to create new Email Grantee ACLs. Between July 15, 2025 and
October 1, 2025, you will begin to see an increasing rate of HTTP 405 errors for
requests to Amazon S3 when attempting to create new Email Grantee ACLs.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-ConfigureS3BucketLogging "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-ConfigureS3BucketLogging")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- BucketName

Type: String

Description: (Required) The name of the Amazon S3 Bucket for which you want to
configure logging.

- GrantedPermission

Type: String

Valid values: FULL_CONTROL | READ | WRITE

Description: (Required) Logging permissions assigned to the grantee for
the bucket.

- GranteeEmailAddress

Type: String

(Optional) Email address of the grantee.

- GranteeId

Type: String

Description: (Optional) The canonical user ID of the grantee.

- GranteeType

Type: String

Valid values: CanonicalUser | AmazonCustomerByEmail | Group

Description: (Required) Type of grantee.

- GranteeUri

Type: String

Description: (Optional) URI of the grantee group.

- TargetBucket

Type: String

Description: (Required) Specifies the bucket where you want Amazon S3 to store
server access logs. You can have your logs delivered to any bucket that you
own. You can also configure multiple buckets to deliver their logs to the
same target bucket. In this case you should choose a different TargetPrefix
for each source bucket so that the delivered log files can be distinguished
by key.

- TargetPrefix

Type: String

Default: /

Description: (Optional) Specifies a prefix for the keys under which the
log files will be stored.

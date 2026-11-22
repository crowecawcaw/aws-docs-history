

# `AWSSupportRemediator-EnableElbLogging`

**Description**

Enables access logging for an Elastic Load Balancing (ELB) Application Load Balancer or Classic Load Balancer.

The runbook writes access logs to an Amazon Simple Storage Service (Amazon S3) bucket that you identify by a tag key-value pair.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Application and Classic Load Balancers logging should be enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-5).

If the load balancer does not exist or access logging is already enabled, the automation completes successfully without making changes. The automation fails if no Amazon S3 bucket matches the provided tag key-value pair, or if more than one Amazon S3 bucket matches.

The target Amazon S3 bucket must be in the same AWS Region and AWS account as the load balancer. The bucket must have a bucket policy that grants ELB permission to write access logs.

Running this automation concurrently against the same load balancer with different parameter values can result in an unpredictable final configuration. Run the automation serially against any given load balancer.

To disable access logging after running this automation, modify the load balancer attributes to set access logging to disabled. Disabling access logging does not delete existing log objects from the destination Amazon S3 bucket. Delete them manually or configure an Amazon S3 Lifecycle rule to stop retaining log data and incurring storage charges.

Storing access logs incurs Amazon S3 storage costs. For more information about pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

**Important considerations**  
You are responsible for reviewing automation actions before they run.
This automation might cause stack drift if the resource is part of an AWS CloudFormation stack.
Access to `AWSSupportRemediator-*` runbooks requires an active Business Support\+, Enterprise Support, or Unified Operations Support plan. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ ElasticLoadBalancerArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the Application Load Balancer or Classic Load Balancer.
+ TargetBucketTagKey

  Type: String

  Description: (Required) The tag key (case-sensitive) used to identify the target Amazon S3 bucket. Use this along with `TargetBucketTagValue` to tag the bucket that serves as the destination bucket for access logs.
+ TargetBucketTagValue

  Type: String

  Description: (Required) The tag value (case-sensitive) used to identify the target Amazon S3 bucket. Use this along with `TargetBucketTagKey` to tag the bucket that serves as the destination bucket for access logs.
+ S3BucketPrefix

  Type: String

  Description: (Optional) The prefix (logical hierarchy) for the Amazon S3 bucket keys used to store access logs. The prefix that you specify must not include the string AWSLogs. For more information, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html).

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `elasticloadbalancing:DescribeLoadBalancerAttributes`
+ `elasticloadbalancing:ModifyLoadBalancerAttributes`
+ `tag:GetResources`

**Document Steps**

1. **retrieveTargetBucketName** - Identifies the Amazon S3 bucket tagged with the provided tag key-value pair to use as the access log destination.

1. **validateElb** - Validates whether the Application Load Balancer or Classic Load Balancer exists and determines whether access logging is already enabled.

1. **branchOnChangeRequired** - Branches on whether the automation needs to enable access logging on the load balancer.

1. **branchOnElbType** - Branches on whether the load balancer is an Application Load Balancer or a Classic Load Balancer.

1. **enableClbLogging** - Enables access logging on the Classic Load Balancer by updating its access log configuration to write to the target Amazon S3 bucket.

1. **enableAlbLogging** - Enables access logging on the Application Load Balancer by updating its attributes to write to the target Amazon S3 bucket.

**Outputs**
+ validateElb.InitialLoggingStatus: The access logging configuration of the load balancer before the automation runs.
+ validateElb.ChangeRequired: Whether a change is required to enable access logging on the load balancer.
+ validateElb.ValidationMessage: A message describing the validation result.
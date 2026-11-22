

# `AWSSupportRemediator-EnableEc2InstanceImdsv2`

**Description**

Enables [Instance Metadata Service Version 2 (IMDSv2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) on an Amazon Elastic Compute Cloud (Amazon EC2) instance by setting `HttpTokens` to `required`.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [EC2 instances should use Instance Metadata Service Version 2 (IMDSv2)](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-8).

If the Amazon EC2 instance does not exist, is terminated, already has IMDSv2 enabled, or has the instance metadata service HTTP endpoint disabled, the automation completes successfully without making changes.

Before enabling IMDSv2, the runbook inspects the Amazon CloudWatch `MetadataNoToken` metric for the specified check period to detect existing IMDSv1 usage. If the runbook detects any IMDSv1 requests during the check period, or if no metric data is available for the check period, the automation ends in a failed state. This safeguard avoids disrupting workloads that still depend on IMDSv1.

The `HttpPutResponseHopLimit` parameter controls the maximum number of network hops allowed for the instance metadata token. A hop limit of 1 restricts token access to processes running directly on the instance. A hop limit of 2 also allows access from containers running on the instance.

Note: Enabling IMDSv2 might disrupt services on instances that depend on IMDSv1, even if the runbook detected no IMDSv1 traffic during the analysis period. Confirm that all applications and scripts running on the instance are compatible with IMDSv2 before running this automation.

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
+ IMDSv1MetricCheckPeriod

  Type: Integer

  Description: (Required) The number of days (42-455) to analyze IMDSv1 usage metrics in CloudWatch. If the Amazon EC2 instance launched within the specified period, the analysis begins from the instance's launch time.
+ InstanceId

  Type: `AWS::EC2::Instance::Id`

  Description: (Required) The ID of the Amazon EC2 instance on which to enable IMDSv2.
+ HttpPutResponseHopLimit

  Type: Integer

  Description: (Optional) The maximum number of network hops allowed for the instance metadata token. A hop limit of 1 restricts token access to processes running directly on the instance. A hop limit of 2 also allows access from containers running on the instance.

  Default: 2

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `cloudwatch:GetMetricStatistics`
+ `ec2:DescribeInstances`
+ `ec2:ModifyInstanceMetadataOptions`

**Document Steps**

1. **validateInstance** - Validates that the Amazon EC2 instance exists and checks whether IMDSv2 is already enabled or the metadata HTTP endpoint is disabled. Inspects the CloudWatch `MetadataNoToken` metric for IMDSv1 usage during the requested check period. Fails the automation if the runbook detects any IMDSv1 requests or if no metric data is available.

1. **branchOnChangeRequired** - Branches on whether a change is required. Ends the automation successfully when no change is required; otherwise proceeds to handle the instance state.

1. **branchOnHandleInstanceState** - Branches on the current state of the Amazon EC2 instance. Transitional states (`pending`, `stopping`) wait for the instance to reach a stable state before enabling IMDSv2. Stable states (`running`, `stopped`) proceed directly to enabling IMDSv2.

1. **waitForRunningState** - Waits for the Amazon EC2 instance to reach the `running` state when the initial state is `pending`. The runbook enables IMDSv2 only after the instance reaches a stable state.

1. **waitForStoppedState** - Waits for the Amazon EC2 instance to reach the `stopped` state when the initial state is `stopping`. The runbook enables IMDSv2 only after the instance reaches a stable state.

1. **enableIMDSv2** - Enables IMDSv2 on the Amazon EC2 instance by calling `ModifyInstanceMetadataOptions` with `HttpTokens: required` and `HttpEndpoint: enabled`, using the requested `HttpPutResponseHopLimit`.

**Outputs**
+ validateInstance.ChangeRequired: Whether a change is required to enable IMDSv2 on the instance.
+ validateInstance.ValidationMessage: A message describing the validation result when no change is required.
+ validateInstance.IMDSEndpointInitiallyEnabled: Whether the instance metadata service HTTP endpoint was enabled on the instance before this automation ran.
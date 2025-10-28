# Enabling and configuring AWS Config for Security Hub CSPM

AWS Security Hub CSPM uses AWS Config rules to run security checks and generate findings for most controls.
AWS Config provides a detailed view of the configuration of AWS resources in your AWS account.
It uses rules to establish a baseline configuration for your resources and a configuration
recorder to detect whether a particular resource violates the conditions of a rule.

Some rules, referred to as AWS Config managed rules, are predefined and developed by AWS Config. Other
rules are custom AWS Config rules that Security Hub CSPM develops. AWS Config rules that Security Hub CSPM uses for controls are
referred to as _service-linked rules_. Service-linked rules allow
AWS services such as Security Hub CSPM to create AWS Config rules in your account.

To receive control findings in Security Hub CSPM, you must enable AWS Config for your account. You must also
turn on resource recording for the types of resources that enabled controls evaluate. Security Hub CSPM
can then create the appropriate AWS Config rules for the controls and begin to run security checks
and generate findings for the controls.

###### Topics

- [Considerations before enabling and configuring AWS Config](#securityhub-prereq-config "#securityhub-prereq-config")
- [Recording resources in AWS Config](#config-resource-recording "#config-resource-recording")
- [Ways to enable and configure AWS Config](#config-how-to-enable "#config-how-to-enable")
- [Understanding the Config.1 control](#config-1-overview "#config-1-overview")
- [Generating
  service-linked rules](#securityhub-standards-generate-awsconfigrules "#securityhub-standards-generate-awsconfigrules")
- [Cost considerations](#config-cost-considerations "#config-cost-considerations")

## Considerations before enabling and configuring AWS Config

To receive control findings in Security Hub CSPM, AWS Config must be enabled for your account in each
AWS Region where Security Hub CSPM is enabled. If you use Security Hub CSPM for a multi-account environment,
AWS Config must be enabled in each Region for the administrator account and all member
accounts.

We strongly recommend that you turn on resource recording in AWS Config _before_ you enable any Security Hub CSPM
standards and controls. This helps you ensure that your control findings are accurate.

To turn on resource recording in AWS Config, you must have sufficient permissions to record
resources in the AWS Identity and Access Management (IAM) role that's attached to the configuration recorder.
In addition, ensure that no IAM policies or AWS Organizations policies prevent AWS Config from having
permission to record your resources. Security Hub CSPM controls evaluate resource configurations
directly and don’t take AWS Organizations policies into account. For more information about AWS Config
recording, see [Working with the
configuration recorder](../../../config/latest/developerguide/stop-start-recorder.md "../../../config/latest/developerguide/stop-start-recorder.md") in the _AWS Config Developer Guide_.

If you enable a standard in Security Hub CSPM but haven't enabled AWS Config, Security Hub CSPM tries to create
service-linked AWS Config rules according to the following schedule:

- On the day that you enable the standard.
- The day after you enable the standard.
- 3 days after you enable the standard.
- 7 days after you enable the standard, and continuously every 7 days
  thereafter.

If you use central configuration, Security Hub CSPM also tries to create service-linked AWS Config rules
each time you associate a configuration policy that enables one or more standards with
accounts, organizational units (OUs), or the root.

## Recording resources in AWS Config

When you enable AWS Config, you must specify which AWS resources you want the AWS Config
configuration recorder to record. Through the service-linked rules, the configuration
recorder allows Security Hub CSPM to detect changes to your resource configurations.

For Security Hub CSPM to generate accurate control findings, you must turn on recording in AWS Config
for the types of resources that correspond to your enabled controls. It's primarily
enabled controls with a _change triggered_ schedule type that require
resource recording. Some controls with a _periodic_ schedule type
also require resource recording. For a list of these controls and their corresponding
resources, see [Required AWS Config resources for control
findings](controls-config-resources.md "controls-config-resources.md").

###### Warning

If you don't configure AWS Config recording correctly for Security Hub CSPM controls, it can result
in inaccurate control findings, particularly in the following instances:

- You never recorded the resource for a given control, or you disabled
  recording of a resource before creating that type of resource. In these
  cases, you receive a `WARNING` finding for the control at issue,
  even though you might have created resources in scope of the control after
  you disabled recording. This `WARNING` finding is a default
  finding that doesn't actually evaluate the configuration state of the
  resource.
- You disable recording for a resource that's evaluated by a particular
  control. In this case, Security Hub CSPM retains the control findings that were
  generated before you disabled recording, even though the control isn't
  evaluating new or updated resources. Security Hub CSPM also changes the compliance
  status of the findings to `WARNING`. These retained findings
  might not accurately reflect a resource's current configuration
  state.

By default, AWS Config records all supported _Regional resources_ that it
discovers in the AWS Region in which it is running. To receive all Security Hub CSPM control
findings, you must also configure AWS Config to record _global resources_.
To conserve costs, we recommend recording global resources in a single Region only. If
you use central configuration or cross-Region aggregation, this Region should be your
home Region.

In AWS Config, you can choose between _continuous recording_ and
_daily recording_ of changes in resource state. If you choose
daily recording, AWS Config delivers resource configuration data at the end of each
24–hour period if there are changes in resource state. If there are no changes,
no data is delivered. This can delay the generation of Security Hub CSPM findings for
change-triggered controls until a 24–hour period is complete.

For more information about AWS Config recording, see [Recording AWS resources](../../../config/latest/developerguide/select-resources.md "../../../config/latest/developerguide/select-resources.md") in the _AWS Config Developer Guide_.

## Ways to enable and configure AWS Config

You can enable AWS Config and turn on resource recording in any of the following ways:

- **AWS Config console** – You can
  enable AWS Config for an account by using the AWS Config console. For instructions, see [Setting up AWS Config with the console](../../../config/latest/developerguide/gs-console.md "../../../config/latest/developerguide/gs-console.md") in the _AWS Config Developer Guide_.
- **AWS CLI or SDKs** – You can
  enable AWS Config for an account by using the AWS Command Line Interface (AWS CLI). For instructions, see [Setting up AWS Config with the AWS CLI](../../../config/latest/developerguide/gs-cli.md "../../../config/latest/developerguide/gs-cli.md") in the _AWS Config Developer Guide_. AWS software development kits (SDKs)
  are also available for many programming languages.
- **CloudFormation template** – To enable AWS Config for
  many accounts, we recommend using the AWS CloudFormation template named **Enable
  AWS Config**. To access this template, see [AWS CloudFormation StackSet sample templates](../../../AWSCloudFormation/latest/UserGuide/stacksets-sampletemplates.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-sampletemplates.md") in the
  _AWS CloudFormation User Guide_.

By default, this template excludes recording for IAM global resources. Ensure
that you turn on recording for IAM global resources in only one AWS Region
to conserve recording costs. If you have cross-Region aggregation enabled, this
should be your [Security Hub CSPM home Region](finding-aggregation.md "finding-aggregation.md").
Otherwise, it can be any Region that Security Hub CSPM is available in that supports
recording of IAM global resources. We recommend running one StackSet to record
all resources, including IAM global resources, in the home Region or other
selected Region. Then, run a second StackSet to record all resources except
IAM global resources in other Regions.

- **GitHub script** – Security Hub CSPM offers a [GitHub
  script](https://github.com/awslabs/aws-securityhub-multiaccount-scripts "https://github.com/awslabs/aws-securityhub-multiaccount-scripts") that enables Security Hub CSPM and AWS Config for multiple accounts across
  Regions. This script is useful if you haven't integrated with AWS Organizations, or you
  have some member accounts that aren't part of an organization.

For more information, see the following blog post on the _AWS
Security blog_: [Optimize AWS Config for AWS Security Hub CSPM to effectively manage your cloud security
posture](https://aws.amazon.com/blogs/security/optimize-aws-config-for-aws-security-hub-to-effectively-manage-your-cloud-security-posture/ "https://aws.amazon.com/blogs/security/optimize-aws-config-for-aws-security-hub-to-effectively-manage-your-cloud-security-posture/").

## Understanding the Config.1 control

In Security Hub CSPM, the [Config.1](config-controls.md#config-1 "config-controls.md#config-1") control generates
`FAILED` findings in your account if AWS Config is disabled. It also generates
`FAILED` findings in your account if AWS Config is enabled but resource
recording isn't turned on.

If AWS Config is enabled and resource recording is turned on, but resource recording isn't
turned on for a type of resource that an enabled control checks, Security Hub CSPM generates a
`FAILED` finding for the Config.1 control. In addition to this
`FAILED` finding, Security Hub CSPM generates `WARNING` findings for the
enabled control and the types of resources that the control checks. For example, if you
enable the [KMS.5](kms-controls.md#kms-5 "kms-controls.md#kms-5") control and resource recording isn't
turned on for AWS KMS keys, Security Hub CSPM generates a `FAILED` finding for the
Config.1 control. Security Hub CSPM also generates `WARNING` findings for the KMS.5
control and your KMS keys.

To receive a `PASSED` finding for the Config.1 control, turn on resource
recording for all the resource types that correspond to enabled controls. Also disable
controls that aren't required for your organization. This helps ensure that you don't
have configuration gaps in your security control checks. It also helps ensure that you
receive accurate findings about misconfigured resources.

If you're the delegated Security Hub CSPM administrator for an organization,
AWS Config recording must be configured correctly for your account and your member accounts.
If you use cross-Region aggregation, AWS Config recording must be configured correctly in the
home Region and all linked Regions. Global resources do not need to be recorded in
linked Regions.

## Generating

service-linked rules

For every control that uses a service-linked AWS Config rule, Security Hub CSPM creates instances of
the required rule in your AWS environment.

These service-linked rules are specific to Security Hub CSPM. Security Hub CSPM creates these
service-linked rules even if other instances of the same rules already exist. The
service-linked rule adds `securityhub` before the original rule name and a
unique identifier after the rule name. For example, for the AWS Config managed rule
`vpc-flow-logs-enabled`, the service-linked rule name might be
`securityhub-vpc-flow-logs-enabled-12345`.

There are quotas for the number of AWS Config managed rules that can be used to evaluate
controls. AWS Config rules that Security Hub CSPM creates don't count towards those quotas. You can enable
a security standard even if you've already reached the AWS Config quota for managed rules in
your account. To learn more about quotas for AWS Config rules, see [Service limits for AWS Config](../../../config/latest/developerguide/configlimits.md "../../../config/latest/developerguide/configlimits.md")
in the _AWS Config Developer Guide_.

## Cost considerations

Security Hub CSPM can impact your AWS Config configuration recorder costs by updating the
`AWS::Config::ResourceCompliance` configuration item. Updates can
occur each time a Security Hub CSPM control associated with an AWS Config rule changes compliance
state, is enabled or disabled, or has parameter updates. If you use the AWS Config configuration recorder only for
Security Hub CSPM, and don't use this configuration item for other purposes, we recommend
turning off recording for it in AWS Config. This can reduce your AWS Config
costs. You don't need to record `AWS::Config::ResourceCompliance` for security
checks to work in Security Hub CSPM.

For information about the costs associated with resource recording, see [AWS Security Hub CSPM pricing](https://aws.amazon.com/security-hub/pricing/ "https://aws.amazon.com/security-hub/pricing/") and
[AWS Config pricing](https://aws.amazon.com/config/pricing/ "https://aws.amazon.com/config/pricing/").

# Security Hub CSPM controls for Amazon EC2 Auto Scaling

These Security Hub CSPM controls evaluate the Amazon EC2 Auto Scaling service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [AutoScaling.1] Amazon EC2 Auto Scaling groups associated with a load balancer should use ELB health checks

**Related requirements:** PCI DSS v3.2.1/2.2, NIST.800-53.r5 CA-7, NIST.800-53.r5 CP-2(2), NIST.800-53.r5 SI-2

**Category:** Identify > Inventory

**Severity:** Low

**Resource type:**
`AWS::AutoScaling::AutoScalingGroup`

**AWS Config rule:**
[`autoscaling-group-elb-healthcheck-required`](../../../config/latest/developerguide/autoscaling-group-elb-healthcheck-required.md "../../../config/latest/developerguide/autoscaling-group-elb-healthcheck-required.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon EC2 Amazon EC2 Auto Scaling group that is associated with a load balancer
uses ELB (ELB) health checks. The control fails if the Amazon EC2 Auto Scaling group doesn't use ELB health checks.

ELB health checks help ensure that an Amazon EC2 Auto Scaling group can determine an instance's health based on additional tests
provided by the load balancer. Using ELB health checks also helps support the availability of
applications that use EC2 Amazon EC2 Auto Scaling groups.

### Remediation

To add ELB health checks, see [Add ELB health checks](../../../autoscaling/ec2/userguide/as-add-elb-healthcheck.md#as-add-elb-healthcheck-console "../../../autoscaling/ec2/userguide/as-add-elb-healthcheck.md#as-add-elb-healthcheck-console") in the _Amazon EC2 Auto Scaling User Guide_.

## [AutoScaling.2] Amazon EC2 Auto Scaling group should cover multiple Availability Zones

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-2(2), NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::AutoScaling::AutoScalingGroup`

**AWS Config rule:**
[`autoscaling-multiple-az`](../../../config/latest/developerguide/autoscaling-multiple-az.md "../../../config/latest/developerguide/autoscaling-multiple-az.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter              | Description                          | Type | Allowed custom values | Security Hub CSPM default value |
| ---------------------- | ------------------------------------ | ---- | --------------------- | ------------------------------- |
| `minAvailabilityZones` | Minimum number of Availability Zones | Enum | `2, 3, 4, 5, 6`       | `2`                             |

This control checks whether an Amazon EC2 Auto Scaling group spans at least the specified number of Availability Zones (AZs). The
control fails if an Amazon EC2 Auto Scaling group doesn't span at least the specified number of AZs. Unless you provide a custom parameter
value for the minimum number of AZs, Security Hub CSPM uses a default value of two AZs.

An Amazon EC2 Auto Scaling group that doesn't span multiple AZs can't launch instances in another AZ to compensate if the configured single
AZ becomes unavailable. However, an Amazon EC2 Auto Scaling group with a single Availability Zone may be preferred in some use cases, such as batch
jobs or when inter-AZ transfer costs need to be kept to a minimum. In such cases, you can disable this control or suppress its findings.

### Remediation

To add AZs to an existing Amazon EC2 Auto Scaling group, see [Add and remove Availability Zones](../../../autoscaling/ec2/userguide/as-add-availability-zone.md "../../../autoscaling/ec2/userguide/as-add-availability-zone.md") in the _Amazon EC2 Auto Scaling User Guide_.

## [AutoScaling.3] Amazon EC2 Auto Scaling group launch configurations should configure EC2 instances to require Instance Metadata Service Version 2 (IMDSv2)

**Related requirements:** NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-6, NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, PCI DSS v4.0.1/2.2.6

**Category:** Protect > Secure network configuration

**Severity:** High

**Resource type:**
`AWS::AutoScaling::LaunchConfiguration`

**AWS Config rule:**
[`autoscaling-launchconfig-requires-imdsv2`](../../../config/latest/developerguide/autoscaling-launchconfig-requires-imdsv2.md "../../../config/latest/developerguide/autoscaling-launchconfig-requires-imdsv2.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether IMDSv2 is enabled on all instances launched by Amazon EC2 Amazon EC2 Auto Scaling
groups. The control fails if the Instance Metadata Service (IMDS) version isn't
included in the launch configuration or is configured as `token optional`, which is a setting
that allows either IMDSv1 or IMDSv2.

IMDS provides data about your instance that you can use to configure or manage the running instance.

Version 2 of the IMDS adds new protections that weren't available in IMDSv1 to further safeguard your EC2 instances.

### Remediation

An Amazon EC2 Auto Scaling group is associated with one launch configuration at a time. You cannot modify a
launch configuration after you create it. To change the launch configuration for
an Amazon EC2 Auto Scaling group, use an existing launch configuration as the basis for a new
launch configuration with IMDSv2 enabled. For more information, see [Configure instance metadata options for new instances](../../../AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.md "../../../AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.md") in the _Amazon EC2 User Guide_.

## [AutoScaling.4] Amazon EC2 Auto Scaling group launch configuration should not have a metadata response hop limit greater than 1

###### Important

Security Hub CSPM retired this control in April 2024.
For more information, see [Change log for Security Hub CSPM controls](controls-change-log.md "controls-change-log.md").

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2)

**Category:** Protect > Secure network configuration

**Severity:** High

**Resource type:**
`AWS::AutoScaling::LaunchConfiguration`

**AWS Config rule:**
[`autoscaling-launch-config-hop-limit`](../../../config/latest/developerguide/autoscaling-launch-config-hop-limit.md "../../../config/latest/developerguide/autoscaling-launch-config-hop-limit.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks the number of network hops that a metadata token can travel. The control fails if the metadata response hop limit is greater than `1`.

The Instance Metadata Service (IMDS) provides metadata information about an Amazon EC2 instance and is useful for application configuration.
Restricting the HTTP `PUT` response for the metadata service to only the EC2 instance protects the IMDS from unauthorized use.

The Time To Live (TTL) field in the IP packet is reduced by one on every hop. This reduction can be used to ensure that the packet
does not travel outside EC2. IMDSv2 protects EC2 instances that may have been misconfigured as open routers, layer 3 firewalls, VPNs, tunnels, or NAT
devices, which prevents unauthorized users from retrieving metadata. With IMDSv2, the `PUT` response that contains the secret token cannot travel outside
the instance because the default metadata response hop limit is set to `1`. However, if this value is greater than `1`, the token can leave the EC2 instance.

### Remediation

To modify the metadata response hop limit for an existing launch configuration, see [Modify instance metadata options for existing instances](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-options.md#configuring-IMDS-existing-instances "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-options.md#configuring-IMDS-existing-instances") in the _Amazon EC2 User Guide_.

## [Autoscaling.5] Amazon EC2 instances launched using Amazon EC2 Auto Scaling group launch configurations should not have Public IP addresses

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9), PCI DSS v4.0.1/1.4.4

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** High

**Resource type:**
`AWS::AutoScaling::LaunchConfiguration`

**AWS Config rule:**
[`autoscaling-launch-config-public-ip-disabled`](../../../config/latest/developerguide/autoscaling-launch-config-public-ip-disabled.md "../../../config/latest/developerguide/autoscaling-launch-config-public-ip-disabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon EC2 Auto Scaling group's associated launch configuration assigns a
[public IP address](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#public-ip-addresses "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#public-ip-addresses") to the group's instances. The control fails if the
associated launch configuration assigns a public IP address.

Amazon EC2 instances in an Amazon EC2 Auto Scaling group launch configuration should not have an associated public
IP address, except for in limited edge cases. Amazon EC2 instances should only be
accessible from behind a load balancer instead of being directly exposed to the
internet.

### Remediation

An Amazon EC2 Auto Scaling group is associated with one launch configuration at a time. You cannot modify a launch configuration after you create it. To change the launch configuration for an Amazon EC2 Auto Scaling group, use an existing launch configuration as the basis for a new launch configuration. Then, update the Amazon EC2 Auto Scaling group to use the new launch configuration.
For step-by-step instructions, see [Change the launch configuration for an Amazon EC2 Auto Scaling group](../../../autoscaling/ec2/userguide/change-launch-config.md "../../../autoscaling/ec2/userguide/change-launch-config.md") in
the _Amazon EC2 Auto Scaling User Guide_. When creating the new launch configuration, under **Additional configuration**, for **Advanced details, IP address type**, choose **Do not assign a public IP address to any instances**.

After you change the launch configuration, Amazon EC2 Auto Scaling launches new instances with the new configuration options. Existing instances aren't affected. To update an existing instance, we recommend that you refresh your instance, or allow automatic scaling to gradually replace older instances with newer instances based on your termination policies.
For more information about updating Amazon EC2 Auto Scaling instances, see [Update Amazon EC2 Auto Scaling instances](../../../autoscaling/ec2/userguide/update-auto-scaling-group.md#update-auto-scaling-instances "../../../autoscaling/ec2/userguide/update-auto-scaling-group.md#update-auto-scaling-instances") in the _Amazon EC2 Auto Scaling User Guide_.

## [AutoScaling.6] Amazon EC2 Auto Scaling groups should use multiple instance types in multiple Availability Zones

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-2(2), NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::AutoScaling::AutoScalingGroup`

**AWS Config rule:**
[`autoscaling-multiple-instance-types`](../../../config/latest/developerguide/autoscaling-multiple-instance-types.md "../../../config/latest/developerguide/autoscaling-multiple-instance-types.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon EC2 Amazon EC2 Auto Scaling group uses multiple instance types. The control fails if the Amazon EC2 Auto Scaling group has only one instance type defined.

You can enhance availability by deploying your application across multiple instance types running in multiple Availability Zones. Security Hub CSPM
recommends using multiple instance types so that the Amazon EC2 Auto Scaling group can launch another instance type if there is insufficient instance capacity in your chosen Availability Zones.

### Remediation

To create an Amazon EC2 Auto Scaling group with multiple instance types, see [Amazon EC2 Auto Scaling groups with multiple instance types and purchase options](../../../autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.md") in
the _Amazon EC2 Auto Scaling User Guide_.

## [AutoScaling.9] Amazon EC2 Auto Scaling groups should use Amazon EC2 launch templates

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2)

**Category:** Identify > Resource Configuration

**Severity:** Medium

**Resource type:**
`AWS::AutoScaling::AutoScalingGroup`

**AWS Config rule:**
[`autoscaling-launch-template`](../../../config/latest/developerguide/autoscaling-launch-template.md "../../../config/latest/developerguide/autoscaling-launch-template.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon EC2 Amazon EC2 Auto Scaling group is created from an EC2 launch template. This control
fails if an Amazon EC2 Amazon EC2 Auto Scaling group is not created with a launch template or if a launch template is not specified in a mixed instances policy.

An EC2 Amazon EC2 Auto Scaling group can be created from either an EC2 launch template or a launch configuration.
However, using a launch template to create an Amazon EC2 Auto Scaling group ensures that you have access to the latest features and improvements.

### Remediation

To create an Amazon EC2 Auto Scaling group with an EC2 launch template, see [Create an Amazon EC2 Auto Scaling group using a launch template](../../../autoscaling/ec2/userguide/create-asg-launch-template.md "../../../autoscaling/ec2/userguide/create-asg-launch-template.md") in the _Amazon EC2 Auto Scaling User Guide_.
For information about how to replace a launch configuration with a launch template, see [Replace a launch configuration with a launch template](../../../autoscaling/ec2/userguide/replace-launch-config.md "../../../autoscaling/ec2/userguide/replace-launch-config.md") in the _Amazon EC2 User Guide_.

## [AutoScaling.10] EC2 Amazon EC2 Auto Scaling groups should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::AutoScaling::AutoScalingGroup`

**AWS Config rule:** `tagged-autoscaling-autoscalinggroup` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

This control checks whether an Amazon EC2 Auto Scaling group has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the Amazon EC2 Auto Scaling group doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the Amazon EC2 Auto Scaling group isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_AWS General Reference_.

### Remediation

To add tags to an Amazon EC2 Auto Scaling group, see [Tag Amazon EC2 Auto Scaling groups and instances](../../../autoscaling/ec2/userguide/ec2-auto-scaling-tagging.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-tagging.md") in the _Amazon EC2 Auto Scaling User Guide_.

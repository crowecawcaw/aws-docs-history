# Security Hub CSPM controls for AWS Network Firewall

These AWS Security Hub CSPM controls evaluate the AWS Network Firewall service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [NetworkFirewall.1] Network Firewall firewalls should be deployed across multiple Availability Zones

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36,
NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::NetworkFirewall::Firewall`

**AWS Config rule:**
[netfw-multi-az-enabled](../../../config/latest/developerguide/netfw-multi-az-enabled.md "../../../config/latest/developerguide/netfw-multi-az-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control evaluates whether a firewall managed through AWS Network Firewall is deployed across multiple Availability Zones (AZs).
The control fails if a firewall is deployed in only one AZ.

AWS global infrastructure includes multiple AWS Regions. AZs are physically separated, isolated
locations within each Region that are connected by low-latency, high-throughput, and highly
redundant networking. By deploying a Network Firewall firewall across multiple AZs, you can balance and shift traffic among AZs,
which helps you design highly available solutions.

### Remediation

**Deploying a Network Firewall firewall across multiple AZs**

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewalls**.
3. On the **Firewalls** page, select the firewall that you want to edit.
4. On the firewall details page, choose the **Firewall details** tab.
5. In the **Associated policy and VPC** section, choose **Edit**
6. To add a new AZ, choose **Add New Subnet**. Select the AZ and subnet that you would like to use. Ensure that you select at least two AZs.
7. Choose **Save**.

## [NetworkFirewall.2] Network Firewall logging should be enabled

**Related requirements:** NIST.800-53.r5 AC-2(12),
NIST.800-53.r5 AC-2(4), NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AC-6(9), NIST.800-53.r5
AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5
AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 AU-9(7), NIST.800-53.r5 CA-7,
NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-3(8), NIST.800-53.r5 SI-4, NIST.800-53.r5
SI-4(20), NIST.800-53.r5 SI-7(8), NIST.800-171.r2 3.1.20, NIST.800-171.r2 3.13.1

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::NetworkFirewall::LoggingConfiguration`

**AWS Config rule:**
[netfw-logging-enabled](../../../config/latest/developerguide/netfw-logging-enabled.md "../../../config/latest/developerguide/netfw-logging-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether logging is enabled for an AWS Network Firewall firewall. The control fails if logging isn't
enabled for at least one log type or if the logging destination doesn't exist.

Logging helps you maintain the reliability, availability, and performance of your firewalls. In Network Firewall, logging
gives you detailed information about network traffic, including the time that the stateful engine received a packet
flow, detailed information about the packet flow, and any stateful rule action taken against the packet flow.

### Remediation

To enable logging for a firewall, see [Updating a firewall's logging configuration](../../../network-firewall/latest/developerguide/firewall-update-logging-configuration.md "../../../network-firewall/latest/developerguide/firewall-update-logging-configuration.md")
in the _AWS Network Firewall Developer Guide_.

## [NetworkFirewall.3] Network Firewall policies should have at least one rule group associated

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-2, NIST.800-171.r2 3.1.3, NIST.800-171.r2 3.13.1

**Category:** Protect > Secure Network Configuration

**Severity:** Medium

**Resource type:**
`AWS::NetworkFirewall::FirewallPolicy`

**AWS Config rule:**
[netfw-policy-rule-group-associated](../../../config/latest/developerguide/netfw-policy-rule-group-associated.md "../../../config/latest/developerguide/netfw-policy-rule-group-associated.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a Network Firewall policy has any stateful or stateless rule groups associated. The control fails if stateless or
stateful rule groups are not assigned.

A firewall policy defines how your firewall monitors and handles traffic in Amazon Virtual Private Cloud
(Amazon VPC). Configuration of stateless and stateful rule groups helps to filter packets
and traffic flows, and defines default traffic handling.

### Remediation

To add a rule group to a Network Firewall policy, see [Updating a firewall policy](../../../network-firewall/latest/developerguide/firewall-policy-updating.md "../../../network-firewall/latest/developerguide/firewall-policy-updating.md") in the _AWS Network Firewall Developer Guide_.
For information about creating and managing rule groups, see [Rule groups in AWS Network Firewall](../../../network-firewall/latest/developerguide/rule-groups.md "../../../network-firewall/latest/developerguide/rule-groups.md").

## [NetworkFirewall.4] The default stateless action for Network Firewall policies should be drop or forward for full packets

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2

**Category:** Protect > Secure Network Configuration

**Severity:** Medium

**Resource type:**
`AWS::NetworkFirewall::FirewallPolicy`

**AWS Config rule:**
[netfw-policy-default-action-full-packets](../../../config/latest/developerguide/netfw-policy-default-action-full-packets.md "../../../config/latest/developerguide/netfw-policy-default-action-full-packets.md")

**Schedule type:** Change triggered

**Parameters:**

- `statelessDefaultActions: aws:drop,aws:forward_to_sfe` (not customizable)

This control checks whether the default stateless action for full packets for a Network Firewall policy is drop or forward. The control passes if `Drop`
or `Forward` is selected, and fails if `Pass` is selected.

A firewall policy defines how your firewall monitors and handles traffic in Amazon VPC. You
configure stateless and stateful rule groups to filter packets and traffic flows.
Defaulting to `Pass` can allow unintended traffic.

### Remediation

To change your firewall policy, see [Updating a firewall policy](../../../network-firewall/latest/developerguide/firewall-policy-updating.md "../../../network-firewall/latest/developerguide/firewall-policy-updating.md") in the _AWS Network Firewall Developer Guide_.
For **Stateless default actions**, choose **Edit**. Then, choose **Drop** or **Forward to stateful rule groups**
as the **Action**.

## [NetworkFirewall.5] The default stateless action for Network Firewall policies should be drop or forward for fragmented packets

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5
CM-2, NIST.800-171.r2 3.1.3, NIST.800-171.r2 3.1.14, NIST.800-171.r2 3.13.1,
NIST.800-171.r2 3.13.6

**Category:** Protect > Secure Network Configuration

**Severity:** Medium

**Resource type:**
`AWS::NetworkFirewall::FirewallPolicy`

**AWS Config rule:**
[netfw-policy-default-action-fragment-packets](../../../config/latest/developerguide/netfw-policy-default-action-fragment-packets.md "../../../config/latest/developerguide/netfw-policy-default-action-fragment-packets.md")

**Schedule type:** Change triggered

**Parameters:**

- `statelessFragDefaultActions (Required) : aws:drop, aws:forward_to_sfe` (not customizable)

This control checks whether the default stateless action for fragmented packets for a
Network Firewall policy is drop or forward. The control passes if `Drop` or
`Forward` is selected, and fails if `Pass` is
selected.

A firewall policy defines how your firewall monitors and handles traffic in Amazon VPC. You
configure stateless and stateful rule groups to filter packets and traffic flows.
Defaulting to `Pass` can allow unintended traffic.

### Remediation

To change your firewall policy, see [Updating a firewall policy](../../../network-firewall/latest/developerguide/firewall-policy-updating.md "../../../network-firewall/latest/developerguide/firewall-policy-updating.md") in the _AWS Network Firewall Developer Guide_.
For **Stateless default actions**, choose **Edit**. Then, choose **Drop** or **Forward to stateful rule groups**
as the **Action**.

## [NetworkFirewall.6] Stateless Network Firewall rule group should not be empty

**Related requirements:** NIST.800-53.r5 AC-4(21),
NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5
SC-7(21), NIST.800-53.r5 SC-7(5), NIST.800-171.r2 3.1.3, NIST.800-171.r2 3.1.14,
NIST.800-171.r2 3.13.1, NIST.800-171.r2 3.13.6

**Category:** Protect > Secure Network Configuration

**Severity:** Medium

**Resource type:**
`AWS::NetworkFirewall::RuleGroup`

**AWS Config rule:**
[netfw-stateless-rule-group-not-empty](../../../config/latest/developerguide/netfw-stateless-rule-group-not-empty.md "../../../config/latest/developerguide/netfw-stateless-rule-group-not-empty.md")

**Schedule type:** Change triggered

**Parameters:**
None

This control checks if a stateless rule group in AWS Network Firewall contains rules. The control fails if there are no rules in the rule group.

A rule group contains rules that define how your firewall processes traffic in your VPC. An empty stateless rule group, when present in a firewall policy, might give the impression that the rule group will process traffic. However, when the stateless rule group is empty, it does not process traffic.

### Remediation

To add rules to your Network Firewall rule group, see [Updating a stateful rule group](../../../network-firewall/latest/developerguide/rule-group-stateful-updating.md "../../../network-firewall/latest/developerguide/rule-group-stateful-updating.md") in the _AWS Network Firewall Developer Guide_.
On the firewall details page, for **Stateless rule group**, choose **Edit** to
add rules.

## [NetworkFirewall.7] Network Firewall firewalls should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::NetworkFirewall::Firewall`

**AWS Config rule:** `tagged-networkfirewall-firewall` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`              |

This control checks whether an AWS Network Firewall firewall has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the firewall doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the firewall isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
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

To add tags to an Network Firewall firewall, see [Tagging AWS Network Firewall resources](../../../network-firewall/latest/developerguide/tagging.md "../../../network-firewall/latest/developerguide/tagging.md") in the _AWS Network Firewall Developer Guide_.

## [NetworkFirewall.8] Network Firewall firewall policies should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::NetworkFirewall::FirewallPolicy`

**AWS Config rule:** `tagged-networkfirewall-firewallpolicy` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`              |

This control checks whether an AWS Network Firewall firewall policy has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the firewall policy doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the firewall policy isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
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

To add tags to an Network Firewall policy, see [Tagging AWS Network Firewall resources](../../../network-firewall/latest/developerguide/tagging.md "../../../network-firewall/latest/developerguide/tagging.md") in the _AWS Network Firewall Developer Guide_.

## [NetworkFirewall.9] Network Firewall firewalls should have deletion protection enabled

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-2,
NIST.800-53.r5 CM-2(2),
NIST.800-53.r5 CM-3,
NIST.800-53.r5 SC-5(2)

**Category:** Protect > Network Security

**Severity:** Medium

**Resource type:**
`AWS::NetworkFirewall::Firewall`

**AWS Config rule:**
[netfw-deletion-protection-enabled](../../../config/latest/developerguide/netfw-deletion-protection-enabled.md "../../../config/latest/developerguide/netfw-deletion-protection-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS Network Firewall firewall has deletion protection enabled. The control fails if deletion
protection isn't enabled for a firewall.

AWS Network Firewall is a stateful, managed network firewall and intrusion detection service that enables you to inspect and
filter traffic to, from, or between your Virtual Private Clouds (VPCs). The deletion protection setting protects against accidental
deletion of the firewall.

### Remediation

To enable delete protection on an existing Network Firewall firewall, see [Updating a firewall](../../../network-firewall/latest/developerguide/firewall-updating.md "../../../network-firewall/latest/developerguide/firewall-updating.md") in the _AWS Network Firewall Developer Guide_.
For **Change protections**, select **Enable**. You can also
enable deletion protection by invoking the [UpdateFirewallDeleteProtection](../../../network-firewall/latest/APIReference/API_UpdateFirewallDeleteProtection.md "../../../network-firewall/latest/APIReference/API_UpdateFirewallDeleteProtection.md") API and setting the `DeleteProtection` field to `true`.

## [NetworkFirewall.10] Network Firewall firewalls should have subnet change

protection enabled

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2), NIST.800-53.r5 CM-3, NIST.800-53.r5
SC-5(2)

**Category:** Protect > Network Security

**Severity:** Medium

**Resource type:**
`AWS::NetworkFirewall::Firewall`

**AWS Config rule:**
[netfw-subnet-change-protection-enabled](../../../config/latest/developerguide/netfw-subnet-change-protection-enabled.md "../../../config/latest/developerguide/netfw-subnet-change-protection-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether subnet change protection is enabled for an AWS Network Firewall
firewall. The control fails if subnet change protection isn't enabled for the
firewall.

AWS Network Firewall is a stateful, managed network firewall and intrusion detection service
that you can use to inspect and filter traffic to, from, or between your Virtual Private
Clouds (VPCs). If you enable subnet change protection for a Network Firewall firewall, you can
protect the firewall against accidental changes to the firewall's subnet
associations.

### Remediation

For information about enabling subnet change protection for an existing Network Firewall
firewall, see [Updating a
firewall](../../../network-firewall/latest/developerguide/firewall-updating.md "../../../network-firewall/latest/developerguide/firewall-updating.md") in the _AWS Network Firewall Developer Guide_.

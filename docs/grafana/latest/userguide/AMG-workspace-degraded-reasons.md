

# Troubleshoot degraded workspaces in Amazon Managed Grafana
<a name="AMG-workspace-degraded-reasons"></a>

An Amazon Managed Grafana workspace can enter a degraded state for several reasons, including VPC configuration issues and KMS key problems. When a workspace is degraded, you may experience availability loss, inability to make configuration changes, and missed security updates. The following sections describe each degraded reason and the actions you can take to resolve it.

## KMS key disabled (not recoverable)
<a name="degraded-kms-key-failed"></a>

Your workspace has failed and cannot be recovered because the KMS key used in the workspace has been disabled for more than 7 days, or the KMS grant has been revoked.

You will experience the following issues:
+ A complete availability loss for the workspace, resulting in non-functioning alerts and inaccessible dashboards
+ Inability to make configuration changes to your workspace
+ Your workspace will not be able to receive security updates or patches
+ All workspace data is permanently lost and cannot be recovered

**To resolve this issue:**

This workspace cannot be recovered. You must create a new workspace. For more information about encryption at rest, see [Encryption at rest](AMG-encryption-at-rest.md). For best practices on managing KMS keys, see [Best practices for AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html) in the *AWS KMS Developer Guide*.

## KMS key disabled (recoverable)
<a name="degraded-kms-key-disabled"></a>

Your workspace is disabled and non-operational because the KMS key used for customer managed key encryption has been disabled.

Until you take action, you will experience the following issues:
+ A complete availability loss for the workspace, resulting in non-functioning alerts and inaccessible dashboards
+ Inability to make configuration changes to your workspace
+ Your workspace will not be able to receive security updates or patches

**To resolve this issue:**

Re-enable the KMS key and restore Amazon Managed Grafana access in the key policy. For more information, see [Enabling and disabling keys](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html) in the *AWS KMS Developer Guide*.

**Important**  
You must re-enable the KMS key within 7 days. After this period, the workspace transitions to a `FAILED` state and cannot be recovered.  
If you revoke KMS grants created by Amazon Managed Grafana to access your KMS key, the grants cannot be recreated, and the data in the workspace is lost permanently. For more information about grants, see [Grants in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) in the *AWS KMS Developer Guide*.

## Deleted security group
<a name="degraded-broken-security-group"></a>

Your workspace is disabled and non-operational because a security group associated with the workspace VPC configuration has been deleted.

Until you take action, you will experience the following issues:
+ A complete availability loss for the workspace, resulting in non-functioning alerts and inaccessible dashboards
+ Inability to make configuration changes to your workspace
+ Your workspace will not be able to receive security updates or patches

**To resolve this issue:**

1. Open the Amazon Managed Grafana console and select your workspace.

1. Update the security groups to valid security groups under the **Outbound VPC connection** setting.

1. Confirm the change and retry the VPC connection.

To avoid this issue in the future, update the security groups in your Amazon Managed Grafana console before deleting them from their VPC.

## Deleted subnet
<a name="degraded-broken-subnet"></a>

Your workspace is disabled and non-operational because a subnet has been deleted from your Elastic Network Interface (ENI).

Until you take action, you will experience the following issues:
+ A complete availability loss for the workspace, resulting in non-functioning alerts and inaccessible dashboards
+ Inability to make configuration changes to your workspace
+ Your workspace will not be able to receive security updates or patches

**To resolve this issue:**

1. Open the Amazon Managed Grafana console and select your workspace.

1. Update the subnets to valid subnets under the **Outbound VPC connection** setting.

1. Confirm the change and retry the VPC connection.

To avoid this issue in the future, update the subnets in your Amazon Managed Grafana console before deleting them from their VPC.

## IP address exhaustion
<a name="degraded-ip-exhaustion"></a>

Your workspace is experiencing availability loss because the subnets connected to your workspace do not have enough free IP addresses.

**To resolve this issue:**

1. Open the Amazon Managed Grafana console. In the left navigation pane, choose **All workspaces**, then select your workspace.

1. In the **Network access control** tab, under **Outbound VPC connection**, choose each subnet to access the Subnet Details page.

1. Verify that each subnet has at least 15 available IPv4 addresses.

1. If a subnet has fewer than 15 free IP addresses, free up IP addresses by releasing addresses associated with instances or deleting unused network interfaces.

1. If you cannot free up IP addresses, replace the subnet with one that has at least 15 free IP addresses. We recommend using dedicated subnets for Amazon Managed Grafana. For step-by-step instructions, see [What should I do if I'm unable to update an Amazon Managed Grafana workspace due to insufficient IP addresses?](AMG-configure-vpc-faq.md#vpc-faq-ip-exhaustion).

We strongly recommend that you configure alarms to monitor IP usage in your VPC subnets. For more information, see [Track IP addresses](https://docs.aws.amazon.com/vpc/latest/ipam/tracking-ip-addresses-ipam.html) in the *Amazon VPC IPAM Guide*.

## Missing DHCP option set
<a name="degraded-broken-dhcp"></a>

Your workspace is experiencing availability loss because the VPC connected to your workspace does not have a DHCP option set configured.

**To resolve this issue:**

1. Open the Amazon Managed Grafana console. In the left navigation pane, choose **All workspaces**, then select your workspace.

1. In the **Network access control** tab, under **Outbound VPC connection**, open the VPC associated with your workspace.

1. In the VPC Details, choose **Actions**, then choose **Edit VPC settings**.

1. Under **DHCP settings**, change the DHCP option set from **No DHCP Option set** to a valid option set. For more information, see [DHCP option sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) in the *Amazon VPC User Guide*.
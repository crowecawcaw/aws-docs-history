# Considerations for working with firewalls and firewall endpoints

Before you create, update, or delete a firewall and its endpoints in AWS Network Firewall, review these considerations.

For information on considerations specific to transit gateway-attached firewalls, see [Considerations for transit gateway-attached firewalls](tgw-firewall-considerations.md "tgw-firewall-considerations.md").

## General firewall considerations

**Account status impacts**

When a firewall owner's account becomes inactive:

- The firewall enters a `FAIL_CLOSED` state, dropping all traffic through both primary endpoints and VPC endpoint associations
- No metering occurs for the firewall or its associated endpoints
- VPC endpoint association owners receive a notification about the firewall account's inactive state

When a VPC endpoint association owner's account becomes inactive:

- Only that specific VPC endpoint association enters a `FAIL_CLOSED` state
- The inactive endpoint is excluded from the firewall's consolidated billing
- Other VPC endpoint associations continue to function normally

For more information on potential error scenarios and how to resolve them,
see [Troubleshooting firewall endpoint failures in AWS Network Firewall](firewall-troubleshooting-endpoint-failures.md "firewall-troubleshooting-endpoint-failures.md")

**CloudWatch metrics access**

Access to CloudWatch metrics varies by role:

- Firewall owners have full access to metrics
- VPC endpoint association owners have limited access

For details, see [AWS Network Firewall metrics in Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

**AWS KMS key considerations**

When there are issues with the AWS KMS key used by the firewall owner:

- A failure notification appears in the firewall's status
- A failure notification appears in all associated VPC endpoint association statuses
- The firewall cannot process traffic until the AWS KMS key is restored to an active state

These failures can occur if the AWS KMS key is revoked, disabled, or deleted. To restore service, the firewall owner must ensure their AWS KMS key is active and properly configured.

For more information on potential error scenarios and how to resolve them,
see [Troubleshooting firewall endpoint failures in AWS Network Firewall](firewall-troubleshooting-endpoint-failures.md "firewall-troubleshooting-endpoint-failures.md").

## VPC endpoint association considerations

Before you use VPC endpoint associations in AWS Network Firewall, consider the following:

**Firewall unsharing impacts**

When a firewall owner unshares a firewall:

- Existing VPC endpoint associations continue to function
- VPC endpoint association owners can no longer view firewall metadata
- VPC endpoint association owners can still delete their associations
- The firewall cannot be deleted until all VPC endpoint associations are removed

For more information about unsharing firewalls, see [Unsharing a shared Network Firewall resource](sharing.md#sharing-unshare "sharing.md#sharing-unshare").

**TLS inspection limitations**

###### Important

TLS inspection is not supported for firewalls with VPC endpoint associations.

- A firewall policy that has TLS inspection enabled cannot be added to a firewall that has VPC endpoint associations.
- A VPC endpoint association cannot be created from a firewall that has a firewall policy with TLS inspection enabled.

For details, see [Troubleshooting firewall endpoint failures in AWS Network Firewall](firewall-troubleshooting-endpoint-failures.md "firewall-troubleshooting-endpoint-failures.md") and [Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall](tls-inspection-configurations.md "tls-inspection-configurations.md").

**IP address considerations**

When managing multiple VPCs:

- Exercise caution with overlapping IP address ranges
- Security and network policies apply consistently across overlapping IP ranges in different VPCs
- Configure the `HOME_NET` setting explicitly in firewall policies to include associated endpoints

For more information on potential error scenarios and how to resolve them,
see [Troubleshooting firewall endpoint failures in AWS Network Firewall](firewall-troubleshooting-endpoint-failures.md "firewall-troubleshooting-endpoint-failures.md").

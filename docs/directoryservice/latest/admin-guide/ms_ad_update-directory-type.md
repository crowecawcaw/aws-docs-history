# Updating directory network type

You can update your Directory Service directory's network type from IPv4 to Dual-stack (IPv4 and IPv6).
Updating the network type to include IPv6 IP addresses provides a larger address space than IPv4.
IPv4 and IPv6 communication are independent of each other.

For details, see [Compare IPv4 and IPv6](../../../vpc/latest/userguide/ipv4-ipv6-comparison.md "../../../vpc/latest/userguide/ipv4-ipv6-comparison.md") in the
_Amazon Virtual Private Cloud User Guide_.

###### Important

This is a one-way operation that cannot be reversed. Test in a non-production environment
first.

## Prerequisites

Before updating your directory network type, ensure the following requirements are
met:

- Your VPC and the associated subnets in which your directory currently exists must be
  configured with IPv6 CIDR ranges. For details, see [IPv6 support for your VPC](../../../vpc/latest/userguide/vpc-migrate-ipv6.md "../../../vpc/latest/userguide/vpc-migrate-ipv6.md") in the
  _Amazon Virtual Private Cloud User Guide_.
- You have administrative access to the AWS Management Console.
- Your directory must be in Active state.
- You have appropriate IAM permissions to modify Directory Service settings.

## To update directory network type

###### To update your directory to dual-stack networking

###### Note

If your directory is replicated in multiple regions, perform this update in each
region.

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, choose
   **Directories**.
2. Select the target directory.
3. Go to the **Networking & security** tab.
4. Choose **Add IPv6 support**. This option is only available for IPv4-only
   directories.
5. Review the update information and pricing details.
6. Choose **Add** to confirm the update.

After initiating the update, the directory status changes to **Updating**
during the update process The update typically takes 15-30 minutes to complete Once complete, the
directory status returns to **Active**.

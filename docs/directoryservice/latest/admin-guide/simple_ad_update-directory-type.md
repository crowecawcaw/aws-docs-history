

# Updating directory network type
<a name="simple_ad_update-directory-type"></a>

You can update your Directory Service directory's network type from IPv4 to Dual-stack (IPv4 and IPv6). Updating the network type to include IPv6 IP addresses provides a larger address space than IPv4. IPv4 and IPv6 communication are independent of each other.

For details, see [Compare IPv4 and IPv6](https://docs.aws.amazon.com/vpc/latest/userguide/ipv4-ipv6-comparison.html) in the *Amazon Virtual Private Cloud User Guide*.

**Important**  
This is a one-way operation that cannot be reversed. Test in a non-production environment first.

## Prerequisites
<a name="simple_ad_update-directory-type-prereq"></a>

Before updating your directory network type, ensure the following requirements are met:
+ Your VPC must be configured with IPv6 CIDR ranges. For details, see [IPv6 support for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6.html) in the *Amazon Virtual Private Cloud User Guide*.
+ You have administrative access to the AWS Management Console.
+ Your directory must be in Active state.
+ You have appropriate IAM permissions to modify Directory Service settings.

## To update directory network type
<a name="simple_ad_update-directory-type-procedure"></a>

**To update your directory to dual-stack networking**
**Note**  
If your directory is replicated in multiple regions, perform this update in each region.

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/) navigation pane, choose **Directories**.

1. Select the target directory.

1. Go to the **Networking & security** tab.

1. Choose **Add IPv6 support**. This option is only available for IPv4-only directories.

   IPv6 only directories are not supported.

1. Review the update information and pricing details.

1. Choose **Add** to confirm the update.

After initiating the update, the directory status changes to **Updating** during the update process The update typically takes 15-30 minutes to complete Once complete, the directory status returns to **Active**.
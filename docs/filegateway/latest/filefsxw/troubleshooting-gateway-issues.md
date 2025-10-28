Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Troubleshooting problems with your Storage Gateway

deployment

Following, you can find information about best practices and
troubleshooting issues related to gateways, host platforms, file systems, high availability,
data recovery, and snapshots. The on-premises gateway troubleshooting information covers
gateways deployed on supported virtualization platforms. The troubleshooting information for
high availability issues covers gateways running on VMware vSphere High Availability (HA)
platform.

**Topics**

- [Troubleshooting: gateway
  offline issues](troubleshooting-gateway-offline.md "troubleshooting-gateway-offline.md") - Learn how to diagnose
  problems that can cause your gateway to appear offline in the Storage Gateway
  console.
- [Troubleshooting: Active
  Directory issues](troubleshooting-active-directory.md "troubleshooting-active-directory.md") - Learn what to do if
  you receive error messages such as `NETWORK_ERROR`, `TIMEOUT`,
  or `ACCESS_DENIED` when trying to join your File Gateway to a Microsoft
  Active Directory domain.
- [Troubleshooting: gateway activation issues](troubleshooting-gateway-activation.md "troubleshooting-gateway-activation.md") - Learn what to do if
  you receive an internal error message when attempting to activate your
  Storage Gateway.
- [Troubleshooting: on-premises gateway issues](troubleshooting-on-premises-gateway-issues.md "troubleshooting-on-premises-gateway-issues.md") - Learn about
  typical issues that you might encounter working with your on-premises gateways, and
  how to allow Support to connect to your gateway to assist with troubleshooting.
- [Troubleshooting: Microsoft
  Hyper-V setup issues](troubleshooting-hyperv-setup.md "troubleshooting-hyperv-setup.md") - Learn about typical
  issues that you might encounter when deploying Storage Gateway on the Microsoft
  Hyper-V platform.
- [Troubleshooting: Amazon EC2
  gateway issues](troubleshooting-EC2-gateway-issues.md "troubleshooting-EC2-gateway-issues.md") - Find information
  about typical issues that you might encounter when working with gateways deployed on
  Amazon EC2.
- [Troubleshooting:
  hardware appliance issues](troubleshooting-hardware-appliance-issues.md "troubleshooting-hardware-appliance-issues.md") - Learn how to
  resolve issues that you might encounter with the AWS Storage Gateway Hardware Appliance.
- [Troubleshooting:
  File Gateway issues](troubleshooting-file-gateway-issues.md "troubleshooting-file-gateway-issues.md") - Find information
  that can help you understand the cause of errors and health notifications that
  appear in your File Gateway's CloudWatch logs.
- [Troubleshooting: high availability
  issues](troubleshooting-ha-issues.md "troubleshooting-ha-issues.md") - Learn what to do if you
  experience issues with gateways that are deployed in a VMware HA environment.

## High Availability Health

Notifications

When running your gateway on the VMware vSphere High Availability (HA) platform, you
may receive health notifications. For more information about health notifications, see
[Troubleshooting: high availability
issues](troubleshooting-ha-issues.md "troubleshooting-ha-issues.md").

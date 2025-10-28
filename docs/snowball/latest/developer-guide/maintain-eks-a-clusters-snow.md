Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Creating and maintaining clusters on Snowball Edge devices

## Best practices for creating clusters on a Snowball Edge

To create an Amazon EKS Anywhere cluster, refer to [Create Snow clusters](https://anywhere.eks.amazonaws.com/docs/getting-started/production-environment/snow-getstarted/ "https://anywhere.eks.amazonaws.com/docs/getting-started/production-environment/snow-getstarted/").

Keep the following best practices in mind when creating Amazon EKS Anywhere clusters on Snowball Edge devices:

- Before creating a cluster in a static IP address range, ensure that there are no other clusters on your Snowball Edge device using the same IP address range.
- Before creating a cluster with DHCP addressing on your Snowball Edge device, ensure that all static IP address ranges in use for clusters are not in the DHCP pool subnet.
- When creating more than one cluster, wait until one cluster is successfully provisioned and running before you create another one.

## Upgrading clusters on a Snowball Edge

To upgrade an Amazon EKS Anywhere admin AMI or EKS Distro AMI, contact AWS Support. Support will provide a Snowball Edge update containing the upgraded AMI. Then, download and install the Snowball Edge update. See [Downloading updates to Snowball Edge devices](download-updates.md "download-updates.md") and [Installing updates to Snowball Edge devices](install-updates.md "install-updates.md").

After you upgrade your Amazon EKS Anywhere AMI, you need to start a new Amazon EKS Anywhere admin
instance. See [Run an Amazon EKS Anywhere admin instance on a Snowball Edge](eksa-configuration.md#start-admin-instance "eksa-configuration.md#start-admin-instance").
Then, copy key files, the cluster folder, credentials, and certificates from the previous
admin instance to the upgraded instance. These are in a folder that's named for the
cluster.

## Cleaning up cluster resources on a Snowball Edge

If you create multiple clusters on your Snowball Edge devices and don't delete them correctly or if there is a problem in the cluster and the cluster creates replacement nodes after resuming, there will be resource leak. A sample script tool is available for you to modify and use to clean your Amazon EKS Anywhere admin instance and your Snowball Edge devices. See [Amazon EKS Anywhere on AWS Snow cleanup tools](https://github.com/aws-samples/aws-snow-tools-for-eks-anywhere/tree/main/cleanup-tools#eks-anywhere-on-snow-cleanup-tools "https://github.com/aws-samples/aws-snow-tools-for-eks-anywhere/tree/main/cleanup-tools#eks-anywhere-on-snow-cleanup-tools").

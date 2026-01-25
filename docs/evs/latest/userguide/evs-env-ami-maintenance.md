# AMI maintenance

Amazon EVS deploys ESX hosts with a custom EVS Amazon Machine Image (AMI).
The AMI contains a custom vendor add-on containing the required packages for running ESX on Amazon EC2.

## Troubleshoot add host failure due to incompatible cluster image

When you add a host to your environment, the host has the latest available version of the EVS custom vendor add-on.
If your environment uses hosts with an older add-on version, adding new hosts fails with an error that the new host is not compatible with your cluster image.
For detailed steps to fix this issue, see [Add host failure due to incompatible cluster image](troubleshooting.md#troubleshoot-cluster-image "troubleshooting.md#troubleshoot-cluster-image").



# Amazon Machine Images (AMIs) for AWS PCS

AWS PCS launches compute nodes from an AMI that you choose, so you control the software and configuration on the compute nodes in your cluster. For production AI/ML and HPC workloads, you can use the AWS-maintained PCS-ready AWS Deep Learning AMI (DLAMI). If you're evaluating AWS PCS, you can use a sample AMI that AWS provides. You can also build your own AMI for full control over your compute nodes.

You can specify the AMI on the compute node group with `amiId`, in its custom launch template, or both. With standard configuration, you must specify `amiId`. If you specify an AMI in both places, AWS PCS uses `amiId` instead of the AMI in the launch template. To use the AMI in the custom launch template instead, set `amiId` to an empty string (`""`) when you update the compute node group. For more information, see [Configuring instance settings for compute node groups in AWS PCS](working-with_cng_instance-settings.md).

**Topics**
+ [Using PCS-ready DLAMI with AWS PCS](working-with_ami_pcs-ready-dlami.md)
+ [Using sample Amazon Machine Images (AMIs) with AWS PCS](working-with_ami_samples.md)
+ [Custom Amazon Machine Images (AMIs) for AWS PCS](working-with_ami_custom.md)
+ [Software installers to build custom AMIs for AWS PCS](working-with_ami_installers.md)
+ [Release notes for AWS PCS sample AMIs](ami-release-notes.md)
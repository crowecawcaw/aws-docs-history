# Working with Amazon Linux AMIs in Amazon EMR

## Amazon Linux Amazon Machine Images (AMIs)

Amazon EMR uses an Amazon Linux Amazon Machine Image (AMI) to initialize Amazon EC2 instances when you
create and launch a cluster. The AMI contains the Amazon Linux operating system, other software,
and the configurations required for each instance to host your cluster
applications.

By default, when you create a cluster, Amazon EMR uses a default Amazon Linux (AL) AMI that is created
specifically for the Amazon EMR release version you use. For more information about the
default Amazon Linux AMI, see [Using the default Amazon Linux AMI for Amazon EMR](emr-default-ami.md "emr-default-ami.md").
When you use Amazon EMR 5.7.0 or higher, you can choose to specify a custom Amazon Linux AMI instead
of the default Amazon Linux AMI for Amazon EMR. A custom AMI allows you to encrypt the root device
volume and to customize applications and configurations as an alternative to using
bootstrap actions. You can specify a custom AMI for each instance type in the instance
group or instance fleet configuration of an Amazon EMR cluster. Multiple custom AMI support
gives you the flexibility to use more than one architecture type in a cluster. See [Using a custom AMI to provide more flexibility for Amazon EMR cluster configuration](emr-custom-ami.md "emr-custom-ami.md").

Amazon EMR automatically attaches an Amazon EBS General Purpose SSD volume as the root device
for all AMIs. EBS-backed AMIs enhance performance. For more information about Amazon Linux AMIs,
see [Amazon Machine Images (AMI)](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md"). For more
information about instance storage for Amazon EMR instances, see [Instance storage options and behavior in Amazon EMR](emr-plan-storage.md "emr-plan-storage.md").

###### Topics

- [Using the default Amazon Linux AMI for Amazon EMR](emr-default-ami.md "emr-default-ami.md")
- [Using a custom AMI to provide more flexibility for Amazon EMR cluster configuration](emr-custom-ami.md "emr-custom-ami.md")
- [Change the Amazon Linux release when you
  create an EMR cluster](emr-custom-ami-change-al-release.md "emr-custom-ami-change-al-release.md")
- [Customizing the Amazon EBS root device
  volume](emr-custom-ami-root-volume-size.md "emr-custom-ami-root-volume-size.md")

# Amazon EC2 AMI lifecycle

An Amazon Machine Image (AMI) is an image that contains the software configuration required
to set up and boot an instance. You must specify an AMI when you launch an instance. You
can use AMIs provided by Amazon, or you can create your own AMIs. The AMI must be
located in the AWS Region in which you want to launch your instance.

The lifecycle of an AMI includes creating, copying, deprecating, disabling, and deleting
(deregistering) the AMI.

**Create AMIs.** While Amazon provides AMIs that you can use to
launch your instances, you can create custom AMIs tailored to your needs. To create a
custom AMI, launch an instance from an existing AMI, customize the instance (for
example, install software and configure operating system settings), and then create an
AMI from the instance. Any instance customizations are saved to the new AMI, so that
instances launched from your new AMI include these customizations.

**Attestable AMIs.** To create an AMI that supports EC2
instance attestation, see [Attestable AMIs](attestable-ami.md "attestable-ami.md").

**Copy AMIs.** You can use an AMI to launch an instance only
in the AWS Region in which the AMI is located. If you need to launch instances with
the same configuration in multiple Regions, copy the AMI to the other Regions.

**Deprecate AMIs.** To mark an AMI as superseded or out of
date, you can set an immediate or future deprecation date. Deprecated AMIs are hidden
from AMI listings, but users and services can continue to use deprecated AMIs if they
know the AMI ID.

**Disable AMIs.** To temporarily prevent an AMI from being
used, you can disable it. When an AMI is disabled, it can't be used to launch new
instances. However, if you re-enable the AMI, it can be used to launch instances again.
Note that disabling an AMI doesn't affect existing instances that have already been
launched from it.

**Deregister (delete) AMIs.** When you no longer need an AMI,
you can deregister it, preventing it from being used to launch new instances. If the AMI
matches a retention rule, it moves to the Recycle Bin, where it can be restored before
its retention period expires, after which it is permanently deleted. If it doesn't match
a retention rule, it is permanently deleted immediately. Note that deregistering an AMI
does not affect existing instances that were launched from the AMI.

**Automate the AMI lifecycle.** You can use Amazon Data Lifecycle Manager to automate
the creation, retention, copy, deprecation, and deregistration of Amazon EBS-backed AMIs and
their backing snapshots. You can also use EC2 Image Builder to automate the creation, management,
an deployment of customized AMIs. For more information, see [Automate backups with
Amazon Data Lifecycle Manager](../../../ebs/latest/userguide/snapshot-lifecycle.md "../../../ebs/latest/userguide/snapshot-lifecycle.md") in the _Amazon EBS User Guide_ and the
[EC2
Image Builder User Guide](../../../imagebuilder/latest/userguide/what-is-image-builder.md "../../../imagebuilder/latest/userguide/what-is-image-builder.md").

###### Contents

- [Create an AMI](creating-an-ami-ebs.md "creating-an-ami-ebs.md")
- [Create an Amazon S3-backed AMI](creating-an-ami-instance-store.md "creating-an-ami-instance-store.md")
- [Create an AMI using Windows Sysprep](ami-create-win-sysprep.md "ami-create-win-sysprep.md")
- [Copy an AMI](CopyingAMIs.md "CopyingAMIs.md")
- [Store and restore an AMI](ami-store-restore.md "ami-store-restore.md")
- [AMI ancestry](ami-ancestry.md "ami-ancestry.md")
- [AMI usage](ec2-ami-usage.md "ec2-ami-usage.md")
- [Deprecate an AMI](ami-deprecate.md "ami-deprecate.md")
- [Disable an AMI](disable-an-ami.md "disable-an-ami.md")
- [Deregister an AMI](deregister-ami.md "deregister-ami.md")

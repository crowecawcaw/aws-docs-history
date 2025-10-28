# Upgrade an EC2 Windows instance to a newer version of

Windows Server

If it's time to upgrade the Windows Server operating system on your EC2 Windows instance
from an earlier version, you can use one of the following methods.

**In-place upgrade**

An in-place upgrade operates on an existing instance. Only the operating system
files are affected during this process, while your settings, server roles, and data
are left intact.

**Migration (also known as a side-by-side upgrade)**

A migration involves capturing settings, configurations, and data, and porting these
to a newer operating system on a fresh EC2 Windows instance. You can launch your instance
from a public or private Windows AMI that you subscribe to from the AWS Marketplace, or an AMI
that's shared with you. You can also create a custom AMI with EC2 Image Builder. See the
[Image Builder User Guide](../../../imagebuilder/latest/userguide/what-is-image-builder.md "../../../imagebuilder/latest/userguide/what-is-image-builder.md") for more information.

###### Note

AWS provides a set of publicly available Amazon Machine Images (AMIs) for Windows
Server versions that run on EC2 instances. These AMIs are updated on a monthly basis.
For information about the latest Windows AMIs, see the [AWS Windows AMI Reference](../../../ec2/latest/windows-ami-reference/windows-amis.md "../../../ec2/latest/windows-ami-reference/windows-amis.md").

Microsoft has traditionally recommended migrating to a newer version of Windows Server
instead of upgrading in place. Migrating can result in fewer upgrade errors or issues, but can take
longer than an in-place upgrade because of the need to provision a new instance, plan for
and port applications, and adjust configuration settings on the new instance. An in-place
upgrade can be faster, but software incompatibilities can produce errors.

###### Contents

- [Perform an in-place upgrade on your EC2 Windows instance](os-inplaceupgrade.md "os-inplaceupgrade.md")
- [Use Automation runbooks to upgrade an EC2 Windows instance](automated-upgrades.md "automated-upgrades.md")
- [Migrate an EC2 Windows instance to a Nitro-based instance type](migrating-latest-types.md "migrating-latest-types.md")
- [Troubleshoot an operating system upgrade on an EC2 Windows instance](os-upgrade-trbl.md "os-upgrade-trbl.md")

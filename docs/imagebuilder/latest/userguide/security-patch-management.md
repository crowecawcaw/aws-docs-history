# Patch Management for Image Builder images

AWS provides updated managed AMIs each month that have the latest updates and
security patches applied for the following operating systems. You can use these AMIs
as the base image for your customizations. For more information, see
[Supported operating systems](what-is-image-builder.md#image-builder-os "what-is-image-builder.md#image-builder-os").

- Linux distributions including Amazon Linux 2, AL2023, Red Hat Enterprise Linux (RHEL),
  CentOS, Ubuntu, SUSE Linux Enterprise Server
- Windows Server 2016 and later
- macOS 10.14.x and later
  After you create a custom image, you are responsible for Amazon EC2 system patching, per
  the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"). If the EC2 instances in your application
  workload can be easily replaced, then it might be most efficient to update the base AMI
  and redeploy all compute nodes based on this image.

###### Note

For macOS patching, we recommend that you create a new version of your recipe that
uses the latest managed AMI for the base image, and then build an updated custom image
from the recipe and your other image build resources. If your Mac instances are not
easily replaced, see the [Update the operating system and
software on Mac instances](../../../AWSEC2/latest/UserGuide/mac-instance-updates.md "../../../AWSEC2/latest/UserGuide/mac-instance-updates.md") page in the _Amazon EC2 User Guide_ for
more information.

The following are two ways you can keep your Image Builder AMIs up to date.

- **AWS-provided patching components** –
  EC2 Image Builder provides the following build components that install all pending
  operating system updates:

      + `update-linux`
      + `update-windows`

  These components use the `UpdateOS` action module. For more
  information, see [UpdateOS](toe-action-modules.md#action-modules-updateos "toe-action-modules.md#action-modules-updateos"). The components can
  be added to your image build pipelines by selecting them from the list of
  AWS-provided components.

- **Custom build components with patching
  operations** – To selectively install or update patches on
  operating systems of supported AMIs, you can author an Image Builder component to install
  the required patches. A custom component can install patches using shell scripts
  (Bash or PowerShell), or it can use the `UpdateOS` action module to
  specify patches for installation or exclusion. For more information, see [Action modules supported by AWSTOE
  component manager](toe-action-modules.md "toe-action-modules.md").

Component that uses the `UpdateOS` action module (Linux and
Windows only. The `UpdateOS` action module is not supported for macOS.)

```
schemaVersion: 1.0
phases:
  - name: build
	steps:
	  - name: UpdateOS
		action: UpdateOS
```

Component that uses Bash to install yum updates

```
schemaVersion: 1.0
phases:
  - name: build
	steps:
	  - name: InstallYumUpdates
		action: ExecuteBash
		inputs:
		  commands:
			- sudo yum update -y
```

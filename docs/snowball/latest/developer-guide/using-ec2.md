AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Using Amazon EC2-compatible compute instances on Snowball Edge

You can run Amazon EC2-compatible compute instances hosted on a Snowball Edge with the
`sbe1`, `sbe-c`, and `sbe-g` instance types. The
`sbe1` instance type works on devices with the Snowball Edge Storage
Optimized option. The `sbe-c` instance type works on devices with the
Snowball Edge Compute Optimized option. For a list of supported instance types, see [Quotas for compute instances on a Snowball Edge device](ec2-edge-limits.md "ec2-edge-limits.md").

All three compute instance types supported for use on Snowball Edge device options
are unique to Snowball Edge devices. Like their cloud-based counterparts, these
instances require Amazon Machine Images (AMIs) to launch. You choose the AMI to be that
base image for an instance in the cloud, before you create your Snowball Edge
job.

To use a compute instance on a Snowball Edge, create a job to order a Snowball Edge device and specify your AMIs.
You can do this using the [AWS Snow Family Management Console](https://console.aws.amazon.com/snowfamily/home "https://console.aws.amazon.com/snowfamily/home"), the AWS CLI, or one of the AWS SDKs.
Typically, there are some housekeeping prerequisites that you must perform before
creating your job, to use your instances.

After your device arrives, you can start managing your AMIs and instances. You can
manage your compute instances on a Snowball Edge through an Amazon EC2-compatible endpoint.
This type of endpoint supports many of the Amazon EC2-compatible CLI commands and actions for the AWS
SDKs. You can't use the AWS Management Console on the Snowball Edge to manage your AMIs and compute
instances.

When you're done with your device, return it to AWS. If the device was used in an
import job, the data transferred using the Amazon S3 adapter or the NFS interface is
imported into Amazon S3. Otherwise, we perform a complete erasure of the device when it is
returned to AWS. This erasure follows the National Institute of Standards and
Technology (NIST) 800-88 standards.

###### Important

- Using encrypted AMIs on Snowball Edge Edge devices is not supported.
- Data in compute instances running on a Snowball Edge isn't imported
  into AWS.

###### Topics

- [Difference between Amazon EC2 and Amazon EC2-compatible instances on Snowball Edge](#ec2-compatible-sbe "#ec2-compatible-sbe")
- [Pricing for Compute Instances on Snowball
  Edge](#pricing-for-ec2-edge "#pricing-for-ec2-edge")
- [Using an Amazon EC2-compatible AMI on Snowball Edge](using-ami.md "using-ami.md")
- [Importing a virtual machine image to a Snowball Edge device](ec2-ami-import-cli.md "ec2-ami-import-cli.md")
- [Using the AWS CLI and API operations on
  Snowball Edge device](using-ec2-cli-specify-region.md "using-ec2-cli-specify-region.md")
- [Network configurations for compute instances on Snowball Edge](network-config-ec2.md "network-config-ec2.md")
- [Using SSH to connect to compute instances on a
  Snowball Edge](ssh-ec2-edge.md "ssh-ec2-edge.md")
- [Transferring data from EC2-compatible compute instances
  to S3 buckets on the same Snowball Edge](data-transfer-ec2-s3-edge.md "data-transfer-ec2-s3-edge.md")
- [Starting EC2-compatible instances automatically](using-ec2-edge-client.md "using-ec2-edge-client.md")
- [Using the Amazon EC2-compatible endpoint on a Snowball Edge](using-ec2-endpoint.md "using-ec2-endpoint.md")
- [Autostarting EC2-compatible instances with launch
  templates on a Snowball Edge](ec2-autostart.md "ec2-autostart.md")
- [Using Instance Metadata Service for Snow with Amazon EC2-compatible instances on a Snowball Edge](imds.md "imds.md")
- [Using block storage with Amazon EC2-compatible instances on Snowball Edge](edge-ebs.md "edge-ebs.md")
- [Controlling network traffic with security groups on Snowball Edge](edge-security-groups.md "edge-security-groups.md")
- [Supported EC2-compatible instance metadata and user data on Snowball Edge](edge-compute-instance-metadata.md "edge-compute-instance-metadata.md")
- [Stopping EC2-compatible instances running on Snowball Edge](#managing-ec2-instances "#managing-ec2-instances")

## Difference between Amazon EC2 and Amazon EC2-compatible instances on Snowball Edge

AWS Snowball Edge EC2-compatible instances allow customers to use and manage Amazon EC2-compatible instances using a subset of EC2 APIs and a subset of AMIs.

## Pricing for Compute Instances on Snowball

Edge

There are additional costs associated with using compute instances. For more
information, see [AWS Snowball Edge Pricing](http://aws.amazon.com/snowball-edge/pricing "http://aws.amazon.com/snowball-edge/pricing").

## Stopping EC2-compatible instances running on Snowball Edge

To avoid accidentally deleting the Amazon EC2-compatible instances that you create on a device,
don't shut down your instances from the operating system. For example, don't
use the `shutdown` or `reboot` commands. Shutting down an instance
from within the operating system has the same effect as calling the [terminate-instances](../../../cli/latest/reference/ec2/terminate-instances.md "../../../cli/latest/reference/ec2/terminate-instances.md")
command.

Instead, use the [stop-instances](../../../cli/latest/reference/ec2/stop-instances.md "../../../cli/latest/reference/ec2/stop-instances.md") command to suspend Amazon EC2-compatible instances that you want to
preserve.

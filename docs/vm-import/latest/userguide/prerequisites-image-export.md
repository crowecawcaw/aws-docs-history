# Prerequisites for exporting an

image from Amazon EC2

To export a VM from Amazon EC2, first meet the following prerequisites.

- Install the AWS CLI. For more information, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

###### Tip

In [supported
AWS Regions](../../../cloudshell/latest/userguide/supported-aws-regions.md "../../../cloudshell/latest/userguide/supported-aws-regions.md"), you can also use [AWS CloudShell](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") for a
browser-based, pre-authenticated shell that launches directly from the
AWS Management Console.

- Create an Amazon Simple Storage Service (Amazon S3) bucket for storing the exported images or choose an existing
  bucket. The bucket must be in the Region where you want to export your VMs.
  Additionally, the bucket must belong to the AWS account where you are
  performing the export operation. For more information about S3 buckets, see the
  [Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md").
- Create an IAM role named `vmimport`. For more information,
  see [Required service role](required-permissions.md#vmimport-role "required-permissions.md#vmimport-role").

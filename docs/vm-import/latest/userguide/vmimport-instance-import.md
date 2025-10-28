# Import a VM as an EC2 instance using VM Import/Export

###### Important

We strongly recommend that you import VMs as Amazon Machine Images (AMI) instead of
instances. For more information, see [Import a VM to Amazon EC2 as an image using VM Import/Export](vmimport-image-import.md "vmimport-image-import.md").

You can use VM Import/Export to import virtual machine (VM) images from your
virtualization environment to Amazon EC2 as instances. Subsequently, you can export the VM images
from the instance back to your virtualization environment. This enables you to leverage your
investments in the VMs that you have built to meet your IT security, configuration
management, and compliance requirements by bringing them into Amazon EC2.

###### Contents

- [Limitations of instance import](#vmimport-instance-import-limitations "#vmimport-instance-import-limitations")
- [Import a VM with instance import](#vmimport-instance-import-prerequisites "#vmimport-instance-import-prerequisites")

## Limitations of instance import

Importing a VM as an instance has the following limitations:

- The AWS Command Line Interface (AWS CLI) does not support importing a VM as an instance, so you
  must use the deprecated Amazon EC2 Command Line Interface (Amazon EC2 CLI).
- You cannot import a Windows instance that uses the bring your own license
  (BYOL) model as an instance. Instead, you must import the VM as an AMI.
- VM Import/Export supports importing Windows instances into most instance types.
  Linux instances can be imported into the following instance types:
  - General purpose: `t2.micro` | `t2.small` | `t2.medium` | `m3.medium` | `m3.large` | `m3.xlarge` | `m3.2xlarge`
  - Compute optimized: `c3.large` | `c3.xlarge` | `c3.2xlarge` | `c3.4xlarge` | `c3.8xlarge` | `cc1.4xlarge` | `cc2.8xlarge`
  - Memory optimized: `r3.large` | `r3.xlarge` | `r3.2xlarge` | `r3.4xlarge` | `r3.8xlarge` | `cr1.8xlarge`
  - Storage optimized: `i2.xlarge` | `i2.2xlarge` | `i2.4xlarge` | `i2.8xlarge` | `hi1.4xlarge` | `hi1.8xlarge`

- The `ImportInstance` and `ImportVolume` API actions are
  supported only in the following Regions and will not be supported in any
  additional Regions.
  - North America: us-east-1 | us-west-1 | us-west-2 | us-east-2 |
    ca-central-1 | us-gov-west-1
  - South America: sa-east-1
  - Europe/Middle East/Africa: eu-west-1 | eu-central-1
  - Asia Pacific: ap-southeast-1 | ap-northeast-1 | ap-southeast-2 |
    ap-northeast-2 | ap-south-1 | cn-north-1

## Import a VM with instance import

You can use the `ImportInstance` operation to import your VM as an
instance. For more information, see [ImportInstance](../../../AWSEC2/latest/APIReference/API_ImportInstance.md "../../../AWSEC2/latest/APIReference/API_ImportInstance.md") in
the _Amazon Elastic Compute Cloud API Reference_.

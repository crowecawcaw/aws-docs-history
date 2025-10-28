# Operating systems

AWS ParallelCluster supports Amazon Linux 2, Amazon Linux 2023, Ubuntu24.04, Ubuntu 22.04, Ubuntu 20.04, Red Hat Enterprise Linux 8 (RHEL8), Rocky 8, Red Hat Enterprise Linux 9 (RHEL9), and Rocky 9. AWS ParallelCluster offers pre-built AMIs for select operating systems, for more details on AMIs
provided by AWS ParallelCluster refer to [Image section](Image-v3.md "Image-v3.md").

## Operating system considerations

**Ubuntu 22.04 & Ubuntu 24.04**

Ubuntu 22.04 & Ubuntu 24.04 require more secure keys for ssh and do not support RSA keys by default.
Please generate an ed25519 key and use that for cluster creation.

Ubuntu 22.04 cannot be updated to the latest kernel because there is no FSx client for that
kernel.

**RHEL 8**

RedHat Enterprise Linux 8.7 (rhel8) is added starting in AWS ParallelCluster version 3.6.0. If
you configure your cluster to use rhel8, the on-demand cost for any instance type is higher than
when you configure your cluster to use other supported operation systems.

For more information about pricing, see [On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand "https://aws.amazon.com/ec2/pricing/on-demand") and [How is Red Hat Enterprise
Linux on Amazon Elastic Compute Cloud offered and priced?](https://aws.amazon.com/partners/redhat/faqs/#Pricing_and_Billing "https://aws.amazon.com/partners/redhat/faqs/#Pricing_and_Billing").

**Rocky 8**

AWS ParallelCluster 3.8.0 supports Rocky Linux 8, but pre-built Rocky Linux 8 AMIs (for x86
and ARM architectures) are not available. AWS ParallelCluster 3.8.0 supports creating clusters with
Rocky Linux 8 using custom AMIs using the [CustomAmi](Image-v3.md#yaml-Image-CustomAmi "Image-v3.md#yaml-Image-CustomAmi")
property. For more information about building custom AMIs, refer to [AWS ParallelCluster AMI customization](custom-ami-v3.md "custom-ami-v3.md").

To build your custom AMI from a base Rocky Linux 8 AMI, you can consider subscribing to the
[Rocky Linux 8 AMIs](https://aws.amazon.com/marketplace/seller-profile?id=01538adc-2664-49d5-b926-3381dffce12d "https://aws.amazon.com/marketplace/seller-profile?id=01538adc-2664-49d5-b926-3381dffce12d") available on the AWS [Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace"). Make sure to review the pricing
and subscription costs for Rocky Linux 8 AMIs on the AWS Marketplace. Alternatively you can
also use the [official Rocky Linux 8
AMIs](https://rockylinux.org/cloud-images/ "https://rockylinux.org/cloud-images/")as your base AMI.

**Rocky9**

AWS ParallelCluster 3.9.0 supports Rocky Linux 9, but pre-built Rocky Linux 9 AMIs (for x86
and ARM architectures) are not available. AWS ParallelCluster 3.9.0 supports creating clusters with
Rocky Linux 9 using custom AMIs using the [CustomAmi](Image-v3.md#yaml-Image-CustomAmi "Image-v3.md#yaml-Image-CustomAmi") property.
For more information about building custom AMIs, refer to [AWS ParallelCluster
AMI customization](custom-ami-v3.md "custom-ami-v3.md"). To build your custom AMI from a base Rocky Linux 9 AMI, you can also
use the [official Rocky Linux 9 AMIs](https://rockylinux.org/cloud-images/ "https://rockylinux.org/cloud-images/") as
your base AMI. Custom Rocky Linux 9 AMI build may fail if the base AMI does not have the latest
kernel. To upgrade the kernel before building the AMI:

- Launch an instance using a rocky9 AMI id from here: [https://rockylinux.org/cloud-images/](https://rockylinux.org/cloud-images/ "https://rockylinux.org/cloud-images/")
- ssh into the instance and run the following command:`sudo yum -y update`
- Create an image from the instance to use as `ParentImage`

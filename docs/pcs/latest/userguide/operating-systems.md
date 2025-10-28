# Supported operating systems in AWS PCS

AWS PCS uses the Amazon Machine Image (AMI) configured for a compute node group
to launch EC2 instances in that compute node group. The AMI determines the operating
system that the EC2 instances use. You can't change the operating system in AWS PCS
sample AMIs. You must create a custom AMI if you want to use a different operating system.
For more information, see [Amazon Machine Images (AMIs) for AWS PCS](working-with_ami.md "working-with_ami.md").

###### Supported operating systems

- ###### Amazon Linux 2

This is the operating system in the AWS PCS sample AMIs.

###### Important

Sample AMIs are for demonstration purposes and are not recommended for production
workloads. You should create and use a custom AMI for production workloads, even if
you intend to use Amazon Linux 2.

- ###### RedHat Enterprise Linux 9 (RHEL 9)

The on-demand cost for RHEL any instance type is higher than
for other supported operation systems. For more information about pricing, see
[On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand "https://aws.amazon.com/ec2/pricing/on-demand") and
[How is Red Hat Enterprise
Linux on Amazon Elastic Compute Cloud offered and priced?](https://aws.amazon.com/partners/redhat/faqs/#Pricing_and_Billing "https://aws.amazon.com/partners/redhat/faqs/#Pricing_and_Billing").

- ###### Rocky Linux 9

You can use the [official Rocky Linux 9 AMIs](https://rockylinux.org/cloud-images/ "https://rockylinux.org/cloud-images/") as
a base for a custom AMI. Your custom AMI build might fail if the base AMI doesn't have the latest
kernel.

###### To upgrade the kernel

    1. Launch an instance using a rocky9 AMI id from here: [https://rockylinux.org/cloud-images/](https://rockylinux.org/cloud-images/ "https://rockylinux.org/cloud-images/")
    2. ssh into the instance and run the following command:



    ```
    sudo yum -y update
    ```
    3. Create an image from the instance. You specify this image as the `ParentImage`
     for your custom AMI.

- ###### Ubuntu 22.04

Ubuntu 22.04 requires more secure keys for SSH and doesn't support RSA keys by default.
We recommend you generate and use an ED25519 key instead.

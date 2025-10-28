# Deploy a customized Amazon EC2 instance for

Tape Gateway

You can deploy and activate a Tape Gateway on an Amazon Elastic Compute Cloud (Amazon EC2) instance. The
AWS Storage Gateway Amazon Machine Image (AMI) is available as a community AMI.

###### Note

Storage Gateway community AMIs are published and fully supported by AWS. You can see that
the publisher is AWS, a verified provider.

Tape Gateway AMIs use the following naming convention. The version
number appended to the AMI name changes with each version release.

`aws-storage-gateway-CLASSIC-2.9.0`

###### To deploy an Amazon EC2 instance to host your Tape Gateway

1. Start setting up a new gateway using the Storage Gateway console. For instructions, see
   [Set
   up a Tape Gateway](create-gateway-vtl.md#set-up-gateway-tape "create-gateway-vtl.md#set-up-gateway-tape"). When you reach the **Platform
   options** section, choose **Amazon EC2** as the
   **Host platform**, then use the following steps to launch the
   Amazon EC2 instance that will host your Tape Gateway.
2. Choose **Launch instance** to open the AWS Storage Gateway AMI template
   in the Amazon EC2 console, where you can configure additional settings.

Use **Quicklaunch** to launch the Amazon EC2 instance with default
settings. For more information on Amazon EC2 Quicklaunch default sepcifications, see
[Quicklaunch
Configuration Specifications for Amazon EC2.](ec2-quicklaunch-settings.md "ec2-quicklaunch-settings.md") 3. For **Name**, enter a name for the Amazon EC2 instance. After the
instance is deployed, you can search for this name to find your instance on list
pages in the Amazon EC2 console. 4. In the **Instance type** section, for **Instance
type**, choose the hardware configuration for your instance. The
hardware configuration must meet certain minimum requirements to support your
gateway. We recommend starting with the **m5.xlarge** instance
type, which meets the minimum hardware requirements for your gateway to function
properly. For more information, see [Requirements for Amazon EC2 instance
types](Requirements.md#requirements-hardware-storage "Requirements.md#requirements-hardware-storage").

You can resize your instance after you launch, if necessary. For more information,
see [Resizing your
instance](../../../AWSEC2/latest/UserGuide/ec2-instance-resize.md "../../../AWSEC2/latest/UserGuide/ec2-instance-resize.md") in the _Amazon EC2 User Guide_.

###### Note

Certain instance types, particularly i3 EC2, use NVMe SSD disks. These can
cause problems when you start or stop Tape Gateway; for
example, you can lose data from the cache. Monitor the
`CachePercentDirty` Amazon CloudWatch metric, and only start or stop your
system when that parameter is `0`. To learn more about monitoring
metrics for your gateway, see [Storage
Gateway metrics and dimensions](../../../AmazonCloudWatch/latest/monitoring/awssg-metricscollected.md "../../../AmazonCloudWatch/latest/monitoring/awssg-metricscollected.md") in the CloudWatch documentation. 5. In the **Key pair (login)** section, for \*\*Key pair name

- \*required*\*\*, select the key pair you want to use
  to securely connect to your instance. You can create a new key pair if necessary.
  For more information, see [Create a key pair](../../../AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.md#create-a-key-pair "../../../AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.md#create-a-key-pair") in the *Amazon Elastic Compute Cloud User Guide for Linux
  Instances\*.

6. In the **Network settings** section, review the preconfigured
   settings and choose **Edit** to make changes to the following
   fields:
   1. For **VPC - _required_**, choose the
      VPC where you want to launch your Amazon EC2 instance. For more information, see
      [How Amazon VPC works](../../../vpc/latest/userguide/how-it-works.md "../../../vpc/latest/userguide/how-it-works.md") in the _Amazon Virtual Private Cloud User
      Guide_.
   2. (Optional) For **Subnet**, choose the subnet where you
      want to launch your Amazon EC2 instance.
   3. For **Auto-assign Public IP**, choose
      **Enable**.

7. In the **Firewall (security groups)** subsection, review the
   preconfigured settings. You can change the default name and description of the new
   security group to be created for your Amazon EC2 instance if you want, or choose to apply
   firewall rules from an existing security group instead.
8. In the **Inbound security groups rules** subsection, add firewall
   rules to open the ports that clients will use to connect to your instance. For more
   information on the ports required for Tape Gateway, see
   [Port
   requirements](Requirements.md#requirements-network "Requirements.md#requirements-network"). For more information on adding firewall rules, see [Security group rules](../../../AWSEC2/latest/UserGuide/security-group-rules.md "../../../AWSEC2/latest/UserGuide/security-group-rules.md") in the _Amazon Elastic Compute Cloud User Guide for Linux
   Instances_.

###### Note

Tape Gateway requires TCP port 80 to be open for inbound traffic and for
one-time HTTP access during gateway activation. After activation, you can close
this port.

Additionally, you must open TCP port 3260 for iSCSI access. 9. In the **Advanced network configuration** subsection, review the
preconfigured settings and make changes if necessary. 10. In the **Configure storage** section, choose **Add new
volume** to add storage to your gateway instance.

###### Important

You must add at least one Amazon EBS volume with at least **165
GiB** capacity for cache storage, and at least one Amazon EBS volume
with at least **150 GiB** capacity for upload
buffer, in addition to the preconfigured **Root volume**. For
increased performance, we recommend allocating multiple EBS volumes for cache
storage with at least 150 GiB each. 11. In the **Advanced details** section, review the preconfigured
settings and make changes if necessary. 12. Choose **Launch instance** to launch your new Amazon EC2 gateway
instance with the configured settings. 13. To verify that your new instance launched successfully, navigate to the
**Instances** page in the Amazon EC2 console and search for your new
instance by name. Ensure that that **Instance state** displays
**Running**
_with a green check mark_, and that the **Status
check** is complete, and _shows a green check
mark_. 14. Select your instance from the details page. Copy the **Public IPv4
address** from the **Instance summary** section, then
return to the **Set up gateway** page in the Storage Gateway console to
resume setting up your Tape Gateway.
You can determine the AMI ID to use for launching a Tape Gateway by using the
Storage Gateway console or by querying the AWS Systems Manager parameter store.

**To determine the AMI ID, do one of the following:**

- Start setting up a new gateway using the Storage Gateway console. For instructions, see
  [Set
  up a Tape Gateway](create-gateway-vtl.md#set-up-gateway-tape "create-gateway-vtl.md#set-up-gateway-tape"). When you reach the **Platform
  options** section, choose **Amazon EC2** as the
  **Host platform**, then choose **Launch
  instance** to open the AWS Storage Gateway AMI template in the Amazon EC2
  console.

You are redirected to the EC2 community AMI page, where you can see the AMI ID for
your AWS Region in the URL.

- Query the Systems Manager parameter store. You can use the AWS CLI or
  Storage Gateway API to query the Systems Manager public parameter under the namespace
  `/aws/service/storagegateway/ami/VTL/latest`. For example, using the
  following CLI command returns the ID of the current AMI in the AWS Region you
  specify.

```
aws --region `us-east-2` ssm get-parameter --name /aws/service/storagegateway/ami/VTL/latest
```

The CLI command returns output similar to the following.

```
{
    "Parameter": {
        "Type": "String",
        "LastModifiedDate": 1561054105.083,
        "Version": 4,
        "ARN": "arn:aws:ssm:us-east-2::parameter/aws/service/storagegateway/ami/VTL/latest",
        "Name": "/aws/service/storagegateway/ami/VTL/latest",
        "Value": "**ami-123c45dd67d891000**"
    }
}
```

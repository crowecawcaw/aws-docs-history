# Troubleshooting Amazon EC2 gateway

issues

In the following sections, you can find typical issues that you might encounter
working with your gateway deployed on Amazon EC2. For more information about the difference
between an on-premises gateway and a gateway deployed in Amazon EC2, see [Deploy a customized Amazon EC2 instance for
Tape Gateway](ec2-gateway-common.md "ec2-gateway-common.md").

###### Topics

- [Your gateway activation hasn't occurred
  after a few moments](#activation-issues "#activation-issues")
- [You can't find your EC2 gateway instance in the
  instance list](#find-instance "#find-instance")
- [You created an Amazon EBS volume but can't attach
  it to your EC2 gateway instance](#ebs-volume-issue "#ebs-volume-issue")
- [You get a message that you have no disks available when
  you try to add storage volumes](#no-disk "#no-disk")
- [You want to remove a disk allocated as upload
  buffer space to reduce upload buffer space](#uploadbuffer-issue "#uploadbuffer-issue")
- [Throughput to or from your EC2 gateway
  drops to zero](#gateway-throughput-issue "#gateway-throughput-issue")
- [You want Support to help troubleshoot
  your EC2 gateway](#EC2-EnableAWSSupportAccess "#EC2-EnableAWSSupportAccess")
- [You want to connect to your gateway instance
  using the Amazon EC2 serial console](#ec2-serial-console "#ec2-serial-console")

## Your gateway activation hasn't occurred

after a few moments

Check the following in the Amazon EC2 console:

- Port 80 is activated in the security group that you associated with the
  instance. For more information about adding a security group rule, see
  [Adding a security group rule](../../../AWSEC2/latest/UserGuide/ec2-security-groups.md#adding-security-group-rule "../../../AWSEC2/latest/UserGuide/ec2-security-groups.md#adding-security-group-rule") in the
  _Amazon EC2 User Guide_.
- The gateway instance is marked as running. In the Amazon EC2 console, the
  **State** value for the instance should be
  RUNNING.
- Make sure that your Amazon EC2 instance type meets the minimum requirements, as
  described in [Storage requirements](Requirements.md#requirements-storage "Requirements.md#requirements-storage").

After correcting the problem, try activating the gateway again. To do this, open
the Storage Gateway console, choose **Deploy a new Gateway on Amazon EC2**,
and re-enter the IP address of the instance.

## You can't find your EC2 gateway instance in the

instance list

If you didn't give your instance a resource tag and you have many instances
running, it can be hard to tell which instance you launched. In this case, you can
take the following actions to find the gateway instance:

- Check the name of the Amazon Machine Image (AMI) on the
  **Description** tab of the instance. An instance based
  on the Storage Gateway AMI should start with the text
  `aws-storage-gateway-ami`.
- If you have several instances based on the Storage Gateway AMI, check the instance
  launch time to find the correct instance.

## You created an Amazon EBS volume but can't attach

it to your EC2 gateway instance

Check that the Amazon EBS volume in question is in the same Availability Zone as the
gateway instance. If there is a discrepancy in Availability Zones, create a new
Amazon EBS volume in the same Availability Zone as your instance.

## You get a message that you have no disks available when

you try to add storage volumes

For a newly activated gateway, no volume storage is defined. Before you can define
volume storage, you must allocate local disks to the gateway to use as an upload
buffer and cache storage. For a gateway deployed to Amazon EC2, the local disks are Amazon EBS
volumes attached to the instance. This error message likely occurs because no Amazon EBS
volumes are defined for the instance.

Check block devices defined for the instance that is running the gateway. If there
are only two block devices (the default devices that come with the AMI), then you
should add storage. For more information on doing so, see [Deploy a customized Amazon EC2 instance for
Tape Gateway](ec2-gateway-common.md "ec2-gateway-common.md"). After
attaching two or more Amazon EBS volumes, try creating volume storage on the
gateway.

## You want to remove a disk allocated as upload

buffer space to reduce upload buffer space

Follow the steps in [Determining the size of
upload buffer to allocate](decide-local-disks-and-sizes.md#CachedLocalDiskUploadBufferSizing-common "decide-local-disks-and-sizes.md#CachedLocalDiskUploadBufferSizing-common").

## Throughput to or from your EC2 gateway

drops to zero

Verify that the gateway instance is running. If the instance is starting due to a
reboot, for example, wait for the instance to restart.

Also, verify that the gateway IP has not changed. If the instance was stopped and
then restarted, the IP address of the instance might have changed. In this case, you
need to activate a new gateway.

You can view the throughput to and from your gateway from the Amazon CloudWatch console.
For more information about measuring throughput to and from your gateway and AWS,
see [Measuring Performance Between Your
Tape Gateway and AWS](PerfGatewayAWS-vtl-common.md "PerfGatewayAWS-vtl-common.md").

## You want Support to help troubleshoot

your EC2 gateway

Storage Gateway provides a local console you can use to perform several maintenance tasks,
including activating Support to access your gateway to assist you with troubleshooting
gateway issues. By default, Support access to your gateway is deactivated. You provide
this access through the Amazon EC2 local console. You log in to the Amazon EC2 local console
through a Secure Shell (SSH). To successfully log in through SSH, your
instance's security group must have a rule that opens TCP port 22.

###### Note

If you add a new rule to an existing security group, the new rule applies to
all instances that use that security group. For more information about security
groups and how to add a security group rule, see [Amazon EC2 security
groups](../../../AWSEC2/latest/UserGuide/using-network-security.md "../../../AWSEC2/latest/UserGuide/using-network-security.md") in the _Amazon EC2 User Guide_.

To let Support connect to your gateway, you first log in to the local console for
the Amazon EC2 instance, navigate to the Storage Gateway's console, and then provide
the access.

###### To activate Support access to a gateway deployed on an Amazon EC2 instance

1. Log in to the local console for your Amazon EC2 instance. For instructions, go
   to [Connect to your
   instance](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md") in the _Amazon EC2 User Guide_.

You can use the following command to log in to the EC2 instance's
local console.

```
ssh –i `PRIVATE-KEY` admin@`INSTANCE-PUBLIC-DNS-NAME`
```

###### Note

The `PRIVATE-KEY` is the
`.pem` file containing the private certificate of
the EC2 key pair that you used to launch the Amazon EC2 instance. For more
information, see [Retrieving the public key for your key pair](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md#retriving-the-public-key "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md#retriving-the-public-key") in the
_Amazon EC2 User Guide_.

The `INSTANCE-PUBLIC-DNS-NAME` is the public
Domain Name System (DNS) name of your Amazon EC2 instance that your gateway
is running on. You obtain this public DNS name by selecting the Amazon EC2
instance in the EC2 console and clicking the
**Description** tab. 2. At the prompt, enter `6 - Command Prompt` to open the
Support Channel console. 3. Enter `h` to open the **AVAILABLE
COMMANDS** window. 4. Do one of the following:

    * If your gateway is using a public endpoint, in the
     **AVAILABLE COMMANDS** window, enter
     `open-support-channel` to connect to
     customer support for Storage Gateway. Allow TCP port 22 so you can open a
     support channel to AWS. When you connect to customer support,
     Storage Gateway assigns you a support number. Make a note of your
     support number.
    * If your gateway is using a VPC endpoint, in the
     **AVAILABLE COMMANDS** window, enter
     `open-support-channel`. If your gateway is
     not activated, provide the VPC endpoint or IP address to connect to
     customer support for Storage Gateway. Allow TCP port 22 so you can open
     a support channel to AWS. When you connect to customer support,
     Storage Gateway assigns you a support number. Make a note of your
     support number.

###### Note

The channel number is not a Transmission Control Protocol/User
Datagram Protocol (TCP/UDP) port number. Instead, the gateway makes a
Secure Shell (SSH) (TCP 22) connection to Storage Gateway servers and
provides the support channel for the connection. 5. After the support channel is established, provide your support service
number to Support so Support can provide troubleshooting assistance. 6. When the support session is completed, enter `q` to
end it. Don't close the session until Support notifies you that the support
session is complete. 7. Enter `exit` to exit the Storage Gateway console. 8. Follow the console menus to log out of the Storage Gateway instance.

## You want to connect to your gateway instance

using the Amazon EC2 serial console

You can use the Amazon EC2 serial console to troubleshoot boot, network configuration,
and other issues. For instructions and troubleshooting tips, see [Amazon EC2
Serial Console](../../../AWSEC2/latest/UserGuide/ec2-serial-console.md "../../../AWSEC2/latest/UserGuide/ec2-serial-console.md") in the _Amazon Elastic Compute Cloud User Guide_.

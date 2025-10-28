# Troubleshooting: Amazon EC2 gateway

issues

In the following sections, you can find typical issues that you might encounter
working with your gateway deployed on Amazon EC2. For more information about the difference
between an on-premises gateway and a gateway deployed in Amazon EC2, see [Deploy a default Amazon EC2 host for
S3 File Gateway](ec2-gateway-file.md "ec2-gateway-file.md").

For information about using ephemeral storage, see [Using ephemeral storage with EC2 gateways](ephemeral-disk-cache.md "ephemeral-disk-cache.md").

###### Topics

- [Your gateway activation hasn't occurred
  after a few moments](#activation-issues "#activation-issues")
- [You can't find your EC2 gateway instance in the
  instance list](#find-instance "#find-instance")
- [You want to connect to your gateway instance
  using the Amazon EC2 serial console](#ec2-serial-console "#ec2-serial-console")
- [You want Support to help troubleshoot
  your Amazon EC2 gateway](#EC2-EnableAWSSupportAccess "#EC2-EnableAWSSupportAccess")

## Your gateway activation hasn't occurred

after a few moments

Check the following in the Amazon EC2 console:

- Port 80 is open in the security group that you associated with the
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

## You want to connect to your gateway instance

using the Amazon EC2 serial console

You can use the Amazon EC2 serial console to troubleshoot boot, network configuration,
and other issues. For instructions and troubleshooting tips, see [Amazon EC2
Serial Console](../../../AWSEC2/latest/UserGuide/ec2-serial-console.md "../../../AWSEC2/latest/UserGuide/ec2-serial-console.md") in the _Amazon Elastic Compute Cloud User Guide_.

## You want Support to help troubleshoot

your Amazon EC2 gateway

Storage Gateway provides a local console you can use to perform several maintenance tasks,
including allowing Support to access your gateway to assist you with troubleshooting
gateway issues. By default, Support access to your gateway is turned off. You turn on
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

###### To turn on Support access for a gateway deployed on an Amazon EC2 instance

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
end it. Don't close the session until Amazon Web Services Support notifies you that
the support session is complete. 7. Enter `exit` to exit the Storage Gateway console. 8. Follow the console menus to log out of the Storage Gateway instance.

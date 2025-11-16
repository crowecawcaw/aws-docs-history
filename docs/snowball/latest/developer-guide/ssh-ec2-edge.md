AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Using SSH to connect to compute instances on a

Snowball Edge

To use Secure Shell (SSH) to connect to compute instances on a Snowball Edge, you have the following options for providing or creating an SSH key.

- You can provide the SSH key for the Amazon Machine Image (AMI) when you create a job to order a device. For more information, see [Creating a job to order a Snowball Edge](create-job-common.md "create-job-common.md").
- You can provide the SSH key for the AMI when you create a virtual machine image to import to a Snowball Edge. For more information, see [Importing a virtual machine image to a Snowball Edge device](ec2-ami-import-cli.md "ec2-ami-import-cli.md").
- You can create a key pair on the Snowball Edge and choose to launch an instance with that locally generated public key. For more information, see [Create a key pair using Amazon EC2](../../../AWSEC2/latest/UserGuide/create-key-pairs.md#having-ec2-create-your-key-pair "../../../AWSEC2/latest/UserGuide/create-key-pairs.md#having-ec2-create-your-key-pair") in the Amazon EC2 User Guide.

###### To connect to an instance through SSH

1. Make sure that your device is powered on, connected to the network, and
   unlocked. For more information, see [Connecting a Snowball Edge to your local
   network](getting-started.md#getting-started-connect "getting-started.md#getting-started-connect").
2. Make sure that you have your network settings configured for your compute
   instances. For more information, see [Network configurations for compute instances on Snowball Edge](network-config-ec2.md "network-config-ec2.md").
3. Check your notes to find the PEM or PPK key pair that you used for this
   specific instance. Make a copy of those files somewhere on your computer. Make a
   note of the path to the PEM file.
4. Connect to your instance through SSH as in the following example command. The
   IP address is the IP address of the virtual network interface (VNIC) that you
   set up in [Network configurations for compute instances on Snowball Edge](network-config-ec2.md "network-config-ec2.md").

```

  ssh -i `path/to/PEM/key/file` `instance-user-name`@`192.0.2.0`
```

For more information, see [Connecting to Your Linux
Instance Using SSH](../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md "../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md") in the*Amazon EC2 User Guide.*

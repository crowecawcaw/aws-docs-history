# Launch an Amazon EC2 client instance for interacting with

AWS CloudHSM

To interact with and manage your AWS CloudHSM cluster and HSM instances, you must be able to
communicate with the elastic network interfaces of your HSMs. The easiest way to do this is
to use an EC2 instance in the same VPC as your cluster. You can also use the following AWS
resources to connect to your cluster:

- [Amazon VPC Peering](../../../vpc/latest/peering/Welcome.md "../../../vpc/latest/peering/Welcome.md")
- [Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md")
- [VPN Connections](../../../AmazonVPC/latest/UserGuide/vpn-connections.md "../../../AmazonVPC/latest/UserGuide/vpn-connections.md")

###### Note

This guide provides a simplified example of how to connect an EC2 instance to your AWS CloudHSM cluster. For best practices around secure network configurations, refer to [Secure access to your cluster](bp-cluster-management.md#bp-secure-access "bp-cluster-management.md#bp-secure-access").

The AWS CloudHSM documentation typically assumes that you are using an EC2 instance in the same
VPC and Availability Zone (AZ) in which you create your cluster.

###### To create an EC2 instance

1. Open the **EC2 Dashboard** at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Select **Launch instance**. From the drop-down menu, choose **Launch instance**.
3. In the **Name** field, enter a name for your EC2 instance.
4. In the **Applications and OS Images (Amazon Machine Image)** section, choose an Amazon Machine Image (AMI) that corresponds to a platform CloudHSM supports.
   For more information, see [AWS CloudHSM Client SDK 5 supported platforms](client-supported-platforms.md "client-supported-platforms.md").
5. In the **Instance Type** section, choose an instance type.
6. In the **Key pair** section, use an existing key pair or select **Create new key pair** and complete the following steps:
   1. For **Key pair name**, enter a name for the key pair.
   2. For **Key pair type**, choose a key pair type.
   3. For **Private key file format**, choose the private key file format.
   4. Select **Create key pair**.
   5. Download and save the private key file.###### Important

This is your only chance to save the private key file. Download and store the file in a safe place. You must provide the name of your
key pair when you launch an instance. Additionally, you must provide the corresponding private key each time you connect to the instance and
choose the key pair that you created when setting up. 7. In **Network settings**, select **Edit**. 8. For **VPC**, choose the VPC that you previously created for your cluster. 9. For **Subnet**, choose the public subnet that you created for the VPC. 10. For **Auto-assign Public IP**, choose **Enable**. 11. For **Auto-assign IPv6 IP**, choose **Enable** to use IPv6 connectivity with your clusters
and the Dual-stack NetworkType. If you enable this option, update your Amazon EC2 instance's security group rules, VPC and subnet route tables, and network ACLs to allow IPv6 outbound traffic from the instance to the HSMs. 12. Choose **Select an existing security group**. 13. In **Common security groups**, select the default security group from the drop-down menu. 14. In **Configure Storage**, use the drop-down menus to choose a storage configuration. 15. In the **Summary** window, select **Launch instance**.

###### Note

Completing this step will start the process for creating your EC2 instance.
For more information about creating a Linux Amazon EC2 client, see [Getting Started with Amazon EC2 Linux
Instances](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md"). For information about connecting to the running client, see the
following topics:

- [Connecting to Your
  Linux Instance Using SSH](../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md "../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md")
- [Connecting to Your Linux Instance from
  Windows Using PuTTY](../../../AWSEC2/latest/UserGuide/putty.md "../../../AWSEC2/latest/UserGuide/putty.md")

The Amazon EC2 user guide contains detailed instructions for setting up and using your Amazon EC2 instances. The following list provides an overview of available documentation for Linux and Windows Amazon EC2 clients:

- To create a Linux Amazon EC2 client, see [Getting Started with Amazon EC2 Linux Instances](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md").

For information about connecting to the running client, see the following topics:

    + [Connecting to your Linux Instance Using SSH](../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md "../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md")
    + [Connecting to Your Linux Instance from Windows Using PuTTY](../../../AWSEC2/latest/UserGuide/putty.md "../../../AWSEC2/latest/UserGuide/putty.md")

- To create a Windows Amazon EC2 client, see [Getting Started with Amazon EC2 Windows Instances](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md"). For more information about connecting to your Windows client, see [Connect to Your Windows Instance](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows").

###### Note

Your EC2 instance can run all of the AWS CLI commands contained in this guide. If the AWS CLI
is not installed, you can download it from [AWS Command Line Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"). If you are using Windows, you can download and run a 64-bit
or 32-bit Windows installer. If you are using Linux or macOS, you can install the
CLI using pip.

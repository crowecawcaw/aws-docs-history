# Listing and connecting to server instances

This topic explains how to view a list of the Amazon EC2 instances running your Elastic Beanstalk application environment and how to connect to them.

You can view a list of Amazon EC2 instances running your AWS Elastic Beanstalk application environment through the Elastic Beanstalk console. You can connect to the instances using
any SSH client. You can connect to the instances running Windows using Remote Desktop.

###### Important

Before you can access your Elastic Beanstalk–provisioned Amazon EC2 instances, you must create an Amazon EC2 key pair and configure your Elastic Beanstalk–provisioned
Amazon EC2instances to use the Amazon EC2 key pair. You can set up your Amazon EC2 key pairs using the [AWS Management
Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/"). For instructions on creating a key pair for Amazon EC2, see the _Amazon EC2 Getting Started Guide_. For more information on
how to configure your Amazon EC2 instances to use an Amazon EC2 key pair, see [EC2 key pair](using-features.managing.security.md#using-features.managing.security.keypair "using-features.managing.security.md#using-features.managing.security.keypair").

By default, Elastic Beanstalk does not enable remote connections to EC2 instances in a Windows container except for those in legacy Windows containers. (Elastic Beanstalk
configures EC2 instances in legacy Windows containers to use port 3389 for RDP connections.) You can enable remote connections to your EC2 instances
running Windows by adding a rule to a security group that authorizes inbound traffic to the instances. We strongly recommend that you remove the rule when
you end your remote connection. You can add the rule again the next time you need to log in remotely. For more information, see [Adding a Rule for Inbound
RDP Traffic to a Windows Instance](../../../AWSEC2/latest/WindowsGuide/authorizing-access-to-an-instance.md#authorizing-access-to-an-instance-rdp "../../../AWSEC2/latest/WindowsGuide/authorizing-access-to-an-instance.md#authorizing-access-to-an-instance-rdp") and [Connect to Your Windows Instance](../../../AWSEC2/latest/WindowsGuide/EC2Win_GetStarted.md#connecting_to_windows_instance "../../../AWSEC2/latest/WindowsGuide/EC2Win_GetStarted.md#connecting_to_windows_instance") in the
_Amazon Elastic Compute Cloud User Guide for Microsoft Windows_.

###### To view and connect to Amazon EC2 instances for an environment

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane of the console, choose **Load Balancers**.
3. Load balancers created by Elastic Beanstalk have **awseb** in the name. Find the load balancer for your environment and click it.
4. Choose the **Instances** tab in the bottom pane of the console.

A list of the instances that the load balancer for your Elastic Beanstalk environment uses is displayed. Make a note of an instance ID that you want to connect
to. 5. In the navigation pane of the Amazon EC2 console, choose **Instances**, and find your instance ID in the list. 6. Right-click the instance ID for the Amazon EC2 instance running in your environment's load balancer, and then select **Connect** from
the context menu. 7. Make a note of the instance's public DNS address on the **Description** tab. 8. Connect to an instance running Linux by using the SSH client of your choice, and then type **ssh -i .ec2/mykeypair.pem
ec2-user@<public-DNS-of-the-instance>** .
For more information on connecting to an Amazon EC2 Linux instance, see [Getting Started with Amazon EC2 Linux
Instances](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md") in the _Amazon EC2 User Guide_.

If your Elastic Beanstalk environment uses the [.NET on Windows Server platform](create_deploy_NET.container.console.md "create_deploy_NET.container.console.md"), see [Getting Started with Amazon EC2 Windows Instances](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md") in the _Amazon EC2 User Guide_.

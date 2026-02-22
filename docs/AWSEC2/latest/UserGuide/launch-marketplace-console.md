# Launch an Amazon EC2 instance from an AWS Marketplace

AMI

You can subscribe to an AWS Marketplace AMI and launch an instance from it using the Amazon EC2 console
or a command line tool. For more information about AWS Marketplace AMIs, see [Paid AMIs in the AWS Marketplace for Amazon EC2 instances](paid-amis.md "paid-amis.md").

To cancel your subscription to the AMI after launch, you must first terminate all
instances that were launched from the AMI. For more information, see [Manage your AWS Marketplace
subscriptions](marketplace-manage-subscriptions.md "marketplace-manage-subscriptions.md").

###### To launch an instance from an AWS Marketplace AMI using the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the Amazon EC2 console dashboard, choose **Launch
   instance**.
3. (Optional) Under **Name and tags**, for
   **Name**, enter a descriptive name for your
   instance.
4. Under **Application and OS Images (Amazon Machine
   Image)**, choose **Browse more AMIs**, and
   then choose the **AWS Marketplace AMIs** tab. Find a suitable AMI
   by browsing the categories or using the search functionality. To choose
   a product, choose **Select**.
5. A window opens with an overview of the product you've selected. You
   can view the pricing information, as well as any other information that
   the vendor has provided. When you're ready, choose **Subscribe and launch**.
   This will start your subscription immediately. While the subscription is underway, you can
   configure the instance by continuing with the steps in this
   procedure. If there are any problems with your credit card
   details, you will be asked to update your account
   details.

###### Note

You're not charged for using the product until you have launched
an instance with the AMI. Take note of the pricing for each
supported instance type when you select an instance type. Additional
taxes might also apply to the product. 6. For **Instance type**, select an instance type for
your instance. The instance type defines the hardware configuration and
size of the instance to launch. 7. Under **Key pair (login)**, for **Key pair
name**, choose an existing key pair or create a new
one. 8. Under **Network settings**, for **Firewall
(security groups)**, take note of the new security group
that was created according to the vendor's specifications for the
product. The security group might include rules that allow all IPv4
addresses (`0.0.0.0/0`) access on SSH (port 22) on Linux or
RDP (port 3389) on Windows. We recommend that you adjust these rules to
allow only a specific address or range of addresses to access your
instance over those ports. 9. You can use the other fields on the screen to configure your instance,
add storage, and add tags. For information about the different options
that you can configure, see [Reference for Amazon EC2 instance configuration parameters](ec2-instance-launch-parameters.md "ec2-instance-launch-parameters.md"). 10. In the **Summary** panel, under **Software
Image (AMI)**, check the details of the AMI from which
you're about to launch the instance. Also check the other configuration
details that you specified. When you're ready to launch your instance,
choose **Launch instance**. 11. Depending on the product you've subscribed to, the instance might take
a few minutes or more to launch. If there are any problems
with your credit card details, you will be asked to update your account
details. When the launch confirmation page displays, choose
**View all instances** to go to the
**Instances** page.

###### Note

You are charged the subscription price as long as your instance is
in the `running` state, even if it is idle. If your
instance is stopped, you might still be charged for storage. 12. When your instance is in the `running` state, you can
connect to it. To do this, select your instance in the list, choose
**Connect**, and choose a connection option. For
more information about connecting to your instance, see [Connect to your EC2 instance](connect.md "connect.md").

###### Important

Check the vendor's usage instructions carefully, as you might need
to use a specific username to connect to your instance. For
information about accessing your subscription details, see [Manage your AWS Marketplace
subscriptions](marketplace-manage-subscriptions.md "marketplace-manage-subscriptions.md"). 13. If the instance fails to launch or the state immediately goes to
`terminated` instead of `running`, see [Troubleshoot Amazon EC2 instance launch issues](troubleshooting-launch.md "troubleshooting-launch.md").

###### To launch an instance from an AWS Marketplace AMI using a command line tool

To launch instances from AWS Marketplace products using a command line tool, first
ensure that you are subscribed to the product. You can then launch an instance with
the product's AMI ID using the following methods:

| Method                           | Documentation                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS CLI                          | Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command, or see the following topic for<br>more information: [Launch<br>your instance](../../../cli/latest/userguide/cli-services-ec2-instances.md "../../../cli/latest/userguide/cli-services-ec2-instances.md") in the _AWS Command Line Interface User Guide_.         |
| AWS Tools for Windows PowerShell | Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") command, or see the following topic for<br>more information: [Launch an Amazon EC2 Instance Using Windows<br>PowerShell](../../../powershell/latest/userguide/pstools-ec2-launch.md "../../../powershell/latest/userguide/pstools-ec2-launch.md") |
| Query API                        | Use the [RunInstances](../APIReference/API_RunInstances.md "../APIReference/API_RunInstances.md") request.                                                                                                                                                                                                                                                                                                 |

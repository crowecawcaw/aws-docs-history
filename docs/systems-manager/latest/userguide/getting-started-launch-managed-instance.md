• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Perform a node task with

Systems Manager

Use this tutorial to get started with AWS Systems Manager. You'll learn how to launch an Amazon Elastic Compute Cloud
(Amazon EC2) instance that is managed by Systems Manager, and how to connect to the managed
instance.

Because Systems Manager is a collection of multiple tools, no single walkthrough or tutorial can
introduce the entire service. This tutorial provides an introduction to some of the
tools.

## Prerequisites

Before you begin, be sure that you've completed the steps in [Managing EC2 instances with Systems Manager](systems-manager-setting-up-ec2.md "systems-manager-setting-up-ec2.md").

## Launch an

instance using an AMI with SSM Agent preinstalled

You can launch an Amazon EC2 instance using the AWS Management Console as described in the following
procedure. This tutorial is intended to help you launch your first managed instance
quickly, so it doesn't cover all possible options.

###### To launch an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the EC2 console dashboard, in the **Launch instance**
   box, choose **Launch instance**, and then choose
   **Launch instance** from the options that appear.
3. For **Name and tags**, for **Name**, enter a
   descriptive name for your instance.
4. For **Application and OS Images (Amazon Machine Image)**, do
   the following:
   1. Choose the **Quick Start** tab, and then choose Amazon Linux.
      This is the operating system (OS) for your instance.
   2. For **Amazon Machine Image (AMI)**, choose an HVM
      version of Amazon Linux 2.

5. For **Instance type**, from the **Instance
   type** list, choose the hardware configuration for your instance.
   Choose the `t2.micro` instance type, which is selected by default.
   The `t2.micro` instance type is eligible for the AWS Free Tier. In
   AWS Regions where `t2.micro` is unavailable, you can use a
   `t3.micro` instance under the Free Tier. For more information,
   see [AWS Free Tier](https://aws.amazon.com/free "https://aws.amazon.com/free").
6. For **Key pair (login)**, for **Key pair
   name**, choose a key pair.
7. For **Network settings**, choose **Edit**.
   For **Security group name**, notice that the wizard created and
   selected a security group for you. You can use this security group, or
   alternatively you can select a security group that you created previously using
   the following steps:
   1. Choose **Select existing security group**.
   2. From **Common security groups**, choose your security
      group from the list of existing security groups.

8. If you aren't using Default Host Management Configuration, expand the
   **Advanced details** section, and for **IAM
   instance profile**, choose the instance profile that you created
   when getting set up in [Configure instance permissions required for
   Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md").
9. Keep the default selections for the other configuration settings for your
   instance.
10. Review a summary of your instance configuration in the
    **Summary** pane. When you're ready, choose
    **Launch instance**.
11. A confirmation page informs you that your instance is launching. Choose
    **View all instances** to close the confirmation page and
    return to the console.
12. On the **Instances** screen, you can view the status of the
    launch. It takes a short time for an instance to launch.
13. It can take a few minutes for the instance to show as managed and be ready for
    you to connect to it. To check that your instance passed its status checks, view
    this information in the **Status check** column.

## Connect to your managed

instance using Systems Manager

###### To connect to your managed instance

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose the button next to the instance that you want to connect to.
4. In the **Node actions** menu, choose **Start terminal
   session**.
5. Select **Connect**.

## Clean up your instance

If you're done working with the managed instance that you created for this tutorial,
terminate it. Terminating an instance effectively deletes it.

###### To terminate your instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**. In the list of
   instances, select the instance.
3. Choose **Instance state**, **Terminate
   instance**.
4. Choose **Terminate** when prompted for confirmation.

Amazon EC2 shuts down and terminates your instance. After your instance is
terminated, it remains visible on the console briefly, and then the entry is
deleted automatically. You can't remove the terminated instance from the console
display yourself.

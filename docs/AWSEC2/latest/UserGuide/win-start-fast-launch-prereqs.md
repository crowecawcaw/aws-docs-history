# EC2 Fast Launch prerequisites for Windows

Before you set up EC2 Fast Launch, verify that you've met the following
prerequisites that are required to create snapshots for the AMIs in your AWS account:

- If you provide a custom launch template when you configure EC2 Fast Launch,
  the service uses the VPC and other configuration settings that you've defined in
  the launch template. For more information, see [Use a launch template when you set up EC2 Fast Launch](win-fast-launch-configure.md#win-fast-launch-with-template "win-fast-launch-configure.md#win-fast-launch-with-template").
- If you don't use a custom launch template to configure your settings, you must attach the
  [EC2FastLaunchFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-EC2FastLaunchFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-EC2FastLaunchFullAccess") policy
  to your current IAM role before you enable EC2 Fast Launch. Then the service automatically
  creates an AWS CloudFormation stack with the following resources in your AWS account.
  - A virtual private cloud (VPC)
  - Private subnets across multiple Availability Zones
  - A launch template configured with Instance Metadata Service Version 2 (IMDSv2)
  - A security group with no inbound or outbound rules

- Private EC2 Fast Launch AMIs must support user data script execution.
- To configure EC2 Fast Launch for an AMI, you must create the AMI
  using **Sysprep** with the shutdown option. The EC2 Fast Launch feature
  doesn't currently support AMIs that were created from a running instance.

To create an AMI using **Sysprep**, see
[Create an Amazon EC2 AMI using Windows Sysprep](ami-create-win-sysprep.md "ami-create-win-sysprep.md").

- To enable EC2 Fast Launch for an [encrypted AMI](AMIEncryption.md "AMIEncryption.md")
  that uses a customer managed key for encryption, you must grant the service-linked role
  for EC2 Fast Launch permission to use the CMK. For more information, see
  [Access to customer managed keys](slr-windows-fast-launch.md#win-faster-launching-slr-access-to-cust-keys "slr-windows-fast-launch.md#win-faster-launching-slr-access-to-cust-keys").
- The default quota for **Max parallel launches** across all AMIs in an AWS account
  is 40 per Region. You can request a Service Quotas increase for your account, as follows.

      1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").
      2. In the navigation pane, choose AWS services.
      3. In the search bar, enter `EC2 Fast Launch`, and select the result.
      4. Select the link for **Parallel instance launches** to open
       the service quota detail page.
      5. Choose **Request increase at account level**.

  For more information, see
  [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md")
  in the _Service Quotas User Guide_.

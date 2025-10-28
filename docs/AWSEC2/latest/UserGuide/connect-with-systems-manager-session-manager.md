# Connect to your Amazon EC2 instance using Session Manager

Session Manager is a fully-managed AWS Systems Manager capability for managing your Amazon EC2 instances
through an interactive, one-click, browser-based shell, or through the AWS CLI. You can use
Session Manager to start a session with an instance in your account. After the session is
started, you can run interactive commands on the instance as you would for any other
connection type. For more information about Session Manager, see [AWS Systems Manager Session
Manager](../../../systems-manager/latest/userguide/session-manager.md "../../../systems-manager/latest/userguide/session-manager.md") in the _AWS Systems Manager User Guide_.

###### Prerequisites

Before you attempt to connect to an instance using Session Manager, you must complete
the required setup steps. For example, the instance must be managed by SSM and must
have an attached IAM role with the **AmazonSSMManagedInstanceCore**
policy. For more information, see [Setting up
Session Manager](../../../systems-manager/latest/userguide/session-manager-getting-started.md "../../../systems-manager/latest/userguide/session-manager-getting-started.md").

###### To connect to an Amazon EC2 instance using Session Manager on the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance and choose **Connect**.
4. For the connection method, choose **Session Manager**.
5. Choose **Connect** to start the session.

![The Connect button on the Session Manager tab.](images/connect-method-session-manager.png)

###### Troubleshooting

If you receive an error that you're not authorized to perform one or more
Systems Manager actions (`ssm:`command-name``),
you must update your policies to allow you to start sessions from the Amazon EC2
console. For more information and instructions, see [Quickstart default IAM policies for Session Manager](../../../systems-manager/latest/userguide/getting-started-restrict-access-quickstart.md "../../../systems-manager/latest/userguide/getting-started-restrict-access-quickstart.md") in the
_AWS Systems Manager User Guide_.

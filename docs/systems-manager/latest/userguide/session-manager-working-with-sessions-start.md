• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Start a

session

You can use the AWS Systems Manager console, the Amazon Elastic Compute Cloud (Amazon EC2) console, the AWS Command Line Interface
(AWS CLI), or SSH to start a session.

###### Topics

- [Starting a session (Systems Manager console)](#start-sys-console "#start-sys-console")
- [Starting a session (Amazon EC2
  console)](#start-ec2-console "#start-ec2-console")
- [Starting a session (AWS CLI)](#sessions-start-cli "#sessions-start-cli")
- [Starting a session (SSH)](#sessions-start-ssh "#sessions-start-ssh")
- [Starting a session (port
  forwarding)](#sessions-start-port-forwarding "#sessions-start-port-forwarding")
- [Starting a session (port
  forwarding to remote host)](#sessions-remote-port-forwarding "#sessions-remote-port-forwarding")
- [Starting a session
  (interactive and noninteractive commands)](#sessions-start-interactive-commands "#sessions-start-interactive-commands")

## Starting a session (Systems Manager console)

You can use the AWS Systems Manager console to start a session with a managed node in
your account.

###### Note

Before you start a session, make sure that you have completed the setup steps for
Session Manager. For information, see [Setting up Session Manager](session-manager-getting-started.md "session-manager-getting-started.md").

###### To start a session (Systems Manager console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Session Manager**.
3. Choose **Start session**.
4. (Optional) Enter a session description in the **Reason for
   session** field.
5. For **Target instances**, choose the option button to
   the left of the managed node that you want to connect to.

If the node that you want isn't in the list, or if you select a node
and receive a configuration error, see [Managed node not
available or not configured for Session Manager](session-manager-troubleshooting.md#session-manager-troubleshooting-instances "session-manager-troubleshooting.md#session-manager-troubleshooting-instances") for
troubleshooting steps. 6. Choose **Start session** to launch the session
immediately.

-or-

Choose **Next** for session options. 7. (Optional) For **Session document**, select the
document that you want to run when the session starts. If your document
supports runtime parameters, you can enter one or more comma-separated
values in each parameter field. 8. Choose **Next**. 9. Choose **Start session**.

After the connection is made, you can run bash commands (Linux
and macOS) or PowerShell commands (Windows) as
you would through any other connection type.

###### Important

If you want to allow users to specify a document when starting sessions in
the Session Manager console, note the following:

- You must grant users the `ssm:GetDocument` and
  `ssm:ListDocuments` permissions in their IAM
  policy. For more information, see [Grant
  access to custom Session documents in the console](getting-started-restrict-access-examples.md#grant-access-documents-console-example "getting-started-restrict-access-examples.md#grant-access-documents-console-example").
- The console only supports Session documents that have the
  `sessionType` defined as
  `Standard_Stream`. For more information, see [Session document schema](session-manager-schema.md "session-manager-schema.md").

## Starting a session (Amazon EC2

console)

You can use the Amazon Elastic Compute Cloud (Amazon EC2) console to start a session with an instance
in your account.

###### Note

If you receive an error that you aren't authorized to perform one or more
Systems Manager actions (`ssm:`command-name``,
then you must contact your administrator for assistance. Your administrator
is the person that provided you with your sign-in credentials. Ask that
person to update your policies to allow you to start sessions from the Amazon EC2
console. If you're an administrator, see [Sample IAM
policies for Session Manager](getting-started-restrict-access-quickstart.md "getting-started-restrict-access-quickstart.md") for more
information.

###### To start a session (Amazon EC2 console)

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance and choose **Connect**.
4. For **Connection method**, choose
   **Session Manager**.
5. Choose **Connect**.

After the connection is made, you can run bash commands (Linux
and macOS) or PowerShell commands (Windows) as
you would through any other connection type.

## Starting a session (AWS CLI)

Install and configure the AWS Command Line Interface (AWS CLI), if you haven't already.

For information, see [Installing or updating the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

Before you start a session, make sure that you have completed the setup steps for
Session Manager. For information, see [Setting up Session Manager](session-manager-getting-started.md "session-manager-getting-started.md").

To use the AWS CLI to run session commands, the Session Manager plugin must also be installed on your
local machine. For information, see [Install the Session Manager plugin
for the AWS CLI](session-manager-working-with-install-plugin.md "session-manager-working-with-install-plugin.md").

To start a session using the AWS CLI, run the following command replacing
`instance-id` with your own information.

```
aws ssm start-session \
    --target `instance-id`
```

For information about other options you can use with the
**start-session** command, see [start-session](../../../cli/latest/reference/ssm/start-session.md "../../../cli/latest/reference/ssm/start-session.md")
in the AWS Systems Manager section of the AWS CLI Command Reference.

## Starting a session (SSH)

To start a Session Manager SSH session, version 2.3.672.0 or later of SSM Agent must
be installed on the managed node.

###### SSH connection requirements

Take note of the following requirements and limitations for session
connections using SSH through Session Manager:

- Your target managed node must be configured to support SSH
  connections. For more information, see [(Optional) Allow and control permissions for SSH connections through Session Manager](session-manager-getting-started-enable-ssh-connections.md "session-manager-getting-started-enable-ssh-connections.md").
- You must connect using the managed node account associated with the
  Privacy Enhanced Mail (PEM) certificate, not the `ssm-user`
  account that is used for other types of session connections. For
  example, on EC2 instances for Linux and macOS, the
  default user is `ec2-user`. For information about identifying
  the default user for each instance type, see [Get Information About Your Instance](../../../AWSEC2/latest/UserGuide/connection-prereqs.md#connection-prereqs-get-info-about-instance "../../../AWSEC2/latest/UserGuide/connection-prereqs.md#connection-prereqs-get-info-about-instance") in the
  _Amazon EC2 User Guide_.
- Logging isn't available for Session Manager sessions that connect through port forwarding or
  SSH. This is because SSH encrypts all session data within the secure TLS connection established between the AWS CLI
  and Session Manager endpoints, and Session Manager only serves as a tunnel for
  SSH connections.

###### Note

Before you start a session, make sure that you have completed the setup steps for
Session Manager. For information, see [Setting up Session Manager](session-manager-getting-started.md "session-manager-getting-started.md").

To start a session using SSH, run the following command. Replace each
`example resource placeholder` with your own
information.

```
ssh -i `/path/my-key-pair.pem` `username@instance-id`
```

###### Tip

When you start a session using SSH, you can copy local files to the target
managed node using the following command format.

```
scp -i `/path/my-key-pair.pem /path/ExampleFile.txt username@instance-id:~`
```

For information about other options you can use with the
**start-session** command, see [start-session](../../../cli/latest/reference/ssm/start-session.md "../../../cli/latest/reference/ssm/start-session.md")
in the AWS Systems Manager section of the AWS CLI Command Reference.

## Starting a session (port

forwarding)

To start a Session Manager port forwarding session, version 2.3.672.0 or later of
SSM Agent must be installed on the managed node.

###### Note

Before you start a session, make sure that you have completed the setup steps for
Session Manager. For information, see [Setting up Session Manager](session-manager-getting-started.md "session-manager-getting-started.md").

To use the AWS CLI to run session commands, you must install the Session Manager plugin on
your local machine. For information, see [Install the Session Manager plugin
for the AWS CLI](session-manager-working-with-install-plugin.md "session-manager-working-with-install-plugin.md").

Depending on your operating system and command line tool, the placement of
quotation marks can differ and escape characters might be required.

To start a port forwarding session, run the following command from the CLI.
Replace each `example resource placeholder` with your
own information.

Linux & macOS

```
aws ssm start-session \
    --target `instance-id` \
    --document-name AWS-StartPortForwardingSession \
    --parameters '{"portNumber":["`80`"], "localPortNumber":["`56789`"]}'
```

Windows

```
aws ssm start-session ^
    --target `instance-id` ^
    --document-name AWS-StartPortForwardingSession ^
    --parameters portNumber="`3389`",localPortNumber="`56789`"
```

`portNumber` is the remote port on the managed node where you want
the session traffic to be redirected. For example, you might specify port
`3389` for connecting to a Windows node using the
Remote Desktop Protocol (RDP). If you don't specify the `portNumber`
parameter, Session Manager uses `80` as the default value.

`localPortNumber` is the port on your local computer where traffic
starts, such as `56789`. This value is what you enter when connecting
to a managed node using a client. For example,
`localhost:56789`.

For information about other options you can use with the
**start-session** command, see [start-session](../../../cli/latest/reference/ssm/start-session.md "../../../cli/latest/reference/ssm/start-session.md")
in the AWS Systems Manager section of the AWS CLI Command Reference.

For more information about port forwarding sessions, see [Port Forwarding Using AWS Systems Manager Session Manager](https://aws.amazon.com/blogs/aws/new-port-forwarding-using-aws-system-manager-sessions-manager/ "https://aws.amazon.com/blogs/aws/new-port-forwarding-using-aws-system-manager-sessions-manager/") in the _AWS News Blog_.

## Starting a session (port

forwarding to remote host)

To start a Session Manager port forwarding session to a remote host, version
3.1.1374.0 or later of SSM Agent must be installed on the managed node. The
remote host isn't required to be managed by Systems Manager.

###### Note

Before you start a session, make sure that you have completed the setup steps for
Session Manager. For information, see [Setting up Session Manager](session-manager-getting-started.md "session-manager-getting-started.md").

To use the AWS CLI to run session commands, you must install the Session Manager plugin on
your local machine. For information, see [Install the Session Manager plugin
for the AWS CLI](session-manager-working-with-install-plugin.md "session-manager-working-with-install-plugin.md").

Depending on your operating system and command line tool, the placement of
quotation marks can differ and escape characters might be required.

To start a port forwarding session, run the following command from the AWS CLI.
Replace each `example resource placeholder` with your
own information.

Linux & macOS

```
aws ssm start-session \
    --target `instance-id` \
    --document-name AWS-StartPortForwardingSessionToRemoteHost \
    --parameters '{"host":["`mydb.example.us-east-2.rds.amazonaws.com`"],"portNumber":["`3306`"], "localPortNumber":["`3306`"]}'
```

Windows

```
aws ssm start-session ^
    --target `instance-id` ^
    --document-name AWS-StartPortForwardingSessionToRemoteHost ^
    --parameters host="`mydb.example.us-east-2.rds.amazonaws.com`",portNumber="`3306`",localPortNumber="`3306`"
```

The `host` value represents the hostname or IP address of the
remote host that you want to connect to. General connectivity and name
resolution requirements between the managed node and the remote host still
apply.

`portNumber` is the remote port on the managed node where you want
the session traffic to be redirected. For example, you might specify port
`3389` for connecting to a Windows node using the
Remote Desktop Protocol (RDP). If you don't specify the `portNumber`
parameter, Session Manager uses `80` as the default value.

`localPortNumber` is the port on your local computer where traffic
starts, such as `56789`. This value is what you enter when connecting
to a managed node using a client. For example,
`localhost:56789`.

For information about other options you can use with the
**start-session** command, see [start-session](../../../cli/latest/reference/ssm/start-session.md "../../../cli/latest/reference/ssm/start-session.md")
in the AWS Systems Manager section of the AWS CLI Command Reference.

### Starting a

session with an Amazon ECS task

Session Manager supports starting a port forwarding session with a task inside an
Amazon Elastic Container Service (Amazon ECS) cluster. To do so, enable ECS Exec. For more information,
see [Monitor Amazon Elastic Container Service
containers with ECS Exec](../../../AmazonECS/latest/developerguide/ecs-exec.md "../../../AmazonECS/latest/developerguide/ecs-exec.md") in the
_Amazon Elastic Container Service Developer Guide_.

You must also update the task role in IAM to include the following
permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssmmessages:CreateControlChannel",
 "ssmmessages:CreateDataChannel",
 "ssmmessages:OpenControlChannel",
 "ssmmessages:OpenDataChannel"
 ],
 "Resource": "*"
 }
 ]
}`

```

To start a port forwarding session with an Amazon ECS task, run the following
command from the AWS CLI. Replace each `example resource
 placeholder` with your own information.

###### Note

Remove the < and > symbols from the `target`
parameter. These symbols are provided for reader clarification
only.

Linux & macOS

```
aws ssm start-session \
    --target ecs:<`ECS_cluster_name`>_<`ECS_container_ID`>_<`container_runtime_ID`> \
    --document-name AWS-StartPortForwardingSessionToRemoteHost \
    --parameters '{"host":["`URL`"],"portNumber":["`port_number`"], "localPortNumber":["`port_number`"]}'
```

Windows

```
aws ssm start-session ^
    --target ecs:<`ECS_cluster_name`>_<`ECS_container_ID`>_<`container_runtime_ID`> ^
    --document-name AWS-StartPortForwardingSessionToRemoteHost ^
    --parameters host="`URL`",portNumber="`port_number`",localPortNumber="`port_number`"
```

## Starting a session

(interactive and noninteractive commands)

Before you start a session, make sure that you have completed the setup steps for
Session Manager. For information, see [Setting up Session Manager](session-manager-getting-started.md "session-manager-getting-started.md").

To use the AWS CLI to run session commands, the Session Manager plugin must also be installed
on your local machine. For information, see [Install the Session Manager plugin
for the AWS CLI](session-manager-working-with-install-plugin.md "session-manager-working-with-install-plugin.md").

To start an interactive command session, run the following command. Replace
each `example resource placeholder` with your own
information.

Linux & macOS

```
aws ssm start-session \
    --target `instance-id` \
    --document-name `CustomCommandSessionDocument` \
    --parameters '{"logpath":["/var/log/amazon/ssm/amazon-ssm-agent.log"]}'
```

Windows

```
aws ssm start-session ^
    --target `instance-id` ^
    --document-name `CustomCommandSessionDocument` ^
    --parameters logpath="/var/log/amazon/ssm/amazon-ssm-agent.log"
```

For information about other options you can use with the
**start-session** command, see [start-session](../../../cli/latest/reference/ssm/start-session.md "../../../cli/latest/reference/ssm/start-session.md")
in the AWS Systems Manager section of the AWS CLI Command Reference.

**More info**

- [Use port forwarding in AWS Systems Manager Session Manager to connect
  to remote hosts](https://aws.amazon.com/blogs/mt/use-port-forwarding-in-aws-systems-manager-session-manager-to-connect-to-remote-hosts/ "https://aws.amazon.com/blogs/mt/use-port-forwarding-in-aws-systems-manager-session-manager-to-connect-to-remote-hosts/")
- [Amazon EC2 instance port forwarding with AWS Systems Manager](https://aws.amazon.com/blogs/mt/amazon-ec2-instance-port-forwarding-with-aws-systems-manager/ "https://aws.amazon.com/blogs/mt/amazon-ec2-instance-port-forwarding-with-aws-systems-manager/")
- [Manage AWS Managed Microsoft AD resources with Session Manager
  port forwarding](https://aws.amazon.com/blogs/mt/manage-aws-managed-microsoft-ad-resources-with-session-manager-port-forwarding/ "https://aws.amazon.com/blogs/mt/manage-aws-managed-microsoft-ad-resources-with-session-manager-port-forwarding/")
- [Port Forwarding Using AWS Systems Manager Session Manager](https://aws.amazon.com/blogs/aws/new-port-forwarding-using-aws-system-manager-sessions-manager/ "https://aws.amazon.com/blogs/aws/new-port-forwarding-using-aws-system-manager-sessions-manager/") on
  the _AWS News Blog_.

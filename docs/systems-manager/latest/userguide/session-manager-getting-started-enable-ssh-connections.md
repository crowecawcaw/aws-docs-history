AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Step 8:

(Optional) Allow and control permissions for SSH connections through
Session Manager

You can allow users in your AWS account to use the AWS Command Line Interface (AWS CLI) to
establish Secure Shell (SSH) connections to managed nodes using AWS Systems Manager Session Manager.
Users who connect using SSH can also copy files between their local machines and
managed nodes using Secure Copy Protocol (SCP). You can use this functionality to
connect to managed nodes without opening inbound ports or maintaining bastion
hosts.

When you establish SSH connections through Session Manager, the AWS CLI and SSM Agent
create secure WebSocket connections over TLS to Session Manager endpoints. The SSH session
runs within this encrypted tunnel, providing an additional layer of security without
requiring inbound ports to be opened on your managed nodes.

After allowing SSH connections, you can use AWS Identity and Access Management (IAM) policies to
explicitly allow or deny users, groups, or roles to make SSH connections using
Session Manager.

###### Note

Logging isn't available for Session Manager sessions that connect through port forwarding or
SSH. This is because SSH encrypts all session data within the secure TLS connection established between the AWS CLI
and Session Manager endpoints, and Session Manager only serves as a tunnel for
SSH connections.

###### Topics

- [Allowing SSH connections for Session Manager](#ssh-connections-enable "#ssh-connections-enable")
- [Controlling user permissions for
  SSH connections through Session Manager](#ssh-connections-permissions "#ssh-connections-permissions")

## Allowing SSH connections for Session Manager

Use the following steps to allow SSH connections through Session Manager on a managed
node.

###### To allow SSH connections for Session Manager

1.  On the managed node to which you want to allow SSH connections, do the
    following:
    - Ensure that SSH is running on the managed node. (You can close
      inbound ports on the node.)
    - Ensure that SSM Agent version 2.3.672.0 or later is installed
      on the managed node.

    For information about installing or updating SSM Agent on a
    managed node, see the following topics:

        + [Manually installing and
         uninstalling SSM Agent on EC2 instances for Windows Server](manually-install-ssm-agent-windows.md "manually-install-ssm-agent-windows.md").
        + [Manually installing and
         uninstalling SSM Agent on EC2 instances for Linux](manually-install-ssm-agent-linux.md "manually-install-ssm-agent-linux.md")
        + [Manually installing and
         uninstalling SSM Agent on EC2 instances for macOS](manually-install-ssm-agent-macos.md "manually-install-ssm-agent-macos.md")
        + [How to install the SSM Agent on hybrid Windows nodes](hybrid-multicloud-ssm-agent-install-windows.md "hybrid-multicloud-ssm-agent-install-windows.md")
        + [How to install the SSM Agent on hybrid Linux nodes](hybrid-multicloud-ssm-agent-install-linux.md "hybrid-multicloud-ssm-agent-install-linux.md")

    ###### Note

    To use Session Manager with on-premises servers, edge devices,
    and virtual machines (VMs) that you activated as managed
    nodes, you must use the advanced-instances tier. For more
    information about advanced instances, see [Configuring instance
    tiers](fleet-manager-configure-instance-tiers.md "fleet-manager-configure-instance-tiers.md").

2.  On the local machine from which you want to connect to a managed node
    using SSH, do the following:
    - Ensure that version 1.1.23.0 or later of the Session Manager plugin is
      installed.

    For information about installing the Session Manager plugin, see [Install the Session Manager plugin
    for the AWS CLI](session-manager-working-with-install-plugin.md "session-manager-working-with-install-plugin.md").
    - Update the SSH configuration file to allow running a proxy
      command that starts a Session Manager session and transfer all data
      through the connection.

    **Linux and
    macOS**

    ###### Tip

    The SSH configuration file is typically located at
    `~/.ssh/config`.

    Add the following to the configuration file on the local
    machine.

    ```
    # SSH over Session Manager
    Host i-* mi-*
        ProxyCommand sh -c "aws ssm start-session --target %h --document-name AWS-StartSSHSession --parameters 'portNumber=%p'"
        User ec2-user
    ```

    **Windows**

    ###### Tip

    The SSH configuration file is typically located at
    `C:\Users\`<username>`\.ssh\config`.

    Add the following to the configuration file on the local
    machine.

    ```
    # SSH over Session Manager
    Host i-* mi-*
        ProxyCommand C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe "aws ssm start-session --target %h --document-name AWS-StartSSHSession --parameters portNumber=%p"
    ```

    - Create or verify that you have a Privacy Enhanced Mail
      certificate (a PEM file), or at minimum a public key, to use
      when establishing connections to managed nodes. This must be a
      key that is already associated with the managed node. The
      permissions of your private key file must be set so that only
      you can read it. You can use the following command to set the
      permissions of your private key file so that only you can read
      it.

    ```
    chmod 400 `<my-key-pair>`.pem
    ```

    For example, for an Amazon Elastic Compute Cloud (Amazon EC2) instance, the key pair
    file you created or selected when you created the instance. (You
    specify the path to the certificate or key as part of the
    command to start a session. For information about starting a
    session using SSH, see [Starting a session (SSH)](session-manager-working-with-sessions-start.md#sessions-start-ssh "session-manager-working-with-sessions-start.md#sessions-start-ssh").)

## Controlling user permissions for

SSH connections through Session Manager

After you enable SSH connections through Session Manager on a managed node, you can
use IAM policies to allow or deny users, groups, or roles the ability to make
SSH connections through Session Manager.

###### To use an IAM policy to allow SSH connections through Session Manager

- Use one of the following options:
  - **Option 1**: Open the IAM
    console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").

  In the navigation pane, choose **Policies**,
  and then update the permissions policy for the user or role you
  want to allow to start SSH connections through Session Manager.

  For example, add the following element to the Quickstart
  policy you created in [Quickstart end user
  policies for Session Manager](getting-started-restrict-access-quickstart.md#restrict-access-quickstart-end-user "getting-started-restrict-access-quickstart.md#restrict-access-quickstart-end-user").
  Replace each `example resource
 placeholder` with your own information.

  JSON

  ```
  `{
   "Version":"2012-10-17",
   "Statement": [
   {
   "Effect": "Allow",
   "Action": "ssm:StartSession",
   "Resource": [
   "arn:aws:ec2:`us-east-1`:`111122223333`:instance/`instance-id`",
   "arn:aws:ssm:*:*:document/AWS-StartSSHSession"
   ]
   },
   {
   "Effect": "Allow",
   "Action": "ssmmessages:OpenDataChannel",
   "Resource": "arn:aws:ssm:*:*:session/${aws:userid}-*"
   }
   ]
  }`

  ```

  - **Option 2**: Attach an inline
    policy to a user policy by using the AWS Management Console, the AWS CLI, or
    the AWS API.

  Using the method of your choice, attach the policy statement
  in **Option 1** to the policy for
  an AWS user, group, or role.

  For information, see [Adding and Removing IAM Identity Permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in
  the _IAM User Guide_.

###### To use an IAM policy to deny SSH connections through Session Manager

- Use one of the following options:
  - **Option 1**: Open the IAM
    console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"). In the navigation pane,
    choose **Policies**, and then update the
    permissions policy for the user or role to block from starting
    Session Manager sessions.

  For example, add the following element to the Quickstart
  policy you created in [Quickstart end user
  policies for Session Manager](getting-started-restrict-access-quickstart.md#restrict-access-quickstart-end-user "getting-started-restrict-access-quickstart.md#restrict-access-quickstart-end-user").

  JSON

  ```
  `{
   "Version":"2012-10-17",
   "Statement": [
   {
   "Effect": "Deny",
   "Action": "ssm:StartSession",
   "Resource": "arn:aws:ssm:*:*:document/AWS-StartSSHSession"
   },
   {
   "Effect": "Allow",
   "Action": "ssmmessages:OpenDataChannel",
   "Resource": "arn:aws:ssm:*:*:session/${aws:userid}-*"
   }
   ]
  }`

  ```

  - **Option 2**: Attach an inline
    policy to a user policy by using the AWS Management Console, the AWS CLI, or
    the AWS API.

  Using the method of your choice, attach the policy statement
  in **Option 1** to the policy for
  an AWS user, group, or role.

  For information, see [Adding and Removing IAM Identity Permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in
  the _IAM User Guide_.

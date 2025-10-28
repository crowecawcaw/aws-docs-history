# Connect to an Amazon EC2 instance using

EC2 Instance Connect Endpoint

You can use EC2 Instance Connect Endpoint to connect to an Amazon EC2 instance that supports SSH or
RDP.

###### Prerequisites

- You must have the required IAM permission to connect to an EC2 Instance Connect Endpoint.
  For more information, see [Permissions to use EC2 Instance Connect Endpoint to connect to
  instances](permissions-for-ec2-instance-connect-endpoint.md#iam-OpenTunnel "permissions-for-ec2-instance-connect-endpoint.md#iam-OpenTunnel").
- The EC2 Instance Connect Endpoint must be in one of the following states:
  - **create-complete** for a new endpoint
  - **update-in-progress**,
    **update-complete**, or
    **update-failed** for an existing endpoint being
    modified. When modifying an endpoint, it continues using its original
    configuration until the status changes to
    **update-complete**.

  If your VPC doesn't have an EC2 Instance Connect Endpoint, you can create one. For
  more information, see [Create an EC2 Instance Connect Endpoint](create-ec2-instance-connect-endpoints.md "create-ec2-instance-connect-endpoints.md").

- The EC2 Instance Connect Endpoint IP address type must be compatible with the IP address type
  of the instance. If your endpoint IP address type is dual-stack, then it can
  work for both IPv4 and IPv6 addresses.
- (Linux instances) To use the Amazon EC2 console to connect to your instance, or to
  use the CLI to connect and have EC2 Instance Connect handle the ephemeral key, your
  instance must have EC2 Instance Connect installed. For more information, see [Install
  EC2 Instance Connect](ec2-instance-connect-set-up.md "ec2-instance-connect-set-up.md").
- Ensure that the security group of the instance allows inbound SSH traffic from
  the EC2 Instance Connect Endpoint. For more information, see [Target instance security group
  rules](eice-security-groups.md#resource-security-group-rules "eice-security-groups.md#resource-security-group-rules").

###### Connection options

- [Connect to your Linux instance using
  the Amazon EC2 console](#connect-using-the-ec2-console "#connect-using-the-ec2-console")
- [Connect to your Linux instance using
  SSH](#eic-connect-using-ssh "#eic-connect-using-ssh")
- [Connect to your Linux instance with its
  instance ID using the AWS CLI](#eic-connect-using-cli "#eic-connect-using-cli")
- [Connect to your Windows instance using
  RDP](#eic-connect-using-rdp "#eic-connect-using-rdp")
- [Troubleshoot](#troubleshoot-eice "#troubleshoot-eice")

## Connect to your Linux instance using

the Amazon EC2 console

You can connect to an instance using the Amazon EC2 console (a browser-based client) as
follows.

###### To connect to your instance using the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance, and then choose **Connect**.
4. Choose the **EC2 Instance Connect** tab.
5. For **Connection type**, choose **Connect using a
   Private IP**.
6. Choose either **Private IPv4 address** or **IPv6
   address**. The options are available based on the IP addresses
   assigned to your instance. If an option is greyed out, your instance does
   not have an IP address of that type assigned to it.
7. For **EC2 Instance Connect Endpoint**, choose the ID of
   the EC2 Instance Connect Endpoint.

###### Note

The EC2 Instance Connect Endpoint must be compatible with the IP address you chose in
the previous step. If your endpoint IP address type is dual-stack, then
it can work for both IPv4 and IPv6 addresses. For more information, see
[Create an EC2 Instance Connect Endpoint](create-ec2-instance-connect-endpoints.md "create-ec2-instance-connect-endpoints.md"). 8. For **Username**, if the AMI that you used to launch the
instance uses a username other than `ec2-user`, enter the correct
username. 9. For **Max tunnel duration (seconds)**, enter the maximum
allowed duration for the SSH connection.

The duration must comply with any `maxTunnelDuration` condition
specified in the IAM policy. If you don't have access to the IAM policy,
contact your administrator. 10. Choose **Connect**. This opens a terminal window for your
instance.

## Connect to your Linux instance using

SSH

You can use SSH to connect to your Linux instance, and use the
`open-tunnel` command to establish a private tunnel. You can use
`open-tunnel` in single connection or multi-connection mode. You can
specify your instance ID, a private IPv4 address, or an IPv6 address.

For information about using the AWS CLI to connect to your instance using SSH, see
[Connect using the AWS CLI](ec2-instance-connect-methods.md#connect-linux-inst-eic-cli-ssh "ec2-instance-connect-methods.md#connect-linux-inst-eic-cli-ssh").

The following examples use [OpenSSH](https://www.openssh.com/ "https://www.openssh.com/").
You can use any other SSH client that supports a proxy mode.

### Single connection

**To allow only a single connection to an instance using
SSH and the `open-tunnel` command**

Use `ssh` and the [open-tunnel](../../../cli/latest/reference/ec2-instance-connect/open-tunnel.md "../../../cli/latest/reference/ec2-instance-connect/open-tunnel.md") AWS CLI command as follows. The
`-o` proxy command encloses the `open-tunnel` command
that creates the private tunnel to the instance.

```
ssh -i `my-key-pair`.pem `ec2-user`@`i-1234567890abcdef0` \
    -o ProxyCommand='aws ec2-instance-connect open-tunnel --instance-id `i-1234567890abcdef0`'
```

For:

- `-i` – Specify the key pair that was used to launch
  the instance.
- ``ec2-user`@`i-1234567890abcdef0``
  – Specify the username of the AMI that was used to launch the
  instance, and the instance ID. For instances with an IPv6 address, you
  must specify the IPv6 address instead of the instance ID.
- `--instance-id` – Specify the ID of the instance to
  connect to. Alternatively, specify `%h`, which extracts the
  instance ID from the user. For instances with an IPv6 address, replace
  `--instance-id
`i-1234567890abcdef0`` with
`--private-ip-address
`2001:db8::1234:5678:1.2.3.4``.

### Multi-connection

To allow multiple connections to an instance, first run the [open-tunnel](../../../cli/latest/reference/ec2-instance-connect/open-tunnel.md "../../../cli/latest/reference/ec2-instance-connect/open-tunnel.md") AWS CLI command to start listening for
new TCP connections, and then use `ssh` to create a new TCP
connection and a private tunnel to your instance.

###### To allow multiple connections to your instance using SSH and the

`open-tunnel` command

1. Run the following command to start listening for new TCP connections
   on the specified port on your local machine.

```
aws ec2-instance-connect open-tunnel \
    --instance-id `i-1234567890abcdef0` \
    --local-port `8888`
```

Expected output:

```
Listening for connections on port 8888.
```

2. In a _new terminal window_, run the
   following `ssh` command to create a new TCP connection and a
   private tunnel to your instance.

```
ssh -i `my-key-pair`.pem ec2-user@localhost -p `8888`
```

Expected output – In the _first_ terminal window, you'll see the following:

```
[1] Accepted new tcp connection, opening websocket tunnel.
```

You might also see the following:

```
[1] Closing tcp connection.
```

## Connect to your Linux instance with its

instance ID using the AWS CLI

If you only know your instance ID, you can use the [ec2-instance-connect
ssh](../../../cli/latest/reference/ec2-instance-connect/ssh.md "../../../cli/latest/reference/ec2-instance-connect/ssh.md") AWS CLI command to connect to your instance using an SSH client. For
more information, see [Connect using the AWS CLI](ec2-instance-connect-methods.md#connect-linux-inst-eic-cli-ssh "ec2-instance-connect-methods.md#connect-linux-inst-eic-cli-ssh").

###### Prerequisites

- Install AWS CLI version 2 and configure it using your credentials. For more
  information, see [Install or
  update to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") and [Configure the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the
  _AWS Command Line Interface User Guide_.
- Alternatively, open AWS CloudShell and run AWS CLI commands in its
  pre-authenticated shell.

###### To connect to an instance using the instance ID and an EC2 Instance Connect Endpoint

If you only know the instance ID, use the [ec2-instance-connect
ssh](../../../cli/latest/reference/ec2-instance-connect/ssh.md "../../../cli/latest/reference/ec2-instance-connect/ssh.md") CLI command, and specify the `ssh` command, the
instance ID, and the `--connection-type` parameter with the
`eice` value to use an EC2 Instance Connect Endpoint. If the instance only has
an IPv6 address, you must also include the `--instance-ip` parameter
with the IPv6 address.

- If the instance has a private IPv4 address (it can also have an IPv6
  address) use the following command and parameters:

```
aws ec2-instance-connect ssh \
    --instance-id `i-1234567890example` \
    --os-user `ec2-user` \
    --connection-type eice
```

- If the instance only has an IPv6 address, include the
  `--instance-ip` parameter with the IPv6 address:

```
aws ec2-instance-connect ssh \
    --instance-id `i-1234567890example` \
    --instance-ip `2001:db8::1234:5678:1.2.3.4` \
    --os-user `ec2-user` \
    --connection-type eice
```

###### Tip

If you get an error, make sure that you're using AWS CLI version 2. The
`ssh` parameter is only available in AWS CLI version 2. For more
information, see [About
AWS CLI version 2](../../../cli/latest/userguide/cli-chap-welcome.md#welcome-versions-v2 "../../../cli/latest/userguide/cli-chap-welcome.md#welcome-versions-v2") in the _AWS Command Line Interface User Guide_.

## Connect to your Windows instance using

RDP

You can use Remote Desktop Protocol (RDP) over EC2 Instance Connect Endpoint to connect to a
Windows instance without a public IPv4 address or public DNS name.

###### To connect to your Windows instance using an RDP client

1. Complete Steps 1 – 8 in [Connect to your
   Windows instance using RDP](connect-rdp.md "connect-rdp.md"). After downloading the RDP desktop
   file at Step 8, you'll get an **Unable to connect**
   message, which is to be expected because your instance does not have a
   public IP address.
2. Run the following command to establish a private tunnel to the VPC in
   which the instance is located. `--remote-port` must be
   `3389` because RDP uses port 3389 by default.

```
aws ec2-instance-connect open-tunnel \
    --instance-id `i-1234567890abcdef0` \
    --remote-port 3389 \
    --local-port `any-port`
```

3. In your **Downloads** folder, find the RDP desktop file
   that you downloaded, and drag it onto the RDP client window.
4. Right-click the RDP desktop file and choose
   **Edit**.
5. In the **Edit PC** window, for **PC
   name** (the instance to connect to), enter
   `localhost:`local-port`, where
`local-port`` uses the same
   value as you specified in Step 2, and then choose
   **Save**.

Note that the following screenshot of the **Edit PC**
window is from Microsoft Remote Desktop on a Mac. If you are using a Windows
client, the window might be different.

![The RDP client with the example "localhost:5555" in the PC name field.](images/ec2-instance-connect-endpoint-rdp.png) 6. In the RDP client, right-click the PC (that you just configured) and
choose **Connect** to connect to your instance. 7. At the prompt, enter the decrypted password for the administrator
account.

## Troubleshoot

Use the following information to help diagnose and fix issues that you might
encounter when using EC2 Instance Connect Endpoint to connect an instance.

### Can't connect to your instance

The following are common reasons why you might not be able to connect to your
instance.

- Security groups – Check the security groups assigned to the
  EC2 Instance Connect Endpoint and your instance. For more information about the
  required security group rules, see [Security groups for EC2 Instance Connect Endpoint](eice-security-groups.md "eice-security-groups.md").
- Instance state – Verify that your instance is in the
  `running` state.
- Key pair – If the command you're using to connect requires a
  private key, verify that your instance has a public key and that you
  have the corresponding private key.
- IAM permissions – Verify that you have the required IAM
  permissions. For more information, see [Grant permissions to use
  EC2 Instance Connect Endpoint](permissions-for-ec2-instance-connect-endpoint.md "permissions-for-ec2-instance-connect-endpoint.md").

For more troubleshooting tips for Linux instances, see [Troubleshoot issues connecting to your Amazon EC2 Linux instance](TroubleshootingInstancesConnecting.md "TroubleshootingInstancesConnecting.md"). For troubleshooting
tips for Windows instances, see [Troubleshoot issues connecting to your Amazon EC2 Windows instance](troubleshoot-connect-windows-instance.md "troubleshoot-connect-windows-instance.md").

### ErrorCode: AccessDeniedException

If you receive an `AccessDeniedException` error, and the
`maxTunnelDuration` condition is specified in the IAM policy, be
sure to specify the `--max-tunnel-duration` parameter when connecting
to an instance. For more information about this parameter, see [open-tunnel](../../../cli/latest/reference/ec2-instance-connect/open-tunnel.md "../../../cli/latest/reference/ec2-instance-connect/open-tunnel.md") in the _AWS CLI Command Reference_.

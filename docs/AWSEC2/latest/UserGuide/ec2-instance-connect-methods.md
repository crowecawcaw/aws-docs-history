# Connect to a Linux instance using

EC2 Instance Connect

The following instructions explain how to connect to your Linux instance using EC2 Instance Connect
through the Amazon EC2 console, the AWS CLI, or an SSH client.

When you connect to an instance using EC2 Instance Connect through the console or AWS CLI, the
EC2 Instance Connect API automatically pushes an SSH public key to the [instance metadata](ec2-instance-metadata.md "ec2-instance-metadata.md") where it remains for 60
seconds. An IAM policy attached to your user authorizes this action. If you prefer
using your own SSH key, you can use an SSH client and explicitly push your SSH key to
the instance using EC2 Instance Connect.

###### Considerations

After connecting to an instance using EC2 Instance Connect, the connection persists until the SSH
session is terminated. The duration of the connection is not determined by the
duration of your IAM credentials. If your IAM credentials expire, the connection
continues to persist. When using the EC2 Instance Connect console experience, if your IAM
credentials expire, terminate the connection by closing the browser page. When using
your own SSH client and EC2 Instance Connect to push your key, you can set a SSH timeout
value to terminate the SSH session automatically.

###### Requirements

Before you begin, be sure to review the [prerequisites](ec2-instance-connect-prerequisites.md "ec2-instance-connect-prerequisites.md").

###### Connection options

- [Connect using the Amazon EC2
  console](#ec2-instance-connect-connecting-console "#ec2-instance-connect-connecting-console")
- [Connect using the AWS CLI](#connect-linux-inst-eic-cli-ssh "#connect-linux-inst-eic-cli-ssh")
- [Connect using your own key
  and SSH client](#ec2-instance-connect-connecting-aws-cli "#ec2-instance-connect-connecting-aws-cli")
- [Troubleshoot](#ic-troubleshoot "#ic-troubleshoot")

## Connect using the Amazon EC2

console

You can connect to an instance using EC2 Instance Connect through the Amazon EC2 console.

###### Requirements

To connect using the Amazon EC2 console, the instance must have either a public IPv4 or IPv6
address. If the instance only has a private IPv4 address, you can use the [ec2-instance-connect AWS CLI](#connect-linux-inst-eic-cli-ssh "#connect-linux-inst-eic-cli-ssh")
to connect.

###### To connect to your instance using the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance and choose **Connect**.
4. Choose the **EC2 Instance Connect** tab.
5. Choose **Connect using a Public IP**.
6. If there is a choice, select the IP address to connect to. Otherwise, the
   IP address is selected automatically.
7. For **Username**, verify the username.
8. Choose **Connect** to establish a connection. An in-browser terminal
   window opens.

## Connect using the AWS CLI

You can use the [ec2-instance-connect](../../../cli/latest/reference/ec2-instance-connect/index.md "../../../cli/latest/reference/ec2-instance-connect/index.md") AWS CLI to connect to your instance with an SSH
client. EC2 Instance Connect attempts to establish a connection using an available IP
address in a predefined order, based on the specified connection type. If an IP
address isn't available, it automatically tries the next one in the order.

###### Connection types

`auto` (default)

EC2 Instance Connect tries to connect using the instance's IP addresses in the following order
and with the corresponding connection type:

1. Public IPv4: `direct`
2. Private IPv4: `eice`
3. IPv6: `direct`

`direct`

EC2 Instance Connect tries to connect using the instance's IP addresses in the following
order:

1. Public IPv4
2. IPv6
3. Private IPv4 (it does not connect over an EC2 Instance Connect Endpoint)

`eice`

EC2 Instance Connect tries to connect using the instance's private IPv4 address and an [EC2 Instance Connect Endpoint](connect-with-ec2-instance-connect-endpoint.md "connect-with-ec2-instance-connect-endpoint.md").

###### Note

In the future, we might change the behavior of the `auto` connection type.
To ensure that your desired connection type is used, we recommend that you explicitly set
the `--connection-type` to either `direct` or
`eice`.

###### Requirements

You must use AWS CLI version 2. For more information, see [Install or update to the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

###### To connect to an instance using the instance ID

If you only know the instance ID, and want to let EC2 Instance Connect determine the connection
type to use when connecting to your instance, use the [ec2-instance-connect ssh](../../../cli/latest/reference/ec2-instance-connect/ssh.md "../../../cli/latest/reference/ec2-instance-connect/ssh.md") CLI command
with the instance ID.

```
aws ec2-instance-connect ssh --instance-id `i-1234567890example`
```

###### To connect to an instance using the instance ID and an EC2 Instance Connect Endpoint

If you want to connect to your instance over an [EC2 Instance Connect Endpoint](connect-with-ec2-instance-connect-endpoint.md "connect-with-ec2-instance-connect-endpoint.md"), use the preceding command
and also specify the `--connection-type` parameter with the `eice`
value.

```
aws ec2-instance-connect ssh --instance-id `i-1234567890example` --connection-type eice
```

###### To connect to an instance using the instance ID and your own private key file

If you want to connect to your instance over an EC2 Instance Connect Endpoint using your own private key,
specify the instance ID and the path to the private key file. Do not include
`file://` in the path; the following example will fail:
`file:///path/to/key`.

```
aws ec2-instance-connect ssh --instance-id `i-1234567890example` --private-key-file `/path/to/key`.pem
```

###### Tip

If you get an error when using these commands, make sure that you're using AWS CLI version
2, because the `ssh` command is only available in this major version.
We also recommend regularly updating to the latest minor version of AWS CLI
version 2 to access the latest features. For more information, see [About
AWS CLI version 2](../../../cli/latest/userguide/cli-chap-welcome.md#welcome-versions-v2 "../../../cli/latest/userguide/cli-chap-welcome.md#welcome-versions-v2") in the _AWS Command Line Interface User Guide_.

## Connect using your own key

and SSH client

You can use your own SSH key and connect to your instance from the SSH client of
your choice while using the EC2 Instance Connect API. This enables you to benefit from the
EC2 Instance Connect capability to push a public key to the instance. This connection
method works for instances with public and private IP addresses.

###### Requirements

- Requirements for key pairs
  - Supported types: RSA (OpenSSH and SSH2) and ED25519
  - Supported lengths: 2048 and 4096
  - For more information, see [Create a key pair using
    a third-party tool and import the public key to Amazon EC2](create-key-pairs.md#how-to-generate-your-own-key-and-import-it-to-aws "create-key-pairs.md#how-to-generate-your-own-key-and-import-it-to-aws").

- When connecting to an instance that has only private IP addresses, the
  local computer from which you are initiating the SSH session must have
  connectivity to the EC2 Instance Connect service endpoint (to push your SSH public
  key to the instance) as well as network connectivity to the instance's
  private IP address to establish the SSH session. The EC2 Instance Connect service
  endpoint is reachable over the internet or over an AWS Direct Connect public virtual
  interface. To connect to the instance's private IP address, you can leverage
  services such as [AWS Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/"), [AWS Site-to-Site VPN](https://aws.amazon.com/vpn/ "https://aws.amazon.com/vpn/"),
  or [VPC
  peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md").

###### To connect to your instance using your own key and any SSH client

1. ###### (Optional) Generate new SSH private and public keys

You can generate new SSH private and public keys, `my_key` and
`my_key.pub`, using the following command:

```
ssh-keygen -t rsa -f my_key
```

2. ###### Push your SSH public key to the instance

Use the [send-ssh-public-key](../../../cli/latest/reference/ec2-instance-connect/send-ssh-public-key.md "../../../cli/latest/reference/ec2-instance-connect/send-ssh-public-key.md") command to push your SSH
public key to the instance. If you launched your instance using AL2023 or
Amazon Linux 2, the default username for the AMI is `ec2-user`. If you
launched your instance using Ubuntu, the default username for the AMI is
`ubuntu`.

The following example pushes the public key to the specified instance in
the specified Availability Zone, to authenticate
`ec2-user`.

```
aws ec2-instance-connect send-ssh-public-key \
    --region `us-west-2` \
    --availability-zone `us-west-2b` \
    --instance-id `i-001234a4bf70dec41EXAMPLE` \
    --instance-os-user `ec2-user` \
    --ssh-public-key file://`my_key.pub`
```

3. ###### Connect to the instance using your private key

Use the **ssh** command to connect to the instance using
the private key before the public key is removed from the instance metadata
(you have 60 seconds before it is removed). Specify the private key that
corresponds to the public key, the default username for the AMI that you
used to launch your instance, and the instance's public DNS name (if
connecting over a private network, specify the private DNS name or IP
address). Add the `IdentitiesOnly=yes` option to ensure that only
the files in the ssh config and the specified key are used for the
connection.

```
ssh -o "IdentitiesOnly=yes" -i `my_key` `ec2-user`@`ec2-198-51-100-1.compute-1.amazonaws.com`
```

The following example uses `timeout 3600` to set your SSH
session to terminate after 1 hour. Processes started during the session may
continue running on your instance after the session terminates.

```
timeout 3600 ssh -o “IdentitiesOnly=yes” -i `my_key` `ec2-user`@`ec2-198-51-100-1.compute-1.amazonaws.com`
```

## Troubleshoot

If you receive an error while attempting to connect to your instance, see the
following:

- [Troubleshoot issues connecting to your Amazon EC2 Linux instance](TroubleshootingInstancesConnecting.md "TroubleshootingInstancesConnecting.md")
- [How do I troubleshoot issues connecting to my EC2 instance using EC2
  Instance Connect?](https://repost.aws/knowledge-center/ec2-instance-connect-troubleshooting "https://repost.aws/knowledge-center/ec2-instance-connect-troubleshooting")

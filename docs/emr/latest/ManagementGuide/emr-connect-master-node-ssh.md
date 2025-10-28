# Connect to the Amazon EMR cluster primary node using

SSH

Secure Shell (SSH) is a network protocol you can use to create a secure connection to
a remote computer. After you make a connection, the terminal on your local computer
behaves as if it is running on the remote computer. Commands you issue locally run on
the remote computer, and the command output from the remote computer appears in your
terminal window.

When you use SSH with AWS, you are connecting to an EC2 instance, which is a virtual
server running in the cloud. When working with Amazon EMR, the most common use of SSH is to
connect to the EC2 instance that is acting as the primary node of the cluster.

Using SSH to connect to the primary node gives you the ability to monitor and interact
with the cluster. You can issue Linux commands on the primary node, run applications
such as Hive and Pig interactively, browse directories, read log files, and so on. You
can also create a tunnel in your SSH connection to view the web interfaces hosted on the
primary node. For more information, see [View web interfaces hosted on Amazon EMR
clusters](emr-web-interfaces.md "emr-web-interfaces.md").

To connect to the primary node using SSH, you need the public DNS name of the primary
node. In addition, the security group associated with the primary node must have an
inbound rule that allows SSH (TCP port 22) traffic from a source that includes the
client where the SSH connection originates. You may need to add a rule to allow an SSH
connection from your client. For more information about modifying security group rules,
see [Control network traffic with security groups for your Amazon EMR cluster](emr-security-groups.md "emr-security-groups.md") and [Adding rules to a security
group](../../../AWSEC2/latest/UserGuide/using-network-security.md "../../../AWSEC2/latest/UserGuide/using-network-security.md") in the _Amazon EC2 User Guide_.

## Retrieve the public DNS name of the primary

node

You can retrieve the primary public DNS name using the Amazon EMR console and the
AWS CLI.

Console

###### To retrieve the public DNS name of the primary node with the new

console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation
   pane, choose **Clusters**, and then select the
   cluster where you want to retrieve the public DNS name.
3. Note the **Primary node public DNS** value in
   the **Summary** section of the cluster details
   page.

CLI

###### To retrieve the public DNS

name of the primary node with the AWS CLI

1. To retrieve the cluster identifier, type the following
   command.

```
aws emr list-clusters
```

The output lists your clusters including the cluster IDs. Note
the cluster ID for the cluster to which you are
connecting.

```
"Status": {
    "Timeline": {
        "ReadyDateTime": 1408040782.374,
        "CreationDateTime": 1408040501.213
    },
    "State": "WAITING",
    "StateChangeReason": {
        "Message": "Waiting after step completed"
    }
},
"NormalizedInstanceHours": 4,
**"Id": "j-2AL4XXXXXX5T9"**,
"Name": "My cluster"
```

2. To list the cluster instances including the public DNS name
   for the cluster, type one of the following commands. Replace
   `j-2AL4XXXXXX5T9` with the cluster
   ID returned by the previous command.

```
aws emr list-instances --cluster-id `j-2AL4XXXXXX5T9`
```

Or:

```
aws emr describe-cluster --cluster-id `j-2AL4XXXXXX5T9`
```

The output lists the cluster instances including DNS names and
IP addresses. Note the value for `PublicDnsName`.

```
"Status": {
    "Timeline": {
        "ReadyDateTime": 1408040779.263,
        "CreationDateTime": 1408040515.535
    },
    "State": "RUNNING",
    "StateChangeReason": {}
},
"Ec2InstanceId": "i-e89b45e7",
**"PublicDnsName": "ec2-###-##-##-###.us-west-2.compute.amazonaws.com"**

"PrivateDnsName": "ip-###-##-##-###.us-west-2.compute.internal",
"PublicIpAddress": "##.###.###.##",
"Id": "ci-12XXXXXXXXFMH",
"PrivateIpAddress": "###.##.#.###"
```

For more information, see [Amazon EMR commands
in the AWS CLI](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").

## Connect to the primary node using SSH and an

Amazon EC2 private key on Linux, Unix, and Mac OS X

To create an SSH connection authenticated with a private key file, you need to
specify the Amazon EC2 key pair private key when you launch a cluster. For more
information about accessing your key pair, see [Amazon EC2 key pairs](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") in the
_Amazon EC2 User Guide_.

Your Linux computer most likely includes an SSH client by default. For example, OpenSSH is
installed on most Linux, Unix, and macOS operating systems. You can check for an
SSH client by typing **ssh** at the command line. If your computer
does not recognize the command, install an SSH client to connect to the
primary node. The OpenSSH project provides a free implementation of the full suite of
SSH tools. For more information, see the [OpenSSH](http://www.openssh.org/ "http://www.openssh.org/") website.

The following instructions demonstrate opening an SSH connection to the Amazon EMR
primary node on Linux, Unix, and Mac OS X.

###### To configure the key pair

private key file permissions

Before you can use your Amazon EC2 key pair private key to create an SSH
connection, you must set permissions on the `.pem` file so
that only the key owner has permission to access the file. This is required for
creating an SSH connection using terminal or the AWS CLI.

1. Ensure you've allowed inbound SSH traffic. For instructions, see [Before you connect to Amazon EMR: Authorize inbound
   traffic](emr-connect-ssh-prereqs.md "emr-connect-ssh-prereqs.md").
2. Locate your `.pem` file. These instructions assume that
   the file is named `mykeypair.pem` and that it is stored
   in the current user's home directory.
3. Type the following command to set the permissions. Replace
   `~/mykeypair.pem` with the full path and file
   name of your key pair private key file. For example
   `C:/Users/<username>/.ssh/mykeypair.pem`.

```
chmod 400 `~/mykeypair.pem`
```

If you do not set permissions on the `.pem` file, you
will receive an error indicating that your key file is unprotected and the
key will be rejected. To connect, you only need to set permissions on the
key pair private key file the first time you use it.

###### To connect to the primary node using the terminal

1. Open a terminal window. On Mac OS X, choose **Applications >
   Utilities > Terminal**. On other Linux distributions,
   terminal is typically found at **Applications > Accessories >
   Terminal**.
2. To establish a connection to the primary node, type the following command.
   Replace `ec2-###-##-##-###.compute-1.amazonaws.com`
   with the primary public DNS name of your cluster and replace
   `~/mykeypair.pem` with the full path and file
   name of your `.pem` file. For example
   `C:/Users/<username>/.ssh/mykeypair.pem`.

```
ssh hadoop@`ec2-###-##-##-###.compute-1.amazonaws.com` -i `~/mykeypair.pem`
```

###### Important

You must use the login name `hadoop` when you connect to
the Amazon EMR primary node; otherwise, you may see an error similar to
`Server refused our key`. 3. A warning states that the authenticity of the host you are connecting to
cannot be verified. Type `yes` to continue. 4. When you are done working on the primary node, type the following command
to close the SSH connection.

```
exit
```

If you're experiencing difficulty with using SSH to connect to your primary node,
see [Troubleshoot connecting to your instance](../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md "../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md").

## Connect to the primary node using SSH on

Windows

Windows users can use an SSH client such as PuTTY to connect to the primary
node. Before connecting to the Amazon EMR primary node, you should download and install
PuTTY and PuTTYgen. You can download these tools from the [PuTTY download
page](http://www.chiark.greenend.org.uk/~sgtatham/putty/ "http://www.chiark.greenend.org.uk/~sgtatham/putty/").

PuTTY does not natively support the key pair private key file format
(`.pem`) generated by Amazon EC2. You use PuTTYgen to convert
your key file to the required PuTTY format (`.ppk`). You must
convert your key into this format (`.ppk`) before attempting to
connect to the primary node using PuTTY.

For more information about converting your key, see [Converting your private key using
PuTTYgen](../../../AWSEC2/latest/UserGuide/putty.md "../../../AWSEC2/latest/UserGuide/putty.md") in the _Amazon EC2 User Guide_.

###### To connect to the primary node using

PuTTY

1. Ensure you've allowed inbound SSH traffic. For instructions, see [Before you connect to Amazon EMR: Authorize inbound
   traffic](emr-connect-ssh-prereqs.md "emr-connect-ssh-prereqs.md").
2. Open `putty.exe`. You can also launch PuTTY from the
   Windows programs list.
3. If necessary, in the **Category** list, choose
   **Session**.
4. For **Host Name (or IP address)**, type
   `hadoop@``MasterPublicDNS`. For
   example:
   `hadoop@``ec2-###-##-##-###.compute-1.amazonaws.com`.
5. In the **Category** list, choose \*\*Connection
   > SSH**, **Auth\*\*.
6. For **Private key file for authentication**, choose
   **Browse** and select the `.ppk`
   file that you generated.
7. Choose **Open** and then **Yes** to
   dismiss the PuTTY security alert.

###### Important

When logging into the primary node, type `hadoop` if you
are prompted for a user name . 8. When you are done working on the primary node, you can close the SSH
connection by closing PuTTY.

###### Note

To prevent the SSH connection from timing out, you can choose
**Connection** in the **Category**
list and select the option **Enable TCP_keepalives**.
If you have an active SSH session in PuTTY, you can change your
settings by opening the context (right-click) for the PuTTY title bar
and choosing **Change Settings**.

If you're experiencing difficulty with using SSH to connect to your primary node,
see [Troubleshoot connecting to your instance](../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md "../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md").

## Connect to the primary node using the

AWS CLI

You can create an SSH connection with the primary node using the AWS CLI on Windows
and on Linux, Unix, and Mac OS X. Regardless of the platform, you need the public
DNS name of the primary node and your Amazon EC2 key pair private key. If you are using
the AWS CLI on Linux, Unix, or Mac OS X, you must also set permissions on the private
key (`.pem` or `.ppk`) file as shown in [To configure the key pair
private key file permissions](#emr-keypair-file-permission-config "#emr-keypair-file-permission-config").

###### To connect to the primary node using the AWS CLI

1. Ensure you've allowed inbound SSH traffic. For instructions, see [Before you connect to Amazon EMR: Authorize inbound
   traffic](emr-connect-ssh-prereqs.md "emr-connect-ssh-prereqs.md").
2. To retrieve the cluster identifier, type:

```
aws emr list-clusters
```

The output lists your clusters including the cluster IDs. Note the cluster
ID for the cluster to which you are connecting.

```
"Status": {
    "Timeline": {
        "ReadyDateTime": 1408040782.374,
        "CreationDateTime": 1408040501.213
    },
    "State": "WAITING",
    "StateChangeReason": {
        "Message": "Waiting after step completed"
    }
},
"NormalizedInstanceHours": 4,
**"Id": "j-2AL4XXXXXX5T9"**,
"Name": "AWS CLI cluster"
```

3. Type the following command to open an SSH connection to the primary node.
   In the following example, replace `j-2AL4XXXXXX5T9`
   with the cluster ID and replace `~/mykeypair.key`
   with the full path and file name of your `.pem` file (for
   Linux, Unix, and Mac OS X) or `.ppk` file (for Windows).
   For example
   `C:\Users\<username>\.ssh\mykeypair.pem`.

```
aws emr ssh --cluster-id `j-2AL4XXXXXX5T9` --key-pair-file `~/mykeypair.key`
```

4. When you are done working on the primary node, close the AWS CLI window.

For more information, see [Amazon EMR commands in
the AWS CLI](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md"). If you're experiencing difficulty with using SSH to
connect to your primary node, see [Troubleshoot connecting to your instance](../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md "../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md").

# Option 2, part 1: Set up an SSH tunnel to the

primary node using dynamic port forwarding

To connect to the local web server on the primary node, you create an SSH
tunnel between your computer and the primary node. This is also known as
_port forwarding_. If you create your SSH
tunnel using dynamic port forwarding, all traffic routed to a specified unused
local port is forwarded to the local web server on the primary node. This
creates a SOCKS proxy. You can then configure your Internet browser to use an
add-on such as FoxyProxy or SwitchyOmega to manage your SOCKS proxy settings.

Using a proxy management add-on allows you to automatically filter URLs based
on text patterns and to limit the proxy settings to domains that match the form
of the primary node's public DNS name. The browser add-on automatically handles
turning the proxy on and off when you switch between viewing websites hosted on
the primary node, and those on the Internet.

Before you begin, you need the public DNS name of the primary node and your
key pair private key file. For information about how to locate the primary public
DNS name, see [Retrieve the public DNS name of the primary
node](emr-connect-master-node-ssh.md#emr-connect-master-dns "emr-connect-master-node-ssh.md#emr-connect-master-dns"). For more information about
accessing your key pair, see [Amazon EC2 key pairs](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") in the _Amazon EC2 User Guide_.
For more information about the sites you might want to view on the primary node,
see [View web interfaces hosted on Amazon EMR
clusters](emr-web-interfaces.md "emr-web-interfaces.md").

## Set up an SSH tunnel to the primary

node using dynamic port forwarding with OpenSSH

###### To set up an SSH tunnel using dynamic

port forwarding with OpenSSH

1. Ensure you've allowed inbound SSH traffic. For instructions, see
   [Before you connect to Amazon EMR: Authorize inbound
   traffic](emr-connect-ssh-prereqs.md "emr-connect-ssh-prereqs.md").
2. Open a terminal window. On Mac OS X, choose \*\*Applications
   > Utilities > Terminal**. On other Linux
   > distributions, terminal is typically found at **Applications
   > Accessories > Terminal\*\*.
3. Type the following command to open an SSH tunnel on your local
   machine. Replace `~/mykeypair.pem` with the
   location and file name of your `.pem` file,
   replace `8157` with an unused, local port
   number, and replace
   `ec2-###-##-##-###.compute-1.amazonaws.com`
   with the primary public DNS name of your cluster.

```
ssh -i `~/mykeypair.pem` -N -D `8157` hadoop@`ec2-###-##-##-###.compute-1.amazonaws.com`
```

After you issue this command, the terminal remains open and does
not return a response.

###### Note

`-D` signifies the use of dynamic port forwarding
which allows you to specify a local port used to forward data to
all remote ports on the primary node's local web server. Dynamic
port forwarding creates a local SOCKS proxy listening on the
port specified in the command. 4. After the tunnel is active, configure a SOCKS proxy for your
browser. For more information, see [Option 2, part 2: Configure
proxy settings to view websites hosted on the Amazon EMR cluster primary node](emr-connect-master-node-proxy.md "emr-connect-master-node-proxy.md"). 5. When you are done working with the web interfaces on the primary
node, close the terminal window.

## Set up an SSH tunnel using dynamic port

forwarding with the AWS CLI

You can create an SSH connection with the primary node using the AWS CLI on
Windows and on Linux, Unix, and Mac OS X. If you are using the AWS CLI on
Linux, Unix, or Mac OS X, you must set permissions on the
`.pem` file as shown in [To configure the key pair
private key file permissions](emr-connect-master-node-ssh.md#emr-keypair-file-permission-config "emr-connect-master-node-ssh.md#emr-keypair-file-permission-config"). If you are using
the AWS CLI on Windows, PuTTY must appear in the path environment variable
or you may receive an error such as **`OpenSSH or PuTTY not
 available`**.

###### To set up an SSH tunnel using dynamic port

forwarding with the AWS CLI

1. Ensure you've allowed inbound SSH traffic. For instructions, see
   [Before you connect to Amazon EMR: Authorize inbound
   traffic](emr-connect-ssh-prereqs.md "emr-connect-ssh-prereqs.md").
2. Create an SSH connection with the primary node as shown in [Connect to the primary node using the
   AWS CLI](emr-connect-master-node-ssh.md#emr-connect-cli "emr-connect-master-node-ssh.md#emr-connect-cli").
3. To retrieve the cluster identifier, type:

```
aws emr list-clusters
```

The output lists your clusters including the cluster IDs. Note the
cluster ID for the cluster to which you are connecting.

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

4. Type the following command to open an SSH tunnel to the primary
   node using dynamic port forwarding. In the following example,
   replace `j-2AL4XXXXXX5T9` with the cluster
   ID and replace `~/mykeypair.key` with the
   location and file name of your `.pem` file (for
   Linux, Unix, and Mac OS X) or `.ppk` file (for
   Windows).

```
aws emr socks --cluster-id `j-2AL4XXXXXX5T9` --key-pair-file `~/mykeypair.key`
```

###### Note

The socks command automatically configures dynamic port
forwarding on local port 8157. Currently, this setting cannot be
modified. 5. After the tunnel is active, configure a SOCKS proxy for your
browser. For more information, see [Option 2, part 2: Configure
proxy settings to view websites hosted on the Amazon EMR cluster primary node](emr-connect-master-node-proxy.md "emr-connect-master-node-proxy.md"). 6. When you are done working with the web interfaces on the primary
node, close the AWS CLI window.

For more information on using Amazon EMR commands in the AWS CLI, see
[https://docs.aws.amazon.com/cli/latest/reference/emr](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").

## Set up an SSH tunnel to the primary

node using PuTTY

Windows users can use an SSH client such as PuTTY to create an SSH
tunnel to the primary node. Before connecting to the Amazon EMR primary node, you
should download and install PuTTY and PuTTYgen. You can download these
tools from the [PuTTY
download page](http://www.chiark.greenend.org.uk/~sgtatham/putty/ "http://www.chiark.greenend.org.uk/~sgtatham/putty/").

PuTTY does not natively support the key pair private key file format
(`.pem`) generated by Amazon EC2. You use PuTTYgen to
convert your key file to the required PuTTY format
(`.ppk`). You must convert your key into this format
(`.ppk`) before attempting to connect to the primary
node using PuTTY.

For more information about converting your key, see [Converting your private key using
PuTTYgen](../../../AWSEC2/latest/UserGuide/putty.md "../../../AWSEC2/latest/UserGuide/putty.md") in the _Amazon EC2 User Guide_.

###### To set up an SSH tunnel using dynamic

port forwarding using PuTTY

1. Ensure you've allowed inbound SSH traffic. For instructions, see
   [Before you connect to Amazon EMR: Authorize inbound
   traffic](emr-connect-ssh-prereqs.md "emr-connect-ssh-prereqs.md").
2. Double-click `putty.exe` to start PuTTY. You
   can also launch PuTTY from the Windows programs list.

###### Note

If you already have an active SSH session with the primary
node, you can add a tunnel by right-clicking the PuTTY title
bar and choosing **Change Settings**. 3. If necessary, in the **Category** list, choose
**Session**. 4. In the **Host Name** field, type
`hadoop@``MasterPublicDNS`.
For example:
`hadoop@``ec2-###-##-##-###.compute-1.amazonaws.com`. 5. In the **Category** list, expand
**Connection > SSH**, and then choose
**Auth**. 6. For **Private key file for authentication**,
choose **Browse** and select the
`.ppk` file that you generated.

###### Note

PuTTY does not natively support the key pair private key
file format (`.pem`) generated by Amazon EC2. You
use PuTTYgen to convert your key file to the required PuTTY
format (`.ppk`). You must convert your key
into this format (`.ppk`) before attempting
to connect to the primary node using PuTTY. 7. In the **Category** list, expand
**Connection > SSH**, and then choose
**Tunnels**. 8. In the **Source port** field, type
`8157` (an unused local port), and then choose
**Add**. 9. Leave the **Destination** field blank. 10. Select the **Dynamic** and
**Auto** options. 11. Choose **Open**. 12. Choose **Yes** to dismiss the PuTTY security
alert.

###### Important

When you log in to the primary node, type `hadoop`
if you are prompted for a user name. 13. After the tunnel is active, configure a SOCKS proxy for your
browser. For more information, see [Option 2, part 2: Configure
proxy settings to view websites hosted on the Amazon EMR cluster primary node](emr-connect-master-node-proxy.md "emr-connect-master-node-proxy.md"). 14. When you are done working with the web interfaces on the primary
node, close the PuTTY window.

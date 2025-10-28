# General connection prerequisites

The following are general prerequisites to connect to an instance. Note that there might be additional prerequisites that are
specific to the connection option that you choose.

###### General prerequisites

- Check that your instance has passed its status checks.
  It can take a few minutes for an instance to be ready to accept connection requests.
  For more information, see [View status checks](viewing_status.md "viewing_status.md").
- [Get the required instance details](#connection-prereqs-get-info-about-instance "#connection-prereqs-get-info-about-instance").
- [Locate the private key and set permissions](#connection-prereqs-private-key "#connection-prereqs-private-key").
- [(Optional) Get the instance fingerprint](#connection-prereqs-fingerprint "#connection-prereqs-fingerprint").

## Get the required instance details

To prepare to connect to your instance, get the following information from the Amazon EC2 console
or by using the command line.

![The Instances pane of the Amazon EC2 console.](images/connection-prereqs-console2.png)

- Get the public DNS name of the instance.

You can get the public DNS for your instance from the Amazon EC2 console. Check the
**Public IPv4 DNS** column of the
**Instances** pane. If this column is hidden, choose the
settings icon (
![The gear icon.](images/settings-icon.png)
) in the top-right corner of the screen, and select
**Public IPv4 DNS**. You can also find the public DNS in the
instance information section of the **Instances** pane. When you
select the instance in the **Instances** pane of the Amazon EC2 console,
information about that instance will appear on the lower half of the page. Under the
**Details** tab, look for **Public IPv4
DNS**.

If you prefer, you can use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md")
(AWS CLI) or [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md") (AWS Tools for Windows PowerShell) commands.

If no **Public IPv4 DNS** is displayed, verify that the
**Instance state** is **Running**, and that
you have not launched the instance in a private subnet. If you launched your
instance using the [launch instance
wizard](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md"), you may have edited the **Auto-assign public
IP** field under **Network settings** and changed the
value to **Disable**. If you disable the **Auto-assign
public IP** option, the instance is not assigned a public IP address
when it is launched.

- (IPv6 only instances) Get the IPv6 address of the instance.

If you assigned an IPv6 address to your instance, you can optionally connect to
the instance using its IPv6 address instead of a public IPv4 address or public IPv4
DNS hostname. Your local computer must have an IPv6 address and must be configured
to use IPv6. You can get the IPv6 address of your instance from the Amazon EC2 console.
Check the **IPv6 IPs** column of the **Instances**
pane. Or, you can find the IPv6 address in the instance information section. When
you select the instance in the **Instances** pane of the Amazon EC2
console, information about that instance will appear on the lower half of the page.
Under the **Details** tab, look for **IPv6
address**.

If you prefer, you can use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md")
(AWS CLI) or [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md") (AWS Tools for Windows PowerShell) commands. For more information about IPv6,
see [IPv6 addresses](using-instance-addressing.md#ipv6-addressing "using-instance-addressing.md#ipv6-addressing").

- (Linux instances) Get the username for your instance.

You can connect to your instance using the username for your user account or the default
username for the AMI that you used to launch your instance.

    + Get the username for your user account.


    For more information about how to create a user account, see [Manage system users on your Amazon EC2 Linux instance](managing-users.md "managing-users.md").
    + Get the default username for the AMI that you used to launch your instance.




    	- Amazon Linux –
    	 `ec2-user`
    	- CentOS –
    	 `centos` or `ec2-user`
    	- Debian –
    	 `admin`
    	- Fedora –
    	 `fedora` or `ec2-user`
    	- FreeBSD –
    	 `ec2-user`
    	- RHEL –
    	 `ec2-user` or `root`
    	- SUSE –
    	 `ec2-user` or `root`
    	- Ubuntu –
    	 `ubuntu`
    	- Oracle –
    	 `ec2-user`
    	- Bitnami –
    	 `bitnami`
    	- Rocky Linux –
    	 `rocky`
    	- Other –
    	 Check with the AMI provider

## Locate the private key and set permissions

You must know the location of your private key file to make the initial connection
to a Linux instance using SSH or a Windows instances using RDP. For SSH
connections, you must set file permissions so that only you can read the private key.

For information about how key pairs work when using Amazon EC2, see [Amazon EC2 key pairs and Amazon EC2 instances](ec2-key-pairs.md "ec2-key-pairs.md").

- Locate the private key.

Get the fully-qualified path to the location on your computer of the
`.pem` file for the key pair that you specified when you launched the
instance. For more information, see [Identify the public key specified at
launch](describe-keys.md#identify-key-pair-specified-at-launch "describe-keys.md#identify-key-pair-specified-at-launch").

If you can't find your private key file, see [I've lost my private key. How can I connect to my instance?](TroubleshootingInstancesConnecting.md#replacing-lost-key-pair "TroubleshootingInstancesConnecting.md#replacing-lost-key-pair")

(Linux instances) If you are connecting to your instance using PuTTY and need to
convert the `.pem` file to `.ppk`, see [Convert your private key using PuTTYgen](connect-linux-inst-from-windows.md#putty-private-key "connect-linux-inst-from-windows.md#putty-private-key").

- (Linux instances) Set the permissions of your private key so that only
  you can read it.
  - Connect from macOS or Linux

  If you plan to use an SSH client on a macOS or Linux computer to connect to your Linux
  instance, use the following command to set the permissions of your private key file so that
  only you can read it.

  ```
  `chmod 400 `key-pair-name`.pem`
  ```

  If you do not set these permissions, then you cannot connect to your instance using this
  key pair. For more information, see [Error: Unprotected private key file](TroubleshootingInstancesConnecting.md#troubleshoot-unprotected-key "TroubleshootingInstancesConnecting.md#troubleshoot-unprotected-key").
  - Connect from Windows

  Open File Explorer and right-click on the `.pem` file. Select
  **Properties** > **Security
  tab** and choose **Advanced**. Choose
  **Disable inheritance**. Remove access to all
  users except for the current user.

## (Optional) Get the instance fingerprint

To protect yourself from man-in-the-middle attacks, you can verify the authenticity of the
instance you're about to connect to by verifying the fingerprint that is displayed.
Verifying the fingerprint is useful if you launched your instance from a public AMI
provided by a third party.

###### Task overview

First, get the instance fingerprint from the instance. Then, when you connect to the
instance and are prompted to verify the fingerprint, compare the fingerprint you
obtained in this procedure with the fingerprint that is displayed. If the
fingerprints don't match, someone might be attempting a man-in-the-middle attack. If
they match, you can confidently connect to your instance.

###### Prerequisites to get the instance fingerprint

- The instance must not be in the `pending` state. The fingerprint is available
  only after the first boot of the instance is complete.
- You must be the instance owner to get the console output.
- There are various ways to get the instance fingerprint. If you want to use the
  AWS CLI, it must be installed on your local computer. For information about
  installing the AWS CLI, see [Getting started with the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the
  _AWS Command Line Interface User Guide_.

###### To get the instance fingerprint

In Step 1, you get the console output, which includes the instance fingerprint. In Step 2,
you find the instance fingerprint in the console output.

1. Get the console output using one of the following methods.

Console

    1. Open the Amazon EC2 console at
     [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
    2. From the left navigator, choose **Instances**.
    3. Select your instance, and then choose
     **Actions**, **Monitor and
     troubleshoot**, **Get system
     log**.

AWS CLI
On your local computer (not on the instance you're connecting to),
use the [get-console-output](../../../cli/latest/reference/ec2/get-console-output.md "../../../cli/latest/reference/ec2/get-console-output.md") command. If the output is large,
[you can pipe it to a text file](../../../cli/latest/userguide/cli-usage-output-format.md "../../../cli/latest/userguide/cli-usage-output-format.md"), where it might be easier
to read.

```
aws ec2 get-console-output \
    --instance-id `i-1234567890abcdef0` \
    --query Output \
    --output text > `temp.txt`
```

PowerShell
On your local computer, use the following
[Get-EC2ConsoleOutput](../../../powershell/latest/reference/items/Get-EC2ConsoleOutput.md "../../../powershell/latest/reference/items/Get-EC2ConsoleOutput.md")
cmdlet.

```
$encodedOutput = (Get-EC2ConsoleOutput -InstanceId `i-1234567890abcdef0`).Output
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($encodedOutput))
```

2. In the console output, find the instance (host) fingerprint, which is located under
   `BEGIN SSH HOST KEY FINGERPRINTS`. There might be several
   instance fingerprints. When you connect to your instance, it will display only
   one of the fingerprints.

The exact output can vary by operating system, AMI version, and whether AWS
created the key pairs. The following is example output.

```
ec2:#############################################################
ec2: -----BEGIN SSH HOST KEY FINGERPRINTS-----
ec2: 256 SHA256:l4UB/neBad9tvkgJf1QZWxheQmR59WgrgzEimCG6kZY no comment (ECDSA)
ec2: 256 SHA256:kpEa+rw/Uq3zxaYZN8KT501iBtJOIdHG52dFi66EEfQ no comment (ED25519)
ec2: 2048 SHA256:L8l6pepcA7iqW/jBecQjVZClUrKY+o2cHLI0iHerbVc no comment (RSA)
ec2: -----END SSH HOST KEY FINGERPRINTS-----
ec2: #############################################################
```

###### Note

You'll reference this fingerprint when you connect to the instance.

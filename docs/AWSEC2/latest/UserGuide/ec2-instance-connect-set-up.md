# Install EC2 Instance Connect on your EC2

instances

To connect to a Linux instance using EC2 Instance Connect, the instance must have
EC2 Instance Connect installed. Installing EC2 Instance Connect configures the SSH daemon on the
instance.

For more information about the EC2 Instance Connect package, see [aws/aws-ec2-instance-connect-config](https://github.com/aws/aws-ec2-instance-connect-config "https://github.com/aws/aws-ec2-instance-connect-config") on the GitHub website.

###### Note

If you configured the `AuthorizedKeysCommand` and
`AuthorizedKeysCommandUser` settings for SSH authentication, the
EC2 Instance Connect installation will not update them. As a result, you can't use
EC2 Instance Connect.

## Install

prerequisites

Before you install EC2 Instance Connect, ensure that you meet the following
prerequisites.

- **Verify that the instance uses one of the
  following:**
  - Amazon Linux 2 prior to version 2.0.20190618 \*
  - AL2023 minimal AMI or Amazon ECS-optimized AMI
  - CentOS Stream 8 and 9
  - macOS Sonoma prior to 14.2.1, Ventura prior to 13.6.3, and Monterey prior to 12.7.2 \*
  - Red Hat Enterprise Linux (RHEL) 8 and 9
  - Ubuntu 16.04 and 18.04 \*

###### Tip

\* For Amazon Linux 2, macOS, and Ubuntu: If you launched your instance using a later version than
those listed above, EC2 Instance Connect comes preinstalled and no manual
installation is required.

- **Verify the general prerequisites for
  EC2 Instance Connect.**

For more information, see [Prerequisites for
EC2 Instance Connect](ec2-instance-connect-prerequisites.md "ec2-instance-connect-prerequisites.md").

- **Verify the prerequisites for connecting to your
  instance using an SSH client on your local machine.**

For more information, see [Connect to your Linux instance using SSH](connect-to-linux-instance.md "connect-to-linux-instance.md").

- Get the ID of the instance.

You can get the ID of your instance using the Amazon EC2 console (from the
**Instance ID** column). If you prefer, you can use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") (AWS CLI) or
[Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md")
(AWS Tools for Windows PowerShell) command.

## Manually install

EC2 Instance Connect

###### Note

If you launched your instance using one of the following AMIs, EC2 Instance Connect
is pre-installed and you can skip this procedure:

- AL2023 standard AMI
- Amazon Linux 2 2.0.20190618 or later
- macOS Sonoma 14.2.1 or later
- macOS Ventura 13.6.3 or later
- macOS Monterey 12.7.2 or later
- Ubuntu 20.04 or later

Use one of the following procedures for installing EC2 Instance Connect, depending on the
operating system of your instance.

Amazon Linux 2

###### To install EC2 Instance Connect on an instance launched with

Amazon Linux 2

1. Connect to your instance using SSH.

Replace the example values in the following command with your
values. Use the SSH key pair that was assigned to your instance
when you launched it and the default username of the AMI that
you used to launch your instance. For Amazon Linux 2, the default
username is `ec2-user`.

```
`$` ssh -i `my_ec2_private_key`.pem `ec2-user`@`ec2-a-b-c-d.us-west-2.compute.amazonaws.com`
```

For more information about connecting to your instance, see
[Connect to your Linux instance using an SSH client](connect-linux-inst-ssh.md "connect-linux-inst-ssh.md"). 2. Install the EC2 Instance Connect package on your instance.

```
`[ec2-user ~]$` sudo yum install ec2-instance-connect
```

You should see three new scripts in the
`/opt/aws/bin/` folder:

```
eic_curl_authorized_keys
eic_parse_authorized_keys
eic_run_authorized_keys
```

3. (Optional) Verify that EC2 Instance Connect was successfully
   installed on your instance.

```
`[ec2-user ~]$` sudo less /etc/ssh/sshd_config
```

EC2 Instance Connect was successfully installed if the
`AuthorizedKeysCommand` and
`AuthorizedKeysCommandUser` lines contain the
following values:

```
AuthorizedKeysCommand /opt/aws/bin/eic_run_authorized_keys %u %f
AuthorizedKeysCommandUser ec2-instance-connect
```

    * `AuthorizedKeysCommand` sets the
     `eic_run_authorized_keys` script
     to look up the keys from the instance metadata
    * `AuthorizedKeysCommandUser` sets the system
     user as `ec2-instance-connect`

###### Note

If you previously configured
`AuthorizedKeysCommand` and
`AuthorizedKeysCommandUser`, the
EC2 Instance Connect installation will not change the values and
you will not be able to use EC2 Instance Connect.

CentOS

###### To install EC2 Instance Connect on an instance launched with

CentOS

1. Connect to your instance using SSH.

Replace the example values in the following command with your
values. Use the SSH key pair that was assigned to your instance
when you launched it and the default username of the AMI that
you used to launch your instance. For CentOS, the default
username is `centos` or `ec2-user`.

```
`$` ssh -i `my_ec2_private_key`.pem `centos`@`ec2-a-b-c-d.us-west-2.compute.amazonaws.com`
```

For more information about connecting to your instance, see
[Connect to your Linux instance using an SSH client](connect-linux-inst-ssh.md "connect-linux-inst-ssh.md"). 2. If you use an HTTP or HTTPS proxy, you must set the
`http_proxy` or `https_proxy`
environment variables in the current shell session.

If you're not using a proxy, you can skip this step.

    * For an HTTP proxy server, run the following
     commands:



    ```
    `$` export http_proxy=http://hostname:port
    `$` export https_proxy=http://hostname:port
    ```
    * For an HTTPS proxy server, run the following
     commands:



    ```
    `$` export http_proxy=https://hostname:port
    `$` export https_proxy=https://hostname:port
    ```

3. Install the EC2 Instance Connect package on your instance by running
   the following commands.

The EC2 Instance Connect configuration files for CentOS are provided
in a Red Hat Package Manager (RPM) package, with different RPM
packages for CentOS 8 and CentOS 9 and for instance types that
run on Intel/AMD (x86_64) or ARM (AArch64).

Use the command block for your operating system and CPU
architecture.

    * CentOS 8


    Intel/AMD (x86\_64)



    ```
    `[ec2-user ~]$` mkdir /tmp/ec2-instance-connect
    `[ec2-user ~]$` curl https://amazon-ec2-instance-connect-us-west-2.s3.us-west-2.amazonaws.com/latest/linux_amd64/ec2-instance-connect-2.0.0-5.rhel8.x86_64.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect.rpm
    `[ec2-user ~]$` curl https://amazon-ec2-instance-connect-us-west-2.s3.us-west-2.amazonaws.com/latest/linux_amd64/ec2-instance-connect-selinux-2.0.0-5.noarch.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
    `[ec2-user ~]$` sudo yum install -y /tmp/ec2-instance-connect/ec2-instance-connect.rpm /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
    ```

    ARM (AArch64)



    ```
    `[ec2-user ~]$` mkdir /tmp/ec2-instance-connect
    `[ec2-user ~]$` curl https://amazon-ec2-instance-connect-us-west-2.s3.us-west-2.amazonaws.com/latest/linux_arm64/ec2-instance-connect-2.0.0-5.rhel8.aarch64.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect.rpm
    `[ec2-user ~]$` curl https://amazon-ec2-instance-connect-us-west-2.s3.us-west-2.amazonaws.com/latest/linux_arm64/ec2-instance-connect-selinux-2.0.0-5.noarch.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
    `[ec2-user ~]$` sudo yum install -y /tmp/ec2-instance-connect/ec2-instance-connect.rpm /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
    ```
    * CentOS 9


    Intel/AMD (x86\_64)



    ```
    `[ec2-user ~]$` mkdir /tmp/ec2-instance-connect
    `[ec2-user ~]$` curl https://amazon-ec2-instance-connect-us-west-2.s3.us-west-2.amazonaws.com/latest/linux_amd64/ec2-instance-connect-2.0.0-5.rhel9.x86_64.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect.rpm
    `[ec2-user ~]$` curl https://amazon-ec2-instance-connect-us-west-2.s3.us-west-2.amazonaws.com/latest/linux_amd64/ec2-instance-connect-selinux-2.0.0-5.noarch.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
    `[ec2-user ~]$` sudo yum install -y /tmp/ec2-instance-connect/ec2-instance-connect.rpm /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
    ```

    ARM (AArch64)



    ```
    `[ec2-user ~]$` mkdir /tmp/ec2-instance-connect
    `[ec2-user ~]$` curl https://amazon-ec2-instance-connect-us-west-2.s3.us-west-2.amazonaws.com/latest/linux_arm64/ec2-instance-connect-2.0.0-5.rhel9.aarch64.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect.rpm
    `[ec2-user ~]$` curl https://amazon-ec2-instance-connect-us-west-2.s3.us-west-2.amazonaws.com/latest/linux_arm64/ec2-instance-connect-selinux-2.0.0-5.noarch.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
    `[ec2-user ~]$` sudo yum install -y /tmp/ec2-instance-connect/ec2-instance-connect.rpm /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
    ```

You should see the following new script in the
`/opt/aws/bin/` folder:

```
eic_run_authorized_keys
```

4.  (Optional) Verify that EC2 Instance Connect was successfully
    installed on your instance.

        * For CentOS 8:



        ```
        `[ec2-user ~]$` sudo less /lib/systemd/system/sshd.service.d/ec2-instance-connect.conf
        ```
        * For CentOS 9:



        ```
        `[ec2-user ~]$` sudo less /etc/ssh/sshd_config.d/60-ec2-instance-connect.conf
        ```

    EC2 Instance Connect was successfully installed if the
    `AuthorizedKeysCommand` and
    `AuthorizedKeysCommandUser` lines contain the
    following values:

```
AuthorizedKeysCommand /opt/aws/bin/eic_run_authorized_keys %u %f
AuthorizedKeysCommandUser ec2-instance-connect
```

    * `AuthorizedKeysCommand` sets the
     `eic_run_authorized_keys` script
     to look up the keys from the instance metadata
    * `AuthorizedKeysCommandUser` sets the system
     user as `ec2-instance-connect`

###### Note

If you previously configured
`AuthorizedKeysCommand` and
`AuthorizedKeysCommandUser`, the
EC2 Instance Connect installation will not change the values and
you will not be able to use EC2 Instance Connect.

macOS

###### To install EC2 Instance Connect on an instance launched with

macOS

1. Connect to your instance using SSH.

Replace the example values in the following command with your
values. Use the SSH key pair that was assigned to your instance
when you launched it and the default username of the AMI that
you used to launch your instance. For macOS instances, the
default username is `ec2-user`.

```
`$` ssh -i `my_ec2_private_key`.pem `ec2-user`@`ec2-a-b-c-d.us-west-2.compute.amazonaws.com`
```

For more information about connecting to your instance, see
[Connect to your Linux instance using an SSH client](connect-linux-inst-ssh.md "connect-linux-inst-ssh.md"). 2. Update Homebrew using the following command. The update will
list the software that Homebrew knows about. The EC2 Instance Connect
package is provided via Homebrew on macOS instances. For more information, see [Update the operating system and software on Amazon EC2 Mac instances](mac-instance-updates.md "mac-instance-updates.md").

```
`[ec2-user ~]$` brew update
```

3. Install the EC2 Instance Connect package on your instance. This will
   install the software and configure sshd to use it.

```
`[ec2-user ~]$` brew install ec2-instance-connect
```

You should see the following new script in the
`/opt/aws/bin/` folder:

```
eic_run_authorized_keys
```

4. (Optional) Verify that EC2 Instance Connect was successfully
   installed on your instance.

```
`[ec2-user ~]$` sudo less /etc/ssh/sshd_config.d/60-ec2-instance-connect.conf
```

EC2 Instance Connect was successfully installed if the
`AuthorizedKeysCommand` and
`AuthorizedKeysCommandUser` lines contain the
following values:

```
AuthorizedKeysCommand /opt/aws/bin/eic_run_authorized_keys %u %f
AuthorizedKeysCommandUser ec2-instance-connect
```

    * `AuthorizedKeysCommand` sets the
     `eic_run_authorized_keys` script
     to look up the keys from the instance metadata
    * `AuthorizedKeysCommandUser` sets the system
     user as `ec2-instance-connect`

###### Note

If you previously configured
`AuthorizedKeysCommand` and
`AuthorizedKeysCommandUser`, the
EC2 Instance Connect installation will not change the values and
you will not be able to use EC2 Instance Connect.

RHEL

###### To install EC2 Instance Connect on an instance launched with Red Hat

Enterprise Linux (RHEL)

1. Connect to your instance using SSH.

Replace the example values in the following command with your
values. Use the SSH key pair that was assigned to your instance
when you launched it and the default username of the AMI that
you used to launch your instance. For RHEL, the default username
is `ec2-user` or `root`.

```
`$` ssh -i `my_ec2_private_key`.pem `ec2-user`@`ec2-a-b-c-d.us-west-2.compute.amazonaws.com`
```

For more information about connecting to your instance, see
[Connect to your Linux instance using an SSH client](connect-linux-inst-ssh.md "connect-linux-inst-ssh.md"). 2. If you use an HTTP or HTTPS proxy, you must set the
`http_proxy` or `https_proxy`
environment variables in the current shell session.

If you're not using a proxy, you can skip this step.

    * For an HTTP proxy server, run the following
     commands:



    ```
    `$` export http_proxy=http://hostname:port
    `$` export https_proxy=http://hostname:port
    ```
    * For an HTTPS proxy server, run the following
     commands:



    ```
    `$` export http_proxy=https://hostname:port
    `$` export https_proxy=https://hostname:port
    ```

3. Install the EC2 Instance Connect package on your instance by running
   the following commands.

The EC2 Instance Connect configuration files for RHEL are provided in
a Red Hat Package Manager (RPM) package, with different RPM
packages for RHEL 8 and RHEL 9 and for instance types that run
on Intel/AMD (x86_64) or ARM (AArch64).

Use the command block for your operating system and CPU
architecture.

    * RHEL 8


    Intel/AMD (x86\_64)



    ```
    `[ec2-user ~]$` mkdir /tmp/ec2-instance-connect
    `[ec2-user ~]$` curl https://amazon-ec2-instance-connect-us-west-2.s3.us-west-2.amazonaws.com/latest/linux_amd64/ec2-instance-connect-2.0.0-5.rhel8.x86_64.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect.rpm
    `[ec2-user ~]$` curl https://amazon-ec2-instance-connect-us-west-2.s3.us-west-2.amazonaws.com/latest/linux_amd64/ec2-instance-connect-selinux-2.0.0-5.noarch.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
    `[ec2-user ~]$` sudo yum install -y /tmp/ec2-instance-connect/ec2-instance-connect.rpm /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
    ```

    ARM (AArch64)



    ```
    `[ec2-user ~]$` mkdir /tmp/ec2-instance-connect
    `[ec2-user ~]$` curl https://amazon-ec2-instance-connect-us-west-2.s3.us-west-2.amazonaws.com/latest/linux_arm64/ec2-instance-connect-2.0.0-5.rhel8.aarch64.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect.rpm
    `[ec2-user ~]$` curl https://amazon-ec2-instance-connect-us-west-2.s3.us-west-2.amazonaws.com/latest/linux_arm64/ec2-instance-connect-selinux-2.0.0-5.noarch.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
    `[ec2-user ~]$` sudo yum install -y /tmp/ec2-instance-connect/ec2-instance-connect.rpm /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
    ```
    * RHEL 9


    Intel/AMD (x86\_64)



    ```
    `[ec2-user ~]$` mkdir /tmp/ec2-instance-connect
    `[ec2-user ~]$` curl https://amazon-ec2-instance-connect-us-west-2.s3.us-west-2.amazonaws.com/latest/linux_amd64/ec2-instance-connect-2.0.0-5.rhel9.x86_64.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect.rpm
    `[ec2-user ~]$` curl https://amazon-ec2-instance-connect-us-west-2.s3.us-west-2.amazonaws.com/latest/linux_amd64/ec2-instance-connect-selinux-2.0.0-5.noarch.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
    `[ec2-user ~]$` sudo yum install -y /tmp/ec2-instance-connect/ec2-instance-connect.rpm /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
    ```

    ARM (AArch64)



    ```
    `[ec2-user ~]$` mkdir /tmp/ec2-instance-connect
    `[ec2-user ~]$` curl https://amazon-ec2-instance-connect-us-west-2.s3.us-west-2.amazonaws.com/latest/linux_arm64/ec2-instance-connect-2.0.0-5.rhel9.aarch64.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect.rpm
    `[ec2-user ~]$` curl https://amazon-ec2-instance-connect-us-west-2.s3.us-west-2.amazonaws.com/latest/linux_arm64/ec2-instance-connect-selinux-2.0.0-5.noarch.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
    `[ec2-user ~]$` sudo yum install -y /tmp/ec2-instance-connect/ec2-instance-connect.rpm /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
    ```

You should see the following new script in the
`/opt/aws/bin/` folder:

```
eic_run_authorized_keys
```

4.  (Optional) Verify that EC2 Instance Connect was successfully
    installed on your instance.

        * For RHEL 8:



        ```
        `[ec2-user ~]$` sudo less /lib/systemd/system/sshd.service.d/ec2-instance-connect.conf
        ```
        * For RHEL 9:



        ```
        `[ec2-user ~]$` sudo less /etc/ssh/sshd_config.d/60-ec2-instance-connect.conf
        ```

    EC2 Instance Connect was successfully installed if the
    `AuthorizedKeysCommand` and
    `AuthorizedKeysCommandUser` lines contain the
    following values:

```
AuthorizedKeysCommand /opt/aws/bin/eic_run_authorized_keys %u %f
AuthorizedKeysCommandUser ec2-instance-connect
```

    * `AuthorizedKeysCommand` sets the
     `eic_run_authorized_keys` script
     to look up the keys from the instance metadata
    * `AuthorizedKeysCommandUser` sets the system
     user as `ec2-instance-connect`

###### Note

If you previously configured
`AuthorizedKeysCommand` and
`AuthorizedKeysCommandUser`, the
EC2 Instance Connect installation will not change the values and
you will not be able to use EC2 Instance Connect.

Ubuntu

###### To install EC2 Instance Connect on an instance launched with Ubuntu

16.04 or later

1. Connect to your instance using SSH.

Replace the example values in the following command with your
values. Use the SSH key pair that was assigned to your instance
when you launched it and use the default username of the AMI
that you used to launch your instance. For an Ubuntu AMI, the
username is `ubuntu`.

```
`$` ssh -i `my_ec2_private_key`.pem `ubuntu`@`ec2-a-b-c-d.us-west-2.compute.amazonaws.com`
```

For more information about connecting to your instance, see
[Connect to your Linux instance using an SSH client](connect-linux-inst-ssh.md "connect-linux-inst-ssh.md"). 2. (Optional) Ensure your instance has the latest Ubuntu
AMI.

Run the following commands to update all the packages on your
instance.

```
`ubuntu:~$` sudo apt-get update
```

```
`ubuntu:~$` sudo apt-get upgrade
```

3. Install the EC2 Instance Connect package on your instance.

```
`ubuntu:~$` sudo apt-get install ec2-instance-connect
```

You should see three new scripts in the
`/usr/share/ec2-instance-connect/` folder:

```
eic_curl_authorized_keys
eic_parse_authorized_keys
eic_run_authorized_keys
```

4. (Optional) Verify that EC2 Instance Connect was successfully
   installed on your instance.

```
`ubuntu:~$` sudo less /lib/systemd/system/ssh.service.d/ec2-instance-connect.conf
```

EC2 Instance Connect was successfully installed if the
`AuthorizedKeysCommand` and
`AuthorizedKeysCommandUser` lines contain the
following values:

```
AuthorizedKeysCommand /usr/share/ec2-instance-connect/eic_run_authorized_keys %%u %%f
AuthorizedKeysCommandUser ec2-instance-connect
```

    * `AuthorizedKeysCommand` sets the
     `eic_run_authorized_keys` script
     to look up the keys from the instance metadata
    * `AuthorizedKeysCommandUser` sets the system
     user as `ec2-instance-connect`

###### Note

If you previously configured
`AuthorizedKeysCommand` and
`AuthorizedKeysCommandUser`, the
EC2 Instance Connect installation will not change the values and
you will not be able to use EC2 Instance Connect.

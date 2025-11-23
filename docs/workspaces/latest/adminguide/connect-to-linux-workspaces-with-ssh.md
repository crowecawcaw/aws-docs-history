# Enable SSH connections for

your Linux WorkSpaces in WorkSpaces Personal

If you or your users want to connect to your Linux WorkSpaces by using the command line,
you can enable SSH connections. You can enable SSH connections to all WorkSpaces in a
directory or to individual WorkSpaces in a directory.

To enable SSH connections, you create a new security group or update an existing
security group and add a rule to allow inbound traffic for this purpose. Security groups
act as a firewall for associated instances, controlling both inbound and outbound traffic
at the instance level. After you create or update your security group, your users and
others can use PuTTY or other terminals to connect from their devices to your Linux
WorkSpaces. For more information, see [Security groups for WorkSpaces Personal](amazon-workspaces-security-groups.md "amazon-workspaces-security-groups.md").

For a video tutorial, see [How can I connect to my Linux Amazon WorkSpaces using SSH?](https://aws.amazon.com/premiumsupport/knowledge-center/linux-workspace-ssh/ "https://aws.amazon.com/premiumsupport/knowledge-center/linux-workspace-ssh/") on the AWS Knowledge Center.
This tutorial is for Amazon Linux 2 WorkSpaces only.

###### Contents

- [Prerequisites for SSH
  connections to Linux WorkSpaces](#before-you-begin-enable-ssh-linux-workspaces "#before-you-begin-enable-ssh-linux-workspaces")
- [Enable SSH
  connections to all Linux WorkSpaces in a directory](#enable-ssh-directory-level-access-linux-workspaces "#enable-ssh-directory-level-access-linux-workspaces")
- [Password-based authentication in WorkSpaces](#enable-ssh-access-old-version "#enable-ssh-access-old-version")
- [Enable SSH connections to a
  specific Linux WorkSpace](#enable-ssh-access-specific-linux-workspace "#enable-ssh-access-specific-linux-workspace")
- [Connect to a Linux
  WorkSpace using Linux or PuTTY](#ssh-connection-linux-workspace-using-linux-or-putty "#ssh-connection-linux-workspace-using-linux-or-putty")

## Prerequisites for SSH

connections to Linux WorkSpaces

- Enabling inbound SSH traffic to a WorkSpace — To add a rule to allow
  inbound SSH traffic to one or more Linux WorkSpaces, make sure that you have the
  public or private IP addresses of the devices that require SSH connections to your
  WorkSpaces. For example, you can specify the public IP addresses of devices
  outside your virtual private cloud (VPC) or the private IP address of another EC2
  instance in the same VPC as your WorkSpace.

If you plan to connect to a WorkSpace from your local device, you can use the
search phrase "what is my IP address" in an internet browser or use the following
service: [Check IP](https://checkip.amazonaws.com/ "https://checkip.amazonaws.com/").

- Connecting to a WorkSpace — The following information is required to
  initiate an SSH connection from a device to a Linux WorkSpace.
  - The NetBIOS name of the Active Directory domain that you are connected
    to.
  - Your WorkSpace user name.
  - The public or private IP address of the WorkSpace that you want to
    connect to.

  Private: If your VPC is attached to a corporate network and you have
  access to that network, you can specify the private IP address of the
  WorkSpace.

  Public: If your WorkSpace has a public IP address, you can use the
  WorkSpaces console to find the public IP address, as described in the
  following procedure.

###### To find the IP addresses for the Linux WorkSpace you want to connect to and your

user name

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **WorkSpaces**.
3. In the list of WorkSpaces, choose the WorkSpace that you want to enable SSH
   connections to.
4. In the **Running mode** column, confirm that the WorkSpace
   status is **Available**.
5. Click the arrow to the left of the WorkSpace name to display the inline
   summary, and note the following information:
   - The **WorkSpace IP**. This is the private IP address of
     the WorkSpace.

   The private IP address is required for obtaining the elastic network
   interface associated with the WorkSpace. The network interface is required
   to retrieve information such as the security group or public IP address
   associated with the WorkSpace.
   - The WorkSpace **Username**. This is the user name that
     you specify to connect to the WorkSpace.

6. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
7. In the navigation pane, choose **Network Interfaces**.
8. In the search box, type the **WorkSpace IP** that you noted in
   Step 5.
9. Select the network interface associated with the **WorkSpace
   IP**.
10. If your WorkSpace has a public IP address, it is displayed in the
    **IPv4 Public IP** column. Make a note of this address, if
    applicable.

###### To find the NetBIOS name of the Active Directory domain that you are connected

to

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. In the list of directories, click the **Directory ID** link of
   the directory for the WorkSpace.
3. In the **Directory details** section, note the
   **Directory NetBIOS name**.

## Enable SSH

connections to all Linux WorkSpaces in a directory

To enable SSH connections to all Linux WorkSpaces in a directory, do the
following.

###### To create a security group with a rule to allow inbound SSH traffic to all Linux

WorkSpaces in a directory

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Security Groups**.
3. Choose **Create Security Group**.
4. Type a name and optionally, a description for your security group.
5. For **VPC**, choose the VPC that contains the WorkSpaces that
   you want to enable SSH connections to.
6. On the **Inbound** tab, choose **Add Rule**,
   and do the following:
   - For **Type**, choose **SSH**.
   - For **Protocol**, TCP is automatically specified when
     you choose **SSH**.
   - For **Port Range**, 22 is automatically specified when
     you choose **SSH**.
   - For **Source**, specify the CIDR range of the public IP
     addresses for the computers that users will use to connect to their
     WorkSpaces. For example, a corporate network or a home network.
   - For **Description** (optional), type a description for
     the rule.

7. Choose **Create**.
8. Attach this security group to your WorkSpaces. For more information on adding this security group to your WorkSpaces, see
   [Security groups for WorkSpaces Personal](amazon-workspaces-security-groups.md "amazon-workspaces-security-groups.md").
   If you want to automatically attach additional security groups to your WorkSpaces, refer to this
   [blog post](https://aws.amazon.com/blogs/desktop-and-application-streaming/automatically-attach-additional-security-groups-to-amazon-appstream-2-0-and-amazon-workspaces/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/automatically-attach-additional-security-groups-to-amazon-appstream-2-0-and-amazon-workspaces/").

## Password-based authentication in WorkSpaces

###### To enable password authentication in newly created Linux WorkSpaces

1. Launch the WorkSpaces client and login to your WorkSpace.
2. Open the Terminal window.
3. In the Terminal window, run the following command to enable SSH Password Authentication in cloud-init.

```
sudo bash -c 'touch /etc/cloud/cloud.cfg.d/15_sshpwauth.cfg && echo "ssh_pwauth: true" > /etc/cloud/cloud.cfg.d/15_sshpwauth.cfg && sudo rm /var/lib/cloud/instance/sem/config_set_passwords && sudo cloud-init single --name set-passwords'
```

This script will do the following:

    * Create a configuration file in the cloud-init directory `/etc/cloud/cloud.cfg.d/`.
    * Modify the configuration file to tell cloud-init to enable SSH password authentication.
    * Reset the `set-passwords` cloud-init module so that it can be run again.
    * Run the `set-passwords` cloud-init module by itself. This will write a file that enables SSH password authentication
     to the SSH configuration directory, `/etc/ssh/sshd_config.d/`, and restart SSHD so that the setting will take place immediately.

This enables SSH password authentication on your WorkSpace and will persist through custom images.
If you enable SSH password authentication only in the SSHD configuration file,
without configuring cloud-init, the setting will not persist through imaging on some Linux WorkSpaces.
For more information, see Set Passwords in the cloud-init module documentation.

###### To disable password authentication in existing Linux WorkSpaces

1. Launch the WorkSpaces client and login to your WorkSpace.
2. Open the Terminal window.
3. In the Terminal window, run the following command to disable SSH Password Authentication in cloud-init.

```
sudo bash -c 'touch /etc/cloud/cloud.cfg.d/15_sshpwauth.cfg && echo "ssh_pwauth: false" > /etc/cloud/cloud.cfg.d/15_sshpwauth.cfg && sudo rm /var/lib/cloud/instance/sem/config_set_passwords && sudo cloud-init single —name set-passwords'
```

This script will do the following:

    * Create a configuration file in the cloud-init directory `/etc/cloud/cloud.cfg.d/`.
    * Modify the configuration file to tell cloud-init to disable SSH password authentication.
    * Reset the `set-passwords` cloud-init module so that it can be run again.
    * Run the `set-passwords` cloud-init module by itself. This will write a file that enables SSH password authentication
     to the SSH configuration directory, `/etc/ssh/sshd_config.d/`, and restart SSHD so that the setting will take place immediately.

This immediately disables SSH in the WorkSpace and will persist through custom images.

## Enable SSH connections to a

specific Linux WorkSpace

To enable SSH connections to a specific Linux WorkSpace, do the following.

###### To add a rule to an existing security group to allow inbound SSH traffic to a

specific Linux WorkSpace

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Network & Security**,
   choose **Network Interfaces**.
3. In the search bar, type the private IP address of the WorkSpace that you want
   to enable SSH connections to.
4. In the **Security groups** column, click the link for the
   security group.
5. On the **Inbound** tab, choose
   **Edit**.
6. Choose **Add Rule**, and then do the following:
   - For **Type**, choose **SSH**.
   - For **Protocol**, TCP is automatically specified when
     you choose **SSH**.
   - For **Port Range**, 22 is automatically specified when
     you choose **SSH**.
   - For **Source**, choose **My IP** or
     **Custom**, and specify a single IP address or an IP
     address range in CIDR notation. For example, if your IPv4 address is
     `203.0.113.25`, specify `203.0.113.25/32` to list
     this single IPv4 address in CIDR notation. If your company allocates
     addresses from a range, specify the entire range, such as
     `203.0.113.0/24`.
   - For **Description** (optional), type a description for
     the rule.

7. Choose **Save**.

## Connect to a Linux

WorkSpace using Linux or PuTTY

After you create or update your security group and add the required rule, your users and
others can use Linux or PuTTY to connect from their devices to your WorkSpaces.

###### Note

Before completing either of the following procedures, make sure that you have the
following:

- The NetBIOS name of the Active Directory domain that you are connected
  to.
- The username that you use to connect to the WorkSpace.
- The public or private IP address of the WorkSpace that you want to connect
  to.
  For instructions on how to obtain this information, see "Prerequisites for SSH
  Connections to Linux WorkSpaces" earlier in this topic.

###### To connect to an Linux WorkSpace using Linux

1. Open the command prompt as an administrator and enter the following command. For
   `NetBIOS name`, `Username`, and
   `WorkSpace IP`, enter the applicable values.

```
`ssh "``NetBIOS_NAME``\``Username``"@``WorkSpaceIP`
```

The following is an example of the SSH command where:

    * The `NetBIOS_NAME` is anycompany
    * The `Username` is janedoe
    * The `WorkSpace IP` is 203.0.113.25

```
`ssh "anycompany\janedoe"@203.0.113.25`
```

2. When prompted, enter the same password that you use when authenticating with the
   WorkSpaces client (your Active Directory password).

###### To connect to an Linux WorkSpace using PuTTY

1.  Open PuTTY.
2.  In the **PuTTY Configuration** dialog box, do the
    following:

        * For **Host Name (or IP address)**, enter the following
         command. Replace the values with the NetBIOS name of the Active Directory
         domain that you are connected to, the user name that you use to connect to the
         WorkSpace, and the IP address of the WorkSpace that you want to connect
         to.



        ```
        `NetBIOS_NAME``\``Username``@``WorkSpaceIP`
        ```
        * For **Port**, enter `22`.
        * For **Connection type**, choose
         **SSH**.

    For an example of the SSH command, see step 1 in the previous procedure.

3.  Choose **Open**.
4.  When prompted, enter the same password that you use when authenticating with the
    WorkSpaces client (your Active Directory password).

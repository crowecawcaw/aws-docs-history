# Mounting on EC2 Mac instances

using the EFS mount helper

This procedure requires the following:

- You have installed the `amazon-efs-utils` package on the Amazon EC2 Mac
  instance. For more information, see [Installing the Amazon EFS client on EC2 Mac instances
  running macOS Big Sur, macOS Monterey, or macOS Ventura](installing-amazon-efs-utils.md#install-efs-utils-macOS "installing-amazon-efs-utils.md#install-efs-utils-macOS").
- You have created mount targets for the file system. You can create mount targets at file system creation and
  add them to existing file systems. For more information, see [Managing mount targets](accessing-fs.md "accessing-fs.md").
- You are mounting the file system on an EC2 Mac instance running macOS Big Sur,
  Monterey, or Ventura. Other macOS versions are not supported.

###### Note

Only EC2 Mac instances running macOS Big Sur, Monterey, and Ventura are supported. Other
macOS versions are not supported for use with Amazon EFS.

###### To mount your EFS file system using the EFS mount helper on

EC2 Mac instances running macOS Big Sur, Monterey, or Ventura

1. Open a terminal window on your EC2 Mac instance through Secure Shell (SSH),
   and log in with the appropriate user name. For more information, see [Connect to your
   EC2 instance](../../../AWSEC2/latest/UserGuide/connect.md "../../../AWSEC2/latest/UserGuide/connect.md") in the
   _Amazon EC2 User Guide_.
2. Create a directory to use as the file system mount point using the following command:

```
sudo mkdir efs
```

3. Run the following command to mount your file system.

###### Note

By default, the EFS mount helper uses encryption in transit when mounting on
EC2 Mac instances, whether or not you use the `tls` option in the
mount command.

```
sudo mount -t efs `file-system-id` `efs-mount-point/`
```

```
sudo mount -t efs fs-abcd123456789ef0 efs/
```

You can also use the `tls` option when mounting.

```
sudo mount -t efs -o tls fs-abcd123456789ef0:/ efs
```

To mount a file system on an EC2 Mac instance without using encryption in
transit, use the `notls` option, as shown in the following command.

```
sudo mount -t efs -o notls `file-system-id` `efs-mount-point/`
```

You can view and copy the exact commands to mount your file system in the management console's
**Attach** dialog box, described as follows.

    1. In the Amazon EFS console, choose the file system that you want to mount to display its details
     page.
    2. To display the mount commands to use for this file system, choose **Attach** in the upper right.


    The **Attach** screen displays the exact commands to use for mounting the file system in the following ways:




    	* (**Mount via DNS**) Using the file system's DNS name with the EFS
    	 mount helper or an NFS client.
    	* (**Mount via IP**) Using the mount target IP address in the selected
    	 Availability Zone with an NFS client.

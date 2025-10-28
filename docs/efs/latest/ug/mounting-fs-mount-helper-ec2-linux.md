# Mounting on EC2 Linux instances

using the EFS mount helper

This procedure requires the following:

- You have installed the `amazon-efs-utils` package on the Amazon EC2
  instance. For more information, see [Manually installing the Amazon EFS client](installing-amazon-efs-utils.md "installing-amazon-efs-utils.md").
- You have created mount targets for the file system. For more information, see [Managing mount targets](accessing-fs.md "accessing-fs.md").

###### To mount your EFS file system using

the mount helper on EC2 Linux instances

1. Open a terminal window on your EC2 instance through Secure Shell (SSH), and
   log in with the appropriate user name. For more information, see
   [Connect to your
   EC2 instance](../../../AWSEC2/latest/UserGuide/connect.md "../../../AWSEC2/latest/UserGuide/connect.md") in the
   _Amazon EC2 User Guide_.
2. Create a directory `efs` that you will use as the file system mount point using the following command:

```
sudo mkdir efs
```

3. Run one of the following commands to mount your file system.

###### Note

If the EC2 instance and the file system you are mounting are located in different
AWS Regions, see [Mounting EFS file systems from a different AWS Region](mount-different-region.md "mount-different-region.md") to edit the `region` property in
the `efs-utils.conf` file.

    * To mount using the file system id:



    ```
    sudo mount -t efs `file-system-id` `efs-mount-point`/
    ```

    Use the ID of the file system you are mounting in place ``file-system-id`` and `efs` in place of `efs-mount-point`.



    ```
    sudo mount -t efs fs-abcd123456789ef0 efs/
    ```

    Alternatively, if you want to use encryption of data in transit, you can mount your
     file system with the following command.



    ```
    sudo mount -t efs -o tls fs-abcd123456789ef0:/ efs/
    ```
    * To mount using the file system DNS name:



    ```
    sudo mount -t efs -o tls `file-system-dns-name` `efs-mount-point`/
    ```


    ```
    sudo mount -t efs -o tls fs-abcd123456789ef0.efs.us-east-2.amazonaws.com efs/
    ```
    * To mount using the mount target IP address:



    ```
    sudo mount -t efs -o tls,mounttargetip=`mount-target-ip` `file-system-id` `efs-mount-point`/
    ```


    ```
    sudo mount -t efs -o tls,mounttargetip=192.0.2.0 fs-abcd123456789ef0 efs/
    ```

You can view and copy the exact commands to mount your file system in the
**Attach** dialog box.

    1. In the Amazon EFS console, choose the file system that you want to mount to display its details
     page.
    2. To display the mount commands to use for this file system, choose **Attach** in the upper right.


    The **Attach** screen displays the exact commands to use for mounting the file system in the following ways:




    	* (**Mount via DNS**) Using the file system's DNS name with the EFS
    	 mount helper or an NFS client.
    	* (**Mount via IP**) Using the mount target IP address in the selected
    	 Availability Zone with an NFS client.

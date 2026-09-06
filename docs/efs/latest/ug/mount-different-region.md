

# Mounting EFS file systems from a different AWS Region
<a name="mount-different-region"></a>

To mount your EFS file system from an EC2 instance that is in a different AWS Region than the file system, you must edit the `region` property value in the `efs-utils.conf` file.

**To edit the `region` property in `efs-utils.conf`**

1. Access the terminal for your EC2 instance through Secure Shell (SSH), and log in with the appropriate user name. For more information, see [Connect to your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html) in the *Amazon EC2 User Guide*. 

1. Locate the `/etc/amazon/efs/efs-utils.conf` file, and open it using your preferred editor.

1. Locate the following line:

   ```
   #region = us-east-1
   ```

   1. Uncomment the line.

   1. If the file system is not located in the `us-east-1` Region, replace `us-east-1` with the ID of the Region in which the file system is located.

   1. Save the changes.

1. Add a host entry for the cross region mount. For more information on how to do this, see [Step 3: Add a host entry for the mount target](efs-different-vpc.md#wt6-efs-utils-step3).

1. Mount the file system using the EFS mount helper for [Linux](mounting-fs-mount-helper-ec2-linux.md) or [Mac](mounting-fs-mount-helper-ec2-mac.md) instances.
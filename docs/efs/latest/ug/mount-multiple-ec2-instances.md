# Mounting EFS to multiple

EC2 instances

You can mount EFS file systems to multiple Amazon EC2 instances remotely and
securely without having to log in to the instances by using the AWS Systems Manager
Run Command. For more information about AWS Systems Manager Run Command, see
[AWS Systems Manager Run
Command](../../../systems-manager/latest/userguide/run-command.md "../../../systems-manager/latest/userguide/run-command.md") in the _AWS Systems Manager User Guide_. The following prerequisites
are required before mounting EFS file systems using this method:

1. The EC2 instances are launched with an instance profile that includes the
   `AmazonElasticFileSystemsUtils` permissions policy. For more information,
   see [Step 1: Configure an IAM instance
   profile with the required permissions](setting-up-aws-sys-mgr.md#configure-sys-mgr-iam-instance-profile "setting-up-aws-sys-mgr.md#configure-sys-mgr-iam-instance-profile").
2. Version 1.28.1 or later of the Amazon EFS client (amazon-efs-utils package) is installed on the
   EC2 instances. You can use AWS Systems Manager to automatically install the
   package on your instances. For more information, see [Step 2: Configure an association used by State
   Manager](setting-up-aws-sys-mgr.md#config-sys-mgr-association "setting-up-aws-sys-mgr.md#config-sys-mgr-association").

###### To mount multiple EFS file systems to multiple EC2 instances using

the console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Run Command**.
3. Choose **Run a command**.
4. Enter `AWS-RunShellScript` in the **Commands** search field.
5. Select **AWS-RunShellScript**.
6. In **Command parameters** enter the mount command to use for each
   EFS file system that you want to mount. For example:

```
sudo mount -t efs -o tls fs-12345678:/ /mnt/efs
sudo mount -t efs -o tls,accesspoint=fsap-12345678 fs-01233210 /mnt/efs
```

For more information about EFS mount commands using the Amazon EFS client, see
[Mounting on EC2 Linux instances
using the EFS mount helper](mounting-fs-mount-helper-ec2-linux.md "mounting-fs-mount-helper-ec2-linux.md") or [Mounting on EC2 Mac instances
using the EFS mount helper](mounting-fs-mount-helper-ec2-mac.md "mounting-fs-mount-helper-ec2-mac.md"). 7. Select the target AWS Systems Manager managed EC2 instances that you want the command to run
on. 8. Make any other additional settings you would like. Then choose **Run** to run
the command and mount the EFS file systems specified in the command.

Once you run the command, you can see its status in the command
history.

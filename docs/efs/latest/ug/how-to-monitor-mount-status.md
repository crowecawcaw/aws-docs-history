# Monitoring mount attempt successes and failures

You can use Amazon CloudWatch Logs to monitor and report the success or failure of mount attempts for
your EFS file systems remotely without having to log into the clients. Use the
following procedure to configure your EC2 instance to use CloudWatch Logs to monitor the
success or failure of its file system mount attempts.

###### To enable mount attempt success or failure notification in CloudWatch logs

1. Install `amazon-efs-utils` on the EC2 instance mounting the file system. For more information, see
   [Automatically installing or updating
   Amazon EFS client using AWS Systems Manager](manage-efs-utils-with-aws-sys-manager.md "manage-efs-utils-with-aws-sys-manager.md") or
   [Manually installing the Amazon EFS client](installing-amazon-efs-utils.md "installing-amazon-efs-utils.md").
2. Install `botocore` on the EC2 instance that will mount the file system. For more information, see
   [Installing and upgrading botocore](install-botocore.md "install-botocore.md").
3. Enable the CloudWatch Logs feature in `amazon-efs-utils`. When
   you use AWS Systems Manager to install and configure `amazon-efs-utils`,
   CloudWatch logging is automatically done for you. When you
   install the `amazon-efs-utils` package manually, you
   have to manually update the `/etc/amazon/efs/efs-utils.conf`
   configuration file by uncommenting the `# enabled = true` line in the
   `cloudwatch-log` section. Use one of the following commands to enable CloudWatch Logs manually.

For Linux instances:

```
sudo sed -i -e '/\[cloudwatch-log\]/{N;s/# enabled = true/enabled = true/}' /etc/amazon/efs/efs-utils.conf
```

For MacOS instances:

```
EFS_UTILS_VERSION= `efs-utils-version`
sudo sed -i -e '/\[cloudwatch-log\]/{N;s/# enabled = true/enabled = true/;}' /usr/local/Cellar/amazon-efs-utils/${EFS_UTILS_VERSION}/libexec/etc/amazon/efs/efs-utils.conf
```

For Mac2 instances:

```
EFS_UTILS_VERSION= `efs-utils-version`
sudo sed -i -e '/\[cloudwatch-log\]/{N;s/# enabled = true/enabled = true/;}' /opt/homebrew/Cellar/amazon-efs-utils/${EFS_UTILS_VERSION}/libexec/etc/amazon/efs/efs-utils.conf
```

4. Optionally, you can configure CloudWatch Logs group names and set the log retention days in the `efs-utils.conf` file.
   If you want to have separate log groups in CloudWatch for each mounted file system, add `/{fs_id}` to the end of the
   `log_group_name` field in `efs-utils.conf` file, as follows:

```
[cloudwatch-log]
log_group_name = /aws/efs/utils/{fs_id}
```

5. Attach the `AmazonElasticFileSystemsUtils` AWS managed policy to the IAM role that you have attached to the EC2 instance,
   or to the AWS credentials configured on your instance. You can use Systems Manager to do this, for more information, see
   [Step 1: Configure an IAM instance
   profile with the required permissions](setting-up-aws-sys-mgr.md#configure-sys-mgr-iam-instance-profile "setting-up-aws-sys-mgr.md#configure-sys-mgr-iam-instance-profile").
   The following are examples of mount attempt status log entries:

```
Successfully mounted fs-12345678.efs.us-east-1.amazonaws.com at /home/ec2-user/efs
Mount failed, Failed to resolve "fs-01234567.efs.us-east-1.amazonaws.com"
```

###### To view mount status in CloudWatch Logs

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Log groups** in the left-hand navigation bar.
3. Choose the **/aws/efs/utils** log group. You will see a log stream for each
   Amazon EC2 instance and EFS file system combination.
4. Choose a log stream to view specific log events including mount attempt success or failure status.

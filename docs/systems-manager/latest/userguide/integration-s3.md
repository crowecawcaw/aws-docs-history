AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Running scripts from Amazon S3

This section describes how to download and run scripts from Amazon Simple Storage Service (Amazon S3). The
following topic includes information and terminology relating to Amazon S3. To learn more
about Amazon S3, see [What is Amazon S3?](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") You can run
different types of scripts, including Ansible Playbooks, Python, Ruby, Shell, and
PowerShell.

You can also download a directory that includes multiple scripts. When you run the
primary script in the directory, AWS Systems Manager also runs any referenced scripts that are
included in the directory.

Note the following important details about running scripts from Amazon S3:

- Systems Manager doesn't verify that your script is capable of running on an node.
  Before you download and run the script, verify that the required software is
  installed on the node. Or, you can create a composite document that installs
  the software by using either Run Command or State Manager, tools in AWS Systems Manager, and
  then downloads and runs the script.
- Verify that your user, role, or group has been granted the AWS Identity and Access Management
  (IAM) permissions needed to read from the S3 bucket.
- Ensure that the instance profile on your Amazon Elastic Compute Cloud (Amazon EC2) instances has
  `s3:ListBucket` and `s3:GetObject` permissions. If
  the instance profile doesn't have these permissions, the system fails to
  download your script from the S3 bucket. For more information, see [Using instance profiles](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md") in the
  _IAM User Guide_.

## Run shell scripts from Amazon S3

This following information includes procedures to help you run scripts from
Amazon Simple Storage Service (Amazon S3) by using either the AWS Systems Manager console or the AWS Command Line Interface (AWS CLI).
Though shell scripts are used in the examples, other types of scripts can be
substituted.

### Run a shell script from Amazon S3

(console)

###### Run a shell script from Amazon S3

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Run Command**.
3. Choose **Run command**.
4. In the **Command document** list, choose
   **`AWS-RunRemoteScript`**.
5. In **Command parameters**, do the
   following:
   - In **Source Type**, select **S3**.
   - In the **Source Info** text box, enter
     the required information to access the source in the
     following format. Replace each `example resource
placeholder` with your own
     information.

   ###### Note

   Replace https://s3.`aws-api-domain` with the URL for your
   bucket. You can copy your bucket URL in Amazon S3 on the
   **Objects** tab.

   ```
   {"path":"https://s3.`aws-api-domain`/`path to script`"}
   ```

   The following is an example.

   ```
   {"path":"https://amzn-s3-demo-bucket.s3.us-east-2.amazonaws.com/scripts/shell/helloWorld.sh"}
   ```

   - In the **Command Line** field, enter
     parameters for the script execution. Here is an
     example.

   ```
   helloWorld.sh argument-1 argument-2
   ```

   - (Optional) In the **Working Directory**
     field, enter the name of a directory on the node where you
     want to download and run the script.
   - (Optional) In **Execution Timeout**,
     specify the number of seconds for the system to wait before
     failing the script command execution.

6. In the **Targets** section, choose the managed nodes on which you want to
   run this operation by specifying tags, selecting instances or edge devices manually, or
   specifying a resource group.

###### Tip

If a managed node you expect to see isn't listed, see [Troubleshooting managed
node availability](fleet-manager-troubleshooting-managed-nodes.md "fleet-manager-troubleshooting-managed-nodes.md") for troubleshooting
tips. 7. For **Other parameters**:

    * For **Comment**, enter information about this command.
    * For **Timeout (seconds)**, specify the number of seconds for the
     system to wait before failing the overall command execution.

8. For **Rate control**:
   - For **Concurrency**, specify either a number or a percentage of
     managed nodes on which to run the command at the same time.

   ###### Note

   If you selected targets by specifying tags applied to managed nodes or by
   specifying AWS resource groups, and you aren't certain how many managed
   nodes are targeted, then restrict the number of targets that can run the
   document at the same time by specifying a percentage.
   - For **Error threshold**, specify when to stop running the command
     on other managed nodes after it fails on either a number or a percentage of nodes.
     For example, if you specify three errors, then Systems Manager stops sending the command when
     the fourth error is received. Managed nodes still processing the command might also
     send errors.

9. (Optional) For **Output options**, to save the command output to a file,
   select the **Write command output to an S3 bucket** box. Enter the bucket
   and prefix (folder) names in the boxes.

###### Note

The S3 permissions that grant the ability to write the data to an S3 bucket are those
of the instance profile (for EC2 instances) or IAM service role (hybrid-activated
machines) assigned to the instance, not those of the IAM user performing this task.
For more information, see [Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md") or [Create an IAM service role for a hybrid
environment](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md"). In addition, if the specified S3 bucket is in a different
AWS account, make sure that the instance profile or IAM service role associated with
the managed node has the necessary permissions to write to that bucket. 10. In the **SNS notifications** section, if you want notifications sent
about the status of the command execution, select the **Enable SNS
notifications** check box.

For more information about configuring Amazon SNS notifications for Run Command, see [Monitoring Systems Manager status changes using
Amazon SNS notifications](monitoring-sns-notifications.md "monitoring-sns-notifications.md"). 11. Choose **Run**.

### Run a shell script from Amazon S3

(command line)

1. Install and configure the AWS Command Line Interface (AWS CLI), if you haven't already.

For information, see [Installing or updating the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"). 2. Run the following command. Replace each `example
 resource placeholder` with your own
information.

###### Note

Replace https://s3.`aws-api-domain`/`script
path` with the URL for your bucket. You can
copy your bucket URL in Amazon S3 on the **Objects**
tab.

Linux & macOS

```
aws ssm send-command \
    --document-name "AWS-RunRemoteScript" \
    --output-s3-bucket-name "`amzn-s3-demo-bucket`" \
    --output-s3-key-prefix "`key-prefix`" \
    --targets "Key=InstanceIds,Values=`instance-id`" \
    --parameters '{"sourceType":["S3"],"sourceInfo":["{\"path\":\"https://s3.`aws-api-domain`/`script path`\"}"],"commandLine":["`script name and arguments`"]}'
```

Windows

```
aws ssm send-command ^
    --document-name "AWS-RunRemoteScript" ^
    --output-s3-bucket-name "`amzn-s3-demo-bucket`" ^
    --output-s3-key-prefix "`key-prefix`" ^
    --targets "Key=InstanceIds,Values=`instance-id`" ^
    --parameters "sourceType"="S3",sourceInfo='{\"path\":\"https://s3.`aws-api-domain`/`script path`\"}',"commandLine"="`script name and arguments`"
```

PowerShell

```
Send-SSMCommand `
    -DocumentName "AWS-RunRemoteScript" `
    -OutputS3BucketName "`amzn-s3-demo-bucket`" `
    -OutputS3KeyPrefix "`key-prefix`" `
    -Target @{Key="InstanceIds";Values=@("`instance-id`")} `
    -Parameter @{
        sourceType = "S3";
        sourceInfo = '{"path": "s3://`bucket-name/path/to/script`"}';
        commandLine = "`script name and arguments`"
    }

```

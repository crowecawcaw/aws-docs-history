• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Run Ansible

Playbooks from GitHub

This section includes procedures to help you run Ansible
Playbooks from GitHub by using either the console or the
AWS Command Line Interface (AWS CLI).

###### Before you begin

If you plan to run a script stored in a private GitHub
repository, create an AWS Systems Manager `SecureString` parameter for your
GitHub security access token. You can't access a script
in a private GitHub repository by manually passing your token
over SSH. The access token must be passed as a Systems Manager
`SecureString` parameter. For more information about creating
a `SecureString` parameter, see [Creating Parameter Store parameters in
Systems Manager](sysman-paramstore-su-create.md "sysman-paramstore-su-create.md").

## Run an

Ansible Playbook from GitHub
(console)

###### Run an Ansible Playbook from

GitHub

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Run Command**.
3. Choose **Run command**.
4. In the **Command document** list, choose
   **`AWS-RunRemoteScript`**.
5. In **Command parameters**, do the
   following:
   - In **Source Type**, select
     **GitHub**.
   - In the **Source Info** box, enter the
     required information to access the source in the following
     format.

   ```
   {
     "owner": "`owner_name`",
     "repository": "`repository_name`",
     "getOptions": "branch:`branch_name`",
     "path": "`path_to_scripts_or_directory`",
     "tokenInfo": "{{ssm-secure:`SecureString_parameter_name`}}"
   }
   ```

   This example downloads a file named
   `webserver.yml`.

   ```
   {
       "owner": "TestUser1",
       "repository": "GitHubPrivateTest",
       "getOptions": "branch:myBranch",
       "path": "scripts/webserver.yml",
       "tokenInfo": "{{ssm-secure:mySecureStringParameter}}"
   }
   ```

   ###### Note

   `"branch"` is required only if your SSM
   document is stored in a branch other than
   `master`.

   To use the version of your scripts that are in a
   particular _commit_ in your
   repository, use `commitID` with
   `getOptions` instead of
   `branch`. For example:

   `"getOptions":
 "commitID:bbc1ddb94...b76d3bEXAMPLE",`
   - In the **Command Line** field, enter
     parameters for the script execution. Here is an
     example.

   `ansible-playbook -i “localhost,” --check -c
 local webserver.yml`
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

## Run an

Ansible Playbook from GitHub by using
the AWS CLI

1. Install and configure the AWS Command Line Interface (AWS CLI), if you haven't already.

For information, see [Installing or updating the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"). 2. Run the following command to download and run a script from
GitHub.

```
aws ssm send-command \
    --document-name "AWS-RunRemoteScript" \
    --instance-ids "`instance-IDs`"\
    --parameters '{"sourceType":["GitHub"],"sourceInfo":["{\"owner\":\"`owner_name`\", \"repository\": \"`repository_name`\", \"path\": \"`path_to_file_or_directory`\", \"tokenInfo\":\"{{ssm-secure:`name_of_your_SecureString_parameter`}}\" }"],"commandLine":["`commands_to_run`"]}'
```

Here is an example command to run on a local Linux machine.

```
aws ssm send-command \
    --document-name "AWS-RunRemoteScript" \
    --instance-ids "i-02573cafcfEXAMPLE" \
    --parameters '{"sourceType":["GitHub"],"sourceInfo":["{\"owner\":\"TestUser1\", \"repository\": \"GitHubPrivateTest\", \"path\": \"scripts/webserver.yml\", \"tokenInfo\":\"{{ssm-secure:mySecureStringParameter}}\" }"],"commandLine":["ansible-playbook -i “localhost,” --check -c local webserver.yml"]}'
```

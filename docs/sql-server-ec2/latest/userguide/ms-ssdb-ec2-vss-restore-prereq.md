# VSS snapshot restore prerequisites

To restore your SQL Server databases from AWS VSS solution based EBS snapshots, you must meet the following
prerequisites.

###### Note

The `AWSEC2-RestoreSqlServerDatabaseWithVss` automation runbook only
supports restoring snapshots to the original EC2 instance where the snapshots were created.

- **Disk management configuration** – Your EC2 database
  instance must be configured with Basic Disks. For more information, see [Basic Disks](https://learn.microsoft.com/en-us/windows/win32/fileio/basic-and-dynamic-disks#basic-disks "https://learn.microsoft.com/en-us/windows/win32/fileio/basic-and-dynamic-disks#basic-disks") on the _Microsoft Learn_ website.
- **Microsoft SQL Server deployment options** – To restore a
  SQL Server database with the `AWSEC2-RestoreSqlServerDatabaseWithVss` automation
  runbook, the database must either be configured as a standalone deployment, or be the primary
  database in a Microsoft SQL Server Always On availability group. For more information,
  see [Deployment options](create-sql-server-on-ec2-instance.md#create-sql-server-deployment-options "create-sql-server-on-ec2-instance.md#create-sql-server-deployment-options").
- **Configure settings to save VSS metadata files** –
  To successfully initiate
  a restore operation, the following two VSS metadata files are required. These files are
  generated for each snapshot set taken during the snapshotting process.

      + `{Snapshot set id}-{timestamp}-BackupComponentDocument.xml`
      + `{Snapshot set id}-{timestamp}-SqlServerWriter.xml`

  To ensure that these files are generated, set the `SaveVssMetadata` parameter
  to `true` when you run the command document.

- [Grant IAM permissions for the restore process](#ms-ssdb-ec2-vss-restore-iam "#ms-ssdb-ec2-vss-restore-iam").

## Grant IAM permissions for the restore process

The `AWSEC2-RestoreSqlServerDatabaseWithVss` automation runbook needs permission
to perform the Amazon EC2 and Systems Manager operations that the runbook uses to restore the database. Follow
these steps to grant the appropriate permissions.

1. [Create an IAM policy to restore a
   SQL Server database from AWS VSS solution based snapshots](#ms-ssdb-ec2-vss-restore-iam-policy "#ms-ssdb-ec2-vss-restore-iam-policy").
2. [Attach the IAM policy to the
   role that's used for the automation runbook](#ms-ssdb-ec2-vss-restore-iam-policy-attach "#ms-ssdb-ec2-vss-restore-iam-policy-attach").

### Create an IAM policy to restore a

SQL Server database from AWS VSS solution based snapshots

To create the IAM policy that grants the permissions needed to restore a Microsoft SQL Server
database from VSS based snapshots in the AWS Management Console, follow these steps.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**, and then
   choose **Create policy**.
3. Choose **JSON** in the policy editor panel.
4. Copy the following policy content into the editor. This policy grants permissions
   to create volumes from VSS snapshots, attach them to instances, and invoke the SSM
   `SendDocument` and `GetDocument` API operations to run the
   automation document for database restoration.

###### Note

(Optional) To enhance security, you can further customize the policy by implementing
custom conditions or specifying exact resource ARNs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CreateVolumeAccessVolume",
 "Effect": "Allow",
 "Action": "ec2:CreateVolume",
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "aws:RequestTag/AwsVssConfig": "*"
 },
 "ArnLike": {
 "ec2:ParentSnapshot": "arn:aws:ec2:*:*:*"
 }
 }
 },
 {
 "Sid": "CreateVolumeWithTagging",
 "Effect": "Allow",
 "Action": "ec2:CreateTags",
 "Resource": "arn:aws:ec2:*:*:volume/*",
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction": "CreateVolume"
 }
 }
 },
 {
 "Sid": "AttachVolumeAccessVolume",
 "Effect": "Allow",
 "Action": "ec2:AttachVolume",
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "ec2:ResourceTag/AwsVssConfig": "*"
 }
 }
 },
 {
 "Sid": "AttachVolumeAccessInstance",
 "Effect": "Allow",
 "Action": "ec2:AttachVolume",
 "Resource": "arn:aws:ec2:*:*:instance/*"
 },
 {
 "Sid": "DescribeVolumes",
 "Effect": "Allow",
 "Action": "ec2:DescribeVolumes",
 "Resource": "*"
 },
 {
 "Sid": "DescribeSnapshots",
 "Effect": "Allow",
 "Action": "ec2:DescribeSnapshots",
 "Resource": "*"
 },
 {
 "Sid": "DescribeInstanceAttribute",
 "Effect": "Allow",
 "Action": "ec2:DescribeInstanceAttribute",
 "Resource": "arn:aws:ec2:*:*:instance/*"
 },
 {
 "Sid": "SsmAutomationRead",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeInstanceInformation",
 "ssm:ListCommandInvocations",
 "ssm:ListCommands"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SsmRunCommand",
 "Effect": "Allow",
 "Action": [
 "ssm:SendCommand",
 "ssm:GetDocument"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:instance/*",
 "arn:aws:ssm:*:*:document/AWSEC2-RestoreSqlServerDatabaseWithVss",
 "arn:aws:ssm:*:*:document/AWS-ConfigureAWSPackage",
 "arn:aws:ssm:*:*:document/AWSEC2-PrepareVssRestore",
 "arn:aws:ssm:*:*:document/AWSEC2-RunVssRestoreForSqlDatabase"
 ]
 }
 ]
}`

```

5. Choose **Next**.
6. Enter a unique name and optional description for your policy, then
   choose **Create policy**.

### Attach the IAM policy to the

role that's used for the automation runbook

You can choose from the following options to attach your policy to the role that
Systems Manager uses for the `AWSEC2-RestoreSqlServerDatabaseWithVss` automation
runbook.

- Create a role, attach your policy, and add a PassRole policy to restrict access.
  The automation assumes the role that's specified in the `AutomationAssumeRole`
  parameter. Expand the `Invoke automation with an assumed role (recommended)`
  section to see detailed steps.
- Attach the policy to your console role. The automation uses the console role
  that's defined for your current session. Expand the `Invoke automation with 
current session’s console role` section to see detailed steps.

###### Step 1: Create the role that the automation assumes and attach your policy

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose `Roles`, and then choose
   **Create role**. This opens the **Select trusted
   entity** page.
3. In the **Trusted entity type** panel, choose
   **AWS service**. This is the default selection.
4. In the **Use case** panel, select **Systems Manager**
   from the list, and then choose **Next**. This opens the
   **Add permissions** page.
5. Search for the name of the policy that you created for the database restore
   runbook. Select the check box next to the name and then choose
   **Next**. This takes you to the **Name, review, and
   create** page.
6. In the **Role details** panel, enter **Role name**
   and **Description**.
7. When you've finished reviewing, choose **Create role**. This
   takes you back to the **Roles** page.
8. Open the detail page for the role that you just created. Take note of the
   **Role Name** at the top for future reference.

Copy the **Role ARN** from the **Summary**
panel to use in the next steps, then continue to Step 2 to create a PassRole policy
for your role.

###### Step 2: Create an inline policy to pass the role that the automation assumes

1. In the detail page for the role that you just created, choose the
   **Permissions** tab.
2. Choose **Add inline policy** from the **Add
   permissions** menu. This opens the **Specify
   permissions** page.
3. Select the **Visual** policy editor.
4. Choose **IAM** from the **Service**
   list.
5. In the **Actions allowed** search box, enter
   `PassRole`, then select the **PassRole**
   check box.
6. The **Resources** panel opens with the
   **Specific** option selected by default. Select the
   **Add ARNs** link to open a panel where you can
   specify the ARN for your role.
7. In the **Resource ARN** box, paste the
   ARN that you copied at the end of Step 1. IAM automatically populates
   the role name based on the ARN.
8. Choose Add ARNs to save your resource ARN. This takes you back to the
   **Specify permissions** page, and shows your entry.
9. Choose **Next** to review your policy. This opens the
   **Review and create** page.
10. On the Review Policy page, enter a name (for example,
    `VssRestorePassRolePolicy`) and then choose **Next**
    to create the PassRole policy for your role.
11. Open the IAM console at
    [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
12. In the navigation pane, choose **Roles**, and then
    select the role that your current console session is using. The current role
    appears in the upper right corner of the console, where you'll see the
    following pattern:

```
`role`/`user` @ `account`
```

3. In the **Permissions** tab, choose **Attach
   policies** from the **Add permissions** menu. This
   opens the **Attach policy to <selected role>** page.
4. Use the search bar in the **Other permissions policies** panel
   to search for the name of the policy that you created for the database restore
   runbook. Select the check box next to the name and then choose **Add
   permissions**.

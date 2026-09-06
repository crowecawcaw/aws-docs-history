

# VSS snapshot restore prerequisites
<a name="ms-ssdb-ec2-vss-restore-prereq"></a>

To restore your SQL Server databases from AWS VSS solution based EBS snapshots, you must meet the following prerequisites.

**Note**  
The `AWSEC2-RestoreSqlServerDatabaseWithVss` automation runbook only supports restoring snapshots to the original EC2 instance where the snapshots were created.
+ **Disk management configuration** – Your EC2 database instance must be configured with Basic Disks. For more information, see [Basic Disks](https://learn.microsoft.com/en-us/windows/win32/fileio/basic-and-dynamic-disks#basic-disks) on the *Microsoft Learn* website.
+ **Microsoft SQL Server deployment options** – To restore a SQL Server database with the `AWSEC2-RestoreSqlServerDatabaseWithVss` automation runbook, the database must either be configured as a standalone deployment, or be the primary database in a Microsoft SQL Server Always On availability group. For more information, see [Deployment options](create-sql-server-on-ec2-instance.md#create-sql-server-deployment-options).
+ **Configure settings to save VSS metadata files** – To successfully initiate a restore operation, VSS metadata files are required. The following files are generated for each snapshot set taken during the snapshotting process.
  + `{Snapshot set id}-{timestamp}-BCD.xml`
  + `{Snapshot set id}-{timestamp}-SqlServerWriter.xml`
  + `{Snapshot set id}-{timestamp}-VolumeMapping.json`
**Note**  
The volume mapping metadata file (`{Snapshot set id}-{timestamp}-VolumeMapping.json`) maps Windows drives to their corresponding snapshots and is used in VSS restore operations to create EBS volumes from snapshots that contains database files to be restored.

  To ensure that these files are generated, set the `SaveVssMetadata` parameter to `true` when you run the command document.
+ [Grant IAM permissions for the restore process](#ms-ssdb-ec2-vss-restore-iam).

## Grant IAM permissions for the restore process
<a name="ms-ssdb-ec2-vss-restore-iam"></a>

Executing the `AWSEC2-RestoreSqlServerDatabaseWithVss` automation runbook to restore databases needs permissions to perform necessary Amazon EC2 and Systems Manager operations. Follow these steps to grant the appropriate permissions.

1. [Attach the AWSEC2VssRestorePolicy managed policy to the role that's used for the automation execution](#ms-ssdb-ec2-vss-restore-iam-policy-attach).

1. [Grant IAM permissions to the invoker role for starting and managing automation executions](#ms-ssdb-ec2-vss-restore-iam-policy-add).

### Attach the AWSEC2VssRestorePolicy managed policy to the role that's used for the automation execution
<a name="ms-ssdb-ec2-vss-restore-iam-policy-attach"></a>

You can choose from the following options to attach the **AWSEC2VssRestorePolicy** AWS managed policy to the role that Systems Manager uses for interacting with Amazon EC2 and Systems Manager when executing the `AWSEC2-RestoreSqlServerDatabaseWithVss` automation runbook. For more information about this managed policy, see [AWSEC2VssRestorePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSEC2VssRestorePolicy).
+ Create a role, attach the **AWSEC2VssRestorePolicy** managed policy, and add a PassRole policy to restrict access. Use the ARN of this role for the `AutomationAssumeRole` parameter when invoking the automation, and the automation execution will assume this role. Expand the `Invoke automation with an assumed role (recommended)` section to see detailed steps.
+ Attach the **AWSEC2VssRestorePolicy** managed policy to the invoker role that initiates the automation execution, without specifying the `AutomationAssumeRole` parameter. For example, if you start the automation execution from the AWS console, the console role acts as the invoker role. Expand the `Invoke automation without an assumed role` section to see detailed steps.

### Invoke automation with an assumed role (recommended)
<a name="ms-ssdb-ec2-vss-restore-assume-role"></a>

**Step 1: Create the role that the automation assumes and attach your policy**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose `Roles`, and then choose **Create role**. This opens the **Select trusted entity** page.

1. In the **Trusted entity type** panel, choose **AWS service**. This is the default selection.

1. In the **Use case** panel, select **Systems Manager** from the list, and then choose **Next**. This opens the **Add permissions** page.

1. Search for **AWSEC2VssRestorePolicy**. Select the check box next to the name and then choose **Next**. This takes you to the **Name, review, and create** page.

1. In the **Role details** panel, enter **Role name** and **Description**.

1. When you've finished reviewing, choose **Create role**. This takes you back to the **Roles** page.

1. Open the detail page for the role that you just created. Take note of the **Role Name** at the top for future reference.

   Copy the **Role ARN** from the **Summary** panel to use in the next steps, then continue to Step 2 to create a PassRole policy for your role.

**Step 2: Create an inline policy to pass the role that the automation assumes**

1. In the detail page for the role that you just created, choose the **Permissions** tab.

1. Choose **Add inline policy** from the **Add permissions** menu. This opens the **Specify permissions** page.

1. Select the **Visual** policy editor.

1. Choose **IAM** from the **Service** list.

1. In the **Actions allowed** search box, enter `PassRole`, then select the **PassRole** check box.

1. The **Resources** panel opens with the **Specific** option selected by default. Select the **Add ARNs** link to open a panel where you can specify the ARN for your role.

1. In the **Resource ARN** box, paste the ARN that you copied at the end of Step 1. IAM automatically populates the role name based on the ARN.

1. Choose Add ARNs to save your resource ARN. This takes you back to the **Specify permissions** page, and shows your entry.

1. Choose **Next** to review your policy. This opens the **Review and create** page.

1. On the Review Policy page, enter a name (for example, `VssRestorePassRolePolicy`) and then choose **Next** to create the PassRole policy for your role.

### Invoke automation without an assumed role
<a name="ms-ssdb-ec2-vss-restore-use-console-role"></a>

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**, and then select the role that will be used to start the automation execution. For example, if you will start the automation execution from console, you should choose the current console role, which appears in the upper right corner of the console:

   ```
   {{role}}/{{user}} @ {{account}}
   ```

1. In the **Permissions** tab, choose **Attach policies** from the **Add permissions** menu. This opens the **Attach policy to <selected role>** page.

1. Use the search bar in the **Other permissions policies** panel to search for **AWSEC2VssRestorePolicy**. Select the check box next to the name and then choose **Add permissions**.

### Grant IAM permissions to the invoker role for starting and managing automation executions
<a name="ms-ssdb-ec2-vss-restore-iam-policy-add"></a>

To attach necessary permissions to the role that starts and manages the `AWSEC2-RestoreSqlServerDatabaseWithVss` automation executions, follow these steps.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**, and then select the role that will be used to start the automation execution.

1. Choose **Add inline policy** from the **Add permissions** menu. This opens the **Specify permissions** page.

1. Select the **JSON** policy editor and copy the following JSON policy content into the editor. The policy allows the role to:
   + Execute the `AWSEC2-RestoreSqlServerDatabaseWithVss` automation runbook.
   + Stop and send signals to an automation execution.
   + View details about the automation execution after it has been started.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 		 	 	 
       "Statement": [
           {
               "Sid": "StartVssRestoreAutomationExecution",
               "Effect": "Allow",
               "Action": "ssm:StartAutomationExecution",
               "Resource": [
                   "arn:aws:ssm:*:*:document/AWSEC2-RestoreSqlServerDatabaseWithVss",
                   "arn:aws:ssm:*:*:automation-execution/*"
               ]
           },
           {
               "Sid": "ManageVssRestoreAutomationExecution",
               "Effect": "Allow",
               "Action": [
                   "ssm:StopAutomationExecution",
                   "ssm:GetAutomationExecution",
                   "ssm:DescribeAutomationExecutions",
                   "ssm:DescribeAutomationStepExecutions",
                   "ssm:SendAutomationSignal"
               ],
               "Resource": [
                   "arn:aws:ssm:*:*:automation-execution/*"
               ]
           }
       ]
   }
   ```

------

1. If you are to start the `AWSEC2-RestoreSqlServerDatabaseWithVss` automation with an assume role by providing a role arn to the `AutomationAssumeRole` parameter, you will need to add the following permission to the above policy statements, and replace the `[AutomationAssumeRole's ARN]` placeholder with the ARN of the role created in step `Invoke runbook automation with an assumed role (recommended)`. The permission allows the invoker role to pass the automation assume role to Systems Manager.

   ```
   {
   	"Action": "iam:PassRole",
   	"Effect": "Allow",
   	"Resource": [
   		"[AutomationAssumeRole's ARN]"
   	]
   }
   ```

1. Choose **Next** to review your policy. This opens the review and create page.

1. On the **Review Policy** page, enter a name (for example, `VssRestoreRunSSMAutomationPolicy`) and then choose **Next** to create and add the inline policy to your role.
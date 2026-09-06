

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Setting up Change Calendar
<a name="systems-manager-change-calendar-prereqs"></a>

Complete the following before using Change Calendar.

## Install latest command line tools
<a name="change-calendar-prereqs-tools"></a>

Install the latest command line tools to get state information about calendars.


| Requirement | Description | 
| --- | --- | 
| AWS CLI | (Optional) To use the AWS Command Line Interface (AWS CLI) to get state information about calendars, install the newest release of the AWS CLI on your local computer.<br />For more information about how to install or upgrade the CLI, see [Installing, updating, and uninstalling the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) in the *AWS Command Line Interface User Guide*. | 
| AWS Tools for PowerShell | (Optional) To use the Tools for PowerShell to get state information about calendars, install the newest release of Tools for PowerShell on your local computer.<br />For more information about how to install or upgrade the Tools for PowerShell, see [Installing the AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up.html) in the *AWS Tools for PowerShell User Guide*. | 

## Set up permissions
<a name="change-calendar-prereqs-permissions"></a>

If your user, group, or role is assigned administrator permissions, then you have full access to Change Calendar. If you don't have administrator permissions, then an administrator must give you permission by either assigning the `AmazonSSMFullAccess` managed policy, or assigning a policy that provides the necessary permissions to your user, group, or role.

The following permissions are required to work with Change Calendar.

**Change Calendar entries**  
To create, update, or delete a Change Calendar entry, including adding and removing events from the entry, a policy attached to your user, group, or role must allow the following actions:  
+ `ssm:CreateDocument`
+ `ssm:DeleteDocument`
+ `ssm:DescribeDocument`
+ `ssm:DescribeDocumentPermission`
+ `ssm:GetCalendar`
+ `ssm:ListDocuments`
+ `ssm:ModifyDocumentPermission`
+ `ssm:PutCalendar`
+ `ssm:UpdateDocument`
+ `ssm:UpdateDocumentDefaultVersion`

**Calendar state**  
To get information about the current or upcoming state of the calendar, a policy attached to your user, group, or role must allow the following action:  
+ `ssm:GetCalendarState`

**Operational events**  
To view operational events, such as maintenance windows, associations, and planned automations, the policy attached to your user, group, or role must allow the following actions:  
+ `ssm:DescribeMaintenanceWindows`
+ `ssm:DescribeMaintenanceWindowExecution`
+ `ssm:DescribeAutomationExecutions`
+ `ssm:ListAssociations`

**Note**  
Change Calendar entries that are owned by (that is, created by) accounts other than yours are read-only, even if they're shared with your account. Maintenance windows, State Manager associations, and automations aren't shared.
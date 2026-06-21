# Adding and removing AWS Managed Microsoft AD members to groups and groups to groups

With the [AWS Directory Service Data
API](../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/Welcome.md "../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/Welcome.md"), a member can be a user, group, or computer. A user represents a person or
entity that can access your directory. Groups allow you to grant and deny permissions to more
than one user at a time.

Use the following procedures to manage group membership for AWS Managed Microsoft AD users and groups
with AWS Directory Service Data in the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

## Adding a user to a group

Use the following procedure to add an AWS Managed Microsoft AD user to a group with
AWS Directory Service Data in the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

###### Important

When you add an AWS Managed Microsoft AD user to a group, the user inherits the roles and
permissions assigned to the group.

###### Before you begin, complete the following:

- [Creating your AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory "ms_ad_getting_started.md#ms_ad_getting_started_create_directory").
- Enable [user and group management
  for Directory Service Data](ms_ad_users_groups_mgmt_enable_disable.md "ms_ad_users_groups_mgmt_enable_disable.md"). You can only enable this feature from the Primary AWS Region for your directory. For
  more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
- You'll need the necessary IAM permissions to use AWS Directory Service Data. To get started,
  you can use the [AWS managed policy: AWSDirectoryServiceDataFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataFullAccess") or [AWS managed policy: AWSDirectoryServiceDataReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataReadOnlyAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataReadOnlyAccess"). For more
  information, see [Directory Service API permissions: Actions, resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md "UsingWithDS_IAM_ResourcePermissions.md") and [Security
  best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies "../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies").
- [Create an AWS Managed Microsoft AD user](ms_ad_create_user.md "ms_ad_create_user.md").
- [Create an AWS Managed Microsoft AD group](ms_ad_create_group.md "ms_ad_create_group.md").

AWS Management Console
You can add an AWS Managed Microsoft AD member to a group with the AWS Management Console.

###### To add AWS Managed Microsoft AD user to a group with the AWS Management Console

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. From the navigation pane, choose **Active Directory**, and then choose
   **Directories**. You're directed to the
   **Directories** screen where you can view a list of directories
   in your AWS Region.
3. Choose a directory. You're directed to the **Directory
   details** screen.
4. Choose **Groups**. To find groups, enter the group name in
   the search box under the **Groups** section. The tab shows a list
   of groups in your AWS Region.
5. Choose a group. You're directed to the **Group details**
   screen.
6. Choose **Members**. The tab shows a list of users and child
   groups by member type in your group.
7. Under **Members** tab, Choose **Add
   member**.
8. Under **Members**, select the user you want to add to your
   group, and then choose **Add member to group**. To find members,
   enter the user logon name for users and group name for groups in the search box
   under the **Members** section.

AWS CLI
The following describes how to format a request that adds an AWS Managed Microsoft AD member
to a group with the AWS Directory Service Data CLI.

###### To add an AWS Managed Microsoft AD user to a group with the AWS CLI

- To add a user to a group, open the AWS CLI, and run the following command
  with your Directory ID, group name, and member name:

```
aws ds-data add-group-member \
  --directory-id `d-1234567890` \
  --group-name "`your-group-name`" \
  --member-name "`jane.doe`"
```

For more information, see [`add-group-member`](../../../cli/latest/reference/ds-data/add-group-member.md "../../../cli/latest/reference/ds-data/add-group-member.md").

PowerShell
The following describes how to format a request that adds an AWS Managed Microsoft AD member
to a group with AWS Tools for PowerShell.

###### To add an AWS Managed Microsoft AD user to a group with AWS Tools for PowerShell

- To add a user to a group, open PowerShell, and run the
  following command with your Directory ID, group name, and member name:

```
Add-DSDGroupMember `
    -DirectoryId `d-1234567890` `
    -GroupName "`your-group-name`" `
    -MemberName "`jane.doe`"
```

For more information, see [`Add-DSDGroupMember`](../../../powershell/latest/reference/items/Add-DSDGroupMember.md "../../../powershell/latest/reference/items/Add-DSDGroupMember.md").

## Removing a user from a group

With the [AWS Directory Service Data
API](../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/Welcome.md "../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/Welcome.md"), a member can be a user, group, or computer. A user represents a person or
entity that can access your directory. Groups allow you to grant and deny permissions to
more than one user at a time.

Use the following procedure to remove an AWS Managed Microsoft AD user from a group with
AWS Directory Service Data in the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

###### Important

When you remove an AWS Managed Microsoft AD user from a group, the user loses the roles and
permissions assigned to the group.

AWS Management Console
You can remove an AWS Managed Microsoft AD member from a group with the AWS Management Console.

###### To remove an AWS Managed Microsoft AD user from a group with the AWS Management Console

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. From the navigation pane, choose **Active Directory**, and then choose
   **Directories**. You're directed to the
   **Directories** screen where you can view a list of directories
   in your AWS Region.
3. Choose a directory. You're directed to the **Directory
   details** screen.
4. Choose **Groups**. The tab shows a list of groups in your
   AWS Region.
5. Choose a group. To find groups, enter the group name in the search box under
   the **Groups** section. You're directed to the **Group
   details** screen.
6. Choose **Members**. The tab shows a list of users and child
   groups by member type in your group.
7. Select the user you want to remove from your group, and then choose
   **Remove**. To find users, enter the user logon name in the
   search box under the **Members** section.
8. Confirm that you want to remove the user from your group, and then choose
   **Remove** again.

AWS CLI
The following describes how to format a request that removes an AWS Managed Microsoft AD
member from a group with the AWS Directory Service Data CLI.

###### To remove an AWS Managed Microsoft AD user from a group with AWS CLI

- To remove a user from a group, open the AWS CLI, and run the following command
  with your Directory ID, group name, and member name:

```
aws ds-data remove-group-member \
  --directory-id `d-1234567890` \
  --group-name "`your-group-name`" \
  --member-name "`jane.doe`"
```

For more information, see [`remove-group-member`](../../../cli/latest/reference/ds-data/remove-group-member.md "../../../cli/latest/reference/ds-data/remove-group-member.md").

PowerShell
The following describes how to format a request that removes an AWS Managed Microsoft AD
member from a group with AWS Tools for PowerShell.

###### To remove an AWS Managed Microsoft AD user from a group with AWS Tools for PowerShell

- To remove a user from a group, open PowerShell, and run the
  following command with your Directory ID, group name, and member name:

```
Remove-DSDGroupMember `
    -DirectoryId `d-1234567890` `
    -GroupName "`your-group-name`" `
    -MemberName "`jane.doe`"
```

For more information, see [`Remove-DSDGroupMember`](../../../powershell/latest/reference/items/Remove-DSDGroupMember.md "../../../powershell/latest/reference/items/Remove-DSDGroupMember.md").

## Adding a group to a group

When you add an AWS Managed Microsoft AD group to another group, the groups share a parent-child
relationship. The child group gains access to the roles and permissions that are assigned to
the parent group. You can add a child group to your group and your group to a parent
group.

AWS Management Console
You can add an AWS Managed Microsoft AD group to a group with the AWS Management Console.

###### To add a child group to your group with the AWS Management Console

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. From the navigation pane, choose **Active Directory**, and then choose
   **Directories**. You're directed to the
   **Directories** screen where you can view a list of directories
   in your AWS Region.
3. Choose a directory. You're directed to the **Directory
   details** screen.
4. Choose **Groups**. The tab shows a list of groups in your
   AWS Region.
5. Choose a group. To find groups, enter the group name in the search box under
   the **Groups** section. You're directed to the **Group
   details** screen.
6. Choose **Members**. The tab shows a list of users and child
   groups by member type in your group.
7. Choose **Add member**.
8. Under **Members**, select the child group(s) you want to add
   to your group, and then choose **Add member to group**.

###### To add a parent group to a group with the AWS Management Console

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. From the navigation pane, choose **Active Directory**, and then choose
   **Directories**. You're directed to the
   **Directories** screen where you can view a list of directories
   in your AWS Region.
3. Choose a directory. You're directed to the **Directory
   details** screen.
4. Choose **Groups**. The tab shows a list of groups in your
   AWS Region.
5. Choose a group. To find groups, enter the group name in the search box under
   the **Groups** section. You're directed to the **Group
   details** screen.
6. Choose **Parent groups**. The tab shows a list of groups
   that your group is a member of.
7. Choose **Add parent groups**.
8. Under **Groups**, select the group(s) you want to add your
   group to, and then choose **Add parent groups** again.

AWS CLI
The following describes how to format a request that adds an AWS Managed Microsoft AD group
to a group with the AWS Directory Service Data CLI.

###### To add a child group to your group with the AWS CLI

- To add a child group to a parent group, open the AWS CLI, and run the following
  command with your Directory ID, group name, and member name:

```
aws ds-data add-group-member \
  --directory-id `d-1234567890` \
  --group-name "`parent-group-name`" \
  --member-name "`child-group-name`"
```

For more information, see [`add-group-member`](../../../cli/latest/reference/ds-data/add-group-member.md "../../../cli/latest/reference/ds-data/add-group-member.md").

PowerShell
The following describes how to format a request that adds an AWS Managed Microsoft AD group
to a group with AWS Tools for PowerShell.

###### To add a child group to your group with AWS Tools for PowerShell

- To add a child group to a parent group, open PowerShell, and
  run the following command with your Directory ID, group name, and member name:

```
Add-DSDGroupMember `
    -DirectoryId `d-1234567890` `
    -GroupName "`parent-group-name`" `
    -MemberName "`child-group-name`"
```

For more information, see [`Add-DSDGroupMember`](../../../powershell/latest/reference/items/Add-DSDGroupMember.md "../../../powershell/latest/reference/items/Add-DSDGroupMember.md").

## Removing a group from a group

When you remove an AWS Managed Microsoft AD group from another group, the groups no longer share a
parent-child relationship. The child group loses access to the roles and permissions that
are assigned to the parent group. You can remove a child group from your group and your
group from a parent group.

AWS Management Console
You can remove an AWS Managed Microsoft AD group from a group with the AWS Management Console.

###### To remove a child group from your group with the AWS Management Console

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. From the navigation pane, choose **Active Directory**, and then choose
   **Directories**. You're directed to the
   **Directories** screen where you can view a list of directories
   in your AWS Region.
3. Choose a directory. You're directed to the **Directory
   details** screen.
4. Choose **Groups**. The tab shows a list of groups in your
   AWS Region.
5. Choose a group. You're directed to the **Group details**
   screen. To find groups, enter the group name in the search box under the
   **Groups** section.
6. Choose **Members**. The tab shows a list of users and child
   groups by member type in your group.
7. Select the child group(s) you want to remove from your group, and then choose
   **Remove**.
8. Confirm the child group(s) you want to remove from your group, and then
   choose **Remove** again.

###### To remove your group from a parent group with the AWS Management Console

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. From the navigation pane, choose **Active Directory**, and then choose
   **Directories**. You're directed to the
   **Directories** screen where you can view a list of directories
   in your AWS Region.
3. Choose a directory. You're directed to the **Directory
   details** screen.
4. Choose **Groups**. The tab shows a list of groups in your
   AWS Region.
5. Choose a group. You're directed to the **Group details**
   screen. To find groups, enter the group name in the search box under the
   **Groups** section.
6. Choose **Parent groups**. The tab shows a list of groups
   that your group is a member of.
7. Select the parent group you want to remove your group from, and then choose
   **Remove parent groups**.
8. Confirm the parent group you want to remove your group from, and then choose
   **Remove parent groups** again.

AWS CLI
The following describes how to format a request that removes an AWS Managed Microsoft AD group
from a group with the AWS Directory Service Data CLI.

- ###### To remove a child group from a parent group with the AWS CLI

To remove a child group from a parent group, open the AWS CLI, and run the
following command with your Directory ID, group name, and member name:

```
aws ds-data remove-group-member \
  --directory-id `d-1234567890` \
  --group-name "`parent-group-name`" \
  --member-name "`child-group-name`"
```

For more information, see [`remove-group-member`](../../../cli/latest/reference/ds-data/remove-group-member.md "../../../cli/latest/reference/ds-data/remove-group-member.md").

PowerShell
The following describes how to format a request that removes an AWS Managed Microsoft AD group
from a group with AWS Tools for PowerShell.

- ###### To remove a child group from a parent group with AWS Tools for PowerShell

To remove a child group from a parent group, open the
PowerShell, and run the following command with your Directory ID,
group name, and member name:

```
Remove-DSDGroupMember `
    -DirectoryId `d-1234567890` `
    -GroupName "`parent-group-name`" `
    -MemberName "`child-group-name`"
```

For more information, see [`Remove-DSDGroupMember`](../../../powershell/latest/reference/items/Remove-DSDGroupMember.md "../../../powershell/latest/reference/items/Remove-DSDGroupMember.md").

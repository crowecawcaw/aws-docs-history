

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Using global view
<a name="global-view-main"></a>

Use the global view feature to see source servers across various member accounts and to perform various actions such as installing the SSM Agent.

To use global view attach the [AWSOrganizationsReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSOrganizationsReadOnlyAccess.html) managed policy to the user.

The main **Global view** page provides an overview of your account. The information differs for a management account and a member account.
+ Management account: Displays **Account information** that includes the AWS organizations permissions, number of linked accounts, and the total number of source servers, applications, and waves. The **Linked account** section displays the relevant information only for the linked accounts.
+ Member account: Displays the **Account information** that includes the AWS organizations permissions, and the number of source servers, applications, and waves in the specific account.

As a management account, you are able to choose **All accounts** and **My account** from the drop-down menu, changing your view of source servers, applications, or waves.

## Source servers in member accounts
<a name="global-view-source-servers"></a>

As a management account, you can view source servers in your account and all member accounts. You can also perform specific actions on managed servers.

### Single managed source server
<a name="global-view-source-servers-single"></a>

As a management account, you can perform the following actions on a single managed source server.
+ Change staging disk type
+ Edit replication settings
+ Launch settings – edit general launch settings only
+ Post launch
  + Deactivate the post-launch feature for this server
  + Change deployment settings (test and cutover, test only, or cutover only)
+ Start/stop replication
+ Test and cutover drop-down menu: 
  + Launch test 
  + Mark as ready for cutover 
  + Revert to ready for testing
  + Launch cutover
  + Finalize cutover
  + Revert to ready for cutover
  + Terminate launch instances

### Multiple managed source server
<a name="global-view-source-servers-multiple"></a>

As a management account, you can perform the following actions on multiple managed source servers.
+ Edit replication settings – the edited servers must be from the same account
+ Add server to application – the added servers must be from the same account 
+  Disconnect servers from service 
+  Mark as archived 
+  Start/stop replication 

## Applications
<a name="global-view-source-servers-application"></a>

As a management account, you can perform the following actions on a single or multiple managed applications:
+ Add application
+ Edit application
+ Delete application
+ Test and cutover drop-down menu (these actions can also be performed on multiple applications): 
  + Launch test 
  + Mark as ready for cutover 
  + Revert to ready for testing
  + Launch cutover
  + Finalize cutover
  + Revert to ready for cutover
  + Add application to wave
  + Start/stop replication
  + Archive application

## Waves
<a name="global-view-source-servers-wave"></a>

As a management account, you can perform the following actions on a single managed applications:
+ Add wave
+ Edit wave
+ Delete wave
+ Test and cutover drop-down menu (these actions can also be performed on multiple waves):
  + Launch test
  + Mark as ready for cutover 
  + Revert to ready for testing
  + Launch cutover
  + Finalize cutover
  + Revert to ready for cutover
  + Add application to wave
  + Start/stop replication
  + Archive application

## Import/Export
<a name="global-view-source-servers-import-export"></a>

Use this feature to import and export your source servers, applications, and waves from a single or multiple accounts using the CSV template file.
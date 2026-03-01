# Backing up virtual machines

After [Adding a hypervisor](working-with-hypervisors.md#add-hypervisor "working-with-hypervisors.md#add-hypervisor"), Backup gateway
automatically lists your virtual machines. You can view your virtual machines by choosing
either **Hypervisors** or **Virtual machines** in the
left navigation pane.

- Choose **Hypervisors** to view only the virtual machines managed
  by a specific hypervisor. With this view, you can work with one virtual machine at a
  time.
- Choose **Virtual machines** to view all the virtual machines
  across all the hypervisors you added to your AWS account. With this view, you can
  work with some or all your virtual machines across multiple hypervisors.
  Regardless of which view you choose, to perform a backup operation on a specific
  virtual machine, choose its **VM name** to open its detail page. The VM
  detail page is the starting point for the following procedures.

## Creating an on-demand backup of a virtual machine

An [on-demand](recov-point-create-on-demand-backup.md "recov-point-create-on-demand-backup.md") backup is a one-time, full backup you manually initiate. You can
use on-demand backups to test AWS Backup’s backup and restore capabilities.

###### To create an on-demand backup of a virtual machine:

1. Choose **Create on-demand backup**.
2. [Configure your on-demand backup](recov-point-create-on-demand-backup.md "recov-point-create-on-demand-backup.md").
3. Choose **Create on-demand backup**.
4. Check when your backup job has the status `Completed`. In the left
   navigation menu, choose **Jobs**.
5. Choose the **Backup Job ID** to view backup job information
   such as the **Backup size** and time elapsed between the
   **Creation date** and **Completion
   date**.

## Incremental VM backups

Newer VMware versions contain a feature called
[Changed Block Tracking](https://kb.vmware.com/s/article/1020128 "https://kb.vmware.com/s/article/1020128"),
which keeps track of the storage blocks of virtual machines as they change over time.
When you use AWS Backup to back up a virtual machine, AWS Backup attempts to use the CBT data if it
is available. AWS Backup uses CBT data to speed up the backup process; without CBT
data, backup jobs
are often slower and use more hypervisor resources.
The backup can still be successfully completed even when the CBT data is not valid or available.
For example, the CBT data might not be valid or might be unavailable if the virtual machine
or ESXi host experiences a hard shutdown.

On the occasions CBT data is invalid or unavailable, the backup status will read
`Successful` with a message. In these cases, the message will indicate that, in the
absence of CBT data, AWS Backup used its own proprietary change detection mechanism to complete the
backup instead of VMware's CBT data. Subsequent backups will reattempt to use CBT data, and in
most cases the CBT data will be successfully valid and available. If the issue persists, see
[VMware Troubleshooting](vm-troubleshooting.md "vm-troubleshooting.md") for steps to remedy.

For CBT to function correctly, the following must be true:

- Host needs to be ESXi 4.0 or later
- The VM owning the disks must have hardware version 7 or later
- CBT must be enabled for the virtual machine (it is enabled by default)

To verify if a virtual disk has CBT enabled:

1. Open the vSphere Client and select a powered-off virtual machine.
2. Right-click the virtual machine and navigate to
   **Edit Settings** > **Options** > **Advanced/General**
   > **Configuration Parameters**.
3. The option `ctkEnabled` needs to equal `True`.

## Automating virtual machine backup by assigning resources to a backup plan

A [backup plan](about-backup-plans.md "about-backup-plans.md") is a
user-defined data protection policy that automates data protection across many AWS
services and third-party applications. You first create your backup plan by specifying
its backup frequency, retention period, lifecycle policy, and many other options. To
create a backup plan, see Getting started tutorial.

After you create your backup plan, you assign AWS Backup-supported resources, including
virtual machines, to that backup plan. AWS Backup offers [many ways to assign
resources](assigning-resources.md "assigning-resources.md"), including assigning all the resources in your account, including or
excluding single specific resources, or adding resources with certain tags.

In addition to its existing resource assignment features, AWS Backup support for virtual
machines introduces several new features to help you quickly assign virtual machines to
backup plans. From the **Virtual machines** page, you can assign tags
to multiple virtual machines or use the new **Assign resources to
plan** feature. Use these features to assign your virtual machines already
discovered by AWS Backup gateway.

If you anticipate discovering and assigning additional virtual machines in the
future, and would like to automate the resource assignment step to include those future
virtual machines, use the new **Create group assignment**
feature.

## VMware Tags

[**Tags**](API_BGW_VmwareTag.md "API_BGW_VmwareTag.md") are key-value pairs you can use to manage, to filter,
and to search for your resources.

A VMware tag is composed of a **category** and a
**tag name**. VMware tags are used to group virtual machines. A tag name
is a label assigned to a virtual machine. A category is a collection of tag names.

In AWS tags, you can use characters among UTF-8 letters, numbers, spaces, and
special characters `+ - = . _ : /` .

If you use tags on your virtual machines, you can add up to 10 matching tags in
AWS Backup to help with organization. You can map up to 10 VMware tags to AWS tags. In the
[AWS Backup console](https://console.aws.amazon.com/backup/ "https://console.aws.amazon.com/backup/"), these can be found in
**External resources > Virtual Machines > AWS tags** or
**VMware tags**.

### VMware tag mapping

If you use tags on your virtual machines, you can add up to 10 matching tags in AWS Backup
for additional clarity and organization. Mappings apply to any virtual machine on the
hypervisor.

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the console, go to **edit Hypervisor**
   (Click **External resources**, then **Hypervisors**,
   then click the Hypervisor name, then click **Manage mappings**).
3. The last pane, **VMware tag mapping**, contains four
   textbox fields into which you can enter your VMware tag information into
   corresponding AWS tags. The four fields are **Vmware tag category**,
   **VMware tag name**, **AWS tag key**, and
   **AWS tag value** (_example: Category = OS;
   Tag name = Windows; AWS tag key = OS-Windows, and AWS tag value = Windows)_.
4. After you have entered your preferred values, click **Add mapping**.
   If you make an error, you can click **Remove** to delete entered information.
5. After adding mapping(s), specify the IAM role you intend to use to apply these
   AWS tags to the VMware virtual machines.

The policy
[`AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync`](security-iam-awsmanpol.md#aws-managed-policies "security-iam-awsmanpol.md#aws-managed-policies") contains
needed permissions. You can attach this policy to the role you are using (or have an administrator
attached it) or you can create a custom policy for the role being used. 6. Lastly, click **Add hypervisor** or **Save**.

The IAM role trust relationship should be modified to add the
backup-gateway.amazonaws.com and backup.amazonaws.com services.
Without this service, you will likely experience an error
when you map tags. To edit the trust relationship for an existing role,

1. Log into the [IAM console](https://console.aws.amazon.com/iamv2/home?region=us-west-2#/home "https://console.aws.amazon.com/iamv2/home?region=us-west-2#/home").
2. In the navigation pane of the console, choose **Roles**.
3. Choose the name of the role you wish to modify, then select the
   **Trust relationships** tab on the details page.
4. Under **Policy Document, paste the following:**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "backup.amazonaws.com",
 "backup-gateway.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

5. Choose **Update Trust Policy**.

See [Editing the trust
relationship for an existing role](../../../directoryservice/latest/admin-guide/edit_trust.md "../../../directoryservice/latest/admin-guide/edit_trust.md") in the _AWS Directory Service
Administration Guide_ for more detail.

### View VMware tag mappings

In the [AWS Backup console](https://console.aws.amazon.com/backup/ "https://console.aws.amazon.com/backup/"),
click on **External Resources**, then click
on **Hypervisors**, then click on the Hypervisor name link to view properties
for the selected hypervisor. Under the summary pane, there are four tabs, the last of which
is **VMware tag mappings**. Note if you do not yet have mappings, "No
VMware tag mappings." will be displayed.

From here, you can sync the metadata of virtual machines discovered by the hypervisor,
you can copy mappings to your hypervisor(s),
you can add AWS tags mapped to teh VMware tags to the backup selection of a backup plan,
or you can manage mappings.

In the console, to see which tags are applied to a selected virtual machine, click
**Virtual machines**, then the virtual machine name, then
**AWS tags** or **VMware tags**. You can view the
tags associated with this virtual machine, and additionally you can manage the tags.

### Assign virtual machines to plan using VMware tag mappings

To assign virtual machines to a backup plan using mapped tags, do the following:

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the console go to VMware tag mappings on the hypervisor details page
   (click **External resources**, then click **Hypervisors**
   then click on the hypervisor name).
3. Select the checkbox next to multiple mapped tags to assign those tags to
   the same backup plan.
4. Click **Add to resource assignment**.
5. Choose an existing **Backup plan** from the dropdown list.
   Alternatively, you can choose **Create backup plan** to create a new backup plan.
6. Click **Confirm**. This opens the **Assign resources**
   page with **Refine selection using tags** fields with values pre-populated.

### VMware tags using the AWS CLI

AWS Backup uses the API call [`PutHypervisorPropertyMappings`](API_BGW_PutHypervisorPropertyMappings.md "API_BGW_PutHypervisorPropertyMappings.md") to map hypervisor entity properties
in on-premise to properties in AWS.

In the AWS CLI, use the operation `put-hypervisor-property-mappings`:

```
aws backup-gateway put-hypervisor-property-mappings \
--hypervisor-arn arn:aws:backup-gateway:region:account:hypervisor/hypervisorId \
--vmware-to-aws-tag-mappings `list of VMware to AWS tag mappings` \
--iam-role-arn arn:aws:iam::account:role/roleName \
--region `AWSRegion`
--endpoint-url `URL`
```

Here is an example:

```
aws backup-gateway put-hypervisor-property-mappings \
--hypervisor-arn arn:aws:backup-gateway:us-east-1:123456789012:hypervisor/hype-12345 \
--vmware-to-aws-tag-mappings VmwareCategory=OS,VmwareTagName=Windows,AwsTagKey=OS-Windows,AwsTagValue=Windows \
--iam-role-arn arn:aws:iam::123456789012:role/SyncRole \
--region us-east-1
```

You can also use
[`GetHypervisorPropertyMappings`](API_BGW_GetHypervisorPropertyMappings.md "API_BGW_GetHypervisorPropertyMappings.md") to assist with property mappings
information. In the AWS CLI, use the operation `get-hypervisor-property-mappings`.
Here is an example template:

```
aws backup-gateway get-hypervisor-property-mappings --hypervisor-arn `HypervisorARN`
--region `AWSRegion`
```

Here is an example:

```
aws backup-gateway get-hypervisor-property-mappings \
--hypervisor-arn arn:aws:backup-gateway:us-east-1:123456789012:hypervisor/hype-12345 \
--region us-east-1
```

### Sync metadata of virtual machines discovered by the hypervisor in AWS using API, CLI, or SDK

You can sync the metadata of virtual machines. When you do, the VMware tags present
on the virtual machine that are part of the mappings will be synched. Also, AWS
tags mapped to the VMware tags present on the virtual machine will be applied to the
AWS Virtual Machine resource.

AWS Backup uses the API call [`StartVirtualMachinesMetadataSync`](API_BGW_StartVirtualMachinesMetadataSync.md "API_BGW_StartVirtualMachinesMetadataSync.md") to sync the metadata of the virtual
machines discovered by the hypervisor. To sync metadata of virtual machines discovered by the hypervisor using
AWS CLI, use the operation `start-virtual-machines-metadata-sync`.

Example template:

```
aws backup-gateway start-virtual-machines-metadata-sync \
--hypervisor-arn `Hypervisor ARN`
--region `AWSRegion`
```

Example:

```
aws backup-gateway start-virtual-machines-metadata-sync \
--hypervisor-arn arn:aws:backup-gateway:us-east-1:123456789012:hypervisor/hype-12345 \
--region us-east-1
```

You can also use [`GetHypervisor`](API_BGW_GetHypervisor.md "API_BGW_GetHypervisor.md") to assist with hypervisor information, such as host, state, status
of latest metadata sync, and also to retrieve the last successful metadata sync time. In the AWS CLI,
use the operation `get-hypervisor`.

Example template:

```
aws backup-gateway get-hypervisor \
--hypervisor-arn `Hypervisor ARN`
--region `AWSRegion`
```

Example:

```
aws backup-gateway get-hypervisor \
--hypervisor-arn arn:aws:backup-gateway:us-east-1:123456789012:hypervisor/hype-12345 \
--region us-east-1
```

For more information, see API documentation
[VmwareTag](API_BGW_VmwareTag.md "API_BGW_VmwareTag.md")
and [VmwareToAwsTagMapping](API_BGW_VmwareToAwsTagMapping.md "API_BGW_VmwareToAwsTagMapping.md").

This feature will be available on new gateways deployed after December 15, 2022. For existing
gateways, this new capability will be available through an automatic software update on or before
January 30, 2023. To update the gateway to the latest version manually, use
AWS CLI command [UpdateGatewaySoftwareNow](API_BGW_UpdateGatewaySoftwareNow.md "API_BGW_UpdateGatewaySoftwareNow.md").

Example:

```
aws backup-gateway update-gateway-software-now \
--gateway-arn arn:aws:backup-gateway:us-east-1:123456789012:gateway/bgw-12345 \
--region us-east-1
```

## Assigning virtual machines using tags

You can assign your virtual machines currently discovered by AWS Backup, along with other
AWS Backup resources, by assigning them a tag that you have already assigned to one of your
existing backup plans. You can also create a [new backup plan](creating-a-backup-plan.md "creating-a-backup-plan.md")
and a new [tag-based resource
assignment](assigning-resources.md "assigning-resources.md"). Backup plans check for newly-assigned resources each time they run
a backup job.

###### To tag multiple virtual machines with the same tag:

1. In the left navigation pane, choose **Virtual
   machines**.
2. Select the checkbox next to **VM name** to choose all your
   virtual machines. Alternatively, select the checkbox next to the VM names you want
   to tag.
3. Choose **Add tags**.
4. Type in a tag **Key**.
5. Recommended: type in a tag **Value**.
6. Choose **Confirm**.

## Assigning virtual machines using the Assign resources to plan feature

You can assign virtual machines currently discovered by AWS Backup to an existing or new
backup plan using the **Assign resources to plan** feature.

###### To assign virtual machines using the Assign resources to plan feature:

1. In the left navigation pane, choose **Virtual
   machines**.
2. Select the checkbox next to **VM name** to choose all your
   virtual machines. Alternatively, select the checkbox next to multiple VM names to
   assign them to the same backup plan.
3. Choose **Assignments**, then choose **Assign resources
   to plan**.
4. Type in a **Resource assignment name**.
5. Choose a resource assignment **IAM role** to create backups and
   manage recovery points. If you do not have a specific IAM role to use, we recommend
   the **Default role** which has the correct permissions.
6. In the **Backup plan** section, choose an existing
   **Backup plan** from the dropdown list. Alternatively, choose
   **Create backup plan** to create a new backup plan.
7. Choose **Assign resources**.
8. Optional: Verify your virtual machines are assigned to a backup plan by choosing
   **View Backup plan**. Then, in the **Resource
   assignments** section, choose the resource assignment
   **Name**.

## Assigning virtual machines using the Create group assignment feature

Unlike the preceding two resource assignment features for virtual machines, the
**Create group assignment** feature not only assigns virtual machines
currently discovered by AWS Backup, but also virtual machines discovered in the future in a
folder or hypervisor you define.

Also, you do not need to select any checkboxes to use the **Create group
assignment** feature.

###### To assign virtual machines using the Assign resources to plan feature:

1. In the left navigation pane, choose **Virtual
   machines**.
2. Choose **Assignments**, then choose **Create group
   assignment**.
3. Type in a **Resource assignment name**.
4. Choose a resource assignment **IAM role** to create backups and
   manage recovery points. If you do not have a specific IAM role to use, we recommend
   the **Default role** which has the correct permissions.
5. In the **Resource group** section, select the **Group
   type** dropdown menu. Your options are **Folder** or
   **Hypervisor**.
   1. Choose **Folder** to assign all the virtual machines in a
      folder on a hypervisor. Select a folder **Group name**, such as
      `datacenter/vm`, using the dropdown menu. You can also choose to
      include **Subfolders**.

   ###### Note

   To make Folder-based assignments, during the discovery process, AWS Backup tags
   virtual machines with the folder it finds them in during the discovery
   process. If you later move a virtual machine to a different folder, AWS Backup
   cannot update the tag for you due to AWS tagging best practices. This
   assignment method might result in continuing to take backups of virtual
   machines you moved out of your assigned folder. 2. Choose **Hypervisor** to assign all the virtual machines
   managed by a hypervisor. Select a hypervisor ID **Group name**
   using the dropdown menu.

6. In the **Backup plan** section, choose an existing
   **Backup plan** from the dropdown list. Alternatively, choose
   **Create backup plan** to create a new backup plan.
7. Choose **Create group assignment**.
8. Optional: verify your virtual machines are assigned to a backup plan by choosing
   **View Backup plan**. In the **Resource
   assignments** section, choose the resource assignment
   **Name**.

**Next steps**

To restore a virtual machine, see [Restore a virtual machine using AWS Backup](restoring-vm.md "restoring-vm.md").

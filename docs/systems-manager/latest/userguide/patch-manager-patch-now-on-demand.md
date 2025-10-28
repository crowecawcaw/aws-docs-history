# Patching managed nodes on

demand

Using the **Patch now** option in Patch Manager, a tool in AWS Systems Manager,
you can run on-demand patching operations from the Systems Manager console. This means you
don’t have to create a schedule in order to update the compliance status of your
managed nodes or to install patches on noncompliant nodes. You also don’t need to
switch the Systems Manager console between Patch Manager and Maintenance Windows, a tool in AWS Systems Manager, in
order to set up or modify a scheduled patching window.

**Patch now** is especially useful when you must apply zero-day
updates or install other critical patches on your managed nodes as soon as
possible.

###### Note

Patching on demand is supported for a single AWS account-AWS Region pair
at a time. It can't be used with patching operations that are based on
_patch policies_. We recommend using patch policies for
keeping all your managed nodes in compliance. For more information about working
with patch policies, see [Patch policy configurations in Quick Setup](patch-manager-policies.md "patch-manager-policies.md").

###### Topics

- [How 'Patch now' works](#patch-on-demand-how-it-works "#patch-on-demand-how-it-works")
- [Running 'Patch now'](#run-patch-now "#run-patch-now")

## How 'Patch now' works

To run **Patch now**, you specify just two required
settings:

- Whether to scan for missing patches only, or to scan _and_ install patches on your managed
  nodes
- Which managed nodes to run the operation on

When the **Patch now** operation runs, it determines which
patch baseline to use in the same way one is selected for other patching
operations. If a managed node is associated with a patch group, the patch
baseline specified for that group is used. If the managed node isn't associated
with a patch group, the operation uses the patch baseline that is currently set
as the default for the operating system type of the managed node. This can be a
predefined baseline, or the custom baseline you have set as the default. For
more information about patch baseline selection, see [Patch groups](patch-manager-patch-groups.md "patch-manager-patch-groups.md").

Options you can specify for **Patch now** include choosing
when, or whether, to reboot managed nodes after patching, specifying an Amazon Simple Storage Service
(Amazon S3) bucket to store log data for the patching operation, and running Systems Manager
documents (SSM documents) as lifecycle hooks during patching.

### Concurrency and error

thresholds for 'Patch now'

For **Patch now** operations, concurrency and error
threshold options are handled by Patch Manager. You don't need to specify how
many managed nodes to patch at once, nor how many errors are permitted
before the operation fails. Patch Manager applies the concurrency and error
threshold settings described in the following tables when you patch on
demand.

###### Important

The following thresholds apply to `Scan and install`
operations only. For `Scan` operations, Patch Manager attempts to
scan up to 1,000 nodes concurrently, and continue scanning until it has
encountered up to 1,000 errors.

Concurrency: Install operations| Total number of managed nodes in the **Patch
now** operation | Number of managed nodes scanned or patched at a
time |
| --- | --- |
| Fewer than 25 | 1 |
| 25-100 | 5% |
| 101 to 1,000 | 8% |
| More than 1,000 | 10% | Error threshold: Install operations| Total number of managed nodes in the **Patch now** operation | Number of errors permitted before the operation fails |
| --- | --- |
| Fewer than 25 | 1 |
| 25-100 | 5 |
| 101 to 1,000 | 10 |
| More than 1,000 | 10 | ### Using 'Patch now' lifecycle hooks **Patch now** provides you with the ability to run SSM Command documents as lifecycle hooks during an `Install` patching operation. You can use these hooks for tasks such as shutting down applications before patching or running health checks on your applications after patching or after a reboot. For more information about using lifecycle hooks, see [SSM Command document for patching: AWS-RunPatchBaselineWithHooks](patch-manager-aws-runpatchbaselinewithhooks.md "patch-manager-aws-runpatchbaselinewithhooks.md"). The following table lists the lifecycle hooks available for each of the three **Patch now** reboot options, in addition to sample uses for each hook. Lifecycle hooks and sample uses| Reboot option | Hook: Before installation | Hook: After installation | Hook: On exit | Hook: After scheduled reboot |
| --- | --- | --- | --- | --- |
| **Reboot if needed** | Run an SSM document before patching begins. Example use: Safely shut down applications before the patching process begins. | Run an SSM document at the end of the patching operation and before managed node reboot. Example use: Run operations such as installing third-party applications before a potential reboot. | Run an SSM document after the patching operation is complete and instances are rebooted. Example use: Ensure that applications are running as expected after patching. | _Not available_ |
| **Do not reboot my instances** | Same as above. | Run an SSM document at the end of the patching operation. Example use: Ensure that applications are running as expected after patching. | _Not available_ | _Not available_ |
| **Schedule a reboot time** | Same as above. | Same as for **Do not reboot my instances**. | _Not available_ | Run an SSM document immediately after a scheduled reboot is complete. Example use: Ensure that applications are running as expected after the reboot. | ## Running 'Patch now' Use the following procedure to patch your managed nodes on demand. ###### To run 'Patch now' 1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/"). 2. In the navigation pane, choose **Patch Manager**. 3. Choose **Patch now**. 4. For **Patching operation**, choose one of the following: <br>• **Scan**: Patch Manager finds which patches are missing from your managed nodes but doesn't install them. You can view the results in the **Compliance** dashboard or in other tools you use for viewing patch compliance. <br>• **Scan and install**: Patch Manager finds which patches are missing from your managed nodes and installs them. 5. Use this step only if you chose **Scan and install** in the previous step. For **Reboot option**, choose one of the following: <br>• **Reboot if needed**: After installation, Patch Manager reboots managed nodes only if needed to complete a patch installation. <br>• **Don't reboot my instances**: After installation, Patch Manager doesn't reboot managed nodes. You can reboot nodes manually when you choose or manage reboots outside of Patch Manager. <br>• **Schedule a reboot time**: Specify the date, time, and UTC time zone for Patch Manager to reboot your managed nodes. After you run the **Patch now** operation, the scheduled reboot is listed as an association in State Manager with the name `AWS-PatchRebootAssociation`. ###### Important If you cancel the main patching operation after it has started, the `AWS-PatchRebootAssociation` association in State Manager is NOT automatically canceled. To prevent unexpected reboots, you must manually delete `AWS-PatchRebootAssociation` from State Manager if you no longer want the scheduled reboot to occur. Failure to do so may result in unplanned system reboots that could impact production workloads. You can find this association in the Systems Manager console under **State Manager** > **Associations**. 6. For **Instances to patch**, choose one of the following: <br>• **Patch all instances**: Patch Manager runs the specified operation on all managed nodes in your AWS account in the current AWS Region. <br>• **Patch only the target instances I specify**: You specify which managed nodes to target in the next step. 7. Use this step only if you chose **Patch only the target instances I specify** in the previous step. In the **Target selection** section, identify the nodes on which you want to run this operation by specifying tags, selecting nodes manually, or specifying a resource group. ###### Note If a managed node you expect to see isn't listed, see [Troubleshooting managed node availability](fleet-manager-troubleshooting-managed-nodes.md "fleet-manager-troubleshooting-managed-nodes.md") for troubleshooting tips. If you choose to target a resource group, note that resource groups that are based on an AWS CloudFormation stack must still be tagged with the default `aws:cloudformation:`stack-id``tag. If it has been removed, Patch Manager might be unable to determine which managed nodes belong to the resource group. 8. (Optional) For **Patching log storage**, if you want to create and save logs from this patching operation, select the S3 bucket for storing the logs. ###### Note The S3 permissions that grant the ability to write the data to an S3 bucket are those of the instance profile (for EC2 instances) or IAM service role (hybrid-activated machines) assigned to the instance, not those of the IAM user performing this task. For more information, see [Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md") or [Create the IAM service role required for Systems Manager in hybrid and multicloud environments](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md"). In addition, if the specified S3 bucket is in a different AWS account, make sure that the instance profile or IAM service role associated with the managed node has the necessary permissions to write to that bucket. 9. (Optional) If you want to run SSM documents as lifecycle hooks during specific points of the patching operation, do the following: <br>• Choose **Use lifecycle hooks**. <br>• For each available hook, select the SSM document to run at the specified point of the operation: + Before installation + After installation + On exit + After scheduled reboot ###### Note The default document,`AWS-Noop`, runs no operations. 10. Choose **Patch now**. The **Association execution summary** page opens. (Patch now uses associations in State Manager, a tool in AWS Systems Manager, for its operations.) In the **Operation summary** area, you can monitor the status of scanning or patching on the managed nodes you specified.

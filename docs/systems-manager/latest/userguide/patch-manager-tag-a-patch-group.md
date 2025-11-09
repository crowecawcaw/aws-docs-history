AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Creating and managing patch

groups

If you are _not_ using patch policies in your
operations, you can organize your patching efforts by adding managed nodes to patch
groups by using tags.

###### Note

Patch groups are not used in patching operations that are based on
_patch policies_. For information about working with
patch policies, see [Patch policy configurations in Quick Setup](patch-manager-policies.md "patch-manager-policies.md").

Patch group functionality is not supported in the console for account-Region
pairs that did not already use patch groups before patch policy support was
released on December 22, 2022. Patch group functionality is still available in
account-Region pairs that began using patch groups before this date.

To use tags in patching operations, you must apply the tag key `Patch
 Group` or `PatchGroup` to your managed nodes. You must also
specify the name that you want to give the patch group as the value of the tag. You
can specify any tag value, but the tag key must be `Patch Group` or
`PatchGroup`.

`PatchGroup` (without a space) is required if you have [allowed tags in EC2 instance metadata](../../../AWSEC2/latest/UserGuide/Using_Tags.md#allow-access-to-tags-in-IMDS "../../../AWSEC2/latest/UserGuide/Using_Tags.md#allow-access-to-tags-in-IMDS").

After you group your managed nodes using tags, you add the patch group value to a
patch baseline. By registering the patch group with a patch baseline, you ensure
that the correct patches are installed during the patching operation. For more
information about patch groups, see [Patch groups](patch-manager-patch-groups.md "patch-manager-patch-groups.md").

Complete the tasks in this topic to prepare your managed nodes for patching using
tags with your nodes and patch baseline. Task 1 is required only if you are patching
Amazon EC2 instances. Task 2 is required only if you are patching non-EC2 instances in a
[hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment. Task 3 is required for all managed nodes.

###### Tip

You can also add tags to managed nodes using the AWS CLI command
`add-tags-to-resource` or the Systems Manager API operation
ssm-agent-minimum-s3-permissions-required`AddTagsToResource`.

###### Tasks

- [Task 1: Add EC2 instances to a
  patch group using tags](#sysman-patch-group-tagging-ec2 "#sysman-patch-group-tagging-ec2")
- [Task 2: Add managed nodes
  to a patch group using tags](#sysman-patch-group-tagging-managed "#sysman-patch-group-tagging-managed")
- [Task 3: Add a patch group to
  a patch baseline](#sysman-patch-group-patchbaseline "#sysman-patch-group-patchbaseline")

## Task 1: Add EC2 instances to a

patch group using tags

You can add tags to EC2 instances using the Systems Manager console or the Amazon EC2
console. This task is required only if you are patching Amazon EC2 instances.

###### Important

You can't apply the `Patch Group` tag (with a space) to an
Amazon EC2 instance if the **Allow tags in instance metadata**
option is enabled on the instance. Allowing tags in instance metadata
prevents tag key names from containing spaces. If you have [allowed tags in EC2 instance metadata](../../../AWSEC2/latest/UserGuide/Using_Tags.md#allow-access-to-tags-in-IMDS "../../../AWSEC2/latest/UserGuide/Using_Tags.md#allow-access-to-tags-in-IMDS"), you must use the tag key
`PatchGroup` (without a space).

###### Option 1: To add EC2 instances to a patch group (Systems Manager console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. In the **Managed nodes** list, choose the ID of a
   managed EC2 instance that you want to configure for patching. Node IDs
   for EC2 instances begin with `i-`.

###### Note

When using the Amazon EC2 console and AWS CLI, it's possible to apply
`Key = Patch Group` or `Key = PatchGroup`
tags to instances that aren't yet configured for use with
Systems Manager.

If a managed node you expect to see isn't listed, see [Troubleshooting managed
node availability](fleet-manager-troubleshooting-managed-nodes.md "fleet-manager-troubleshooting-managed-nodes.md") for troubleshooting
tips. 4. Choose the **Tags** tab, then choose
**Edit**. 5. In the left column, enter `Patch Group` or
`PatchGroup`. If you have [allowed tags in EC2 instance metadata](../../../AWSEC2/latest/UserGuide/Using_Tags.md#allow-access-to-tags-in-IMDS "../../../AWSEC2/latest/UserGuide/Using_Tags.md#allow-access-to-tags-in-IMDS"), you must use
`PatchGroup` (without a space). 6. In the right column, enter a tag value to serve as the name for the
patch group. 7. Choose **Save**. 8. Repeat this procedure to add other EC2 instances to the same patch
group.

###### Option 2: To add EC2 instances to a patch group (Amazon EC2 console)

1. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/"),
   and then choose **Instances** in the navigation pane.
2. In the list of instances, choose an instance that you want to
   configure for patching.
3. In the **Actions** menu, choose **Instance
   settings**, **Manage tags**.
4. Choose **Add new tag**.
5. For **Key**, enter `Patch Group`
   or `PatchGroup`. If you have [allowed tags in EC2 instance metadata](../../../AWSEC2/latest/UserGuide/Using_Tags.md#allow-access-to-tags-in-IMDS "../../../AWSEC2/latest/UserGuide/Using_Tags.md#allow-access-to-tags-in-IMDS"), you must use
   `PatchGroup` (without a space).
6. For **Value**, enter a value to serve as the name for
   the patch group.
7. Choose **Save**.
8. Repeat this procedure to add other instances to the same patch
   group.

## Task 2: Add managed nodes

to a patch group using tags

Follow the steps in this topic to add tags to AWS IoT Greengrass core devices and
non-EC2 hybrid-activated managed nodes (mi-\*). This task is required only if you
are patching non-EC2 instances in a hybrid and multicloud environment.

###### Note

You can't add tags for non-EC2 managed nodes using the Amazon EC2
console.

###### To add non-EC2 managed nodes to a patch group (Systems Manager console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. In the **Managed nodes** list, choose the name of the
   managed node that you want to configure for patching.

###### Note

If a managed node you expect to see isn't listed, see [Troubleshooting managed
node availability](fleet-manager-troubleshooting-managed-nodes.md "fleet-manager-troubleshooting-managed-nodes.md") for troubleshooting
tips. 4. Choose the **Tags** tab, then choose
**Edit**. 5. In the left column, enter `Patch Group` or
`PatchGroup`. If you have [allowed tags in EC2 instance metadata](../../../AWSEC2/latest/UserGuide/Using_Tags.md#allow-access-to-tags-in-IMDS "../../../AWSEC2/latest/UserGuide/Using_Tags.md#allow-access-to-tags-in-IMDS"), you must use
`PatchGroup` (without a space). 6. In the right column, enter a tag value to serve as the name for the
patch group. 7. Choose **Save**. 8. Repeat this procedure to add other managed nodes to the same patch
group.

## Task 3: Add a patch group to

a patch baseline

To associate a specific patch baseline with your managed nodes, you must add
the patch group value to the patch baseline. By registering the patch group with
a patch baseline, you can ensure that the correct patches are installed during a
patching operation. This task is required whether you are patching EC2
instances, non-EC2 managed nodes, or both.

For more information about patch groups, see [Patch groups](patch-manager-patch-groups.md "patch-manager-patch-groups.md").

###### Note

The steps you follow depend on whether you first accessed Patch Manager before
or after the [patch policies](patch-manager-policies.md "patch-manager-policies.md")
release on December 22, 2022.

###### To add a patch group to a patch baseline (Systems Manager console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Patch Manager**.
3. If you're accessing Patch Manager for the first time in the current
   AWS Region and the Patch Manager start page opens, choose **Start
   with an overview**.
4. Choose the **Patch baselines** tab, and then in the
   **Patch baselines** list, choose the name of the
   patch baseline that you want to configure for your patch group.

If you didn't first access Patch Manager until after the patch policies
release, you must choose a custom baseline that you have created. 5. If the **Baseline ID** details page includes an
**Actions** menu, do the following:

    * Choose **Actions**, then **Modify
     patch groups**.
    * Enter the tag *value* you
     added to your managed nodes in [Task 2: Add managed nodes
     to a patch group using tags](#sysman-patch-group-tagging-managed "#sysman-patch-group-tagging-managed"), then
     choose **Add**.

If the **Baseline ID** details page does _not_ include an **Actions**
menu, patch groups can't be configured in the console. Instead, you can
do either of the following:

    * (Recommended) Set up a patch policy in Quick Setup, a tool in
     AWS Systems Manager, to map a patch baseline to one or more EC2
     instances.


    For more information, see [Using Quick Setup patch policies](patch-manager-policies.md "patch-manager-policies.md") and [Automate organization-wide patching using a Quick Setup patch
     policy](quick-setup-patch-manager.md "quick-setup-patch-manager.md").
    * Use the [register-patch-baseline-for-patch-group](../../../cli/latest/reference/ssm/register-patch-baseline-for-patch-group.md "../../../cli/latest/reference/ssm/register-patch-baseline-for-patch-group.md")
     command in the AWS Command Line Interface (AWS CLI) to configure a patch
     group.

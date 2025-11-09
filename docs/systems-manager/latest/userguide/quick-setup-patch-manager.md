AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Configure patching for instances in an

organization using a Quick Setup patch policy

With Quick Setup, a tool in AWS Systems Manager, you can create patch policies powered by
Patch Manager. A patch policy defines the schedule and baseline to use when automatically
patching your Amazon Elastic Compute Cloud (Amazon EC2) instances and other managed nodes. Using a single
patch policy configuration, you can define patching for all accounts in multiple
AWS Regions in your organization, for only the accounts and Regions you choose, or
for a single account-Region pair. For more information about patch policies, see
[Patch policy configurations in Quick Setup](patch-manager-policies.md "patch-manager-policies.md").

###### Prerequisite

To define a patch policy for a node using Quick Setup, the node must be a
_managed node_. For more information about
managing your nodes, see [Setting up Systems Manager unified console
for an organization](systems-manager-setting-up-organizations.md "systems-manager-setting-up-organizations.md").

###### Important

**Patch compliance scanning methods** –
Systems Manager supports several methods for scanning managed nodes for patch compliance.
If you implement more than one of these methods at a time, the patch compliance
information you see is always the result of the most recent scan. Results from
previous scans are overwritten. If the scanning methods use different patch
baselines, with different approval rules, the patch compliance information can
change unexpectedly. For more information, see [Identifying the
execution that created patch compliance data](patch-manager-compliance-data-overwrites.md "patch-manager-compliance-data-overwrites.md").

**Association compliance status and patch
policies** – The patching status for a managed node that's
under a Quick Setup patch policy matches the status of the State Manager association
execution for that node. If the association execution status is
`Compliant`, the patching status for the managed node is also
marked `Compliant`. If the association execution status is
`Non-Compliant`, the patching status for the managed node is also
marked `Non-Compliant`.

## Supported Regions for patch

policy configurations

Patch policy configurations in Quick Setup are currently supported in the
following Regions:

- US East (Ohio) (us-east-2)
- US East (N. Virginia) (us-east-1)
- US West (N. California) (us-west-1)
- US West (Oregon) (us-west-2)
- Asia Pacific (Mumbai) (ap-south-1)
- Asia Pacific (Seoul) (ap-northeast-2)
- Asia Pacific (Singapore) (ap-southeast-1)
- Asia Pacific (Sydney) (ap-southeast-2)
- Asia Pacific (Tokyo) (ap-northeast-1)
- Canada (Central) (ca-central-1)
- Europe (Frankfurt) (eu-central-1)
- Europe (Ireland) (eu-west-1)
- Europe (London) (eu-west-2)
- Europe (Paris) (eu-west-3)
- Europe (Stockholm) (eu-north-1)
- South America (São Paulo) (sa-east-1)

## Permissions for the patch

policy S3 bucket

When you create a patch policy, Quick Setup creates an Amazon S3 bucket that contains
a file named `baseline_overrides.json`. This file stores
information about the patch baselines that you specified for your patch
policy.

The S3 bucket is named in the format
`aws-quicksetup-patchpolicy-`account-id`-`quick-setup-configuration-id``.

For example:
`aws-quicksetup-patchpolicy-123456789012-abcde`

If you're creating a patch policy for an organization, the bucket is created
in your organization's management account.

There are two use cases when you must provide other AWS resources with
permission to access this S3 bucket using AWS Identity and Access Management (IAM) policies:

- [Case 1: Use
  your own instance profile or service role with your managed nodes
  instead of one provided by Quick Setup](#patch-policy-instance-profile-service-role "#patch-policy-instance-profile-service-role")
- [Case 2: Use VPC endpoints to connect to
  Systems Manager](#patch-policy-vpc "#patch-policy-vpc")

The permissions policy you need in either case is located in the section
below, [Policy permissions for
Quick Setup S3 buckets](#patch-policy-bucket-permissions "#patch-policy-bucket-permissions").

### Case 1: Use

your own instance profile or service role with your managed nodes
instead of one provided by Quick Setup

Patch policy configurations include an option to **Add required
IAM policies to existing instance profiles attached to your
instances**.

If you don't choose this option but want Quick Setup to patch your managed
nodes using this patch policy, you must ensure that the following are
implemented:

- The IAM managed policy `AmazonSSMManagedInstanceCore`
  must be attached to the [IAM instance profile](setup-instance-permissions.md "setup-instance-permissions.md") or [IAM service
  role](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md") that's used to provide Systems Manager permissions to your
  managed nodes.
- You must add permissions to access your patch policy bucket as an
  inline policy to the IAM instance profile or IAM service role.
  You can provide wildcard access to all
  `aws-quicksetup-patchpolicy` buckets or only
  the specific bucket created for your organization or account, as
  shown in the earlier code samples.
- You must tag your IAM instance profile or IAM service role
  with the following key-value pair.

`Key:
 QSConfigId-`quick-setup-configuration-id`,
 Value:
 `quick-setup-configuration-id``

`quick-setup-configuration-id` represents
the value of the parameter applied to the AWS CloudFormation stack that is
used in creating your patch policy configuration. To retrieve this
ID, do the following:

    1. Open the AWS CloudFormation console at
     [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
    2. Select the name of the stack that is used to create your
     patch policy. The name is in a format such as
     `StackSet-AWS-QuickSetup-PatchPolicy-LA-q4bkg-52cd2f06-d0f9-499e-9818-d887cEXAMPLE`.
    3. Choose the **Parameters** tab.
    4. In the **Parameters** list, in the
     **Key** column, locate the key
     **QSConfigurationId**. In the
     **Value** column for its row, locate
     the configuration ID, such as `abcde`.


    In this example, for the tag to apply to your instance
     profile or service role, the key is
     `QSConfigId-abcde`, and the value is
     `abcde`.

For information about adding tags to an IAM role, see [Tagging IAM roles](../../../IAM/latest/UserGuide/id_tags_roles.md#id_tags_roles_procs-console "../../../IAM/latest/UserGuide/id_tags_roles.md#id_tags_roles_procs-console") and [Managing tags on instance profiles (AWS CLI or AWS API)](../../../IAM/latest/UserGuide/id_tags_instance-profiles.md#id_tags_instance-profile_procs-cli-api "../../../IAM/latest/UserGuide/id_tags_instance-profiles.md#id_tags_instance-profile_procs-cli-api") in the
_IAM User Guide_.

### Case 2: Use VPC endpoints to connect to

Systems Manager

If you use VPC endpoints to connect to Systems Manager, your VPC endpoint policy for
S3 must allow access to your Quick Setup patch policy S3 bucket.

For information about adding permissions to a VPC endpoint policy for S3,
see [Controlling access from VPC endpoints with bucket policies](../../../AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.md "../../../AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.md") in
the _Amazon S3 User Guide_.

### Policy permissions for

Quick Setup S3 buckets

You can provide wildcard access to all
`aws-quicksetup-patchpolicy` buckets or only the
specific bucket created for your organization or account. To provide the
necessary permissions for the two cases described below, use either
format.

All patch policy buckets
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AccessToAllPatchPolicyRelatedBuckets",
 "Effect": "Allow",
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::aws-quicksetup-patchpolicy-*"
 }
 ]
}`

```

Specific patch policy bucket
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AccessToMyPatchPolicyRelatedBucket",
 "Effect": "Allow",
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::aws-quicksetup-patchpolicy-`111122223333`-`quick-setup-configuration-id`"
 }
 ]
}`

```

###### Note

After the patch policy configuration is created, you can
locate the full name of your bucket in the S3 console. For
example:
`aws-quicksetup-patchpolicy-123456789012-abcde`

## Random patch baseline IDs in

patch policy operations

Patching operations for patch policies utilize the
`BaselineOverride` parameter in the
`AWS-RunPatchBaseline` SSM Command document.

When you use `AWS-RunPatchBaseline` for patching
_outside_ of a patch policy, you can use
`BaselineOverride` to specify a list of patch baselines to use
during the operation that are different from the specified defaults. You create
this list in a file named `baseline_overrides.json` and
manually add it to an Amazon S3 bucket that you own, as explained in [Using the
BaselineOverride parameter](patch-manager-baselineoverride-parameter.md "patch-manager-baselineoverride-parameter.md").

For patching operations based on patch policies, however, Systems Manager automatically
creates an S3 bucket and adds a `baseline_overrides.json`
file to it. Then, every time Quick Setup runs a patching operation (using the
Run Command tool, the system generates a random ID for each patch baseline. This ID
is different for every patch policy patching operation, and the patch baseline
it represents is not stored or accessible to you in your account.

As a result, you will not see the ID of the patch baseline selected in your
configuration in patching logs. This applies to both AWS managed patch
baselines and custom patch baselines you might have selected. The baseline ID
reported in the log is instead that one that was generated for that specific
patching operation.

In addition, if you attempt to view details in Patch Manager about a patch baseline
that was generated with a random ID, the system reports that the patch baseline
doesn't exist. This is expected behavior and can be ignored.

## Creating a patch policy

To create a patch policy, perform the following tasks in the Systems Manager
console.

###### To create a patch policy with Quick Setup

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").

If you are setting up patching for an organization, make sure you are
signed in to the management account for the organization. You can't set
up the policy using the delegated administrator account or a member account. 2. In the navigation pane, choose **Quick Setup**. 3. On the **Patch Manager** card, choose
**Create**.

###### Tip

If you already have one or more configurations in your account,
first choose the **Library** tab or the
**Create** button in the
**Configurations** section to view the
cards. 4. For **Configuration name**, enter a name to help
identify the patch policy. 5. In the **Scanning and installation** section, under
**Patch operation**, choose whether the patch
policy will **Scan** the specified targets or
**Scan and install** patches on the specified
targets. 6. Under **Scanning schedule**, choose **Use
recommended defaults** or **Custom scan
schedule**. The default scan schedule will scan your
targets daily at 1:00 AM UTC.

    * If you choose **Custom scan schedule**,
     select the **Scanning frequency**.
    * If you choose **Daily**, enter the time, in
     UTC, that you want to scan your targets.
    * If you choose **Custom CRON Expression**,
     enter the schedule as a **CRON expression**.
     For more information about formatting CRON expressions for
     Systems Manager, see [Reference: Cron and rate expressions
     for Systems Manager](reference-cron-and-rate-expressions.md "reference-cron-and-rate-expressions.md").


    Also, select **Wait to scan targets until first CRON
     interval**. By default, Patch Manager immediately scans
     nodes as they become targets.

7. If you chose **Scan and install**, choose the
   **Installation schedule** to use when installing
   patches to the specified targets. If you choose **Use
   recommended defaults**, Patch Manager will install weekly
   patches at 2:00 AM UTC on Sunday.
   - If you choose **Custom install schedule**,
     select the **Installation Frequency**.
   - If you choose **Daily**, enter the time, in
     UTC, that you want to install updates on your targets.
   - If you choose **Custom CRON expression**,
     enter the schedule as a **CRON expression**.
     For more information about formatting CRON expressions for
     Systems Manager, see [Reference: Cron and rate expressions
     for Systems Manager](reference-cron-and-rate-expressions.md "reference-cron-and-rate-expressions.md").

   Also, clear **Wait to install updates until first CRON
   interval** to immediately install updates on nodes
   as they become targets. By default, Patch Manager waits until the
   first CRON interval to install updates.
   - Choose **Reboot if needed** to reboot the
     nodes after patch installation. Rebooting after installation is
     recommended but can cause availability issues.

8. In the **Patch baseline** section, choose the patch
   baselines to use when scanning and updating your targets.

By default, Patch Manager uses the predefined patch baselines. For more
information, see [Predefined
baselines](patch-manager-predefined-and-custom-patch-baselines.md#patch-manager-baselines-pre-defined "patch-manager-predefined-and-custom-patch-baselines.md#patch-manager-baselines-pre-defined").

If you choose **Custom patch baseline**, change the
selected patch baseline for operating systems that you don't want to use
a predefined AWS patch baseline.

###### Note

If you use VPC endpoints to connect to Systems Manager, make sure
your VPC endpoint policy for S3 allows access to this S3 bucket. For
more information, see [Permissions for the patch
policy S3 bucket](#patch-policy-s3-bucket-permissions "#patch-policy-s3-bucket-permissions").

###### Important

If you are using a [patch policy
configuration](patch-manager-policies.md "patch-manager-policies.md") in Quick Setup, updates you make to custom patch baselines are
synchronized with Quick Setup once an hour.

If a custom patch baseline that was referenced in a patch policy is deleted, a banner
displays on the Quick Setup **Configuration details** page for your patch
policy. The banner informs you that the patch policy references a patch baseline that no
longer exists, and that subsequent patching operations will fail. In this case, return to
the Quick Setup **Configurations** page, select the Patch Manager configuration ,
and choose **Actions**, **Edit configuration**. The
deleted patch baseline name is highlighted, and you must select a new patch baseline for the
affected operating system. 9. (Optional) In the **Patching log storage** section,
select **Write output to S3 bucket** to store patching
operation logs in an Amazon S3 bucket.

###### Note

If you are setting up a patch policy for an organization, the
management account for your organization must have at least read-only
permissions for this bucket. All organization units included in the
policy must have write-access to the bucket. For information about
granting bucket access to different accounts, see [Example 2: Bucket owner granting cross-account bucket
permissions](../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md "../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md") in the
_Amazon Simple Storage Service User Guide_. 10. Choose **Browse S3** to select the bucket that you
want to store patch log output in. The management account must have read
access to this bucket. All non-management accounts and targets
configured in the **Targets** section must have write
access to the provided S3 bucket for logging. 11. In the **Targets** section, choose one of the
following to identify the accounts and Regions for this patch policy
operation.

###### Note

If you are working in a single account, options for working with
organizations and organizational units (OUs) are not available. You
can choose whether to apply this configuration to all AWS Regions
in your account or only the Regions you select.

If you previously specified a Home Region for you account and
haven't onboarded to the new Quick Setup console experience, you can't
exclude that Region from the **Targets**
configuration.

    * **Entire organization** – All accounts
     and Regions in your organization.
    * **Custom** – Only the OUs and Regions
     that you specify.




    	+ In the **Target OUs** section, select
    	 the OUs where you want to set up the patch policy.
    	+ In the **Target Regions** section,
    	 select the Regions where you want to apply the patch
    	 policy.
    * **Current account** – Only the Regions
     you specify in the account you are currently signed into are
     targeted. Choose one of the following:




    	+ **Current Region** – Only
    	 managed nodes in the Region selected in the console are
    	 targeted.
    	+ **Choose Regions** – Choose
    	 the individual Regions to apply the patch policy
    	 to.

12. For **Choose how you want to target instances**,
    choose one of the following to identify the nodes to patch:
    - **All managed nodes** – All managed
      nodes in the selected OUs and Regions.
    - **Specify the resource group** –
      Choose the name of a resource group from the list to target its
      associated resources.

    ###### Note

    Currently, selecting resource groups is supported only for
    single account configurations. To patch resources in
    multiple accounts, choose a different targeting
    option.
    - **Specify a node tag** – Only nodes
      tagged with the key-value pair that you specify are patched in
      all accounts and Regions you have targeted.
    - **Manual** – Choose managed nodes from
      all specified accounts and Regions manually from a list.

    ###### Note

    This option currently supports only Amazon EC2 instances. You
    can add a maximum of 25 instances manually in a patch policy
    configuration.

13. In the **Rate control** section, do the
    following:
    - For **Concurrency**, enter a number or
      percentage of nodes to run the patch policy on at the same
      time.
    - For **Error threshold**, enter the number or
      percentage of nodes that can experience an error before the
      patch policy fails.

14. (Optional) Select the **Add required IAM policies to
    existing instance profiles attached to your instances**
    check box.

This selection applies the IAM policies created by this Quick Setup
configuration to nodes that already have an instance profile attached
(EC2 instances) or a service role attached (hybrid-activated nodes). We
recommend this selection when your managed nodes already have an
instance profile or service role attached, but it doesn't contain all
the permissions required for working with Systems Manager.

Your selection here is applied to managed nodes created later in the
accounts and Regions that this patch policy configuration applies
to.

###### Important

If you don't select this check box but want Quick Setup to patch your
managed nodes using this patch policy, you must do the
following:

Add permissions to your [IAM instance profile](setup-instance-permissions.md "setup-instance-permissions.md") or [IAM service
role](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md") to access the S3 bucket created for your patch
policy

Tag your IAM instance profile or IAM service role with a
specific key-value pair.

For information, see [Case 1: Use
your own instance profile or service role with your managed nodes
instead of one provided by Quick Setup](#patch-policy-instance-profile-service-role "#patch-policy-instance-profile-service-role"). 15. Choose **Create**.

To review patching status after the patch policy is created, you can
access the configuration from the [Quick Setup](https://console.aws.amazon.com/systems-manager/quick-setup "https://console.aws.amazon.com/systems-manager/quick-setup") page.

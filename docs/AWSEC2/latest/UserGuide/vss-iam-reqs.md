

# Use an IAM managed policy to grant permissions for VSS based snapshots
<a name="vss-iam-reqs"></a>

The AWSEC2VssSnapshotPolicy managed policy enables Systems Manager to perform the following actions on your Windows instance:
+ Create and tag EBS snapshots
+ Create and tag Amazon Machine Images (AMIs)
+ Attach metadata, such as the device ID, to the default snapshot tags that VSS creates.

This topic covers permission details for the VSS managed policy, and how to attach it to your EC2 instance profile IAM role.

**Topics**
+ [AWSEC2VssSnapshotPolicy managed policy details](#vss-iam-manpol-AWSEC2VssSnapshotPolicy)
+ [Attach the VSS snapshot managed policy to your instance profile role](#vss-snapshots-attach-policy)

## AWSEC2VssSnapshotPolicy managed policy details
<a name="vss-iam-manpol-AWSEC2VssSnapshotPolicy"></a>

An AWS managed policy is a standalone policy that Amazon provides for AWS customers. AWS managed policies are designed to grant permissions for common use cases. You can't change the permissions that are defined in AWS managed policies. However, you can copy the policy and use it as a baseline for a [customer managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that is specific to your use case.

 For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

To use the **AWSEC2VssSnapshotPolicy** managed policy, you can attach it to the IAM role that's attached to your EC2 Windows Instances. This policy enables the EC2 VSS solution to create and add tags to Amazon Machine Images (AMIs) and EBS Snapshots. To attach the policy, see [Attach the VSS snapshot managed policy to your instance profile role](#vss-snapshots-attach-policy).

### Permissions granted by AWSEC2VssSnapshotPolicy
<a name="vss-iam-manpol-AWSEC2VssSnapshotPolicy-details"></a>

The **AWSEC2VssSnapshotPolicy** policy includes the following Amazon EC2 permissions to allow Amazon EC2 to create and manage VSS snapshots on your behalf. You can attach this managed policy to the IAM instance profile role that you use for your EC2 Windows instances.
+ **ec2:CreateTags** – Add tags to EBS snapshots and AMIs to help identify and categorize the resources.
+ **ec2:DescribeInstanceAttribute** – Retrieve the EBS volumes and corresponding block device mappings that are attached to the target instance.
+ **ec2:CreateSnapshots** – Create snapshots of EBS volumes.
+ **ec2:CreateImage** – Create an AMI from a running EC2 instance.
+ **ec2:DescribeImages** – Retrieve the information for EC2 AMIs and snapshots.
+ **ec2:DescribeSnapshots** – Determine the create time and status of snapshots to verify application consistency.

**Note**  
To view permission details for this policy, see [AWSEC2VssSnapshotPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSEC2VssSnapshotPolicy.html) in the *AWS Managed Policy Reference*.

### Streamline permissions for specific use cases - advanced
<a name="scope-down-perms"></a>

The `AWSEC2VssSnapshotPolicy` managed policy includes permissions for all of the ways that you can create VSS based snapshots. You can create a custom policy that includes only the permissions that you need.

**Use case: Create AMI, Use case: Use AWS Backup service**

If you exclusively use the `CreateAmi` option, or if you create VSS based snapshots only through the AWS Backup service, then you can streamline the policy statements as follows.
+ Omit policy statements identified by the following statement IDs (SIDs):
  + `CreateSnapshotsWithTag`
  + `CreateSnapshotsAccessInstance`
  + `CreateSnapshotsAccessVolume`
+ Adjust the `CreateTagsOnResourceCreation` statement as follows:
  + Remove `arn:aws:ec2:*:*:snapshot/*` from the resources.
  + Remove `CreateSnapshots` from the `ec2:CreateAction` condition.
+ Adjust the `CreateTagsAfterResourceCreation` statement to remove `arn:aws:ec2:*:*:snapshot/*` from the resources.
+ Adjust the `DescribeImagesAndSnapshots` statement to remove `ec2:DescribeSnapshots` from the statement action.

**Use case: Snapshot only**

If you don't use the `CreateAmi` option, then you can streamline the policy statements as follows.
+ Omit policy statements identified by the following statement IDs (SIDs):
  + `CreateImageAccessInstance`
  + `CreateImageWithTag`
+ Adjust the `CreateTagsOnResourceCreation` statement as follows:
  + Remove `arn:aws:ec2:*:*:image/*` from the resources.
  + Remove `CreateImage` from the `ec2:CreateAction` condition.
+ Adjust the `CreateTagsAfterResourceCreation` statement to remove `arn:aws:ec2:*:*:image/*` from the resources.
+ Adjust the `DescribeImagesAndSnapshots` statement to remove `ec2:DescribeImages` from the statement action.

**Note**  
To ensure that your customized policy performs as expected, we recommend that you regularly review and incorporate updates to the managed policy.

## Attach the VSS snapshot managed policy to your instance profile role
<a name="vss-snapshots-attach-policy"></a>

To grant permissions for VSS based snapshots for your EC2 Windows instance, you can attach the **AWSEC2VssSnapshotPolicy** managed policy to your instance profile role as follows. It's important to ensure that your instance meets all [System requirements](application-consistent-snapshots-prereqs.md#vss-sys-reqs).

**Note**  
To use the managed policy, your instance must have the `AwsVssComponents` package version `2.3.1` or later installed. For version history, see [AwsVssComponents package versions](vss-comps-history.md#AwsVssComponents-history).

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles** to see a list of IAM roles that you have access to.

1. Select the **Role name** link for the role that's attached to your instance. This opens the role detail page.

1. To attach the managed policy, choose **Add permissions**, located in the upper right corner of the list panel. Then select **Attach policies** from the dropdown list.

1. To streamline results, enter the policy name in the search bar (`AWSEC2VssSnapshotPolicy`).

1. Select the checkbox next to the name of the policy to attach, and choose **Add permissions**.
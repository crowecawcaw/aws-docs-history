# Troubleshoot Amazon Data Lifecycle Manager issues

The following documentation can help you troubleshoot problems that you might encounter.

###### Topics

- [Error: Role with name already exists](#dlm-role-arn-issue "#dlm-role-arn-issue")

## Error: `Role with name already exists`

###### Description

You get the `Role with name AWSDataLifecycleManagerDefaultRole already exists` or
`Role with name AWSDataLifecycleManagerDefaultRoleForAMIManagement already exists` error
when you try to create a policy using the console.

###### Cause

The ARN format of the default role differs depending on whether it was created using the
console or the AWS CLI. While the ARNs are different, the roles use the same role name, which
results in a role naming conflict between the console and the AWS CLI.

###### Solution

To resolve this issue, do the following:

1. (_For snapshot policies enabled for pre and post scripts only_) Manually
   attach the **AWSDataLifecycleManagerSSMFullAccess** AWS managed policy to
   the **AWSDataLifecycleManagerDefaultRole** IAM role. For more information, see
   [Adding IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console").
2. When creating your Amazon Data Lifecycle Manager policy, for **IAM role**, select **Choose
   another role**, and then select either **AWSDataLifecycleManagerDefaultRole**
   (for a snapshot policy), or **AWSDataLifecycleManagerDefaultRoleForAMIManagement**
   (for an AMI policy).
3. Continue to create the policy as usual.

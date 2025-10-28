# Using identity-based

policies

By default, IAM users and roles don't have permission to create or modify AWS Elastic Disaster Recovery resources.
They also can't perform tasks using the AWS
Management Console, AWS CLI, or AWS API. An IAM administrator must create IAM
policies that grant users and roles permission to perform specific API
operations on the specified resources they need. The administrator must then
attach those policies to the users or groups that require those permissions. To
learn how to attach policies to a user or group, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the IAM User Guide.
To learn how to create an IAM identity-based policy using example JSON policy
documents, see [Creating policies on the JSON tab in the IAM User Guide.](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor")

###### Topics

- [Customer-managed policies in AWS Elastic Disaster Recovery](customer_managed_policies_drs.md "customer_managed_policies_drs.md")
- [Console Full Access Policy -
  AWSElasticDisasterRecoveryConsoleFullAccess](customer_managed_policies_drs_full_access.md "customer_managed_policies_drs_full_access.md")
- [Console Full Access Policy -
  AWSElasticDisasterRecoveryConsoleFullAccess_v2](customer_managed_policies_drs_full_access_v2.md "customer_managed_policies_drs_full_access_v2.md")
- [Launch Actions Policy -
  AWSElasticDisasterRecoveryLaunchActionsPolicy](customer_managed_policies_launch_actions.md "customer_managed_policies_launch_actions.md")
- [Console Read-Only Access Policy

* AWSElasticDisasterRecoveryReadOnlyAccess](customer_managed_policies_drs_readonly.md "customer_managed_policies_drs_readonly.md")

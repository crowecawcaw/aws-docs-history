# Minimum IAM policies

This document describes the minimum IAM policies needed to run the main use cases of eksctl. These are the ones used to
run the integration tests.

###### Note

Remember to replace `<account_id>` with your own.

###### Note

An AWS Managed Policy is created and administered by AWS. You cannot change the permissions defined in AWS managed policies.

**AmazonEC2FullAccess (AWS Managed Policy)**

[View AmazonEC2FullAccess policy definition.](../../../aws-managed-policy/latest/reference/AmazonEC2FullAccess.md "../../../aws-managed-policy/latest/reference/AmazonEC2FullAccess.md")

**AWSCloudFormationFullAccess (AWS Managed Policy)**

[View AWSCloudFormationFullAccess policy definition.](../../../aws-managed-policy/latest/reference/AWSCloudFormationFullAccess.md "../../../aws-managed-policy/latest/reference/AWSCloudFormationFullAccess.md")

**EksAllAccess**

```
# Error: No files found with UUID: 27ad3ff9-60be-4128-8b83-f8833a6e39aa
```

**IamLimitedAccess**

```
# Error: No files found with UUID: 5500eeb9-bf3d-498d-999b-7f8036e705a5
```

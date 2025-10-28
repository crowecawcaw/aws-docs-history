# Troubleshoot customer managed keys in AWS IAM Identity Center

This topic describes common customer managed key related errors you might encounter when using AWS IAM Identity Center and provides troubleshooting steps to resolve them.

## Access Denied: KMS Decrypt Permission Issue

**Error:** "User xxxxxxx is not authorized to perform: kms:Decrypt on the resource associated with this ciphertext because no identity-based policy allows the kms:Decrypt action"

The user or IAM principal lacks the required `kms:Decrypt` permission in either their IAM policy or KMS key policy.

**Troubleshooting with AWS CloudTrail:**

1. Look for `kms.amazonaws.com` events in CloudTrail
2. Search for event name `Decrypt`
3. Review the `errorCode` and `errorMessage` fields
4. Check `userIdentity` to confirm which principal attempted the operation

To resolve this issue, grant the user or IAM principal `kms:Decrypt` access permissions in their IAM policy and KMS key policy. For more information, see [Implementing customer managed KMS keys in AWS IAM Identity Center](identity-center-customer-managed-keys.md "identity-center-customer-managed-keys.md").

## AWS managed application login failures with a customer managed KMS key enabled in IAM Identity Center

If no Identity Center users can log into AWS managed applications and you have a customer managed KMS key enabled in your IAM Identity Center instance, verify that the KMS key policy grants the AWS managed applications permissions to use the customer managed KMS key. For more information, see [Baseline KMS key and IAM policy statements](baseline-KMS-key-policy.md "baseline-KMS-key-policy.md").

## AWS managed application installation and/or user assignment failures with a customer managed KMS key enabled in IAM Identity Center

**Error:** "User xxxxxxx is not authorized to perform: kms:Decrypt on the resource associated with this ciphertext because no identity-based policy allows the kms:Decrypt action"

The user or IAM principal lacks the required `kms:Decrypt` permission in either their IAM policy or KMS key policy.

**Troubleshooting with CloudTrail:**

1. Search for event name `Decrypt`
2. Review the `errorCode` and `errorMessage` fields
3. Check `userIdentity` to confirm which principal attempted the operation

To resolve this issue, grant the user or IAM principal `kms:Decrypt` access permissions in their IAM policy and KMS key policy. For more information, see [Implementing customer managed KMS keys in AWS IAM Identity Center](identity-center-customer-managed-keys.md "identity-center-customer-managed-keys.md").

## KMS Permissions Issue: Configuring Customer Managed Key with AWS IAM Identity Center

The user or IAM principal lacks one or more required KMS permissions (`kms:Decrypt`, `kms:Encrypt`, `kms:GenerateDataKey`, `kms:DescribeKey`) when enabling customer managed key.

**Troubleshooting with CloudTrail:**

1. Search for `Decrypt`, `Encrypt`, `GenerateDataKey`, or `DescribeKey` events
2. Review the `errorCode` and `errorMessage` fields
3. Check `userIdentity` to confirm which principal attempted the operation

To resolve this issue, grant all required KMS permissions to the user or IAM principal in their identity-based policy or KMS key policy. For more information, see [Implementing customer managed KMS keys in AWS IAM Identity Center](identity-center-customer-managed-keys.md "identity-center-customer-managed-keys.md").

## AWS access portal login failures with a customer managed KMS key enabled in IAM Identity Center

**Error:** "ERROR Code: 0001 - IdentityCenter service access is blocked. Reach out to your IdentityCenter admin for further steps."

If users cannot log in to the AWS access portal and you have a customer managed KMS key enabled in your IAM Identity Center instance, verify that the KMS key policy grants the necessary permissions to Identity Center and Identity Store. For more information, see [Baseline KMS key and IAM policy statements](baseline-KMS-key-policy.md "baseline-KMS-key-policy.md").

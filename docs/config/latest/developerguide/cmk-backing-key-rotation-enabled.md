# cmk-backing-key-rotation-enabled

Checks if automatic key rotation is enabled for each key and matches to the key ID of the customer created AWS KMS key. The rule is NON_COMPLIANT if the AWS Config recorder role for a resource does not have the kms:DescribeKey permission.

###### Note

Automatic key rotation is not supported for asymmetric KMS keys, HMAC KMS keys, KMS keys with imported key material, or KMS keys in custom key stores.

**Identifier:** CMK_BACKING_KEY_ROTATION_ENABLED

**Resource Types:** AWS::KMS::Key

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Middle East (UAE) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

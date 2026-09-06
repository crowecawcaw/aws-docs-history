

# Customer-managed keys (optional)
<a name="next-gen-cmk"></a>

Next generation Resilience Hub supports customer-managed AWS KMS keys (CMKs) for encrypting your data. To use a CMK, ensure your IAM policy includes the following AWS KMS permissions:
+ `kms:DescribeKey`
+ `kms:GenerateDataKey`
+ `kms:Encrypt`
+ `kms:Decrypt`

For scheduled or long-running assessments, also include `kms:CreateGrant`.

No changes to the invoker role are needed for CMK encryption. Next generation Resilience Hub uses your caller identity for synchronous operations and AWS KMS grants for asynchronous operations.
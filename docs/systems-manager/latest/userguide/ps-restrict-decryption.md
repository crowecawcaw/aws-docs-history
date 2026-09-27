

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Restricting decryption of `SecureString` parameter values
<a name="ps-restrict-decryption"></a>

A `SecureString` parameter value is encrypted with an AWS KMS key. Any principal that retrieves the decrypted value must have `kms:Decrypt` permission on that key, whichever Parameter Store operation they call. This makes AWS KMS key permissions an effective control for `SecureString` parameters, because a single AWS KMS policy statement applies to all retrieval paths at once.

To use this control effectively, encrypt sensitive parameters with a customer managed key rather than the AWS managed key.

**Important**  
The AWS managed key for Parameter Store (`aws/ssm`) grants `Decrypt` permission to all IAM principals in the AWS account. If you need different levels of access to `SecureString` parameters within an account, don't encrypt them with the default key.

For key policy examples, including how to deny access to the AWS managed key and how to grant access to a customer managed key, see [Encrypting and decrypting parameters using AWS KMS keys](parameter-store-setting-up.md#ps-kms-permissions).

**Note**  
Restricting `kms:Decrypt` prevents a principal from reading an encrypted *value*. It doesn't hide the parameter's name, description, or other metadata, which aren't encrypted, and it doesn't prevent the parameter from being listed. Use Parameter Store action denies as described in [Restricting access to specific parameters and paths](ps-restrict-parameter-access.md) to control those.
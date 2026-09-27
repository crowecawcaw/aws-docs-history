

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Restricting access to specific parameters and paths
<a name="ps-restrict-parameter-access"></a>

Use the following approach to restrict access to a parameter or a set of parameters. This approach reflects the authorization behavior described in [How Parameter Store authorizes parameter retrieval](ps-retrieval-authorization.md).

**To restrict access to specific parameters or paths**

1. **Prefer granting narrow access over denying broad access.** Where you can, scope `Allow` statements to the smallest set of parameters a principal needs, rather than granting broad access and then subtracting from it. An `Allow` statement that never grants access to a parameter doesn't depend on you enumerating every action correctly.

1. **Separate sensitive parameters into their own path.** Restricting access is simpler when sensitive parameters don't share a path with parameters that principals are allowed to read. For example, store restricted values under `/myapp/restricted/` rather than alongside general configuration under `/myapp/config/`. For more information about organizing parameters, see [Working with parameter hierarchies in Parameter Store](sysman-paramstore-hierarchies.md).

1. **When you deny access, deny every action that can return the value.** Include `ssm:GetParameter`, `ssm:GetParameters`, `ssm:GetParameterHistory`, and `ssm:GetParametersByPath`, or use `ssm:GetParameter*` to match all four.

1. **For `GetParametersByPath`, deny every ancestor path.** A deny on the parameter's own ARN doesn't stop the parameter from being returned by a call against a path above it. To protect `/myapp/restricted/db-password`, deny `ssm:GetParametersByPath` for `/myapp/restricted`, `/myapp`, and `/`.

1. **For `SecureString` parameters, restrict `kms:Decrypt` on the KMS key.** Retrieving a decrypted `SecureString` value requires `kms:Decrypt` permission on the key that encrypted it, regardless of which Parameter Store operation is used. Denying `kms:Decrypt` therefore prevents decryption through every retrieval path. See [Restricting decryption of `SecureString` parameter values](ps-restrict-decryption.md).

1. **Verify the result.** Test each retrieval operation as the restricted principal. Include a test of `GetParametersByPath` against each ancestor path to confirm the policy behaves as you intend. You can also use the IAM [policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html) to evaluate a policy against specific actions and resources.

For more information about how IAM combines `Allow` and `Deny` statements, see [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) in the *IAM User Guide*.
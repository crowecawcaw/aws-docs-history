# Considerations for customer managed KMS keys and advanced KMS key policies

When implementing customer managed KMS keys with IAM Identity Center, consider these factors that affect setup, security, and ongoing maintenance of your encryption configuration.


## Considerations for choosing baseline vs. advanced KMS key policy statements


When deciding whether to make the KMS key permissions more specific using [Advanced KMS key policy statements](advanced-kms-policy.md "advanced-kms-policy.md"), consider the management overhead and the security needs of your organization. More specific policy statements provide finer-grained control over who can use the key and for what purposes; however, they require ongoing maintenance as your IAM Identity Center configuration evolves. For example, if you restrict the use of the KMS key to specific AWS managed application deployments, you'll need to update the key policy whenever your organization wants to deploy or undeploy an application. Less restrictive policies reduce administrative burden but may grant broader permissions than necessary for your security requirements.


## Considerations for enabling a new IAM Identity Center instance with a customer managed KMS key



 The considerations here apply if you're using the encryption context as described in [Advanced KMS key policy statements](advanced-kms-policy.md "advanced-kms-policy.md") to restrict use of the KMS key to a specific IAM Identity Center instance.
 



 When enabling a new IAM Identity Center instance with a customer managed KMS key, the IAM Identity Center and Identity Store ARNs are not available until after setup. You have the following options:
 



* Use generic ARN patterns temporarily, and then replace with full ARNs after the instance is enabled. Remember to switch between StringEquals and StringLike operators as needed.




	+ For IAM Identity Center SPN: "arn:${Partition}:sso:::instance/\*".
	+ For Identity Store SPN: "arn:${Partition}:identitystore::${Account}:identitystore/\*".
* Use "purpose:KEY\_CONFIGURATION" in the ARN temporarily. This works only for instance enablement and must be replaced with the actual ARN for your IAM Identity Center instance to function normally. The advantage of this approach is that you cannot forget to replace this after the instance is enabled.
 




	+ For IAM Identity Center SPN, use: "arn:${Partition}:sso:::instance/purpose:KEY\_CONFIGURATION"
	+ For Identity Store SPN, use: "arn:${Partition}:identitystore::${Account}:identitystore/purpose:KEY\_CONFIGURATION"
###### Important


 Don't apply this configuration to a KMS key already in use in an existing IAM Identity Center instance, as it may disrupt its normal operations.
* Omit the encryption context condition from the KMS key policy until after the instance is enabled.

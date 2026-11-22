

# Cross-service confused deputy prevention in Amazon OpenSearch Memory

The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action. In AWS, cross-service impersonation can result in the confused deputy problem. Cross-service impersonation can occur when one service (the *calling service*) calls another service (the *called service*). The calling service can be manipulated to use its permissions to act on another customer's resources in a way it should not otherwise have permission to access.

Amazon OpenSearch Memory doesn't assume a role in your account and doesn't support resource-based policies, so there is no OpenSearch Memory resource policy to which you need to add the `aws:SourceArn` or `aws:SourceAccount` condition keys.

When OpenSearch Memory accesses other AWS resources on your behalf, it does so with your permissions. When you create a space with a customer managed key, or read or write data in such a space, OpenSearch Memory uses your AWS KMS key with the permissions of the principal that made the request. Your key policy and IAM policies apply to that principal.

To limit how your key can be used, add the `kms:ViaService` condition to the key policy so that the key can be used only through OpenSearch Memory. For more information, see [Permissions required for a customer managed key](memory-data-protection.md#memory-encryption-permissions).
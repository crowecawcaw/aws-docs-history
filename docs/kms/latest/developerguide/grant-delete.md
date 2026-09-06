

# Retiring and revoking grants
<a name="grant-delete"></a>

To delete a grant, retire or revoke it.

The [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) and [RevokeGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html) operations are very similar to each other. Both operations delete a grant, which eliminates the permissions the grant allows. The primary difference between these operations is how they are authorized.

**RevokeGrant**  
Like most AWS KMS operations, access to the `RevokeGrant` operation is controlled through [key policies](key-policies.md) and [IAM policies](iam-policies.md). The [RevokeGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html) API can be called by any principal with `kms:RevokeGrant` permission. This permission is included in the standard permissions given to key administrators. Typically, administrators revoke a grant to deny permissions the grant allows.

**RetireGrant**  
The grant determines who can retire it. This design allows you to control the lifecycle of a grant without changing key policies or IAM policies. Typically, you retire a grant when you are done using its permissions.  
A grant can be retired by any of the following:  
+ The [retiring principal](grants.md#terms-retiring-principal) or [retiring service principal](grants.md#terms-retiring-service-principal) specified in the grant.
+ The [grantee principal](grants.md#terms-grantee-principal) or [grantee service principal](grants.md#terms-grantee-service-principal), if the grant includes the `RetireGrant` operation.
+ The AWS account in which the grant was created.
There is a `kms:RetireGrant` permission that can be used in IAM policies, but it has limited utility. Principals specified in the grant can retire a grant without the `kms:RetireGrant` permission. The `kms:RetireGrant` permission alone does not allow principals to retire a grant. The `kms:RetireGrant` permission is not effective in a [key policy](key-policies.md) or [resource control policy](resource-control-policies.md).  
+ To deny permission to retire a grant, you can use a `Deny` action with the `kms:RetireGrant` permission in your IAM policies.
+ The AWS account that owns the KMS key can delegate the `kms:RetireGrant` permission to an IAM principal in the account. 
+ If the retiring principal is a different AWS account, administrators in the other account can use `kms:RetireGrant` to delegate permission to retire the grant to an IAM principal in that account.

The AWS KMS API follows an [eventual consistency](grants.md#terms-eventual-consistency) model. When you create, retire, or revoke a grant, there might be a brief delay before the change is available throughout AWS KMS. It typically takes less than a few seconds for the change to propagate throughout the system, but in some cases it can take several minutes. If you need to delete a new grant immediately, before it is available throughout AWS KMS, [use a grant token](using-grant-token.md) to retire the grant. You cannot use a grant token to revoke a grant.
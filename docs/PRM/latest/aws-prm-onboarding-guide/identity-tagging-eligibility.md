

# Eligibility

Use the following table to determine whether your engagement model is eligible for Identity Tagging.


| Engagement model | Eligible | Details | 
| --- | --- | --- | 
| Partner operates in a customer account via a tagged IAM role (cross-account or same-account) | Yes | Tag the role your organization assumes. API actions on billable resources are attributed to your product. | 
| Partner invokes a metered service (for example, Amazon Bedrock) via a tagged IAM role or user | Yes | Exact revenue is attributed through the metering path using IAM principal cost allocation. | 
| Partner accesses the customer environment only through AWS IAM Identity Center (permission sets / federated sessions) | No | Permission sets are not taggable IAM principals. Support is deferred to a future phase. Use another ARM attribution method where applicable. | 
| Partner's contribution is through resource ownership or SDK embedding rather than an operating identity | No | Use Resource Tagging or User Agent String instead. | 

**Important**  
If your only path into the customer environment is through AWS IAM Identity Center permission sets or other federated sessions, Identity Tagging is not available at this time because those sessions are not backed by a taggable IAM principal. Use Resource Tagging or User Agent String where your product's architecture supports them.

## Supported partitions
<a name="identity-tagging-partitions"></a>

Identity Tagging is supported in the AWS commercial partition only. Note, however, customers in regulated or public-sector industries running in the commercial partition remain fully in scope.


# Eligibility

Use the following table to determine whether your deployment model is eligible for Account Tagging for SaaS products.


| Deployment model | Eligible | Details | 
| --- | --- | --- | 
| One product runs in one or more dedicated AWS accounts | Yes | Each account maps to exactly one product. Tag all accounts hosting the product. | 
| Multiple listings represent the same underlying product across one or more accounts | Yes | All consumption in those accounts is attributable to a single product. | 
| Multiple products share one AWS account | No | Use Resource Tagging or User Agent String instead. | 

**Important**  
If multiple products share the same AWS account, Account Tagging for SaaS products is not available. In this scenario, use Resource Tagging to tag individual resources per product, or User Agent String to attribute consumption at the API call level.
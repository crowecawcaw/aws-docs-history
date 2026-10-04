

# Additional cost components
<a name="transform-app-assessments-cost-components"></a>

Beyond the per-workload service recommendations, AWS Transform models several cross-cutting cost components so your total cost of ownership comparison reflects the full picture on both sides of the migration.

## On-premises pricing
<a name="transform-app-assessments-cost-components-onprem"></a>

AWS Transform estimates your current on-premises costs to provide a baseline for comparison with AWS pricing. Most organizations have on-premises costs that a server inventory does not capture—colocation rent, networking, custom vendor deals, hardware refresh cycles, and maintenance contracts. You can add these directly through chat, and AWS Transform folds them into the baseline. On-premises cost adjustments are reflected in the PDF report and chat responses, but not in the PPTX export.

Example prompts:
+ "Update the on-premises server cost to $500 per server per month"
+ "My data center is a colo and I pay $10M a year in rent, add this to my on-premises costs"
+ "Add $100,000 annual maintenance costs to the on-premises baseline"

## Network costs
<a name="transform-app-assessments-cost-components-network"></a>

AWS Transform estimates network-related costs for your migration, including data transfer and connectivity requirements, and includes them in the AWS side of the comparison.

## Support costs
<a name="transform-app-assessments-cost-components-support"></a>

AWS Transform includes AWS Support plan costs in the assessment based on your selected support tier, such as Business Support or Enterprise Support.

## End user computing
<a name="transform-app-assessments-cost-components-euc"></a>

AWS Transform assesses end user computing workloads that are candidates for Amazon WorkSpaces rather than Amazon EC2, and models the cost of running them on Amazon WorkSpaces. This lets you separate virtual desktop workloads from server workloads in your business case.

## Adding other AWS services
<a name="transform-app-assessments-cost-components-additional-services"></a>

You can add rough cost estimates for AWS services that are not fully modeled by AWS Transform assessments, so your analysis is more complete. These estimates are less accurate than the automated recommendations. For example, you can ask AWS Transform to add AWS Backup, Amazon CloudWatch, or AWS Direct Connect costs, or to move specific servers to another service such as Amazon Connect and remove them from the compute model.
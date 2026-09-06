

# DRHCCOST01-BP01 Implement a comprehensive tagging strategy for hybrid edge workloads
<a name="drhccost01-bp01"></a>

 Implement cost attribution using resource tagging. 

 **Desired outcome:** You use tags to attribute workload costs. 

 **Benefits of establishing this best practice:** You can have a better understanding of what is driving the cost of the workload. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-47"></a>

 Implementing a comprehensive tagging strategy is crucial for effectively managing hybrid edge workloads. Tagging enables cost attribution and usage metering through the use of identifiers and cost allocation tags in the [Cost and Usage Report (CUR)](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/). It also facilitates [management and governance](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-strategies-governance) and lifecycle management through automation of policies and processes using custom tags and services like AWS Config and AWS Systems Manager. 

 Tagging in hybrid edge environments like Outposts and Local Zones operates similarly to cloud Regions, providing a consistent experience and familiar tools. Organizations can use existing tools and services to manage tagging strategies at scale across hybrid edge workloads, including implementing [automated tagging policies and remediation workflows](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-laying-the-foundation/tagging.html?ref=wellarchitected#enforce-quality-of-tagging) to comply with tagging standards. 

 Tagging enables organizations to derive total cost of ownership associated with workloads. Tagging in hybrid edge (Outposts and Local Zones) operates similarly as in-Region. Once a tag is activated as a cost allocation tag, data appears in the [Cost and Usage Report (CUR)](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/) for analysis. 
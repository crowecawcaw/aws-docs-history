

# COST07-BP02 Choose Regions based on cost

 Resource prices vary by Region. Where latency, data residency, data sovereignty, and regulatory rules permit, placing a workload in a lower-cost Region reduces spend. Data transfer costs and service availability can outweigh the price difference. 

 **Desired outcome:** 
+  Your workloads run in the lowest-cost Region that still meets their latency, data residency, data sovereignty, and regulatory requirements. 
+  Your Region selection accounts for data transfer costs, not resource prices alone. 
+  You deploy across multiple Regions only where a business, resiliency, or compliance need justifies it. 

 **Common anti-patterns:** 
+  Choosing a Region that fails to meet workload latency, data residency, data sovereignty, or regulatory requirements. 
+  Comparing resource prices across Regions while ignoring data transfer costs that erase the savings. 
+  Building multi-Region deployments without a clear business or resiliency need. 
+  Defaulting every workload to one home Region without checking whether a lower-cost Region qualifies. 

 **Benefits of establishing this best practice:** 
+  Eligible workloads run at lower resource rates, which reduces overall cost. 
+  Region decisions weigh total cost, including data transfer, rather than resource price alone. 
+  Compliance and latency requirements stay satisfied because cost is one input among several. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 The [AWS Cloud infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) spans [many locations worldwide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) and is built around Regions, Availability Zones, Local Zones, AWS Outposts, and Wavelength Zones. A Region is a separate geographic area that contains multiple Availability Zones. Each Availability Zone is one or more discrete data centers with redundant power, networking, and connectivity. Prices vary by Region because the cost of operating infrastructure varies by location. 

 Region choice balances several competing requirements. Placing resources closer to users lowers latency. Data privacy, sovereignty, and regulatory rules can require that data stay within a specific geography. Cost pushes toward the cheapest qualifying Region. When a workload has no data residency, security, or business obligation and moves little data relative to its size, the lowest-priced Region is a valid choice. Use the [AWS Pricing Calculator](https://calculator.aws/#/) to estimate workload costs across Regions. 

 Data transfer is the cost that most often erases regional savings. A cheaper Region far from your users or other resources can cost more overall once cross-Region and internet egress charges are counted. Weigh the resource-price saving against the data transfer it creates before committing to a move. Service availability limits Region choice. Not every service or feature is available in every Region, so a low-cost Region that lacks a required service is not an option. 

 Compare candidate Regions across all requirements at once. Figure 1 shows a matrix that scores Regions on compliance, latency, service availability, and cost. <a name="cost07-bp02-fig1"></a>

![Comparison matrix scoring candidate AWS Regions across compliance, latency, service availability, and cost.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/region-feature-matrix.png)

*Region comparison matrix across compliance, latency, service availability, and cost*


 In Figure 1, Region 6 is the strongest option because latency is low, the required service is available, and it is the cheapest qualifying Region. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Compare Region pricing for the workload:** Start with the highest costs by service and usage type in the current Region, then calculate the same usage in other available Regions with the AWS Pricing Calculator. If the forecasted saving outweighs the cost of moving the component or workload, plan the migration. 

1.  **Confirm requirements before considering multiple Regions:** Review data privacy, security, sovereignty, and performance obligations to determine whether any rule restricts Region choice. Use multiple Regions only when a business, resiliency, or compliance need justifies the added cost and complexity. 

1.  **Model data transfer costs:** Calculate the data transfer that a Region change would create, and keep data close to both your customers and your resources. Where data transfer drives cost, use [Amazon CloudFront](https://aws.amazon.com/cloudfront/), [AWS PrivateLink](https://aws.amazon.com/privatelink/), [AWS Direct Connect](https://aws.amazon.com/directconnect/), and [Site-to-Site VPN](https://aws.amazon.com/vpn/) to reduce networking cost, improve performance, and strengthen security. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST04-BP03 Optimize services to reduce data transfer costs](cost04-bp03.md) 
+  [COST07-BP01 Perform pricing model analysis](cost07-bp01.md) 

 **Related documents:** 
+  [Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) 
+  [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) 

 **Related examples:** 
+  [Overview of Data Transfer Costs for Common Architectures](https://aws.amazon.com/blogs/architecture/overview-of-data-transfer-costs-for-common-architectures/) 
+  [Cost Considerations for Global Deployments](https://aws.amazon.com/blogs/aws-cloud-financial-management/cost-considerations-for-global-deployments/) 
+  [What to Consider when Selecting a Region for your Workloads](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/) 
+  [Service control policy examples, including Region restriction](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples.html) 

 **Related services:** 
+  [AWS Pricing Calculator](https://calculator.aws/#/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 
+  [AWS Direct Connect](https://aws.amazon.com/directconnect/) 
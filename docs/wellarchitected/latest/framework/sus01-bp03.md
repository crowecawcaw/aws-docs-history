

# SUS01-BP03 Select Regions that align to your sustainability goals

 While many factors influence Region selection, incorporating sustainability into your decision-making can support your environmental goals. Choose an AWS Region by first evaluating essential requirements such as cost, latency, service availability, and compliance. Then, from the shortlisted Regions that meet these criteria, consider the carbon intensity of each Region's power grid to make an environmentally conscious decision. 

 **Desired outcome:** 
+  You deploy workloads in AWS Regions with lower carbon intensity and higher carbon-free energy availability where business requirements allow. 
+  You reduce the environmental impact of your workloads while continuing to meet critical business requirements, without compromising performance or agility. 

 **Common anti-patterns:** 
+  Selecting Regions based solely on proximity to team location. 
+  Ignoring sustainability factors completely in Region selection decisions. 
+  Deploying all workloads in a single Region without consideration for the specific needs of a given workload. 
+  Using only a previously selected region, even when regions with lower emission factors that satisfy business requirement become available. 
+  Not taking advantage of geographic flexibility when it exists. 

 **Benefits of establishing this best practice:** 
+  Reduces the carbon footprint of your cloud workloads. 
+  Establishes awareness of regional differences within your teams, helping them make informed tradeoffs. 
+  Supports organizational sustainability goals and commitments. 
+  Demonstrates environmental responsibility to stakeholders. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Implementing a Region selection strategy that aligns to sustainability requirements requires understanding both your workload requirements and the sustainability characteristics of different AWS Regions. By analyzing these factors and making informed decisions, you can optimize your workload placement for both business needs and environmental impact. 

 Based on the [Green House Gas Protocol](https://ghgprotocol.org/scope-2-guidance), there are two ways to consider the carbon intensity of generated electricity: location-based method (LBM) and market-based method (MBM). 
+  LBM emission factors measure the average emissions intensity of the grids where the electricity consumption occurs. 
+  MBM emission factors measure the emissions intensity based on the electricity that organizations have chosen to purchase at the grid level. 

 When business requirements allow, choose Regions that have both a low MBM and low LBM value. Both MBM and LBM carbon intensity values can change over time, and therefore the best Region for your workload may change over time. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Understand the carbon intensity of AWS Regions: 
   +  Review [Amazon's carbon free energy projects and their locations](https://sustainability.aboutamazon.com/climate-solutions/carbon-free-energy). 
   +  Understand [Amazon's renewable energy methodology](https://sustainability.aboutamazon.com/renewable-energy-methodology.pdf). 
   +  Consider both [location-based (grid) and market-based (renewable energy purchases)](https://ghgprotocol.org/sites/default/files/2023-03/Scope%202%20Guidance.pdf) carbon metrics. 

1.  Analyze your workload requirements and constraints: 
   +  Identify regulatory and compliance requirements that may restrict Region choice. 
   +  Evaluate latency requirements based on end user locations, integrated services or additional data sources. 
   +  Determine [service and feature availability](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/?p=ngi&loc=4)y needs for each workload. 
   +  Calculate the cost implications of different Region options. 
   +  Review data in the Customer Carbon Footprint Tool to see how your current regional deployment strategy [influences the emissions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/) associated with your AWS workloads. 

1.  Develop a Region selection strategy that balances requirements: 
   +  Create a decision framework that weighs sustainability alongside other factors, based on your organization's sustainability goals. 
   +  Identify workloads with flexibility in their geographical placement. 
   +  Prioritize Regions that have low LBM and MBM for geographically-flexible workloads. 
   +  Some organizations will have specific LBM or MBM related goals or strategies. In those cases, prioritize low LBM or low MBM Regions. 

1.  Implement Region placement decisions: 
   +  Deploy new workloads according to your Region selection strategy. 
   +  Document the sustainability impact of your Region choices. 

1.  Monitor and adjust over time: 
   +  Track how grid carbon intensity changes over time, using sources such as [EPA](https://www.epa.gov/egrid), [AIB](https://www.aib-net.org/facts/european-residual-mix), and [IEA](https://www.iea.org/data-and-statistics/data-sets). 
   +  Monitor how your AWS emissions change over time, based on your Regional distribution, in the AWS Sustainability service. 
   +  Reassess workload placement as business requirements evolve. 
   +  Update your Region strategy as AWS expands its global infrastructure to new Regions. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF01-BP02 Evaluate the trade-offs between performance and other non-functional requirements](perf01-bp02.md) 

 **Related documents:** 
+  [Carbon emissions](https://docs.aws.amazon.com/sustainability/latest/userguide/methodology-carbon.html) 
+  [Renewable Energy Methodology](https://sustainability.aboutamazon.com/renewable-energy-methodology.pdf) 
+  [Input data](https://docs.aws.amazon.com/sustainability/latest/userguide/methodology-input-data.html) 
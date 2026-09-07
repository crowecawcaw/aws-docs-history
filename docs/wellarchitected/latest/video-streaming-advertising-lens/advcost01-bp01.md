

# ADVCOST01-BP01 Continually measure costs of different real-time bidding workloads, and adjust resource allocation accordingly
<a name="advcost01-bp01"></a>

 With fluctuations in usage over time, the costs associated with real-time bidding workloads can vary significantly. Continually monitoring costs is the best way to keep them under control. 

## Implementation guidance
<a name="implementation-guidance-57"></a>
+  Set KPIs for each campaign to evaluate cost-to-revenue ratios, as this is key to measuring value generation. 
+  Set KPIs for billing metrics (for example, resource costs) as well as campaign metrics (for example, click-through rate or new subscribers). 
+  Implement cost allocation tags for resources relevant to campaign tracking. 
+  Use the Cost and Usage Dashboards Operations Solution (CUDOS) Dashboard as a way to quickly visualize information about RTB costs and performance. 
+  Use [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) for one-off visualizations of cost data. 
+  Generate [Quick](https://aws.amazon.com/quicksight/) dashboards that are specific to each campaign or that comprise the business as a whole. 
+  Configure Quick with user-configurable filters to allow users to focus on the data that matters most to them. 
+  Configure Quick to email dashboard reports to users on a schedule to automate and simplify the process. 
+  Regularly evaluate the data and report findings back to the business. 
+  As campaigns progress, continually re-evaluate them, and adjust resource allocation to meet value generation goals. 

## Key AWS services
<a name="key-aws-services-32"></a>
+  [Amazon Athena](https://aws.amazon.com/athena/) 
+  [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) 

## Resources
<a name="resources-51"></a>
+  [Guidance for Deploying a Data Transfer Dashboard for AdTech on AWS](https://aws.amazon.com/solutions/guidance/deploying-a-data-transfer-dashboard-for-adtech-on-aws/) 
+  [Guidance for Capturing Advertising OpenRTB (Real-Time Bidding) Events for Analytics on AWS](https://aws.amazon.com/solutions/guidance/capturing-advertising-openrtb-real-time-bidding-events-for-analytics-on-aws/) 
+  [Using CUDOS Dashboard visualizations for AWS Marketplace spend visibility and optimization](https://aws.amazon.com/blogs/awsmarketplace/using-cudos-dashboard-visualizations-aws-marketplace-spend-visibility-optimization/) 
+  [Additional dashboards](https://catalog.workshops.aws/awscid/en-US/dashboards/additional) 
+  [Organizing costs using AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html) 
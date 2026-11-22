

# SUS01-BP02 Create dashboards to combine resource usage efficiency and environmental impact data

 The carbon emissions associated with your AWS usage are [influenced by several factors](https://sustainability.aboutamazon.com/aws-customer-carbon-footprint-methodology.pdf), including the resources you have provisioned to support your workload. Efficient use of resources reduces the environmental impact of your workload and is directly correlated with the emissions associated with the workload. Create dashboards that visualize your resource usage efficiency (RUE) alongside data from the [AWS Sustainability service](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html) to provide a holistic view of your cloud workload's environmental impact. Dashboards should showcase RUE and workload environmental impact. 

 **Desired outcome:** 
+  You create clear dashboards that visualize both resource utilization and the associated carbon emissions in one view. 
+  You track sustainability performance over time, identify optimization opportunities, and demonstrate progress toward your environmental goals. 
+  You use the insights from these dashboards to drive continuous improvement in workload sustainability. 

 **Common anti-patterns:** 
+  Creating dashboards that are too complex, requiring specialist knowledge to understand. 
+  Failing to establish connections between resource metrics and carbon emissions. 
+  Failing to use the carbon emissions or water withdrawl data available in the AWS Sustainability service 
+  Focusing exclusively on either technical metrics (such as CPU utilization) or carbon data without integrating both. 
+  Creating static dashboards that aren't regularly updated or connected to live data. 
+  Presenting data without context, benchmarks, or targets for improvement. 

 **Benefits of establishing this best practice:** 
+  Provides visibility into the environmental impact of operational decisions. 
+  Creates a common understanding of sustainability metrics across technical and non-technical stakeholders. 
+  Enables early identification of inefficiencies or unexpected resource consumption. 
+  Supports data-driven decision making for sustainability improvements. 
+  Helps track progress toward organizational sustainability goals. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Effective dashboards present complex sustainability data in an accessible format, tailored to meet the needs of different stakeholders. Creating dashboards provides a straightforward way for leaders and technical teams to identify trends, spot anomalies, and track progress toward sustainability goals. By combining resource metrics with emissions data, these dashboards establish a clear connection between operational decisions and environmental outcomes. Additional metrics, such as utilization metrics, response time, and latency may be useful to visualize in one place. This visualization can help track how sustainability-related optimizations can in turn reduce cost or improve performance. 

 Regularly collect carbon emissions and usage data. Calculate the [SUS01-BP01 Understand your resource usage efficiency](sus01-bp01.md) for your workload. Determine the workload carbon intensity by ingesting data from the AWS Sustainability service and dividing the carbon emissions value by a business metric or workload outcome. The denominator for RUE and the carbon intensity should be the same, as this makes it more consistent to track progress over time. 

### Implementation steps
<a name="implementation-steps"></a>

 Depending on your preferred business intelligence products either start with existing AWS solutions or build dashboards on top of your own business intelligence stack. 

1.  Gather and prepare your data sources: 
   +  Set up [CUR 2.0 via Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) to collect detailed usage data. 
   +  Set up a Data Export for the [carbon emissions table](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-carbon-emissions.html). 

1.  Design your dashboard layout and content: 
   +  Identify the key metrics and visualizations that will be most useful for your audience. 
   +  Plan how to present both resource utilization and carbon emissions in a cohesive way. 
   +  Consider different dashboard views for different stakeholders. For example, technical, business, and executive. 
   +  You may also want to include metrics for cost, performance, and resilience to have a single view of your workload, as seen in the [Cloud Intelligence Dashboards](https://catalog.workshops.aws/awscid/en-US/dashboards). 

1.  Implement your dashboard: 
   +  If you're using Cloud Intelligence Dashboards, deploy the [Sustainability proxy metrics dashboards](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/sustainability-proxy-metrics-dashboard.html). 
   +  Otherwise, use [AWS Quick Sight](https://aws.amazon.com/quick/quicksight/) to create interactive dashboards with data from multiple sources. 
   +  Configure [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) dashboards for real-time monitoring of resource metrics 
   +  Create custom visualizations using Amazon Managed Grafana if needed for more complex requirements. 

1.  Integrate carbon footprint data: 
   +  Import carbon data from data exports. 
   +  Create visualizations that combine RUE and the carbon data, and normalize with your workload's business metric or workload outcome. 
   +  Include Regional carbon intensity information to contextualize emissions data. 

1.  Enhance your dashboards with actionable insights: 
   +  Add baselines, thresholds, and targets to provide context for the metrics. 
   +  Include trend lines to show progress over time. 
   +  [Configure alerts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) for significant deviations or opportunities for improvement. 

1.  Drive continuous improvement: 
   +  Use these dashboards to evaluate and implement specific improvements. 
   +  Based on your learnings, establish standards, and apply successful improvements to other workloads. Capture and share your methodology, related artifacts, and net benefits, across teams and organizations so that others replicate your success. 
   +  Monitor RUE and track changes to total impact over time. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SUS01-BP01 Understand your resource usage efficiency](sus01-bp01.md) 
+  [SUS01-BP03 Select Regions that align to your sustainability goals](sus01-bp03.md) 
+  [COST03-BP01 Track resources over their lifetime](cost03-bp01.md) 

 **Related documents:** 
+  [AWS Sustainability API and console](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html) 
+  [Calculation methodology](https://docs.aws.amazon.com/sustainability/latest/userguide/methodology.html) 
+  [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) 
+  [What is AWS Quick?](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html) 
+  [Get your data in bulk](https://docs.aws.amazon.com/sustainability/latest/userguide/bulk-data.html) 

 **Related examples:** 
+  [Unlocking the power of Carbon Emissions CUR](https://catalog.workshops.aws/unlock-carbon-and-cur) 
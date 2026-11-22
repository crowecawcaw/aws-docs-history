

# Measure and monitor sustainability

 This capability covers guidance on how to understand and monitor the emissions associated with your AWS usage. It helps you verify that your provisioned resources are generating real business value and that these resources are used fully. 

 There are two critical components for you to understand and monitor your emissions. 

 Monitor your *resource usage efficiency (RUE)*. RUE is a ratio, where the numerator should be the core resource consumption metric and the denominator is a business or customer metric. An example of RUE could be: 

![Formula dividing gigabytes of storage in Amazon S3 Standard by the number of active customers.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/sus01-storage-per-customer-formula.png)

*Storage provisioned per active customer*


 Additionally, monitor your emissions in the [AWS Sustainability Console](https://aws.amazon.com/sustainability/tools/console/). This tool helps you track your historical emissions from AWS usage and includes [Greenhouse Gas Protocol](https://ghgprotocol.org/) Scope 1, 2 and 3 emissions, as explained in the [methodology document](https://sustainability.aboutamazon.com/aws-customer-carbon-footprint-methodology.pdf). 

 The data in the AWS Sustainability service is is available through [Carbon emissions Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-carbon-emissions.html) and via [API](https://docs.aws.amazon.com/sustainability/latest/APIReference/Welcome.html) to simplify automation and integrating this data into dashboards. 

 Together, RUE and carbon emissions data help you understand your resource usage and its relative carbon impact. As detailed in the [methodology](https://sustainability.aboutamazon.com/aws-customer-carbon-footprint-methodology.pdf), emissions in AWS Sustainability depend on your usage. Track workload RUE and emissions over time to observe how efficiency gains and changes in your workload demand influence your emissions. 


|  SUS01: How do you measure, monitor, and account for the sustainability impact of your workload?  | 
| --- | 
|  [SUS01-BP01 Understand your resource usage efficiency](sus01-bp01.md)  | 
|  [SUS01-BP02 Create dashboards to combine resource usage efficiency and environmental impact data](sus01-bp02.md)  | 
|  [SUS01-BP03 Select Regions that align to your sustainability goals](sus01-bp03.md)  | 

## Capability intent
<a name="sus01-intent"></a>
+  Resource usage efficiency metrics relate the resources provisioned for a workload to a unit of business value, using stable definitions that stay comparable across releases and over time. 
+  Baselines and improvement targets make sustainability progress measurable and comparable across the organization. 
+  Efficiency and carbon emissions data sit in the same view, normalized to the same business metric, so teams can see how an operational decision influences emissions. 
+  Dashboards draw from actual billing, usage, and carbon data rather than one-time snapshots. 
+  Region selection weighs grid carbon intensity alongside cost, latency, service availability, and compliance, and placement is reassessed as grid intensity and business needs change. 

## Common issues to watch for
<a name="sus01-issues"></a>
+  Teams track cost as a proxy for efficiency, so a lower bill from discounts or commitments looks like progress even when resource use per unit of work has not changed. 
+  The efficiency metric definition changes between reporting periods, which limits the value of historical comparison. 
+  Carbon data and resource metrics live on separate views, which hides the link between an operational decision and its environmental outcome. 
+  Dashboards present metrics without baselines, targets, or benchmarks, so a viewer cannot tell a good number from a bad one. 
+  Region selection ignores grid carbon intensity, or treats placement as a one-time decision that drifts out of alignment as grid mixes and business needs change. 


# MLSUS06-BP01 Measure material efficiency
<a name="mlsus06-bp01"></a>

 Measure efficiency of your workload in provisioned resources per unit of work to determine not only the business success of the workload, but also its material efficiency. Use this measure as a baseline for your sustainability improvement process. 

 **Desired outcome:** You can quantify and track the resources required by your machine learning workload to deliver its business outcomes. By measuring resources per unit of work, you create a sustainable baseline that allows you to track improvements over time, make data-driven decisions about resource optimization, and demonstrate the environmental impact of your sustainability efforts. 

 **Common anti-patterns:** 
+  Focusing exclusively on business metrics without considering resource consumption. 
+  Measuring total resource usage without normalizing by business outcomes. 
+  Making optimization decisions without quantitative data on resource efficiency. 

 **Benefits of establishing this best practice:** 
+  Creates a clear way to measure sustainability progress over time. 
+  Enables comparison of different implementations based on material efficiency. 
+  Provides data to demonstrate ROI on sustainability improvements. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Material efficiency is a critical aspect of sustainable machine learning workloads. By measuring the resources provisioned per unit of work, you gain visibility into how efficiently your workload uses cloud resources to deliver business value. This approach normalizes your sustainability metrics across different workload sizes, usage patterns, and business outcomes. 

 When implementing material efficiency measurements, you should first determine what constitutes a *unit of work* for your specific ML workload. This could be a model training run, a prediction request, a processed transaction, or another relevant business outcome. Then, establish which resources to track. Typically, this is compute (vCPU minutes), storage (GB), and network (GB transferred). By dividing your provisioned resources by these units of work, you create a normalized efficiency metric that can be tracked over time. 

 For example, a recommendation engine might track vCPU minutes per recommendation delivered, or a fraud detection system could measure GB of storage per fraudulent transaction identified. Tracking these metrics can determine if changes to your architecture, algorithms, or deployment strategies are improving efficiency or creating waste. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define your unit of work**. Identify what business outcomes your ML workload produces, such as model training completions, predictions made, insights generated, or transactions processed. Verify that this metric directly relates to business value delivered. 

1.  **Establish resource metrics**. Track key resource consumption metrics using Amazon CloudWatch. For ML workloads, important metrics include compute utilization (vCPU minutes), memory usage, storage consumption (GB), and network transfer (GB). AWS Cost Explorer can identify key cost drivers in your ML workload. 

1.  **Calculate baseline efficiency**. Divide your resource consumption metrics by your units of work to create efficiency ratios (for example, vCPU minutes per prediction, GB storage per model training run, or network transfer per transaction). Document these values as your baseline for future comparisons. 

1.  **Set improvement targets**. Based on your baseline measurements, set realistic targets for reducing resource consumption per unit of work. Consider both absolute reductions (total resources) and percentage improvements over the baseline. 

1.  **Implement monitoring and reporting**. Use Amazon CloudWatch dashboards to visualize your efficiency metrics over time. Set up alerts for significant deviations from expected efficiency. Amazon SageMaker AI provides built-in monitoring capabilities for ML workloads to track resource utilization. 

1.  **Quantify improvement benefits**. When implementing changes, calculate both the immediate resource savings and the projected long-term benefits. Include the return on investment from your improvement activities to demonstrate value to stakeholders. 

1.  **Review and optimize regularly**. Schedule regular reviews of your efficiency metrics to identify new optimization opportunities. As your workload evolves, your baseline and targets may need adjustment. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Analyzing your costs and usage with AWS Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-what-is.html) 
+  [Data and model quality monitoring with Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) 
+  [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) 
+  [Measure results and replicate successes](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/measure-results-and-replicate-successes.html) 
+  [AWS Well-Architected Framework - Sustainability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) 
+  [Cloud Financial Management with AWS](https://aws.amazon.com/aws-cost-management/) 


# MLCOST04-BP08 Stop resources when not in use
<a name="mlcost04-bp08"></a>

 Stop resources that are not in use to reduce cost. For example, hosted Jupyter environments used to explore small samples of data can be stopped when not actively in use. Where practical, commit the work, stop them, and restart when needed. The same approach can be used to stop the computing and the data storage services. 

 **Desired outcome:** You significantly reduce your ML infrastructure costs by only paying for resources when they are actively being used. You have automated systems in place to monitor and shut down idle resources, along with proper alerts to track spending patterns and avoid unexpected charges. You maintain the ability to quickly restart resources when needed while minimizing wasteful spending on idle compute and storage. 

 **Common anti-patterns:** 
+  Leaving development environments running regardless of actual usage. 
+  Neglecting to set up automatic shutdown mechanisms for idle resources. 
+  Ignoring cost monitoring tools and billing alerts. 
+  Using persistent storage for temporary data that could be deleted. 

 **Benefits of establishing this best practice:** 
+  Significant cost savings (up to 75% by running resources only during business hours compared to running continually). 
+  Better alignment of spending with actual usage patterns. 
+  Reduced environmental impact through more efficient resource consumption. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Optimizing costs is a crucial aspect of running machine learning workloads in the cloud. ML workloads often require significant computational resources, but those resources aren't needed continuously. By implementing automatic shutdown mechanisms for idle resources, you can achieve substantial cost savings while maintaining the ability to rapidly resume work when needed. 

 For ML development environments like SageMaker AI notebooks, the cost-optimization opportunity is particularly significant since these environments are typically used intermittently during the exploration and development phases. By committing code to repositories regularly and shutting down environments when not in use, you improve both cost efficiency and version control of your work. 

 Additionally, proper monitoring of spending patterns assists you in identifying optimization opportunities and avoiding unexpected costs. With AWS tools, you can set up alerts, track resource utilization, and implement automated responses to idle resources. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Set up Amazon CloudWatch billing alarms**. Use [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html) to monitor your estimated AWS charges. When you enable monitoring of estimated charges, these calculations are sent several times daily to CloudWatch as metric data. Configure alerts to be notified when your resource charges exceed predefined thresholds to stay within budget and quickly identify unexpected spending patterns. 

1.  **Configure Amazon SageMaker AI notebook lifecycle configurations**. Create [lifecycle configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html) that include shell scripts to run when you create or start notebook instances. These scripts can check for notebook instance activity and automatically shut down idle instances. This way, you're not paying for compute resources when they aren't actively processing workloads. 

1.  **Implement Amazon SageMaker AI Studio idle shutdown**. For [Amazon SageMaker AI Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-idle-shutdown.html) environments, install the auto-shutdown JupyterLab extension either [manually or automatically](https://github.com/aws-samples/sagemaker-studio-auto-shutdown-extension). This extension detects idle Studio resources and can shut down individual components, including notebooks, terminals, kernels, applications, and instances when they're not being used. 

1.  **Use AWS Cost Explorer to identify optimization opportunities**. Regularly analyze your ML infrastructure spending patterns using [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to identify resources that might be consistently underutilized. Look for patterns that indicate resources could benefit from scheduled shutdowns during off-hours. 

1.  **Implement instance scheduling**. Use the [AWS Instance Scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler/) to create automated schedules for starting and stopping resources based on your team's working hours. This is particularly useful for development environments that are only needed during business hours. 

1.  **Train teams on cost-aware practices**. Educate your ML teams on the importance of shutting down resources when not in use and committing their work regularly. Create a cost-aware culture where resource efficiency is valued alongside development productivity. 

1.  **Implement enhanced auto-shutdown capabilities**. Use improved SageMaker AI Studio auto-shutdown features with better idle detection and more granular control over resource shutdown policies to minimize costs from unused resources. 

1.  **Use Spot Instances for interruptible workloads**. For ML training jobs that can handle interruptions, use [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/) to achieve significant cost savings compared to on-demand pricing. Make sure your workloads are designed to checkpoint progress and can resume from interruptions. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Idle shutdown](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-idle-shutdown.html) 
+  [Customization of a SageMaker AI notebook instance using an LCC script](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html) 
+  [Instance Scheduler on AWS](https://aws.amazon.com/solutions/implementations/instance-scheduler/) 
+  [Create a billing alarm to monitor your estimated AWS charges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html) 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 
+  [Amazon SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing/) 
+  [Cloud Financial Management with AWS](https://aws.amazon.com/aws-cost-management/) 

 **Related videos:** 
+  [Saving cost on your machine learning training and inference on AWS](https://www.youtube.com/watch?v=keowy9YfxlcDeploy) 
+  [Deploy an ML model for best performance, cost, and prediction quality](https://www.youtube.com/watch?v=ftCFf57dQQY) 

 **Related examples:** 
+  [AWS CloudFormation templates for automated instance scheduling](https://github.com/aws-solutions/aws-instance-scheduler) 
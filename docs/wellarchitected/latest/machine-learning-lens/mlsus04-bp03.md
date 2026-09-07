

# MLSUS04-BP03 Archive or delete unnecessary training artifacts
<a name="mlsus04-bp03"></a>

 Remove training artifacts that are unused and no longer required to limit wasted resources. Determine when you can archive training artifacts to more energy-efficient storage or safely delete them. 

 **Desired outcome:** You reduce your environmental footprint by removing unnecessary storage of ML training artifacts. Your organization maintains only essential training data and models, efficiently archives what might be needed later, and systematically removes what is no longer required. This approach not only conserves resources but also simplifies management of your machine learning assets. 

 **Common anti-patterns:** 
+  Keeping training artifacts indefinitely. 
+  Ignoring the accumulation of unused logs, models, and experiment data. 
+  Not implementing systematic cleanup processes for completed experiments. 

 **Benefits of establishing this best practice:** 
+  Reduced storage costs and resource consumption. 
+  Improved organization and discoverability of important ML artifacts. 
+  Enhanced security through reduced data surface area. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Machine learning workflows generate substantial volumes of artifacts during the development process. These include experiment data, logs, model checkpoints, and various intermediary outputs. While some of these artifacts are essential for long-term use, many become unnecessary after model deployment or project completion. 

 Consider the lifecycle of your ML artifacts. Some might need preservation for compliance-aligned or reproducibility purposes, while others can be safely removed once they've served their immediate purpose. For artifacts that must be retained but are rarely accessed, consider using tiered storage options that balance accessibility with resource efficiency. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Organize your ML experiments with management tools**. Use [SageMaker AI Experiments](https://aws.amazon.com/sagemaker/ai/experiments/) to track, compare, and organize your machine learning experiments in a structured manner. This organization makes it more straightforward to identify which artifacts are essential and which can be archived or deleted. 

1.  **Implement regular cleanup procedures**. Follow the [clean up training resources](https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-cleanup.html) guidance from AWS to systematically remove SageMaker AI resources you no longer need. Create automated cleanup workflows that run on a schedule to avoid the accumulation of unused artifacts. 

1.  **Set appropriate log retention policies**. By default, Amazon CloudWatch retains logs indefinitely, which consumes unnecessary resources. Implement [limited retention time](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention) for your notebooks and training logs to automatically expire and delete logs after they're no longer needed. 

1.  **Establish storage lifecycle policies**. Configure [Amazon S3 lifecycle policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to automatically transition training artifacts to more cost-effective and energy-efficient storage classes like Amazon Glacier or S3 Glacier Deep Archive based on access patterns. 

1.  **Monitor storage utilization**. Use [Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-analytics-insights/) to gain visibility into your storage usage patterns and identify opportunities for optimization. Track metrics regularly to verify that your cleanup procedures are effective. 

1.  **Implement container image cleanup**. Use [Amazon ECR lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) to automatically clean up unused container images that may have been created during training jobs. This avoids the accumulation of outdated or unused container images. 

1.  **Establish artifact tagging standards**. Create a consistent tagging strategy for ML artifacts to identify their purpose, associated projects, and expiration dates. This makes it simpler to determine what can be archived or deleted during cleanup processes. 

1.  **Leverage managed MLflow for experiment tracking**. Use [managed MLflow on SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) to create, manage, analyze, and compare your machine learning experiments with better organization and tracking capabilities, making it more straightforward to identify which experiments and associated artifacts can be safely archived or deleted. 

1.  **For GenAI foundation models, implement token usage monitoring and cleanup**. For generative AI projects, monitor token usage and intermediate outputs, which can quickly accumulate. Implement automated cleanup of temporary prompts, completions, and generated content that isn't required for the final model. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Clean up Amazon SageMaker AI notebook instance resources](https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-cleanup.html) 
+  [Cataloging and analyzing your data with S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html) 
+  [What Is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) 
+  [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention) 
+  [Automate the cleanup of images by using lifecycle policies in Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) 
+  [AWS Systems Manager for Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) 
+  [What Is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) 
+  [Optimizing MLOps for Sustainability](https://aws.amazon.com/blogs/machine-learning/optimizing-mlops-for-sustainability/) 
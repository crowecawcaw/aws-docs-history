

# MLSUS06-BP02 Retrain only when necessary
<a name="mlsus06-bp02"></a>

 Because of model drift, robustness requirements, or new ground truth data being available, models usually need to be retrained. Instead of retraining arbitrarily, monitor your ML model in production, automate your model drift detection and only retrain when your model's predictive performance has fallen below defined KPIs. 

 **Desired outcome:** You will establish a data-driven approach to model retraining that optimizes computational resources while maintaining model performance. By implementing automated monitoring and drift detection systems, you can identify when your model's performance degrades below acceptable thresholds and retrain only when necessary. This reduces unnecessary computational overhead while verifying that your models remain accurate and relevant. 

 **Common anti-patterns:** 
+  Retraining models on a fixed schedule regardless of performance. 
+  Manual monitoring of model performance leading to delayed detection of drift. 
+  Retraining without clear performance thresholds or KPIs. 

 **Benefits of establishing this best practice:** 
+  Reduced computational resources and carbon footprint. 
+  Lower operational costs for model maintenance. 
+  More efficient use of data science team resources. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Machine learning models deployed in production environments naturally experience degradation in performance over time due to changes in data patterns, user behaviors, or business environments. This phenomenon, known as model drift, requires retraining to maintain optimal performance. However, retraining a model consumes significant computational resources, which impacts both operational costs and environmental sustainability. 

 By implementing automated monitoring systems and establishing clear performance thresholds, you can make data-driven decisions about when to retrain your models. This approach verifies that you're using computational resources efficiently while maintaining the effectiveness of your ML systems. Through continuous monitoring, you can detect both concept drift (changes in the relationship between input and output variables) and data drift (changes in the distribution of input data). 

 Your monitoring strategy should incorporate both technical metrics (such as accuracy, precision, recall) and business-relevant KPIs that directly tie to organizational outcomes. By correlating these metrics with specific thresholds for retraining, you create a sustainable approach to model maintenance that optimizes both performance and resource utilization. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Determine key performance indicators**. Work with business stakeholders to identify minimum acceptable accuracy levels and maximum acceptable error rates for your models. These KPIs should directly connect to business outcomes and provide clear thresholds for when retraining becomes necessary. Consider both technical metrics (precision, recall, F1 score) and business metrics (conversion rates, user engagement, revenue impact) when establishing these thresholds. 

1.  **Monitor your model deployed in Production**. Implement [Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to continuously evaluate your deployed models. SageMaker AI Model Monitor provides capabilities for data quality monitoring, model quality monitoring, bias drift monitoring, and feature attribution drift monitoring. Configure alerts based on your established KPIs to automatically notify your team when performance begins to degrade. 

1.  **Set up baseline metrics**. Create a baseline of your model's performance metrics immediately after deployment. This serves as a reference point against which future performance can be measured. SageMaker AI Model Monitor can automatically generate these baselines from your training data or initial inference data. 

1.  **Configure drift detection thresholds**. Define specific threshold values that indicate when drift has occurred to a degree that warrants retraining. These thresholds should be based on your KPIs and statistical measures of data or concept drift. Configure [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) alarms to go off when these thresholds are exceeded. 

1.  **Automate your retraining pipelines**. Use [Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/), [AWS Step Functions for Amazon SageMaker AI](https://docs.aws.amazon.com/step-functions/latest/dg/connect-sagemaker.html), or third-party tools to create automated workflows that can be initiated when drift is detected. These pipelines should handle data preparation, model training, evaluation, and deployment with minimal manual intervention. 

1.  **Optimize retraining frequency**. Based on historical drift patterns, adjust monitoring sensitivity and retraining thresholds to optimize the frequency of retraining. Finding the right balance keeps models performant while minimizing computational overhead. 

1.  **Establish canary deployments**. When deploying retrained models, use [SageMaker AI deployment options](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails.html) like canary deployments to gradually shift traffic to the new model while monitoring performance, allowing for quick rollback if issues arise. 

1.  **Leverage enhanced bias and drift detection**. Use improved [SageMaker AI Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html) capabilities with enhanced bias detection, new fairness metrics, and better visualization tools to more accurately detect when retraining is necessary. 

1.  **Implement feedback loops for generative models**. Establish mechanisms to collect user feedback and engagement metrics to detect when outputs become less relevant or helpful. Use [Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/) for fine-tuning foundation models when drift is detected in generative applications. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Amazon SageMaker AI Model Monitor documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) 
+  [Amazon SageMaker AI Pipelines documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html) 
+  [Amazon SageMaker AI Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html) 
+  [Amazon SageMaker AI Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html) 
+  [AWS Step Functions for Data Science](https://docs.aws.amazon.com/step-functions/latest/dg/connect-sagemaker.html) 
+  [SageMaker AI Deployment Guardrails](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails.html) 
+  [SageMaker AI Governance](https://aws.amazon.com/sagemaker/ai/ml-governance/) 
+  [Optimizing MLOps for Sustainability](https://aws.amazon.com/blogs/machine-learning/optimizing-mlops-for-sustainability/) 

 **Related videos:** 
+  [SageMaker AI HyperPod: Revolutionizing Foundation Model Training with Resilience and Performance](https://aws.amazon.com/awstv/watch/c60e1437f63/) 
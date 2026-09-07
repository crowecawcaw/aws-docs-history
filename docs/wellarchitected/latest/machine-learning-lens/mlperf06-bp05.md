

# MLPERF06-BP05 Establish an automated re-training framework
<a name="mlperf06-bp05"></a>

 Monitor data and model predictions to identify errors due to data and concept drift. By implementing automated model re-training at scheduled intervals or when performance metrics reach defined thresholds, you can maintain model accuracy and effectiveness over time. This approach keeps your machine learning models relevant as data patterns evolve. 

 **Desired outcome:** You can detect when your deployed ML models experience data drift or performance degradation, and automatically run retraining processes. You establish mechanisms to monitor data statistics and ML inferences in production, allowing you to maintain high-quality predictions without manual intervention. Your models are consistently updated with new data, and model versions are properly tracked to maintain traceability and reproducibility. 

 **Common anti-patterns:** 
+  Waiting for model performance to fail catastrophically before initiating retraining. 
+  Manually monitoring model performance without automated alerts or prompts. 
+  Retraining on a fixed schedule regardless of model performance or data patterns. 
+  Lacking proper version control for retrained models. 
+  Not maintaining consistent evaluation metrics across model versions. 

 **Benefits of establishing this best practice:** 
+  Maintains model accuracy and relevance as data patterns evolve. 
+  Reduces manual intervention required to keep models performing optimally. 
+  Enables quick response to data drift and concept drift. 
+  Creates a documented, repeatable process for model updates. 
+  Provides consistent model quality through automated evaluation. 
+  Maximizes return on investment for machine learning solutions. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Establishing an automated retraining framework is crucial for maintaining ML model performance over time. As new data becomes available or as the underlying patterns in your data change, your models can drift and become less accurate. By implementing a systematic approach to model monitoring and retraining, you can verify that your ML solutions continue to deliver business value. 

 Avoid waiting for model performance to fail catastrophically before initiating retraining. Many organizations manually monitor model performance without automated alerts or prompts, retrain on a fixed schedule regardless of model performance or data patterns, lack proper version control for retrained models, and don't maintain consistent evaluation metrics across model versions. 

 Start by defining clear performance metrics for your models that align with your business objectives. These metrics should be continuously monitored in production to detect performance degradation. Additionally, monitor your input data for statistical changes that may indicate drift from the training distribution. When changes are detected, your automated framework should run retraining workflows. 

 The process should include data preparation, model training with both existing and new data, thorough evaluation, and controlled deployment. Each retrained model should be versioned appropriately to maintain traceability and allow for rollback if needed. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define model performance metrics**. Establish clear metrics that measure how well your model is performing relative to business objectives. These could include accuracy, precision, recall, F1 score, or custom domain-specific metrics. Verify that these metrics can be calculated automatically and regularly in your production environment. 

1.  **Configure monitoring systems**. Use [Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to continuously monitor the quality of your ML models in production. Set up data quality monitoring to detect drift in input features, model quality monitoring to track prediction quality, bias drift monitoring to detect changes in fairness metrics, and feature attribution drift to identify changes in feature importance. 

1.  **Establish retraining prompts**. Define the conditions that will initiate model retraining. These can include scheduled intervals based on business requirements, performance degradation beyond defined thresholds, detection of data drift above acceptable limits, and availability of new training data. Set up [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) alerts to notify or automatically run retraining workflows. 

1.  **Design retraining pipelines**. Create automated pipelines using [Amazon SageMaker AI Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html) that handle the entire retraining workflow, including data preparation, feature engineering, model training, evaluation, and deployment. For large-scale foundation model training or distributed workloads, leverage [Amazon SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html) which provides managed, resilient high-performance clusters with automatic health checks and PyTorch auto-resume capabilities for long-running training jobs. In your pipeline, include steps for validation against holdout data before deployment. 

1.  **Implement model versioning**. Use [Amazon SageMaker AI Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) to track and manage different versions of your models. As a result, you can recreate a model version if needed and provide traceability for your deployed models. Associate metadata with each version to document training data, hyperparameters, and performance metrics. 

1.  **Automate data processing for new training data**. Set up automated data processing workflows that prepare new data for training. Configure [Amazon S3](https://aws.amazon.com/s3/) event notifications to run Lambda functions or [AWS Step Functions](https://aws.amazon.com/step-functions/) workflows when new data becomes available. Use [Amazon SageMaker AI Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html) to manage features consistently across training and inference. 

1.  **Set up orchestration**. Use [AWS Step Functions Data Science SDK for SageMaker AI](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-python-sdk.html) to orchestrate complex ML workflows. Define each step in the workflow and configure alerts to initiate the process. For detecting new training data, combine [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) with Amazon CloudWatch Events to automatically start Step Function workflows. 

1.  **Implement deployment safeguards**. Use deployment techniques like blue-green deployment or canary releases to safely transition to new model versions. Monitor the performance of new models closely during initial deployment and configure automatic rollback if performance degrades. 

1.  **Create feedback loops**. Establish mechanisms to collect ground truth data from production to continually evaluate and improve your models. This might involve user feedback, delayed outcomes, or manual labeling processes for a subset of predictions. 

1.  **Document the retraining process**. Create comprehensive documentation for your retraining framework, including prompts, pipelines, evaluation criteria, and deployment strategies. This process fosters knowledge transfer and consistent application of the process. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html) 
+  [Amazon SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html) 
+  [Retraining Models on New Data](https://docs.aws.amazon.com/machine-learning/latest/dg/retraining-models-on-new-data.html) 
+  [Data and model quality monitoring with SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) 
+  [Train a Machine Learning Model (using AWS Step Functions)](https://docs.aws.amazon.com/step-functions/latest/dg/sample-train-model.html) 
+  [Amazon SageMaker AI Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html) 
+  [Model Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) 
+  [Best practices and design patterns for building machine learning workflows with Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/best-practices-and-design-patterns-for-building-machine-learning-workflows-with-amazon-sagemaker-pipelines/) 
+  [Create SageMaker AI Pipelines for training, consuming and monitoring your batch use cases](https://aws.amazon.com/blogs/machine-learning/create-sagemaker-pipelines-for-training-consuming-and-monitoring-your-batch-use-cases/) 
+  [Launch Amazon SageMaker AI Autopilot experiments directly from within Amazon SageMaker AI Pipelines to easily automate MLOps workflows](https://aws.amazon.com/blogs/machine-learning/automating-complex-deep-learning-model-training-using-amazon-sagemaker-debugger-and-aws-step-functions/) 

 **Related videos:** 
+  [Automating Machine Learning Workflows: Leveraging Amazon SageMaker AI Pipelines and Autopilot for Efficient Model Development and Deployment](https://aws.amazon.com/awstv/watch/f2ed03696ea/) 

 **Related examples:** 
+  [Amazon SageMaker AI MLOps Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/63069e26-921c-4ce1-9cc7-dd882ff62575/en-US/lab6-mlops) 
+  [Amazon SageMaker AI MLOps](https://github.com/aws-samples/mlops-amazon-sagemaker-devops-with-ml) 
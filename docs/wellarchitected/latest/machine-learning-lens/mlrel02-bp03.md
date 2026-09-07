

# MLREL02-BP03 Automate managing data changes
<a name="mlrel02-bp03"></a>

 Effective management of machine learning training data changes is crucial for maintaining model reproducibility and providing consistent performance over time. By implementing automated version control for training data, you can precisely recreate a model version when needed and maintain a clear audit trail of data transformations. 

 **Desired outcome:** You establish automated processes for tracking and managing changes to your training data using version control technology. You gain the ability to reproduce model versions exactly as they were originally created, track data lineage through your ML pipeline, and maintain consistent model performance across deployments. Your ML operations become more reliable, transparent, and compatible with governance requirements. 

 **Common anti-patterns:** 
+  Manually tracking data versions in spreadsheets or documentation. 
+  Storing multiple versions of datasets with inconsistent naming conventions. 
+  Neglecting to record relationships between datasets and resulting models. 
+  Not preserving feature engineering transformations applied to training data. 
+  Relying on ad-hoc backup processes instead of systematic version control. 

 **Benefits of establishing this best practice:** 
+  Enables reproducible machine learning by maintaining exact data version history. 
+  Improves troubleshooting by allowing precise recreation of model versions. 
+  Enhances collaboration among data scientists through shared version control. 
+  Provides audit trail for governance requirements. 
+  Reduces errors in model deployment by providing consistent training data. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Managing changes to training data is fundamental to maintaining reproducible machine learning models. As your data evolves through acquisition, cleaning, and feature engineering, implementing automated version control allows you to track these changes systematically. This provides confidence that you can recreate any model version precisely when needed, which is essential for troubleshooting, compliance alignment, and proviidng consistent performance. 

 By implementing automated data versioning, you create a traceable history of your training data that integrates seamlessly with your ML pipeline. This approach mirrors software development best practices by treating data as a critical asset requiring the same level of version control as code. When data changes occur, whether through new acquisitions or transformations, your versioning system automatically captures these changes, making it possible to track model lineage from training data to deployment. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement a data version control system**. Begin by setting up a data version control system that can handle ML datasets efficiently. Tools like Git LFS, DVC (Data Version Control), or AWS solutions can be used to track changes in your training datasets. These tools provide mechanisms to capture dataset metadata and references without storing the entire dataset in the version control repository. 

1.  **Establish a data management strategy**. Define clear workflows for how data should be versioned, including naming conventions, branching strategies, and metadata requirements. Document how data should flow through your ML pipeline and how versions will be tracked at each stage. 

1.  **Use AWS MLOps Framework**. Implement the [AWS MLOps Framework](https://aws.amazon.com/sagemaker/ai/mlops/) to establish a standardized interface for managing ML pipelines. This framework works with both Amazon Machine Learning services and third-party services, providing a comprehensive solution for ML operations. The framework allows you to upload trained models (bring your own model), configure pipeline orchestration, and monitor operations—all while maintaining version control of data assets. 

1.  **Integrate with SageMaker AI Model Registry**. Use [Amazon SageMaker AI Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) to track model versions and their associated artifacts. Model Registry maintains comprehensive records of model lineage, including which datasets were used for training and validation, preserving the connection between models and their source data. 

1.  **Establish CI/CD for ML pipelines**. Set up continuous integration and continuous deployment (CI/CD) pipelines specifically designed for ML workflows using [Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/). This assists you to version and test changes to both code and data properly before moving to production. 

1.  **Create reproducible training environments**. Use container technology to package your training environment along with references to specific data versions. [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) provides mechanisms to create reproducible training jobs that can reference specific versions of your datasets stored in [Amazon S3](https://aws.amazon.com/s3/). 

1.  **Implement data quality monitoring**. Set up automated monitoring of data quality metrics to detect drift or anomalies in incoming data. Tools like [Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) can identify when new data differs from the baseline training data, allowing you to make informed decisions about model retraining. 

1.  **Configure automated testing**. Implement automated tests that validate data consistency and model performance when data versions change. This verifies that new data meets quality standards before being used in training or inference. 

1.  **Document data versioning procedures**. Create comprehensive documentation that describes your data versioning strategy, including how to retrieve specific versions of datasets and how to match models with their corresponding training data versions. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Implement MLOps](https://docs.aws.amazon.com/sagemaker/latest/dg/mlops.html) 
+  [Model Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) 
+  [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/) 
+  [Data and model quality monitoring with Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) 
+  [Amazon SageMaker AI Pipelines Brings DevOps Capabilities to your Machine Learning Projects](https://aws.amazon.com/blogs/machine-learning/promote-pipelines-in-a-multi-environment-setup-using-amazon-sagemaker-model-registry-hashicorp-terraform-github-and-jenkins-ci-cd/) 
+  [Building, automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/) 
+  [Fully managed MLflow 3.0 on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/accelerating-generative-ai-development-with-fully-managed-mlflow-3-0-on-amazon-sagemaker-ai/) 

 **Related videos:** 
+  [Implementing End-to-End MLOps Solutions with Amazon SageMaker AI](https://aws.amazon.com/awstv/watch/5057107a7fc/) 
+  [Accelerate production for gen AI using Amazon SageMaker AI MLOps & FMOps](https://www.youtube.com/watch?v=-3Otl7GVeCc) 
+  [Deliver high-performance ML models faster with MLOps tools](https://www.youtube.com/watch?v=T9llSCYJXxc) 

 **Related examples:** 
+  [Amazon SageMaker AI secure MLOps](https://github.com/aws-samples/amazon-sagemaker-secure-mlops) 
+  [ML Pipelines using Amazon SageMaker AI](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops/sm-mlflow_pipelines) 
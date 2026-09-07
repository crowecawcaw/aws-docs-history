

# MLPERF04-BP04 Establish feature statistics
<a name="mlperf04-bp04"></a>

 Establishing key statistics to measure changes in data that affect model outcomes is crucial for maintaining ML model performance. By analyzing feature importance and sensitivity, you can select the most critical features to monitor and detect when data drifts outside acceptable ranges so you can determine when model retraining is necessary. 

 **Desired outcome:** You establish a robust monitoring system that tracks key statistics for the most influential features in your machine learning models. You can detect data drift that could impact model performance, allowing for timely model retraining decisions based on quantitative measures rather than intuition. Your monitoring system alerts you when important features drift outside their expected statistical ranges, providing continuous model reliability and performance. 

 **Common anti-patterns:** 
+  Monitoring features equally without considering their relative importance to model outcomes. 
+  Failing to establish baseline statistics for important features before deploying models. 
+  Not setting appropriate thresholds for data drift alerts. 
+  Monitoring only model outputs without analyzing input feature distributions. 
+  Neglecting to perform sensitivity analysis to understand model behavior at decision boundaries. 

 **Benefits of establishing this best practice:** 
+  Early detection of data quality issues that could affect model performance. 
+  Reduced model performance degradation through timely retraining. 
+  Greater understanding of which features most impact model predictions. 
+  Improved model reliability in production environments. 
+  Enhanced ability to explain model behavior and decision boundaries to stakeholders. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Establishing feature statistics is essential for maintaining model performance over time. As real-world data evolves, your model's predictive power can deteriorate if the data drift exceeds certain thresholds. By focusing on the most influential features and understanding your model's sensitivity to changes in these features, you can create an effective monitoring strategy. 

 Start by analyzing which features have the greatest impact on your model's predictions through feature importance analysis. Then establish baseline statistics for these critical features using your training data. Monitor these statistics in production, comparing them to your baseline, and set up alerts when deviations occur. This approach allows you to proactively address potential model performance issues before they impact your business outcomes. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Analyze feature distributions with Data Wrangler**. Use [Amazon SageMaker AI Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-analyses.html) to perform exploratory data analysis on your dataset. Examine the distribution of each feature, identify outliers, and understand relationships between features. Data Wrangler provides visualizations such as histograms, scatter plots, and correlation matrices to understand your data's characteristics before training. 

1.  **Train your model with proper tracking**. When training your model, capture metadata about the training process using [SageMaker AI Managed MLFlow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html). This can establish a baseline for comparison and enables reproducibility of your experiments. Track key metrics, parameters, and the training dataset version to maintain a complete record of model development. 

1.  **Determine feature importance**. After training your model, analyze which features have the greatest impact on predictions. Use built-in feature importance methods in SageMaker AI, such as SHAP (SHapley Additive exPlanations) values or permutation importance. Alternatively, use model-specific methods like feature importance in tree-based models or coefficient magnitudes in linear models. 

1.  **Perform sensitivity analysis**. Map out regions in feature space where predictions change abruptly or remain invariant. Focus particularly on features near decision boundaries where small changes can alter model outputs. Use [Amazon SageMaker AI Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-detect-data-bias.html) to analyze how variations in input features affect predictions and understand which features require the closest monitoring. 

1.  **Check for data bias**. Use Amazon SageMaker AI Clarify to analyze your dataset for potential biases. Imbalances or biases in your training data can lead to poor generalization and unfair predictions. Identify and address these issues before deploying your model to create ethical and reliable ML systems. 

1.  **Establish monitoring baseline**. Configure [Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to create a baseline from your training data. This baseline captures the expected statistical properties of your features, including distributions, ranges, and relationships. SageMaker AI automatically analyzes and creates constraints for each feature based on the training data. 

1.  **Configure data quality monitoring**. Set up SageMaker AI Model Monitor to continuously evaluate production data against your established baseline. Configure monitoring schedules based on your application's requirements—hourly, daily, or weekly. Define thresholds for acceptable deviation from the baseline for each important feature. 

1.  **Implement data drift detection**. Configure alerts to notify you when important features drift outside their acceptable statistical ranges. Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to set up alarms that run when drift metrics exceed thresholds. This enables timely intervention when data quality issues arise. 

1.  **Create model retraining prompts**. Establish criteria for when to retrain your model based on data drift metrics. For example, if multiple important features show drift, or if a single critical feature drifts beyond a certain threshold, run the model retraining process. 

1.  **Set up continuous feedback loop**. Implement a system to continuously gather new labeled data for model retraining. This verifies that your model can adapt to legitimate changes in data distribution over time. Use [AWS Step Functions](https://aws.amazon.com/step-functions/) to orchestrate workflows that include data collection, preprocessing, model training, and deployment. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Pre-training Data Bias](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-detect-data-bias.html) 
+  [Data and model quality monitoring with SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) 
+  [Data quality](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-quality.html) 
+  [Accelerate generative AI development using managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) 

 **Related videos:** 
+  [Prepare data for machine learning with ease, speed, and accuracy](https://www.youtube.com/watch?v=Wi3eJxfX754) 
+  [Detect machine learning (ML) model drift in production](https://www.youtube.com/watch?v=J9T0X9Jxl_w) 

 **Related examples:** 
+  [Lab 1. Feature Engineering](https://catalog.us-east-1.prod.workshops.aws/workshops/63069e26-921c-4ce1-9cc7-dd882ff62575/en-US/lab1-feature-engineering) 
+  [SageMaker AI Model Monitor Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor) 
+  [SageMaker AI Clarify Explainability Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-clarify) 
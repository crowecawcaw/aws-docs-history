

# RAIMON01-BP04 Create monitoring dashboards for operational visibility
<a name="raimon01-bp04"></a>

 Design role-based monitoring dashboards that present relevant system health, performance, and risk indicators tailored to each stakeholder group's responsibilities and expertise levels. Create technical dashboards for engineering teams that show detailed performance metrics, error rates, and component-level health indicators with capabilities for deep-dive analysis. Develop executive dashboards that present summary-level information about benefit realization, risk mitigation effectiveness, and overall system performance against business objectives. Implement governance dashboards for teams that track adherence to release criteria and incident response metrics with historical trending capabilities. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation considerations
<a name="implementation-considerations-94"></a>

1.  Map stakeholder dashboard requirements by role. For example, a healthcare AI system can create separate views for clinical staff showing patient outcomes, technical teams showing model performance, and executives showing system impact. Use QuickSight for dashboards and IAM for access control. 

1.  Create dashboards for performance metrics and have mechanisms for triggering alarms when threshold is met. For example, you can monitor each part of your Amazon Bedrock application using Amazon CloudWatch, which collects raw data and processes it into readable, near real-time metrics. You can graph the metrics using the CloudWatch console. You can also set alarms to watch for certain thresholds and send notifications or take actions when values exceed those thresholds. Amazon CloudWatch metric may include Bedrock Guardrails metrics like total requests intervened by guardrail for various reasons like denied topics, in appropriate content, sensitive information or context grounding concerns. Controlling CloudWatch metrics visibility by role is accomplished through AWS Identity and Access Management (IAM) policies. 

1.  When using Amazon SageMaker AI Model Monitor, Amazon SageMaker AI Model Dashboard can be used to track the performance of models as they make real-time predictions on live data. Use a dashboard to find models that violate thresholds you set for data quality, model quality, bias and explainability. 

1.  Data Quality: Compares live data to training data. If they diverge, your model's inferences may no longer be accurate. 

1.  Model Quality: Compares the predictions that the model makes with the actual Ground Truth labels that the model attempts to predict. 

1.  Bias Drift: Compares the distribution of live data to training data, which can also cause inaccurate predictions. 

1.  Feature Attribution/Explainability Drift: Compare the relative rankings of your features in training data versus live data, which could also be a result of bias drift. 

## Resources
<a name="resources-90"></a>

 **Related documents** 
+  [Data quality](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-quality.html) 
+  [Model quality](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality.html) 
+  [Bias drift for models in production](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-bias-drift.html) 
+  [Feature attribution drift for models in production](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-feature-attribution-drift.html) 
+  [Implement safeguards for your application by associating a guardrail with your agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-guardrail.html) 
+  [Monitor Amazon Bedrock Guardrails using CloudWatch metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-guardrails-cw-metrics.html) 
+  [Amazon SageMaker AI Model Dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard.html) 
+  [Automated monitoring of your machine learning models with Amazon SageMaker AI Model Monitor and sending predictions to human review workflows using Amazon A2I](https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/) 
+  [Amazon SageMaker AI Model Monitor – Fully Managed Automatic Monitoring For Your Machine Learning Models](https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/) 
+  [ISO/IEC 42001:2023 A.6.2.6 AI system operation and monitoring](https://www.iso.org/standard/42001) 

 **Related tools** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
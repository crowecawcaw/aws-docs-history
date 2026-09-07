

# MLREL05-BP01 Allow automatic scaling of the model endpoint
<a name="mlrel05-bp01"></a>

 Implement capabilities that allow the automatic scaling of model endpoints. This improves the reliable processing of predictions to meet changing workload demands. Include monitoring on endpoints to identify a threshold that initiates the addition or removal of resources to support current demand. 

 **Desired outcome:** You can efficiently handle varying workload demands by implementing automatic scaling for your model endpoints. Your endpoints dynamically adjust resources based on real-time needs, providing consistent performance and availability without manual intervention. This results in reliable prediction processing, optimal resource utilization, and cost-effective operations. 

 **Common anti-patterns:** 
+  Manually scaling endpoints in response to traffic changes. 
+  Over-provisioning resources to handle peak loads at non-peak times. 
+  Neglecting to set up monitoring for endpoint performance. 
+  Ignoring traffic patterns when configuring scaling policies. 
+  Using fixed infrastructure that can't adapt to changing workloads. 

 **Benefits of establishing this best practice:** 
+  Improves reliability and availability of prediction services. 
+  Optimizes costs through dynamic resource allocation. 
+  Enhances user experience with consistent response times. 
+  Reduces operational overhead through automation. 
+  Strengthens ability to handle unexpected traffic spikes. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Automatic scaling of model endpoints is critical for maintaining reliable machine learning services in production. By implementing auto scaling, your endpoints can handle varying loads efficiently without manual intervention. This capability is especially important for applications with fluctuating traffic patterns or those that experience periodic spikes in demand. 

 When setting up automatic scaling, you need to consider appropriate metrics that trigger scaling actions, such as CPU utilization, memory usage, or request latency. Define appropriate thresholds for these metrics so that your system scale at the right time - not too early (which wastes resources) or too late (which impacts performance). 

 Monitoring is an essential component of an auto scaling solution. By implementing comprehensive monitoring, you gain visibility into endpoint performance and scaling operations, allowing you to optimize your configuration over time based on real usage patterns. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure automatic scaling for Amazon SageMaker AI endpoints**. Amazon SageMaker AI supports [automatic scaling (auto scaling)](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html) for your hosted models. SageMaker AI endpoints can be configured with auto scaling to maintain service availability as traffic increases. Automatic scaling automatically provisions new resources horizontally to handle increased user demand or system load. 

1.  **Set up appropriate scaling policies**. Define target metrics for scaling such as CPU utilization, memory usage, or request count. Configure appropriate minimum and maximum instance counts based on your expected traffic patterns and performance requirements. Consider implementing both scale-out policies (adding capacity when load increases) and scale-in policies (removing capacity when load decreases) to optimize resource utilization. 

1.  **Implement comprehensive monitoring**. Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to monitor the performance of your endpoint and collect metrics that can inform scaling decisions. Create dashboards to visualize endpoint performance and scaling activities. Set up alerts to notify you of issues or anomalies with your endpoints. 

1.  **Leverage SageMaker AI Serverless Inference**. For workloads with intermittent or unpredictable traffic patterns, consider using [Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html), which automatically scales compute capacity up and down based on traffic, avoiding the need to choose instance types or manage scaling policies. 

1.  **Utilize SageMaker AI Inference Recommender**. Before deploying models to production, use [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) to get recommendations on instance types and configurations that will best meet your performance and cost requirements, assisting you in optimizing your scaling policies. 

1.  **Implement load testing**. Perform load testing on your endpoints to understand how they behave under different traffic conditions. This information can fine-tune your scaling policies so that they're effective when real traffic increases occur. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Automatic scaling of Amazon SageMaker AI models](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html) 
+  [Deploy models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) 
+  [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) 
+  [Configuring autoscaling inference endpoints in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/configuring-autoscaling-inference-endpoints-in-amazon-sagemaker/) 
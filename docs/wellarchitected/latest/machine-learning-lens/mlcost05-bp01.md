

# MLCOST05-BP01 Use an appropriate deployment option
<a name="mlcost05-bp01"></a>

 Use the right deployment option for your machine learning models to optimize cost and performance based on your specific use case requirements. Select real-time inference for low latency applications, batch transform for large datasets, or edge deployment for applications that require local processing. 

 **Desired outcome:** You have an optimized model deployment strategy that balances performance and cost efficiency. You can choose the appropriate deployment option based on your specific use case requirements, whether that's real-time inference for low-latency applications, batch processing for large datasets, or edge deployment for scenarios requiring local processing. 

 **Common anti-patterns:** 
+  Using real-time endpoints for deployment scenarios regardless of traffic patterns. 
+  Overlooking serverless or asynchronous options when they would be more cost-effective. 
+  Deploying separate endpoints for each model when multiple models could be hosted more efficiently together. 
+  Running inference in the cloud when edge deployment would be more efficient for local data processing. 
+  Overprovisioning compute resources for inference endpoints. 

 **Benefits of establishing this best practice:** 
+  Cost optimization through selection of the most efficient deployment option for each use case. 
+  Improved performance by matching deployment options to specific latency requirements. 
+  Increased operational efficiency through managed inference services. 
+  Flexibility to handle varying inference workloads and traffic patterns. 
+  Simplified ML model management across cloud and edge environments. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 When deploying machine learning models, selecting the right deployment option is crucial for achieving optimal performance and cost efficiency. Amazon SageMaker AI provides multiple deployment options that can be tailored to your specific use case requirements. Real-time inference is ideal for applications requiring low latency responses, such as real-time recommendations or fraud detection. Batch transform is better suited for processing large datasets in offline mode, such as document processing or periodic scoring jobs. Edge deployment brings inference capabilities directly to edge devices, reducing latency and bandwidth requirements while enabling offline processing. 

 Consider the pattern of requests your application needs to handle. If you need consistent, low-latency responses for interactive applications with steady traffic, real-time inference is appropriate. If you process data in batches without immediate response requirements, batch transform offers cost efficiency. For applications with unpredictable or bursty traffic patterns, serverless inference can automatically scale to match demand while minimizing costs during idle periods. For workloads with large payloads or long processing times, asynchronous inference provides a queuing mechanism that improves efficiency. 

 Also consider resource utilization. Multi-model endpoints and multi-container endpoints enable you to optimize costs by sharing resources across multiple models or containers. This approach is particularly valuable when you have many models with variable usage patterns or complementary resource requirements. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Evaluate your inference requirements**. Determine your application's needs for latency, throughput, payload size, and traffic patterns. Consider whether your application requires real-time responses or can process data in batches. Assess if your models should run in the cloud or at the edge based on connectivity, latency requirements, and data privacy considerations. 

1.  **Use Amazon SageMaker AI for model deployment**. [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) offers a comprehensive set of deployment options to optimize price-performance for most use cases. It's a fully managed service that integrates with MLOps tools for effective model management in production with reduced operational burden. 

1.  **Select the appropriate inference option based on your use case**. Choose from several SageMaker AI inference options: 
   +  [Amazon SageMaker AI Real-time Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html) for low-latency, interactive applications requiring immediate responses 
   +  [Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) for workloads with intermittent or unpredictable traffic patterns 
   +  [Amazon SageMaker AI Asynchronous Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html) for large payload sizes, long processing times, or when immediate responses aren't required 
   +  [Amazon SageMaker AI Batch Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html) for offline processing of large datasets 

1.  **Implement multi-model endpoints for cost optimization**. Use [Amazon SageMaker AI Multi-Model Endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html) to deploy multiple models on a single endpoint with shared container resources. This approach improves endpoint utilization and reduces hosting costs compared to single-model endpoints. SageMaker AI manages the loading of models into memory and scales them based on traffic patterns. 

1.  **Deploy multiple containers on a single endpoint**. Implement [SageMaker AI multi-container endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-endpoints.html) to deploy multiple containers using different models or frameworks on a single endpoint. Run containers in sequence as an inference pipeline or access each container individually through direct invocation to improve endpoint utilization and optimize costs. 

1.  **Automate endpoint changes through a pipeline**. Use [Amazon SageMaker AI Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html) to automate the model deployment process. Create CI/CD pipelines that handle model training, evaluation, and deployment, enabling consistent and repeatable deployment processes. 

1.  **Monitor and optimize your deployment**. Implement continuous monitoring of your inference endpoints to track performance metrics, cost, and resource utilization. Use this data to fine-tune your deployment strategy and make adjustments as needed to optimize for cost efficiency and performance. 

1.  **Use AI-powered code generation for deployment automation**. Use AI-powered development tools like [Amazon Q Developer](https://aws.amazon.com/q/developer/) and [Kiro](https://kiro.ai/) to generate deployment scripts, automate infrastructure configuration, and accelerate the implementation of optimal deployment strategies. 

1.  **For generative AI workloads, consider deployment options for foundation models**. Evaluate specialized deployment options like [Amazon Bedrock](https://aws.amazon.com/bedrock/) for fully managed foundation models or [SageMaker AI JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart.html) for pre-trained models with optimized deployment configurations. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Deploy models for inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html) 
+  [Deploy models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) 
+  [Multi-model endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html) 
+  [Batch transform for inference with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html) 
+  [Hosting options](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-options.html) 
+  [Asynchronous inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html) 
+  [Model deployment at the edge with SageMaker AI Edge Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/edge.html) 
+  [Inference pipelines in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html) 

 **Related examples:** 
+  [SageMaker AI Serverless Inference Walkthrough](https://github.com/aws/amazon-sagemaker-examples/blob/main/serverless-inference/Serverless-Inference-Walkthrough.ipynb) 
+  [SageMaker AI Edge Manager Workshop](https://github.com/aws-samples/amazon-sagemaker-edge-manager-workshop) 
+  [SageMaker AI Asynchronous Inference Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/async-inference) 
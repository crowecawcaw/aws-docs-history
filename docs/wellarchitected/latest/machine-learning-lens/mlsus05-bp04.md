

# MLSUS05-BP04 Deploy multiple models behind a single endpoint
<a name="mlsus05-bp04"></a>

 Host multiple models behind a single endpoint to improve endpoint utilization. Sharing endpoint resources is more sustainable and less expensive than deploying a single model behind one endpoint. 

 **Desired outcome:** Your organization achieves greater efficiency in your model deployments by consolidating multiple models on shared infrastructure. This can reduce costs by increasing utilization of your endpoint resources, minimize environmental impact through reduced carbon emissions, and simplify your model deployment architecture. 

 **Common anti-patterns:** 
+  Deploying each model on its own dedicated endpoint regardless of utilization patterns. 
+  Over-provisioning resources for endpoints that serve infrequently accessed models. 
+  Creating separate infrastructure for similar models that could share resources. 

 **Benefits of establishing this best practice:** 
+  Reduced costs through better utilization of compute resources. 
+  Decreased carbon footprint by up to 90% compared to single-model deployments. 
+  Improved scalability for serving multiple models. 
+  Enhanced operational efficiency for inference workloads. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Model deployment architecture significantly impacts both cost and sustainability. By hosting multiple models behind a single endpoint, you can substantially improve resource utilization, reducing both expenses and environmental impact. Amazon SageMaker AI provides several approaches to implement this practice, each suitable for different scenarios depending on your model types, access patterns, and processing requirements. 

 Consider your workload characteristics when selecting a deployment approach. For a large collection of similar models that aren't accessed simultaneously, multi-model endpoints (MME) offer the most efficient solution. When you need to deploy different model types with varying framework requirements, multi-container endpoints (MCE) provide flexibility. For sequential processing workflows, inference pipelines allow you to chain preprocessing, prediction, and postprocessing steps. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Assess your model deployment needs**. Evaluate your current deployment architecture, focusing on model similarity, access patterns, and resource requirements. Identify opportunities to consolidate models based on these characteristics. 

1.  **Select the appropriate deployment method**. Choose from one of SageMaker AI's three approaches based on your workload requirements: 
   +  Multi-model endpoints for similar models with varied access patterns 
   +  Multi-container endpoints for heterogeneous models requiring different frameworks 
   +  Inference pipelines for sequential processing workflows 

1.  **Implement multi-model endpoints**. Use SageMaker AI's multi-model endpoint capability to host multiple models within a single container. This approach is ideal when you have many similar models that use the same framework and don't need to be accessed simultaneously. Configure the endpoint to dynamically load and unload models based on usage patterns to optimize memory utilization. 

1.  **Deploy multi-container endpoints**. When your models require different containers or frameworks, use [SageMaker AI multi-container endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-endpoints.html) to host up to 15 containers on a single endpoint. Configure each container with its specific model and framework requirements while sharing the underlying infrastructure resources. 

1.  **Create inference pipelines**. For workflows that require sequential processing, implement a [SageMaker AI inference pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html) to chain multiple containers. Define the sequence to handle preprocessing, model inference, and postprocessing steps as a unified flow, passing outputs from one container as inputs to the next. 

1.  **Monitor and optimize resource utilization**. Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to track endpoint metrics including CPU utilization, memory usage, and invocation patterns. Analyze this data to further optimize your deployment by adjusting instance types or scaling configurations based on actual usage. 

1.  **Implement cost tracking**. Set up cost allocation tags to monitor the efficiency gains from your consolidated endpoint deployment. Compare the costs before and after implementation to quantify savings and justify the architectural approach. 

1.  **Leverage modular deployment architectures**. Use [SageMaker AI multi-container endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-endpoints.html) and [inference pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html) to create modular inference architectures that can efficiently share resources across different model components and processing stages. 

1.  **Consider sustainability metrics**. Track carbon emission reductions resulting from your optimized deployment architecture. Using [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/), you can measure the environmental impact of your workloads and report on sustainability improvements. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Multi-model endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html) 
+  [Multi-container endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-endpoints.html) 
+  [Inference pipelines in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html) 
+  [Deploy models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) 
+  [Automatic scaling of Amazon SageMaker AI models](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html) 
+  [Asynchronous inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html) 
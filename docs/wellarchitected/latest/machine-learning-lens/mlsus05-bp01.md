

# MLSUS05-BP01 Align SLAs with sustainability goals
<a name="mlsus05-bp01"></a>

 Define service level agreements (SLAs) that support your sustainability goals while meeting your business requirements. Define SLAs to meet your business requirements, not exceed them. Make trade-offs that significantly reduce environmental impacts in exchange for acceptable decreases in service levels. 

 **Desired outcome:** You establish SLAs that balance business requirements with sustainability objectives, optimizing resource utilization while maintaining acceptable service levels. By implementing appropriate inference methods based on latency tolerance, availability needs, and response time requirements, you can reduce idle resources, minimize energy consumption, and lower your machine learning workload's environmental impact. 

 **Common anti-patterns:** 
+  Maintaining always-on inference endpoints for workloads with sporadic or batch processing needs. 
+  Setting unnecessarily stringent response time requirements when users can tolerate some latency. 
+  Configuring excessive redundancy beyond what's needed for business continuity. 

 **Benefits of establishing this best practice:** 
+  Reduced infrastructure costs through optimized resource utilization. 
+  Lower carbon footprint from minimized idle computing resources. 
+  Alignment of technical operations with organizational sustainability goals. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 When designing machine learning systems, your SLA choices directly impact resource consumption and environmental sustainability. By carefully analyzing your actual business requirements rather than automatically opting for maximum performance, you can identify opportunities to make sustainable trade-offs without compromising essential functionality. 

 Consider your application's true latency requirements, availability needs, and processing patterns. For example, if your users can tolerate a response time of seconds rather than milliseconds, asynchronous or batch processing approaches can dramatically reduce resource usage compared to always-on real-time endpoints. Similarly, if your application can gracefully handle occasional unavailability during instance failures, you can avoid overprovisioning redundant capacity. 

 The goal is to make conscious trade-offs that balance sustainability with business needs, focusing on what's truly required rather than defaulting to full time maximum performance. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Queue incoming requests and process them asynchronously**. If your users can tolerate some latency, deploy your model on [serverless](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) or [asynchronous endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html) to reduce resources that are idle between tasks and minimize the impact of load spikes. These options will automatically scale the instance or endpoint count to zero when there are no requests to process, so you only maintain an inference infrastructure when your endpoint is processing requests. 

1.  **Adjust availability**. If your users can tolerate some latency in the rare case of a failover, don't provision extra capacity. If an outage occurs or an instance fails, Amazon SageMaker AI [automatically attempts to distribute your instances across Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-best-practices.html#deployment-best-practices-availability-zones). Adjusting availability is an example of a [conscious trade off](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-as-a-non-functional-requirement.html) you can make to meet your sustainability targets. 

1.  **Adjust response time**. When you don't need real-time inference, use [SageMaker AI Batch Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html). Unlike a persistent endpoint, clusters are decommissioned when batch transform jobs finish so you don't continuously maintain an inference infrastructure. 

1.  **Conduct workload analysis**. Assess your machine learning workload's usage patterns and latency requirements to determine the most sustainable deployment option. Identify periods of peak activity versus low or no usage to determine if on-demand scaling is appropriate for your needs. 

1.  **Define sustainability metrics**. Establish key metrics to track your sustainability improvements, such as compute hours saved, idle time reduced, or overall carbon footprint reduction. Include these metrics alongside traditional performance indicators in your operational dashboards. 

1.  **Leverage enhanced serverless inference capabilities**. Use improved [SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) with increased memory configurations and better cold-start performance for variable workloads that don't require always-on infrastructure. 

1.  **Optimize large language model deployments with serverless deployment or batch processing**. For generative AI workloads using large language models (LLMs), consider serverless model inference through SageMaker AI or implement [Bedrock batch processing](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html) for non-interactive generation tasks like content summarization or document analysis to reduce resource consumption. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Asynchronous inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html) 
+  [Batch transform for inference with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html) 
+  [Deploy models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) 
+  [Multi-model endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html) 
+  [Best practices for deploying models on SageMaker AI Hosting Services](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-best-practices.html) 
+  [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) 
+  [Sustainability as a non-functional requirement](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-as-a-non-functional-requirement.html) 
+  **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
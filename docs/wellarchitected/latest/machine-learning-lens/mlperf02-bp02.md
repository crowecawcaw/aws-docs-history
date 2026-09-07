

# MLPERF02-BP02 Use purpose-built AI and ML services and resources
<a name="mlperf02-bp02"></a>

 Consider how the workload could be handled by pre-built AI services or ML resources. Better performance can often be delivered more efficiently by using pre-optimized components included in AI and ML managed services. Select an optimal mix of bespoke and pre-built components to meet the workload requirements. 

 **Desired outcome:** You achieve a balanced approach to your machine learning workloads by implementing purpose-built AI and ML services and resources. You leverage pre-built components where appropriate to accelerate development, reduce management overhead, and improve performance while maintaining the flexibility to create custom solutions where your business needs demand it. This approach optimizes both your team's productivity and the overall effectiveness of your AI/ML solutions. 

 **Common anti-patterns:** 
+  Building ML components from scratch when suitable pre-built solutions exist. 
+  Failing to evaluate the full range of AWS AI and ML services before starting development. 
+  Over-customizing solutions when standard services would adequately meet requirements. 
+  Underutilizing AWS marketplace solutions and pre-trained models. 
+  Not considering hybrid approaches that combine managed services with custom ML models. 

 **Benefits of establishing this best practice:** 
+  Accelerated time-to-market for ML solutions. 
+  Reduced operational overhead for maintaining ML infrastructure. 
+  Lower development costs through leveraging pre-built components. 
+  Access to continuously improved and updated AI technologies. 
+  Ability to focus resources on high-value business differentiators. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Implement purpose-built AI and ML services to focus on business outcomes rather than infrastructure management. AWS provides a comprehensive portfolio of AI services, ranging from ready-to-use APIs to fully customizable ML solutions. Each service addresses different levels of complexity and customization requirements. 

 When evaluating your ML workloads, assess which components could benefit from managed services. Tasks like image classification, regression, clustering, or time series forecasting can often be accomplished with [SageMaker AI built-in algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) without requiring custom algorithm development. For more specialized needs, you can leverage pre-trained models through services like [Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/) or develop custom models using [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/). 

 Resist the temptation to over-customize solutions when standard services would adequately meet requirements. Organizations often underutilize AWS marketplace solutions and pre-trained models, missing opportunities to accelerate development. The key is finding the right balance between using managed services for common ML tasks and building custom solutions for your unique business requirements. Consider hybrid approaches that combine managed services with custom ML models rather than pursuing an all-or-nothing strategy. 

 Consider your team's capabilities when making these decisions. If you lack specialized ML expertise, starting with fully managed AI services provides immediate value while your team builds skills. As your team's capabilities grow, you can selectively add custom components where they provide strategic advantage. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Assess your ML use cases and requirements**. Begin by clearly defining your business use cases and understanding the ML capabilities needed. Evaluate whether your requirements can be met by pre-built services or require custom development. Consider factors like accuracy requirements, latency needs, and the availability of training data. 

1.  **Learn about AWS managed AI services**. Determine whether [AWS managed AI services](https://aws.amazon.com/machine-learning/ai-services/) are applicable to the business use case. Understand how managed AWS AI services can relieve the burden of training and maintaining an ML pipeline. Use [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) to develop in the cloud and understand the roles and responsibilities needed to maintain the ML workload. Consider combining managed AI services with custom ML models built on Amazon SageMaker AI. 

1.  **Explore SageMaker AI built-in algorithms and automated ML capabilities**. Learn about [SageMaker AI built-in algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) for supervised learning tasks like classification, regression, and forecasting. Consider [SageMaker AI Autopilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html) for automated machine learning that handles data analysis, feature engineering, algorithm selection, and hyperparameter tuning. Explore [Amazon SageMaker AI JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) for pre-trained models across various ML domains, including [foundation models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models.html) that can be fine-tuned for your specific ML tasks. For enterprise environments, implement [SageMaker AI JumpStart Private Model Hubs](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs.html) to create curated repositories of both prebuilt and custom models with centralized governance and version management. 

1.  **Investigate marketplace solutions**. Learn about [SageMaker AI Algorithms and Models in AWS Marketplace](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-marketplace.html), a curated digital catalog that makes it simple for you to find, buy, deploy, and manage third-party software and services. Explore specialized algorithms or pre-trained models that might be relevant to your use case. 

1.  **Implement a hybrid approach where appropriate**. Design your ML architecture to leverage the most suitable services for each component. Use AWS managed services for standard ML tasks and focus custom development on business differentiators. This balanced approach optimizes both development efficiency and solution effectiveness. 

1.  **Establish a model evaluation framework**. Create a systematic process for evaluating pre-built models against your requirements. Define clear metrics for accuracy, latency, cost, and other relevant factors. Use this framework to make data-driven decisions about which components to build versus buy. 

1.  **Plan for operational integration**. Verify that your chosen ML services can integrate effectively with your existing systems and workflows. Design appropriate data pipelines, APIs, and monitoring systems to support your hybrid ML architecture. For development flexibility, leverage remote IDE connectivity to securely connect third-party developer environments such as VS Code to SageMaker AI Studio, enabling professional MLOps workflows while maintaining centralized governance. Consider security, regulatory adherence, and governance requirements when implementing these integrations. 

1.  **Optimize model performance and deployment**. Use [SageMaker AI model optimization](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize.html) capabilities including quantization, compilation, and speculative decoding to improve inference performance. Use [SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) to automatically benchmark and select optimal instance types, configurations, and parameters for your inference endpoints. Deploy using [SageMaker AI deployment options](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-deployment.html) such as real-time hosting, serverless inference, or batch transform based on your latency and throughput requirements. 

1.  **Implement model monitoring and governance**. Establish monitoring for model performance, data drift, and model drift using [SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html). Implement proper model versioning, A/B testing capabilities, and rollback procedures to maintain model quality and reliability in production environments. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Built-in algorithms and pretrained models in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) 
+  [SageMaker AI JumpStart Foundation Models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models.html) 
+  [Private curated hubs for foundation model access control in JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs.html) 
+  [Best practices for deploying models on SageMaker AI Hosting Services](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-best-practices.html) 
+  [Inference optimization for Amazon SageMaker AI models](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize.html) 
+  [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) 
+  [Model deployment options in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-deployment.html) 
+  [Distributed training optimization](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training-optimize.html) 
+  [SageMaker AI JumpStart pretrained models](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) 
+  [Machine Learning on AWS](https://aws.amazon.com/machine-learning/) 
+  [Architecture Best Practices for Machine Learning](https://aws.amazon.com/architecture/machine-learning/) 
+  [Data and model quality monitoring with SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) 
+  [SageMaker AI Algorithms and Models in AWS Marketplace](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-marketplace.html) 
+  [Docker containers for training and deploying models](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers.html) 
+  [Train a Model with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html) 

 **Related videos:** 
+  [Building and Deploying ML Models Fast with Amazon SageMaker AI JumpStart](https://www.youtube.com/watch?v=i4W7SfP6_38) 
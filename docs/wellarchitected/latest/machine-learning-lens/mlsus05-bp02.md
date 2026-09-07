

# MLSUS05-BP02 Use efficient silicon
<a name="mlsus05-bp02"></a>

 Choosing the right compute architecture for your machine learning workloads can significantly reduce energy consumption and carbon footprint while maintaining high performance. 

 **Desired outcome:** You select and deploy the most energy-efficient instance types for your machine learning workloads, resulting in reduced power consumption, lower costs, and a more sustainable ML infrastructure without compromising performance or functionality. 

 **Common anti-patterns:** 
+  Using general-purpose instances for specialized ML workloads. 
+  Selecting hardware based primarily on performance without considering power efficiency. 
+  Not optimizing ML models to work efficiently on specialized hardware. 

 **Benefits of establishing this best practice:** 
+  Reduced energy consumption by up to 60% with purpose-built ML accelerators. 
+  Decreased carbon footprint of your ML operations. 
+  Improved performance-per-watt metrics for your ML infrastructure. 
+  Better alignment with organizational sustainability goals. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 The energy efficiency of your ML infrastructure directly impacts both your operating costs and environmental footprint. By selecting purpose-built hardware accelerators designed specifically for ML workloads, you can achieve significant sustainability improvements while maintaining or even improving performance. 

 AWS has developed several specialized compute architectures optimized for different ML workload types, from training to inference. Each is designed to deliver maximum performance per watt to assist in meeting sustainability goals while effectively running your ML applications. These purpose-built solutions are particularly important for large-scale ML deployments where small efficiency improvements can result in substantial energy savings when scaled across your infrastructure. 

 When choosing compute resources for your ML workloads, consider not only the raw performance but also the energy efficiency of the hardware. The most powerful instance sometimes isn't the most sustainable choice, as matching the hardware capabilities to your specific workload requirements can often lead to better sustainability outcomes. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Assess your ML workload requirements**. Before selecting compute resources, analyze your ML workload characteristics including model size, batch processing capabilities, latency requirements, and throughput needs. This assessment can determine which specialized hardware will provide the optimal balance between performance and sustainability. 

1.  **Use AWS Graviton3 for CPU-based ML inference**. [AWS Graviton3](https://aws.amazon.com/ec2/graviton/) processors offer the best performance per watt in Amazon EC2, using up to 60% less energy than comparable instances. They deliver up to three times better performance compared to Graviton2 processors for ML workloads and support bfloat16, making them ideal for efficient CPU-based inference. 

1.  **Deploy AWS Inferentia for deep learning inference**. Amazon EC2 [Inf2 instances](https://aws.amazon.com/machine-learning/inferentia/) offer up to 50% better performance per watt over comparable Amazon EC2 instances. These instances are purpose-built to run deep learning models at scale and assist in meeting sustainability goals when deploying ultra-large models. 

1.  **Leverage AWS Trainium for ML training**. Amazon EC2 [Trn2 instances](https://aws.amazon.com/machine-learning/trainium/) based on custom-designed AWS Trainium chips offer up to 50% cost-to-train savings over comparable instances. When using a Trainium-based instance cluster, total energy consumption for training BERT Large from scratch is approximately 25% lower compared to same-sized clusters of comparable accelerated EC2 instances. 

1.  **Optimize your models for the target hardware**. Use the [AWS Neuron SDK](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/) to compile and optimize your ML models specifically for AWS Inferentia and Trainium chips. This verifies that your models can take full advantage of the hardware's power-efficient design and specialized ML acceleration features. 

1.  **Monitor and measure power efficiency**. Use Amazon CloudWatch metrics to track the resource utilization of your ML workloads. Compare performance-per-watt metrics across different instance types to validate your efficiency improvements and identify areas for further optimization. 

1.  **Leverage purpose-built training infrastructure**. For large-scale model training, use [SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html) which provides purpose-built infrastructure for distributed training with automatic checkpoint storage and recovery, optimizing resource utilization for long-running training jobs. 

1.  **Evaluate serverless options for intermittent workloads**. For ML inference workloads with variable traffic patterns, consider [Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) to automatically scale compute resources based on traffic, reducing idle resource waste. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Amazon EC2 instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) 
+  [Specifications for Amazon EC2 accelerated computing instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/accelerated-computing-instances.html#aws-inferentia-instances) 
+  [AWS Neuron SDK Documentation](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/) 
+  [What is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) 

 **Related examples:** 
+  [AWS Graviton Technical Guide](https://github.com/aws/aws-graviton-getting-started) 
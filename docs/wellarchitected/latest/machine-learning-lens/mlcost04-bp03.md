

# MLCOST04-BP03 Select local training for small scale experiments
<a name="mlcost04-bp03"></a>

 When developing machine learning models, choosing the right training environment is crucial for both cost efficiency and rapid experimentation. By evaluating whether to train your ML model locally or in the cloud, you can optimize your development workflow and appropriately match resources to the scale of your experiment. 

 **Desired outcome:** You can rapidly iterate on machine learning experiments with small datasets by training models locally, while having a clear path to scale up to cloud-based training when working with larger datasets. This approach enables faster development cycles during the experimentation phase and cost-effective scaling when required for production workloads. 

 **Common anti-patterns:** 
+  Deploying cloud-based training clusters regardless of dataset size. 
+  Using oversized compute instances for small-scale experimentation. 
+  Not considering the time and cost implications of repeatedly launching training clusters during the experimentation phase. 
+  Failing to right-size compute resources based on specific workload requirements. 

 **Benefits of establishing this best practice:** 
+  Reduced development costs during experimentation phases. 
+  Faster iteration cycles when testing various algorithms and configurations. 
+  Simplified workflow for early-stage development. 
+  Clear scaling path from local experimentation to production deployment. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 When developing machine learning models, you often need to experiment with multiple algorithms, configurations, and hyperparameters before finding an optimal solution. The choice between local training and cloud-based training significantly impacts both development speed and cost efficiency. 

 Local training is most advantageous during early experimentation phases when working with small datasets. This approach reduces the overhead of provisioning cloud resources and waiting for training clusters to spin up for each experiment iteration. Your development cycle becomes more agile as you can quickly test hypotheses and make adjustments without incurring additional cloud costs. 

 As your models and datasets grow in size and complexity, transitioning to cloud-based training becomes necessary. Cloud environments offer scalable computing resources that can handle large datasets and complex models that would be impractical to process on local machines. By right-sizing your compute instances based on your specific workload requirements, you can maintain cost efficiency while gaining the performance benefits of cloud infrastructure. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Evaluate your training requirements**. Before deciding on local or cloud-based training, assess your dataset size, model complexity, and computational requirements. Small datasets (typically under a few gigabytes) and simpler models are generally good candidates for local training, especially during initial experimentation. 

1.  **Set up Amazon SageMaker AI local mode**. When experimenting with small datasets, use Amazon SageMaker AI's local mode to train models directly on your notebook instance. This approach allows you to test and iterate on your code without provisioning separate training clusters. To implement local mode: 

   ```
   from sagemaker.estimator import Estimator
   
   estimator = Estimator(
       image_uri="your-container-image",
       role="your-sagemaker-role",
       instance_count=1,
       instance_type="local"
   )
   
   estimator.fit({"train": "s3://your-bucket/train-data"})
   ```

1.  **Use local development environment with SageMaker AI SDK**. For development outside of SageMaker AI notebooks, install the SageMaker AI Python SDK on your local machine. This allows you to develop and test locally while still having the ability to deploy models to AWS: 

   ```
   pip install sagemaker
   ```

1.  **Profile your workloads for cloud deployment**. As your models mature and datasets grow, prepare for cloud deployment by profiling your workloads. Identify memory usage, CPU and GPU requirements, and processing time to determine appropriate instance types for cloud-based training. 

1.  **Right-size cloud-based training clusters**. When moving to cloud training, select appropriate instance types based on your workload profiling. Consider factors such as: 
   +  Model architecture (CPU and GPU requirements) 
   +  Memory needs 
   +  Dataset size and I/O patterns 
   +  Training time constraints 
   +  Cost constraints 

1.  **Implement distributed training for large-scale workloads**. For large datasets or complex models, configure distributed training across multiple instances to reduce training time. 

1.  **Monitor and optimize cloud resource usage**. Regularly review your training job metrics to identify opportunities for optimization. Use SageMaker AI Experiments to track and compare resource utilization across different training configurations. 

1.  **Use enhanced local development capabilities**. Use improved SageMaker AI local mode with better debugging and monitoring capabilities, allowing for more efficient local experimentation before scaling to cloud resources. 

1.  **For generative AI workloads, use foundation models efficiently**. When working with generative AI and foundation models, consider using Amazon SageMaker AI JumpStart for local experimentation with smaller, distilled versions of foundation models before fine-tuning larger models in the cloud. This approach allows for rapid prototyping while managing costs effectively. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Model training](https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html) 
+  [AWS Pricing Calculator](https://calculator.aws/#/createCalculator/SageMaker AI) 
+  [What is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) 
+  [SageMaker AI Python SDK Documentation](https://sagemaker.readthedocs.io/en/stable/) 
+  [SageMaker AI JumpStart pretrained models](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) 
+  [Generative AI Cost Optimization Strategies](https://aws.amazon.com/blogs/enterprise-strategy/generative-ai-cost-optimization-strategies/) 

 **Related videos:** 
+  [Train with Amazon SageMaker AI on your local machine](https://www.youtube.com/watch?v=K3ngZKF31mc) 

 **Related examples:** 
+  [SageMaker AI Local Mode Examples](https://github.com/aws-samples/amazon-sagemaker-local-mode) 
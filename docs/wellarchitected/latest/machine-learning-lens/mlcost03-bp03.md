# MLCOST03-BP03 Use managed data processing capabilities

With managed data processing, you can use a simplified, managed
experience to run your data processing workloads, such as feature
engineering, data validation, model evaluation, and model
interpretation.

**Desired outcome:** By implementing
managed data processing capabilities, you can streamline your
machine learning workflow with fully managed infrastructure for data
preprocessing and postprocessing tasks. You gain the ability to run
processing jobs that integrate with popular frameworks while
maintaining operational efficiency, allowing your team to focus on
creating valuable ML models rather than managing infrastructure.

**Common anti-patterns:**

- Building and maintaining custom data processing infrastructure.
- Managing your own compute clusters for data processing tasks.
- Manually handling scaling, deployment, and cleanup of processing
  resources.
- Using inconsistent processing environments across development
  and production.

**Benefits of establishing this best
practice:**

- Reduced operational overhead with fully managed infrastructure.
- Simplified integration with popular ML frameworks and AWS
  services.
- Enhanced productivity by focusing on ML development rather than
  infrastructure management.
- Seamless integration with other SageMaker AI capabilities.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Amazon SageMaker AI Processing provides a managed solution for
running these data processing workloads. Instead of provisioning
and managing your own infrastructure, SageMaker AI handles the
provisioning, scaling, and cleanup of resources. Processing jobs
accept data from Amazon S3 as input and store processed results
back to S3 as output. You can use AWS-provided container images
that come pre-configured with popular data science frameworks, or
you can bring your own custom containers for specialized
processing needs.

By using SageMaker AI Processing, you can integrate data processing
steps seamlessly into your ML pipelines and create consistency
between development and production environments while reducing
operational overhead. This allows your data scientists and ML
engineers to focus on extracting insights from data rather than
managing infrastructure.

### Implementation steps

1. **Set up your processing job
   environment**. Create an Amazon SageMaker AI notebook
   instance or Studio environment from which you'll configure
   and launch your processing jobs. This provides an
   interactive environment for development and testing of your
   data processing scripts before scaling to larger datasets.
2. **Select or create a processing
   container**. Choose from SageMaker AI's built-in
   processing containers for frameworks like scikit-learn,
   PyTorch, TensorFlow, or Apache Spark. Alternatively, create
   a custom Docker container if you have specialized framework
   requirements. The container will include the runtime
   environment and dependencies needed for your processing
   tasks.
3. **Prepare your processing
   script**. Develop a script that runs within the
   processing container to perform your data transformation,
   feature engineering, model evaluation, or other processing
   tasks. This script should read input data, process it
   according to your requirements, and write output to the
   designated locations.
4. **Configure storage
   locations**. Set up Amazon S3 buckets to store your
   input data, processing scripts, and output results.
   SageMaker AI Processing jobs use S3 as the primary storage
   mechanism for exchanging data between steps in your ML
   workflow.
5. **Launch a processing job**.
   Use the SageMaker AI Python SDK or AWS console to configure and
   start your processing job. Specify parameters such as
   instance type, instance count, environment variables, and
   input and output configurations. SageMaker AI will provision
   the requested resources, run your processing script, and
   then automatically clean up the resources when the job
   completes.
6. **Monitor job progress and analyze
   results**. Track your processing job through the
   SageMaker AI console or API. Review logs to debug issues. Once
   completed, access the processed data in the specified S3
   output locations for use in subsequent ML workflow steps.
7. **Integrate with ML
   pipelines**. Incorporate your processing jobs into
   [SageMaker AI
   Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/") to create automated end-to-end ML
   workflows. This enables you to orchestrate data
   preprocessing, model training, evaluation, and deployment
   steps in a repeatable manner.
8. **Optimize resource utilization and
   costs**. Review processing job metrics to identify
   opportunities for optimizing instance selection and
   parallelization strategies. Consider using Spot instances
   for cost savings on non-time-sensitive processing jobs.
9. **Use enhanced processing
   capabilities**. Use SageMaker AI Processing with
   better integration to popular ML frameworks and enhanced
   monitoring capabilities for more efficient data processing
   workflows.
10. **Use AI-powered code generation for
    data processing**. Use AI-powered development tools
    like
    [Amazon Q Developer](https://aws.amazon.com/q/developer/ "https://aws.amazon.com/q/developer/") and
    [Kiro](https://kiro.ai/ "https://kiro.ai/") to generate
    data processing scripts, automate pipeline creation, and
    accelerate the development of custom data transformation
    workflows.
11. **Implement data validation and
    quality checks**. Incorporate data validation steps
    in your processing jobs to check data quality before model
    training. Use SageMaker AI Clarify within processing jobs to
    detect bias in your datasets and implement model
    explainability.

## Resources

**Related documents:**

- [Data
  transformation workloads with SageMaker AI Processing](../../../sagemaker/latest/dg/processing-job.md "../../../sagemaker/latest/dg/processing-job.md")
- [CreateProcessingJob](../../../sagemaker/latest/APIReference/API_CreateProcessingJob.md "../../../sagemaker/latest/APIReference/API_CreateProcessingJob.md")
- [Managed
  Spot Training in Amazon SageMaker AI](../../../sagemaker/latest/dg/model-managed-spot-training.md "../../../sagemaker/latest/dg/model-managed-spot-training.md")
- [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/ "https://aws.amazon.com/sagemaker/feature-store/")
- [Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/ "https://aws.amazon.com/sagemaker/data-wrangler/")

**Related examples:**

- [Amazon SageMaker AI Processing jobs](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation/scikit_learn_data_processing_and_model_evaluation.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation/scikit_learn_data_processing_and_model_evaluation.html")
- [SageMaker AI
  Processing with Spark](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_processing/spark_distributed_data_processing "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_processing/spark_distributed_data_processing")

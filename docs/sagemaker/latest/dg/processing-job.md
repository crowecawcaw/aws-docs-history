

# Data transformation workloads with SageMaker Processing
<a name="processing-job"></a>

SageMaker Processing refers to SageMaker AI’s capabilities to run data pre and post processing, feature engineering, and model evaluation tasks on SageMaker AI's fully-managed infrastructure. These tasks are executed as [processing jobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProcessingJob.html). The following provides information and resources to learn about SageMaker Processing.

Using SageMaker Processing API, data scientists can run scripts and notebooks to process, transform, and analyze datasets to prepare them for machine learning. When combined with the other critical machine learning tasks provided by SageMaker AI, such as training and hosting, Processing provides you with the benefits of a fully managed machine learning environment, including all the security and compliance support built into SageMaker AI. You have the flexibility to use the built-in data processing containers or to bring your own containers for custom processing logic and then submit jobs to run on SageMaker AI managed infrastructure. 

**Note**  
 You can create a processing job programmatically by calling the [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html) API action in any language supported by SageMaker AI or by using the AWS CLI. For information on how this API action translates into a function in the language of your choice, see the [See Also](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html#API_CreateProcessingJob_SeeAlso) section of CreateProcessingJob and choose an SDK. As an example, for Python users, refer to the [Amazon SageMaker Processing](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_core.html) section of SageMaker Python SDK. Alternatively, see the full request syntax of [create\_processing\_job](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/create_processing_job.html) in the AWS SDK for Python (Boto3).

The following diagram shows how Amazon SageMaker AI spins up a Processing job. Amazon SageMaker AI takes your script, copies your data from Amazon Simple Storage Service (Amazon S3), and then pulls a processing container. The underlying infrastructure for a Processing job is fully managed by Amazon SageMaker AI. After you submit a processing job, SageMaker AI launches the compute instances, processes and analyzes the input data, and releases the resources upon completion. The output of the Processing job is stored in the Amazon S3 bucket you specified. 

**Note**  
Your input data must be stored in an Amazon S3 bucket. Alternatively, you can use Amazon Athena or Amazon Redshift as input sources.

![Running a processing job.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/Processing-1.png)


**Tip**  
To learn best practices for distributed computing of machine learning (ML) training and processing jobs in general, see [Distributed computing with SageMaker AI best practices](distributed-training-options.md).

## Use Amazon SageMaker Processing Sample Notebooks
<a name="processing-job-sample-notebooks"></a>

We provide two sample Jupyter notebooks that show how to perform data preprocessing, model evaluation, or both.

For a sample notebook that shows how to run scikit-learn scripts to perform data preprocessing and model training and evaluation with the SageMaker Python SDK for Processing, see [scikit-learn Processing](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation). This notebook also shows how to use your own custom container to run processing workloads with your Python libraries and other specific dependencies.

For a sample notebook that shows how to use Amazon SageMaker Processing to perform distributed data preprocessing with Spark, see [Distributed Processing (Spark)](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker_processing/spark_distributed_data_processing/sagemaker-spark-processing.ipynb). This notebook also shows how to train a regression model using XGBoost on the preprocessed dataset.

For instructions on how to create and access Jupyter notebook instances that you can use to run these samples in SageMaker AI, see [Amazon SageMaker notebook instances](nbi.md). After you have created a notebook instance and opened it, choose the **SageMaker AI Examples** tab to see a list of all the SageMaker AI samples. To open a notebook, choose its **Use** tab and choose **Create copy**.

## Monitor Amazon SageMaker Processing Jobs with CloudWatch Logs and Metrics
<a name="processing-job-cloudwatch"></a>

Amazon SageMaker Processing provides Amazon CloudWatch logs and metrics to monitor processing jobs. CloudWatch provides CPU, GPU, memory, GPU memory, and disk metrics, and event logging. For more information, see [Amazon SageMaker AI metrics in Amazon CloudWatch](monitoring-cloudwatch.md) and [CloudWatch Logs for Amazon SageMaker AI](logging-cloudwatch.md).
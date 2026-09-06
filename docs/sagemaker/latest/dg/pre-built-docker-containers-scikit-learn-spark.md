

# Accessing Docker Images for Scikit-learn and Spark ML
<a name="pre-built-docker-containers-scikit-learn-spark"></a>

SageMaker AI provides prebuilt Docker images that install the scikit-learn and Spark ML libraries. These libraries also include the dependencies needed to build Docker images that are compatible with SageMaker AI using the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable). With the SDK, you can use scikit-learn for machine learning tasks and use Spark ML to create and tune machine learning pipelines. For instructions on installing and using the SDK, see [SageMaker Python SDK](https://github.com/aws/sagemaker-python-sdk#installing-the-sagemaker-python-sdk). 

You can also access the images from an Amazon ECR repository in your own environment.

Use the following commands to find out which versions of the images are available. For example, use the following to find the available `sagemaker-sparkml-serving` image in the `ca-central-1` Region:

```
aws \
    ecr describe-images \
    --region ca-central-1 \
    --registry-id 341280168497 \
    --repository-name sagemaker-sparkml-serving
```

## Accessing an image from the SageMaker AI Python SDK
<a name="pre-built-docker-containers-scikit-learn-spark-sdk"></a>

The following table contains links to the GitHub repositories with the source code for the scikit-learn and Spark ML containers. The table also contains links to instructions that show how use these containers with Python SDK ModelTrainers to run your own training algorithms and hosting your own models. 


| Library | Prebuilt Docker Image Source Code | Instructions | 
| --- | --- | --- | 
| scikit-learn | [SageMaker AI Scikit-learn Containers](https://github.com/aws/sagemaker-scikit-learn-container) | [Using Scikit-learn with the Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) | 
| Spark ML | [SageMaker AI Spark ML Serving Containers](https://github.com/aws/sagemaker-sparkml-serving-container) | [SparkML Python SDK Documentation](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_core.html) | 

For more information and links to github repositories, see [Resources for using Scikit-learn with Amazon SageMaker AI](sklearn.md) and [Resources for using SparkML Serving with Amazon SageMaker AI](sparkml-serving.md).

## Specifying the Prebuilt Images Manually
<a name="pre-built-containers-scikit-learn-manual"></a>

If you are not using the SageMaker Python SDK and one of its ModelTrainers to manage the container, you have to retrieve the relevant prebuilt container manually. The SageMaker AI prebuilt Docker images are stored in Amazon Elastic Container Registry (Amazon ECR). You can push or pull them using their fullname registry addresses. SageMaker AI uses the following Docker Image URL patterns for scikit-learn and Spark ML:
+ `{{<ACCOUNT_ID>}}.dkr.ecr.{{<REGION_NAME>}}.amazonaws.com/sagemaker-scikit-learn:{{<SCIKIT-LEARN_VERSION>}}-cpu-py{{<PYTHON_VERSION>}}`

  For example, `{{746614075791}}.dkr.ecr.{{us-west-1}}.amazonaws.com/{{sagemaker-scikit-learn:1.2-1-cpu-py3}}`
+ `{{<ACCOUNT_ID>}}.dkr.ecr.{{<REGION_NAME>}}.amazonaws.com/sagemaker-sparkml-serving:{{<SPARK-ML_VERSION>}}`

  For example, `{{341280168497}}.dkr.ecr.{{ca-central-1}}.amazonaws.com/{{sagemaker-sparkml-serving:2.4}}`

For account IDs and AWS Region names, see [Docker Registry Paths and Example Code](https://docs.aws.amazon.com/sagemaker/latest/dg-ecr-paths/sagemaker-algo-docker-registry-paths).
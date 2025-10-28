# Model Hosting FAQs

Refer to the following FAQ items for answers to commonly asked questions about SageMaker AI Inference Hosting.

## General Hosting

The following FAQ items answer common general questions for SageMaker AI Inference.

A: After you build and train models, Amazon SageMaker AI provides four options to deploy
them so you can start making predictions. Real-Time Inference is suitable for
workloads with millisecond latency requirements, payload sizes up to 25 MB, and
processing times of up to 60 seconds for regular responses and 8 minutes for streaming responses. Batch Transform is ideal for offline
predictions on large batches of data that are available up front. Asynchronous Inference is
designed for workloads that do not have sub-second latency requirements, payload
sizes up to 1 GB, and processing times of up to 60 minutes. With Serverless Inference, you can
quickly deploy machine learning models for inference without having to configure
or manage the underlying infrastructure, and you pay only for the compute
capacity used to process inference requests, which is ideal for intermittent
workloads.

If you
want to process requests in batches, you might want to choose Batch Transform.
Otherwise, if you want to receive inference for each request to your model, you
might want to choose Asynchronous Inference, Serverless Inference, or Real-Time Inference. You can choose Asynchronous Inference
if you have long processing times or large payloads and want to queue requests.
You can choose Serverless Inference if your workload has unpredictable or intermittent traffic.
You can choose Real-Time Inference if you have sustained traffic and need lower
and consistent latency for your requests.

A: To optimize your costs with SageMaker AI Inference, you should choose the right
hosting option for your use case. You can also use Inference features such as
[Amazon SageMaker AI Savings Plans](https://aws.amazon.com/savingsplans/ml-pricing/ "https://aws.amazon.com/savingsplans/ml-pricing/"),
model optimization with
[SageMaker Neo](neo.md "neo.md"),
[Multi-Model Endpoints](multi-model-endpoints.md "multi-model-endpoints.md")
and [Multi-Container Endpoints](multi-container-endpoints.md "multi-container-endpoints.md"),
or autoscaling. For tips on how to
optimize your Inference costs, see [Inference cost optimization best practices](inference-cost-optimization.md "inference-cost-optimization.md").

A: You should use Amazon SageMaker Inference Recommender if you need recommendations for the right
endpoint configuration to improve performance and reduce costs. Previously, data
scientists who wanted to deploy their models had to run manual benchmarks to
select the right endpoint configuration. First, they had to select the right
machine learning instance type out of more than 70 available instance types
based on the resource requirements of their models and sample payloads, and then
optimize the model to account for differing hardware. Then, they had to conduct
extensive load tests to validate that latency and throughput requirements were
met and that the costs were low. Inference Recommender eliminates this complexity by helping
you do the following:

- Get started in minutes with an instance recommendation.
- Conduct load tests across instance types to get recommendations on
  your endpoint configuration within hours.
- Automatically tune container and model server parameters as well as
  perform model optimizations for a given instance type.
  A: SageMaker AI endpoints are HTTP REST endpoints that use a containerized web server,
  which includes a model server. These containers are responsible for loading up
  and serving requests for a machine learning model. They implement a web server
  that responds to `/invocations` and `/ping` on port

8080.

Common model servers include TensorFlow Serving, TorchServe and Multi Model Server.
SageMaker AI framework containers have these model servers built in.

A: Everything in SageMaker AI Inference is containerized. SageMaker AI provides managed containers for popular frameworks
such as TensorFlow, SKlearn, and HuggingFace. For a comprehensive updated list of those images, see
[Available Images](https://github.com/aws/deep-learning-containers/blob/master/available_images.md "https://github.com/aws/deep-learning-containers/blob/master/available_images.md").

Sometimes there are custom frameworks for which you might need to build a
container. This approach is known as _Bring Your Own
Container_ or _BYOC_. With the
BYOC approach, you provide the Docker image to set up your framework or library.
Then, you push the image to Amazon Elastic Container Registry (Amazon ECR) so that you can use the image with SageMaker AI.

Alternatively, instead of building an image from scratch, you can extend a container. You can take one of the
base images that SageMaker AI provides and add your dependencies on top of it in your Dockerfile.

A: SageMaker AI offers the capacity to bring your own trained framework model that you've
trained outside of SageMaker AI and deploy it on any of the SageMaker AI hosting options.

SageMaker AI requires you to package the model in a `model.tar.gz` file and
have a specific directory structure. Each framework has its own model structure
(see the following question for example structures). For more information, see
the SageMaker Python SDK documentation for [TensorFlow](https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/deploying_tensorflow_serving.html#deploying-directly-from-model-artifacts "https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/deploying_tensorflow_serving.html#deploying-directly-from-model-artifacts"), [PyTorch](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#bring-your-own-model "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#bring-your-own-model"), and [MXNet](https://sagemaker.readthedocs.io/en/stable/frameworks/mxnet/using_mxnet.html#deploy-endpoints-from-model-data "https://sagemaker.readthedocs.io/en/stable/frameworks/mxnet/using_mxnet.html#deploy-endpoints-from-model-data").

While you can choose from prebuilt framework images such as TensorFlow, PyTorch, and
MXNet to host your trained model, you can also build your own container to host
your trained models on SageMaker AI endpoints. For a walkthrough, see the example Jupyter
notebook [Building your own algorithm container](https://github.com/aws/amazon-sagemaker-examples/blob/main/advanced_functionality/scikit_bring_your_own/scikit_bring_your_own.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/advanced_functionality/scikit_bring_your_own/scikit_bring_your_own.ipynb").

A: SageMaker AI requires your model artifacts to be compressed in a `.tar.gz` file, or a _tarball_. SageMaker AI automatically extracts this `.tar.gz`
file into the `/opt/ml/model/` directory in your container. The tarball shouldn't contain any symlinks or unncessary files. If you are making use of one of the framework containers,
such as TensorFlow, PyTorch, or MXNet, the container expects your TAR structure to be as follows:

**TensorFlow**

````
model.tar.gz/
|--[model_version_number]/
|--variables
|--saved_model.pb code/
|--inference.py
|--requirements.txt ``` **PyTorch** ``` model.tar.gz/
|- model.pth
|- code/
|- inference.py
|- requirements.txt  # only for versions 1.3.1 and higher ``` **MXNet** ``` model.tar.gz/
|- model-symbol.json
|- model-shapes.json
|- model-0000.params
|- code/
|- inference.py
|- requirements.txt # only for versions 1.6.0 and higher ``` A: `ContentType` is the MIME type of the input data in the request body (the MIME type of the data you are sending to your endpoint). The model server uses the `ContentType` to determine if it can handle the type provided or not. `Accept` is the MIME type of the inference response (the MIME type of the data your endpoint returns). The model server uses the `Accept` type to determine if it can handle returning the type provided or not. Common MIME types include `text/csv`, `application/json`, and `application/jsonlines`. A: SageMaker AI passes any request onto the model container without modification. The container must contain the logic to deserialize the request. For information about the formats defined for built-in algorithms, see [Common Data Formats for Inference](cdf-inference.md "cdf-inference.md"). If you are building your own container or using a SageMaker AI Framework container, you can include the logic to accept a request format of your choice. Similarly, SageMaker AI also returns the response without modification, and then the client must deserialize the response. In case of the built-in algorithms, they return responses in specific formats. If you are building your own container or using a SageMaker AI Framework container, you can include the logic to return a response in the format you choose. Use the [Invoke Endpoint](../APIReference/API_runtime_InvokeEndpoint.md "../APIReference/API_runtime_InvokeEndpoint.md") API call to make inference against your endpoint. When passing your input as a payload to the `InvokeEndpoint` API, you must provide the correct type of input data that your model expects. When passing a payload in the `InvokeEndpoint` API call, the request bytes are forwarded directly to the model container. For example, for an image, you may use `application/jpeg` for the `ContentType`, and make sure that your model can perform inference on this type of data. This applies for JSON, CSV, video, or any other type of input with which you may be dealing. Another factor to consider is payload size limits. The payload limits are 25 MB for real-time endpoints and 4 MB for serverless endpoints. You can split your video into multiple frames and invoke the endpoint with each frame individually. Alternatively, if your use case permits, you can send the whole video in the payload using an asynchronous endpoint, which supports up to 1 GB payloads. For an example that showcases how to run computer vision inference on large videos with Asynchronous Inference, see this [blog post](https://aws.amazon.com/blogs/machine-learning/run-computer-vision-inference-on-large-videos-with-amazon-sagemaker-asynchronous-endpoints/ "https://aws.amazon.com/blogs/machine-learning/run-computer-vision-inference-on-large-videos-with-amazon-sagemaker-asynchronous-endpoints/"). ## Real-Time Inference The following FAQ items answer common questions for SageMaker AI Real-Time Inference. A: You can create a SageMaker AI endpoint through AWS-supported tooling such as the AWS SDKs, the SageMaker Python SDK, the AWS Management Console, AWS CloudFormation, and the AWS Cloud Development Kit (AWS CDK). There are three key entities in endpoint creation: a SageMaker AI model, a SageMaker AI endpoint configuration, and a SageMaker AI endpoint. The SageMaker AI model points towards the model data and image you are using. The endpoint configuration defines your production variants, which might include the instance type and instance count. You can then use either the [create\_endpoint](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_endpoint "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_endpoint") API call or the [.deploy()](https://sagemaker.readthedocs.io/en/stable/api/inference/model.html "https://sagemaker.readthedocs.io/en/stable/api/inference/model.html") call for SageMaker AI to create an endpoint using the metadata from your model and endpoint configuration. A: No, you can use the various AWS SDKs (see [Invoke](../APIReference/API_runtime_InvokeEndpoint.md#API_runtime_InvokeEndpoint_SeeAlso "../APIReference/API_runtime_InvokeEndpoint.md#API_runtime_InvokeEndpoint_SeeAlso")/[Create](../APIReference/API_CreateEndpoint.md#API_CreateEndpoint_SeeAlso "../APIReference/API_CreateEndpoint.md#API_CreateEndpoint_SeeAlso") for available SDKs) or even call the corresponding web APIs directly. A: A Multi-Model Endpoint is a Real-Time Inference option that SageMaker AI provides. With Multi-Model Endpoints, you can host thousands of models behind one endpoint. [Multi Model Server](https://github.com/awslabs/multi-model-server "https://github.com/awslabs/multi-model-server") is an open-source framework for serving machine learning models. It provides the HTTP front-end and model management capabilities required by multi-model endpoints to host multiple models within a single container, load models into and unload models out of the container dynamically, and perform inference on a specified loaded model. A: SageMaker AI Real-Time Inference supports various model deployment architecture such as Multi-Model Endpoints, Multi-Container Endpoints, and Serial Inference Pipelines. [Multi-Model Endpoints (MME)](multi-model-endpoints.md "multi-model-endpoints.md") – MME allows customers to deploy 1000s of hyper‐personalized models in a cost effective way. All the models are deployed on a shared‐resource fleet. MME works best when the models are of similar size and latency and belong to the same ML framework. These endpoints are ideal for when you have don’t need to call the same model at all times. You can dynamically load respective models onto the SageMaker AI endpoint to serve your request. [Multi-Container Endpoints (MCE)](multi-container-endpoints.md "multi-container-endpoints.md") – MCE allows customers to deploy 15 different containers with diverse ML frameworks and functionalities with no cold starts while only using one SageMaker endpoint. You can directly invoke these containers. MCE is best for when you want to keep all the models in memory. [Serial Inference Pipelines (SIP)](inference-pipelines.md "inference-pipelines.md") – You can use SIP to chain together 2‐15 containers on a single endpoint. SIP is mostly suitable for combining preprocessing and model inference in one endpoint and for low latency operations. ## Serverless Inference The following FAQ items answer common questions for Amazon SageMaker Serverless Inference. A: [Deploy models with Amazon SageMaker Serverless Inference](serverless-endpoints.md "serverless-endpoints.md") is a purpose-built serverless model serving option that makes it easy to deploy and scale ML models. Serverless Inference endpoints automatically start compute resources and scale them in and out depending on traffic, eliminating the need for you to choose instance type, run provisioned capacity, or manage scaling. You can optionally specify the memory requirements for your serverless endpoint. You pay only for the duration of running the inference code and the amount of data processed, not for idle periods. A: Serverless Inference simplifies the developer experience by eliminating the need to provision capacity up front and manage scaling policies. Serverless Inference can scale instantly from tens to thousands of inferences within seconds based on the usage patterns, making it ideal for ML applications with intermittent or unpredictable traffic. For example, a chatbot service used by a payroll processing company experiences an increase in inquiries at the end of the month while traffic is intermittent for rest of the month. Provisioning instances for the entire month in such scenarios is not cost-effective, as you end up paying for idle periods. Serverless Inference helps address these types of use cases by providing you automatic and fast scaling out of the box without the need for you to forecast traffic up front or manage scaling policies. Additionally, you pay only for the compute time to run your inference code and for data processing, making it ideal for workloads with intermittent traffic. A: Your serverless endpoint has a minimum RAM size of 1024 MB (1 GB), and the maximum RAM size you can choose is 6144 MB (6 GB). The memory sizes you can choose are 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB. Serverless Inference auto-assigns compute resources proportional to the memory you select. If you choose a larger memory size, your container has access to more vCPUs. Choose your endpoint’s memory size according to your model size. Generally, the memory size should be at least as large as your model size. You may need to benchmark in order to choose the right memory selection for your model based on your latency SLAs. The memory size increments have different pricing; see the [Amazon SageMaker pricing page](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/") for more information. ## Batch Transform The following FAQ items answer common questions for SageMaker AI Batch Transform. A: For specific file formats such as CSV, RecordIO and TFRecord, SageMaker AI can split your data into single-record or multi-record mini batches and send this as a payload to your model container. When the value of `BatchStrategy` is `MultiRecord`, SageMaker AI sends the maximum number of records in each request, up to the `MaxPayloadInMB` limit. When the value of `BatchStrategy` is `SingleRecord`, SageMaker AI sends individual records in each request. A: The maximum timeout for Batch Transform is 3600 seconds. The [maximum payload size](../APIReference/API_CreateTransformJob.md#sagemaker-CreateTransformJob-request-MaxPayloadInMB "../APIReference/API_CreateTransformJob.md#sagemaker-CreateTransformJob-request-MaxPayloadInMB") for a record (per mini batch) is 100 MB. A: If you are using the `CreateTransformJob` API, you can reduce the time it takes to complete batch transform jobs by using optimal values for parameters such as `MaxPayloadInMB`, `MaxConcurrentTransforms`, or `BatchStrategy`. The ideal value for `MaxConcurrentTransforms` is equal to the number of compute workers in the batch transform job. If you are using the SageMaker AI console, you can specify these optimal parameter values in the **Additional configuration** section of the **Batch transform job configuration** page. SageMaker AI automatically finds the optimal parameter settings for built-in algorithms. For custom algorithms, provide these values through an [execution-parameters](your-algorithms-batch-code.md#your-algorithms-batch-code-how-containe-serves-requests "your-algorithms-batch-code.md#your-algorithms-batch-code-how-containe-serves-requests") endpoint. A: Batch Transform supports CSV and JSON. ## Asynchronous Inference The following FAQ items answer common general questions for SageMaker AI Asynchronous Inference. A: Asynchronous Inference queues incoming requests and processes them asynchronously. This option is ideal for requests with large payload sizes or long processing times that need to be processed as they arrive. Optionally, you can configure auto-scaling settings to scale down the instance count to zero when not actively processing requests. A: Amazon SageMaker AI supports automatic scaling (autoscaling) your asynchronous endpoint. Autoscaling dynamically adjusts the number of instances provisioned for a model in response to changes in your workload. Unlike other hosted models SageMaker AI supports, with Asynchronous Inference you can also scale down your asynchronous endpoints instances to zero. Requests that are received when there are zero instances are queued for processing once the endpoint scales up. For more information, see [Autoscale an asynchronous endpoint](async-inference-autoscale.md "async-inference-autoscale.md"). Amazon SageMaker Serverless Inference also automatically scales down to zero. You won’t see this because SageMaker AI manages scaling your serverless endpoints, but if you are not experiencing any traffic, the same infrastructure applies.
````

# Enable deployment

When adding a model to share, you can optionally provide an inference environment in
which collaborators in your organization can deploy the shared model for inference.

After training your machine learning model, you'll need to deploy it to an Amazon SageMaker AI
endpoint for inference. This involves providing a container environment, an inference
script, the model artifacts generated during training, and selecting an appropriate compute
instance type. Configuring these settings properly is crucial for ensuring your deployed
model can make accurate predictions and handle inference requests efficiently. To set up
your model for inference, follow these steps:

1. Add a container to use for inference. You can bring your own container in Amazon ECR or
   use an Amazon SageMaker Deep Learning Container.
2. Provide the Amazon S3 URI to an inference script. Custom inference scripts run inside
   your chosen container. Your inference script should include a function for model
   loading, and optionally functions generating predictions, and input and output
   processing. For more information on creating inference scripts for the framework of your
   choice, see [Frameworks](https://sagemaker.readthedocs.io/en/stable/frameworks/index.html "https://sagemaker.readthedocs.io/en/stable/frameworks/index.html") in the SageMaker Python SDK documentation. For example, for TensorFlow, see
   [How to implement the pre- and/or post-processing handler(s)](https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/deploying_tensorflow_serving.html#how-to-implement-the-pre-and-or-post-processing-handler-s "https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/deploying_tensorflow_serving.html#how-to-implement-the-pre-and-or-post-processing-handler-s").
3. Provide an Amazon S3 URI for model artifacts. Model artifacts are the output that results
   from training a model, and typically consist of trained parameters, a model definition
   that describes how to compute inferences, and other metadata. If you trained your model
   in SageMaker AI, the model artifacts are saved as a single compressed TAR file in Amazon S3. If you
   trained your model outside SageMaker AI, you need to create this single compressed TAR file and
   save it in an Amazon S3 location.
4. Select an instance type. We recommend a GPU instance with more memory for training
   with large batch sizes. For a comprehensive list of SageMaker training instances across AWS
   Regions, see the **On-Demand Pricing** table in [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

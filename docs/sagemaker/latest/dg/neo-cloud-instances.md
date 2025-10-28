# Cloud Instances

Amazon SageMaker Neo provides compilation support for popular machine learning frameworks such as
TensorFlow, PyTorch, MXNet, and more. You can deploy your compiled model to cloud instances
and AWS Inferentia instances. For a full list of supported frameworks and instances types,
see [Supported
Instances Types and Frameworks](neo-supported-cloud.md "neo-supported-cloud.md").

You can compile your model in one of three ways: through the AWS CLI, the SageMaker AI Console, or
the SageMaker AI SDK for Python. See, [Use Neo to
Compile a Model](neo-job-compilation.md "neo-job-compilation.md") for more information. Once compiled, your model artifacts
are stored in the Amazon S3 bucket URI you specified during the compilation job. You can deploy
your compiled model to cloud instances and AWS Inferentia instances using the SageMaker AI SDK for Python,
AWS SDK for Python (Boto3), AWS CLI, or the AWS console.

If you deploy your model using AWS CLI, the console, or Boto3, you must select a Docker
image Amazon ECR URI for your primary container. See [Neo Inference Container Images](neo-deployment-hosting-services-container-images.md "neo-deployment-hosting-services-container-images.md") for a list of Amazon ECR URIs.

###### Topics

- [Supported Instance Types and Frameworks](neo-supported-cloud.md "neo-supported-cloud.md")
- [Deploy a Model](neo-deployment-hosting-services.md "neo-deployment-hosting-services.md")
- [Inference Requests With a Deployed Service](neo-requests.md "neo-requests.md")
- [Inference
  Container Images](neo-deployment-hosting-services-container-images.md "neo-deployment-hosting-services-container-images.md")

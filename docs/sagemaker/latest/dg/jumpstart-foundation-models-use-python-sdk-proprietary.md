

# Deploy proprietary foundation models with the `ModelBuilder` class
<a name="jumpstart-foundation-models-use-python-sdk-proprietary"></a>

Proprietary models must be deployed using the model package information after subscribing to the model in AWS Marketplace. For more information about SageMaker AI and AWS Marketplace, see [Buy and Sell Amazon SageMaker AI Algorithms and Models in AWS Marketplace](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-marketplace.html). To find AWS Marketplace links for the latest proprietary models, see [Getting started with Amazon SageMaker JumpStart](https://aws.amazon.com/sagemaker/jumpstart/getting-started/?sagemaker-jumpstart-cards.sort-by=item.additionalFields.priority&sagemaker-jumpstart-cards.sort-order=asc&awsf.sagemaker-jumpstart-filter-product-type=product-type%23foundation-model&awsf.sagemaker-jumpstart-filter-text=*all&awsf.sagemaker-jumpstart-filter-vision=*all&awsf.sagemaker-jumpstart-filter-tabular=*all&awsf.sagemaker-jumpstart-filter-audio-tasks=*all&awsf.sagemaker-jumpstart-filter-multimodal=*all&awsf.sagemaker-jumpstart-filter-RL=*all&sagemaker-jumpstart-cards.q=proprietary&sagemaker-jumpstart-cards.q_operator=AND).

After subscribing to the model of your choice in AWS Marketplace, you can deploy the foundation model using the SageMaker Python SDK. Reference the subscribed model package by its ARN and deploy it with `ModelBuilder`.

For example, the following code deploys a JumpStart model using Jurassic-2 Jumbo Instruct from AI21 Labs:

```
from sagemaker.core.resources import ModelPackage
from sagemaker.serve import ModelBuilder

model_package_arn = {{"arn:aws:sagemaker:us-east-1:865070037744:model-package/j2-jumbo-instruct-v1-1-43-4e47c49e61743066b9d95efed6882f35"}}

# Reference the subscribed Marketplace model package by its ARN.
model_package = ModelPackage.get(model_package_name=model_package_arn)

# Build and deploy with ModelBuilder. Marketplace packages do not carry
# JumpStart hosting configurations, so specify an instance_type explicitly
# (choose one from the package's supported real-time inference instance types).
model_builder = ModelBuilder(
    model=model_package,
    role_arn={{"arn:aws:iam::123456789012:role/SageMakerExecutionRole"}},
    instance_type={{"ml.g5.12xlarge"}},
)
model = model_builder.build()
endpoint = model_builder.deploy()
```

For step-by-step examples, find and run the notebook associated with the proprietary foundation model of your choice in SageMaker Studio Classic. See [Use foundation models in Amazon SageMaker Studio Classic](jumpstart-foundation-models-use-studio.md) for more information. For more information on the SageMaker Python SDK, see [ModelBuilder](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_serve.html#sagemaker.serve.ModelBuilder) in the SageMaker Python SDK documentation on the Read the Docs website.
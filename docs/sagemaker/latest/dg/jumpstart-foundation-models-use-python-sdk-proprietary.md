# Deploy

proprietary foundation models with the `ModelPackage`
class

Proprietary models must be deployed using the model package information after
subscribing to the model in AWS Marketplace. For more information about SageMaker AI and AWS Marketplace,
see [Buy and Sell Amazon SageMaker AI
Algorithms and Models in AWS Marketplace](sagemaker-marketplace.md "sagemaker-marketplace.md"). To find AWS Marketplace links for the latest
proprietary models, see [Getting started with Amazon SageMaker JumpStart](https://aws.amazon.com/sagemaker/jumpstart/getting-started/?sagemaker-jumpstart-cards.sort-by=item.additionalFields.priority&sagemaker-jumpstart-cards.sort-order=asc&awsf.sagemaker-jumpstart-filter-product-type=product-type%23foundation-model&awsf.sagemaker-jumpstart-filter-text=*all&awsf.sagemaker-jumpstart-filter-vision=*all&awsf.sagemaker-jumpstart-filter-tabular=*all&awsf.sagemaker-jumpstart-filter-audio-tasks=*all&awsf.sagemaker-jumpstart-filter-multimodal=*all&awsf.sagemaker-jumpstart-filter-RL=*all&sagemaker-jumpstart-cards.q=proprietary&sagemaker-jumpstart-cards.q_operator=AND "https://aws.amazon.com/sagemaker/jumpstart/getting-started/?sagemaker-jumpstart-cards.sort-by=item.additionalFields.priority&sagemaker-jumpstart-cards.sort-order=asc&awsf.sagemaker-jumpstart-filter-product-type=product-type%23foundation-model&awsf.sagemaker-jumpstart-filter-text=*all&awsf.sagemaker-jumpstart-filter-vision=*all&awsf.sagemaker-jumpstart-filter-tabular=*all&awsf.sagemaker-jumpstart-filter-audio-tasks=*all&awsf.sagemaker-jumpstart-filter-multimodal=*all&awsf.sagemaker-jumpstart-filter-RL=*all&sagemaker-jumpstart-cards.q=proprietary&sagemaker-jumpstart-cards.q_operator=AND").

After subscribing to the model of your choice in AWS Marketplace, you can deploy the
foundation model using the SageMaker Python SDK and the SDK associated
with the model provider. For example, AI21 Labs, Cohere, and LightOn use the
`"ai21[SM]"`, `cohere-sagemaker`, and
`lightonsage` packages, respectively.

For example, to define a JumpStart model using Jurassic-2 Jumbo Instruct from AI21
Labs, use the following code:

```
import sagemaker
import ai21

role = get_execution_role()
sagemaker_session = sagemaker.Session()
model_package_arn = `"arn:aws:sagemaker:us-east-1:865070037744:model-package/j2-jumbo-instruct-v1-1-43-4e47c49e61743066b9d95efed6882f35"`

my_model = ModelPackage(
    role=role, model_package_arn=model_package_arn, sagemaker_session=sagemaker_session
)
```

For step-by-step examples, find and run the notebook associated with the
proprietary foundation model of your choice in SageMaker Studio Classic. See [Use foundation models in
Amazon SageMaker Studio Classic](jumpstart-foundation-models-use-studio.md "jumpstart-foundation-models-use-studio.md") for more
information. For more information on the SageMaker Python SDK, see
[`ModelPackage`](https://sagemaker.readthedocs.io/en/stable/api/inference/model.html#sagemaker.model.ModelPackage "https://sagemaker.readthedocs.io/en/stable/api/inference/model.html#sagemaker.model.ModelPackage").

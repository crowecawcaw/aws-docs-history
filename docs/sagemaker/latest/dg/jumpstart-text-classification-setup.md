# Set up your evaluation environment

Set up SageMaker AI Studio to access JumpStart models for text classification evaluation. This section covers configuring permissions and understand the associated costs before you deploy models.

## Prerequisites

Before you begin, make sure that you have an AWS account with SageMaker AI permissions. For account setup instructions, see [Set up SageMaker AI Prerequisites](gs-set-up.md "gs-set-up.md").

## Set up SageMaker AI Studio for JumpStart model evaluation

If you don't have access to SageMaker AI Studio, see [Quick setup](onboard-quick-start.md "onboard-quick-start.md") to create a domain.

To get started with your text classification project in SageMaker Studio:

1. Open the SageMaker AI Studio Control Panel.
2. Select your user profile.
3. Choose **Open Studio**.
4. Wait for Studio to load (this may take 2-3 minutes on first launch).
5. Verify that JumpStart appears in the left navigation panel.

## Understanding SageMaker AI costs

When you use SageMaker AI Studio, you incur costs for:

- SageMaker AI endpoint hosting (varies by instance type and duration).
- Amazon S3 storage for datasets and model artifacts.
- Notebook instance runtime (some usage covered by AWS Free Tier for eligible accounts).

###### Note

Using the Studio interface incurs no additional charges.

### Cost management recommendations

Follow these recommendations to minimize costs during your evaluation:

- Use default instances as specified for DistilBERT and BERT models.
- Delete endpoints immediately after evaluation.
- Monitor your usage with [AWS Pricing Calculator](https://aws.amazon.com/calculator.aws/#/addService/SageMaker "https://aws.amazon.com/calculator.aws/#/addService/SageMaker").
- For current storage rates, see [Amazon Simple Storage Service Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

###### Warning

Be sure to shut down endpoints and clean up resources after completing this tutorial to avoid ongoing charges.

Continue to [Select and deploy text classification models](jumpstart-text-classification-deploy.md "jumpstart-text-classification-deploy.md").

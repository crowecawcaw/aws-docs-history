

# Set up your evaluation environment
<a name="jumpstart-text-classification-setup"></a>

Set up SageMaker AI Studio to access JumpStart models for text classification evaluation. This section covers configuring permissions and understand the associated costs before you deploy models.

## Prerequisites
<a name="w2aac37c15c19b5"></a>

Before you begin, make sure that you have an AWS account with SageMaker AI permissions. For account setup instructions, see [Set up SageMaker AI Prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-set-up.html).

## Set up SageMaker AI Studio for JumpStart model evaluation
<a name="w2aac37c15c19b7"></a>

If you don't have access to SageMaker AI Studio, see [Quick setup](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-quick-start.html) to create a domain.

To get started with your text classification project in SageMaker Studio:

1. Open the SageMaker AI Studio Control Panel.

1. Select your user profile.

1. Choose **Open Studio**.

1. Wait for Studio to load (this may take 2-3 minutes on first launch).

1. Verify that JumpStart appears in the left navigation panel.

## Understanding SageMaker AI costs
<a name="w2aac37c15c19b9"></a>

When you use SageMaker AI Studio, you incur costs for:
+ SageMaker AI endpoint hosting (varies by instance type and duration).
+ Amazon S3 storage for datasets and model artifacts.
+ Notebook instance runtime (some usage covered by AWS Free Tier for eligible accounts).

**Note**  
Using the Studio interface incurs no additional charges.

### Cost management recommendations
<a name="w2aac37c15c19b9b9"></a>

Follow these recommendations to minimize costs during your evaluation:
+ Use default instances as specified for DistilBERT and BERT models.
+ Delete endpoints immediately after evaluation.
+ Monitor your usage with [AWS Pricing Calculator](https://aws.amazon.com/calculator.aws/#/addService/SageMaker).
+ For current storage rates, see [Amazon Simple Storage Service Pricing](https://aws.amazon.com/s3/pricing/).

**Warning**  
Be sure to shut down endpoints and clean up resources after completing this tutorial to avoid ongoing charges.

Continue to [Select and deploy text classification models](jumpstart-text-classification-deploy.md).
# Nova Forge access and setup

## Subscribe to Nova Forge

To access Nova Forge features, complete the following steps:

1. Verify administrator access to the AWS account.
2. Navigate to the SageMaker AI AI console and request access to Nova Forge.
3. Wait for the Nova team to email a confirmation after the subscription
   request is approved.
4. Tag your SageMaker HyperPod execution role with the
   `forge-subscription` tag. This tag is required for accessing
   Nova Forge features and checkpoints. Add the following tag to your execution
   role:
   - Key: `forge-subscription`
   - Value: `true`

5. Set up the necessary SageMaker HyperPod infrastructure by following the [workshop instructions](https://catalog.us-east-1.prod.workshops.aws/workshops/dcac6f7a-3c61-4978-8344-7535526bf743/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/dcac6f7a-3c61-4978-8344-7535526bf743/en-US") for configuring the environment with
   Forge-enabled features.

###### Note

Standard Amazon Nova features remain available without a Forge subscription. Nova
Forge is designed for building custom frontier models with control and
flexibility across all model training phases.

## Content moderation settings

If you need access to Nova Forge, customizable content moderation settings (CCMS)
are available for Amazon Nova Lite 1.0 and Pro 1.0 models. CCMS allows adjustment of
content moderation controls to align with specific business requirements while
maintaining essential responsible AI safeguards. To determine if a business model is
appropriate for CCMS, contact an AWS Account Manager.

For additional information on configuring and using CCMS with custom models, see
the Responsible AI Toolkit and Content Moderation section.

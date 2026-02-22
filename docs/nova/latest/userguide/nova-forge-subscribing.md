# Subscribe to Amazon Nova Forge

To access Amazon Nova Forge features, complete the following steps:

1. Verify administrator access to the AWS account.
2. Navigate to the SageMaker AI console and request access to Amazon Nova Forge.
3. Wait for the Amazon Nova team to email a confirmation after the subscription request is
   approved.
4. Tag your execution role with the `forge-subscription` tag.
   This tag is required for accessing Amazon Nova Forge features and checkpoints. Add the following
   tag to your execution role:
   - Key: `forge-subscription`
   - Value: `true`

###### Note

Standard Amazon Nova features remain available without a Forge subscription. Amazon Nova Forge is
designed for building custom frontier models with control and flexibility across all model
training phases.

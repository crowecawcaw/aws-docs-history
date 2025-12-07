# Subscribe to Nova Forge

To access Nova Forge features, complete the following steps:

1. Verify administrator access to the AWS account.
2. Navigate to the SageMaker AI AI console and request access to Nova Forge.
3. Wait for the Nova team to email a confirmation after the subscription request is
   approved.
4. Tag your SageMaker HyperPod execution role with the `forge-subscription` tag.
   This tag is required for accessing Nova Forge features and checkpoints. Add the following
   tag to your execution role:
   - Key: `forge-subscription`
   - Value: `true`

###### Note

Standard Amazon Nova features remain available without a Forge subscription. Nova Forge is
designed for building custom frontier models with control and flexibility across all model
training phases.

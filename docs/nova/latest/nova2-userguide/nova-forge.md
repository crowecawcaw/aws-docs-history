# Amazon Nova Forge

Amazon Nova Forge is a first-of-its-kind service that offers organizations the easiest and most cost-effective way to build their own frontier models using Nova.

Amazon Nova Forge introduces the concept of “open training" models, which give
organizations access to a variety of early model checkpoints and the ability to blend
proprietary data with Amazon-curated data sets at every stage of model training. This allows
the models to maximize learning from proprietary data while minimizing risk of forgetting
foundational skills like reasoning.

Nova Forge provides the following key capabilities:

- Access checkpoints across all phases of model development, and leverage new Nova models before they are widely available
- Blend your proprietary data with Amazon Nova-curated training data
- Perform reinforcement learning with reward functions in your environment
- Use push-button recipes that are optimized to build with Nova through visual workflows or a command line interface
- Use the Responsible AI Toolkit to align models to Amazon Nova's responsible AI guidelines during the training process and implement runtime controls to moderate model responses during inference.

## Prerequisites

###### Topics

- [Subscribe to Nova Forge](#nova-forge-prereq-access "#nova-forge-prereq-access")
- [Other prerequisites](#nova-forge-prereq-other "#nova-forge-prereq-other")

### Subscribe to Nova Forge

To request access to the Amazon Nova Forge service, add the following tag to your console IAM role: key forge-subscription with value true. After you've added this tag to your role, please go to SageMaker AI Console > Model training and customization and
click on Nova Forge. On this page, you'll find details about the service, pricing
information and the capabilities. You can request subscription and then manage your
subscription from this page.

1. The role should have permission to call api
   `ListAttachedRolePolicy`, and the response should include
   either `AdministratorAccess` or
   `AmazonSageMakerFullAccess` policy.
2. The sign-in role should have permission to call api
   `ListRoleTags`, and the response tags should include
   `tag.key=forge-subscription`.

### Other prerequisites

Also ensure the following prerequisites are complete:

1. [General prerequisites](nova-model.md#nova-model-general-prerequisites "nova-model.md#nova-model-general-prerequisites")
2. Additional steps for users: Add Restricted Instance Group
   (RIG) to your SageMaker HyperPod cluster (to complete follow steps [here](../../../sagemaker/latest/dg/nova-hp-cluster.md "../../../sagemaker/latest/dg/nova-hp-cluster.md"))

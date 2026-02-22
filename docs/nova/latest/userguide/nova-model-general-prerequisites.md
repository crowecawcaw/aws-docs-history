# General prerequisites

The customization process involves several key stages including model training,
evaluation, and deployment for inference, each requiring specific resources and
configurations. Before beginning your Amazon Nova model customization on SageMaker, ensure you have
the following general prerequisites.

- An AWS account. If you don't have an AWS account, follow [these
  instructions](../../../sagemaker/latest/dg/gs-set-up.md#sign-up-for-aws "../../../sagemaker/latest/dg/gs-set-up.md#sign-up-for-aws") to sign up for one.
- [Installing the
  AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") and [Setting up the
  configuration](../../../cli/latest/userguide/getting-started-quickstart.md "../../../cli/latest/userguide/getting-started-quickstart.md").
- Access to the [base Amazon Nova model customization recipes](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/ "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/").
- Familiarity of [YAML](https://yaml.org/ "https://yaml.org/") configuration
  files.
- Familiarity of how to run a notebook in your environment.
- Familiarity of how to create AWS resources like [Amazon S3
  buckets](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") and [IAM roles with
  appropriate permissions](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md").
- Familiarity of how to [train a model with
  SageMaker](../../../sagemaker/latest/dg/how-it-works-training.md "../../../sagemaker/latest/dg/how-it-works-training.md").
- Familiarity of [SageMaker HyperPod with
  EKS orchestration](../../../sagemaker/latest/dg/sagemaker-hyperpod-eks.md "../../../sagemaker/latest/dg/sagemaker-hyperpod-eks.md").
- Familiarity of [SageMaker HyperPod CLI](../../../sagemaker/latest/dg/sagemaker-hyperpod-eks-run-jobs-access-nodes.md "../../../sagemaker/latest/dg/sagemaker-hyperpod-eks-run-jobs-access-nodes.md").
- Familiarity of [Amazon Nova foundational
  models](customization.md "customization.md").
- Familiarity of [available Amazon Nova models
  and algorithms for customization](nova-model-recipes.md#nova-model-algorithm "nova-model-recipes.md#nova-model-algorithm").
- Familiarity of [Amazon Bedrock
  inference](../../../=/bedrock/latest/userguide/inference-how.md "../../../=/bedrock/latest/userguide/inference-how.md").

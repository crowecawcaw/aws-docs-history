

# General prerequisites
<a name="nova-model-general-prerequisites"></a>

The customization process involves several key stages including model training, evaluation, and deployment for inference, each requiring specific resources and configurations. Before beginning your Amazon Nova model customization on SageMaker, ensure you have the following general prerequisites.
+ An AWS account. If you don't have an AWS account, follow [these instructions](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-set-up.html#sign-up-for-aws) to sign up for one.
+ [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [Setting up the configuration](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html).
+ Access to the [base Amazon Nova model customization recipes](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/).
+ Familiarity of [YAML](https://yaml.org/) configuration files.
+ Familiarity of how to run a Jupyter notebook in your environment.
+ Familiarity of how to create AWS resources like [Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) and [IAM roles with appropriate permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html).
+ Familiarity of how to [train a model with SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html).
+ Familiarity of [SageMaker HyperPod with EKS orchestration](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks.html).
+ Familiarity of [SageMaker HyperPod CLI](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-run-jobs-access-nodes.html).
+ Familiarity of [Amazon Nova foundational models](https://docs.aws.amazon.com/nova/latest/userguide/customization.html).
+ Familiarity of [available Amazon Nova models and algorithms for customization](nova-model-recipes.md#nova-model-algorithm).
+ Familiarity of [Amazon Bedrock inference](https://docs.aws.amazon.com/=/bedrock/latest/userguide/inference-how.html).
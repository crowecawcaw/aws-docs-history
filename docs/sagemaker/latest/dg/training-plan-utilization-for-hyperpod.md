# Training plans

utilization for Amazon SageMaker HyperPod clusters

To use SageMaker training plans for your Amazon SageMaker HyperPod cluster, you specify the training plan you
want to use at the cluster instance level when creating or updating your cluster.

###### Note

- The training plan must be in the `Scheduled` or `Active` status
  to be used by an HyperPod cluster.
- Ensure the cluster configuration aligns with the Availability Zone (AZ) specified in
  your training plan.

For VPC setup, resource location, and security group configuration, refer to [Setting up SageMaker HyperPod
with a custom Amazon VPC](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-optional-vpc "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-optional-vpc") in the SageMaker HyperPod
documentation.

If setting up HyperPod with Amazon FSx for Lustre, learn about Region and AZ
selection, review VPC configuration requirements, and understand AZ alignment best
practices in [(Optional) Setting up
SageMaker HyperPod with Amazon FSx for Lustre](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-optional-fsx "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-optional-fsx").

- You can select a plan for each of your instance groups. However, we do not recommend
  using a training plan for the primary instance group of a cluster, as primary nodes
  require continuous, stable resources that don't align with the fixed duration and
  potentially discontinuous nature of training plan capacities.

###### Topics

- [Create a SageMaker HyperPod
  cluster on training plans using the SageMaker AI console](use-training-plan-for-hyperpod-creation-using-console.md "use-training-plan-for-hyperpod-creation-using-console.md")
- [Update a SageMaker HyperPod
  cluster on training plans using the SageMaker AI console](use-training-plan-for-hyperpod-update-using-console.md "use-training-plan-for-hyperpod-update-using-console.md")
- [Create a
  SageMaker HyperPod cluster on training plans using the SageMaker API, or AWS CLI](use-training-plan-for-hyperpod-creation-using-api-cli-sdk.md "use-training-plan-for-hyperpod-creation-using-api-cli-sdk.md")
- [Update a
  SageMaker HyperPod cluster on training plans using the SageMaker API, or AWS CLI](use-training-plan-for-hyperpod-update-using-api-cli-sdk.md "use-training-plan-for-hyperpod-update-using-api-cli-sdk.md")

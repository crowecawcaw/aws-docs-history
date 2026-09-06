

# Installing the SageMaker HyperPod CLI
<a name="sagemaker-hyperpod-eks-run-jobs-access-nodes"></a>

SageMaker HyperPod provides the [SageMaker HyperPod command line interface](https://github.com/aws/sagemaker-hyperpod-cli) (CLI) package. 

1. Check if the version of Python on your local machine is between 3.8 and 3.11.

1. Check the prerequisites in the `README` markdown file in the [SageMaker HyperPod CLI](https://github.com/aws/sagemaker-hyperpod-cli) package.

1. Clone the SageMaker HyperPod CLI package from GitHub.

   ```
   git clone https://github.com/aws/sagemaker-hyperpod-cli.git
   ```

1. Install the SageMaker HyperPod CLI.

   ```
   cd sagemaker-hyperpod-cli && pip install .
   ```

1. Test if the SageMaker HyperPod CLI is successfully installed by running the following command. 

   ```
   hyperpod --help
   ```

**Note**  
If you are a data scientist and want to use the SageMaker HyperPod CLI, make sure that your IAM role is set up properly by your cluster admins following the instructions at [IAM users for scientists](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-cluster-user) and [Setting up Kubernetes role-based access control](sagemaker-hyperpod-eks-setup-rbac.md).
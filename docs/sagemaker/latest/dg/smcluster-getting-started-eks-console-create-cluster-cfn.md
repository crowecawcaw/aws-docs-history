# Creating

SageMaker HyperPod clusters using AWS CloudFormation templates

You can create SageMaker HyperPod clusters using the CloudFormation templates for
HyperPod. You must install AWS CLI to proceed.

###### In this topic:

- [Configure resources in the console and deploy using CloudFormation](#smcluster-getting-started-eks-console-create-cluster-deploy-console "#smcluster-getting-started-eks-console-create-cluster-deploy-console")
- [Configure and deploy resources using CloudFormation](#smcluster-getting-started-eks-console-create-cluster-deploy-cfn "#smcluster-getting-started-eks-console-create-cluster-deploy-cfn")

## Configure resources in the console and deploy using CloudFormation

You can configure resources using the AWS Management Console and deploy using the CloudFormation
templates.

Follow these steps.

1. \*Instead of choosing
   **Submit\***, choose **Download
   CloudFormation template parameters** at the end of the tutorial in
   [Getting started with
   SageMaker HyperPod using the SageMaker AI console](smcluster-getting-started-slurm-console.md "smcluster-getting-started-slurm-console.md"). The tutorial
   contains important configuration information you will need to create your
   cluster successfully.

###### Important

If you choose **Submit**, you will not be able to
deploy a cluster with the same name until you delete the cluster.

After you choose **Download CloudFormation template
parameters**, the **Using the configuration file to
create the cluster using the AWS CLI** window will appear on the
right side of the page. 2. On the **Using the configuration file to create the cluster using
the AWS CLI** window, choose **Download configuration
parameters file**. The file will be downloaded to your machine.
You can edit the configuration JSON file based on your needs or leave it
as-is, if no change is required. 3. In the terminal, navigate to the location of the parameter file
`file://params.json`. 4. Run the [create-stack](../../../cli/latest/reference/cloudformation/create-stack.md "../../../cli/latest/reference/cloudformation/create-stack.md") AWS CLI command to deploy the CloudFormation stack that
will provision the configured resources and create the HyperPod
cluster.

```
aws cloudformation create-stack
    --stack-name `my-stack`
    --template-url `https://aws-sagemaker-hyperpod-cluster-setup.amazonaws.com/templates-slurm/main-stack-slurm-based-template.yaml`
    --parameters file://params.json
    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM
```

5. To view the status of the resources provisioning, navigate to the [CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").

After the cluster creation completes, view the new cluster under
**Clusters** in the main pane of the SageMaker HyperPod
console. You can check the status of it displayed under the
**Status** column. 6. After the status of the cluster turns to `InService`, you can
start logging into the cluster nodes. To access the cluster nodes and start
running ML workloads, see [Jobs on SageMaker HyperPod clusters](sagemaker-hyperpod-run-jobs-slurm.md "sagemaker-hyperpod-run-jobs-slurm.md").

## Configure and deploy resources using CloudFormation

You can configure and deploy resources using the CloudFormation templates for
SageMaker HyperPod.

Follow these steps.

1. Download a CloudFormation template for SageMaker HyperPod from the [sagemaker-hyperpod-cluster-setup](https://github.com/aws/sagemaker-hyperpod-cluster-setup "https://github.com/aws/sagemaker-hyperpod-cluster-setup") GitHub repository.
2. Run the [create-stack](../../../cli/latest/reference/cloudformation/create-stack.md "../../../cli/latest/reference/cloudformation/create-stack.md") AWS CLI command to deploy the CloudFormation stack that
   will provision the configured resources and create the HyperPod
   cluster.

```
aws cloudformation create-stack
    --stack-name `my-stack`
    --template-url `URL_of_the_file_that_contains_the_template_body`
    --parameters file://params.json
    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM
```

3. To view the status of the resources provisioning, navigate to the
   CloudFormation console.

After the cluster creation completes, view the new cluster under
**Clusters** in the main pane of the SageMaker HyperPod
console. You can check the status of it displayed under the
**Status** column. 4. After the status of the cluster turns to `InService`, you can
start logging into the cluster nodes.

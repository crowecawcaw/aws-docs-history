**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Copy a container image from one repository to another repository

This topic describes how to pull a container image from a repository that your nodes don’t have access to and push the image to a repository that your nodes have access to. You can push the image to Amazon ECR or an alternative repository that your nodes have access to.

- The Docker engine installed and configured on your computer. For instructions, see [Install Docker Engine](https://docs.docker.com/engine/install/ "https://docs.docker.com/engine/install/") in the Docker documentation.
- Version `2.12.3` or later or version `1.27.160` or later of the AWS Command Line Interface (AWS CLI) installed and configured on your device or AWS CloudShell. To check your current version, use `aws --version | cut -d / -f2 | cut -d ' ' -f1`. Package managers such `yum`, `apt-get`, or Homebrew for macOS are often several versions behind the latest version of the AWS CLI. To install the latest version, see [Installing](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") and [Quick configuration with aws configure](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config") in the _AWS Command Line Interface User Guide_. The AWS CLI version that is installed in AWS CloudShell might also be several versions behind the latest version. To update it, see [Installing AWS CLI to your home directory](../../../cloudshell/latest/userguide/vm-specs.md#install-cli-software "../../../cloudshell/latest/userguide/vm-specs.md#install-cli-software") in the _AWS CloudShell User Guide_.
- An interface VPC endpoint for Amazon ECR if you want your nodes to pull container images from or push container images to a private Amazon ECR repository over Amazon’s network. For more information, see [Create the VPC endpoints for Amazon ECR](../../../AmazonECR/latest/userguide/vpc-endpoints.md#ecr-setting-up-vpc-create "../../../AmazonECR/latest/userguide/vpc-endpoints.md#ecr-setting-up-vpc-create") in the Amazon Elastic Container Registry User Guide.
  Complete the following steps to pull a container image from a repository and push it to your own repository. In the following examples that are provided in this topic, the image for the [Amazon VPC CNI plugin for Kubernetes metrics helper](https://github.com/aws/amazon-vpc-cni-k8s/blob/master/cmd/cni-metrics-helper/README.md "https://github.com/aws/amazon-vpc-cni-k8s/blob/master/cmd/cni-metrics-helper/README.md") is pulled. When you follow these steps, make sure to replace the example values with your own values.

1. If you don’t already have an Amazon ECR repository or another repository, then create one that your nodes have access to. The following command creates an Amazon ECR private repository. An Amazon ECR private repository name must start with a letter. It can only contain lowercase letters, numbers, hyphens (-), underscores (\_), and forward slashes (/). For more information, see [Creating a private repository](../../../AmazonECR/latest/userguide/repository-create.md "../../../AmazonECR/latest/userguide/repository-create.md") in the Amazon Elastic Container Registry User Guide.

You can replace `cni-metrics-helper` with whatever you choose. As a best practice, create a separate repository for each image. We recommend this because image tags must be unique within a repository. Replace `region-code` with an [AWS Region supported by Amazon ECR](../../../general/latest/gr/ecr.md "../../../general/latest/gr/ecr.md").

```
aws ecr create-repository --region region-code --repository-name cni-metrics-helper
```

2. Determine the registry, repository, and tag (optional) of the image that your nodes need to pull. This information is in the `registry/repository[:tag]` format.

Many of the Amazon EKS topics about installing images require that you apply a manifest file or install the image using a Helm chart. However, before you apply a manifest file or install a Helm chart, first view the contents of the manifest or chart’s `values.yaml` file. That way, you can determine the registry, repository, and tag to pull.

For example, you can find the following line in the [manifest file](https://raw.githubusercontent.com/aws/amazon-vpc-cni-k8s/v1.12.6/config/master/cni-metrics-helper.yaml "https://raw.githubusercontent.com/aws/amazon-vpc-cni-k8s/v1.12.6/config/master/cni-metrics-helper.yaml") for the [Amazon VPC CNI plugin for Kubernetes metrics helper](https://github.com/aws/amazon-vpc-cni-k8s/blob/master/cmd/cni-metrics-helper/README.md "https://github.com/aws/amazon-vpc-cni-k8s/blob/master/cmd/cni-metrics-helper/README.md"). The registry is `602401143452.dkr.ecr.us-west-2.amazonaws.com`, which is an Amazon ECR private registry. The repository is `cni-metrics-helper`.

```
image: "602401143452.dkr.ecr.us-west-2.amazonaws.com/cni-metrics-helper:v1.12.6"
```

You may see the following variations for an image location:

    * Only `repository-name:tag`. In this case, `docker.io` is usually the registry, but not specified since Kubernetes prepends it to a repository name by default if no registry is specified.
    * `repository-name/repository-namespace/repository:tag`. A repository namespace is optional, but is sometimes specified by the repository owner for categorizing images. For example, all [Amazon EC2 images in the Amazon ECR Public Gallery](https://gallery.ecr.aws/aws-ec2/ "https://gallery.ecr.aws/aws-ec2/") use the `aws-ec2` namespace.


    Before installing an image with Helm, view the Helm `values.yaml` file to determine the image location. For example, the [values.yaml](https://github.com/aws/amazon-vpc-cni-k8s/blob/master/charts/cni-metrics-helper/values.yaml#L5-L9 "https://github.com/aws/amazon-vpc-cni-k8s/blob/master/charts/cni-metrics-helper/values.yaml#L5-L9") file for the [Amazon VPC CNI plugin for Kubernetes metrics helper](https://github.com/aws/amazon-vpc-cni-k8s/blob/master/cmd/cni-metrics-helper/README.md "https://github.com/aws/amazon-vpc-cni-k8s/blob/master/cmd/cni-metrics-helper/README.md") includes the following lines.



    ```
    image:
      region: us-west-2
      tag: v1.12.6
      account: "602401143452"
      domain: "amazonaws.com"
    ```

3. Pull the container image specified in the manifest file.
   1. If you’re pulling from a public registry, such as the [Amazon ECR Public Gallery](https://gallery.ecr.aws/ "https://gallery.ecr.aws/"), you can skip to the next sub-step, because authentication isn’t required. In this example, you authenticate to an Amazon ECR private registry that contains the repository for the CNI metrics helper image. Amazon EKS maintains the image in each registry listed in [View Amazon container image registries for Amazon EKS add-ons](add-ons-images.md "add-ons-images.md"). You can authenticate to any of the registries by replacing `602401143452` and `region-code` with the information for a different registry. A separate registry exists for each [AWS Region that Amazon EKS is supported in](../../../general/latest/gr/eks.md#eks_region "../../../general/latest/gr/eks.md#eks_region").

   ```
   aws ecr get-login-password --region region-code | docker login --username AWS --password-stdin 602401143452.dkr.ecr.region-code.amazonaws.com
   ```

   2. Pull the image. In this example, you pull from the registry that you authenticated to in the previous sub-step. Replace `602401143452` and `region-code` with the information that you provided in the previous sub-step.

   ```
   docker pull 602401143452.dkr.ecr.region-code.amazonaws.com/cni-metrics-helper:v1.12.6
   ```

4. Tag the image that you pulled with your registry, repository, and tag. The following example assumes that you pulled the image from the manifest file and are going to push it to the Amazon ECR private repository that you created in the first step. Replace `111122223333` with your account ID. Replace `region-code` with the AWS Region that you created your Amazon ECR private repository in.

```
docker tag cni-metrics-helper:v1.12.6 111122223333.dkr.ecr.region-code.amazonaws.com/cni-metrics-helper:v1.12.6
```

5. Authenticate to your registry. In this example, you authenticate to the Amazon ECR private registry that you created in the first step. For more information, see [Registry authentication](../../../AmazonECR/latest/userguide/Registries.md#registry_auth "../../../AmazonECR/latest/userguide/Registries.md#registry_auth") in the Amazon Elastic Container Registry User Guide.

```
aws ecr get-login-password --region region-code | docker login --username AWS --password-stdin 111122223333.dkr.ecr.region-code.amazonaws.com
```

6. Push the image to your repository. In this example, you push the image to the Amazon ECR private repository that you created in the first step. For more information, see [Pushing a Docker image](../../../AmazonECR/latest/userguide/docker-push-ecr-image.md "../../../AmazonECR/latest/userguide/docker-push-ecr-image.md") in the Amazon Elastic Container Registry User Guide.

```
docker push 111122223333.dkr.ecr.region-code.amazonaws.com/cni-metrics-helper:v1.12.6
```

7. Update the manifest file that you used to determine the image in a previous step with the `registry/repository:tag` for the image that you pushed. If you’re installing with a Helm chart, there’s often an option to specify the `registry/repository:tag`. When installing the chart, specify the `registry/repository:tag` for the image that you pushed to your repository.

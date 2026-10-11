

# Adding a new version of your container product on AWS Marketplace
<a name="container-add-version"></a>

As an AWS Marketplace seller, you can add new versions of your container product, manage versions, and update version information. Your product might have several versions over its lifetime. Each version has a set of container images that are specific to that version. The following topics show you how to manage product versions for your container products.

Before you add a version, create the product ID and the pricing for your product. For more information, see [Step 1: Create the product ID and product code for your container product](container-product-getting-started.md#create-initial-container-product). For the limits that apply to repositories, images, and delivery options, see [Limits for container product versions](#container-version-limits).

**Topics**
+ [Step 1: Add repositories](#add-repositories)
+ [Step 2: Upload container images and artifacts to repositories](#upload-resources)
+ [Step 3: Add a new version to your container product](#add-new-version)
+ [Step 4: Update version information](#container-product-updating-version)
+ [Restrict a version of your Amazon EKS add-on](#restriciting-version-eks-addon)
+ [Limits for container product versions](#container-version-limits)

## Step 1: Add repositories
<a name="add-repositories"></a>

Your container images and other artifacts for your product are stored in repositories in AWS Marketplace. Typically, you create one repository for each artifact needed, but the repository can store multiple versions of the artifact (with different tags). All images in your product deployment must come from your AWS Marketplace repositories.

The following procedure describes how to add any needed repositories in AWS Marketplace.

**To add repositories**

1. Sign in to the [AWS Marketplace Management Portal](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. Select **Server** from the **Build** menu.

1. On the **Server products** tab, select the product you want to modify, and then choose **Add repositories** from the **Request changes** dropdown.

1. Enter a name for the repository. Repository names must be unique across all products in your seller account. To create more than one repository, choose **Add new repository** for each additional repository.

1. Select **Submit**.

A new request is created and shown on the **Requests** tab. When it's completed, within minutes, you can start adding container images and other artifacts to the repositories you have created. A product can have up to 70 repositories.

Each repository has a URI in this format: `<registryID>.dkr.ecr.us-east-1.amazonaws.com/<sellerName>/<repositoryName>`. When you push an artifact, its tag is added to the end: `<registryID>.dkr.ecr.us-east-1.amazonaws.com/<sellerName>/<repositoryName>:<tag>`.
+ `registryID` is the ID of the AWS account that hosts AWS Marketplace repositories.
+ `sellerName` is a prefix that AWS Marketplace generates from your seller display name. It doesn't change after it's created. If your display name doesn't produce a prefix, AWS Marketplace uses a UUID (universally unique identifier) instead. To change the prefix, contact the AWS Marketplace operations team.
+ `repositoryName` is the name that you enter in this procedure.
+ `tag` is the tag that you set when you push an artifact to the repository.

## Step 2: Upload container images and artifacts to repositories
<a name="upload-resources"></a>

**To upload container images and artifacts to repositories**

1. Sign in to the [AWS Marketplace Management Portal](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. From the **Build** menu, choose **Server**.

1. On the **Server products** tab, select the product you want to modify.

1. Choose **Add repositories** from the **Request changes** dropdown.

1. Choose **View existing repositories**.

1. Select the repository to which you want to upload.

1. Select **View push commands** to open a list of instructions, including commands you can use to push Docker container images and Helm charts to that repository. 

   For general information about how to push container images and other artifacts to repositories, see [Pushing an image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-push.html) in the *Amazon Elastic Container Registry User Guide*.

1. Use the commands listed to push any needed artifacts from your local repository to the AWS Marketplace repository for your product. The tag that you provide in the `push` command identifies the version of the artifact. Use a tag that matches the product version that the artifact belongs to.

1. Repeat for each container image or artifact that your version needs. Each delivery option can include up to 50 container images or artifacts. For all limits, see [Limits for container product versions](#container-version-limits).

After you upload your artifacts, you're ready to create the version of your product. AWS Marketplace scans your container images automatically to check that they meet the [Container-based product requirements for AWS Marketplace](container-product-policies.md). For more information, see [Container product scans for security issues](container-product-getting-started.md#container-security).

### Adding a new delivery option
<a name="add-delivery-option"></a>

Each version of your container product would need a delivery option. Delivery option specifies the deployment options available for the buyer. Depending on one of the delivery options below, you would need to upload the appropriate artifacts into the repositories.
+ For a **Container image** delivery option, upload all the container images required for the product installation into the Amazon Elastic Container Registry (Amazon ECR) repository created in the AWS Marketplace console.
+ For a **Helm chart** delivery option, upload the Helm chart and container images into the Amazon ECR repository created in the AWS Marketplace console.
+ For an **Amazon EKS console add-on** delivery option, upload the Helm chart and container images into the Amazon ECR repository created in the AWS Marketplace console.

## Step 3: Add a new version to your container product
<a name="add-new-version"></a>

**To add a new version to your container product**

1. Sign in to the [AWS Marketplace Management Portal](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. Choose **Server** from the **Build** menu.

1. On the **Server products** tab, select the product you want to add a version to. Then choose **Add new version** from the **Request changes** dropdown.

1. On the **Add new version** page, enter the **Version title** and **Release notes** for your version.

1. After entering the version details, the next step is to add delivery options. Delivery options are sets of instructions and information that buyers can use to launch the software from your product version. Delivery options are known as *fulfillment options* to buyers. Create one delivery option for each way that buyers can set up your product, for example Kubernetes and Ubuntu deployments that use different container images. Each request can include up to four delivery options.

   1. If the product already has delivery options in other versions, you can use the existing option as a template to add a delivery option to the new version. In **Delivery options**, choose the delivery option that you want to add from the list. You can edit the option using the instructions in the following steps.

   1. To add a new delivery option, choose **New delivery option**. After adding an option, follow the instructions in the following steps to configure it.

1. Choose a delivery method for the delivery option. The delivery method determines how buyers will launch your software.
   + For a **Container image** delivery option, provide paths to container images in an Amazon Elastic Container Registry (Amazon ECR) repository that was created in the AWS Marketplace console. Buyers use the container image paths to launch the software by pulling the images directly into their environments.
   + For a **Helm chart** delivery option, provide paths to Helm charts in an Amazon ECR repository that was created in the AWS Marketplace console. Buyers install the Helm charts in their deployment environment to launch the software.
   + For an **Amazon EKS console add-on** delivery option, provide paths to Helm charts in an Amazon ECR repository that was created in the AWS Marketplace console. Buyers install the container using the Amazon EKS console or native Amazon EKS add-on APIs to launch the software. For more information, see [Available Amazon EKS add-ons from Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html#workloads-add-ons-available-eks).

   1. To add a **Container image** delivery option, perform the following steps:

      1. In **Container images**, add the Amazon ECR URL to the container images that contain the product version software.

      1. In **Delivery option title** and **Deployment option description**, enter a title and description for this delivery option.

      1. In **Usage instructions**, enter detailed information to help your buyers use your software after launching it.

      1. In **Supported services**, select the environments that buyers can launch the software in.

      1. In **Deployment templates**, add resources that buyers can use to launch the software. Enter a title and a URL to the resource for each template.

   1. To add a **Helm chart** delivery option, perform the following steps:

      1. In **Helm chart**, add the Amazon ECR URL to the Helm chart that buyers will install in their deployment environment to launch your software.

      1. In **Container images**, add the Amazon ECR URL to the container images that contain the product version software.

      1. In **Delivery option title** and **Deployment option description**, enter a title and description for this delivery option.

      1. In **Usage instructions**, enter detailed information to help your buyers use your software after launching it.

      1. In **Supported services**, select the environments that buyers can launch the software in.

      1. *Optional - * In **Helm release name**, enter the name for the Helm release that the `helm install` command uses.

      1. In **Helm installation namespace**, enter the name of the Kubernetes namespace where the Helm chart is installed. This field is required for paid products and optional for free products.

      1. *Optional - * In **Kubernetes service account name**, enter the name of the Kubernetes service account that will be used to connect to AWS Identity and Access Management (IAM). The Kubernetes service account calls AWS services such as licensing or metering.

      1. In **Override parameters**, enter parameters that will be used in the Helm CLI commands that launch the software. These parameters allow buyers to override the provided default values. You can enter up to 15 parameters. For more information, see [Adding a new version to a container-based product](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#container-add-version).

         Paid products must include these override parameters:
         + If the delivery option supports Amazon EKS Anywhere, include exactly one override parameter with a `DefaultValue` of `"${AWSMP_LICENSE_SECRET}"`. The product must also use contract pricing.
         + If you leave **Kubernetes service account name** empty, include exactly one override parameter with a `DefaultValue` of `"${AWSMP_SERVICE_ACCOUNT}"`.

      1. Choose **Hide passwords and secrets** to mask sensitive information in consoles, command line tools, and APIs. For more information, see the `NoEcho` parameter documentation in [Parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html) in the *AWS CloudFormation User Guide*.

   1. To add an **Amazon EKS console add-on** delivery option, make sure that artifacts conform to [Requirements for Amazon EKS add-on products](container-product-policies.md#publishing-eks-add-on), and then perform the following steps. Each request can include only one Amazon EKS add-on delivery option.

      1. In **Helm chart**, add the Amazon ECR URL to the Helm chart that buyers will install in their deployment environment to launch your software.

      1. In **Container images**, add the Amazon ECR URL to the container images that contain the product version software. Make sure that all images within the Helm chart are listed.

      1. In **Delivery option title** and **Deployment option description**, enter a title and description for this delivery option.

      1. In **Visibility**, keep the default value of **Limited selected**.

      1. In **Add-on name**, enter a unique name for this add-on. The add-on name that you enter will be appended with the seller’s name while being displayed in the Amazon EKS console.

      1. In **Add-on version**, enter the version of the add-on that will be visible when installing or upgrading this add-on. Follow the format `major.minor.patch`.

      1. In **Add-on type**, select a category for your add-on from the dropdown list.

      1. In **Kubernetes Version**, select all the Kubernetes versions that your add-on will support.

      1. In **Architecture**, select the platform architectures that your add-on supports. The options are **AMD64** and **ARM64**. We recommend supporting both architectures to maximize compatibility. If your add-on doesn't support ARM64 devices, you must specify a planned date for adding support before your product can be published in all commercial AWS Regions.

      1. In **Namespace**, enter a unique Kubernetes namespace where your add-on will be installed. The `default`, `kube-system`, and `kube-public` namespaces aren't supported for installing third-party add-ons.

      1. In **Environment Override parameters**, you can select up to 2 environment parameters from the Amazon EKS add-on framework. You can map parameter names from your values.yaml to these environment variables, which are `${AWS_REGION}` and `${AWS_EKS_CLUSTER_NAME}`.

1. To add additional delivery options, choose **New delivery option** and repeat the instructions in the previous steps to configure them.

1. Choose **Submit**.

If your request fails, see the [Add a new version Asynchronous Errors table](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#container-add-version) in the *AWS Marketplace Catalog API Reference*.

## Step 4: Update version information
<a name="container-product-updating-version"></a>

After a version is created, it can be helpful to provide updated information to your buyers by modifying the information associated with the version. For example, if you plan to restrict version 1.0 after version 1.1 is released, you can update the description of version 1.0 to direct buyers to version 1.1. Provide the date that version 1.0 will be restricted. You update the version information from the AWS Marketplace Management Portal.

**To update version information**

1. Sign in to the [AWS Marketplace Management Portal](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. Select **Server** from the **Build** menu. 

1. On the **Server products** tab, select the product that you want to modify.

1. From the **Request changes** dropdown, choose **Update version information**.

1. On the **Update version** page, select the version that you want to update.

1. Make updates to the selected version. The fields that are available for updating depend on the status of the product version or delivery option.

   1. For all versions, you can update the **Release notes**.

   1. For versions that are not yet publicly available, you can update the **Version title**.

   1. For delivery options that haven't been restricted, you can update the following fields:
      + **Description**
      + **Usage instructions**
      + **Supported services**

   1. For delivery options in versions that are not yet publicly available, you can update the following fields:
      + **Delivery option titles**
      + **Helm chart** (for **Helm chart** delivery options only)
      + **Container images**
      + **Deployment resources**
      + **AddOn Name**
      + **AddOn Version**
      + **AddOn Type**
      + **Helm Chart URI**
      + **CompatibleKubernetesVersions**
      + **SupportedArchitectures**
      + **Namespace**
      + **EnvironmentOverrideParameters**

   1. For delivery options in versions that are publicly available, you can update **SupportedArchitectures**.

1. Choose **Submit**.

1. Verify that the request appears on the **Requests** tab with the **Under review** status.

You can check the status of your request at any time from the **Requests** tab of the [ Server Products](https://aws.amazon.com/marketplace/management/products/server) page.

## Restrict a version of your Amazon EKS add-on
<a name="restriciting-version-eks-addon"></a>

To restrict a version of your container product published as an add-on, contact the AWS Marketplace operations team using the contact us form at the bottom of the [AWS Marketplace Management Portal](https://us-east-1.console.aws.amazon.com/partnercentral/home).

## Limits for container product versions
<a name="container-version-limits"></a>

The following limits apply to each container product.


| Resource | Limit | 
| --- | --- | 
| Repositories per product | 70 | 
| Delivery options per request | 4 | 
| Amazon EKS add-on delivery options per request | 1 | 
| Container images or artifacts per delivery option | 50 | 
| Container images per delivery option that supports Amazon Bedrock AgentCore | 1 | 
| Override parameters per Helm chart delivery option | 15 | 
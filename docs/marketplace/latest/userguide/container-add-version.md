

# Adding a new version of your container product on AWS Marketplace

As an AWS Marketplace seller, you can add new versions of your container product, manage versions, and update version information. Your product might have several versions over its lifetime. Each version has a set of container images that are specific to that version. The following topics show you how to manage product versions for your container products.

Before you add a version, create your product. For more information, see [Step 1: Create your container product](container-product-getting-started.md#create-initial-container-product). You add the first version in **Step 2: Delivery configuration**, before you set pricing in **Step 3: Procurement configuration**. For the limits that apply to repositories, images, and delivery options, see [Limits for container product versions](#container-version-limits).

To manage versions with the AWS Marketplace Catalog API, including the request schemas and the errors a request can return, see [Work with container-based products](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-container-products.html) in the *AWS Marketplace Developer Guide*.

**Topics**
+ [View repositories and versions](#container-delivery-tab)
+ [Step 1: Add repositories](#add-repositories)
+ [Step 2: Upload container images and artifacts to repositories](#upload-resources)
+ [Step 3: Add a new version to your container product](#add-new-version)
+ [Step 4: Update a version](#container-product-updating-version)
+ [Restrict a version](#container-restricting-version)
+ [Restrict a version of your Amazon EKS add-on](#restriciting-version-eks-addon)
+ [Limits for container product versions](#container-version-limits)

## View repositories and versions
<a name="container-delivery-tab"></a>

The **Delivery** tab of your product lists your repositories and versions, and each version has a details page. Use them to copy repository URIs, check scan results, and find your product ID and product code.

**To view repositories and versions**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

   The **Repositories** section lists the URI of each repository. The **Versions** section lists each version with its **Version title**, **Scan result**, **Version visibility**, and **Due date**. **Due date** is the date by which you must fix security issues that a scan found in the version. After that date, new buyers can't subscribe to the affected versions.

1. Choose a version title to open the version's details page.

   The **Version summary** includes the **Product ID**, **Product code**, and **Scan result**. **Version information** shows the release notes, and the page lists the version's delivery options.

The **Version visibility** column shows one of the following values:
+ **Public** – Buyers can find the version on AWS Marketplace, and any buyer can buy it.
+ **Limited** – Only allowlisted AWS accounts can find and buy the version.
+ **Restricted** – Buyers can find the version on AWS Marketplace, but new buyers can't buy it.

## Step 1: Add repositories
<a name="add-repositories"></a>

Your container images and other artifacts for your product are stored in repositories in AWS Marketplace. Typically, you create one repository for each artifact needed, but the repository can store multiple versions of the artifact (with different tags). All images in your product deployment must come from your AWS Marketplace repositories.

The following procedure shows you how to add repositories in AWS Marketplace.

**To add repositories**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Repositories** section, choose **Add repositories**.

   For a new product, you can instead choose **Start** on the **Add repositories** card under **Step 2: Delivery configuration**.

1. Under **New repositories**, enter a **Repository name**.

   To add more than one repository, choose **Add new repository** for each additional one.

   Repository names must be unique across all products in your seller account and must follow these rules:
   + Use 2 to 256 characters.
   + Use lowercase letters, numbers, hyphens (-), underscores (\_), periods (.), and slashes (/). For example, `nginx-web-app`.
   + Start and end the name with a letter or number, and don't put two of these symbols next to each other.

   After you create a repository, you can't delete it or use it for another product.

1. (Optional) Under **Tags**, add tags to the change request.

1. Choose **Submit**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

When the request is completed, within minutes, you can start adding container images and other artifacts to the repositories you have created. A product can have up to 70 repositories.

Each repository has a URI in this format: `<registryID>.dkr.ecr.us-east-1.amazonaws.com/<sellerName>/<repositoryName>`. When you push an artifact, its tag is added to the end: `<registryID>.dkr.ecr.us-east-1.amazonaws.com/<sellerName>/<repositoryName>:<tag>`.
+ `registryID` is the ID of the AWS account that hosts AWS Marketplace repositories.
+ `sellerName` is a prefix that AWS Marketplace generates from your seller display name. It doesn't change after it's created. If your display name doesn't produce a prefix, AWS Marketplace uses a UUID (universally unique identifier) instead. To change the prefix, contact the AWS Marketplace operations team.
+ `repositoryName` is the name that you enter in this procedure.
+ `tag` is the tag that you set when you push an artifact to the repository.

## Step 2: Upload container images and artifacts to repositories
<a name="upload-resources"></a>

**To upload container images and artifacts to repositories**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Repositories** section, select the repository, and then choose **View push commands**.

   For a new product, you can instead choose **Start** on the **Upload container images to repository** card under **Step 2: Delivery configuration**, and then choose **View push commands** in the repository's row.

   The **Push commands** panel shows the **Repository URI** and the commands to authenticate, build, tag or package, push, and verify your artifact.

1. Run the commands to push the artifacts that your version needs to the repository.

   The commands need the latest version of the AWS CLI and the Docker or Helm 3 client. For general information about pushing artifacts, see [Pushing an image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-push.html) in the *Amazon Elastic Container Registry User Guide*.

   The tag that you provide identifies the version of the artifact. AWS Marketplace repository tags are immutable, so use a new tag for each version, and don't use `latest` or an empty tag. For a Helm chart, the chart name must match the last part of the repository name, and Helm uses the chart version as the tag. Use semantic versioning for chart versions.

1. Repeat for each container image or artifact that your version needs. Each delivery option can include up to 50 container images or artifacts. For all limits, see [Limits for container product versions](#container-version-limits).

1. (Optional) If you started from the **Upload container images to repository** page, choose **Complete**.

   Until at least one of your repositories holds an image, the button reads **Close** and the card stays incomplete.

After you upload your artifacts, you're ready to create the version of your product. AWS Marketplace scans your container images automatically to check that they meet the [Container-based product requirements for AWS Marketplace](container-product-policies.md). For more information, see [Container product scans for security issues](container-product-getting-started.md#container-security).

### Adding a new delivery option
<a name="add-delivery-option"></a>

Each version of your container product would need a delivery option. Delivery option specifies the deployment options available for the buyer. Depending on one of the delivery options below, you would need to upload the appropriate artifacts into the repositories.
+ For a **Container image** delivery option, upload all the container images required for the product installation into the Amazon Elastic Container Registry (Amazon ECR) repository created in the AWS Marketplace console.
+ For a **Helm chart** delivery option, upload the Helm chart and container images into the Amazon ECR repository created in the AWS Marketplace console.
+ For an **Amazon EKS console add-on** delivery option, upload the Helm chart and container images into the Amazon ECR repository created in the AWS Marketplace console.

## Step 3: Add a new version to your container product
<a name="add-new-version"></a>

**To add a new version**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Versions** section, choose **Add version**.

   For a new product, you can instead choose **Start** on the **Configure version and delivery options** card under **Step 2: Delivery configuration**. The card is available after you complete the **Upload container images to repository** card.

1. On the **Provide version information** page, enter the following information:
   + **Version title** – Buyers see this title on the product detail page and when they configure or launch the product. Use up to 64 characters. The title must be unique in your product, ignoring letter case and punctuation. For example, `1.1` and `11` count as the same title. You can't use `latest`.
   + **Release notes** – Describe what's new in this version. Use up to 30,000 characters.

1. (Optional) Under **Tags**, add tags to the change request.

1. Choose **Next**.

   The **Define delivery options** page opens. Continue with the following procedure.

**To define delivery options**

1. On the **Define delivery options** page, under **Delivery option 1**, choose a **Delivery method**.

   A version has one to four delivery options. Delivery options are sets of instructions and information that buyers can use to launch the software from your product version. Buyers know them as *fulfillment options*. Create one delivery option for each way that buyers can set up your product. To add another delivery option, choose **Add delivery option**. To remove one, choose **Remove delivery option**.
   + **Container image** – Buyers pull the container images directly into their environments.
   + **Helm chart** – Buyers install the Helm chart in their deployment environment.
   + **Amazon EKS console add-on** – Buyers install the add-on from the Amazon EKS console or with the Amazon EKS add-on APIs. For more information, see [Available Amazon EKS add-ons from Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html#workloads-add-ons-available-eks).

   To reuse a delivery option from another version, choose it from the **Existing delivery options** list instead. The copy keeps its delivery method and title, which you can't change. You can edit its other fields. Each copy counts toward the four delivery options.
**Note**  
In the AWS European Sovereign Cloud catalog, the **Amazon EKS console add-on** method isn't available. **Supported services** doesn't offer **Amazon ECS Anywhere**, **Amazon EKS Anywhere / Self-managed Kubernetes**, or **Amazon Bedrock AgentCore Runtime**.

1. For a **Container image** delivery option, complete these fields:
   + **Supported services** – Select the services where buyers can launch the software: **Amazon Elastic Container Service (ECS)**, **Amazon Elastic Kubernetes Service (EKS)**, **Amazon ECS Anywhere**, or **Amazon EKS Anywhere / Self-managed Kubernetes**. To list an AI agent or tool that runs on Amazon Bedrock AgentCore Runtime, select **Amazon Bedrock AgentCore Runtime** by itself. For the fields that this service adds, see [Listing Container-based AI agent products](listing-container-ai-agents.md).
   + **Container image** – Choose **Add container image**, and enter the **Container image URI** of an image in one of your AWS Marketplace repositories. Add one URI for each image that the version needs, up to 50. Each URI needs a tag other than `latest`, and you can't list the same URI twice.
   + **Delivery option title** – Buyers see this title as the name of the delivery option. Use up to 72 characters. Each delivery option in the version needs a different title.
   + **Delivery option description** – Buyers see this description on the product detail page and when they configure or launch the product. Use up to 1,000 characters.
   + **Usage instructions** – Enter detailed information to help your buyers use your software after launching it. You can include links to your documentation. Use up to 4,000 characters.
   + (Optional) **Deployment templates** – Add resources that buyers can use to launch the software, such as Helm charts or task definitions. For each template, choose **Add deployment template**, and enter a **Resource title** and a **Resource URL** of up to 256 characters each. You can add up to 4 templates.

1. For a **Helm chart** delivery option, complete these fields:
   + **Supported services** – Select **Amazon Elastic Kubernetes Service (EKS)**, **Amazon EKS Anywhere / Self-managed Kubernetes**, or both.
   + **Helm chart** – Enter the URI of the Helm chart in your AWS Marketplace repository. The tag must be a semantic version, such as `1.0.0`.
   + **Container image** – Add the URI of each container image that the chart uses.
   + **Delivery option title**, **Delivery option description**, and **Usage instructions** – Enter these as you would for a **Container image** delivery option.
   + (Optional) **Helm release name** – Enter the release name, up to 50 characters, for the `helm install` command. If you leave it blank, Helm generates a name.
   + **Helm installation namespace** – Enter the Kubernetes namespace where the chart is installed, up to 50 characters. Paid products need a namespace, even though the console marks this field optional. If a paid product leaves it empty, the request fails.
   + **Kubernetes service account name** – Enter the name, up to 50 characters, of the Kubernetes service account that connects to AWS Identity and Access Management (IAM) to call AWS services such as licensing or metering. The console marks this field optional. A paid product needs this name or an override parameter with a `DefaultValue` of `"${AWSMP_SERVICE_ACCOUNT}"`.
   + (Optional) **Override parameters** – Enter parameters that the Helm commands use to launch the software. Buyers can change the default values. For each parameter, choose **Add override parameter**, and enter an **Override parameter key** of up to 50 characters and an **Override parameter default** of up to 150 characters. You can add up to 15 parameters.

     Paid products must include these override parameters:
     + If the delivery option supports Amazon EKS Anywhere, include exactly one override parameter with a `DefaultValue` of `"${AWSMP_LICENSE_SECRET}"`. The product must also use contract pricing.
     + If you leave **Kubernetes service account name** empty, include exactly one override parameter with a `DefaultValue` of `"${AWSMP_SERVICE_ACCOUNT}"`.
**Note**  
AWS Partner Central has no option to hide override parameter values, such as passwords. To hide a value, use the [AWS Marketplace Catalog API](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#container-add-version). If a delivery option hides override parameter values, use the AWS Marketplace Catalog API to update the option or to reuse it in a new version. If you edit or copy those parameters in AWS Partner Central, their values are no longer hidden.

1. For an **Amazon EKS console add-on** delivery option, make sure that artifacts conform to [Requirements for Amazon EKS add-on products](container-product-policies.md#publishing-eks-add-on), and then complete these fields. A version can include only one Amazon EKS add-on delivery option. A request with more than one fails.
   + **Helm chart** – Enter the URI of the Helm chart in your AWS Marketplace repository. The tag must be a semantic version, such as `1.0.0`.
   + **Container image** – Add the URI of every container image in the Helm chart.
   + **Delivery option title**, **Delivery option description**, and **Usage instructions** – Enter these as you would for a **Container image** delivery option. All three are required.
   + **Add-on name** – Enter a unique name of 3 to 64 characters. Start with a letter or number, and use only letters, numbers, and hyphens. The Amazon EKS console shows the name as `{{seller-alias}}_{{add-on-name}}`.
   + **Add-on version** – Enter the version that buyers see when they install or upgrade the add-on, in the format `major.minor.patch`. For example, `1.2.3`.
   + **Add-on type** – Choose a category for the add-on.
   + **Kubernetes version** – Select each Kubernetes version that the add-on supports, up to 10.
   + **Architectures** – Select the platform architectures that the add-on supports: **amd64**, **arm64**, or both. For the architecture requirements, see [Requirements for Amazon EKS add-on products](container-product-policies.md#publishing-eks-add-on).
   + **Namespace** – Enter a unique Kubernetes namespace for the add-on, up to 63 characters. Use lowercase letters, numbers, and hyphens, and start and end with a letter or number. The `default`, `kube-system`, and `kube-public` namespaces aren't supported for installing third-party add-ons.
   + (Optional) **Environment override parameters** – To map a parameter in your `values.yaml` file to an Amazon EKS add-on environment value, choose **Add environment override parameter**. Enter the **Parameter key**, and choose a **Parameter value**: `${AWS_REGION}` or `${AWS_EKS_CLUSTER_NAME}`. You can add up to 2 parameters.

   A new Amazon EKS add-on delivery option always starts with Limited visibility. To test the add-on and release it to the public, see [Amazon EKS add-on delivery option](test-release-product.md#eks-addon-delivery).

1. Choose **Next**.

1. On the **Review and submit** page, review your version information and delivery options.

   To change a step, choose **Edit**.

1. Choose **Submit**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

If your request fails, see the [Add a new version Asynchronous Errors table](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#container-add-version) in the *AWS Marketplace Catalog API Reference*.

## Step 4: Update a version
<a name="container-product-updating-version"></a>

After a version is created, it can be helpful to provide updated information to your buyers by modifying the information associated with the version. For example, if you plan to restrict version 1.0 after version 1.1 is released, you can update the description of version 1.0 to direct buyers to version 1.1. Provide the date that version 1.0 will be restricted.

**To update version information**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Versions** section, select one version. Choose **Edit**, and then choose **Update version**.

   **Update version** isn't available while your product is Draft or Restricted. You can update only versions with Limited or Public visibility. You can also open the details page of a version and choose **Edit**.

1. On the **Update version information** page, update the **Release notes**.

   **Select version** shows the version that you chose. To update a different version, choose it from the **Version** list. Restricted versions aren't listed. Until the product is Public, you can also update the **Version title**.

1. (Optional) Under **Tags**, add tags to the change request.

1. Choose **Next**.

   The **Update delivery options** page opens. Continue with the following procedure.

**To update delivery options**

1. On the **Update delivery options** page, update the fields of each delivery option.

   You can't change the delivery method. The fields that you can update depend on the delivery method and visibility:
   + For every delivery option, you can update the **Delivery option description** and **Usage instructions**. For **Container image** and **Helm chart** delivery options, you can also update **Supported services**.
   + For **Helm chart** delivery options, you can always update **Helm release name**, **Helm installation namespace**, **Kubernetes service account name**, and **Override parameters**. Override parameters that you edit lose the setting that hides their values. For more information, see [Step 3: Add a new version to your container product](#add-new-version).
   + For **Container image** and **Helm chart** delivery options, you can update the **Delivery option title**, **Container image**, **Helm chart**, and **Deployment templates** until the product is Public.
   + For an **Amazon EKS console add-on** delivery option, you can update the other fields, including **Architectures**, only while the add-on delivery option has Limited visibility. After you release the add-on to the public, those fields are read-only.

1. Choose **Next**.

1. On the **Review and submit** page, review your changes.

1. Choose **Save and submit**.

   **Save and submit** is available after you change at least one field.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

## Restrict a version
<a name="container-restricting-version"></a>

To stop new buyers from subscribing to or deploying a version of your container product, restrict the version. Buyers with an active subscription keep access to the version. You must support those buyers for 90 days after you restrict the version.

The following rules apply:
+ You can restrict only versions with Public visibility.
+ At least one version must stay available, so you can't restrict every public version.
+ One request can restrict up to 50 delivery options. Restricting a version restricts each of its public delivery options, and each one counts toward the 50.
+ You can't undo a restriction.
+ Restricting an Amazon EKS add-on version doesn't remove it from the Amazon EKS console. For more information, see [Restrict a version of your Amazon EKS add-on](#restriciting-version-eks-addon).

**To restrict a version**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Versions** section, select one or more versions.

1. Choose **Edit**, and then choose **Restrict version**.

   When you select more than one version, the action is named **Restrict versions**. To restrict one version from its details page, choose **Restrict version** there.

1. In the confirmation dialog box, choose **Restrict version** or **Restrict versions**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

When the request succeeds, the version's **Version visibility** changes to **Restricted**.

## Restrict a version of your Amazon EKS add-on
<a name="restriciting-version-eks-addon"></a>

To restrict a version of your container product published as an add-on, follow [Restrict a version](#container-restricting-version). Restricting the version removes it from your AWS Marketplace listing, so new buyers can't subscribe to it. The version stays in the Amazon EKS console add-on catalog.

To remove the version from the Amazon EKS console, contact the AWS Marketplace operations team on the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1).

## Limits for container product versions
<a name="container-version-limits"></a>

The following limits apply to each container product.


| Resource | Limit | 
| --- | --- | 
| Repositories per product | 70 | 
| Delivery options per version | 4 | 
| Amazon EKS add-on delivery options per version | 1 | 
| Container images or artifacts per delivery option | 50 | 
| Container images per delivery option that supports Amazon Bedrock AgentCore | 1 | 
| Deployment templates per Container image delivery option | 4 | 
| Override parameters per Helm chart delivery option | 15 | 
| Environment override parameters per Amazon EKS add-on delivery option | 2 | 
| Kubernetes versions per Amazon EKS add-on delivery option | 10 | 
| Delivery options per request to restrict versions or to update version visibility | 50 | 
| Version title length | 64 characters | 
| Release notes length | 30,000 characters | 
| Delivery option title length | 72 characters | 
| Delivery option description length | 1,000 characters | 
| Usage instructions length | 4,000 characters | 
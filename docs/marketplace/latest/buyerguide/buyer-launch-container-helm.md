

# Launching with a Helm fulfillment option
<a name="buyer-launch-container-helm"></a>

For a fulfillment option with a **Helm** delivery method, use the seller-provided instructions to launch the product. This is done by installing a Helm chart using the Helm CLI. You can launch the application on an existing Amazon EKS cluster, or a self-managed cluster on EKS Anywhere, Amazon Elastic Compute Cloud (Amazon EC2), or on-premises.

**Note**  
Your launch environment must use Helm CLI version 3.7.1. For a list of Helm versions, see [Helm releases on GitHub](https://github.com/helm/helm/releases).

The instructions are provided by the seller and are different for each seller and product. The general steps to launch a product with a Helm fulfillment option are as follows:

**To launch a product with a Helm fulfillment option**

1. Follow steps 1–6 of [Launching container software from AWS Marketplace](buyer-configuring-a-product.md), and choose a fulfillment option with a **Helm chart** delivery method.

1. In **Launch target**, choose the environment that you want to deploy on:
   + Choose **Amazon managed Kubernetes** to deploy the application in Amazon EKS.
   + Choose **Self-managed Kubernetes** to deploy the application in [EKS Anywhere](https://anywhere.eks.amazonaws.com/docs/overview/) or on any Kubernetes cluster running in Amazon EC2 or on-premises.

1. If launching in an **Amazon managed Kubernetes** cluster:

   1. To launch on an existing cluster in Amazon EKS, under **Launch method**, choose **Launch on existing cluster** and follow the **Launch instructions**. The instructions include creating an AWS Identity and Access Management (IAM) role and launching the application. Verify that you're using Helm CLI version 3.7.1.

1. If launching in a **Self-managed Kubernetes** cluster:

   1. Verify that you're using Helm CLI version 3.7.1.

   1. Choose **Create token** to generate a license token and IAM role. This token and role is used to communicate with AWS License Manager to validate product entitlements.
**Note**  
You must have `AWSServiceRoleForAWSLicenseManagerRole` in your account to use **Create token**. The maximum number of license tokens for an account is 10.

   1. Choose **Download as CSV** to download a .csv file with the generated token information. As with all secrets and passwords, store the .csv file in a secure location.

   1. Run the commands in **Save as Kubernetes secret** to save the license token and IAM role as a secret in your Kubernetes cluster. This secret is used when you install the Helm chart and launch the application. AWS Marketplace uses the secret to verify the entitlement for this product.

   1. Run the commands in **Launch application using token** to install the Helm chart that deploys the application to your cluster.

   1. Choose **Usage instructions** for documentation from the seller about how to configure and use the product after launching.

   1. *Optional - *Use the provided commands in **[Optional] Download artifacts** to download the product's container images and Helm charts locally.
# Launching with a Helm fulfillment

option

For a fulfillment option with a **Helm** delivery method, use the
seller-provided instructions to launch the product. This is done by installing a Helm chart
using the Helm CLI. You can launch the application on an existing Amazon EKS cluster, or a
self-managed cluster on EKS Anywhere, Amazon Elastic Compute Cloud (Amazon EC2), or
on-premises.

###### Note

Your launch environment must use Helm CLI version 3.7.1. For a list of Helm versions,
see [Helm releases on
GitHub](https://github.com/helm/helm/releases "https://github.com/helm/helm/releases").

If the seller has enabled Quick Launch, you can use it to launch the application. Quick Launch is a
feature in AWS Marketplace that uses CloudFormation to create an Amazon EKS cluster and launch the application on
it. For more information about Quick Launch, see [Launching container products with Quick Launch](quick-launch.md#buyer-launch-container-quicklaunch "quick-launch.md#buyer-launch-container-quicklaunch").

The instructions are provided by the seller and are different for each seller and
product. The general steps to launch a product with a Helm fulfillment option are as
follows:

###### To launch a product with a Helm fulfillment option

1. Follow steps 1–6 of [Launching container software from
   AWS Marketplace](buyer-configuring-a-product.md "buyer-configuring-a-product.md"), and choose a fulfillment option with a
   **Helm chart** delivery method.
2. In **Launch target**, choose the environment that you want to
   deploy on:
   - Choose **Amazon managed Kubernetes** to deploy the application
     in Amazon EKS. If the seller has enabled Quick Launch, you can use it to create a new Amazon EKS
     cluster and launch on it.
   - Choose **Self-managed Kubernetes** to deploy the application in
     [EKS
     Anywhere](https://anywhere.eks.amazonaws.com/docs/overview/ "https://anywhere.eks.amazonaws.com/docs/overview/") or on any Kubernetes cluster running in Amazon EC2 or
     on-premises.

3. If launching in an **Amazon managed Kubernetes** cluster:
   1. To launch on an existing cluster in Amazon EKS, under **Launch
      method**, choose **Launch on existing cluster** and
      follow the **Launch instructions**. The instructions include
      creating an AWS Identity and Access Management (IAM) role and launching the application. Verify that you're
      using Helm CLI version 3.7.1.
   2. To use Quick Launch to create a new Amazon EKS cluster and launch on it, under
      **Launch method**, choose **Launch on a new EKS cluster
      with Quick Launch**. Choose **Launch** to be redirected to
      create a stack in the AWS CloudFormation console. This stack will create an Amazon EKS cluster and
      deploy the application by installing the seller-provided Helm chart.
   3. On the **Quick create stack** page, in **Stack
      name**, provide a name for this stack.
   4. Review the information in the **Parameters** tile and provide
      any necessary information. Review and select the acknowledgements in
      **Capabilities** and choose **Create
      stack**.###### Note

For more information about Quick Launch, including information about CloudFormation, stacks, and
the created Amazon EKS cluster, see [Launching container products with Quick Launch](quick-launch.md#buyer-launch-container-quicklaunch "quick-launch.md#buyer-launch-container-quicklaunch"). 4. If launching in a **Self-managed Kubernetes** cluster:

    1. Verify that you're using Helm CLI version 3.7.1.
    2. Choose **Create token** to generate a license token and IAM
     role. This token and role is used to communicate with AWS License Manager to validate product
     entitlements.


    ###### Note

    You must have `AWSServiceRoleForAWSLicenseManagerRole` in your
     account to use **Create token**. The maximum number of license
     tokens for an account is 10.
    3. Choose **Download as CSV** to download a .csv file with the
     generated token information. As with all secrets and passwords, store the .csv file
     in a secure location.
    4. Run the commands in **Save as Kubernetes secret** to save the
     license token and IAM role as a secret in your Kubernetes cluster. This secret is
     used when you install the Helm chart and launch the application. AWS Marketplace uses the
     secret to verify the entitlement for this product.
    5. Run the commands in **Launch application using token** to
     install the Helm chart that deploys the application to your cluster.
    6. Choose **Usage instructions** for documentation from the seller
     about how to configure and use the product after launching.
    7. *Optional -* Use the provided commands in
     **[Optional] Download artifacts** to download the product's
     container images and Helm charts locally.

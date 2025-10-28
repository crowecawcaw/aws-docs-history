# Container product delivery methods

A product in AWS Marketplace is considered a container product if the seller has provided at least
one fulfillment option with either a **Container image**, **Helm
chart**, or **Add-on for Amazon EKS** delivery method.

## Container image delivery

method

For a fulfillment option with a **Container image** delivery method,
use the seller-provided instructions to launch the product. This is done by pulling Docker
images directly from the AWS Marketplace registry on Amazon Elastic Container Registry. For more information about
launching with this delivery method, see [Launching with a Container image fulfillment option](buyer-launch-container-image.md "buyer-launch-container-image.md").

## Helm chart delivery

method

For a fulfillment option with a **Helm chart** delivery method, use the
seller-provided instructions or deployment template to launch the product. This is done by
installing a Helm chart using the Helm CLI. You can launch the application on an existing
Amazon EKS cluster, or a self-managed cluster on EKS Anywhere, Amazon Elastic Compute Cloud (Amazon EC2),
or on-premises. For more information about launching with this delivery method, see [Launching with a Helm fulfillment
option](buyer-launch-container-helm.md "buyer-launch-container-helm.md").

## Add-on for Amazon EKS

delivery method

For a fulﬁllment option with an **Add-on for Amazon EKS** delivery method,
use the Amazon EKS console or Amazon EKS CLI to launch the product. For more information about Amazon EKS
add-ons, see [Amazon EKS add-ons](../../../eks/latest/userguide/eks-add-ons.md "../../../eks/latest/userguide/eks-add-ons.md").

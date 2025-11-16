AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Configuring Amazon EKS Anywhere on AWS Snow for disconnected operation

Complete this additional configuration of Amazon EKS Anywhere on the Snowball Edge device while it's
connected to a network to prepare Amazon EKS Anywhere to run in an environment without an external network connection.

To configure Amazon EKS Anywhere for disconnected use with your own local, private Kubernetes registry, see [Registry Mirror configuration](https://anywhere.eks.amazonaws.com/docs/reference/clusterspec/optional/registrymirror/ "https://anywhere.eks.amazonaws.com/docs/reference/clusterspec/optional/registrymirror/") in the EKS Anywhere documentation.

If you created a Harbor private registry AMI, follow the procedures in this section.

###### Topics

- [Configure the Harbor registry on a Snowball Edge device](#configure-harbor-snow "#configure-harbor-snow")
- [Use the Harbor registry on the Amazon EKS Anywhere admin instance on a Snowball Edge](#use-local-registry-eksa-instance "#use-local-registry-eksa-instance")

## Configure the Harbor registry on a Snowball Edge device

See [Configure Harbor on a Snowball Edge device](https://github.com/aws-samples/aws-snow-tools-for-eks-anywhere/tree/main/container-registry-ami-builder#configure-harbor-on-a-snowball-edge-device "https://github.com/aws-samples/aws-snow-tools-for-eks-anywhere/tree/main/container-registry-ami-builder#configure-harbor-on-a-snowball-edge-device").

## Use the Harbor registry on the Amazon EKS Anywhere admin instance on a Snowball Edge

See [Import Amazon EKS Anywhere container images to the local Harbor registry on a Snowball Edge device](https://github.com/aws-samples/aws-snow-tools-for-eks-anywhere/tree/main/container-registry-ami-builder#import-eks-anywhere-container-images-to-the-local-harbor-registry-on-a-snowball-device "https://github.com/aws-samples/aws-snow-tools-for-eks-anywhere/tree/main/container-registry-ami-builder#import-eks-anywhere-container-images-to-the-local-harbor-registry-on-a-snowball-device").

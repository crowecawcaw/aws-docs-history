Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Ordering a Snowball Edge device for use with Amazon EKS Anywhere on AWS Snow

To order your Snowball Edge compute optimized, see [Creating a job to order a Snowball Edge device](create-job-common.md "create-job-common.md") in this guide and keep these
items in mind during the ordering process:

- In step 1, choose the **Local compute and storage only** job type.
- In step 2, choose the **Snowball Edge Compute Optimized** device type.
- In step 3, choose **Amazon EKS Anywhere on AWS Snow**, then choose the
  Kubernetes version that you need.

###### Note

In order to deliver the latest software, we may configure the device with a version of ESK Anywhere newer than the one that is currently available. For more info, [Versioning](https://anywhere.eks.amazonaws.com/docs/concepts/support-versions/ "https://anywhere.eks.amazonaws.com/docs/concepts/support-versions/") in the _Amazon EKS User Guide_.

We recommend that you create your Kubernetes cluster with the latest available Kubernetes version supported by Amazon EKS Anywhere. For more information, see [Amazon EKS-Anywhere Versioning](https://anywhere.eks.amazonaws.com/docs/concepts/support-versions/ "https://anywhere.eks.amazonaws.com/docs/concepts/support-versions/"). If your application requires a specific version of Kubernetes, use any version of Kubernetes offered in standard or extended support by Amazon EKS. Consider the release and support dates of Kubernetes versions when planning the lifecycle of your deployment. This will help you avoid the potential loss of support for the version of Kubernetes you intend to use. For more information, see [Amazon EKS Kubernetes release calendar](../../../eks/latest/userguide/kubernetes-versions.md#kubernetes-release-calendar "../../../eks/latest/userguide/kubernetes-versions.md#kubernetes-release-calendar").

- Choose AMIs to include on your device, including the EKS Distro AMI (see [Create an Ubuntu EKS Distro AMI for the Snowball Edge](eksa-gettingstarted.md#create-eksd-ami "eksa-gettingstarted.md#create-eksd-ami")) and, optionally, the Harbor
  AMI that you built (see [Build a Harbor AMI for the Snowball Edge](eksa-gettingstarted.md#existing-private-registry "eksa-gettingstarted.md#existing-private-registry")).
- If you need multiple Snowball Edge devices for high availability, choose the number
  of devices that you need from **High Availability**.
  After you receive your Snowball Edge device or devices, configure Amazon EKS Anywhere according to
  [Configuring and running Amazon EKS Anywhere on Snowball Edge devices](eksa-configuration.md "eksa-configuration.md").

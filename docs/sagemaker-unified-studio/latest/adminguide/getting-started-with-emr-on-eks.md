# Getting started with Amazon EMR on EKS in Amazon SageMaker Unified Studio

Before you begin with Amazon EMR on EKS, you must have a compatible Amazon EKS cluster.
If you do not have an existing Amazon EKS cluster, see
[Get started with Amazon EKS](../../../eks/latest/userguide/getting-started.md "../../../eks/latest/userguide/getting-started.md")
for more information regarding cost, installation and management of an Amazon EKS cluster.

Amazon EMR on EKS and Amazon SageMaker Unified Studio require additional Amazon EKS cluster configurations granting minimum access controls and connectivity.
Review your Amazon EKS cluster configuration and ensure all requirements are fulfilled:

1. [Install and configure the Load Balancer Controller for your Amazon EKS cluster](../../../eks/latest/userguide/aws-load-balancer-controller.md "../../../eks/latest/userguide/aws-load-balancer-controller.md")
2. [Enable Amazon EKS cluster access for Amazon EMR on EKS and Amazon SageMaker Unified Studio](enable-eks-cluster-access-for-emr-on-eks-and-sagemaker-unified-studio.md "enable-eks-cluster-access-for-emr-on-eks-and-sagemaker-unified-studio.md")

Additionally, Amazon EKS clusters in a different account or Amazon VPC network than your Amazon SageMaker Unified Studio domain require additional configuration.
Review your Amazon EKS cluster configuration and ensure all requirements are fulfilled:

1. [Enable cross-account access for Amazon EMR on EKS using Amazon SageMaker Unified Studio associated domains](enable-cross-account-access-using-associated-domains.md "enable-cross-account-access-using-associated-domains.md")
2. [Enable cross-network access for Amazon SageMaker Unified Studio using VPC peering connections](enable-cross-network-access-using-vpc-peering.md "enable-cross-network-access-using-vpc-peering.md")

## Configure project profiles in Amazon SageMaker Unified Studio for Amazon EMR on EKS

For data workers to use Amazon EMR on EKS in Amazon SageMaker Unified Studio, administrators must configure project profiles
with Amazon EMR on EKS environment blueprint configurations.

###### Note

Administrators can configure multiple environment blueprint configurations using different Amazon EKS clusters in the same project profile.
Data workers can view environment blueprint configurations and select a specific Amazon EKS cluster when creating Amazon EMR on EKS resources in a Amazon SageMaker Unified Studio project.

1. Navigate to the [Amazon SageMaker Unified Studio management console](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone").
2. From the navigation bar, select **Domains**.
   For cross-account Amazon EKS clusters, select **Associated domains**.
3. Select the name of the domain you want to configure Amazon EMR on EKS for.
4. In the domain management view, navigate to **Project profiles**.
5. Search for and select your target project profile.
6. In the project profile management view, navigate to the **Blueprint deployment settings** view
   and select **Blueprint deployment settings**.
7. In the **Blueprint** section, select **EmrOnEks** from the dropdown.
8. In the **Account and region** section, specify the same AWS account and AWS region
   as your Amazon EKS cluster.
9. In the **Blueprint parameters** section,
   specify the Amazon EKS cluster ARN as the `eksClusterArn` user parameter value.
10. At the bottom of the page, select **Add blueprint deployment settings**
    to create your Amazon EMR on EKS environment blueprint configuration.

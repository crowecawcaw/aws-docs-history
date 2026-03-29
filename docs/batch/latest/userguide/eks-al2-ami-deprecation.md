# Amazon EKS Amazon Linux 2 AMI deprecation

AWS ended support for Amazon EKS optimized Amazon Linux 2 AMIs on November 26, 2025. On
October 27, 2025, AWS Batch changed the default AMI for new Amazon EKS compute environments to Amazon
Linux 2023. Amazon EKS optimized Amazon Linux 2 AMIs no longer receive software updates, security
patches, or bug fixes from AWS.

###### Important

If you have AWS Batch Amazon EKS compute environments still using Amazon Linux 2, we strongly
recommend migrating to Amazon Linux 2023. It is your responsibility to maintain Amazon EKS optimized
Amazon Linux 2 compute environments after end-of-life.

For more information about the Amazon EKS AL2 end-of-life, see [Amazon EKS AMI deprecation FAQs](../../../eks/latest/userguide/eks-ami-deprecation-faqs.md "../../../eks/latest/userguide/eks-ami-deprecation-faqs.md") in
the _Amazon EKS User Guide_.

For help migrating AWS Batch Amazon EKS compute environments from Amazon Linux 2 to Amazon Linux
2023, see [How to upgrade from EKS AL2 to EKS AL2023](eks-migration-2023.md "eks-migration-2023.md").

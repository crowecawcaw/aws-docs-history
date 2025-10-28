# Amazon EKS Amazon Linux 2 AMI deprecation

AWS will end support for Amazon EKS optimized Amazon Linux 2 AMIs, effective 11/26/25. We
recommend migrating AWS Batch Amazon EKS compute environments to Amazon Linux 2023 prior to 11/26/25 to maintain optimal performance and security.

While you can continue using Batch-provided Amazon EKS optimized Amazon Linux 2 AMIs on your
Amazon EKS compute environments beyond the 11/26/25 end-of-support date, these compute
environments will no longer receive any new software updates, security patches, or bug fixes from
AWS. It is your responsibility to maintain these compute environments on the Amazon EKS optimized
Amazon Linux 2 AMI after end-of-life.

For more information about the Amazon EKS AL2 end-of-life, see [Amazon EKS AMI deprecation FAQs](../../../eks/latest/userguide/eks-ami-deprecation-faqs.md "../../../eks/latest/userguide/eks-ami-deprecation-faqs.md") in
the _Amazon EKS User Guide_.

For help migrating AWS Batch Amazon EKS compute environments from Amazon Linux 2 to Amazon Linux
2023, see [How to upgrade from EKS AL2 to EKS AL2023](eks-migration-2023.md "eks-migration-2023.md").

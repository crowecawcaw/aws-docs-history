# Mixed AMI environments

You can use launch template overrides to create compute environments with both Amazon
Linux 2 (AL2) and Amazon Linux 2023 (AL2023) AMIs. This is useful for using different AMIs for
different architectures or during migration periods when transitioning from AL2 to AL2023.

###### Note

AWS will end support for Amazon EKS AL2-optimized and AL2-accelerated AMIs, starting
11/26/25. While you can continue using AWS Batch-provided Amazon EKS optimized Amazon Linux 2 AMIs on
your Amazon EKS compute environments beyond the 11/26/25 end-of-support date, these compute
environments will no longer receive any new software updates, security patches, or bug fixes
from AWS. Mixed AMI environments can be useful during the transition period, allowing you to
gradually migrate workloads to AL2023 while maintaining compatibility with existing AL2-based
workloads.

Example configuration using both AMI types:

```
{
  "computeResources": {
    "launchTemplate": {
      "launchTemplateId": "TemplateId",
      "version": "1",
      "userdataType": "EKS_BOOTSTRAP_SH",
      "overrides": [
        {
          "instanceType": "c5.large",
          "imageId": "ami-al2-custom",
          "userdataType": "EKS_BOOTSTRAP_SH"
        },
        {
          "instanceType": "c6a.large",
          "imageId": "ami-al2023-custom",
          "userdataType": "EKS_NODEADM"
        }
      ]
    },
    "instanceTypes": ["c5.large", "c6a.large"]
  }
}
```

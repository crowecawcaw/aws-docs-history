# `Image` section

###### Note

Unsupported versions of the official AMIs distributed by AWS ParallelCluster will be made
unavailable after 18 months of inactivity. These old images contain outdated software and cannot receive
support in case of issues. We strongly suggest to move to the latest supported version.

**(Required)** Defines the operating system for the cluster.

```
Image:
  Os: `string`
  CustomAmi: `string`
```

## `Image` properties

`Os` (**Required**,
`String`)

Specifies the operating system to use for the cluster. The supported values are `alinux2`,
`alinux2023`, `ubuntu2404`, `ubuntu2204`, `rhel8`,
`rocky8`, `rhel9`, `rocky9`.

###### Note

RedHat Enterprise Linux 8.7 (`rhel8`) is added starting in AWS ParallelCluster version 3.6.0.

If you configure your cluster to use `rhel`, the on-demand cost for any
instance type is higher than when you configure your cluster to use other supported
operation systems. For more information about pricing, see [On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand "https://aws.amazon.com/ec2/pricing/on-demand") and
[How is
Red Hat Enterprise Linux on Amazon EC2 offered and priced?](https://aws.amazon.com/partners/redhat/faqs/#Pricing_and_Billing "https://aws.amazon.com/partners/redhat/faqs/#Pricing_and_Billing").

RedHat Enterprise Linux 9 (rhel9) is added starting in AWS ParallelCluster version 3.9.0.

All AWS commercial Regions support all of the following operating systems.

| Partition (AWS Regions)                                 | `alinux2` | `ubuntu2204` | `ubuntu2404` | `rhel8` | `rhel9` | `alinux2023` |
| ------------------------------------------------------- | --------- | ------------ | ------------ | ------- | ------- | ------------ |
| Commercial (All AWS Regions not specifically mentioned) | True      | True         | True         | True    | True    | True         |
| AWS GovCloud (US-East) (`us-gov-east-1`)                | True      | True         | True         | True    | True    | True         |
| AWS GovCloud (US-West) (`us-gov-west-1`)                | True      | True         | True         | True    | True    | True         |
| China (Beijing) (`cn-north-1`)                          | True      | True         | True         | True    | True    | True         |
| China (Ningxia) (`cn-northwest-1`)                      | True      | True         | True         | True    | True    | True         |

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

###### Note

AWS ParallelCluster 3.8.0 supports Rocky Linux 8, but pre-built Rocky Linux 8 AMIs (for x86 and
ARM architectures) are not available. AWS ParallelCluster 3.8.0 supports creating
clusters with Rocky Linux 8 using custom AMIs. For more information refer to [Operating system considerations](operating-systems-v3.md#OS-Consideration-v3 "operating-systems-v3.md#OS-Consideration-v3").
AWS ParallelCluster 3.9.0 supports Rocky Linux 9, but pre-built Rocky Linux 9 AMIs (for
x86 and ARM architectures) are not available. AWS ParallelCluster 3.9.0 supports
creating clusters with Rocky Linux 9 using custom AMIs. For more information refer to
[Operating System Considerations](operating-systems-v3.md#OS-Consideration-v3 "operating-systems-v3.md#OS-Consideration-v3").

`CustomAmi` (**Optional**, `String`)

Specifies the ID of a custom AMI to use for the head and compute nodes instead of the default AMI. For more
information, see [AWS ParallelCluster AMI customization](custom-ami-v3.md "custom-ami-v3.md").

If the custom AMI requires additional permissions for its launch, these permissions must be added to both the user and head node policies.

For example, if a custom AMI has an encrypted snapshot associated with it, the following additional policies are required in both the user and head node policies:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey",
 "kms:ReEncrypt*",
 "kms:CreateGrant",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`<AWS_KMS_KEY_ID>`"
 ]
 }
 ]
}`

```

To build a RedHat Enterprise Linux custom AMI, you must configure the OS for installing
the packages that are provided by the RHUI (AWS) repositories:
`rhel-<version>-baseos-rhui-rpms`,
`rhel-<version>-appstream-rhui-rpms`, and
`codeready-builder-for-rhel-<version>-rhui-rpms`. Moreover, the
repositories on the custom AMI must contain `kernel-devel` packages
on the same version as the running kernel version. kernel.

###### Known limitations:

- Only RHEL 8.2 and later versions support FSx for Lustre.
- RHEL 8.7 kernel version 4.18.0-425.3.1.el8 doesn't support FSx for Lustre.
- Only RHEL 8.4 and later versions support EFA.
- AL23 doesn't support NICE DCV, as it doesn't include a graphical desktop
  environment, which is required to run NICE DCV. For more information, see the
  official [NICE DCV
  documentation](../../../dcv.md "../../../dcv.md").

To troubleshoot custom AMI validation warnings, see [Troubleshooting custom AMI issues](troubleshooting-v3-custom-amis.md "troubleshooting-v3-custom-amis.md").

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

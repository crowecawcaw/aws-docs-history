**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Retrieve IAM information about an Amazon EKS add-on

Before you create an add-on, use the AWS CLI to determine:

- If the add-on requires IAM permissions
- The suggested IAM policy to use

## Procedure

1. Determine the name of the add-on you want to install, and the Kubernetes version of your cluster. For more information about add-ons, see [Amazon EKS add-ons](eks-add-ons.md "eks-add-ons.md").
2. Use the AWS CLI to determine if the add-on requires IAM permissions.

```
aws eks describe-addon-versions \
--addon-name <addon-name> \
--kubernetes-version <kubernetes-version>
```

For example:

```
aws eks describe-addon-versions \
--addon-name aws-ebs-csi-driver \
--kubernetes-version 1.30
```

Review the following sample output. Note that `requiresIamPermissions` is `true`, and the default add-on version. You need to specify the add-on version when retrieving the recommended IAM policy.

```
{
    "addons": [
        {
            "addonName": "aws-ebs-csi-driver",
            "type": "storage",
            "addonVersions": [
                {
                    "addonVersion": "v1.31.0-eksbuild.1",
                    "architecture": [
                        "amd64",
                        "arm64"
                    ],
                    "compatibilities": [
                        {
                            "clusterVersion": "1.30",
                            "platformVersions": [
                                "*"
                            ],
                            "defaultVersion": true
                        }
                    ],
                    "requiresConfiguration": false,
                    "requiresIamPermissions": true
                },
[...]
```

3. If the add-on requires IAM permissions, use the AWS CLI to retrieve a recommended IAM policy.

```
aws eks describe-addon-configuration \
--query podIdentityConfiguration \
--addon-name <addon-name> \
--addon-version <addon-version>
```

For example:

```
aws eks describe-addon-configuration \
--query podIdentityConfiguration \
--addon-name aws-ebs-csi-driver \
--addon-version v1.31.0-eksbuild.1
```

Review the following output. Note the `recommendedManagedPolicies`.

```
[
    {
        "serviceAccount": "ebs-csi-controller-sa",
        "recommendedManagedPolicies": [
            "arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy"
        ]
    }
]
```

4. Create an IAM role and attach the recommended Managed Policy. Alternatively, review the managed policy and scope down the permissions as appropriate. For more information see [Create a Pod Identity association (AWS Console)](pod-id-association.md#pod-id-association-create "pod-id-association.md#pod-id-association-create").

## Pod Identity Support Reference

The following table indicates if certain Amazon EKS add-ons support EKS Pod Identity.

| Add-on name                                                                                                                                                                      | Pod identity support | Minimum version required |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------ | ------------------------------------------------ |
| [Amazon EBS CSI Driver](workloads-add-ons-available-eks.md#add-ons-aws-ebs-csi-driver "workloads-add-ons-available-eks.md#add-ons-aws-ebs-csi-driver")                           | Yes                  | v1.26.0-eksbuild.1       |
| [Amazon VPC CNI](workloads-add-ons-available-eks.md#add-ons-vpc-cni "workloads-add-ons-available-eks.md#add-ons-vpc-cni")                                                        | Yes                  | v1.15.5-eksbuild.1       |
| [Amazon EFS CSI Driver](workloads-add-ons-available-eks.md#add-ons-aws-efs-csi-driver "workloads-add-ons-available-eks.md#add-ons-aws-efs-csi-driver")                           | Yes                  | v2.0.5-eksbuild.1        |
| [AWS Distro for OpenTelemetry](workloads-add-ons-available-eks.md#add-ons-adot "workloads-add-ons-available-eks.md#add-ons-adot")                                                | Yes                  | v0.94.1-eksbuild.1       |
| [Mountpoint for Amazon S3 CSI Driver](workloads-add-ons-available-eks.md#mountpoint-for-s3-add-on "workloads-add-ons-available-eks.md#mountpoint-for-s3-add-on")                 | No                   | N/A                      |
| [Amazon CloudWatch Observability agent](workloads-add-ons-available-eks.md#amazon-cloudwatch-observability "workloads-add-ons-available-eks.md#amazon-cloudwatch-observability") | Yes                  | v3.1.0-eksbuild.1        | This table was last updated on October 28, 2024. |

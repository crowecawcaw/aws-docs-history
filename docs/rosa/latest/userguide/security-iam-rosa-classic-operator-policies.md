# ROSA classic operator policies

This section provides details about the operator policies that are required for ROSA classic.
Before you can create a ROSA classic cluster, you must first attach these policies to the relevant operator roles.
A unique set of operator roles is required for each cluster.

These permissions are needed to allow the OpenShift operators to manage ROSA classic cluster nodes.
You can assign a custom prefix to the policy names to simplify policy management (for example, `ManagedOpenShift-openshift-ingress-operator-cloud-credentials`).

## [Prefix]-openshift-ingress-operator-cloud-credentials

You can attach `[Prefix]-openshift-ingress-operator-cloud-credentials` to your IAM entities.
This policy grants required permissions to the Ingress Operator to provision and manage load balancers and DNS configurations for external cluster access.
The policy also allows the Ingress Operator to read and filter Route 53 resource tag values to discover hosted zones.
For more information about the operator, see [OpenShift Ingress Operator](https://github.com/openshift/cluster-ingress-operator "https://github.com/openshift/cluster-ingress-operator") in the OpenShift GitHub documentation.

Permissions defined in this policy document specify which actions are allowed or denied.

```
 {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Action": [
                "elasticloadbalancing:DescribeLoadBalancers",
                "route53:ListHostedZones",
                "route53:ListTagsForResources",
                "route53:ChangeResourceRecordSets",
                "tag:GetResources"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

## [Prefix]-openshift-cluster-csi-drivers-ebs-cloud-credentials

You can attach `[Prefix]-openshift-cluster-csi-drivers-ebs-cloud-credentials` to your IAM entities.
This policy grants required permissions to the Amazon EBS CSI Driver Operator to install and maintain the Amazon EBS CSI driver on a ROSA classic cluster.
For more information about the operator, see [aws-ebs-csi-driver-operator](https://github.com/openshift/aws-ebs-csi-driver-operator#aws-ebs-csi-driver-operator "https://github.com/openshift/aws-ebs-csi-driver-operator#aws-ebs-csi-driver-operator") in the OpenShift GitHub documentation.

Permissions defined in this policy document specify which actions are allowed or denied.

```
 {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Action": [
                "ec2:AttachVolume",
                "ec2:CreateSnapshot",
                "ec2:CreateTags",
                "ec2:CreateVolume",
                "ec2:DeleteSnapshot",
                "ec2:DeleteTags",
                "ec2:DeleteVolume",
                "ec2:DescribeAvailabilityZones",
                "ec2:DescribeInstances",
                "ec2:DescribeSnapshots",
                "ec2:DescribeTags",
                "ec2:DescribeVolumes",
                "ec2:DescribeVolumesModifications",
                "ec2:DetachVolume",
                "ec2:EnableFastSnapshotRestores",
                "ec2:ModifyVolume"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

## [Prefix]-openshift-machine-api-aws-cloud-credentials

You can attach `[Prefix]-openshift-machine-api-aws-cloud-credentials` to your IAM entities.
This policy grants required permissions to the Machine Config Operator to describe, run, and terminate Amazon EC2 instances managed as worker nodes.
This policy also grants permissions to allow for disk encryption of the worker node root volume using AWS KMS keys.
For more information about the operator, see [machine-config-operator](https://github.com/openshift/machine-config-operator "https://github.com/openshift/machine-config-operator") in the OpenShift GitHub documentation.

Permissions defined in this policy document specify which actions are allowed or denied.

```
 {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Action": [
                "ec2:CreateTags",
                "ec2:DescribeAvailabilityZones",
                "ec2:DescribeDhcpOptions",
                "ec2:DescribeImages",
                "ec2:DescribeInstances",
                "ec2:DescribeInternetGateways",
                "ec2:DescribeInstanceTypes",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeRegions",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs",
                "ec2:RunInstances",
                "ec2:TerminateInstances",
                "elasticloadbalancing:DescribeLoadBalancers",
                "elasticloadbalancing:DescribeTargetGroups",
                "elasticloadbalancing:DescribeTargetHealth",
                "elasticloadbalancing:RegisterInstancesWithLoadBalancer",
                "elasticloadbalancing:RegisterTargets",
                "elasticloadbalancing:DeregisterTargets",
                "iam:CreateServiceLinkedRole"
            ],
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Action": [
                "kms:Decrypt",
                "kms:Encrypt",
                "kms:GenerateDataKey",
                "kms:GenerateDataKeyWithoutPlainText",
                "kms:DescribeKey"
            ],
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Action": [
                "kms:RevokeGrant",
                "kms:CreateGrant",
                "kms:ListGrants"
            ],
            "Effect": "Allow",
            "Resource": "*",
            "Condition": {
                "Bool": {
                    "kms:GrantIsForAWSResource": true
                }
            }
        }
    ]
}
```

## [Prefix]-openshift-cloud-credential-operator-cloud-credentials

You can attach `[Prefix]-openshift-cloud-credential-operator-cloud-credentials` to your IAM entities.
This policy grants required permissions to the Cloud Credential Operator to retrieve IAM user details, including access key IDs, attached inline policy documents, user’s creation date, path, user ID, and Amazon Resource Name (ARN).
For more information about the operator, see [cloud-credential-operator](https://github.com/openshift/cloud-credential-operator "https://github.com/openshift/cloud-credential-operator") in the OpenShift GitHub documentation.

Permissions defined in this policy document specify which actions are allowed or denied.

```
 {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Action": [
                "iam:GetUser",
                "iam:GetUserPolicy",
                "iam:ListAccessKeys"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

## [Prefix]-openshift-image-registry-installer-cloud-credentials

You can attach `[Prefix]-openshift-image-registry-installer-cloud-credentials` to your IAM entities.
This policy grants required permissions to the Image Registry Operator to provision and manage resources for ROSA classic’s in-cluster image registry and dependent services, including Amazon S3.
This is required so that the operator can install and maintain the internal registry of a ROSA classic cluster.
For more information about the operator, see [Image Registry Operator](https://github.com/openshift/cluster-image-registry-operator#image-registry-operator "https://github.com/openshift/cluster-image-registry-operator#image-registry-operator") in the OpenShift GitHub documentation.

Permissions defined in this policy document specify which actions are allowed or denied.

```
 {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:CreateBucket",
                "s3:DeleteBucket",
                "s3:PutBucketTagging",
                "s3:GetBucketTagging",
                "s3:PutBucketPublicAccessBlock",
                "s3:GetBucketPublicAccessBlock",
                "s3:PutEncryptionConfiguration",
                "s3:GetEncryptionConfiguration",
                "s3:PutLifecycleConfiguration",
                "s3:GetLifecycleConfiguration",
                "s3:GetBucketLocation",
                "s3:ListBucket",
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:ListBucketMultipartUploads",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

## [Prefix]-openshift-cloud-network-config-controller-cloud-cr

You can attach `[Prefix]-openshift-cloud-network-config-controller-cloud-cr` to your IAM entities.
This policy grants required permissions to the Cloud Network Config Controller Operator to provision and manage networking resources for use by the ROSA classic cluster networking overlay.
The operator uses these permissions to manage private IP addresses for Amazon EC2 instances as part of the ROSA classic cluster.
For more information about the operator, see [Cloud-network-config-controller](https://github.com/openshift/cloud-network-config-controller#cloud-network-config-controller-cncc "https://github.com/openshift/cloud-network-config-controller#cloud-network-config-controller-cncc") in the OpenShift GitHub documentation.

Permissions defined in this policy document specify which actions are allowed or denied.

```
 {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeInstanceStatus",
                "ec2:DescribeInstanceTypes",
                "ec2:UnassignPrivateIpAddresses",
                "ec2:AssignPrivateIpAddresses",
                "ec2:UnassignIpv6Addresses",
                "ec2:AssignIpv6Addresses",
                "ec2:DescribeSubnets",
                "ec2:DescribeNetworkInterfaces"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

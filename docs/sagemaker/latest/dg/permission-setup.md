# Set up permissions

## Roles required for Add-on and its dependencies

### IAM Roles Required for SageMaker Spaces on SageMaker HyperPod

When enabling **SageMaker Spaces (a.k.a\*\***SageMaker IDE / Notebooks)\*\* features on a SageMaker
HyperPod (EKS) cluster, several IAM roles must be created and assigned. These
roles support secure access, routing, remote IDE sessions, and EBS storage
provisioning. The following table summarizes the four roles and when they are
required.

### Role Summary Table

| IAM Role                           | Required?                      | Purpose                                                                                                                                    | Who Uses It?                                    | Customization allowed by SageMaker Console? |
| ---------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- | ------------------------------------------- |
| Spaces Add-on Execution Role       | Always required                | Allows the Spaces controller to manage Spaces, generate presigned URLs, manage SSM sessions                                                | Add-on controller pod (privileged)              | ✔ Yes                                      |
| In-Cluster Router Role             | Required for WebUI access      | Allows router pod to perform KMS operations for JWT signing (WebUI authentication)                                                         | In-cluster router pod (privileged)              | ✔ Yes                                      |
| SSM Managed Instance Role          | Required for Remote IDE access | Used by SSM agent sidecar for SSH-over-SSM remote IDE sessions                                                                             | SSM Agent in Space IDE Pods (not an add-on pod) | ✔ Yes                                      |
| IAM Role for EBS CSI Driver Add-on | Always required                | Allows EBS CSI Driver to create/attach/modify volumes for Spaces workloads                                                                 | EBS CSI Driver Add-on                           | Auto created                                |
| IAM Role for External DNS Add-on   | Required for WebUI access      | It ensures that Space endpoints and in-cluster components can be automatically assigned DNS names in the customer’s Route 53 hosted zones. | External DNS Add-on                             | Auto created                                |

### 1. Spaces Add-on Execution Role (Required)

The Spaces Add-on Execution Role is always required because it is used by the
SageMaker Spaces addon-on controller pod, an administrative component installed
through the EKS add-on. This role allows the controller to manage Spaces, provision
resources, interact with SSM, and generate presigned URLs for
both Remote IDE and WebUI access. It also supports KMS access used for request
signing for authenticating the WebUI https requests. This role can be automatically
created when SageMaker Spaces add-on is installed through the SageMaker Console. For
manual creation, AWS provides the `AmazonSageMakerSpacesControllerPolicy`
managed policy.

**Reference Trust Policy**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "pods.eks.amazonaws.com"
      },
      "Action": [
          "sts:AssumeRole",
          "sts:TagSession"
      ],
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{accountId}}",
          "aws:SourceArn": "arn:aws:eks:{{region}}:{{accountId}}:cluster/{{eksClusterName}}"
        }
      }
    }
  ]
}
```

### 2. In-Cluster Router Role (Required for WebUI Authentication)

The In-Cluster Router Role is used by the **router
pod**, a privileged component that authenticates Spaces WebUI sessions.
The router uses a KMS key to create and sign JWT tokens that authorize user access
to specific Spaces. This role allows the router pod to generate data keys, and
decrypt them. Similar to the controller role, it enforces security using tag- and
cluster-based scope restrictions. This role can be automatically generated when
Spaces add-on is installed via the AWS SageMaker Console, but customers may manually
create it.

**Reference Trust Policy**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "pods.eks.amazonaws.com"
      },
      "Action": [
          "sts:AssumeRole",
          "sts:TagSession"
      ],
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{accountId}}",
          "aws:SourceArn": "arn:aws:eks:{{region}}:{{accountId}}:cluster/{{eksClusterName}}"
        }
      }
    }
  ]
}
```

**Reference Permission Policy**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "KMSDescribeKey",
            "Effect": "Allow",
            "Action": [
                "kms:DescribeKey"
            ],
            "Resource": "arn:aws:kms:{{region}}:{{accountId}}:key/{{kmsKeyId}}"
        },
        {
            "Sid": "KMSKeyOperations",
            "Effect": "Allow",
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "arn:aws:kms:{{region}}:{{accountId}}:key/{{kmsKeyId}}",
            "Condition": {
                "StringEquals": {
                    "kms:EncryptionContext:sagemaker:component": "amazon-sagemaker-spaces",
                    "kms:EncryptionContext:sagemaker:eks-cluster-arn": "${aws:PrincipalTag/eks-cluster-arn}"
                }
            }
        }
    ]
}
```

### 3. SSM Managed Instance Role (Required for Remote IDE Access)

The SSM Managed Instance Role is passed when registering the SSM managed instance
for enabling the remote IDE access. This role allows the SSM agent to register the
pod as an SSM Managed Instance and use the SSM Session Manager channels for Remote
IDE (SSH-over-SSM) connectivity. It can be created automatically when using the AWS
SageMaker Console. For manual deployments, customers must create this role and
provide it to the Spaces add-on. The controller pod itself does not assume this
role; it only provides it when calling `ssm:CreateActivation`.

**Reference Trust Policy**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ssm.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{account}}"
                },
                "ArnEquals": {
                    "aws:SourceArn": "arn:aws:ssm:{{region}}:{{account}}:*"
                }
            }
        }
    ]
}

```

**Reference Permissions Policy**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ssm:DescribeAssociation"
      ],
      "Resource": [
        "arn:aws:ssm:{{region}}:{{account}}:association/*",
        "arn:aws:ssm:{{region}}:{{account}}:document/*",
        "arn:aws:ec2:{{region}}:{{account}}:instance/*",
        "arn:aws:ssm:{{region}}:{{account}}:managed-instance/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "ssm:GetDocument",
        "ssm:DescribeDocument"
      ],
      "Resource": "arn:aws:ssm:{{region}}:{{account}}:document/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ssm:GetParameter",
        "ssm:GetParameters"
      ],
      "Resource": "arn:aws:ssm:{{region}}:{{account}}:parameter/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ssm:ListInstanceAssociations"
      ],
      "Resource": [
        "arn:aws:ec2:{{region}}:{{account}}:instance/*",
        "arn:aws:ssm:{{region}}:{{account}}:managed-instance/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "ssm:PutComplianceItems"
      ],
      "Resource": [
        "arn:aws:ec2:{{region}}:{{account}}:instance/*",
        "arn:aws:ssm:{{region}}:{{account}}:managed-instance/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "ssm:UpdateAssociationStatus"
      ],
      "Resource": [
        "arn:aws:ssm:{{region}}:{{account}}:document/*",
        "arn:aws:ec2:{{region}}:{{account}}:instance/*",
        "arn:aws:ssm:{{region}}:{{account}}:managed-instance/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "ssm:UpdateInstanceAssociationStatus"
      ],
      "Resource": [
        "arn:aws:ssm:{{region}}:{{account}}:association/*",
        "arn:aws:ec2:{{region}}:{{account}}:instance/*",
        "arn:aws:ssm:{{region}}:{{account}}:managed-instance/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "ssm:UpdateInstanceInformation"
      ],
      "Resource": [
        "arn:aws:ec2:{{region}}:{{account}}:instance/*",
        "arn:aws:ssm:{{region}}:{{account}}:managed-instance/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "ssm:GetDeployablePatchSnapshotForInstance",
        "ssm:GetManifest",
        "ssm:ListAssociations",
        "ssm:PutInventory",
        "ssm:PutConfigurePackageResult"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ssmmessages:CreateControlChannel",
        "ssmmessages:CreateDataChannel",
        "ssmmessages:OpenControlChannel",
        "ssmmessages:OpenDataChannel"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2messages:AcknowledgeMessage",
        "ec2messages:DeleteMessage",
        "ec2messages:FailMessage",
        "ec2messages:GetEndpoint"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2messages:GetMessages",
        "ec2messages:SendReply"
      ],
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "ssm:SourceInstanceARN": "arn:aws:ssm:{{region}}:{{account}}:managed-instance/*"
        }
      }
    }
  ]
}
```

### 4. IAM Role for EBS CSI Driver Add-on

The IAM role for the EBS CSI Driver is required because the EBS CSI Driver
provisions persistent volumes for Spaces workloads. While the AWS-managed [AmazonEBSCSIDriverPolicy](../../../aws-managed-policy/latest/reference/AmazonEBSCSIDriverPolicy.md "../../../aws-managed-policy/latest/reference/AmazonEBSCSIDriverPolicy.md") provides baseline permissions, SageMaker
HyperPod clusters require [additional capabilities](sagemaker-hyperpod-eks-ebs.md#sagemaker-hyperpod-eks-ebs-setup "sagemaker-hyperpod-eks-ebs.md#sagemaker-hyperpod-eks-ebs-setup") such as creating fast snapshot restores,
tagging cluster-owned volumes, and attaching/detaching volumes for HyperPod-managed
nodes. These permissions also include SageMaker-specific APIs such as
`sagemaker:AttachClusterNodeVolume`. If EBS CSI Driver is not installed, this role
will now be automatically created by the SageMaker Console during Spaces add-on
installation, **requiring no customer action**.

### 5. IAM Role for External DNS Add-on

The External DNS add-on manages DNS records for Services and Ingress resources on
the HyperPod cluster. It ensures that Space endpoints and in-cluster components can
be automatically assigned DNS names in the customer’s Route 53 hosted zones. Today,
customers often install External DNS manually via a 1-click option in the EKS
console. As part of improving the SageMaker Spaces experience, this role will now be
automatically created by the SageMaker Console during Spaces add-on installation,
**requiring no customer action**.

## Permission setup for AWS Toolkit to Access SageMaker Spaces

To allow the AWS VS Code Toolkit resource explorer side panel to discover and
connect to SageMaker Spaces, the following IAM permissions are required. These
permissions allow the Toolkit to list available SageMaker HyperPod clusters,
retrieve cluster details, and obtain a connection token for the associated Amazon
EKS cluster.

**Required IAM Policy**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SageMakerListClusters",
            "Effect": "Allow",
            "Action": "sagemaker:ListClusters",
            "Resource": "*"
        },
        {
            "Sid": "SageMakerDescribeCluster",
            "Effect": "Allow",
            "Action": "sagemaker:DescribeCluster",
            "Resource": "arn:aws:sagemaker:{{region}}:{{account}}:cluster/cluster-name"
        },
        {
            "Sid": "EksDescribeCluster",
            "Effect": "Allow",
            "Action": "eks:DescribeCluster",
            "Resource": "arn:aws:eks:{{region}}:{{account}}:cluster/cluster-name"
        },
        {
            "Sid": "EksGetToken",
            "Effect": "Allow",
            "Action": "eks:GetToken",
            "Resource": "*"
        }
    ]
}
```

**Scoping Recommendations**

- Replace cluster-name with the specific SageMaker HyperPod cluster(s) your
  users need to access.

- The eks:GetToken action currently does not support resource-level
  restrictions and must use Resource: "\*". This is an AWS service limitation.
  The client side Authentication is performed through [EKS access entries](../../../eks/latest/userguide/access-entries.md "../../../eks/latest/userguide/access-entries.md").

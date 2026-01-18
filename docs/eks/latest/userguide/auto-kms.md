**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Enable EBS Volume Encryption with Customer Managed KMS Keys for EKS Auto Mode

You can encrypt the ephemeral root volume for EKS Auto Mode instances with a customer managed KMS key.

Amazon EKS Auto Mode uses service-linked roles to delegate permissions to other AWS services when managing encrypted EBS volumes for your Kubernetes clusters. This topic describes how to set up the key policy that you need when specifying a customer managed key for Amazon EBS encryption with EKS Auto Mode.

Considerations:

- EKS Auto Mode does not need additional authorization to use the default AWS managed key to protect the encrypted volumes in your account.
- This topic covers encrypting ephemeral volumes, the root volumes for EC2 instances. For more information about encrypting data volumes used for workloads, see [Create a storage class](create-storage-class.md "create-storage-class.md").

## Overview

The following AWS KMS keys can be used for Amazon EBS root volume encryption when EKS Auto Mode launches instances:

- **AWS managed key** – An encryption key in your account that Amazon EBS creates, owns, and manages. This is the default encryption key for a new account.
- **Customer managed key** – A custom encryption key that you create, own, and manage.

###### Note

The key must be symmetric. Amazon EBS does not support asymmetric customer managed keys.

## Step 1: Configure the key policy

Your KMS keys must have a key policy that allows EKS Auto Mode to launch instances with Amazon EBS volumes encrypted with a customer managed key.

Configure your key policy with the following structure:

###### Note

This policy only includes permissions for EKS Auto Mode. The key policy may need additional permissions if other identities need to use the key or manage grants.

```
 {
    "Version":"2012-10-17",
    "Id": "MyKeyPolicy",
    "Statement": [
        {
            "Sid": "Allow use of the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::123456789012:role/ClusterServiceRole"
                ]
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*",
                "kms:DescribeKey"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Allow attachment of persistent resources",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::123456789012:role/ClusterServiceRole"
                ]
            },
            "Action": [
                "kms:CreateGrant",
                "kms:ListGrants",
                "kms:RevokeGrant"
            ],
            "Resource": "*",
            "Condition": {
                "Bool": {
                    "kms:GrantIsForAWSResource": "true"
                }
            }
        }
    ]
}
```

Make sure to replace `<account-id>` with your actual AWS account ID.

When configuring the key policy:

- The `ClusterServiceRole` must have the necessary IAM permissions to use the KMS key for encryption operations
- The `kms:GrantIsForAWSResource` condition ensures that grants can only be created for AWS services

## Step 2: Configure NodeClass with your customer managed key

After configuring the key policy, reference the KMS key in your EKS Auto Mode NodeClass configuration:

```
 apiVersion: eks.amazonaws.com/v1
kind: NodeClass
metadata:
  name: my-node-class
spec:
  # Insert existing configuration

  ephemeralStorage:
    size: "80Gi"  # Range: 1-59000Gi or 1-64000G or 1-58Ti or 1-64T
    iops: 3000    # Range: 3000-16000
    throughput: 125  # Range: 125-1000

    # KMS key for encryption
    kmsKeyID: "<shared id="region.arn"/>kms:<region>:<account-id>:key/<key-id>"
```

Replace the placeholder values with your actual values:

- `<region>` with your AWS region
- `<account-id>` with your AWS account ID
- `<key-id>` with your KMS key ID

You can specify the KMS key using any of the following formats:

- KMS Key ID: `1a2b3c4d-5e6f-1a2b-3c4d-5e6f1a2b3c4d`
- KMS Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1a2b3c4d-5e6f-1a2b-3c4d-5e6f1a2b3c4d`
- Key Alias Name: `alias/eks-auto-mode-key`
- Key Alias ARN: `arn:aws:kms:us-west-2:111122223333:alias/eks-auto-mode-key`

Apply the NodeClass configuration using kubectl:

```
 kubectl apply -f nodeclass.yaml
```

## Related Resources

- [Create a Node Class for Amazon EKS](create-node-class.md "create-node-class.md")
- View more information in the AWS Key Management Service Developer Guide
  - [Permissions for AWS services in key policies](../../../kms/latest/developerguide/key-policy-services.md "../../../kms/latest/developerguide/key-policy-services.md")
  - [Change a key policy](../../../kms/latest/developerguide/key-policy-modifying.md "../../../kms/latest/developerguide/key-policy-modifying.md")
  - [Grants in AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md")

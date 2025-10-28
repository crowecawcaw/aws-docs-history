# Create an IAM role for

HyperPod autoscaling with Karpenter

In the following steps, you'll create an IAM role that allows SageMaker HyperPod to manage
Kubernetes nodes in your cluster through Karpenter-based autoscaling. This role provides
the necessary permissions for HyperPod to add and remove cluster nodes
automatically based on workload demand.

###### Open the IAM console

1. Sign in to the AWS Management Console and open the IAM console at
   console.aws.amazon.com.
2. In the navigation pane, choose **Roles**.
3. Choose **Create role**.

###### Configure the trust policy

1. For **Trusted entity type**, choose **Custom trust
   policy**.
2. In the **Custom trust policy** editor, replace the default
   policy with the following:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "hyperpod.sagemaker.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

3. Choose **Next**.

###### Create and attach the permissions policy

Because SageMaker HyperPod requires specific permissions that aren't available in AWS
managed policies, you must create a custom policy.

1. Choose **Create policy**. This opens a new browser
   tab.
2. Choose the **JSON** tab.
3. Replace the default policy with the following:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sagemaker:BatchAddClusterNodes",
                "sagemaker:BatchDeleteClusterNodes"
            ],
            "Resource": "arn:aws:sagemaker:*:*:cluster/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:CreateGrant",
                "kms:DescribeKey"
            ],
            "Resource": "arn:aws:kms:*:*:key/*",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": "sagemaker.*.amazonaws.com"
                },
                "Bool": {
                    "kms:GrantIsForAWSResource": "true"
                },
                "ForAllValues:StringEquals": {
                    "kms:GrantOperations": [
                        "CreateGrant",
                        "Decrypt",
                        "DescribeKey",
                        "GenerateDataKeyWithoutPlaintext",
                        "ReEncryptTo",
                        "ReEncryptFrom",
                        "RetireGrant"
                    ]
                }
            }
        }
    ]
}
```

4. Choose **Next**.
5. For **Policy name**, enter
   `SageMakerHyperPodKarpenterPolicy`.
6. (Optional) For **Description**, enter a description for the
   policy.
7. Choose **Create policy**.
8. Return to the role creation tab and refresh the policy list.
9. Search for and select the
   **SageMakerHyperPodKarpenterPolicy** that you just
   created.
10. Choose **Next**.

###### Name and create the role

1. For **Role name**, enter
   `SageMakerHyperPodKarpenterRole`.
2. (Optional) For **Description**, enter a description for the
   role.
3. In the **Step 1: Select trusted entities** section, verify
   that the trust policy shows the correct service principals.
4. In the **Step 2: Add permissions** section, verify that
   `SageMakerHyperPodKarpenterPolicy` is attached.
5. Choose **Create role**.

###### Record the role ARN

After the role is created successfully:

1. In the **Roles** list, choose the role name
   `SageMakerHyperPodKarpenterRole`.
2. Copy the **Role ARN** from the **Summary**
   section. You'll need this ARN when creating your HyperPod
   cluster.
   The role ARN follows this format:
   `arn:aws:iam::ACCOUNT-ID:role/SageMakerHyperPodKarpenterRole`.

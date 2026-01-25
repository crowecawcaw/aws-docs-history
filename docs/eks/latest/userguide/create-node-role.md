**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Amazon EKS node IAM role

The Amazon EKS node `kubelet` daemon makes calls to AWS APIs on your behalf. Nodes receive permissions for these API calls through an IAM instance profile and associated policies. Before you can launch nodes and register them into a cluster, you must create an IAM role for those nodes to use when they are launched. This requirement applies to nodes launched with the Amazon EKS optimized AMI provided by Amazon, or with any other node AMIs that you intend to use. Additionally, this requirement applies to both managed node groups and self-managed nodes.

###### Note

You can’t use the same role that is used to create any clusters.

Before you create nodes, you must create an IAM role with the following permissions:

- Permissions for the `kubelet` to describe Amazon EC2 resources in the VPC, such as provided by the [AmazonEKSWorkerNodePolicy](../../../aws-managed-policy/latest/reference/AmazonEKSWorkerNodePolicy.md "../../../aws-managed-policy/latest/reference/AmazonEKSWorkerNodePolicy.md") policy. This policy also provides the permissions for the Amazon EKS Pod Identity Agent.
- Permissions for the `kubelet` to use container images from Amazon Elastic Container Registry (Amazon ECR), such as provided by the [AmazonEC2ContainerRegistryPullOnly](../../../aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryPullOnly.md "../../../aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryPullOnly.md") policy. The permissions to use container images from Amazon Elastic Container Registry (Amazon ECR) are required because the built-in add-ons for networking run pods that use container images from Amazon ECR.
- (Optional) Permissions for the Amazon EKS Pod Identity Agent to use the `eks-auth:AssumeRoleForPodIdentity` action to retrieve credentials for pods. If you don’t use the [AmazonEKSWorkerNodePolicy](../../../aws-managed-policy/latest/reference/AmazonEKSWorkerNodePolicy.md "../../../aws-managed-policy/latest/reference/AmazonEKSWorkerNodePolicy.md"), then you must provide this permission in addition to the EC2 permissions to use EKS Pod Identity.
- (Optional) If you don’t use IRSA or EKS Pod Identity to give permissions to the VPC CNI pods, then you must provide permissions for the VPC CNI on the instance role. You can use either the [`AmazonEKS_CNI_Policy`](../../../aws-managed-policy/latest/reference/AmazonEKS_CNI_Policy.md "../../../aws-managed-policy/latest/reference/AmazonEKS_CNI_Policy.md") managed policy (if you created your cluster with the `IPv4` family) or an [IPv6 policy that you create](cni-iam-role.md#cni-iam-role-create-ipv6-policy "cni-iam-role.md#cni-iam-role-create-ipv6-policy") (if you created your cluster with the `IPv6` family). Rather than attaching the policy to this role however, we recommend that you attach the policy to a separate role used specifically for the Amazon VPC CNI add-on. For more information about creating a separate role for the Amazon VPC CNI add-on, see [Configure Amazon VPC CNI plugin to use IRSA](cni-iam-role.md "cni-iam-role.md").

###### Note

The Amazon EC2 node groups must have a different IAM role than the Fargate profile. For more information, see [Amazon EKS Pod execution IAM role](pod-execution-role.md "pod-execution-role.md").

## Check for an existing node role

You can use the following procedure to check and see if your account already has the Amazon EKS node role.

1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the left navigation pane, choose **Roles**.
3. Search the list of roles for `eksNodeRole`, `AmazonEKSNodeRole`, or `NodeInstanceRole`. If a role with one of those names doesn’t exist, then see [Creating the Amazon EKS node IAM role](#create-worker-node-role "#create-worker-node-role") to create the role. If a role that contains `eksNodeRole`, `AmazonEKSNodeRole`, or `NodeInstanceRole` does exist, then select the role to view the attached policies.
4. Choose **Permissions**.
5. Ensure that the **AmazonEKSWorkerNodePolicy** and **AmazonEC2ContainerRegistryPullOnly** managed policies are attached to the role or a custom policy is attached with the minimal permissions.

###### Note

If the **AmazonEKS_CNI_Policy** policy is attached to the role, we recommend removing it and attaching it to an IAM role that is mapped to the `aws-node` Kubernetes service account instead. For more information, see [Configure Amazon VPC CNI plugin to use IRSA](cni-iam-role.md "cni-iam-role.md"). 6. Choose **Trust relationships**, and then choose **Edit trust policy**. 7. Verify that the trust relationship contains the following policy. If the trust relationship matches the following policy, choose **Cancel**. If the trust relationship doesn’t match, copy the policy into the **Edit trust policy** window and choose **Update policy**.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Principal": {
                "Service": [
                    "ec2.amazonaws.com"
                ]
            }
        }
    ]
}
```

## Creating the Amazon EKS node IAM role

You can create the node IAM role with the AWS Management Console or the AWS CLI.

AWS Management Console

1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the left navigation pane, choose **Roles**.
3. On the **Roles** page, choose **Create role**.
4. On the **Select trusted entity** page, do the following:
   1. In the **Trusted entity type** section, choose **AWS service**.
   2. Under **Use case**, choose **EC2**.
   3. Choose **Next**.

5. On the **Add permissions** page, attach a custom policy or do the following:
   1. In the **Filter policies** box, enter `AmazonEKSWorkerNodePolicy`.
   2. Select the check box to the left of **AmazonEKSWorkerNodePolicy** in the search results.
   3. Choose **Clear filters**.
   4. In the **Filter policies** box, enter `AmazonEC2ContainerRegistryPullOnly`.
   5. Select the check box to the left of **AmazonEC2ContainerRegistryPullOnly** in the search results.

   Either the **AmazonEKS_CNI_Policy** managed policy, or an [IPv6 policy](cni-iam-role.md#cni-iam-role-create-ipv6-policy "cni-iam-role.md#cni-iam-role-create-ipv6-policy") that you create must also be attached to either this role or to a different role that’s mapped to the `aws-node` Kubernetes service account. We recommend assigning the policy to the role associated to the Kubernetes service account instead of assigning it to this role. For more information, see [Configure Amazon VPC CNI plugin to use IRSA](cni-iam-role.md "cni-iam-role.md"). 6. Choose **Next**.

6. On the **Name, review, and create** page, do the following:
   1. For **Role name**, enter a unique name for your role, such as `AmazonEKSNodeRole`.
   2. For **Description**, replace the current text with descriptive text such as `Amazon EKS - Node role`.
   3. Under **Add tags (Optional)**, add metadata to the role by attaching tags as key-value pairs. For more information about using tags in IAM, see [Tagging IAM resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_.
   4. Choose **Create role**.

AWS CLI

1. Run the following command to create the `node-role-trust-relationship.json` file.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Principal": {
                "Service": [
                    "ec2.amazonaws.com"
                ]
            }
        }
    ]
}
```

2. Create the IAM role.

```
aws iam create-role \
  --role-name AmazonEKSNodeRole \
  --assume-role-policy-document file://"node-role-trust-relationship.json"
```

3. Attach two required IAM managed policies to the IAM role.

```
aws iam attach-role-policy \
  --policy-arn arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy \
  --role-name AmazonEKSNodeRole
aws iam attach-role-policy \
  --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPullOnly \
  --role-name AmazonEKSNodeRole
```

4. Attach one of the following IAM policies to the IAM role depending on which IP family you created your cluster with. The policy must be attached to this role or to a role associated to the Kubernetes `aws-node` service account that’s used for the Amazon VPC CNI plugin for Kubernetes. We recommend assigning the policy to the role associated to the Kubernetes service account. To assign the policy to the role associated to the Kubernetes service account, see [Configure Amazon VPC CNI plugin to use IRSA](cni-iam-role.md "cni-iam-role.md").
   - IPv4

   ```
   aws iam attach-role-policy \
     --policy-arn arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy \
     --role-name AmazonEKSNodeRole
   ```

   - IPv6
     1. Copy the following text and save it to a file named `vpc-cni-ipv6-policy.json`.

     ```
     {
         "Version":"2012-10-17",
         "Statement": [
             {
                 "Effect": "Allow",
                 "Action": [
                     "ec2:AssignIpv6Addresses",
                     "ec2:DescribeInstances",
                     "ec2:DescribeTags",
                     "ec2:DescribeNetworkInterfaces",
                     "ec2:DescribeInstanceTypes"
                 ],
                 "Resource": "*"
             },
             {
                 "Effect": "Allow",
                 "Action": [
                     "ec2:CreateTags"
                 ],
                 "Resource": [
                     "arn:aws:ec2:*:*:network-interface/*"
                 ]
             }
         ]
     }
     ```

     2. Create the IAM policy.

     ```
     aws iam create-policy --policy-name AmazonEKS_CNI_IPv6_Policy --policy-document file://vpc-cni-ipv6-policy.json
     ```

     3. Attach the IAM policy to the IAM role. Replace `111122223333` with your account ID.

     ```
     aws iam attach-role-policy \
       --policy-arn arn:aws:iam::111122223333:policy/AmazonEKS_CNI_IPv6_Policy \
       --role-name AmazonEKSNodeRole
     ```

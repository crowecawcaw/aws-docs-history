**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Amazon EKS Auto Mode node IAM role

###### Note

You can’t use the same role that is used to create any clusters.

Before you create nodes, you must create an IAM role with the following policies, or equivalent permissions:

- [AmazonEKSWorkerNodeMinimalPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSWorkerNodeMinimalPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSWorkerNodeMinimalPolicy")
- [AmazonEC2ContainerRegistryPullOnly](../../../AmazonECR/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly "../../../AmazonECR/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly")

## Check for an existing node role

You can use the following procedure to check and see if your account already has the Amazon EKS node role.

1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the left navigation pane, choose **Roles**.
3. Search the list of roles for `AmazonEKSAutoNodeRole`. If a role with one of those names doesn’t exist, then see instructions in the next section to create the role. If a role that contains `AmazonEKSAutoNodeRole` does exist, then select the role to view the attached policies.
4. Choose **Permissions**.
5. Ensure that the required policies above are attached, or equivalent custom policies.
6. Choose **Trust relationships**, and then choose **Edit trust policy**.
7. Verify that the trust relationship contains the following policy. If the trust relationship matches the following policy, choose **Cancel**. If the trust relationship doesn’t match, copy the policy into the **Edit trust policy** window and choose **Update policy**.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

## Creating the Amazon EKS node IAM role

You can create the node IAM role with the AWS Management Console or the AWS CLI.

### AWS Management Console

1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the left navigation pane, choose **Roles**.
3. On the **Roles** page, choose **Create role**.
4. On the **Select trusted entity** page, do the following:
   1. In the **Trusted entity type** section, choose **AWS service**.
   2. Under **Use case**, choose **EC2**.
   3. Choose **Next**.

5. On the **Add permissions** page, attach the following policies:
   - [AmazonEKSWorkerNodeMinimalPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSWorkerNodeMinimalPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSWorkerNodeMinimalPolicy")
   - [AmazonEC2ContainerRegistryPullOnly](../../../AmazonECR/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly "../../../AmazonECR/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly")

6. On the **Name, review, and create** page, do the following:
   1. For **Role name**, enter a unique name for your role, such as `AmazonEKSAutoNodeRole`.
   2. For **Description**, replace the current text with descriptive text such as `Amazon EKS - Node role`.
   3. Under **Add tags (Optional)**, add metadata to the role by attaching tags as key-value pairs. For more information about using tags in IAM, see [Tagging IAM resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_.
   4. Choose **Create role**.

### AWS CLI

**Create the Node IAM Role**

Use the **node-trust-policy.json** file from the previous step to define which entities can assume the role. Run the following command to create the Node IAM Role:

```
aws iam create-role \
    --role-name AmazonEKSAutoNodeRole \
    --assume-role-policy-document file://node-trust-policy.json
```

**Note the Role ARN**

After creating the role, retrieve and save the ARN of the Node IAM Role. You will need this ARN in subsequent steps. Use the following command to get the ARN:

```
aws iam get-role --role-name AmazonEKSAutoNodeRole --query "Role.Arn" --output text
```

**Attach Required Policies**

Attach the following AWS managed policies to the Node IAM Role to provide the necessary permissions:

To attach AmazonEKSWorkerNodeMinimalPolicy:

```
aws iam attach-role-policy \
    --role-name AmazonEKSAutoNodeRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonEKSWorkerNodeMinimalPolicy
```

To attach AmazonEC2ContainerRegistryPullOnly:

```
aws iam attach-role-policy \
    --role-name AmazonEKSAutoNodeRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPullOnly
```

**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Amazon EKS Auto Mode cluster IAM role

An Amazon EKS cluster IAM role is required for each cluster. Kubernetes clusters managed by Amazon EKS use this role to automate routine tasks for storage, networking, and compute autoscaling.

Before you can create Amazon EKS clusters, you must create an IAM role with the policies required for EKS Auto Mode. You can either attach the suggested AWS IAM managed policies, or create custom polices with equivalent permissions.

- [AmazonEKSComputePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSComputePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSComputePolicy")
- [AmazonEKSBlockStoragePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSBlockStoragePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSBlockStoragePolicy")
- [AmazonEKSLoadBalancingPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSLoadBalancingPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSLoadBalancingPolicy")
- [AmazonEKSNetworkingPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSNetworkingPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSNetworkingPolicy")
- [AmazonEKSClusterPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-amazoneksclusterpolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-amazoneksclusterpolicy")

## Check for an existing cluster role

You can use the following procedure to check and see if your account already has the Amazon EKS cluster role.

1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the left navigation pane, choose **Roles**.
3. Search the list of roles for `AmazonEKSAutoClusterRole`. If a role that includes `AmazonEKSAutoClusterRole` doesn’t exist, then see the instructions in the next section to create the role. If a role that includes `AmazonEKSAutoClusterRole` does exist, then select the role to view the attached policies.
4. Choose **Permissions**.
5. Ensure that the **AmazonEKSClusterPolicy** managed policy is attached to the role. If the policy is attached, your Amazon EKS cluster role is properly configured.
6. Choose **Trust relationships**, and then choose **Edit trust policy**.
7. Verify that the trust relationship contains the following policy. If the trust relationship matches the following policy, choose **Cancel**. If the trust relationship doesn’t match, copy the policy into the **Edit trust policy** window and choose **Update policy**.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "eks.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:TagSession"
      ]
    }
  ]
}
```

###### Note

AWS does not require the name `AmazonEKSAutoClusterRole` for this role.

## Creating the Amazon EKS cluster role

You can use the AWS Management Console or the AWS CLI to create the cluster role.

### AWS Management Console

1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. Choose **Roles**, then **Create role**.
3. Under **Trusted entity type**, select **AWS service**.
4. From the **Use cases for other AWS services** dropdown list, choose **EKS**.
5. Choose **EKS - Cluster** for your use case, and then choose **Next**.
6. On the **Add permissions** tab, select the policies and then choose **Next**.
   - [AmazonEKSComputePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSComputePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSComputePolicy")
   - [AmazonEKSBlockStoragePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSBlockStoragePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSBlockStoragePolicy")
   - [AmazonEKSLoadBalancingPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSLoadBalancingPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSLoadBalancingPolicy")
   - [AmazonEKSNetworkingPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSNetworkingPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSNetworkingPolicy")
   - [AmazonEKSClusterPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-amazoneksclusterpolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-amazoneksclusterpolicy")

7. For **Role name**, enter a unique name for your role, such as `AmazonEKSAutoClusterRole`.
8. For **Description**, enter descriptive text such as `Amazon EKS - Cluster role`.
9. Choose **Create role**.

### AWS CLI

1. Copy the following contents to a file named `cluster-trust-policy.json`.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "eks.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:TagSession"
      ]
    }
  ]
}
```

2. Create the role. You can replace `AmazonEKSAutoClusterRole` with any name that you choose.

```
aws iam create-role \
  --role-name AmazonEKSAutoClusterRole \
  --assume-role-policy-document file://"cluster-trust-policy.json"
```

3. Attach the required IAM policies to the role:

**AmazonEKSClusterPolicy**:

```
aws iam attach-role-policy \
    --role-name AmazonEKSAutoClusterRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonEKSClusterPolicy
```

**AmazonEKSComputePolicy**:

```
aws iam attach-role-policy \
    --role-name AmazonEKSAutoClusterRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonEKSComputePolicy
```

**AmazonEKSBlockStoragePolicy**:

```
aws iam attach-role-policy \
    --role-name AmazonEKSAutoClusterRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonEKSBlockStoragePolicy
```

**AmazonEKSLoadBalancingPolicy**:

```
aws iam attach-role-policy \
    --role-name AmazonEKSAutoClusterRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonEKSLoadBalancingPolicy
```

**AmazonEKSNetworkingPolicy**:

```
aws iam attach-role-policy \
    --role-name AmazonEKSAutoClusterRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonEKSNetworkingPolicy
```

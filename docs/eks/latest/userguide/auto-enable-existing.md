**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Enable EKS Auto Mode on an existing cluster

This topic describes how to enable Amazon EKS Auto Mode on your existing Amazon EKS clusters. Enabling Auto Mode on an existing cluster requires updating IAM permissions and configuring core EKS Auto Mode settings. Once enabled, you can begin migrating your existing compute workloads to take advantage of Auto Mode’s simplified operations and automated infrastructure management.

###### Important

Verify you have the minimum required version of certain Amazon EKS Add-ons installed before enabling EKS Auto Mode. For more information, see [Required add-on versions](#auto-addons-required "#auto-addons-required").

Before you begin, ensure you have administrator access to your Amazon EKS cluster and permissions to modify IAM roles. The steps in this topic guide you through enabling Auto Mode using either the AWS Management Console or AWS CLI.

## AWS Management Console

You must be logged into the AWS console with permission to manage IAM, EKS, and EC2 resources.

###### Note

The Cluster IAM role of an EKS Cluster cannot be changed after the cluster is created. EKS Auto Mode requires additional permissions on this role. You must attach additional policies to the current role.

### Update Cluster IAM role

1. Open your cluster overview page in the AWS Management Console.
2. Under **Cluster IAM role ARN**, select **View in IAM**.
3. From the **Add Permissions** dropdown, select **Attach Policies**.
4. Use the **Search** box to find and select the following policies:
   - `AmazonEKSComputePolicy`
   - `AmazonEKSBlockStoragePolicy`
   - `AmazonEKSLoadBalancingPolicy`
   - `AmazonEKSNetworkingPolicy`
   - `AmazonEKSClusterPolicy`

5. Select **Add permissions**
6. From the **Trust relationships** tab, select **Edit trust policy**
7. Insert the following Cluster IAM Role trust policy, and select **Update policy**

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

### Enable EKS Auto Mode

1. Open your cluster overview page in the AWS Management Console.
2. Under **EKS Auto Mode** select **Manage**
3. Toggle **EKS Auto Mode** to on.
4. From the **EKS Node Pool** dropdown, select the default node pools you want to create.
   - Learn more about Node Pools in EKS Auto Mode. For more information, see [Create a Node Pool for EKS Auto Mode](create-node-pool.md "create-node-pool.md").

5. If you have previously created an EKS Auto Mode Node IAM role this AWS account, select it in the **Node IAM Role** dropdown. If you have not created this role before, select **Create recommended Role** and follow the steps.

## AWS CLI

### Prerequisites

- The Cluster IAM Role of the existing EKS Cluster must include sufficent permissiosn for EKS Auto Mode, such as the following policies:
  - `AmazonEKSComputePolicy`
  - `AmazonEKSBlockStoragePolicy`
  - `AmazonEKSLoadBalancingPolicy`
  - `AmazonEKSNetworkingPolicy`
  - `AmazonEKSClusterPolicy`

- The Cluster IAM Role must have an updated trust policy including the `sts:TagSession` action. For more information on creating a Cluster IAM Role, see [Create an EKS Auto Mode Cluster with the AWS CLI](automode-get-started-cli.md "automode-get-started-cli.md").
- `aws` CLI installed, logged in, and a sufficent version. You must have permission to manage IAM, EKS, and EC2 resources. For more information, see [Set up to use Amazon EKS](setting-up.md "setting-up.md").

### Procedure

Use the following commands to enable EKS Auto Mode on an existing cluster.

###### Note

The compute, block storage, and load balancing capabilities must all be enabled or disabled in the same request.

```
aws eks update-cluster-config \
 --name $CLUSTER_NAME \
 --compute-config enabled=true \
 --kubernetes-network-config '{"elasticLoadBalancing":{"enabled": true}}' \
 --storage-config '{"blockStorage":{"enabled": true}}'
```

## Required add-on versions

If you’re planning to enable EKS Auto Mode on an existing cluster, you may need to update certain add-ons. Please note:

- This applies only to existing clusters transitioning to EKS Auto Mode.
- New clusters created with EKS Auto Mode enabled don’t require these updates.

If you have any of the following add-ons installed, ensure they are at least at the specified minimum version:

| Add-on name                          | Minimum required version                                                                                                                                    |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon VPC CNI plugin for Kubernetes | v1.19.0-eksbuild.1                                                                                                                                          |
| Kube-proxy                           | <br>• v1.26.15-eksbuild.19 <br>• v1.27.16-eksbuild.14 <br>• v1.28.15-eksbuild.4 <br>• v1.29.10-eksbuild.3 <br>• v1.30.6-eksbuild.3 <br>• v1.31.2-eksbuild.3 |
| Amazon EBS CSI driver                | v1.37.0-eksbuild.1                                                                                                                                          |
| CSI snapshot controller              | v8.1.0-eksbuild.2                                                                                                                                           |
| EKS Pod Identity Agent               | v1.3.4-eksbuild.1                                                                                                                                           | For more information, see [Update an Amazon EKS add-on](updating-an-add-on.md "updating-an-add-on.md"). ## Next Steps <br>• To migrate Manage Node Group workloads, see [Migrate from EKS Managed Node Groups to EKS Auto Mode](auto-migrate-mng.md "auto-migrate-mng.md"). <br>• To migrate from Self-Managed Karpenter, see [Migrate from Karpenter to EKS Auto Mode using kubectl](auto-migrate-karpenter.md "auto-migrate-karpenter.md"). |

# Dashboard setup

Use the following information to get set up with Amazon SageMaker HyperPod Amazon CloudWatch
Observability EKS add-on. This sets you up with a detailed visual dashboard that
provides a view into metrics for your EKS cluster hardware, team allocation, and
tasks.

If you are having issues setting up, please see [Troubleshoot](sagemaker-hyperpod-eks-operate-console-ui-governance-troubleshoot.md "sagemaker-hyperpod-eks-operate-console-ui-governance-troubleshoot.md") for known troubleshooting solutions.

###### Topics

- [HyperPod Amazon CloudWatch
  Observability EKS add-on prerequisites](#hp-eks-dashboard-prerequisites "#hp-eks-dashboard-prerequisites")
- [HyperPod Amazon CloudWatch
  Observability EKS add-on setup](#hp-eks-dashboard-setup "#hp-eks-dashboard-setup")

## HyperPod Amazon CloudWatch

Observability EKS add-on prerequisites

The following section includes the prerequisites needed before installing the
Amazon EKS Observability add-on.

- Ensure that you have the minimum permission policy for
  HyperPod cluster administrators, in [IAM users for
  cluster admin](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-cluster-admin "sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-cluster-admin").
- Attach the `CloudWatchAgentServerPolicy` IAM policy to
  your worker nodes. To do so, enter the following command. Replace
  `my-worker-node-role` with
  the IAM role used by your Kubernetes worker nodes.

```
aws iam attach-role-policy \
--role-name `my-worker-node-role` \
--policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
```

## HyperPod Amazon CloudWatch

Observability EKS add-on setup

Use the following options to set up the Amazon SageMaker HyperPod Amazon CloudWatch
Observability EKS add-on.

Setup using the SageMaker AI console
The following permissions are required for setup and visualizing
the HyperPod task governance dashboard. This section
expands upon the permissions listed in [IAM users for
cluster admin](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-cluster-admin "sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-cluster-admin").

To manage task governance, use the sample policy:

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:ListClusters",
 "sagemaker:DescribeCluster",
 "sagemaker:ListComputeQuotas",
 "sagemaker:CreateComputeQuota",
 "sagemaker:UpdateComputeQuota",
 "sagemaker:DescribeComputeQuota",
 "sagemaker:DeleteComputeQuota",
 "sagemaker:ListClusterSchedulerConfigs",
 "sagemaker:DescribeClusterSchedulerConfig",
 "sagemaker:CreateClusterSchedulerConfig",
 "sagemaker:UpdateClusterSchedulerConfig",
 "sagemaker:DeleteClusterSchedulerConfig",
 "eks:ListAddons",
 "eks:CreateAddon",
 "eks:DescribeAddon",
 "eks:DescribeCluster",
 "eks:DescribeAccessEntry",
 "eks:ListAssociatedAccessPolicies",
 "eks:AssociateAccessPolicy",
 "eks:DisassociateAccessPolicy"
 ],
 "Resource": "*"
 }
 ]
}`

```

To grant permissions to manage Amazon CloudWatch Observability Amazon EKS and
view the HyperPod cluster dashboard through the SageMaker AI
console, use the sample policy below:

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "eks:ListAddons",
 "eks:CreateAddon",
 "eks:UpdateAddon",
 "eks:DescribeAddon",
 "eks:DescribeAddonVersions",
 "sagemaker:DescribeCluster",
 "sagemaker:DescribeClusterNode",
 "sagemaker:ListClusterNodes",
 "sagemaker:ListClusters",
 "sagemaker:ListComputeQuotas",
 "sagemaker:DescribeComputeQuota",
 "sagemaker:ListClusterSchedulerConfigs",
 "sagemaker:DescribeClusterSchedulerConfig",
 "eks:DescribeCluster",
 "cloudwatch:GetMetricData",
 "eks:AccessKubernetesApi"
 ],
 "Resource": "*"
 }
 ]
}`

```

Navigate to the **Dashboard** tab in the
SageMaker HyperPod console to install the Amazon CloudWatch Observability EKS. To
ensure task governance related metrics are included in the
**Dashboard**, enable the Kueue metrics
checkbox. Enabling the Kueue metrics enables CloudWatch
**Metrics** costs, after free-tier limit is
reached. For more information, see **Metrics** in
[Amazon CloudWatch
Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

Setup using the EKS AWS CLI
Use the following EKS AWS CLI command to install the add-on:

```
aws eks create-addon --cluster-name `cluster-name`
--addon-name amazon-cloudwatch-observability
--configuration-values "`configuration json`"
```

Below is an example of the JSON of the configuration
values:

```
{
    "agent": {
        "config": {
            "logs": {
                "metrics_collected": {
                    "kubernetes": {
                        "kueue_container_insights": true,
                        "enhanced_container_insights": true
                    },
                    "application_signals": { }
                }
            },
            "traces": {
                "traces_collected": {
                    "application_signals": { }
                }
            }
        },
    },
}
```

Setup using the EKS Console UI

1. Navigate to the [EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Choose your cluster.
3. Choose **Add-ons**.
4. Find the **Amazon CloudWatch Observability**
   add-on and install. Install version >= 2.4.0 for the add-on.
5. Include the following JSON, Configuration values:

```
{
    "agent": {
        "config": {
            "logs": {
                "metrics_collected": {
                    "kubernetes": {
                        "kueue_container_insights": true,
                        "enhanced_container_insights": true
                    },
                    "application_signals": { }
                },
            },
            "traces": {
                "traces_collected": {
                    "application_signals": { }
                }
            }
        },
    },
}
```

Once the EKS Observability add-on has been successfully installed, you can
view your EKS cluster metrics under the HyperPod console
**Dashboard** tab.

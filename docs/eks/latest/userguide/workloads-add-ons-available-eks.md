**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# AWS add-ons

The following Amazon EKS add-ons are available to create on your cluster. You can view the most current list of available add-ons using `eksctl`, the AWS Management Console, or the AWS CLI. To see all available add-ons or to install an add-on, see [Create an Amazon EKS add-on](creating-an-add-on.md "creating-an-add-on.md"). If an add-on requires IAM permissions, then you must have an IAM OpenID Connect (OIDC) provider for your cluster. To determine whether you have one, or to create one, see [Create an IAM OIDC provider for your cluster](enable-iam-roles-for-service-accounts.md "enable-iam-roles-for-service-accounts.md"). You can create or delete an add-on after you’ve installed it. For more information, see [Update an Amazon EKS add-on](updating-an-add-on.md "updating-an-add-on.md") or [Remove an Amazon EKS add-on from a cluster](removing-an-add-on.md "removing-an-add-on.md"). For more information about considerations specific to running EKS add-ons with Amazon EKS Hybrid Nodes, see [Configure add-ons for hybrid nodes](hybrid-nodes-add-ons.md "hybrid-nodes-add-ons.md").

You can use any of the following Amazon EKS add-ons.

| Description                                                                                                                                                                                                                                           | Learn more                                                                                                                               | Compatible compute types                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| Provide native VPC networking for your cluster                                                                                                                                                                                                        | [Amazon VPC CNI plugin for Kubernetes](#add-ons-vpc-cni "#add-ons-vpc-cni")                                                              | EC2                                           |
| A flexible, extensible DNS server that can serve as the Kubernetes cluster DNS                                                                                                                                                                        | [CoreDNS](#add-ons-coredns "#add-ons-coredns")                                                                                           | EC2, Fargate, EKS Auto Mode, EKS Hybrid Nodes |
| Maintain network rules on each Amazon EC2 node                                                                                                                                                                                                        | [Kube-proxy](#add-ons-kube-proxy "#add-ons-kube-proxy")                                                                                  | EC2, EKS Hybrid Nodes                         |
| Provide Amazon EBS storage for your cluster                                                                                                                                                                                                           | [Amazon EBS CSI driver](#add-ons-aws-ebs-csi-driver "#add-ons-aws-ebs-csi-driver")                                                       | EC2                                           |
| Provide Amazon EFS storage for your cluster                                                                                                                                                                                                           | [Amazon EFS CSI driver](#add-ons-aws-efs-csi-driver "#add-ons-aws-efs-csi-driver")                                                       | EC2, EKS Auto Mode                            |
| Provide Amazon FSx for Lustre storage for your cluster                                                                                                                                                                                                | [Amazon FSx CSI driver](#add-ons-aws-fsx-csi-driver "#add-ons-aws-fsx-csi-driver")                                                       | EC2, EKS Auto Mode                            |
| Provide Amazon S3 storage for your cluster                                                                                                                                                                                                            | [Mountpoint for Amazon S3 CSI Driver](#mountpoint-for-s3-add-on "#mountpoint-for-s3-add-on")                                             | EC2, EKS Auto Mode                            |
| Detect additional node health issues                                                                                                                                                                                                                  | [Node monitoring agent](#add-ons-eks-node-monitoring-agent "#add-ons-eks-node-monitoring-agent")                                         | EC2, EKS Hybrid Nodes                         |
| Enable the use of snapshot functionality in compatible CSI drivers, such as the Amazon EBS CSI driver                                                                                                                                                 | [CSI snapshot controller](#addons-csi-snapshot-controller "#addons-csi-snapshot-controller")                                             | EC2, Fargate, EKS Auto Mode, EKS Hybrid Nodes |
| SageMaker HyperPod task governance optimizes compute resource allocation and usage across teams in Amazon EKS clusters, addressing inefficiencies in task prioritization and resource sharing.                                                        | [Amazon SageMaker HyperPod task governance](#addons-hyperpod "#addons-hyperpod")                                                         | EC2, EKS Auto Mode,                           |
| The Amazon SageMaker HyperPod Observability AddOn provides comprehensive monitoring and observability capabilities for HyperPod clusters.                                                                                                             | [Amazon SageMaker HyperPod Observability Add-on](#addons-hyperpod-observability "#addons-hyperpod-observability")                        | EC2, EKS Auto Mode,                           |
| Amazon SageMaker HyperPod training operator enables efficient distributed training on Amazon EKS clusters with advanced scheduling and resource management capabilities.                                                                              | [Amazon SageMaker HyperPod training operator](#addons-hyperpod-training-operator "#addons-hyperpod-training-operator")                   | EC2, EKS Auto Mode                            |
| A Kubernetes agent that collects and reports network flow data to Amazon CloudWatch, enabling comprehensive monitoring of TCP connections across cluster nodes.                                                                                       | [AWS Network Flow Monitor Agent](#addons-network-flow "#addons-network-flow")                                                            | EC2, EKS Auto Mode                            |
| Secure, production-ready, AWS supported distribution of the OpenTelemetry project                                                                                                                                                                     | [AWS Distro for OpenTelemetry](#add-ons-adot "#add-ons-adot")                                                                            | EC2, Fargate, EKS Auto Mode, EKS Hybrid Nodes |
| Security monitoring service that analyzes and processes foundational data sources including AWS CloudTrail management events and Amazon VPC flow logs. Amazon GuardDuty also processes features, such as Kubernetes audit logs and runtime monitoring | [Amazon GuardDuty agent](#add-ons-guard-duty "#add-ons-guard-duty")                                                                      | EC2, EKS Auto Mode                            |
| Monitoring and observability service provided by AWS. This add-on installs the CloudWatch Agent and enables both CloudWatch Application Signals and CloudWatch Container Insights with enhanced observability for Amazon EKS                          | [Amazon CloudWatch Observability agent](#amazon-cloudwatch-observability "#amazon-cloudwatch-observability")                             | EC2, EKS Auto Mode, EKS Hybrid Nodes          |
| Ability to manage credentials for your applications, similar to the way that EC2 instance profiles provide credentials to EC2 instances                                                                                                               | [EKS Pod Identity Agent](#add-ons-pod-id "#add-ons-pod-id")                                                                              | EC2, EKS Hybrid Nodes                         |
| Enable cert-manager to issue X.509 certificates from AWS Private CA. Requires cert-manager.                                                                                                                                                           | [AWS Private CA Connector for Kubernetes](#add-ons-aws-privateca-connector "#add-ons-aws-privateca-connector")                           | EC2, Fargate, EKS Auto Mode, EKS Hybrid Nodes |
| Generate Prometheus metrics about SR-IOV network device performance                                                                                                                                                                                   | [SR-IOV Network Metrics Exporter](#add-ons-sriov-network-metrics-exporter "#add-ons-sriov-network-metrics-exporter")                     | EC2                                           |
| Retrieve secrets from AWS Secrets Manager and parameters from AWS Systems Manager Parameter Store and mount them as files in Kubernetes pods.                                                                                                         | [AWS Secrets Store CSI Driver provider](#add-ons-aws-secrets-store-csi-driver-provider "#add-ons-aws-secrets-store-csi-driver-provider") | EC2, EKS Auto Mode, EKS Hybrid Nodes          |
| With Spaces, you can create and manage JupyterLab and Code Editor applications to run interactive ML workloads.                                                                                                                                       | [Amazon SageMaker Spaces](#add-ons-amazon-sagemaker-spaces "#add-ons-amazon-sagemaker-spaces")                                           | Hyperpod                                      |

## Amazon VPC CNI plugin for Kubernetes

The Amazon VPC CNI plugin for Kubernetes Amazon EKS add-on is a Kubernetes container network interface (CNI) plugin that provides native VPC networking for your cluster. The self-managed or managed type of this add-on is installed on each Amazon EC2 node, by default. For more information, see [Kubernetes container network interface (CNI) plugin](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/ "https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/").

###### Note

You do not need to install this add-on on Amazon EKS Auto Mode clusters. For more information, see [Considerations for Amazon EKS Auto Mode](eks-add-ons.md#addon-consider-auto "eks-add-ons.md#addon-consider-auto").

The Amazon EKS add-on name is `vpc-cni`.

### Required IAM permissions

This add-on uses the IAM roles for service accounts capability of Amazon EKS. For more information, see [IAM roles for service accounts](iam-roles-for-service-accounts.md "iam-roles-for-service-accounts.md").

If your cluster uses the `IPv4` family, the permissions in the [AmazonEKS_CNI_Policy](../../../aws-managed-policy/latest/reference/AmazonEKS_CNI_Policy.md "../../../aws-managed-policy/latest/reference/AmazonEKS_CNI_Policy.md") are required. If your cluster uses the `IPv6` family, you must [create an IAM policy](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") with the permissions in [IPv6 mode](https://github.com/aws/amazon-vpc-cni-k8s/blob/master/docs/iam-policy.md#ipv6-mode "https://github.com/aws/amazon-vpc-cni-k8s/blob/master/docs/iam-policy.md#ipv6-mode"). You can create an IAM role, attach one of the policies to it, and annotate the Kubernetes service account used by the add-on with the following command.

Replace `my-cluster` with the name of your cluster and `AmazonEKSVPCCNIRole` with the name for your role. If your cluster uses the `IPv6` family, then replace `AmazonEKS_CNI_Policy` with the name of the policy that you created. This command requires that you have [eksctl](https://eksctl.io "https://eksctl.io") installed on your device. If you need to use a different tool to create the role, attach the policy to it, and annotate the Kubernetes service account, see [Assign IAM roles to Kubernetes service accounts](associate-service-account-role.md "associate-service-account-role.md").

```
eksctl create iamserviceaccount --name aws-node --namespace kube-system --cluster my-cluster --role-name AmazonEKSVPCCNIRole \
    --role-only --attach-policy-arn arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy --approve
```

### Update information

You can only update one minor version at a time. For example, if your current version is `1.28.`x`-eksbuild.`y`` and you want to update to `1.30.`x`-eksbuild.`y``, then you must update your current version to `1.29.`x`-eksbuild.`y`` and then update it again to `1.30.`x`-eksbuild.`y``. For more information about updating the add-on, see [Update the Amazon VPC CNI (Amazon EKS add-on)](vpc-add-on-update.md "vpc-add-on-update.md").

## CoreDNS

The CoreDNS Amazon EKS add-on is a flexible, extensible DNS server that can serve as the Kubernetes cluster DNS. The self-managed or managed type of this add-on was installed, by default, when you created your cluster. When you launch an Amazon EKS cluster with at least one node, two replicas of the CoreDNS image are deployed by default, regardless of the number of nodes deployed in your cluster. The CoreDNS Pods provide name resolution for all Pods in the cluster. You can deploy the CoreDNS Pods to Fargate nodes if your cluster includes a Fargate profile with a namespace that matches the namespace for the CoreDNS deployment. For more information, see [Define which Pods use AWS Fargate when launched](fargate-profile.md "fargate-profile.md")

###### Note

You do not need to install this add-on on Amazon EKS Auto Mode clusters. For more information, see [Considerations for Amazon EKS Auto Mode](eks-add-ons.md#addon-consider-auto "eks-add-ons.md#addon-consider-auto").

The Amazon EKS add-on name is `coredns`.

### Required IAM permissions

This add-on doesn’t require any permissions.

### Additional information

To learn more about CoreDNS, see [Using CoreDNS for Service Discovery](https://kubernetes.io/docs/tasks/administer-cluster/coredns/ "https://kubernetes.io/docs/tasks/administer-cluster/coredns/") and [Customizing DNS Service](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/ "https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/") in the Kubernetes documentation.

## `Kube-proxy`

The `Kube-proxy` Amazon EKS add-on maintains network rules on each Amazon EC2 node. It enables network communication to your Pods. The self-managed or managed type of this add-on is installed on each Amazon EC2 node in your cluster, by default.

###### Note

You do not need to install this add-on on Amazon EKS Auto Mode clusters. For more information, see [Considerations for Amazon EKS Auto Mode](eks-add-ons.md#addon-consider-auto "eks-add-ons.md#addon-consider-auto").

The Amazon EKS add-on name is `kube-proxy`.

### Required IAM permissions

This add-on doesn’t require any permissions.

### Update information

Before updating your current version, consider the following requirements:

- `Kube-proxy` on an Amazon EKS cluster has the same [compatibility and skew policy as Kubernetes](https://kubernetes.io/releases/version-skew-policy/#kube-proxy "https://kubernetes.io/releases/version-skew-policy/#kube-proxy").

### Additional information

To learn more about `kube-proxy`, see [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/ "https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/") in the Kubernetes documentation.

## Amazon EBS CSI driver

The Amazon EBS CSI driver Amazon EKS add-on is a Kubernetes Container Storage Interface (CSI) plugin that provides Amazon EBS storage for your cluster.

###### Note

You do not need to install this add-on on Amazon EKS Auto Mode clusters. Auto Mode includes a block storage capability. For more information, see [Deploy a sample stateful workload to EKS Auto Mode](sample-storage-workload.md "sample-storage-workload.md").

The Amazon EKS add-on name is `aws-ebs-csi-driver`.

### Required IAM permissions

This add-on utilizes the IAM roles for service accounts capability of Amazon EKS. For more information, see [IAM roles for service accounts](iam-roles-for-service-accounts.md "iam-roles-for-service-accounts.md"). The permissions in the [AmazonEBSCSIDriverPolicy](../../../aws-managed-policy/latest/reference/AmazonEBSCSIDriverPolicy.md "../../../aws-managed-policy/latest/reference/AmazonEBSCSIDriverPolicy.md")
AWS managed policy are required. You can create an IAM role and attach the managed policy to it with the following command. Replace `my-cluster` with the name of your cluster and `AmazonEKS_EBS_CSI_DriverRole` with the name for your role. This command requires that you have [eksctl](https://eksctl.io "https://eksctl.io") installed on your device. If you need to use a different tool or you need to use a custom [KMS key](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") for encryption, see [Step 1: Create an IAM role](ebs-csi.md#csi-iam-role "ebs-csi.md#csi-iam-role").

```
eksctl create iamserviceaccount \
    --name ebs-csi-controller-sa \
    --namespace kube-system \
    --cluster my-cluster \
    --role-name AmazonEKS_EBS_CSI_DriverRole \
    --role-only \
    --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
    --approve
```

### Additional information

To learn more about the add-on, see [Use Kubernetes volume storage with Amazon EBS](ebs-csi.md "ebs-csi.md").

## Amazon EFS CSI driver

The Amazon EFS CSI driver Amazon EKS add-on is a Kubernetes Container Storage Interface (CSI) plugin that provides Amazon EFS storage for your cluster.

The Amazon EKS add-on name is `aws-efs-csi-driver`.

### Required IAM permissions

**Required IAM permissions** – This add-on utilizes the IAM roles for service accounts capability of Amazon EKS. For more information, see [IAM roles for service accounts](iam-roles-for-service-accounts.md "iam-roles-for-service-accounts.md"). The permissions in the [AmazonEFSCSIDriverPolicy](../../../aws-managed-policy/latest/reference/AmazonEFSCSIDriverPolicy.md "../../../aws-managed-policy/latest/reference/AmazonEFSCSIDriverPolicy.md")
AWS managed policy are required. You can create an IAM role and attach the managed policy to it with the following commands. Replace `my-cluster` with the name of your cluster and `AmazonEKS_EFS_CSI_DriverRole` with the name for your role. These commands require that you have [eksctl](https://eksctl.io "https://eksctl.io") installed on your device. If you need to use a different tool, see [Step 1: Create an IAM role](efs-csi.md#efs-create-iam-resources "efs-csi.md#efs-create-iam-resources").

```
export cluster_name=my-cluster
export role_name=AmazonEKS_EFS_CSI_DriverRole
eksctl create iamserviceaccount \
    --name efs-csi-controller-sa \
    --namespace kube-system \
    --cluster $cluster_name \
    --role-name $role_name \
    --role-only \
    --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEFSCSIDriverPolicy \
    --approve
TRUST_POLICY=$(aws iam get-role --output json --role-name $role_name --query 'Role.AssumeRolePolicyDocument' | \
    sed -e 's/efs-csi-controller-sa/efs-csi-*/' -e 's/StringEquals/StringLike/')
aws iam update-assume-role-policy --role-name $role_name --policy-document "$TRUST_POLICY"
```

### Additional information

To learn more about the add-on, see [Use elastic file system storage with Amazon EFS](efs-csi.md "efs-csi.md").

## Amazon FSx CSI driver

The Amazon FSx CSI driver Amazon EKS add-on is a Kubernetes Container Storage Interface (CSI) plugin that provides Amazon FSx for Lustre storage for your cluster.

The Amazon EKS add-on name is `aws-fsx-csi-driver`.

###### Note

- Pre-existing Amazon FSx CSI driver installations in the cluster can cause add-on installation failures. When you attempt to install the Amazon EKS add-on version while a non-EKS FSx CSI Driver exists, the installation will fail due to resource conflicts. Use the `OVERWRITE` flag during installation to resolve this issue:

```
aws eks create-addon --addon-name aws-fsx-csi-driver --cluster-name my-cluster --resolve-conflicts OVERWRITE
```

- The Amazon FSx CSI Driver EKS add-on requires the EKS Pod Identity agent for authentication. Without this component, the add-on will fail with the error `Amazon EKS Pod Identity agent is not installed in the cluster`, preventing volume operations. Install the Pod Identity agent before or after deploying the FSx CSI Driver add-on. For more information, see [Set up the Amazon EKS Pod Identity Agent](pod-id-agent-setup.md "pod-id-agent-setup.md").

### Required IAM permissions

This add-on utilizes the IAM roles for service accounts capability of Amazon EKS. For more information, see [IAM roles for service accounts](iam-roles-for-service-accounts.md "iam-roles-for-service-accounts.md"). The permissions in the [AmazonFSxFullAccess](../../../aws-managed-policy/latest/reference/AmazonFSxFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonFSxFullAccess.md")
AWS managed policy are required. You can create an IAM role and attach the managed policy to it with the following command. Replace `my-cluster` with the name of your cluster and `AmazonEKS_FSx_CSI_DriverRole` with the name for your role. This command requires that you have [eksctl](https://eksctl.io "https://eksctl.io") installed on your device.

```
eksctl create iamserviceaccount \
    --name fsx-csi-controller-sa \
    --namespace kube-system \
    --cluster my-cluster \
    --role-name AmazonEKS_FSx_CSI_DriverRole \
    --role-only \
    --attach-policy-arn arn:aws:iam::aws:policy/AmazonFSxFullAccess \
    --approve
```

### Additional information

To learn more about the add-on, see [Use high-performance app storage with Amazon FSx for Lustre](fsx-csi.md "fsx-csi.md").

## Mountpoint for Amazon S3 CSI Driver

The Mountpoint for Amazon S3 CSI Driver Amazon EKS add-on is a Kubernetes Container Storage Interface (CSI) plugin that provides Amazon S3 storage for your cluster.

The Amazon EKS add-on name is `aws-mountpoint-s3-csi-driver`.

### Required IAM permissions

This add-on uses the IAM roles for service accounts capability of Amazon EKS. For more information, see [IAM roles for service accounts](iam-roles-for-service-accounts.md "iam-roles-for-service-accounts.md").

The IAM role that is created will require a policy that gives access to S3. Follow the [Mountpoint IAM permissions recommendations](https://github.com/awslabs/mountpoint-s3/blob/main/doc/CONFIGURATION.md#iam-permissions "https://github.com/awslabs/mountpoint-s3/blob/main/doc/CONFIGURATION.md#iam-permissions") when creating the policy. Alternatively, you may use the AWS managed policy [AmazonS3FullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonS3FullAccess$jsonEditor "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonS3FullAccess$jsonEditor"), but this managed policy grants more permissions than are needed for Mountpoint.

You can create an IAM role and attach your policy to it with the following commands. Replace `my-cluster` with the name of your cluster, `region-code` with the correct AWS Region code, `AmazonEKS_S3_CSI_DriverRole` with the name for your role, and `AmazonEKS_S3_CSI_DriverRole_ARN` with the role ARN. These commands require that you have [eksctl](https://eksctl.io "https://eksctl.io") installed on your device. For instructions on using the IAM console or AWS CLI, see [Step 2: Create an IAM role](s3-csi-create.md#s3-create-iam-role "s3-csi-create.md#s3-create-iam-role").

```
CLUSTER_NAME=my-cluster
REGION=region-code
ROLE_NAME=AmazonEKS_S3_CSI_DriverRole
POLICY_ARN=AmazonEKS_S3_CSI_DriverRole_ARN
eksctl create iamserviceaccount \
    --name s3-csi-driver-sa \
    --namespace kube-system \
    --cluster $CLUSTER_NAME \
    --attach-policy-arn $POLICY_ARN \
    --approve \
    --role-name $ROLE_NAME \
    --region $REGION \
    --role-only
```

### Additional information

To learn more about the add-on, see [Access Amazon S3 objects with Mountpoint for Amazon S3 CSI driver](s3-csi.md "s3-csi.md").

## CSI snapshot controller

The Container Storage Interface (CSI) snapshot controller enables the use of snapshot functionality in compatible CSI drivers, such as the Amazon EBS CSI driver.

The Amazon EKS add-on name is `snapshot-controller`.

### Required IAM permissions

This add-on doesn’t require any permissions.

### Additional information

To learn more about the add-on, see [Enable snapshot functionality for CSI volumes](csi-snapshot-controller.md "csi-snapshot-controller.md").

## Amazon SageMaker HyperPod task governance

SageMaker HyperPod task governance is a robust management system designed to streamline resource allocation and ensure efficient utilization of compute resources across teams and projects for your Amazon EKS clusters. This provides administrators with the capability to set:

- Priority levels for various tasks
- Compute allocation for each team
- How each team lends and borrows idle compute
- If a team preempts their own tasks

HyperPod task governance also provides Amazon EKS cluster Observability, offering real-time visibility into cluster capacity. This includes compute availability and usage, team allocation and utilization, and task run and wait time information, setting you up for informed decision-making and proactive resource management.

The Amazon EKS add-on name is `amazon-sagemaker-hyperpod-taskgovernance`.

### Required IAM permissions

This add-on doesn’t require any permissions.

### Additional information

To learn more about the add-on, see [SageMaker HyperPod task governance](../../../sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance.md "../../../sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance.md")

## Amazon SageMaker HyperPod Observability Add-on

The Amazon SageMaker HyperPod Observability Add-on provides comprehensive monitoring and observability capabilities for HyperPod clusters. This add-on automatically deploys and manages essential monitoring components including node exporter, DCGM exporter, kube-state-metrics, and EFA exporter. It collects and forwards metrics to a customer-designated Amazon Managed Prometheus (AMP) instance and exposes an OTLP endpoint for custom metrics and event ingestion from customer training jobs.

The add-on integrates with the broader HyperPod ecosystem by scraping metrics from various components including HyperPod Task Governance add-on, HyperPod Training Operator, Kubeflow, and KEDA. All collected metrics are centralized in Amazon Managed Prometheus, enabling customers to achieve a unified observability view through Amazon Managed Grafana dashboards. This provides end-to-end visibility into cluster health, resource utilization, and training job performance across the entire HyperPod environment.

The Amazon EKS add-on name is `amazon-sagemaker-hyperpod-observability`.

### Required IAM permissions

This add-on uses the IAM roles for service accounts capability of Amazon EKS. For more information, see [IAM roles for service accounts](iam-roles-for-service-accounts.md "iam-roles-for-service-accounts.md"). The following managed policies are required:

- `AmazonPrometheusRemoteWriteAccess` - for remote writing metrics from the cluster to AMP
- `CloudWatchAgentServerPolicy` - for remote writing the logs from the cluster to CloudWatch

### Additional information

To learn more about the add-on and its capabilities, see [SageMaker HyperPod Observability](../../../sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-observability-cluster.md "../../../sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-observability-cluster.md").

## Amazon SageMaker HyperPod training operator

The Amazon SageMaker HyperPod training operator helps you accelerate generative AI model development by efficiently managing distributed training across large GPU clusters. It introduces intelligent fault recovery, hang job detection, and process-level management capabilities that minimize training disruptions and reduce costs. Unlike traditional training infrastructure that requires complete job restarts when failures occur, this operator implements surgical process recovery to keep your training jobs running smoothly.

The operator also works with HyperPod’s health monitoring and observability functions, providing real-time visibility into training execution and automatic monitoring of critical metrics like loss spikes and throughput degradation. You can define recovery policies through simple YAML configurations without code changes, allowing you to quickly respond to and recover from unrecoverable training states. These monitoring and recovery capabilities work together to maintain optimal training performance while minimizing operational overhead.

The Amazon EKS add-on name is `amazon-sagemaker-hyperpod-training-operator`.

For more information, see [Using the HyperPod training operator](../../../sagemaker/latest/dg/sagemaker-eks-operator.md "../../../sagemaker/latest/dg/sagemaker-eks-operator.md") in the _Amazon SageMaker Developer Guide_.

### Required IAM permissions

This add-on requires IAM permissions, and uses EKS Pod Identity.

AWS suggests the `AmazonSageMakerHyperPodTrainingOperatorAccess`
[managed policy](../../../aws-managed-policy/latest/reference/AmazonSageMakerHyperPodTrainingOperatorAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerHyperPodTrainingOperatorAccess.md").

For more information, see [Installing the training operator](../../../sagemaker/latest/dg/sagemaker-eks-operator-install.md#sagemaker-eks-operator-install-operator "../../../sagemaker/latest/dg/sagemaker-eks-operator-install.md#sagemaker-eks-operator-install-operator") in the _Amazon SageMaker Developer Guide_.

### Additional information

To learn more about the add-on, see [SageMaker HyperPod training operator](../../../sagemaker/latest/dg/sagemaker-eks-operator.md "../../../sagemaker/latest/dg/sagemaker-eks-operator.md").

## AWS Network Flow Monitor Agent

The Amazon CloudWatch Network Flow Monitor Agent is a Kubernetes application that collects TCP connection statistics from all nodes in a cluster and publishes network flow reports to Amazon CloudWatch Network Flow Monitor Ingestion APIs.

The Amazon EKS add-on name is `aws-network-flow-monitoring-agent`.

### Required IAM permissions

This add-on does require IAM permissions.

You need to attach the `CloudWatchNetworkFlowMonitorAgentPublishPolicy` managed policy to the add-on.

For more information on the required IAM setup, see [IAM Policy](https://github.com/aws/network-flow-monitor-agent?tab=readme-ov-file#iam-policy "https://github.com/aws/network-flow-monitor-agent?tab=readme-ov-file#iam-policy") on the Amazon CloudWatch Network Flow Monitor Agent GitHub repo.

For more information about the managed policy, see [CloudWatchNetworkFlowMonitorAgentPublishPolicy](../../../AmazonCloudWatch/latest/monitoring/security-iam-awsmanpol-network-flow-monitor.md#security-iam-awsmanpol-CloudWatchNetworkFlowMonitorAgentPublishPolicy "../../../AmazonCloudWatch/latest/monitoring/security-iam-awsmanpol-network-flow-monitor.md#security-iam-awsmanpol-CloudWatchNetworkFlowMonitorAgentPublishPolicy") in the Amazon CloudWatch User Guide.

### Additional information

To learn more about the add-on, see the [Amazon CloudWatch Network Flow Monitor Agent GitHub repo](https://github.com/aws/network-flow-monitor-agent?tab=readme-ov-file "https://github.com/aws/network-flow-monitor-agent?tab=readme-ov-file").

## Node monitoring agent

The node monitoring agent Amazon EKS add-on can detect additional node health issues. These extra health signals can also be leveraged by the optional node auto repair feature to automatically replace nodes as needed.

###### Note

You do not need to install this add-on on Amazon EKS Auto Mode clusters. For more information, see [Considerations for Amazon EKS Auto Mode](eks-add-ons.md#addon-consider-auto "eks-add-ons.md#addon-consider-auto").

The Amazon EKS add-on name is `eks-node-monitoring-agent`.

### Required IAM permissions

This add-on doesn’t require additional permissions.

### Additional information

For more information, see [Enable node auto repair and investigate node health issues](node-health.md "node-health.md").

## AWS Distro for OpenTelemetry

The AWS Distro for OpenTelemetry Amazon EKS add-on is a secure, production-ready, AWS supported distribution of the OpenTelemetry project. For more information, see [AWS Distro for OpenTelemetry](https://aws-otel.github.io/ "https://aws-otel.github.io/") on GitHub.

The Amazon EKS add-on name is `adot`.

### Required IAM permissions

This add-on only requires IAM permissions if you’re using one of the preconfigured custom resources that can be opted into through advanced configuration.

### Additional information

For more information, see [Getting Started with AWS Distro for OpenTelemetry using EKS Add-Ons](https://aws-otel.github.io/docs/getting-started/adot-eks-add-on "https://aws-otel.github.io/docs/getting-started/adot-eks-add-on") in the AWS Distro for OpenTelemetry documentation.

ADOT requires that the `cert-manager` add-on is deployed on the cluster as a prerequisite, otherwise this add-on won’t work if deployed directly using the [https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest](https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest "https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest")
`cluster_addons` property. For more requirements, see [Requirements for Getting Started with AWS Distro for OpenTelemetry using EKS Add-Ons](https://aws-otel.github.io/docs/getting-started/adot-eks-add-on/requirements "https://aws-otel.github.io/docs/getting-started/adot-eks-add-on/requirements") in the AWS Distro for OpenTelemetry documentation.

## Amazon GuardDuty agent

The Amazon GuardDuty agent Amazon EKS add-on collects [runtime events](../../../guardduty/latest/ug/runtime-monitoring-collected-events.md "../../../guardduty/latest/ug/runtime-monitoring-collected-events.md") (file access, process execution, network connections) from your EKS cluster nodes for analysis by GuardDuty Runtime Monitoring. GuardDuty itself (not the agent) is the security monitoring service that analyzes and processes [foundational data sources](../../../guardduty/latest/ug/guardduty_data-sources.md "../../../guardduty/latest/ug/guardduty_data-sources.md") including AWS CloudTrail management events and Amazon VPC flow logs, as well as [features](../../../guardduty/latest/ug/guardduty-features-activation-model.md "../../../guardduty/latest/ug/guardduty-features-activation-model.md"), such as Kubernetes audit logs and runtime monitoring.

The Amazon EKS add-on name is `aws-guardduty-agent`.

### Required IAM permissions

This add-on doesn’t require any permissions.

### Additional information

For more information, see [Runtime Monitoring for Amazon EKS clusters in Amazon GuardDuty](../../../guardduty/latest/ug/how-runtime-monitoring-works-eks.md "../../../guardduty/latest/ug/how-runtime-monitoring-works-eks.md").

- To detect potential security threats in your Amazon EKS clusters, enable Amazon GuardDuty runtime monitoring and deploy the GuardDuty security agent to your Amazon EKS clusters.

## Amazon CloudWatch Observability agent

The Amazon CloudWatch Observability agent Amazon EKS add-on the monitoring and observability service provided by AWS. This add-on installs the CloudWatch Agent and enables both CloudWatch Application Signals and CloudWatch Container Insights with enhanced observability for Amazon EKS. For more information, see [Amazon CloudWatch Agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md").

The Amazon EKS add-on name is `amazon-cloudwatch-observability`.

### Required IAM permissions

This add-on uses the IAM roles for service accounts capability of Amazon EKS. For more information, see [IAM roles for service accounts](iam-roles-for-service-accounts.md "iam-roles-for-service-accounts.md"). The permissions in the [AWSXrayWriteOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess") and [CloudWatchAgentServerPolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy")
AWS managed policies are required. You can create an IAM role, attach the managed policies to it, and annotate the Kubernetes service account used by the add-on with the following command. Replace `my-cluster` with the name of your cluster and `AmazonEKS_Observability_role` with the name for your role. This command requires that you have [eksctl](https://eksctl.io "https://eksctl.io") installed on your device. If you need to use a different tool to create the role, attach the policy to it, and annotate the Kubernetes service account, see [Assign IAM roles to Kubernetes service accounts](associate-service-account-role.md "associate-service-account-role.md").

```
eksctl create iamserviceaccount \
    --name cloudwatch-agent \
    --namespace amazon-cloudwatch \
    --cluster my-cluster \
    --role-name AmazonEKS_Observability_Role \
    --role-only \
    --attach-policy-arn arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess \
    --attach-policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy \
    --approve
```

### Additional information

For more information, see [Install the CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.md "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.md").

## AWS Private CA Connector for Kubernetes

The AWS Private CA Connector for Kubernetes is an add-on for cert-manager that enables users to obtain Certificates from AWS Private Certificate Authority (AWS Private CA).

- The Amazon EKS add-on name is `aws-privateca-connector-for-kubernetes`.
- The add-on namespace is `aws-privateca-issuer`.

This add-on requires `cert-manager`. `cert-manager` is available on Amazon EKS as a community add-on. For more information about this add-on, see [Cert Manager](community-addons.md#addon-cert-manager "community-addons.md#addon-cert-manager"). For more information about installing add-ons, see [Create an Amazon EKS add-on](creating-an-add-on.md "creating-an-add-on.md").

### Required IAM permissions

This add-on requires IAM permissions.

Use EKS Pod Identities to attach the `AWSPrivateCAConnectorForKubernetesPolicy` IAM Policy to the `aws-privateca-issuer` Kubernetes Service Account. For more information, see [Use Pod Identities to assign an IAM role to an Amazon EKS add-on](update-addon-role.md "update-addon-role.md").

For information about the required permissions, see [AWSPrivateCAConnectorForKubernetesPolicy](../../../aws-managed-policy/latest/reference/AWSPrivateCAConnectorForKubernetesPolicy.md "../../../aws-managed-policy/latest/reference/AWSPrivateCAConnectorForKubernetesPolicy.md") in the AWS Managed Policy Reference.

### Additional information

For more information, see the [AWS Private CA Issuer for Kubernetes GitHub repository](https://github.com/cert-manager/aws-privateca-issuer "https://github.com/cert-manager/aws-privateca-issuer").

For more information about configuring the add-on, see [values.yaml](https://github.com/cert-manager/aws-privateca-issuer/blob/main/charts/aws-pca-issuer/values.yaml "https://github.com/cert-manager/aws-privateca-issuer/blob/main/charts/aws-pca-issuer/values.yaml") in the `aws-privateca-issuer` GitHub repo. Confirm the version of values.yaml matches the version of the add-on installed on your cluster.

This add-on tolerates the `CriticalAddonsOnly` taint used by the `system` NodePool of EKS Auto Mode. For more information, see [Run critical add-ons on dedicated instances](critical-workload.md "critical-workload.md").

## EKS Pod Identity Agent

The Amazon EKS Pod Identity Agent Amazon EKS add-on provides the ability to manage credentials for your applications, similar to the way that EC2 instance profiles provide credentials to EC2 instances.

###### Note

You do not need to install this add-on on Amazon EKS Auto Mode clusters. Amazon EKS Auto Mode integrates with EKS Pod Identity. For more information, see [Considerations for Amazon EKS Auto Mode](eks-add-ons.md#addon-consider-auto "eks-add-ons.md#addon-consider-auto").

The Amazon EKS add-on name is `eks-pod-identity-agent`.

### Required IAM permissions

The Pod Identity Agent add-on itself does not require an IAM role. It uses permissions from the [Amazon EKS node IAM role](create-node-role.md "create-node-role.md") to function, but does not need a dedicated IAM role for the add-on.

### Update information

You can only update one minor version at a time. For example, if your current version is `1.28.x-eksbuild.y` and you want to update to `1.30.x-eksbuild.y`, then you must update your current version to `1.29.x-eksbuild.y` and then update it again to `1.30.x-eksbuild.y`. For more information about updating the add-on, see [Update an Amazon EKS add-on](updating-an-add-on.md "updating-an-add-on.md").

## SR-IOV Network Metrics Exporter

The SR-IOV Network Metrics Exporter Amazon EKS add-on collects and exposes metrics about SR-IOV network devices in Prometheus format. It enables monitoring of SR-IOV network performance on EKS bare metal nodes. The exporter runs as a DaemonSet on nodes with SR-IOV-capable network interfaces and exports metrics that can be scraped by Prometheus.

###### Note

This add-on requires nodes with SR-IOV-capable network interfaces.

| Property               | Value                                                                                                                                                                                          |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add-on name            | `sriov-network-metrics-exporter`                                                                                                                                                               |
| Namespace              | `monitoring`                                                                                                                                                                                   |
| Documentation          | [SR-IOV Network Metrics Exporter GitHub repo](https://github.com/k8snetworkplumbingwg/sriov-network-metrics-exporter "https://github.com/k8snetworkplumbingwg/sriov-network-metrics-exporter") |
| Service account name   | None                                                                                                                                                                                           |
| Managed IAM policy     | None                                                                                                                                                                                           |
| Custom IAM permissions | None                                                                                                                                                                                           |

### AWS Secrets Store CSI Driver provider

The AWS provider for the Secrets Store CSI Driver is an add-on that enables retrieving secrets from AWS Secrets Manager and parameters from AWS Systems Manager Parameter Store and mounting them as files in Kubernetes pods.

### Required IAM permissions

The add-on does not require IAM permissions. However, application pods will require IAM permissions to fetch secrets from AWS Secrets Manager and parameters from AWS Systems Manager Parameter Store. After installing the add-on, access must be configured via IAM Roles for Service Accounts (IRSA) or EKS Pod Identity. To use IRSA, please refer to the Secrets Manager [IRSA setup documentation](../../../secretsmanager/latest/userguide/integrating_ascp_irsa.md "../../../secretsmanager/latest/userguide/integrating_ascp_irsa.md"). To use EKS Pod Identity, please refer to the Secrets Manager [Pod Identity setup documentation](../../../secretsmanager/latest/userguide/ascp-pod-identity-integration.md "../../../secretsmanager/latest/userguide/ascp-pod-identity-integration.md").

AWS suggests the `AWSSecretsManagerClientReadOnlyAccess`
[managed policy](../../../secretsmanager/latest/userguide/reference_available-policies.md#security-iam-awsmanpol-AWSSecretsManagerClientReadOnlyAccess "../../../secretsmanager/latest/userguide/reference_available-policies.md#security-iam-awsmanpol-AWSSecretsManagerClientReadOnlyAccess").

For more information about the required permissions, see `AWSSecretsManagerClientReadOnlyAccess` in the AWS Managed Policy Reference.

### Additional information

For more information, please see the secrets-store-csi-driver-provider-aws [GitHub repository](https://github.com/aws/secrets-store-csi-driver-provider-aws "https://github.com/aws/secrets-store-csi-driver-provider-aws").

To learn more about the add-on, please refer to the [AWS Secrets Manager documentation for the add-on](../../../secretsmanager/latest/userguide/ascp-eks-installation.md "../../../secretsmanager/latest/userguide/ascp-eks-installation.md").

## Amazon SageMaker Spaces

The Amazon SageMaker Spaces Add-on provides ability to run IDEs and Notebooks on EKS or HyperPod-EKS clusters. Administrators can use EKS Console to install the add-on on their cluster, and define default space configurations such as images, compute resources, local storage for notebook settings (additional storage to be attached to their spaces), file systems, and initialization scripts.

AI developers can use kubectl to create, update, and delete spaces. They have the flexibility to use default configurations provided by admins or customize settings. AI developers can access their spaces on EKS or HyperPod-EKS using their local VS Code IDEs, and/or their web browser that hosts their JupyterLab or CodeEditor IDE on custom DNS domain configured by their admins. They can also use kubernetes’ port forwarding feature to access spaces in their web browsers.

The Amazon EKS add-on name is `amazon-sagemaker-spaces`.

### Required IAM permissions

This add-on requires IAM permissions. For more information about the required IAM setup, see [IAM Permissions Setup](../../../sagemaker/latest/dg/permission-setup.md "../../../sagemaker/latest/dg/permission-setup.md") in the _Amazon SageMaker Developer Guide_.

### Additional information

To learn more about the add-on and its capabilities, see [SageMaker AI Notebooks on HyperPod](../../../sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-ide.md "../../../sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-ide.md") in the _Amazon SageMaker Developer Guide_.

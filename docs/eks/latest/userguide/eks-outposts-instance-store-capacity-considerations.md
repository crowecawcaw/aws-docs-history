

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Select instance types and placement for Amazon EKS local clusters on AWS Outposts configured with EC2 instance store
<a name="eks-outposts-instance-store-capacity-considerations"></a>

This topic provides guidance for selecting Kubernetes control plane instance types and configuring placement to meet high-availability requirements for your local Amazon EKS cluster on an AWS Outpost configured with EC2 instance store.

**Note**  
If your Outpost is configured with Amazon EBS instead of EC2 instance store, the architecture described in this topic isn’t available for your Outpost. Outposts configured with EBS will continue to use the existing local clusters implementation. For more information, see [Select instance types and placement groups for Amazon EKS clusters on AWS Outposts based on capacity considerations](eks-outposts-capacity-considerations.md).  
If you are interested in creating a local cluster on an EBS-backed Outpost using the updated local clusters architecture, contact your AWS account team.

## Control plane architecture
<a name="eks-outposts-instance-store-capacity-considerations-architecture"></a>

The local cluster Kubernetes control plane runs on **6 EC2 instances** on your Outpost:
+  **3 control plane instances** — host the Kubernetes control plane components, including the Kubernetes API server, scheduler, and controller manager.
+  **3 `etcd` instances** — store Kubernetes cluster state in an [external etcd topology](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/#external-etcd-topology).

These instances run in an AWS-managed service account on your Outpost. They don’t appear as EC2 instances in your AWS account or in the Amazon EC2 console. The capacity consumed by the control plane is visible in the AWS Outposts console.

The control plane does not horizontally scale under load. If you need a different control plane instance size, you must create a new cluster.

## Instance type selection
<a name="eks-outposts-instance-store-capacity-considerations-instance-type"></a>

With the updated architecture for Amazon EKS local clusters on AWS Outposts, the Kubernetes control plane uses a dedicated `etcd` topology: the API server and `etcd` run on separate instances. When you create a cluster, you specify two instance types: `controlPlaneInstanceType` for the API server and `etcdInstanceType` for `etcd`.

The instance types you choose must be available on your Outpost. Available instance families depend on your Outpost generation and SKU, and different instance families can have different vCPU and memory configurations at the same instance size.

 **API server (`controlPlaneInstanceType`)** 


| Expected worker nodes | vCPUs | Memory | 
| --- | --- | --- | 
| 1–20 | 2 | 8 GiB | 
| 21–100 | 4 | 16 GiB | 
| 101–250 | 8 | 32 GiB | 
| 251–500 | 16 | 64 GiB | 

 ** `etcd` (`etcdInstanceType`)** 


| Expected worker nodes | vCPUs | Memory | 
| --- | --- | --- | 
| 1–50 | 2 | 8 GiB | 
| 51–250 | 4 | 16 GiB | 
| 251–500 | 8 | 32 GiB | 

**Important**  
Make sure that your Outpost has capacity for 3 instances of `controlPlaneInstanceType` and 3 instances of `etcdInstanceType` for the lifetime of your local cluster.

Use these tables as a guideline rather than a strict requirement. We recommend selecting an instance family and size that accommodate your anticipated growth, because `controlPlaneInstanceType` and `etcdInstanceType` can’t be changed after cluster creation. To change either, you must create a new cluster.

## Control plane and `etcd` placement
<a name="eks-outposts-instance-store-capacity-considerations-placement"></a>

For high availability, we recommend spreading your control plane and `etcd` instances across multiple hardware failure domains. You can control this spread using the `spreadLevel` property on `controlPlanePlacement` and `etcdPlacement` in `outpostConfig`. When you set `spreadLevel`, Amazon EKS creates an EC2 placement group with the Spread strategy. You don’t need to pre-create a placement group.

**Note**  
The `groupName` parameter in `controlPlanePlacement` is not used with Outposts that run instance store-based EC2 instances. If you previously used a placement group with a local cluster, you now use `spreadLevel` instead.

### Spread levels
<a name="eks-outposts-instance-store-capacity-considerations-spread-levels"></a>

The `spreadLevel` property accepts two values:
+  ** `host` ** — Spreads control plane instances across different physical hosts. Requires at least 3 hosts configured with the chosen instance type.
+  ** `rack` ** — Spreads control plane instances across different physical Outpost racks. Requires at least 3 racks with hosts configured with the chosen instance type.

## Capacity planning
<a name="eks-outposts-instance-store-capacity-considerations-capacity-planning"></a>

When planning Outpost capacity for local clusters, account for the following:
+  **Control plane and `etcd` instances:** 6 instances per cluster (3 of `controlPlaneInstanceType` and 3 of `etcdInstanceType`).
+  **Worker nodes:** The EC2 instances for your self-managed node groups.
+  **Virtualized hosts:** The control plane must run on virtualized hosts. Your Outpost must have virtualized hosts with sufficient capacity.

## Troubleshooting placement issues
<a name="eks-outposts-instance-store-capacity-considerations-troubleshooting"></a>

If your cluster remains in the `CREATING` or `UPDATING` state for an extended period after you specify a spread level, verify that your Outpost has sufficient hosts or racks with the chosen instance type to satisfy the spread topology.

For more information about troubleshooting local clusters, see [Troubleshoot local Amazon EKS clusters on AWS Outposts configured with EC2 instance store](eks-outposts-instance-store-troubleshooting.md).
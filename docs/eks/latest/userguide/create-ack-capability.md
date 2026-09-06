

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an ACK capability
<a name="create-ack-capability"></a>

This chapter explains how to create an ACK capability on your Amazon EKS cluster.

## Prerequisites
<a name="_prerequisites"></a>

Before creating an ACK capability, ensure you have:
+ An Amazon EKS cluster
+ An IAM Capability Role with permissions for ACK to manage AWS resources
+ Sufficient IAM permissions to create capability resources on EKS clusters
+ The appropriate CLI tool installed and configured, or access to the EKS Console

For instructions on creating the IAM Capability Role, see [Amazon EKS capability IAM role](capability-role.md).

**Important**  
ACK is an infrastructure management capability that grants the ability to create, modify, and delete AWS resources. This is an admin-scoped capability that should be carefully controlled. Anyone with permission to create Kubernetes resources in your cluster can effectively create AWS resources through ACK, subject to the IAM Capability Role permissions. The IAM Capability Role you provide determines which AWS resources ACK can create and manage. For guidance on creating an appropriate role with least-privilege permissions, see [Amazon EKS capability IAM role](capability-role.md) and [Security considerations for EKS Capabilities](capabilities-security.md).

## Choose your tool
<a name="_choose_your_tool"></a>

You can create an ACK capability using the AWS Management Console, AWS CLI, or eksctl:
+  [Create an ACK capability using the Console](ack-create-console.md) - Use the Console for a guided experience
+  [Create an ACK capability using the AWS CLI](ack-create-cli.md) - Use the AWS CLI for scripting and automation
+  [Create an ACK capability using eksctl](ack-create-eksctl.md) - Use eksctl for a Kubernetes-native experience

## What happens when you create an ACK capability
<a name="_what_happens_when_you_create_an_ack_capability"></a>

When you create an ACK capability:

1. EKS creates the ACK capability service and configures it to monitor and manage resources in your cluster

1. Custom Resource Definitions (CRDs) are installed in your cluster

1. An access entry is automatically created for your IAM Capability Role with capability-specific access entry policies that grant baseline Kubernetes permissions (see [Security considerations for EKS Capabilities](capabilities-security.md))

1. The capability assumes the IAM Capability Role you provide

1. ACK begins watching for its custom resources in your cluster

1. The capability status changes from `CREATING` to `ACTIVE` 

Once active, you can create ACK custom resources in your cluster to manage AWS resources.

**Note**  
The automatically created access entry includes the `AmazonEKSACKPolicy` which grants ACK permissions to manage AWS resources. Some ACK resources that reference Kubernetes secrets (such as RDS databases with passwords) require additional access entry policies. To learn more about access entries and how to configure additional permissions, see [Security considerations for EKS Capabilities](capabilities-security.md).

## Next steps
<a name="_next_steps"></a>

After creating the ACK capability:
+  [ACK concepts](ack-concepts.md) - Understand ACK concepts and get started with AWS resources
+  [Configure ACK permissions](ack-permissions.md) - Configure IAM permissions and multi-account patterns
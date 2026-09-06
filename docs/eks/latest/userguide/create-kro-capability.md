

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create a kro capability
<a name="create-kro-capability"></a>

This topic explains how to create a kro capability on your Amazon EKS cluster.

## Prerequisites
<a name="_prerequisites"></a>

Before creating a kro capability, ensure you have:
+ An existing Amazon EKS cluster running a supported Kubernetes version (all versions in standard and extended support are supported)
+ Sufficient IAM permissions to create capability resources on EKS clusters
+ (For CLI/eksctl) The appropriate CLI tool installed and configured

**Note**  
Unlike ACK and Argo CD, kro does not require additional IAM permissions beyond the trust policy. kro operates entirely within your cluster and does not make AWS API calls. However, you still need to provide an IAM Capability Role with the appropriate trust policy. For information about configuring Kubernetes RBAC permissions for kro, see [Configure kro permissions](kro-permissions.md).

## Choose your tool
<a name="_choose_your_tool"></a>

You can create a kro capability using the AWS Management Console, AWS CLI, or eksctl:
+  [Create a kro capability using the Console](kro-create-console.md) - Use the Console for a guided experience
+  [Create a kro capability using the AWS CLI](kro-create-cli.md) - Use the AWS CLI for scripting and automation
+  [Create a kro capability using eksctl](kro-create-eksctl.md) - Use eksctl for a Kubernetes-native experience

## What happens when you create a kro capability
<a name="_what_happens_when_you_create_a_kro_capability"></a>

When you create a kro capability:

1. EKS creates the kro capability service and configures it to monitor and manage resources in your cluster

1. Custom Resource Definitions (CRDs) are installed in your cluster

1. An access entry is automatically created for your IAM Capability Role with the `AmazonEKSKROPolicy` which grants permissions to manage ResourceGraphDefinitions and their instances (see [Security considerations for EKS Capabilities](capabilities-security.md))

1. The capability assumes the IAM Capability Role you provide (used only for the trust relationship)

1. kro begins watching for `ResourceGraphDefinition` resources and their instances

1. The capability status changes from `CREATING` to `ACTIVE` 

Once active, you can create ResourceGraphDefinitions to define custom APIs and create instances of those APIs.

**Note**  
The automatically created access entry includes the `AmazonEKSKROPolicy` which grants kro permissions to manage ResourceGraphDefinitions and their instances. To allow kro to create the underlying Kubernetes resources defined in your ResourceGraphDefinitions (such as Deployments, Services, or ACK resources), you must configure additional access entry policies. To learn more about access entries and how to configure additional permissions, see [Configure kro permissions](kro-permissions.md) and [Security considerations for EKS Capabilities](capabilities-security.md).

## Next steps
<a name="_next_steps"></a>

After creating the kro capability:
+  [kro concepts](kro-concepts.md) - Understand kro concepts and resource composition
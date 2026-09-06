

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Prepare cluster access for hybrid nodes
<a name="hybrid-nodes-cluster-prep"></a>

Before connecting hybrid nodes to your Amazon EKS cluster, you must enable your Hybrid Nodes IAM Role with Kubernetes permissions to join the cluster. See [Prepare credentials for hybrid nodes](hybrid-nodes-creds.md) for information on how to create the Hybrid Nodes IAM role. Amazon EKS supports two ways to associate IAM principals with Kubernetes Role-Based Access Control (RBAC), Amazon EKS access entries and the `aws-auth` ConfigMap. For more information on Amazon EKS access management, see [Grant IAM users and roles access to Kubernetes APIs](grant-k8s-access.md).

Use the procedures below to associate your Hybrid Nodes IAM role with Kubernetes permissions. To use Amazon EKS access entries, your cluster must have been created with the `API` or `API_AND_CONFIG_MAP` authentication modes. To use the `aws-auth` ConfigMap, your cluster must have been created with the `API_AND_CONFIG_MAP` authentication mode. The `CONFIG_MAP`-only authentication mode is not supported for hybrid nodes-enabled Amazon EKS clusters.

## Using Amazon EKS access entries for Hybrid Nodes IAM role
<a name="_using_amazon_eks_access_entries_for_hybrid_nodes_iam_role"></a>

There is an Amazon EKS access entry type for hybrid nodes named HYBRID\_LINUX that can be used with an IAM role. With this access entry type, the username is automatically set to system:node:{{SessionName}}. For more information on creating access entries, see [Create access entries](creating-access-entries.md).

### AWS CLI
<a name="shared_aws_cli"></a>

1. You must have the latest version of the AWS CLI installed and configured on your device. To check your current version, use `aws --version`. Package managers such as yum, apt-get, or Homebrew for macOS are often several versions behind the latest version of the AWS CLI. To install the latest version, see Installing and Quick configuration with aws configure in the AWS Command Line Interface User Guide.

1. Create your access entry with the following command. Replace CLUSTER\_NAME with the name of your cluster and HYBRID\_NODES\_ROLE\_ARN with the ARN of the role you created in the steps for [Prepare credentials for hybrid nodes](hybrid-nodes-creds.md).

   ```
   aws eks create-access-entry --cluster-name CLUSTER_NAME \
       --principal-arn HYBRID_NODES_ROLE_ARN \
       --type HYBRID_LINUX
   ```

### AWS Management Console
<a name="hybrid-nodes-cluster-prep-console"></a>

1. Open the Amazon EKS console at [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. Choose the name of your hybrid nodes-enabled cluster.

1. Choose the **Access** tab.

1. Choose **Create access entry**.

1. For **IAM principal**, select the Hybrid Nodes IAM role you created in the steps for [Prepare credentials for hybrid nodes](hybrid-nodes-creds.md).

1. For **Type**, select **Hybrid Linux**.

1. (Optional) For **Tags**, assign labels to the access entry. For example, to make it easier to find all resources with the same tag.

1. Choose **Skip to review and create**. You cannot add policies to the Hybrid Linux access entry or change its access scope.

1. Review the configuration for your access entry. If anything looks incorrect, choose **Previous** to go back through the steps and correct the error. If the configuration is correct, choose **Create**.

## Using aws-auth ConfigMap for Hybrid Nodes IAM role
<a name="_using_aws_auth_configmap_for_hybrid_nodes_iam_role"></a>

In the following steps, you will create or update the `aws-auth` ConfigMap with the ARN of the Hybrid Nodes IAM Role you created in the steps for [Prepare credentials for hybrid nodes](hybrid-nodes-creds.md).

1. Check to see if you have an existing `aws-auth` ConfigMap for your cluster. Note that if you are using a specific `kubeconfig` file, use the `--kubeconfig` flag.

   ```
   kubectl describe configmap -n kube-system aws-auth
   ```

1. If you are shown an `aws-auth` ConfigMap, then update it as needed.

   1. Open the ConfigMap for editing.

      ```
      kubectl edit -n kube-system configmap/aws-auth
      ```

   1. Add a new `mapRoles` entry as needed. Replace `HYBRID_NODES_ROLE_ARN` with the ARN of your Hybrid Nodes IAM role. Note, `{{SessionName}}` is the correct template format to save in the ConfigMap. Do not replace it with other values.

      ```
      data:
        mapRoles: |
        - groups:
          - system:bootstrappers
          - system:nodes
          rolearn: HYBRID_NODES_ROLE_ARN
          username: system:node:{{SessionName}}
      ```

   1. Save the file and exit your text editor.

1. If there is not an existing `aws-auth` ConfigMap for your cluster, create it with the following command. Replace `HYBRID_NODES_ROLE_ARN` with the ARN of your Hybrid Nodes IAM role. Note that `{{SessionName}}` is the correct template format to save in the ConfigMap. Do not replace it with other values.

   ```
   kubectl apply -f=/dev/stdin <<-EOF
   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: aws-auth
     namespace: kube-system
   data:
     mapRoles: |
     - groups:
       - system:bootstrappers
       - system:nodes
       rolearn: HYBRID_NODES_ROLE_ARN
       username: system:node:{{SessionName}}
   EOF
   ```
**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Get started with Amazon EKS – AWS Management Console and AWS CLI

###### Note

This topic covers getting started **without** EKS Auto Mode. It uses Managed Node Groups to deploy nodes.

EKS Auto Mode automates routine tasks for cluster compute, storage, and networking. [Learn how to get started with Amazon EKS Auto Mode.](getting-started-automode.md "getting-started-automode.md") EKS Auto Mode is the preferred method of deploying nodes.

This guide helps you to create all of the required resources to get started with Amazon Elastic Kubernetes Service (Amazon EKS) using the AWS Management Console and the AWS CLI. In this guide, you manually create each resource. At the end of this tutorial, you will have a running Amazon EKS cluster that you can deploy applications to.

The procedures in this guide give you complete visibility into how each resource is created and how the resources interact with each other. If you’d rather have most of the resources created for you automatically, use the `eksctl` CLI to create your cluster and nodes. For more information, see [Get started with Amazon EKS – eksctl](getting-started-eksctl.md "getting-started-eksctl.md").

## Prerequisites

Before starting this tutorial, you must install and configure the following tools and resources that you need to create and manage an Amazon EKS cluster.

- **AWS CLI**
  – A command line tool for working with AWS services, including Amazon EKS. For more information, see [Installing](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") in the AWS Command Line Interface User Guide. After installing the AWS CLI, we recommend that you also configure it. For more information, see [Quick configuration with aws configure](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config") in the AWS Command Line Interface User Guide. Note that AWS CLI v2 is required to use the **update-kubeconfig** option shown in this page.
- **`kubectl`**
  – A command line tool for working with Kubernetes clusters. For more information, see [Set up kubectl and eksctl](install-kubectl.md "install-kubectl.md").
- **Required IAM permissions**
  – The IAM security principal that you’re using must have permissions to work with Amazon EKS IAM roles, service linked roles, AWS CloudFormation, a VPC, and related resources. For more information, see [Actions](../../../service-authorization/latest/reference/list_amazonelastickubernetesservice.md "../../../service-authorization/latest/reference/list_amazonelastickubernetesservice.md") and [Using service-linked roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") in the IAM User Guide. You must complete all steps in this guide as the same user. To check the current user, run the following command:

```
aws sts get-caller-identity
```

We recommend that you complete the steps in this topic in a Bash shell. If you aren’t using a Bash shell, some script commands such as line continuation characters and the way variables are set and used require adjustment for your shell. Additionally, the quoting and escaping rules for your shell might be different. For more information, see [Using quotation marks with strings in the AWS CLI](../../../cli/latest/userguide/cli-usage-parameters-quoting-strings.md "../../../cli/latest/userguide/cli-usage-parameters-quoting-strings.md") in the AWS Command Line Interface User Guide.

## Step 1: Create your Amazon EKS cluster

###### Important

To get started as simply and quickly as possible, this topic includes steps to create a cluster with default settings. Before creating a cluster for production use, we recommend that you familiarize yourself with all settings and deploy a cluster with the settings that meet your requirements. For more information, see [Create an Amazon EKS cluster](create-cluster.md "create-cluster.md"). Some settings can only be enabled when creating your cluster.

1. Create an Amazon VPC with public and private subnets that meets Amazon EKS requirements. Replace `region-code` with any AWS Region that is supported by Amazon EKS. For a list of AWS Regions, see [Amazon EKS endpoints and quotas](../../../general/latest/gr/eks.md "../../../general/latest/gr/eks.md") in the AWS General Reference guide. You can replace `my-eks-vpc-stack` with any name you choose.

```
aws cloudformation create-stack \
  --region `region-code` \
  --stack-name my-eks-vpc-stack \
  --template-url https://s3.us-west-2.amazonaws.com/amazon-eks/cloudformation/2020-10-29/amazon-eks-vpc-private-subnets.yaml
```

###### Tip

For a list of all the resources the previous command creates, open the AWS CloudFormation console at [https://console.aws.amazon.com/cloudformation/](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/"). Choose the `my-eks-vpc-stack` stack and then choose the **Resources** tab. 2. Create a cluster IAM role and attach the required Amazon EKS IAM managed policy to it. Kubernetes clusters managed by Amazon EKS make calls to other AWS services on your behalf to manage the resources that you use with the service.

    1. Copy the following contents to a file named `eks-cluster-role-trust-policy.json`.



    ```
    {
      "Version":"2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Service": "eks.amazonaws.com"
          },
          "Action": "sts:AssumeRole"
        }
      ]
    }
    ```
    2. Create the role.



    ```
    aws iam create-role \
      --role-name myAmazonEKSClusterRole \
      --assume-role-policy-document file://"eks-cluster-role-trust-policy.json"
    ```
    3. Attach the required Amazon EKS managed IAM policy to the role.



    ```
    aws iam attach-role-policy \
      --policy-arn arn:aws:iam::aws:policy/AmazonEKSClusterPolicy \
      --role-name myAmazonEKSClusterRole
    ```

3. Open the Amazon EKS console at [[https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters")](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").

Make sure that the AWS Region shown in the upper right of your console is the AWS Region that you want to create your cluster in. If it’s not, choose the dropdown next to the AWS Region name and choose the AWS Region that you want to use. 4. Choose **Create cluster**. If you don’t see this option, then choose **Clusters** in the left navigation pane first. 5. On the **Configure cluster** page, do the following:

    1. Select **Custom configuration** and disable **Use EKS Auto Mode**. (If you prefer an EKS Auto Mode cluster, refer instead to [Create an EKS Auto Mode Cluster with the AWS Management Console](automode-get-started-console.md "automode-get-started-console.md").)
    2. Enter a **Name** for your cluster, such as `my-cluster`. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphanumeric character and can’t be longer than 100 characters. The name must be unique within the AWS Region and AWS account that you’re creating the cluster in.
    3. For **Cluster Service Role**, choose `myAmazonEKSClusterRole`.
    4. Leave the remaining settings at their default values and choose **Next**.

6. On the **Specify networking** page, do the following:
   1. Choose the ID of the VPC that you created in a previous step from the **VPC** dropdown list. It is something like `* | my-eks-vpc-stack-VPC`.
   2. Choose the subnets created in a previous step from the **Subnets** dropdown list. The subnets will be something like `* | my-eks-vpc-stack-*`.
   3. Choose the security group created in a previous step from the **Additional security groups** dropdown list. It is something like `* | my-eks-vpc-stack-ControlPlaneSecurityGroup-*`.
   4. Leave the remaining settings at their default values and choose **Next**.

7. On the **Configure observability** page, choose **Next**.
8. On the **Select add-ons** page, choose **Next**.

For more information on add-ons, see [Amazon EKS add-ons](eks-add-ons.md "eks-add-ons.md"). 9. On the **Configure selected add-ons settings** page, choose **Next**. 10. On the **Review and create** page, choose **Create**.

To the right of the cluster’s name, the cluster status is **Creating** for several minutes until the cluster provisioning process completes. Don’t continue to the next step until the status is **Active**.

###### Note

You might receive an error that one of the Availability Zones in your request doesn’t have sufficient capacity to create an Amazon EKS cluster. If this happens, the error output contains the Availability Zones that can support a new cluster. Retry creating your cluster with at least two subnets that are located in the supported Availability Zones for your account. For more information, see [Insufficient capacity](troubleshooting.md#ice "troubleshooting.md#ice").

## Step 2: Configure your computer to communicate with your cluster

In this section, you create a `kubeconfig` file for your cluster. The settings in this file enable the `kubectl` CLI to communicate with your cluster.

Before proceeding, be sure that your cluster creation completed successfully in Step 1.

1. Create or update a `kubeconfig` file for your cluster. Replace `region-code` with the AWS Region that you created your cluster in. Replace `my-cluster` with the name of your cluster.

```
aws eks update-kubeconfig --region `region-code` --name `my-cluster`

```

By default, the `config` file is created in `~/.kube` or the new cluster’s configuration is added to an existing `config` file in `~/.kube`. 2. Test your configuration.

```
kubectl get svc
```

###### Note

If you receive any authorization or resource type errors, see [Unauthorized or access denied (kubectl)](troubleshooting.md#unauthorized "troubleshooting.md#unauthorized") in the troubleshooting topic.

An example output is as follows.

```
NAME             TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
svc/kubernetes   ClusterIP   10.100.0.1   <none>        443/TCP   1m
```

## Step 3: Create nodes

###### Important

To get started as simply and quickly as possible, this topic includes steps to create nodes with mostly default settings. Before creating nodes for production use, we recommend that you familiarize yourself with all settings and deploy nodes with the settings that meet your requirements. For more information, see [Manage compute resources by using nodes](eks-compute.md "eks-compute.md"). Some settings can only be enabled when creating your nodes.

This procedure configures your cluster to use Managed node groups to create nodes, specifying the subnets and node IAM role that you created in previous steps.
It lets you run Amazon Linux applications on Amazon EC2 instances.

To learn more about different ways to configure nodes in EKS, see [Manage compute resources by using nodes](eks-compute.md "eks-compute.md"). After your cluster is deployed, you can add other node types. Though not covered in this guide, you can also add [Windows self-managed](launch-windows-workers.md "launch-windows-workers.md") and [Bottlerocket](launch-node-bottlerocket.md "launch-node-bottlerocket.md") nodes to your cluster.

**To create your EC2 Linux managed node group**

1. Create a node IAM role and attach the required Amazon EKS IAM managed policy to it. The Amazon EKS node `kubelet` daemon makes calls to AWS APIs on your behalf. Nodes receive permissions for these API calls through an IAM instance profile and associated policies.
   1. Copy the following contents to a file named `node-role-trust-policy.json`.

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

   2. Create the node IAM role.

   ```
   aws iam create-role \
     --role-name myAmazonEKSNodeRole \
     --assume-role-policy-document file://"node-role-trust-policy.json"
   ```

   3. Attach the required managed IAM policies to the role.

   ```
   aws iam attach-role-policy \
     --policy-arn arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy \
     --role-name myAmazonEKSNodeRole
   aws iam attach-role-policy \
     --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly \
     --role-name myAmazonEKSNodeRole
   aws iam attach-role-policy \
     --policy-arn arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy \
     --role-name myAmazonEKSNodeRole
   ```

   4. Open the Amazon EKS console at [[https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters")](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
   5. Choose the name of the cluster that you created in [Step 1: Create your Amazon EKS cluster](#eks-create-cluster "#eks-create-cluster"), such as `my-cluster`.
   6. On the **`my-cluster`** page, do the following:
   7. Choose the **Compute** tab.
   8. Choose **Add Node Group**.

2. On the **Configure Node Group** page, do the following:
   1. For **Name**, enter a unique name for your managed node group, such as `my-nodegroup`. The node group name can’t be longer than 63 characters. It must start with letter or digit, but can also include hyphens and underscores for the remaining characters.
   2. For **Node IAM role name**, choose `myAmazonEKSNodeRole` role that you created in a previous step. We recommend that each node group use its own unique IAM role.
   3. Choose **Next**.

3. On the **Set compute and scaling configuration** page, accept the default values and choose **Next**.
4. On the **Specify networking** page, accept the default values and choose **Next**.
5. On the **Review and create** page, review your managed node group configuration and choose **Create**.
6. After several minutes, the **Status** in the **Node Group configuration** section will change from **Creating** to **Active**. Don’t continue to the next step until the status is **Active**.

## Step 4: View resources

You can view your nodes and Kubernetes workloads.

1. In the left navigation pane, choose **Clusters**. In the list of **Clusters**, choose the name of the cluster that you created, such as `my-cluster`.
2. On the **`my-cluster`** page, choose the following:
   1. **Compute**
      tab – You see the list of **Nodes** that were deployed for the cluster. You can choose the name of a node to see more information about it.
   2. **Resources** tab
      – You see all of the Kubernetes resources that are deployed by default to an Amazon EKS cluster. Select any resource type in the console to learn more about it.

## Step 5: Delete resources

After you’ve finished with the cluster and nodes that you created for this tutorial, you should delete the resources that you created. If you want to do more with this cluster before you delete the resources, see [Next steps](#gs-console-next-steps "#gs-console-next-steps").

1. Delete any node groups profiles that you created.
   1. Open the Amazon EKS console at [[https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters")](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
   2. In the left navigation pane, choose **Clusters**. In the list of clusters, choose `my-cluster`.
   3. Choose the **Compute** tab.
   4. If you created a node group, choose the `my-nodegroup` node group and then choose **Delete**. Enter `my-nodegroup`, and then choose **Delete**.
   5. Don’t continue until the node group profiles are deleted.

2. Delete the cluster.
   1. In the left navigation pane, choose **Clusters**. In the list of clusters, choose `my-cluster`.
   2. Choose **Delete cluster**.
   3. Enter `my-cluster` and then choose **Delete**. Don’t continue until the cluster is deleted.

3. Delete the VPC AWS CloudFormation stack that you created.
   1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation/](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
   2. Choose the `my-eks-vpc-stack` stack, and then choose **Delete**.
   3. In the **Delete `my-eks-vpc-stack`** confirmation dialog box, choose **Delete stack**.

4. Delete the IAM roles that you created.
   1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   2. In the left navigation pane, choose **Roles**.
   3. Select each role you created from the list (**`myAmazonEKSClusterRole`**, as well as `myAmazonEKSNodeRole`). Choose **Delete**, enter the requested confirmation text, then choose **Delete**.

## Next steps

The following documentation topics help you to extend the functionality of your cluster.

- The [IAM principal](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal") that created the cluster is the only principal that can make calls to the Kubernetes API server with `kubectl` or the AWS Management Console. If you want other IAM principals to have access to your cluster, then you need to add them. For more information, see [Grant IAM users and roles access to Kubernetes APIs](grant-k8s-access.md "grant-k8s-access.md") and [Required permissions](view-kubernetes-resources.md#view-kubernetes-resources-permissions "view-kubernetes-resources.md#view-kubernetes-resources-permissions").
- Deploy a [sample application](sample-deployment.md "sample-deployment.md") to your cluster.
- Before deploying a cluster for production use, we recommend familiarizing yourself with all of the settings for [clusters](create-cluster.md "create-cluster.md") and [nodes](eks-compute.md "eks-compute.md"). Some settings (such as enabling SSH access to Amazon EC2 nodes) must be made when the cluster is created.
- To increase security for your cluster, [configure the Amazon VPC Container Networking Interface plugin to use IAM roles for service accounts](cni-iam-role.md "cni-iam-role.md").



 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an Amazon EKS cluster with hybrid nodes
<a name="hybrid-nodes-cluster-create"></a>

This topic provides an overview of the available options and describes what to consider when you create a hybrid nodes-enabled Amazon EKS cluster. EKS Hybrid Nodes have the same [Kubernetes version support](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html) as Amazon EKS clusters with cloud nodes, including standard and extended support.

If you are not planning to use EKS Hybrid Nodes, see the primary Amazon EKS create cluster documentation at [Create an Amazon EKS cluster](create-cluster.md).

## Prerequisites
<a name="hybrid-nodes-cluster-create-prep"></a>
+ The [Prerequisite setup for hybrid nodes](hybrid-nodes-prereqs.md) completed. Before you create your hybrid nodes-enabled cluster, you must have your on-premises node and optionally pod CIDRs identified, your VPC and subnets created according to the EKS requirements, and hybrid nodes requirements, and your security group with inbound rules for your on-premises and optionally pod CIDRs. For more information on these prerequisites, see [Prepare networking for hybrid nodes](hybrid-nodes-networking.md).
+ The latest version of the AWS Command Line Interface (AWS CLI) installed and configured on your device. To check your current version, use `aws --version`. Package managers such as yum, apt-get, or Homebrew for macOS are often several versions behind the latest version of the AWS CLI. To install the latest version, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [Configuring settings for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config) in the AWS Command Line Interface User Guide.
+ An [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles#iam-term-principal) with permissions to create IAM roles and attach policies, and create and describe EKS clusters

## Considerations
<a name="hybrid-nodes-cluster-create-consider"></a>
+ Your cluster must use either `API` or `API_AND_CONFIG_MAP` for the cluster authentication mode.
+ Your cluster must use IPv4 address family.
+ Your cluster must use either Public or Private cluster endpoint connectivity. Your cluster cannot use “Public and Private” cluster endpoint connectivity, because the Amazon EKS Kubernetes API server endpoint will resolve to the public IPs for hybrid nodes running outside of your VPC.
+ OIDC authentication is supported for EKS clusters with hybrid nodes.
+ You can add, change, or remove the hybrid nodes configuration of an existing cluster. For more information, see [Enable hybrid nodes on an existing Amazon EKS cluster or modify configuration](hybrid-nodes-cluster-update.md).
+ If you don’t explicitly specify a Kubernetes service IPv4 CIDR when creating a hybrid nodes-enabled cluster, Amazon EKS automatically selects a service CIDR that doesn’t overlap with your configured remote node and pod networks. The assigned CIDR may differ from the standard defaults (`10.100.0.0/16` or `172.20.0.0/16`). For example, if your remote node or pod networks overlap with these default ranges, Amazon EKS selects an alternative CIDR from the private IP ranges such as `172.16.0.0/16`. We recommend that you explicitly specify a service IPv4 CIDR during cluster creation to ensure a predictable configuration. You can find the assigned service CIDR after cluster creation by running `aws eks describe-cluster --name CLUSTER_NAME --query “cluster.kubernetesNetworkConfig.serviceIpv4Cidr”`.

## Step 1: Create cluster IAM role
<a name="hybrid-nodes-cluster-create-iam"></a>

If you already have a cluster IAM role, or you’re going to create your cluster with `eksctl` or AWS CloudFormation, then you can skip this step. By default, `eksctl` and the AWS CloudFormation template create the cluster IAM role for you.

1. Run the following command to create an IAM trust policy JSON file.

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

1. Create the Amazon EKS cluster IAM role. If necessary, preface eks-cluster-role-trust-policy.json with the path on your computer that you wrote the file to in the previous step. The command associates the trust policy that you created in the previous step to the role. To create an IAM role, the [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles#iam-term-principal) that is creating the role must be assigned the `iam:CreateRole` action (permission).

   ```
   aws iam create-role \
       --role-name myAmazonEKSClusterRole \
       --assume-role-policy-document file://"eks-cluster-role-trust-policy.json"
   ```

1. You can assign either the Amazon EKS managed policy or create your own custom policy. For the minimum permissions that you must use in your custom policy, see [Amazon EKS node IAM role](create-node-role.md). Attach the Amazon EKS managed policy named `AmazonEKSClusterPolicy` to the role. To attach an IAM policy to an [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles#iam-term-principal), the principal that is attaching the policy must be assigned one of the following IAM actions (permissions): `iam:AttachUserPolicy` or `iam:AttachRolePolicy`.

   ```
   aws iam attach-role-policy \
       --policy-arn arn:aws:iam::aws:policy/AmazonEKSClusterPolicy \
       --role-name myAmazonEKSClusterRole
   ```

## Step 2: Create hybrid nodes-enabled cluster
<a name="hybrid-nodes-cluster-create-cluster"></a>

You can create a cluster by using:
+  [eksctl](#hybrid-nodes-cluster-create-eksctl) 
+  [AWS CloudFormation](#hybrid-nodes-cluster-create-cfn) 
+  [AWS CLI](#hybrid-nodes-cluster-create-cli) 
+  [AWS Management Console](#hybrid-nodes-cluster-create-console) 

### Create hybrid nodes-enabled cluster - eksctl
<a name="hybrid-nodes-cluster-create-eksctl"></a>

You need to install the latest version of the `eksctl` command line tool. To install or update `eksctl`, see [Installation](https://eksctl.io/installation) in the `eksctl` documentation.

1. Create `cluster-config.yaml` to define a hybrid nodes-enabled Amazon EKS IPv4 cluster. Make the following replacements in your `cluster-config.yaml`. For a full list of settings, see the [eksctl documentation](https://eksctl.io/getting-started/).

   1. Replace `CLUSTER_NAME` with a name for your cluster. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphanumeric character and can’t be longer than 100 characters. The name must be unique within the AWS Region and AWS account that you’re creating the cluster in.

   1. Replace `AWS_REGION` with the AWS Region that you want to create your cluster in.

   1. Replace `K8S_VERSION` with any [Amazon EKS supported version](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html).

   1. Replace `CREDS_PROVIDER` with `ssm` or `ira` based on the credential provider you configured in the steps for [Prepare credentials for hybrid nodes](hybrid-nodes-creds.md).

   1. Replace `CA_BUNDLE_CERT` if your credential provider is set to `ira`, which uses AWS IAM Roles Anywhere as the credential provider. The CA\_BUNDLE\_CERT is the certificate authority (CA) certificate body and depends on your choice of CA. The certificate must be in Privacy Enhanced Mail (PEM) format.

   1. Replace `GATEWAY_ID` with the ID of your virtual private gateway or transit gateway to be attached to your VPC.

   1. Replace `REMOTE_NODE_CIDRS` with the on-premises node CIDR for your hybrid nodes.

   1. Replace `REMOTE_POD_CIDRS` with the on-premises pod CIDR for workloads running on hybrid nodes or remove the line from your configuration if you are not running webhooks on hybrid nodes. You must configure your `REMOTE_POD_CIDRS` if your CNI does not use Network Address Translation (NAT) or masquerading for pod IP addresses when pod traffic leaves your on-premises hosts. You must configure `REMOTE_POD_CIDRS` if you are running webhooks on hybrid nodes, see [Configure webhooks for hybrid nodes](hybrid-nodes-webhooks.md) for more information.

   1. Your on-premises node and pod CIDR blocks must meet the following requirements:

      1. Be within one of the IPv4 RFC-1918 ranges: `10.0.0.0/8`, `172.16.0.0/12`, or `192.168.0.0/16` , or within the CGNAT range defined by RFC 6598: `100.64.0.0/10`.

      1. Not overlap with each other, the `VPC CIDR` for your cluster, or your Kubernetes service IPv4 CIDR

         ```
         apiVersion: eksctl.io/v1alpha5
         kind: ClusterConfig
         
         metadata:
           name: CLUSTER_NAME
           region: AWS_REGION
           version: "K8S_VERSION"
         
         remoteNetworkConfig:
           iam:
             provider: CREDS_PROVIDER # default SSM, can also be set to IRA
             # caBundleCert: CA_BUNDLE_CERT
           vpcGatewayID: GATEWAY_ID
           remoteNodeNetworks:
           - cidrs: ["REMOTE_NODE_CIDRS"]
           remotePodNetworks:
           - cidrs: ["REMOTE_POD_CIDRS"]
         ```

1. Run the following command:

   ```
   eksctl create cluster -f cluster-config.yaml
   ```

   Cluster provisioning takes several minutes. While the cluster is being created, several lines of output appear. The last line of output is similar to the following example line.

   ```
   [✓]  EKS cluster "CLUSTER_NAME" in "REGION" region is ready
   ```

1. Continue with [Step 3: Update kubeconfig](#hybrid-nodes-cluster-create-kubeconfig).

### Create hybrid nodes-enabled cluster - AWS CloudFormation
<a name="hybrid-nodes-cluster-create-cfn"></a>

The CloudFormation stack creates the EKS cluster IAM role and an EKS cluster with the `RemoteNodeNetwork` and `RemotePodNetwork` you specify. Modify the CloudFormation template If you need to customize settings for your EKS cluster that are not exposed in the CloudFormation template.

1. Download the CloudFormation template.

   ```
   curl -OL 'https://raw.githubusercontent.com/aws/eks-hybrid/refs/heads/main/example/hybrid-eks-cfn.yaml'
   ```

1. Create a `cfn-eks-parameters.json` and specify your configuration for each value.

   1.  `CLUSTER_NAME`: name of the EKS cluster to be created

   1.  `CLUSTER_ROLE_NAME`: name of the EKS cluster IAM role to be created. The default in the template is “EKSClusterRole”.

   1.  `SUBNET1_ID`: the ID of the first subnet you created in the prerequisite steps

   1.  `SUBNET2_ID`: the ID of the second subnet you created in the prerequisite steps

   1.  `SG_ID`: the security group ID you created in the prerequisite steps

   1.  `REMOTE_NODE_CIDRS`: the on-premises node CIDR for your hybrid nodes

   1.  `REMOTE_POD_CIDRS`: the on-premises pod CIDR for workloads running on hybrid nodes. You must configure your `REMOTE_POD_CIDRS` if your CNI does not use Network Address Translation (NAT) or masquerading for pod IP addresses when pod traffic leaves your on-premises hosts. You must configure `REMOTE_POD_CIDRS` if you are running webhooks on hybrid nodes, see [Configure webhooks for hybrid nodes](hybrid-nodes-webhooks.md) for more information.

   1. Your on-premises node and pod CIDR blocks must meet the following requirements:

      1. Be within one of the IPv4 RFC-1918 ranges: `10.0.0.0/8`, `172.16.0.0/12`, or `192.168.0.0/16`, or within the CGNAT range defined by RFC 6598: `100.64.0.0/10`.

      1. Not overlap with each other, the `VPC CIDR` for your cluster, or your Kubernetes service IPv4 CIDR.

   1.  `CLUSTER_AUTH`: the cluster authentication mode for your cluster. Valid values are `API` and `API_AND_CONFIG_MAP`. The default in the template is `API_AND_CONFIG_MAP`.

   1.  `CLUSTER_ENDPOINT`: the cluster endpoint connectivity for your cluster. Valid values are “Public” and “Private”. The default in the template is Private, which means you will only be able to connect to the Kubernetes API endpoint from within your VPC.

   1.  `K8S_VERSION`: the Kubernetes version to use for your cluster. See [Amazon EKS supported versions](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html).

      ```
      {
        "Parameters": {
          "ClusterName": "CLUSTER_NAME",
          "ClusterRoleName": "CLUSTER_ROLE_NAME",
          "SubnetId1": "SUBNET1_ID",
          "SubnetId2": "SUBNET2_ID",
          "SecurityGroupId" "SG_ID",
          "RemoteNodeCIDR": "REMOTE_NODE_CIDRS",
          "RemotePodCIDR": "REMOTE_POD_CIDRS",
          "ClusterAuthMode": "CLUSTER_AUTH",
          "ClusterEndpointConnectivity": "CLUSTER_ENDPOINT",
          "K8sVersion": "K8S_VERSION"
        }
       }
      ```

1. Deploy the CloudFormation stack. Replace `STACK_NAME` with your name for the CloudFormation stack and `AWS_REGION` with your AWS Region where the cluster will be created.

   ```
   aws cloudformation deploy \
       --stack-name STACK_NAME \
       --region AWS_REGION \
       --template-file hybrid-eks-cfn.yaml \
       --parameter-overrides file://cfn-eks-parameters.json \
       --capabilities CAPABILITY_NAMED_IAM
   ```

   Cluster provisioning takes several minutes. You can check the status of your stack with the following command. Replace `STACK_NAME` with your name for the CloudFormation stack and `AWS_REGION` with your AWS Region where the cluster will be created.

   ```
   aws cloudformation describe-stacks \
       --stack-name STACK_NAME \
       --region AWS_REGION \
       --query 'Stacks[].StackStatus'
   ```

1. Continue with [Step 3: Update kubeconfig](#hybrid-nodes-cluster-create-kubeconfig).

### Create hybrid nodes-enabled cluster - AWS CLI
<a name="hybrid-nodes-cluster-create-cli"></a>

1. Run the following command to create a hybrid nodes-enabled EKS cluster. Before running the command, replace the following with your settings. For a full list of settings, see the [Create an Amazon EKS cluster](create-cluster.md) documentation.

   1.  `CLUSTER_NAME`: name of the EKS cluster to be created

   1.  `AWS_REGION`: AWS Region where the cluster will be created.

   1.  `K8S_VERSION`: the Kubernetes version to use for your cluster. See Amazon EKS supported versions.

   1.  `ROLE_ARN`: the Amazon EKS cluster role you configured for your cluster. See Amazon EKS cluster IAM role for more information.

   1.  `SUBNET1_ID`: the ID of the first subnet you created in the prerequisite steps

   1.  `SUBNET2_ID`: the ID of the second subnet you created in the prerequisite steps

   1.  `SG_ID`: the security group ID you created in the prerequisite steps

   1. You can use `API` and `API_AND_CONFIG_MAP` for your cluster access authentication mode. In the command below, the cluster access authentication mode is set to `API_AND_CONFIG_MAP`.

   1. You can use the `endpointPublicAccess` and `endpointPrivateAccess` parameters to enable or disable public and private access to your cluster’s Kubernetes API server endpoint. In the command below `endpointPublicAccess` is set to false and `endpointPrivateAccess` is set to true.

   1.  `REMOTE_NODE_CIDRS`: the on-premises node CIDR for your hybrid nodes.

   1.  `REMOTE_POD_CIDRS` (optional): the on-premises pod CIDR for workloads running on hybrid nodes.

   1. Your on-premises node and pod CIDR blocks must meet the following requirements:

      1. Be within one of the IPv4 RFC-1918 ranges: `10.0.0.0/8`, `172.16.0.0/12`, or `192.168.0.0/16`, or within the CGNAT range defined by RFC 6598: `100.64.0.0/10`.

      1. Not overlap with each other, the `VPC CIDR` for your Amazon EKS cluster, or your Kubernetes service IPv4 CIDR.

         ```
         aws eks create-cluster \
             --name CLUSTER_NAME \
             --region AWS_REGION \
             --kubernetes-version K8S_VERSION \
             --role-arn ROLE_ARN \
             --resources-vpc-config subnetIds=SUBNET1_ID,SUBNET2_ID,securityGroupIds=SG_ID,endpointPrivateAccess=true,endpointPublicAccess=false \
             --access-config authenticationMode=API_AND_CONFIG_MAP \
             --remote-network-config '{"remoteNodeNetworks":[{"cidrs":["REMOTE_NODE_CIDRS"]}],"remotePodNetworks":[{"cidrs":["REMOTE_POD_CIDRS"]}]}'
         ```

1. It takes several minutes to provision the cluster. You can query the status of your cluster with the following command. Replace `CLUSTER_NAME` with the name of the cluster you are creating and `AWS_REGION` with the AWS Region where the cluster is creating. Don’t proceed to the next step until the output returned is `ACTIVE`.

   ```
   aws eks describe-cluster \
       --name CLUSTER_NAME \
       --region AWS_REGION \
       --query "cluster.status"
   ```

1. Continue with [Step 3: Update kubeconfig](#hybrid-nodes-cluster-create-kubeconfig).

### Create hybrid nodes-enabled cluster - AWS Management Console
<a name="hybrid-nodes-cluster-create-console"></a>

1. Open the Amazon EKS console at [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. Choose Add cluster and then choose Create.

1. On the Configure cluster page, enter the following fields:

   1.  **Name** – A name for your cluster. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphanumeric character and can’t be longer than 100 characters. The name must be unique within the AWS Region and AWS account that you’re creating the cluster in.

   1.  **Cluster IAM role** – Choose the Amazon EKS cluster IAM role that you created to allow the Kubernetes control plane to manage AWS resources on your behalf.

   1.  **Kubernetes version** – The version of Kubernetes to use for your cluster. We recommend selecting the latest version, unless you need an earlier version.

   1.  **Upgrade policy** - Choose either Extended or Standard.

      1.  **Extended:** This option supports the Kubernetes version for 26 months after the release date. The extended support period has an additional hourly cost that begins after the standard support period ends. When extended support ends, your cluster will be auto upgraded to the next version.

      1.  **Standard:** This option supports the Kubernetes version for 14 months after the release date. There is no additional cost. When standard support ends, your cluster will be auto upgraded to the next version.

   1.  **Cluster access** - choose to allow or disallow cluster administrator access and select an authentication mode. The following authentication modes are supported for hybrid nodes-enabled clusters.

      1.  **EKS API**: The cluster will source authenticated IAM principals only from EKS access entry APIs.

      1.  **EKS API and ConfigMap**: The cluster will source authenticated IAM principals from both EKS access entry APIs and the `aws-auth` ConfigMap.

   1.  **Secrets encryption** – (Optional) Choose to enable secrets encryption of Kubernetes secrets using a KMS key. You can also enable this after you create your cluster. Before you enable this capability, make sure that you’re familiar with the information in [Encrypt Kubernetes secrets with KMS on existing clusters](enable-kms.md).

   1.  **ARC zonal shift** - If enabled, EKS will register your cluster with ARC zonal shift to enable you to use zonal shift to shift application traffic away from an AZ.

   1.  **Tags** – (Optional) Add any tags to your cluster. For more information, see [Organize Amazon EKS resources with tags](eks-using-tags.md).

   1. When you’re done with this page, choose **Next**.

1. On the **Specify networking** page, select values for the following fields:

   1.  **VPC** – Choose an existing VPC that meets [View Amazon EKS networking requirements for VPC and subnets](network-reqs.md) and [Amazon EKS Hybrid Nodes requirements](hybrid-nodes-prereqs.md). Before choosing a VPC, we recommend that you’re familiar with all of the requirements and considerations in View Amazon EKS networking requirements for VPC, subnets, and hybrid nodes. You can’t change which VPC you want to use after cluster creation. If no VPCs are listed, then you need to create one first. For more information, see [Create an Amazon VPC for your Amazon EKS cluster](creating-a-vpc.md) and the [Amazon EKS Hybrid Nodes networking requirements](hybrid-nodes-prereqs.md).

   1.  **Subnets** – By default, all available subnets in the VPC specified in the previous field are preselected. You must select at least two.

   1.  **Security groups** – (Optional) Specify one or more security groups that you want Amazon EKS to associate to the network interfaces that it creates. At least one of the security groups you specify must have inbound rules for your on-premises node and optionally pod CIDRs. See the [Amazon EKS Hybrid Nodes networking requirements](hybrid-nodes-networking.md) for more information. Whether you choose any security groups or not, Amazon EKS creates a security group that enables communication between your cluster and your VPC. Amazon EKS associates this security group, and any that you choose, to the network interfaces that it creates. For more information about the cluster security group that Amazon EKS creates, see [View Amazon EKS security group requirements for clusters](sec-group-reqs.md) You can modify the rules in the cluster security group that Amazon EKS creates.

   1.  **Choose cluster IP address family** – You must choose IPv4 for hybrid nodes-enabled clusters.

   1. (Optional) Choose **Configure Kubernetes Service IP address range** and specify a **Service IPv4 range**. We recommend specifying an explicit service CIDR for hybrid nodes-enabled clusters. If you don’t specify one, Amazon EKS selects a CIDR that avoids conflicts with your remote node and pod networks, which may differ from the standard defaults (`10.100.0.0/16` or `172.20.0.0/16`).

   1.  **Choose Configure remote networks to enable hybrid nodes** and specify your on-premises node and pod CIDRs for hybrid nodes.

   1. You must configure your remote pod CIDR if your CNI does not use Network Address Translation (NAT) or masquerading for pod IP addresses when pod traffic leaves your on-premises hosts. You must configure the remote pod CIDR if you are running webhooks on hybrid nodes.

   1. Your on-premises node and pod CIDR blocks must meet the following requirements:

      1. Be within one of the IPv4 RFC-1918 ranges: `10.0.0.0/8`, `172.16.0.0/12`, or `192.168.0.0/16`, or within the CGNAT range defined by RFC 6598: `100.64.0.0/10`.

      1. Not overlap with each other, the `VPC CIDR` for your cluster, or your Kubernetes service IPv4 CIDR

   1. For **Cluster endpoint access**, select an option. After your cluster is created, you can change this option. For hybrid nodes-enabled clusters, you must choose either Public or Private. Before selecting a non-default option, make sure to familiarize yourself with the options and their implications. For more information, see [Cluster API server endpoint](cluster-endpoint.md).

   1. When you’re done with this page, choose **Next**.

1. (Optional) On the **Configure** observability page, choose which Metrics and Control plane logging options to turn on. By default, each log type is turned off.

   1. For more information about the Prometheus metrics option, see [Monitor your cluster metrics with Prometheus](prometheus.md).

   1. For more information about the EKS control logging options, see [Send control plane logs to CloudWatch Logs](control-plane-logs.md).

   1. When you’re done with this page, choose **Next**.

1. On the **Select add-ons** page, choose the add-ons that you want to add to your cluster.

   1. You can choose as many **Amazon EKS add-ons** and ** AWS Marketplace add-ons** as you require. Amazon EKS add-ons that are not compatible with hybrid nodes are marked with “Not compatible with Hybrid Nodes” and the add-ons have an anti-affinity rule to prevent them from running on hybrid nodes. See Configuring add-ons for hybrid nodes for more information. If the ** AWS Marketplace** add-ons that you want to install isn’t listed, you can search for available ** AWS Marketplace add-ons** by entering text in the search box. You can also search by **category**, **vendor**, or **pricing model** and then choose the add-ons from the search results.

   1. Some add-ons, such as CoreDNS and kube-proxy, are installed by default. If you disable any of the default add-ons, this may affect your ability to run Kubernetes applications.

   1. When you’re done with this page, choose `Next`.

1. On the **Configure selected add-ons settings** page, select the version that you want to install.

   1. You can always update to a later version after cluster creation. You can update the configuration of each add-on after cluster creation. For more information about configuring add-ons, see [Update an Amazon EKS add-on](updating-an-add-on.md). For the add-ons versions that are compatible with hybrid nodes, see [Configure add-ons for hybrid nodes](hybrid-nodes-add-ons.md).

   1. When you’re done with this page, choose Next.

1. On the **Review and create** page, review the information that you entered or selected on the previous pages. If you need to make changes, choose **Edit**. When you’re satisfied, choose **Create**. The **Status** field shows **CREATING** while the cluster is provisioned. Cluster provisioning takes several minutes.

1. Continue with [Step 3: Update kubeconfig](#hybrid-nodes-cluster-create-kubeconfig).

## Step 3: Update kubeconfig
<a name="hybrid-nodes-cluster-create-kubeconfig"></a>

If you created your cluster using `eksctl`, then you can skip this step. This is because `eksctl` already completed this step for you. Enable `kubectl` to communicate with your cluster by adding a new context to the `kubectl` config file. For more information about how to create and update the file, see [Connect kubectl to an EKS cluster by creating a kubeconfig file](create-kubeconfig.md).

```
aws eks update-kubeconfig --name CLUSTER_NAME --region AWS_REGION
```

An example output is as follows.

```
Added new context arn:aws:eks:AWS_REGION:111122223333:cluster/CLUSTER_NAME to /home/username/.kube/config
```

Confirm communication with your cluster by running the following command.

```
kubectl get svc
```

An example output is as follows.

```
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.100.0.1   <none>        443/TCP   28h
```

## Step 4: Cluster setup
<a name="_step_4_cluster_setup"></a>

As a next step, see [Prepare cluster access for hybrid nodes](hybrid-nodes-cluster-prep.md) to enable access for your hybrid nodes to join your cluster.
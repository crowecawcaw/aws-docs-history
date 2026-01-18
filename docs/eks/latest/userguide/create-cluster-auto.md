**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an Amazon EKS Auto Mode cluster

This topic provides detailed instructions for creating an Amazon EKS Auto Mode cluster using advanced configuration options. It covers prerequisites, networking options, and add-on configurations. The process includes setting up IAM roles, configuring cluster settings, specifying networking parameters, and selecting add-ons. Users can create clusters using either the AWS Management Console or the AWS CLI, with step-by-step guidance provided for both methods.

For users seeking a less complex setup process, refer to the following for simplified cluster creation steps:

- [Create an EKS Auto Mode Cluster with the eksctl CLI](automode-get-started-eksctl.md "automode-get-started-eksctl.md")
- [Create an EKS Auto Mode Cluster with the AWS CLI](automode-get-started-cli.md "automode-get-started-cli.md")
- [Create an EKS Auto Mode Cluster with the AWS Management Console](automode-get-started-console.md "automode-get-started-console.md")
  This advanced configuration guide is intended for users who require more granular control over their EKS Auto Mode cluster setup and are familiar with Amazon EKS concepts and requirements. Before proceeding with the advanced configuration, ensure you have met all prerequisites and have a thorough understanding of the networking and IAM requirements for EKS Auto Mode clusters.

EKS Auto Mode requires additional IAM permissions. For more information, see:

- [IAM Roles for EKS Auto Mode Clusters](automode-get-started-cli.md#auto-mode-create-roles "automode-get-started-cli.md#auto-mode-create-roles")
- [Learn about identity and access in EKS Auto Mode](auto-learn-iam.md "auto-learn-iam.md")

###### Note

If you want to create a cluster without EKS Auto Mode, see [Create an Amazon EKS cluster](create-cluster.md "create-cluster.md").

This topic covers advanced configuration. If you are looking to get started with EKS Auto Mode, see [Create a cluster with Amazon EKS Auto Mode](create-auto.md "create-auto.md").

## Prerequisites

- An existing VPC and subnets that meet [Amazon EKS requirements](network-reqs.md "network-reqs.md"). Before you deploy a cluster for production use, we recommend that you have a thorough understanding of the VPC and subnet requirements. If you don’t have a VPC and subnets, you can create them using an [Amazon EKS provided AWS CloudFormation template](creating-a-vpc.md "creating-a-vpc.md").
- The `kubectl` command line tool is installed on your device or AWS CloudShell. The version can be the same as or up to one minor version earlier or later than the Kubernetes version of your cluster. For example, if your cluster version is `1.29`, you can use `kubectl` version `1.28`, `1.29`, or `1.30` with it. To install or upgrade `kubectl`, see [Set up kubectl and eksctl](install-kubectl.md "install-kubectl.md").
- Version `2.12.3` or later or version `1.27.160` or later of the AWS Command Line Interface (AWS CLI) installed and configured on your device or AWS CloudShell. To check your current version, use `aws --version`. To install the latest version, see [Installing](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") and [Quick configuration with aws configure](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config") in the _AWS Command Line Interface User Guide_.
- An [IAM principal](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal") with permissions to create and modify EKS and IAM resources.

## Create cluster - AWS console

1.  Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2.  Choose **Add cluster** and then choose **Create**.
3.  Under _Configuration options_, select **Custom configuration**.
    - This topic covers custom configuration. For information about Quick configuration, see [Create an EKS Auto Mode Cluster with the AWS Management Console](automode-get-started-console.md "automode-get-started-console.md").

4.  Confirm **Use EKS Auto Mode** is enabled.
    - This topic covers creating clusters with EKS Auto Mode. For more information about creating clusters without EKS Auto Mode, see [Create an Amazon EKS cluster](create-cluster.md "create-cluster.md").

5.  On the **Configure cluster** page, enter the following fields:
    - **Name** – A name for your cluster. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphanumeric character and can’t be longer than 100 characters. The name must be unique within the AWS Region and AWS account that you’re creating the cluster in.
    - **Cluster IAM role** – Choose the Amazon EKS cluster IAM role that you created to allow the Kubernetes control plane to manage AWS resources on your behalf. If you haven’t previously created a Cluster IAM role for EKS Auto Mode, select the **Create recommended role** button to create the role with the required permissions in the IAM console.
    - **Kubernetes version** – The version of Kubernetes to use for your cluster. We recommend selecting the latest version, unless you need an earlier version.
    - **Upgrade policy** — The Kubernetes version policy you would like to set for your cluster. If you want your cluster to only run on a standard support version, you can choose **Standard**. If you want your cluster to enter extended support at the end of standard support for a version, you can choose **Extended**. If you select a Kubernetes version that is currently in extended support, you can not select standard support as an option.

6.  In the **Auto Mode Compute** section of the configure cluster page, enter the following fields:
    - **Node pools** — Determine if you want to use the build in node pools. For more information, see [Enable or Disable Built-in NodePools](set-builtin-node-pools.md "set-builtin-node-pools.md").
    - **Node IAM role** — If you enable any of the built-in node pools, you need to select a Node IAM Role. EKS Auto Mode will assign this role to new nodes. You cannot change this value after the cluster is created. If you haven’t previously created a Node IAM role for EKS Auto Mode, select the Create recommended role button to create the role with the required permissions. For more information about this role, see [Learn about identity and access in EKS Auto Mode](auto-learn-iam.md "auto-learn-iam.md").

7.  In the **Cluster access** section of the configure cluster page, enter the following fields:
    - **Bootstrap cluster administrator access** — The cluster creator is automatically a Kubernetes administrator. If you want to disable this, select **Disallow cluster administrator access**.
    - **Cluster authentication mode** — EKS Auto Mode requires EKS access entries, the EKS API authentication mode. You can optionally enable the `ConfigMap` authentication mode by selecting **EKS API and ConfigMap**.

8.  Enter the remaining fields on the configure cluster page:
    - **Secrets encryption** – (Optional) Choose to enable secrets encryption of Kubernetes secrets using a KMS key. You can also enable this after you create your cluster. Before you enable this capability, make sure that you’re familiar with the information in [Encrypt Kubernetes secrets with KMS on existing clusters](enable-kms.md "enable-kms.md").
    - **ARC Zonal shift** — EKS Auto Mode does not support Arc Zonal shift.
    - **Tags** – (Optional) Add any tags to your cluster. For more information, see [Organize Amazon EKS resources with tags](eks-using-tags.md "eks-using-tags.md").

    When you’re done with this page, choose **Next**.

9.  On the **Specify networking** page, select values for the following fields:

        * **VPC** – Choose an existing VPC that meets [Amazon EKS VPC requirements](network-reqs.md#network-requirements-vpc "network-reqs.md#network-requirements-vpc") to create your cluster in. Before choosing a VPC, we recommend that you’re familiar with all of the requirements and considerations in [View Amazon EKS networking requirements for VPC and subnets](network-reqs.md "network-reqs.md"). You can’t change which VPC you want to use after cluster creation. If no VPCs are listed, then you need to create one first. For more information, see [Create an Amazon VPC for your Amazon EKS cluster](creating-a-vpc.md "creating-a-vpc.md").
        * **Subnets** – By default, all available subnets in the VPC specified in the previous field are preselected. You must select at least two.


        The subnets that you choose must meet the [Amazon EKS subnet requirements](network-reqs.md#network-requirements-subnets "network-reqs.md#network-requirements-subnets"). Before selecting subnets, we recommend that you’re familiar with all of the [Amazon EKS VPC and subnet requirements and considerations](network-reqs.md "network-reqs.md").



        **Security groups** – (Optional) Specify one or more security groups that you want Amazon EKS to associate to the network interfaces that it creates.


        Whether you choose any security groups or not, Amazon EKS creates a security group that enables communication between your cluster and your VPC. Amazon EKS associates this security group, and any that you choose, to the network interfaces that it creates. For more information about the cluster security group that Amazon EKS creates, see [View Amazon EKS security group requirements for clusters](sec-group-reqs.md "sec-group-reqs.md"). You can modify the rules in the cluster security group that Amazon EKS creates.
        * **Choose cluster IP address family** – You can choose either **IPv4** and **IPv6**.


        Kubernetes assigns `IPv4` addresses to Pods and services, by default. Before deciding to use the `IPv6` family, make sure that you’re familiar with all of the considerations and requirements in the [VPC requirements and considerations](network-reqs.md#network-requirements-vpc "network-reqs.md#network-requirements-vpc"), [Subnet requirements and considerations](network-reqs.md#network-requirements-subnets "network-reqs.md#network-requirements-subnets"), [View Amazon EKS security group requirements for clusters](sec-group-reqs.md "sec-group-reqs.md"), and [Learn about IPv6 addresses to clusters, Pods, and services](cni-ipv6.md "cni-ipv6.md") topics. If you choose the `IPv6` family, you can’t specify an address range for Kubernetes to assign `IPv6` service addresses from like you can for the `IPv4` family. Kubernetes assigns service addresses from the unique local address range (`fc00::/7`).
        * (Optional) Choose **Configure Kubernetes Service IP address range** and specify a **Service `IPv4` range**.


        Specifying your own range can help prevent conflicts between Kubernetes services and other networks peered or connected to your VPC. Enter a range in CIDR notation. For example: `10.2.0.0/16`.


        The CIDR block must meet the following requirements:




        	+ Be within one of the following ranges: `10.0.0.0/8`, `172.16.0.0/12`, or `192.168.0.0/16`.
        	+ Have a minimum size of `/24` and a maximum size of `/12`.
        	+ Not overlap with the range of the VPC for your Amazon EKS resources.

    You can only specify this option when using the `IPv4` address family and only at cluster creation. If you don’t specify this, then Kubernetes assigns service IP addresses from either the `10.100.0.0/16` or `172.20.0.0/16` CIDR blocks.

        * For **Cluster endpoint access**, select an option. After your cluster is created, you can change this option. Before selecting a non-default option, make sure to familiarize yourself with the options and their implications. For more information, see [Cluster API server endpoint](cluster-endpoint.md "cluster-endpoint.md").


        When you’re done with this page, choose **Next**.

10. (Optional) On the **Configure observability** page, choose which **Metrics** and **Control plane logging** options to turn on. By default, each log type is turned off.
    - For more information about the Prometheus metrics option, see [Step 1: Turn on Prometheus metrics](prometheus.md#turn-on-prometheus-metrics "prometheus.md#turn-on-prometheus-metrics").
    - For more information about the **Control plane logging** options, see [Send control plane logs to CloudWatch Logs](control-plane-logs.md "control-plane-logs.md").
    - When you’re done with this page, choose **Next**.

11. On the **Select add-ons** page, choose the add-ons that you want to add to your cluster. You can choose as many **Amazon EKS add-ons** and **AWS Marketplace add-ons** as you require. If the **AWS Marketplace add-ons** that you want to install isn’t listed, you can click the page numbering to view additional page results or search for available **AWS Marketplace add-ons** by entering text in the search box. You can also filter by **category**, **vendor**, or **pricing model** and then choose the add-ons from the search results. When creating a cluster, you can view, select, and install any add-on that supports EKS Pod Identities as detailed in [Learn how EKS Pod Identity grants pods access to AWS services](pod-identities.md "pod-identities.md").
    - EKS Auto Mode automates the functionality of certain add-ons. If you plan to deploy EKS Managed Node Groups to your EKS Auto Mode Cluster, select **Additional Amazon EKS Add-ons** and review the options. You may need to install add-ons such as CoreDNS and kube-proxy. EKS will only install the add-ons in this section on self-managed nodes and node groups.
    - When you’re done with this page, choose **Next**.

12. On the **Configure selected add-ons settings** page, select the version that you want to install. You can always update to a later version after cluster creation.

For add-ons that support EKS Pod Identities, you can use the console to automatically generate the role with the name, AWS managed policy, and trust policy prepopulated specifically for the add-on. You can re-use existing roles or create new roles for supported add-ons. For the steps to use the console to create roles for add-ons that support EKS Pod Identities, see [Create add-on (AWS Console)](creating-an-add-on.md#create_add_on_console "creating-an-add-on.md#create_add_on_console"). If an add-on does not support EKS Pod Identity, a message displays with instructions to use the wizard to create the IAM roles for service accounts (IRSA) after the cluster is created.

You can update the configuration of each add-on after cluster creation. For more information about configuring add-ons, see [Update an Amazon EKS add-on](updating-an-add-on.md "updating-an-add-on.md"). When you’re done with this page, choose **Next**. 13. On the **Review and create** page, review the information that you entered or selected on the previous pages. If you need to make changes, choose **Edit**. When you’re satisfied, choose **Create**. The **Status** field shows **CREATING** while the cluster is provisioned.

###### Note

You might receive an error that one of the Availability Zones in your request doesn’t have sufficient capacity to create an Amazon EKS cluster. If this happens, the error output contains the Availability Zones that can support a new cluster. Retry creating your cluster with at least two subnets that are located in the supported Availability Zones for your account. For more information, see [Insufficient capacity](troubleshooting.md#ice "troubleshooting.md#ice").

Cluster provisioning takes several minutes.

## Create cluster - AWS CLI

The following CLI instructions cover creating IAM resources and creating the cluster.

### Create an EKS Auto Mode Cluster IAM Role

#### Step 1: Create the Trust Policy

Create a trust policy that allows the Amazon EKS service to assume the role. Save the policy as `trust-policy.json`:

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

#### Step 2: Create the IAM Role

Use the trust policy to create the Cluster IAM Role:

```
aws iam create-role \
    --role-name AmazonEKSAutoClusterRole \
    --assume-role-policy-document file://trust-policy.json
```

#### Step 3: Note the Role ARN

Retrieve and save the ARN of the new role for use in subsequent steps:

```
aws iam get-role --role-name AmazonEKSAutoClusterRole --query "Role.Arn" --output text
```

#### Step 4: Attach Required Policies

Attach the following AWS managed policies to the Cluster IAM Role to grant the necessary permissions:

**AmazonEKSClusterPolicy**:

```
 aws iam attach-role-policy \
    --role-name AmazonEKSAutoClusterRole \
    --policy-arn <shared id="region.arn"/>iam::aws:policy/AmazonEKSClusterPolicy
```

**AmazonEKSComputePolicy**:

```
 aws iam attach-role-policy \
    --role-name AmazonEKSAutoClusterRole \
    --policy-arn <shared id="region.arn"/>iam::aws:policy/AmazonEKSComputePolicy
```

**AmazonEKSBlockStoragePolicy**:

```
 aws iam attach-role-policy \
    --role-name AmazonEKSAutoClusterRole \
    --policy-arn <shared id="region.arn"/>iam::aws:policy/AmazonEKSBlockStoragePolicy
```

**AmazonEKSLoadBalancingPolicy**:

```
 aws iam attach-role-policy \
    --role-name AmazonEKSAutoClusterRole \
    --policy-arn <shared id="region.arn"/>iam::aws:policy/AmazonEKSLoadBalancingPolicy
```

**AmazonEKSNetworkingPolicy**:

```
 aws iam attach-role-policy \
    --role-name AmazonEKSAutoClusterRole \
    --policy-arn <shared id="region.arn"/>iam::aws:policy/AmazonEKSNetworkingPolicy
```

### Create an EKS Auto Mode Node IAM Role

#### Step 1: Create the Trust Policy

Create a trust policy that allows the Amazon EKS service to assume the role. Save the policy as `node-trust-policy.json`:

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

#### Step 2: Create the Node IAM Role

Use the **node-trust-policy.json** file from the previous step to define which entities can assume the role. Run the following command to create the Node IAM Role:

```
aws iam create-role \
    --role-name AmazonEKSAutoNodeRole \
    --assume-role-policy-document file://node-trust-policy.json
```

#### Step 3: Note the Role ARN

After creating the role, retrieve and save the ARN of the Node IAM Role. You will need this ARN in subsequent steps. Use the following command to get the ARN:

```
aws iam get-role --role-name AmazonEKSAutoNodeRole --query "Role.Arn" --output text
```

#### Step 4: Attach Required Policies

Attach the following AWS managed policies to the Node IAM Role to provide the necessary permissions:

**AmazonEKSWorkerNodeMinimalPolicy**:

```
 aws iam attach-role-policy \
    --role-name AmazonEKSAutoNodeRole \
    --policy-arn <shared id="region.arn"/>iam::aws:policy/AmazonEKSWorkerNodeMinimalPolicy
```

**AmazonEC2ContainerRegistryPullOnly**:

```
 aws iam attach-role-policy \
    --role-name AmazonEKSAutoNodeRole \
    --policy-arn <shared id="region.arn"/>iam::aws:policy/AmazonEC2ContainerRegistryPullOnly
```

### Create cluster

1.  Create your cluster with the command that follows. Before running the command, make the following replacements:
    - Replace `region-code` with the AWS Region that you want to create your cluster in.
    - Replace `my-cluster` with a name for your cluster. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphanumeric character and can’t be longer than 100 characters. The name must be unique within the AWS Region and AWS account that you’re creating the cluster in.
    - Replace `1.30` with any [Amazon EKS supported version](kubernetes-versions.md "kubernetes-versions.md").
    - Replace `111122223333` with your account ID
    - If you have created differently named IAM Roles for the Cluster and Node roles, replace the ARNs.
    - Replace the values for `subnetIds` with your own. You can also add additional IDs. You must specify at least two subnet IDs.

    The subnets that you choose must meet the [Amazon EKS subnet requirements](network-reqs.md#network-requirements-subnets "network-reqs.md#network-requirements-subnets"). Before selecting subnets, we recommend that you’re familiar with all of the [Amazon EKS VPC and subnet requirements and considerations](network-reqs.md "network-reqs.md").
    - If you don’t want to specify a security group ID, remove `,securityGroupIds=sg-<ExampleID1>` from the command. If you want to specify one or more security group IDs, replace the values for `securityGroupIds` with your own. You can also add additional IDs.

    Whether you choose any security groups or not, Amazon EKS creates a security group that enables communication between your cluster and your VPC. Amazon EKS associates this security group, and any that you choose, to the network interfaces that it creates. For more information about the cluster security group that Amazon EKS creates, see [View Amazon EKS security group requirements for clusters](sec-group-reqs.md "sec-group-reqs.md"). You can modify the rules in the cluster security group that Amazon EKS creates.

    ```
     aws eks create-cluster \
      --region region-code \
      --name my-cluster \
      --kubernetes-version 1.30 \
      --role-arn <shared id="region.arn"/>iam::111122223333:role/AmazonEKSAutoClusterRole \
      --resources-vpc-config '{"subnetIds": ["subnet-ExampleID1","subnet-ExampleID2"], "securityGroupIds": ["sg-ExampleID1"], "endpointPublicAccess": true, "endpointPrivateAccess": true}' \
      --compute-config '{"enabled": true, "nodeRoleArn": "<shared id="region.arn"/>iam::111122223333:role/AmazonEKSAutoNodeRole", "nodePools": ["general-purpose", "system"]}' \
      --kubernetes-network-config '{"elasticLoadBalancing": {"enabled": true}}' \
      --storage-config '{"blockStorage": {"enabled": true}}' \
      --access-config '{"authenticationMode": "API"}'
    ```

    ###### Note

    You might receive an error that one of the Availability Zones in your request doesn’t have sufficient capacity to create an Amazon EKS cluster. If this happens, the error output contains the Availability Zones that can support a new cluster. Retry creating your cluster with at least two subnets that are located in the supported Availability Zones for your account. For more information, see [Insufficient capacity](troubleshooting.md#ice "troubleshooting.md#ice").

    The following are optional settings that, if required, must be added to the previous command. You can only enable these options when you create the cluster, not after.
    - If you want to specify which `IPv4` Classless Inter-domain Routing (CIDR) block Kubernetes assigns service IP addresses from, you must specify it by adding the `--kubernetes-network-config serviceIpv4Cidr=<cidr-block>` to the following command.

    Specifying your own range can help prevent conflicts between Kubernetes services and other networks peered or connected to your VPC. Enter a range in CIDR notation. For example: `10.2.0.0/16`.

    The CIDR block must meet the following requirements:

        + Be within one of the following ranges: `10.0.0.0/8`, `172.16.0.0/12`, or `192.168.0.0/16`.
        + Have a minimum size of `/24` and a maximum size of `/12`.
        + Not overlap with the range of the VPC for your Amazon EKS resources.


        You can only specify this option when using the `IPv4` address family and only at cluster creation. If you don’t specify this, then Kubernetes assigns service IP addresses from either the `10.100.0.0/16` or `172.20.0.0/16` CIDR blocks.

    - If you’re creating a cluster and want the cluster to assign `IPv6` addresses to Pods and services instead of `IPv4` addresses, add `--kubernetes-network-config ipFamily=ipv6` to the following command.

    Kubernetes assigns `IPv4` addresses to Pods and services, by default. Before deciding to use the `IPv6` family, make sure that you’re familiar with all of the considerations and requirements in the [VPC requirements and considerations](network-reqs.md#network-requirements-vpc "network-reqs.md#network-requirements-vpc"), [Subnet requirements and considerations](network-reqs.md#network-requirements-subnets "network-reqs.md#network-requirements-subnets"), [View Amazon EKS security group requirements for clusters](sec-group-reqs.md "sec-group-reqs.md"), and [Learn about IPv6 addresses to clusters, Pods, and services](cni-ipv6.md "cni-ipv6.md") topics. If you choose the `IPv6` family, you can’t specify an address range for Kubernetes to assign `IPv6` service addresses from like you can for the `IPv4` family. Kubernetes assigns service addresses from the unique local address range (`fc00::/7`).

2.  It takes several minutes to provision the cluster. You can query the status of your cluster with the following command.

```
 aws eks describe-cluster --region region-code --name my-cluster --query "cluster.status"
```

## Next steps

- [Connect kubectl to an EKS cluster by creating a kubeconfig file](create-kubeconfig.md "create-kubeconfig.md")
- [Grant IAM users access to Kubernetes with EKS access entries](access-entries.md "access-entries.md")
- [Enable secrets encryption for your cluster](enable-kms.md "enable-kms.md").
- [Configure logging for your cluster](control-plane-logs.md "control-plane-logs.md").
- [Add nodes to your cluster](eks-compute.md "eks-compute.md").

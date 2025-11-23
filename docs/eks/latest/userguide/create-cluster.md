**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an Amazon EKS cluster

###### Note

This topic covers creating Amazon EKS clusters without EKS Auto Mode.

For detailed instructions on creating an EKS Auto Mode cluster, see [Create an Amazon EKS Auto Mode cluster](create-cluster-auto.md "create-cluster-auto.md").

To get started with EKS Auto Mode, see [Get started with Amazon EKS – EKS Auto Mode](getting-started-automode.md "getting-started-automode.md").

This topic provides an overview of the available options and describes what to consider when you create an Amazon EKS cluster. If you need to create a cluster with your on-premises infrastructure as the compute for nodes, see [Create an Amazon EKS cluster with hybrid nodes](hybrid-nodes-cluster-create.md "hybrid-nodes-cluster-create.md"). If this is your first time creating an Amazon EKS cluster, we recommend that you follow one of our guides in [Get started with Amazon EKS](getting-started.md "getting-started.md"). These guides help you to create a simple, default cluster without expanding into all of the available options.

## Prerequisites

- An existing VPC and subnets that meet [Amazon EKS requirements](network-reqs.md "network-reqs.md"). Before you deploy a cluster for production use, we recommend that you have a thorough understanding of the VPC and subnet requirements. If you don’t have a VPC and subnets, you can create them using an [Amazon EKS provided AWS CloudFormation template](creating-a-vpc.md "creating-a-vpc.md").
- The `kubectl` command line tool is installed on your device or AWS CloudShell. The version can be the same as or up to one minor version earlier or later than the Kubernetes version of your cluster. To install or upgrade `kubectl`, see [Set up kubectl and eksctl](install-kubectl.md "install-kubectl.md").
- Version `2.12.3` or later or version `1.27.160` or later of the AWS Command Line Interface (AWS CLI) installed and configured on your device or AWS CloudShell. To check your current version, use `aws --version | cut -d / -f2 | cut -d ' ' -f1`. Package managers such `yum`, `apt-get`, or Homebrew for macOS are often several versions behind the latest version of the AWS CLI. To install the latest version, see [Installing](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") and [Quick configuration with aws configure](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config") in the _AWS Command Line Interface User Guide_. The AWS CLI version that is installed in AWS CloudShell might also be several versions behind the latest version. To update it, see [Installing AWS CLI to your home directory](../../../cloudshell/latest/userguide/vm-specs.md#install-cli-software "../../../cloudshell/latest/userguide/vm-specs.md#install-cli-software") in the _AWS CloudShell User Guide_.
- An [IAM principal](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal") with permissions to `create` and `describe` an Amazon EKS cluster. For more information, see [Create a local Kubernetes cluster on an Outpost](security-iam-id-based-policy-examples.md#policy-create-local-cluster "security-iam-id-based-policy-examples.md#policy-create-local-cluster") and [List or describe all clusters](security-iam-id-based-policy-examples.md#policy-example2 "security-iam-id-based-policy-examples.md#policy-example2").

## Step 1: Create cluster IAM role

1. If you already have a cluster IAM role, or you’re going to create your cluster with `eksctl`, then you can skip this step. By default, `eksctl` creates a role for you.
2. Run the following command to create an IAM trust policy JSON file.

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

3. Create the Amazon EKS cluster IAM role. If necessary, preface `eks-cluster-role-trust-policy.json` with the path on your computer that you wrote the file to in the previous step. The command associates the trust policy that you created in the previous step to the role. To create an IAM role, the [IAM principal](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal") that is creating the role must be assigned the `iam:CreateRole` action (permission).

```
aws iam create-role --role-name myAmazonEKSClusterRole --assume-role-policy-document file://"eks-cluster-role-trust-policy.json"
```

4. You can assign either the Amazon EKS managed policy or create your own custom policy. For the minimum permissions that you must use in your custom policy, see [Amazon EKS cluster IAM role](cluster-iam-role.md "cluster-iam-role.md").

Attach the Amazon EKS managed policy named [AmazonEKSClusterPolicy](../../../aws-managed-policy/latest/reference/AmazonEKSClusterPolicy.md#AmazonEKSClusterPolicy-json "../../../aws-managed-policy/latest/reference/AmazonEKSClusterPolicy.md#AmazonEKSClusterPolicy-json") to the role. To attach an IAM policy to an [IAM principal](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal"), the principal that is attaching the policy must be assigned one of the following IAM actions (permissions): `iam:AttachUserPolicy` or `iam:AttachRolePolicy`.

```
aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AmazonEKSClusterPolicy --role-name myAmazonEKSClusterRole
```

### Service Linked Role

Amazon EKS automatically creates a service linked role called `AWSServiceRoleForAmazonEKS`.

This is in addition to the cluster IAM role. A service-linked role is a unique type of IAM role that is linked directly to Amazon EKS. The role allows Amazon EKS to manage clusters in your account. For more information, see [Using roles for Amazon EKS clusters](using-service-linked-roles-eks.md "using-service-linked-roles-eks.md").

The IAM Identity you use to create the EKS cluster must have permission to create the service-linked role. This includes the `iam:CreateServiceLinkedRole` permission.

If the service linked role doesn’t already exist, and your current IAM role doesn’t have sufficient permissions to create it, the cluster create operation will fail.

## Step 2: Create cluster

You can create a cluster by using:

- [eksctl](#step2-eksctl "#step2-eksctl")
- [the AWS Management Console](#step2-console "#step2-console")
- [the AWS CLI](#step2-cli "#step2-cli")

### Create cluster - eksctl

1. You need version `0.215.0` or later of the `eksctl` command line tool installed on your device or AWS CloudShell. To install or update `eksctl`, see [Installation](https://eksctl.io/installation "https://eksctl.io/installation") in the `eksctl` documentation.
2. Create an Amazon EKS `IPv4` cluster with the Amazon EKS default Kubernetes version in your default AWS Region. Before running command, make the following replacements:
3. Replace `region-code` with the AWS Region that you want to create your cluster in.
4. Replace `my-cluster` with a name for your cluster. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphanumeric character and can’t be longer than 100 characters. The name must be unique within the AWS Region and AWS account that you’re creating the cluster in.
5. Replace `1.33` with any [Amazon EKS supported version](kubernetes-versions.md "kubernetes-versions.md").
6. Change the values for `vpc-private-subnets` to meet your requirements. You can also add additional IDs. You must specify at least two subnet IDs. If you’d rather specify public subnets, you can change `--vpc-private-subnets` to `--vpc-public-subnets`. Public subnets have an associated route table with a route to an internet gateway, but private subnets don’t have an associated route table. We recommend using private subnets whenever possible.

The subnets that you choose must meet the [Amazon EKS subnet requirements](network-reqs.md#network-requirements-subnets "network-reqs.md#network-requirements-subnets"). Before selecting subnets, we recommend that you’re familiar with all of the [Amazon EKS VPC and subnet requirements and considerations](network-reqs.md "network-reqs.md"). 7. Run the following command:

```
eksctl create cluster --name my-cluster --region region-code --version 1.33 --vpc-private-subnets subnet-ExampleID1,subnet-ExampleID2 --without-nodegroup
```

Cluster provisioning takes several minutes. While the cluster is being created, several lines of output appear. The last line of output is similar to the following example line.

```
[✓]  EKS cluster "my-cluster" in "region-code" region is ready
```

8. Continue with [Step 3: Update kubeconfig](#step3 "#step3")

#### Optional Settings

To see the most options that you can specify when creating a cluster with `eksctl`, use the `eksctl create cluster --help` command. To see all the available options, you can use a `config` file. For more information, see [Using config files](https://eksctl.io/usage/creating-and-managing-clusters/#using-config-files "https://eksctl.io/usage/creating-and-managing-clusters/#using-config-files") and the [config file schema](https://eksctl.io/usage/schema/ "https://eksctl.io/usage/schema/") in the `eksctl` documentation. You can find [config file examples](https://github.com/weaveworks/eksctl/tree/master/examples "https://github.com/weaveworks/eksctl/tree/master/examples") on GitHub.

The following are optional settings that, if required, must be added to the previous command. You can only enable these options when you create the cluster, not after. If you need to specify these options, you must create the cluster with an [eksctl config file](https://eksctl.io/usage/creating-and-managing-clusters/#using-config-files "https://eksctl.io/usage/creating-and-managing-clusters/#using-config-files") and specify the settings, rather than using the previous command.

- If you want to specify one or more security groups that Amazon EKS assigns to the network interfaces that it creates, specify the [securityGroup](https://eksctl.io/usage/schema/#vpc-securityGroup "https://eksctl.io/usage/schema/#vpc-securityGroup") option.

Whether you choose any security groups or not, Amazon EKS creates a security group that enables communication between your cluster and your VPC. Amazon EKS associates this security group, and any that you choose, to the network interfaces that it creates. For more information about the cluster security group that Amazon EKS creates, see [View Amazon EKS security group requirements for clusters](sec-group-reqs.md "sec-group-reqs.md"). You can modify the rules in the cluster security group that Amazon EKS creates.

- If you want to specify which `IPv4` Classless Inter-domain Routing (CIDR) block Kubernetes assigns service IP addresses from, specify the [serviceIPv4CIDR](https://eksctl.io/usage/schema/#kubernetesNetworkConfig-serviceIPv4CIDR "https://eksctl.io/usage/schema/#kubernetesNetworkConfig-serviceIPv4CIDR") option.

Specifying your own range can help prevent conflicts between Kubernetes services and other networks peered or connected to your VPC. Enter a range in CIDR notation. For example: `10.2.0.0/16`.

The CIDR block must meet the following requirements:

    + Be within one of the following ranges: `10.0.0.0/8`, `172.16.0.0/12`, or `192.168.0.0/16`.
    + Have a minimum size of `/24` and a maximum size of `/12`.
    + Not overlap with the range of the VPC for your Amazon EKS resources.


    You can only specify this option when using the `IPv4` address family and only at cluster creation. If you don’t specify this, then Kubernetes assigns service IP addresses from either the `10.100.0.0/16` or `172.20.0.0/16` CIDR blocks.

- If you’re creating cluster and want the cluster to assign `IPv6` addresses to Pods and services instead of `IPv4` addresses, specify the [ipFamily](https://eksctl.io/usage/schema/#kubernetesNetworkConfig-ipFamily "https://eksctl.io/usage/schema/#kubernetesNetworkConfig-ipFamily") option.

Kubernetes assigns `IPv4` addresses to Pods and services, by default. Before deciding to use the `IPv6` family, make sure that you’re familiar with all of the considerations and requirements in the [VPC requirements and considerations](network-reqs.md#network-requirements-vpc "network-reqs.md#network-requirements-vpc"), [Subnet requirements and considerations](network-reqs.md#network-requirements-subnets "network-reqs.md#network-requirements-subnets"), [View Amazon EKS security group requirements for clusters](sec-group-reqs.md "sec-group-reqs.md"), and [Learn about IPv6 addresses to clusters, Pods, and services](cni-ipv6.md "cni-ipv6.md") topics. If you choose the `IPv6` family, you can’t specify an address range for Kubernetes to assign `IPv6` service addresses from like you can for the `IPv4` family. Kubernetes assigns service addresses from the unique local address range (`fc00::/7`).

### Create cluster - AWS console

1.  Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2.  Choose **Add cluster** and then choose **Create**.
3.  Under **Configuration options** select **Custom configuration**
    - For information about quickly creating a cluster wih EKS Auto Mode, see [Create an EKS Auto Mode Cluster with the AWS Management Console](automode-get-started-console.md "automode-get-started-console.md").

4.  Under **EKS Auto Mode**, toggle **Use EKS Auto Mode** off.
    - For information about creating an EKS Auto Mode cluster with custom configuration, see [Create an Amazon EKS Auto Mode cluster](create-cluster-auto.md "create-cluster-auto.md").

5.  On the **Configure cluster** page, enter the following fields:
    - **Name** – A name for your cluster. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphanumeric character and can’t be longer than 100 characters. The name must be unique within the AWS Region and AWS account that you’re creating the cluster in.
    - **Cluster IAM role** – Choose the Amazon EKS cluster IAM role that you created to allow the Kubernetes control plane to manage AWS resources on your behalf.
    - **Kubernetes version** – The version of Kubernetes to use for your cluster. We recommend selecting the latest version, unless you need an earlier version.
    - **Support type** — The Kubernetes version policy you would like to set for your cluster. If you want your cluster to only run on a standard support version, you can choose **Standard support**. If you want your cluster to enter extended support at the end of standard support for a version, you can choose **Extended support**. If you select a Kubernetes version that is currently in extended support, you can not select standard support as an option.
    - **Secrets encryption** – (Optional) Choose to enable secrets encryption of Kubernetes secrets using a KMS key. You can also enable this after you create your cluster. Before you enable this capability, make sure that you’re familiar with the information in [Encrypt Kubernetes secrets with KMS on existing clusters](enable-kms.md "enable-kms.md").
    - **Tags** – (Optional) Add any tags to your cluster. For more information, see [Organize Amazon EKS resources with tags](eks-using-tags.md "eks-using-tags.md").
    - **ARC Zonal shift** - (Optional) You can use Route53 Application Recovery controller to mitigate impaired availability zones. For more information, see [Learn about Amazon Application Recovery Controller (ARC) zonal shift in Amazon EKS](zone-shift.md "zone-shift.md").

6.  In the **Cluster access** section of the configure cluster page, enter the following fields:
    - **Bootstrap cluster administrator access** — The cluster creator is automatically a Kubernetes administrator. If you want to disable this, select **Disallow cluster administrator access**.
    - **Cluster authentication mode** — Determine how you want to grant IAM users and roles access to Kubernetes APIs. For more information, see [Set Cluster Authentication Mode](grant-k8s-access.md#set-cam "grant-k8s-access.md#set-cam").

    When you’re done with this page, choose **Next**.

7.  On the **Specify networking** page, select values for the following fields:

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

8.  (Optional) On the **Configure observability** page, choose which **Metrics** and **Control plane logging** options to turn on. By default, each log type is turned off.

        * For more information about the Prometheus metrics option, see [Step 1: Turn on Prometheus metrics](prometheus.md#turn-on-prometheus-metrics "prometheus.md#turn-on-prometheus-metrics").
        * For more information about the **Control plane logging** options, see [Send control plane logs to CloudWatch Logs](control-plane-logs.md "control-plane-logs.md").

    When you’re done with this page, choose **Next**.

9.  On the **Select add-ons** page, choose the add-ons that you want to add to your cluster. Certain add-ons are pre-selected. You can choose as many **Amazon EKS add-ons** and **AWS Marketplace add-ons** as you require. If the **AWS Marketplace add-ons** that you want to install isn’t listed, you can click the page numbering to view additional page results or search for available **AWS Marketplace add-ons** by entering text in the search box. You can also filter by **category**, **vendor**, or **pricing model** and then choose the add-ons from the search results. When creating a cluster, you can view, select, and install any add-on that supports EKS Pod Identities as detailed in [Learn how EKS Pod Identity grants pods access to AWS services](pod-identities.md "pod-identities.md").

When you’re done with this page, choose **Next**.

Some add-ons, such as Amazon VPC CNI, CoreDNS, and kube-proxy, are installed by default. If you disable any of the default add-ons, this may affect your ability to run Kubernetes applications. 10. On the **Configure selected add-ons settings** page, select the version that you want to install. You can always update to a later version after cluster creation.

For add-ons that support EKS Pod Identities, you can use the console to automatically generate the role with the name, AWS managed policy, and trust policy prepopulated specifically for the add-on. You can re-use existing roles or create new roles for supported add-ons. For the steps to use the console to create roles for add-ons that support EKS Pod Identities, see [Create add-on (AWS Console)](creating-an-add-on.md#create_add_on_console "creating-an-add-on.md#create_add_on_console"). If an add-on does not support EKS Pod Identity, a message displays with instructions to use the wizard to create the IAM roles for service accounts (IRSA) after the cluster is created.

You can update the configuration of each add-on after cluster creation. For more information about configuring add-ons, see [Update an Amazon EKS add-on](updating-an-add-on.md "updating-an-add-on.md"). When you’re done with this page, choose **Next**. 11. On the **Review and create** page, review the information that you entered or selected on the previous pages. If you need to make changes, choose **Edit**. When you’re satisfied, choose **Create**. The **Status** field shows **CREATING** while the cluster is provisioned.

###### Note

You might receive an error that one of the Availability Zones in your request doesn’t have sufficient capacity to create an Amazon EKS cluster. If this happens, the error output contains the Availability Zones that can support a new cluster. Retry creating your cluster with at least two subnets that are located in the supported Availability Zones for your account. For more information, see [Insufficient capacity](troubleshooting.md#ice "troubleshooting.md#ice").

Cluster provisioning takes several minutes. 12. Continue with [Step 3: Update kubeconfig](#step3 "#step3")

### Create cluster - AWS CLI

1.  Create your cluster with the command that follows. Before running the command, make the following replacements:

        * Replace `region-code` with the AWS Region that you want to create your cluster in.
        * Replace `my-cluster` with a name for your cluster. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphanumeric character and can’t be longer than 100 characters. The name must be unique within the AWS Region and AWS account that you’re creating the cluster in.
        * Replace `1.33` with any [Amazon EKS supported version](kubernetes-versions.md "kubernetes-versions.md").
        * Replace `111122223333` with your account ID and `myAmazonEKSClusterRole` with the name of your cluster IAM role.
        * Replace the values for `subnetIds` with your own. You can also add additional IDs. You must specify at least two subnet IDs.


        The subnets that you choose must meet the [Amazon EKS subnet requirements](network-reqs.md#network-requirements-subnets "network-reqs.md#network-requirements-subnets"). Before selecting subnets, we recommend that you’re familiar with all of the [Amazon EKS VPC and subnet requirements and considerations](network-reqs.md "network-reqs.md").
        * If you don’t want to specify a security group ID, remove `,securityGroupIds=sg-<ExampleID1>` from the command. If you want to specify one or more security group IDs, replace the values for `securityGroupIds` with your own. You can also add additional IDs.


        Whether you choose any security groups or not, Amazon EKS creates a security group that enables communication between your cluster and your VPC. Amazon EKS associates this security group, and any that you choose, to the network interfaces that it creates. For more information about the cluster security group that Amazon EKS creates, see [View Amazon EKS security group requirements for clusters](sec-group-reqs.md "sec-group-reqs.md"). You can modify the rules in the cluster security group that Amazon EKS creates.



        ```
        aws eks create-cluster --region region-code --name my-cluster --kubernetes-version 1.33 \
           --role-arn arn:aws:iam::111122223333:role/myAmazonEKSClusterRole \
           --resources-vpc-config subnetIds=subnet-ExampleID1,subnet-ExampleID2,securityGroupIds=sg-ExampleID1
        ```

        ###### Note

        You might receive an error that one of the Availability Zones in your request doesn’t have sufficient capacity to create an Amazon EKS cluster. If this happens, the error output contains the Availability Zones that can support a new cluster. Retry creating your cluster with at least two subnets that are located in the supported Availability Zones for your account. For more information, see [Insufficient capacity](troubleshooting.md#ice "troubleshooting.md#ice").


        The following are optional settings that, if required, must be added to the previous command. You can only enable these options when you create the cluster, not after.
        * By default, EKS installs multiple networking add-ons during cluster creation. This includes the Amazon VPC CNI, CoreDNS, and kube-proxy.


        If you’d like to disable the installation of these default networking add-ons, use the parameter below. This may be used for alternate CNIs, such as Cilium. Review the [EKS API reference](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") for more information.



        `aws eks create-cluster --bootstrapSelfManagedAddons false`
        * If you want to specify which `IPv4` Classless Inter-domain Routing (CIDR) block Kubernetes assigns service IP addresses from, you must specify it by adding the `--kubernetes-network-config serviceIpv4Cidr=<cidr-block>` to the following command.


        Specifying your own range can help prevent conflicts between Kubernetes services and other networks peered or connected to your VPC. Enter a range in CIDR notation. For example: `10.2.0.0/16`.


        The CIDR block must meet the following requirements:




        	+ Be within one of the following ranges: `10.0.0.0/8`, `172.16.0.0/12`, or `192.168.0.0/16`.
        	+ Have a minimum size of `/24` and a maximum size of `/12`.
        	+ Not overlap with the range of the VPC for your Amazon EKS resources.

    You can only specify this option when using the `IPv4` address family and only at cluster creation. If you don’t specify this, then Kubernetes assigns service IP addresses from either the `10.100.0.0/16` or `172.20.0.0/16` CIDR blocks.

        * If you’re creating a cluster and want the cluster to assign `IPv6` addresses to Pods and services instead of `IPv4` addresses, add `--kubernetes-network-config ipFamily=ipv6` to the following command.


        Kubernetes assigns `IPv4` addresses to Pods and services, by default. Before deciding to use the `IPv6` family, make sure that you’re familiar with all of the considerations and requirements in the [VPC requirements and considerations](network-reqs.md#network-requirements-vpc "network-reqs.md#network-requirements-vpc"), [Subnet requirements and considerations](network-reqs.md#network-requirements-subnets "network-reqs.md#network-requirements-subnets"), [View Amazon EKS security group requirements for clusters](sec-group-reqs.md "sec-group-reqs.md"), and [Learn about IPv6 addresses to clusters, Pods, and services](cni-ipv6.md "cni-ipv6.md") topics. If you choose the `IPv6` family, you can’t specify an address range for Kubernetes to assign `IPv6` service addresses from like you can for the `IPv4` family. Kubernetes assigns service addresses from the unique local address range (`fc00::/7`).

2.  It takes several minutes to provision the cluster. You can query the status of your cluster with the following command.

```
aws eks describe-cluster --region region-code --name my-cluster --query "cluster.status"
```

Don’t proceed to the next step until the output returned is `ACTIVE`. 3. Continue with [Step 3: Update kubeconfig](#step3 "#step3")

## Step 3: Update kubeconfig

1. If you created your cluster using `eksctl`, then you can skip this step. This is because `eksctl` already completed this step for you. Enable `kubectl` to communicate with your cluster by adding a new context to the `kubectl`
   `config` file. For more information about how to create and update the file, see [Connect kubectl to an EKS cluster by creating a kubeconfig file](create-kubeconfig.md "create-kubeconfig.md").

```
aws eks update-kubeconfig --region region-code --name my-cluster
```

An example output is as follows.

```
Added new context arn:aws:eks:region-code:111122223333:cluster/my-cluster to /home/username/.kube/config
```

2. Confirm communication with your cluster by running the following command.

```
kubectl get svc
```

An example output is as follows.

```
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.100.0.1   <none>        443/TCP   28h
```

## Step 4: Cluster setup

1. (Recommended) To use some Amazon EKS add-ons, or to enable individual Kubernetes workloads to have specific AWS Identity and Access Management (IAM) permissions, [create an IAM OpenID Connect (OIDC) provider](enable-iam-roles-for-service-accounts.md "enable-iam-roles-for-service-accounts.md") for your cluster. You only need to create an IAM OIDC provider for your cluster once. To learn more about Amazon EKS add-ons, see [Amazon EKS add-ons](eks-add-ons.md "eks-add-ons.md"). To learn more about assigning specific IAM permissions to your workloads, see [IAM roles for service accounts](iam-roles-for-service-accounts.md "iam-roles-for-service-accounts.md").
2. (Recommended) Configure your cluster for the Amazon VPC CNI plugin for Kubernetes plugin before deploying Amazon EC2 nodes to your cluster. By default, the plugin was installed with your cluster. When you add Amazon EC2 nodes to your cluster, the plugin is automatically deployed to each Amazon EC2 node that you add. The plugin requires you to attach one of the following IAM policies to an IAM role. If your cluster uses the `IPv4` family, use the [AmazonEKS_CNI_Policy](../../../aws-managed-policy/latest/reference/AmazonEKS_CNI_Policy.md "../../../aws-managed-policy/latest/reference/AmazonEKS_CNI_Policy.md") managed IAM policy. If your cluster uses the `IPv6` family, use an [IAM policy that you create](cni-iam-role.md#cni-iam-role-create-ipv6-policy "cni-iam-role.md#cni-iam-role-create-ipv6-policy").

The IAM role that you attach the policy to can be the node IAM role, or a dedicated role used only for the plugin. We recommend attaching the policy to this role. For more information about creating the role, see [Configure Amazon VPC CNI plugin to use IRSA](cni-iam-role.md "cni-iam-role.md") or [Amazon EKS node IAM role](create-node-role.md "create-node-role.md"). 3. If you deployed your cluster using the AWS Management Console, you can skip this step. The AWS Management Console deploys the Amazon VPC CNI plugin for Kubernetes, CoreDNS, and `kube-proxy` Amazon EKS add-ons, by default.

If you deploy your cluster using either `eksctl` or the AWS CLI, then the Amazon VPC CNI plugin for Kubernetes, CoreDNS, and `kube-proxy` self-managed add-ons are deployed. You can migrate the Amazon VPC CNI plugin for Kubernetes, CoreDNS, and `kube-proxy` self-managed add-ons that are deployed with your cluster to Amazon EKS add-ons. For more information, see [Amazon EKS add-ons](eks-add-ons.md "eks-add-ons.md"). 4. (Optional) If you haven’t already done so, you can enable Prometheus metrics for your cluster. For more information, see [Create a scraper](../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-create "../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-create") in the _Amazon Managed Service for Prometheus User Guide_. 5. If you plan to deploy workloads to your cluster that use Amazon EBS volumes, then you must install the [Amazon EBS CSI](ebs-csi.md "ebs-csi.md") to your cluster before deploying the workloads.

## Next steps

- The [IAM principal](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal") that created the cluster is the only principal that has access to the cluster. [Grant permissions to other IAM principals](grant-k8s-access.md "grant-k8s-access.md") so they can access your cluster.
- If the IAM principal that created the cluster only has the minimum IAM permissions referenced in the prerequisites, then you might want to add additional Amazon EKS permissions for that principal. For more information about granting Amazon EKS permissions to IAM principals, see [Identity and access management for Amazon EKS](security-iam.md "security-iam.md").
- If you want the IAM principal that created the cluster, or any other principals to view Kubernetes resources in the Amazon EKS console, grant the [Required permissions](view-kubernetes-resources.md#view-kubernetes-resources-permissions "view-kubernetes-resources.md#view-kubernetes-resources-permissions") to the entities.
- If you want nodes and IAM principals to access your cluster from within your VPC, enable the private endpoint for your cluster. The public endpoint is enabled by default. You can disable the public endpoint once you’ve enabled the private endpoint, if desired. For more information, see [Cluster API server endpoint](cluster-endpoint.md "cluster-endpoint.md").
- [Enable secrets encryption for your cluster](enable-kms.md "enable-kms.md").
- [Configure logging for your cluster](control-plane-logs.md "control-plane-logs.md").
- [Add nodes to your cluster](eks-compute.md "eks-compute.md").

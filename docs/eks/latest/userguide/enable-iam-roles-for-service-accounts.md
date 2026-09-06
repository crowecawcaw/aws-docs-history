

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an IAM OIDC provider for your cluster
<a name="enable-iam-roles-for-service-accounts"></a>

Your cluster has an [OpenID Connect](https://openid.net/connect/) (OIDC) issuer URL associated with it. To use AWS Identity and Access Management (IAM) roles for service accounts, an IAM OIDC provider must exist for your cluster’s OIDC issuer URL.

## Prerequisites
<a name="_prerequisites"></a>
+ An existing Amazon EKS cluster. To deploy one, see [Get started with Amazon EKS](getting-started.md).
+ Version `2.12.3` or later or version `1.27.160` or later of the AWS Command Line Interface (AWS CLI) installed and configured on your device or AWS CloudShell. To check your current version, use `aws --version | cut -d / -f2 | cut -d ' ' -f1`. Package managers such as `yum`, `apt-get`, or Homebrew for macOS are often several versions behind the latest version of the AWS CLI. To install the latest version, see [Installing](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) and [Quick configuration with aws configure](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config) in the * AWS Command Line Interface User Guide*. The AWS CLI version that is installed in AWS CloudShell might also be several versions behind the latest version. To update it, see [Installing AWS CLI to your home directory](https://docs.aws.amazon.com/cloudshell/latest/userguide/vm-specs.html#install-cli-software) in the * AWS CloudShell User Guide*.
+ The `kubectl` command line tool is installed on your device or AWS CloudShell. The version can be the same as or up to one minor version earlier or later than the Kubernetes version of your cluster. For example, if your cluster version is `1.29`, you can use `kubectl` version `1.28`, `1.29`, or `1.30` with it. To install or upgrade `kubectl`, see [Set up `kubectl` and `eksctl`](install-kubectl.md).
+ An existing `kubectl` `config` file that contains your cluster configuration. To create a `kubectl` `config` file, see [Connect kubectl to an EKS cluster by creating a kubeconfig file](create-kubeconfig.md).

You can create an IAM OIDC provider for your cluster using `eksctl` or the AWS Management Console.

## Create OIDC provider (eksctl)
<a name="_create_oidc_provider_eksctl"></a>

1. Version `0.215.0` or later of the `eksctl` command line tool installed on your device or AWS CloudShell. To install or update `eksctl`, see [Installation](https://eksctl.io/installation) in the `eksctl` documentation.

1. Determine the OIDC issuer ID for your cluster.

   Retrieve your cluster’s OIDC issuer ID and store it in a variable. Replace `<my-cluster>` with your own value.

   ```
   cluster_name=<my-cluster>
   oidc_id=$(aws eks describe-cluster --name $cluster_name --query "cluster.identity.oidc.issuer" --output text | cut -d '/' -f 5)
   echo $oidc_id
   ```

1. Determine whether an IAM OIDC provider with your cluster’s issuer ID is already in your account.

   ```
   aws iam list-open-id-connect-providers | grep $oidc_id | cut -d "/" -f4
   ```

   If output is returned, then you already have an IAM OIDC provider for your cluster and you can skip the next step. If no output is returned, then you must create an IAM OIDC provider for your cluster.

1. Create an IAM OIDC identity provider for your cluster with the following command.

   ```
   eksctl utils associate-iam-oidc-provider --cluster $cluster_name --approve
   ```
**Note**  
If your cluster’s VPC has no outbound internet access and you haven’t set up private access to the cluster OIDC endpoint, operations that reach that endpoint from inside the VPC, such as creating an OIDC provider with `eksctl`, can’t resolve the OIDC issuer hostname. An example error message follows:  

   ```
   ** server cant find oidc.eks.<region-code>.amazonaws.com: NXDOMAIN
   ```

   To reach the cluster OIDC endpoint privately from your VPC, create a VPC interface endpoint for it (`com.amazonaws.<region-code>.oidc-eks`) with private DNS enabled. For more information, see [Access the cluster OIDC endpoint using AWS PrivateLink](https://docs.aws.amazon.com/eks/latest/userguide/vpc-interface-endpoints.html#oidc-vpc-interface-endpoints).

Alternatively, you can run the command outside the VPC (for example, in AWS CloudShell) or create a split-horizon conditional resolver. For an example, see the [Amazon EKS feature request](https://github.com/aws/containers-roadmap/issues/2038) on GitHub.

## Create OIDC provider (AWS Console)
<a name="create_oidc_provider_shared_aws_console"></a>

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. In the left pane, select **Clusters**, and then select the name of your cluster on the **Clusters** page.

1. In the **Details** section on the **Overview** tab, note the value of the **OpenID Connect provider URL**.

1. Open the IAM console at https://console.aws.amazon.com/iam/.

1. In the left navigation pane, choose **Identity Providers** under **Access management**. If a **Provider** is listed that matches the URL for your cluster, then you already have a provider for your cluster. If a provider isn’t listed that matches the URL for your cluster, then you must create one.

1. To create a provider, choose **Add provider**.

1. For **Provider type**, select **OpenID Connect**.

1. For **Provider URL**, enter the OIDC provider URL for your cluster.

1. For **Audience**, enter `sts.amazonaws.com`.

1. (Optional) Add any tags, for example a tag to identify which cluster is for this provider.

1. Choose **Add provider**.

Next step: [Assign IAM roles to Kubernetes service accounts](associate-service-account-role.md) 
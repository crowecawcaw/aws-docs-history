**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an IAM OIDC provider for your cluster

Your cluster has an [OpenID Connect](https://openid.net/connect/ "https://openid.net/connect/") (OIDC) issuer URL associated with it. To use AWS Identity and Access Management (IAM) roles for service accounts, an IAM OIDC provider must exist for your cluster’s OIDC issuer URL.

## Prerequisites

- An existing Amazon EKS cluster. To deploy one, see [Get started with Amazon EKS](getting-started.md "getting-started.md").
- Version `2.12.3` or later or version `1.27.160` or later of the AWS Command Line Interface (AWS CLI) installed and configured on your device or AWS CloudShell. To check your current version, use `aws --version | cut -d / -f2 | cut -d ' ' -f1`. Package managers such `yum`, `apt-get`, or Homebrew for macOS are often several versions behind the latest version of the AWS CLI. To install the latest version, see [Installing](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") and [Quick configuration with aws configure](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config") in the _AWS Command Line Interface User Guide_. The AWS CLI version that is installed in AWS CloudShell might also be several versions behind the latest version. To update it, see [Installing AWS CLI to your home directory](../../../cloudshell/latest/userguide/vm-specs.md#install-cli-software "../../../cloudshell/latest/userguide/vm-specs.md#install-cli-software") in the _AWS CloudShell User Guide_.
- The `kubectl` command line tool is installed on your device or AWS CloudShell. The version can be the same as or up to one minor version earlier or later than the Kubernetes version of your cluster. For example, if your cluster version is `1.29`, you can use `kubectl` version `1.28`, `1.29`, or `1.30` with it. To install or upgrade `kubectl`, see [Set up kubectl and eksctl](install-kubectl.md "install-kubectl.md").
- An existing `kubectl`
  `config` file that contains your cluster configuration. To create a `kubectl`
  `config` file, see [Connect kubectl to an EKS cluster by creating a kubeconfig file](create-kubeconfig.md "create-kubeconfig.md").

You can create an IAM OIDC provider for your cluster using `eksctl` or the AWS Management Console.

## Create OIDC provider (eksctl)

1. Version `0.215.0` or later of the `eksctl` command line tool installed on your device or AWS CloudShell. To install or update `eksctl`, see [Installation](https://eksctl.io/installation "https://eksctl.io/installation") in the `eksctl` documentation.
2. Determine the OIDC issuer ID for your cluster.

Retrieve your cluster’s OIDC issuer ID and store it in a variable. Replace `<my-cluster>` with your own value.

```
cluster_name=<my-cluster>
oidc_id=$(aws eks describe-cluster --name $cluster_name --query "cluster.identity.oidc.issuer" --output text | cut -d '/' -f 5)
echo $oidc_id
```

3. Determine whether an IAM OIDC provider with your cluster’s issuer ID is already in your account.

```
aws iam list-open-id-connect-providers | grep $oidc_id | cut -d "/" -f4
```

If output is returned, then you already have an IAM OIDC provider for your cluster and you can skip the next step. If no output is returned, then you must create an IAM OIDC provider for your cluster. 4. Create an IAM OIDC identity provider for your cluster with the following command.

```
eksctl utils associate-iam-oidc-provider --cluster $cluster_name --approve
```

###### Note

If you enabled the EKS VPC endpoint, the EKS OIDC service endpoint couldn’t be accessed from inside that VPC. Consequently, your operations such as creating an OIDC provider with `eksctl` in the VPC will not work and will result in a timeout. An example error message follows:

```
** server cant find oidc.eks.<region-code>.amazonaws.com: NXDOMAIN
```

To complete this step, you can run the command outside the VPC, for example in AWS CloudShell or on a computer connected to the internet. Alternatively, you can create a split-horizon conditional resolver in the VPC, such as Route 53 Resolver to use a different resolver for the OIDC Issuer URL and not use the VPC DNS for it. For an example of conditional forwarding in CoreDNS, see the [Amazon EKS feature request](https://github.com/aws/containers-roadmap/issues/2038 "https://github.com/aws/containers-roadmap/issues/2038") on GitHub.

## Create OIDC provider (AWS Console)

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. In the left pane, select **Clusters**, and then select the name of your cluster on the **Clusters** page.
3. In the **Details** section on the **Overview** tab, note the value of the **OpenID Connect provider URL**.
4. Open the IAM console at https://console.aws.amazon.com/iam/.
5. In the left navigation pane, choose **Identity Providers** under **Access management**. If a **Provider** is listed that matches the URL for your cluster, then you already have a provider for your cluster. If a provider isn’t listed that matches the URL for your cluster, then you must create one.
6. To create a provider, choose **Add provider**.
7. For **Provider type**, select **OpenID Connect**.
8. For **Provider URL**, enter the OIDC provider URL for your cluster.
9. For **Audience**, enter `sts.amazonaws.com`.
10. (Optional) Add any tags, for example a tag to identify which cluster is for this provider.
11. Choose **Add provider**.

Next step:
[Assign IAM roles to Kubernetes service accounts](associate-service-account-role.md "associate-service-account-role.md")

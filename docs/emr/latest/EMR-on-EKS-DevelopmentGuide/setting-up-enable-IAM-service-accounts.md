

# Option 2: Enable IAM Roles for Service Accounts (IRSA) on the EKS cluster
<a name="setting-up-enable-IAM-service-accounts"></a>

The IAM roles for service accounts feature is available on Amazon EKS versions 1.14 and later and for EKS clusters that are updated to versions 1.13 or later on or after September 3rd, 2019. To use this feature, you can update existing EKS clusters to version 1.14 or later. For more information, see [Updating an Amazon EKS cluster Kubernetes version](https://docs.aws.amazon.com/eks/latest/userguide/update-cluster.html).

If your cluster supports IAM roles for service accounts, it has an [OpenID Connect](https://openid.net/connect/) issuer URL associated with it. You can view this URL in the Amazon EKS console, or you can use the following AWS CLI command to retrieve it.

**Important**  
You must use the latest version of the AWS CLI to receive the proper output from this command.

```
aws eks describe-cluster --name {{cluster_name}} --query "cluster.identity.oidc.issuer" --output text
```

The expected output is as follows.

```
https://oidc.eks.<region-code>.amazonaws.com/id/EXAMPLED539D4633E53DE1B716D3041E
```

To use IAM roles for service accounts in your cluster, you must create an OIDC identity provider using either [eksctl](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html#create-oidc-eksctl) or the [AWS Management Console](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html#create-oidc-console).

## To create an IAM OIDC identity provider for your cluster with `eksctl`
<a name="setting-up-OIDC-eksctl"></a>

Check your `eksctl` version with the following command. This procedure assumes that you have installed `eksctl` and that your `eksctl` version is 0.32.0 or later.

```
eksctl version
```

For more information about installing or upgrading eksctl, see [Installing or upgrading eksctl](https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html#installing-eksctl).

Create your OIDC identity provider for your cluster with the following command. Replace {{cluster\_name}} with your own value.

```
eksctl utils associate-iam-oidc-provider --cluster {{cluster_name}} --approve
```

## To create an IAM OIDC identity provider for your cluster with the AWS Management Console
<a name="setting-up-OIDC-console"></a>

Retrieve the OIDC issuer URL from the Amazon EKS console description of your cluster, or use the following AWS CLI command.

Use the following command to retrieve the OIDC issuer URL from the AWS CLI.

```
aws eks describe-cluster --name <cluster_name> --query "cluster.identity.oidc.issuer" --output text
```

Use the following steps to retrieve the OIDC issuer URL from the Amazon EKS console. 

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation panel, choose **Identity Providers**, and then choose **Create Provider**.

   1. For **Provider Type**, choose **Choose a provider type**, and then choose **OpenID Connect**.

   1. For **Provider URL**, paste the OIDC issuer URL for your cluster.

   1. For Audience, type sts.amazonaws.com and choose **Next Step**.

1. Verify that the provider information is correct, and then choose **Create** to create your identity provider.
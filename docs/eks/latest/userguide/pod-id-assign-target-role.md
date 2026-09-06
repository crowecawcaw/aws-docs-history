

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Access AWS Resources using EKS Pod Identity Target IAM Roles
<a name="pod-id-assign-target-role"></a>

When running applications on Amazon Elastic Kubernetes Service (Amazon EKS), you might need to access AWS resources that exist in different AWS accounts. This guide shows you how to set up cross account access using EKS Pod Identity, which enables your Kubernetes pods to access other AWS resources using target roles.

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, ensure you have completed the following steps:
+  [Set up the Amazon EKS Pod Identity Agent](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-agent-setup.html) 
+  [Create an EKS Pod Identity role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-role.html) 

## How It Works
<a name="_how_it_works"></a>

Pod Identity enables applications in your EKS cluster to access AWS resources across accounts through a process called role chaining.

When creating a Pod Identity association, you can provide two IAM roles: an [EKS Pod Identity role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-role.html) in the same account as your EKS cluster and a Target IAM Role from the account containing your AWS resources you wish to access (like S3 buckets or RDS Databases). The [EKS Pod Identity role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-role.html) must be in your EKS cluster’s account due to [IAM PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam-passrole-service.html) requirements, while the Target IAM Role can be in any AWS account. PassRole enables an AWS entity to delegate role assumption to another service. EKS Pod Identity uses PassRole to connect a role to a Kubernetes service account, requiring both the role and the identity passing it to be in the same AWS account as the EKS cluster. When your application pod needs to access AWS resources, it requests credentials from Pod Identity. Pod Identity then automatically performs two role assumptions in sequence: first assuming the [EKS Pod Identity role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-role.html), then using those credentials to assume the Target IAM Role. This process provides your pod with temporary credentials that have the permissions defined in the target role, allowing secure access to resources in other AWS accounts.

## Caching considerations
<a name="_caching_considerations"></a>

Due to caching mechanisms, updates to an IAM role in an existing Pod Identity association may not take effect immediately in the pods running on your EKS cluster. The Pod Identity Agent caches IAM credentials based on the association’s configuration at the time the credentials are fetched. If the association includes only an [EKS Pod Identity role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-role.html) and no Target IAM Role, the cached credentials last for 6 hours. If the association includes both the [EKS Pod Identity role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-role.html) ARN and a Target IAM Role, the cached credentials last for 59 minutes. Modifying an existing association, such as updating the [EKS Pod Identity role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-role.html) ARN, adding a Target IAM Role, or updating the Session Policy on the association, does not reset the existing cache. As a result, the agent will not recognize updates until the cached credentials refresh. To apply changes sooner, you can recreate the existing pods; otherwise, you will need to wait for the cache to expire.

## Step 1: Create and associate a Target IAM Role
<a name="_step_1_create_and_associate_a_target_iam_role"></a>

In this step, you will establish a secure trust chain by creating and configuring a Target IAM Role. For demonstration, we will create a new Target IAM Role to establish a trust chain between two AWS accounts: the [EKS Pod Identity role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-role.html) (e.g., `eks-pod-identity-primary-role`) in the EKS cluster’s AWS account gains permission to assume the Target IAM Role (e.g. `eks-pod-identity-aws-resources`) in your target account, enabling access to AWS resources like Amazon S3 buckets.

### Create the Target IAM Role
<a name="_create_the_target_iam_role"></a>

1. Open the [Amazon IAM console](https://console.aws.amazon.com/iam/home).

1. In the top navigation bar, verify that you are signed into the account containing the AWS resources (like S3 buckets or DynamoDB tables) for your Target IAM Role.

1. In the left navigation pane, choose **Roles**.

1. Choose the **Create role** button, then ** AWS account** under "Trusted entity type."

1. Choose **Another AWS account**, enter your AWS account number (the account where your [EKS Pod Identity role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-role.html) exists), then choose **Next**.

1. Add the permission policies you would like to associate to the role (e.g., AmazonS3FullAccess), then choose **Next**.

1. Enter a role name, such as `MyCustomIAMTargetRole`, then choose **Create role**.

### Update the Target IAM Role trust policy
<a name="_update_the_target_iam_role_trust_policy"></a>

1. After creating the role, you’ll be returned to the **Roles** list. Find and select the new role you created in the previous step (e.g., `MyCustomIAMTargetRole`).

1. Select the **Trust relationships** tab.

1. Choose **Edit trust policy**.

1. In the policy editor, replace the default JSON with your trust policy. Replace the placeholder values for role name and `111122223333` in the IAM role ARN with the AWS account ID hosting your EKS cluster. You can also optionally use PrincipalTags in the role trust policy to authorize only specific service accounts from a given cluster and namespace to assume your target role. For example:

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:root"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:TagSession"
      ],
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/eks-cluster-arn": "arn:aws:eks:us-east-1:111122223333:cluster/example-cluster",
          "aws:RequestTag/kubernetes-namespace": "ExampleNameSpace",
          "aws:RequestTag/kubernetes-service-account": "ExampleServiceAccountName"
        },
        "ArnEquals": {
          "aws:PrincipalARN": "arn:aws:iam::111122223333:role/eks-pod-identity-primary-role"
        }
      }
    }
  ]
}
```

The above policy lets the role `eks-pod-identity-primary-role` from AWS account 111122223333 with the relevant [EKS Pod Identity Session Tags](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-abac.html) assume this role.

If you [Disabled Session Tags](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-abac.html#pod-id-abac-tags) in your EKS Pod Identity, EKS Pod Identity also sets the `sts:ExternalId` with information about the cluster, namespace, and service account of a pod when assuming a target role.

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "region/111122223333/cluster-name/namespace/service-account-name"
        },
        "ArnEquals": {
          "aws:PrincipalARN": "arn:aws:iam::111122223333:role/eks-pod-identity-primary-role"
        }
      }
    },
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:root"
      },
      "Action": "sts:TagSession"
    }
  ]
}
```

The above policy helps ensure that only the expected cluster, namespace and service account can assume the target role.

### Update the permission policy for EKS Pod Identity role
<a name="_update_the_permission_policy_for_eks_pod_identity_role"></a>

In this step, you will update the permission policy of the [EKS Pod Identity role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-role.html) associated with your Amazon EKS cluster by adding the Target IAM Role ARN as a resource.

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. In the left navigation pane, select **Clusters**, and then select the name of your EKS cluster.

1. Choose the **Access** tab.

1. Under **Pod Identity associations**, select your [EKS Pod Identity role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-role.html).

1. Choose **Permissions**, **Add permissions**, then **Create inline policy**.

1. Choose **JSON**.

1. In the policy editor, replace the default JSON with your permission policy. Replace the placeholder value for role name and `222233334444` in the IAM role ARN with your Target IAM Role. For example:

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole",
                "sts:TagSession"
            ],
            "Resource": "arn:aws:iam::222233334444:role/eks-pod-identity-aws-resources"
        }
    ]
}
```

## Step 2: Associate the Target IAM Role to a Kubernetes service account
<a name="_step_2_associate_the_target_iam_role_to_a_kubernetes_service_account"></a>

In this step, you will create an association between the Target IAM role and the Kubernetes service account in your EKS cluster.

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. In the left navigation pane, select **Clusters**, and then select the name of the cluster that you want to add the association to.

1. Choose the **Access** tab.

1. In the **Pod Identity associations**, choose **Create**.

1. Choose the [EKS Pod Identity role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-role.html) in **IAM role** for your workloads to assume.

1. Choose the Target IAM role in **Target IAM role** that will be assumed by the [EKS Pod Identity role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-role.html).

1. In the **Kubernetes namespace** field, enter the name of the namespace where you want to create the association (e.g., `my-app-namespace`). This defines where the service account resides.

1. In the **Kubernetes service account** field, enter the name of the service account (e.g., `my-service-account`) that will use the IAM credentials. This links the IAM role to the service account.

1. (Optional) Select **Disable session tags** to disable the default session tags that Pod Identity automatically adds when it assumes the role.

1. (Optional) Toggle **Configure session policy** to configure an IAM policy to apply additional restrictions to this Pod Identity association beyond the permissions defined in the IAM policy attached to the **Target IAM role**.
**Note**  
1. A session policy can only be applied when the **Disable session tags** setting is checked. 2. If you specify a session policy, then the policy restrictions apply to the **Target IAM role**'s permissions and not the **IAM role** associated with this Pod Identity association.

1. Choose **Create** to create the association.
**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Update access entries

You can update an access entry using the AWS Management Console or the AWS CLI.

## AWS Management Console

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Choose the name of the cluster that you want to create an access entry in.
3. Choose the **Access** tab.
4. Choose the access entry that you want to update.
5. Choose **Edit**.
6. For **Username**, you can change the existing value.
7. For **Groups**, you can remove existing group names or add new group names. If the following groups names exist, don’t remove them: **system:nodes** or **system:bootstrappers**. Removing these groups can cause your cluster to function improperly. If you don’t specify any group names and want to use Amazon EKS authorization, associate an [access policy](access-policies.md "access-policies.md") in a later step.
8. For **Tags**, you can assign labels to the access entry. For example, to make it easier to find all resources with the same tag. You can also remove existing tags.
9. Choose **Save changes**.
10. If you want to associate an access policy to the entry, see [Associate access policies with access entries](access-policies.md "access-policies.md").

## AWS CLI

1. Install the AWS CLI, as described in [Installing](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") in the AWS Command Line Interface User Guide.
2. To update an access entry
   Replace `my-cluster` with the name of your cluster, `111122223333` with your AWS account ID, and `EKS-my-cluster-my-namespace-Viewers` with the name of an IAM role.

```
aws eks update-access-entry --cluster-name my-cluster --principal-arn arn:aws:iam::111122223333:role/EKS-my-cluster-my-namespace-Viewers --kubernetes-groups Viewers
```

You can’t use the `--kubernetes-groups` option if the type of the access entry is a value other than `STANDARD`. You also can’t associate an access policy to an access entry with a type other than `STANDARD`.



 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Delete access entries
<a name="deleting-access-entries"></a>

If you discover that you deleted an access entry in error, you can always recreate it. If the access entry that you’re deleting is associated to any access policies, the associations are automatically deleted. You don’t have to disassociate access policies from an access entry before deleting the access entry.

You can delete an access entry using the AWS Management Console or the AWS CLI.

## AWS Management Console
<a name="access-delete-console"></a>

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. Choose the name of the cluster that you want to delete an access entry from.

1. Choose the **Access** tab.

1. In the **Access entries** list, choose the access entry that you want to delete.

1. Choose Delete.

1. In the confirmation dialog box, choose **Delete**.

## AWS CLI
<a name="access-delete-cli"></a>

1. Install the AWS CLI, as described in [Installing](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) in the AWS Command Line Interface User Guide.

1. To delete an access entry Replace {{my-cluster}} with the name of your cluster, {{111122223333}} with your AWS account ID, and {{my-role}} with the name of the IAM role that you no longer want to have access to your cluster.

   ```
   aws eks delete-access-entry --cluster-name my-cluster --principal-arn arn:aws:iam::111122223333:role/my-role
   ```
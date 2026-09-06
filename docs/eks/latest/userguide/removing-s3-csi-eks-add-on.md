

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Remove the Mountpoint for Amazon S3 Amazon EKS add-on
<a name="removing-s3-csi-eks-add-on"></a>

You have two options for removing the [Mountpoint for Amazon S3 CSI driver](s3-csi.md).
+  **Preserve add-on software on your cluster** – This option removes Amazon EKS management of any settings. It also removes the ability for Amazon EKS to notify you of updates and automatically update the Amazon EKS add-on after you initiate an update. However, it preserves the add-on software on your cluster. This option makes the add-on a self-managed installation, rather than an Amazon EKS add-on. With this option, there’s no downtime for the add-on. The commands in this procedure use this option.
+  **Remove add-on software entirely from your cluster** – We recommend that you remove the Amazon EKS add-on from your cluster only if there are no resources on your cluster that are dependent on it. To do this option, delete `--preserve` from the command you use in this procedure.

If the add-on has an IAM account associated with it, the IAM account isn’t removed.

You can use the following tools to remove the Amazon S3 CSI add-on:
+  [eksctl](#eksctl_s3_remove_store_app_data) 
+  [AWS Management Console](#console_s3_remove_store_app_data) 
+  [AWS CLI](#awscli_s3_remove_store_app_data) 

## eksctl
<a name="eksctl_s3_remove_store_app_data"></a>

 **To remove the Amazon S3 CSI add-on using `eksctl` ** 

Replace {{my-cluster}} with the name of your cluster, and then run the following command.

```
eksctl delete addon --cluster my-cluster --name aws-mountpoint-s3-csi-driver --preserve
```

## AWS Management Console
<a name="console_s3_remove_store_app_data"></a>

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. In the left navigation pane, choose **Clusters**.

1. Choose the name of the cluster that you want to remove the Mountpoint for Amazon S3 CSI add-on for.

1. Choose the **Add-ons** tab.

1. Choose **Mountpoint for Amazon S3 CSI Driver**.

1. Choose **Remove**.

1. In the **Remove: aws-mountpoint-s3-csi-driver** confirmation dialog box, do the following:

   1. If you want Amazon EKS to stop managing settings for the add-on, select **Preserve on cluster**. Do this if you want to retain the add-on software on your cluster. This is so that you can manage all of the settings of the add-on on your own.

   1. Enter `aws-mountpoint-s3-csi-driver`.

   1. Select **Remove**.

## AWS CLI
<a name="awscli_s3_remove_store_app_data"></a>

 **To remove the Amazon S3 CSI add-on using the AWS CLI** 

Replace {{my-cluster}} with the name of your cluster, and then run the following command.

```
aws eks delete-addon --cluster-name my-cluster --addon-name aws-mountpoint-s3-csi-driver --preserve
```
**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Add flexibility to plan Kubernetes version upgrades by enabling EKS extended support

This topic describes how to set the _upgrade policy_ of an EKS cluster to enable extended support. The upgrade policy of an EKS cluster determines what happens when a cluster reaches the end of the standard _support period_. If a cluster upgrade policy has extended support enabled, it will enter the extended support period at the end of the standard support period. The cluster will not be automatically upgraded at the end of the standard support period.

Clusters actually in the _extended support period_ incur higher costs. If a cluster merely has the upgrade policy set to enable extended support, and is otherwise in the _standard support period_, it incurs standard costs.

If you create a cluster in the AWS console, it will have the upgrade policy set to disable extended support. If you create a cluster in another way, it will have the upgrade policy set to enable extended support. For example, clusters created with the AWS API have extended support enabled.

For more information about upgrade policies, see [Cluster upgrade policy](view-upgrade-policy.md "view-upgrade-policy.md").

###### Important

If you want your cluster to stay on its current Kubernetes version to take advantage of the extended support period, you must enable the extended support upgrade policy before the end of standard support period.

If you do not enable extended support, your cluster will be automatically upgraded.

## Enable EKS extended support (AWS Console)

1. Navigate to your EKS cluster in the AWS Console. Select the **Overview** tab on the **Cluster Info** page.
2. In the **Kubernetes version settings** section, select **Manage**.
3. Select **Extended support** and then **Save changes**.

## Enable EKS extended support (AWS CLI)

1. Verify the AWS CLI is installed and you are logged in. [Learn how to update and install the AWS CLI.](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
2. Determine the name of your EKS cluster.
3. Run the following command:

```
 aws eks update-cluster-config \
--name <cluster-name> \
--upgrade-policy supportType=EXTENDED
```

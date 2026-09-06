

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Add flexibility to plan Kubernetes version upgrades by enabling EKS extended support
<a name="enable-extended-support"></a>

This topic describes how to set the *upgrade policy* of an EKS cluster to enable extended support. The upgrade policy of an EKS cluster determines what happens when a cluster reaches the end of the standard *support period*. If a cluster upgrade policy has extended support enabled, it will enter the extended support period at the end of the standard support period. The cluster will not be automatically upgraded at the end of the standard support period.

Clusters actually in the *extended support period* incur higher costs. If a cluster merely has the upgrade policy set to enable extended support, and is otherwise in the *standard support period*, it incurs standard costs.

If you create a cluster in the AWS console, it will have the upgrade policy set to disable extended support. If you create a cluster in another way, it will have the upgrade policy set to enable extended support. For example, clusters created with the AWS API have extended support enabled.

For more information about upgrade policies, see [Cluster upgrade policy](https://docs.aws.amazon.com/eks/latest/userguide/view-upgrade-policy.html).

**Important**  
If you want your cluster to stay on its current Kubernetes version to take advantage of the extended support period, we strongly recommend enabling the extended support upgrade policy before the end of the standard support period for your cluster’s Kubernetes version. You can enable extended support after the standard support period ends. However, Amazon EKS cannot guarantee that the change will take effect if an automatic upgrade has already been initiated for your cluster.  
Once your cluster has entered extended support, you cannot disable it. You can only disable extended support for clusters that are running a Kubernetes version in standard support.  
If you do not enable extended support, your cluster will be automatically upgraded after the end of the standard support period.

## Enable EKS extended support (AWS Console)
<a name="enable-support-policy-console"></a>

1. Navigate to your EKS cluster in the AWS Console. Select the **Overview** tab on the **Cluster Info** page.

1. In the **Kubernetes version settings** section, select **Manage**.

1. Select **Extended support** and then **Save changes**.

## Enable EKS extended support (AWS CLI)
<a name="enable-support-policy-cli"></a>

1. Verify the AWS CLI is installed and you are logged in. [Learn how to update and install the AWS CLI.](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) 

1. Determine the name of your EKS cluster.

1. Run the following command:

   ```
   aws eks update-cluster-config \
   --name <cluster-name> \
   --upgrade-policy supportType=EXTENDED
   ```
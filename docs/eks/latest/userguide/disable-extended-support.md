**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Prevent increased cluster costs by disabling EKS extended support

This topic describes how to set the _upgrade policy_ of an EKS cluster to disable extended support. The upgrade policy of an EKS cluster determines what happens when a cluster reaches the end of the standard _support period_. If a cluster upgrade policy has extended support disabled, it will be automatically upgraded to the next Kubernetes version.

For more information about upgrade policies, see [Cluster upgrade policy](view-upgrade-policy.md "view-upgrade-policy.md").

###### Important

You cannot disable extended support once your cluster has entered it. You can only disable extended support for clusters on standard support.

AWS recommends upgrading your cluster to a version in the standard support period.

## Disable EKS extended support (AWS Console)

1. Navigate to your EKS cluster in the AWS Console. Select the **Overview** tab on the **Cluster Info** page.
2. In the **Kubernetes version setting** section, select **Manage**.
3. Select **Standard support** and then **Save changes**.

## Disable EKS extended support (AWS CLI)

1. Verify the AWS CLI is installed and you are logged in. [Learn how to update and install the AWS CLI.](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
2. Determine the name of your EKS cluster.
3. Run the following command:

```
 aws eks update-cluster-config \
--name <cluster-name> \
--upgrade-policy supportType=STANDARD
```

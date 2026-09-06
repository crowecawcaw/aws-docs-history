

# Manage associations for a VPC Lattice service
<a name="service-associations"></a>

When you associate a service with the service network, it enables clients (resources in a VPC associated with the service network), to make requests to this service. You can associate services that are in your account or services that are shared with you from different accounts. This step is optional when creating the service. However, after creation, the service can't communicate with other services until you associate it with a service network. Service owners can associate their services to the service network if their account has the required access. For more information, see [How VPC Lattice works](how-it-works.md).

**To manage service network associations using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **VPC Lattice**, choose **Services**.

1. Select the name of the service to open its details page.

1. Choose the **Service network associations** tab.

1. To create an association, do the following:

   1. Choose **Create associations**.

   1. Select a service network from **VPC Lattice service networks**. To create a service network, choose **Create a VPC Lattice network**.

   1. (Optional) To add a tag, expand **Service association tags**, choose **Add new tag**, and enter a tag key and tag value.

   1. Choose **Save changes**.

1. To delete an association, select the check box for the association and then choose **Actions**, **Delete network associations**. When prompted for confirmation, enter **confirm** and then choose **Delete**.

**To create a service network association using the AWS CLI**  
Use the [create-service-network-service-association](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/create-service-network-service-association.html) command.

**To delete a service network association using the AWS CLI**  
Use the [delete-service-network-service-association](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/delete-service-network-service-association.html) command.


# Delete a VPC Lattice service network
<a name="delete-service-network"></a>

Before you can delete a service network, you must first delete all associations that the service network might have with any service, resource configuration, VPC, or VPC endpoint. When you delete a service network, we also delete all resources related to the service network, such as the resource policy, auth policy, and access log subscriptions.

**To delete a service network using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **VPC Lattice**, choose **Service networks**.

1. Select the check box for the service network, and then choose **Actions**, **Delete service network**.

1. When prompted for confirmation, enter **confirm**, and then choose **Delete**.

**To delete a service network using the AWS CLI**  
Use the [delete-service-network](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/delete-service-network.html) command.
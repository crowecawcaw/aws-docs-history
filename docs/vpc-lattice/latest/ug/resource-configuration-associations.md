# Manage associations for a VPC Lattice

resource configuration

Consumer accounts with which you share a resource configuration with and clients in
your account can access the resource configuration either directly using a VPC endpoint
of type resource or through a VPC endpoint of type service-network. As a result your
resource configuration will have endpoint associations and service network
associations.

## Manage service network

associations

Create or delete a service network association.

###### Note

If you receive an access-denied message while creating the association between
the service network and resource configuration, check your AWS RAM policy version
and ensure that it is version 2. For more information, see the [AWS RAM user guide](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md").

###### To manage a service-network association using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **PrivateLink and
   Lattice**, choose **Resource
   configurations**.
3. Select the name of the resource configuration to open its details
   page.
4. Select **Service network associations** tab.
5. Choose **Create associations**.
6. Select a service network from **VPC Lattice service
   networks**. To create a service network, choose
   **Create a VPC Lattice network**.
7. (Optional) To add a tag, expand **Service association
   tags**, choose **Add new tag**, and enter a
   tag key and tag value.
8. Choose **Save changes**.
9. To delete an association, select the check box for the association and
   then choose **Actions**, **Delete**. When
   prompted for confirmation, enter `confirm` and then
   choose **Delete**.

###### To create a service network association using the AWS CLI

Use the [create-service-network-resource-association](../../../cli/latest/reference/vpc-lattice/create-service-network-resource-association.md "../../../cli/latest/reference/vpc-lattice/create-service-network-resource-association.md") command.

###### To delete a service network association using the AWS CLI

Use the [delete-service-network-resource-association](../../../cli/latest/reference/vpc-lattice/delete-service-network-resource-association.md "../../../cli/latest/reference/vpc-lattice/delete-service-network-resource-association.md") command.

## Manage VPC endpoint

associations

Manage a VPC endpoint association.

###### To manage a VPC endpoint association using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **PrivateLink and
   Lattice**, choose **Resource
   configurations**.
3. Select the name of the resource configuration to open its details
   page.
4. Choose the **Endpoint associations** tab.
5. Select the association ID to open its details page. From here, you can
   modify or delete the association.
6. To create a new endpoint association, go to **PrivateLink and
   Lattice** in the left navigation pane and choose
   **Endpoints**.
7. Choose **Create endpoints**.
8. Select the resource configuration you want to connect to your VPC.
9. Select the VPC, subnets and security groups.
10. (Optional) To tag you VPC endpoint, choose **Add new
    tag**, and enter a tag key and tag value.
11. Choose **Create endpoint**.

###### To create a VPC endpoint association using the AWS CLI

Use the [create-vpc-endpoint](../../../cli/latest/reference/ec2/create-vpc-endpoint.md "../../../cli/latest/reference/ec2/create-vpc-endpoint.md") command.

###### To delete a VPC endpoint association using the AWS CLI

Use the [delete-vpc-endpoint](../../../cli/latest/reference/ec2/delete-vpc-endpoint.md "../../../cli/latest/reference/ec2/delete-vpc-endpoint.md") command.

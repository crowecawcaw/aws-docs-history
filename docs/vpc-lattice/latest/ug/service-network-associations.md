# Manage the associations for a VPC Lattice

service network

When you associate a service or a resource configuration with the service network, it
enables clients in VPCs connected to the service network, to make requests to the
service and resource configuration. When you connect a VPC with the service network, it
enables all the targets within that VPC to be clients and communicate with other
services and resource configurations in the service network.

###### Contents

- [Manage service
  associations](#service-network-service-associations "#service-network-service-associations")
- [Manage resource
  configuration associations](#service-network-resource-config-associations "#service-network-resource-config-associations")
- [Manage VPC associations](#service-network-vpc-associations "#service-network-vpc-associations")
- [Manage VPC endpoint
  associations](#service-network-vpc-endpoint-associations "#service-network-vpc-endpoint-associations")

## Manage service

associations

You can associate services that reside in your account or services that are shared
with you from different accounts. This is an optional step while creating a service
network. However, a service network is not fully functional until you associate a
service. Service owners can associate their services to a service network if their
account has the required access. For more information, see [Identity-based policy examples
for VPC Lattice](security_iam_id-based-policies.md#security_iam_id-based-policy-examples "security_iam_id-based-policies.md#security_iam_id-based-policy-examples").

When you delete a service association, the service can no longer connect to other
services in the service network.

###### To manage service associations using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Service networks**.
3. Select the name of the service network to open its details page.
4. Choose the **Service associations** tab.
5. To create an association, do the following:
   1. Choose **Create associations**.
   2. Select a service from **Services**. To create a
      service, choose **Create an Amazon VPC Lattice
      service**.
   3. (Optional) To add a tag, expand **Service association
      tags**, choose **Add new tag**, and
      enter a tag key and tag value.
   4. Choose **Save changes**.

6. To delete an association, select the check box for the association and
   then choose **Actions**, **Delete service
   associations**. When prompted for confirmation, enter
   `confirm` and then choose
   **Delete**.

###### To create a service association using the AWS CLI

Use the [create-service-network-service-association](../../../cli/latest/reference/vpc-lattice/create-service-network-service-association.md "../../../cli/latest/reference/vpc-lattice/create-service-network-service-association.md") command.

###### To delete a service association using the AWS CLI

Use the [delete-service-network-service-association](../../../cli/latest/reference/vpc-lattice/delete-service-network-service-association.md "../../../cli/latest/reference/vpc-lattice/delete-service-network-service-association.md") command.

## Manage resource

configuration associations

A resource configuration is a logical object that represents either a single
resource or a group of resources. You can associate resource configurations that
reside in your account or resource configurations that are shared with you from
different accounts. This is an optional step while creating a service network.
Resource configuration owners can associate their resource configurations to a
service network if their account has the required access. For more information, see
[Identity-based policy examples for VPC Lattice](security_iam_id-based-policies.md#security_iam_id-based-policy-examples "security_iam_id-based-policies.md#security_iam_id-based-policy-examples").

### Manage

associations between service networks and resource configurations

You can create or delete the association between the service network and
resource configuration.

###### To manage resource configuration associations using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **PrivateLink and
   Lattice**, choose **Service
   networks**.
3. Select the name of the service network to open its details
   page.
4. Choose the **Resource configuration associations**
   tab.
5. To create an association, do the following:
   1. Choose **Create associations**.
   2. Select a resource configuration from **Resource
      configurations**. Choose **Create an Amazon
      VPC Lattice resource configuration.**.
   3. (Optional) To add a tag, expand **Service association
      tags**, choose **Add new tag**,
      and enter a tag key and tag value.
   4. Choose **Save changes**.

6. To delete an association, select the check box for the association and
   then choose **Actions**, **Delete**.
   When prompted for confirmation, enter `confirm` and
   then choose **Delete**.

###### To create a resource configuration association using the AWS CLI

Use the [create-service-network-resource-association](../../../cli/latest/reference/vpc-lattice/create-service-network-resource-association.md "../../../cli/latest/reference/vpc-lattice/create-service-network-resource-association.md") command.

###### To delete a resource configuration association using the AWS CLI

Use the [delete-service-network-resource-association](../../../cli/latest/reference/vpc-lattice/delete-service-network-resource-association.md "../../../cli/latest/reference/vpc-lattice/delete-service-network-resource-association.md") command.

## Manage VPC associations

Clients can send requests to services and resources specified in resource
configurations associated with a service network if the client is in VPCs associated
with the service network. Client traffic that traverses a VPC peering connection or
a transit gateway is only allowed through a service network using a VPC endpoint of
type service network.

Associating a VPC is an optional step when you create a service network. Network
owners can associate VPCs to a service network if their account has the required
access. For more information, see [Identity-based policy examples
for VPC Lattice](security_iam_id-based-policies.md#security_iam_id-based-policy-examples "security_iam_id-based-policies.md#security_iam_id-based-policy-examples").

When you a delete a VPC association, clients in the VPCs can no longer connect to
services in the service network.

###### To manage VPC associations using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Service networks**.
3. Select the name of the service network to open its details page.
4. Choose the **VPC associations** tab.
5. To create a VPC association, do the following:
   1. Choose **Create VPC associations**.
   2. Choose **Add VPC association**.
   3. Select a VPC from **VPC** and select up to five
      security groups from **Security groups**. To create
      a security group, choose **Create new security
      group**.
   4. (Optional) To add a tag, expand **VPC association
      tags**, choose **Add new tag**, and
      enter a tag key and tag value.
   5. Choose **Save changes**.

6. To edit the security groups for an association, select the check box for
   the association and then chose **Actions**, **Edit
   security groups**. Add and remove security groups as
   needed.
7. To delete an association, select the check box for the association and
   then choose **Actions**, **Delete VPC
   associations**. When prompted for confirmation, enter
   `confirm` and then choose
   **Delete**.

###### To create a VPC association using the AWS CLI

Use the [create-service-network-vpc-association](../../../cli/latest/reference/vpc-lattice/create-service-network-vpc-association.md "../../../cli/latest/reference/vpc-lattice/create-service-network-vpc-association.md") command.

###### To update the security groups for a VPC association using the AWS CLI

Use the [update-service-network-vpc-association](../../../cli/latest/reference/vpc-lattice/update-service-network-vpc-association.md "../../../cli/latest/reference/vpc-lattice/update-service-network-vpc-association.md") command.

###### To delete a VPC association using the AWS CLI

Use the [delete-service-network-vpc-association](../../../cli/latest/reference/vpc-lattice/delete-service-network-vpc-association.md "../../../cli/latest/reference/vpc-lattice/delete-service-network-vpc-association.md") command.

## Manage VPC endpoint

associations

Clients can send requests to services and resources specified in resource configurations over a VPC
endpoint (powered by AWS PrivateLink) in their VPC. A VPC endpoint of type
_service network_ connects a VPC to a service network. Client
traffic that comes from outside the VPC over a VPC peering connection, Transit
Gateway, Direct Connect, or VPN can use the VPC endpoint to reach services and
resource configurations. With VPC endpoints, you can connect a VPC to multiple
service networks. When you create a VPC endpoint in a VPC, IP addresses from the VPC (and not IP addresses from the [managed prefix list](security-groups.md#managed-prefix-list "security-groups.md#managed-prefix-list")) are used to establish connectivity to the service network.

###### To manage VPC endpoint associations using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Service networks**.
3. Select the name of the service network to open its details page.
4. Choose the **Endpoint associations** tab to view the VPC
   endpoints connected to your service network.
5. Select the Endpoint ID of the VPC endpoint to open its details page. Then
   modify or delete the VPC endpoint association.

###### To create a new VPC endpoint association using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Endpoints**.
3. Choose **Create endpoints**.
4. For **Type**, choose **Service
   networks**.
5. Select the service network you want to connect to your VPC.
6. Select the VPC, subnets and security groups.
7. (Optional) To add a tag, expand **VPC association tags**,
   choose **Add new tag**, and enter a tag key and tag
   value.
8. Choose **Create endpoint**.

To learn more about VPC endpoint to how to connect to service networks, see [Access
service networks](../../../vpc/latest/privatelink/privatelink-access-service-networks.md "../../../vpc/latest/privatelink/privatelink-access-service-networks.md") in the _AWS PrivateLink user
guide_.

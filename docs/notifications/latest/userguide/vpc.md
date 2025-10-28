# Connecting to AWS User Notifications with interface VPC endpoints

You can use AWS PrivateLink to create a private connection between your virtual private cloud (VPC) and User Notifications so that you can access the service as if it were in your own VPC.
This doesn't require the use of an internet gateway, network address translation (NAT) device, virtual private network (VPN) connection, or AWS Direct Connect connection.
You establish this private connection by creating an interface endpoint that is powered by AWS PrivateLink.
An interface endpoint is an elastic network interface with a private IP address
that serves as an entry point for traffic destined to a supported AWS service. Instances in your VPC don't need public IP addresses to access User Notifications. For more information, see [Amazon Virtual Private Cloud](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md")
and [Interface VPC Endpoints (AWS PrivateLink)](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint").

###### Topics

- [Creating an interface VPC endpoints for User Notifications](#creating-vpc-endpoint "#creating-vpc-endpoint")
- [Creating a VPC endpoint policy for User Notifications](#creating-vpc-endpoint-policy "#creating-vpc-endpoint-policy")

## Creating an interface VPC endpoints for User Notifications

You can create a VPC endpoint for User Notifications using the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see
[Creating an interface Endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for User Notifications using the following service name:

- `com.amazonaws.`region`.notifications`

Create a VPC endpoint for User Notifications Contacts using the following service name:

- `com.amazonaws.`region`.notifications-contacts`

###### Note

The User Notifications Contacts service VPC endpoint is only supported in the us-east-1 (N. Virginia) Region.

If you enable private domain name system (DNS) for the endpoint, you can make API requests to User Notifications using its default DNS name.
For example, `notifications.us-east-1.api.aws`. For more information, see
[Accessing a service through an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#access-service-though-endpoint "../../../vpc/latest/privatelink/create-interface-endpoint.md#access-service-though-endpoint")
in the _Amazon VPC User Guide_.

## Creating a VPC endpoint policy for User Notifications

You can attach an endpoint policy to your VPC endpoint that controls access to User Notifications. The policy specifies the following information:

- The principal that can perform actions
- The actions that can be performed
- The resources on which actions can be performed

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md")
in the _Amazon VPC User Guide_.

### Example: VPC endpoint policy for User Notifications get and list actions

The following endpoint policy grants access to get and list actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "notifications:Get*",
 "notifications:List*",
 "notifications-contacts:Get*",
 "notifications-contacts:List*"

 ],
 "Resource": "*"
 }
 ]
}`

```

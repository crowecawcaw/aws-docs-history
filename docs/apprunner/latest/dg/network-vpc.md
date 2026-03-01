# Enabling VPC access for outgoing traffic

By default, your AWS App Runner application can send messages to public endpoints. This includes
your own solutions, AWS services, and any other public website or web service. Your
application can even send messages to public endpoints of applications that run in a VPC from
[Amazon Virtual Private Cloud](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") (Amazon VPC). If you don't configure a VPC when you
launch your environment, App Runner uses the default VPC, which is public.

You can choose to launch your environment in a custom VPC to customize networking and
security settings for outgoing traffic. You can enable your AWS App Runner service to access
applications that run in a private VPC from Amazon Virtual Private Cloud (Amazon VPC). After you do this, your
application can connect with and send messages to other applications that are hosted in an
[Amazon Virtual Private Cloud](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") (Amazon VPC). Examples are an Amazon RDS database,
Amazon ElastiCache, and other private services that are hosted in a private VPC.

## VPC Connector

You can associate your service with a VPC by creating a VPC endpoint from the App Runner
console, called VPC Connector. To create a VPC Connector, specify the VPC, one or more
subnets, and optionally one or more security groups. After you configure a VPC Connector, you
can use it with one or more App Runner services.

### One-time latency

If you configure your App Runner service with a custom VPC connector for outbound traffic, it
may experience a one-time startup latency of two to five minutes. The startup process waits
until the VPC Connector is ready to connect to other resources before it sets the service
status to _Running_. You can configure a service with a
custom VPC connector when you first create it, or you can do so afterward by doing a service
update.

Note that if you reuse the _same_ VPC connector
configuration for another service there wont be any latency. The VPC connector configuration
is based on the security group and subnet combination. For a given VPC connector
configuration, the latency only happens once, during the initial creation of the VPC
Connector Hyperplane ENIs (elastic network interfaces).

### More about Custom VPC connectors and AWS Hyperplane

The VPC connectors in App Runner are based on AWS Hyperplane, the internal Amazon network
system that's behind several AWS resources, such as [Network Load Balancer](../../../elasticloadbalancing/latest/network/introduction.md "../../../elasticloadbalancing/latest/network/introduction.md"), [NAT Gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md"), and [AWS PrivateLink](../../../vpc/latest/privatelink.md "../../../vpc/latest/privatelink.md"). The AWS Hyperplane technology
provides high throughput and low latency capabilities, along with a higher degree of
sharing. A Hyperplane ENI is created in your subnets when you create a VPC connector and
associate it with your service. A VPC connector configuration is based on a security group
and subnet combination, and you can reference the same VPC Connector across multiple App Runner
services. As a result, the underlying Hyperplane ENIs are shared across your App Runner services.
This sharing is feasible, even as you scale up the number of tasks required to handle the
request load, and results in more efficient utilization of the IP space in your VPC. For
more information, see [Deep Dive on AWS App Runner
VPC Networking](https://aws.amazon.com/blogs/containers/deep-dive-on-aws-app-runner-vpc-networking/ "https://aws.amazon.com/blogs/containers/deep-dive-on-aws-app-runner-vpc-networking/") in the _AWS Container Blog_.

## Subnet

Each subnet is in a specific Availability Zone. For high availability, we recommend that
you select subnets across at least three Availability Zones. If the Region has less than three
Availability Zones, we recommend you select your subnets across all the supported Availability
Zones.

When selecting a subnet for your VPC, ensure that you choose a private subnet, not a
public subnet. This is because, when you create a VPC Connector, the App Runner service creates a
Hyperplane ENI in each of the subnets. Each Hyperplane ENI is assigned a private IP address
only and is tagged with a tag of the _AWSAppRunnerManaged_ key. If you
choose a public subnet, errors will occur when running your App Runner service. However, if your
service needs to access some services that are on the internet or other public AWS services,
see [Considerations when selecting a subnet](#network-vpc.considerations-subnet "#network-vpc.considerations-subnet").

### Considerations when selecting a subnet

- When you connect your service to a VPC, the outbound traffic doesn't have access to
  the public internet. All outbound traffic from your application is directed through the
  VPC that your service is connected to. All networking rules for the VPC apply to the
  outbound traffic of your application. This means that your services can't access the
  public internet and AWS APIs. To gain access, do one of the following:
  - Connect the subnets to the internet through a [NAT Gateway.](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md")
  - Set up [VPC
    endpoints](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") for the AWS services that you want to access. Your service
    stays within the Amazon VPC by using AWS PrivateLink.

- Some Availability Zones in some AWS Regions don't support the subnets that can be
  used with App Runner services. If you choose subnets in these Availability Zones, your service
  fails to be created or updated. For these situations, App Runner provides a detailed error
  message pointing to the unsupported subnets and Availability Zones. When this occurs,
  troubleshoot by removing the unsupported subnets from your request, and then try again.
- The subnets you select must all have the same IP address type, either IPv4 or
  dual-stack.

## Security group

You can optionally specify the security groups that App Runner uses to access AWS under the
specified subnets. If you don't specify security groups, App Runner uses the default security group
of the VPC. The default security group allows all outbound traffic.

Adding a security group provides an additional layer of security to the VPC Connectors,
giving you more control over the network traffic. The VPC Connector is only used for outbound
communication from your application. You use outbound rules to allow communication to the
desired destination endpoints. You must also ensure that any security groups that are
associated with the destination resource have the appropriate inbound rules. Otherwise, these
resources can't accept traffic that comes from the VPC Connector security groups.

###### Note

When you associate your service with a VPC, the following traffic isn't affected:

- Inbound traffic – Incoming messages that your
  application receives are unaffected by an associated VPC. The messages are routed
  through the public domain name that's associated with your service and don't interact
  with the VPC.
- App Runner traffic – App Runner manages several actions on
  your behalf, such as pulling source code and images, pushing logs, and retrieving
  secrets. The traffic that these actions generate isn't routed through your VPC.

To know more about how AWS App Runner integrates with Amazon VPC, see [AWS App Runner
VPC Networking](https://aws.amazon.com/blogs/containers/deep-dive-on-aws-app-runner-vpc-networking/ "https://aws.amazon.com/blogs/containers/deep-dive-on-aws-app-runner-vpc-networking/").

## Manage VPC access

###### Note

If you create an outbound traffic VPC connector for a service, the service startup process that follows will experience a one-time latency. You can set
this configuration for a new service when you create it, or afterward, with a service update. For more information, see [One-time latency](#network-vpc.VPC-connector.latency "#network-vpc.VPC-connector.latency") in the _Networking with App Runner_
chapter of this guide.

Manage VPC access for your App Runner services using one of the following methods:

App Runner console
When you [create a service](manage-create.md "manage-create.md") using the App Runner
console, or when you [update its configuration
later](manage-configure.md "manage-configure.md"), you can choose to configure your outgoing traffic. Look for the
**Networking** configuration section on the console page. For
**Outgoing network traffic**, choose in the following:

- **Public access**: To associate your service with public
  endpoints of other AWS services.
- **Custom VPC**: To associate your service with a VPC from
  Amazon VPC. Your application can connect with and send messages to other applications
  that are hosted in an Amazon VPC.

###### To enable Custom VPC

1. Open the [App Runner console](https://console.aws.amazon.com/apprunner "https://console.aws.amazon.com/apprunner"), and in the **Regions** list, select your AWS Region.
2. Go to **Networking** section under **Configure
   service**.

![App Runner console configuration page showing networking options](images/network-vpc-config-network.png) 3. Choose **Custom VPC**, for **Outgoing network
traffic**. 4. In the navigation pane, choose **VPC connector**.

If you created the VPC connectors, the console displays a list of VPC connectors
in your account. You can choose an existing VPC connector and choose
**Next** to review your configuration. Then, move to the last
step. Alternatively, you can add a new VPC connector using the following
steps. 5. Choose **Add new** to create a new VPC connector for your
service.

Then, the **Add new VPC connector** dialog box opens.

![App Runner console showing Add new VPC connector dialog](images/network-vpc-add-new.png) 6. Enter a name for your VPC connector and select the required VPC from the
available list. 7. For **Subnets** select one subnet for each Availability Zone
that you plan to access the App Runner service from. For better availability, choose three
subnets. Or, if there are less than three subnets, choose all available
subnets.

###### Note

    * Make sure you assign *private* subnets to the VPC
     connector. If you assign public subnets to VPC connector, your service fails
     to create or rolls back automatically during an update.
    * If your outgoing traffic is dual-stack, make sure that all of the subnets
     that you select are configured for dual-stack in the VPC Console.

8. (Optional) For **Security group**, select the security groups
   to associate with the endpoint network interfaces.
9. (Optional) To add a tag, choose **Add new tag** and enter the
   tag key and the tag value.
10. Choose **Add**.

The details of the VPC connector you created appear under **VPC
connector**. 11. Choose **Next** to review your configuration, and then choose
**Create and deploy**.

App Runner creates a VPC connector resource for you, and then associates it with your
service. If the service is successfully created, the console shows the service
dashboard, with a **Service overview** of the new service.

App Runner API or AWS CLI
When you call the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") or [UpdateService](../api/API_UpdateService.md "../api/API_UpdateService.md") App Runner API actions, use the `EgressConfiguration`
member of the `NetworkConfiguration` parameter to specify a VPC connector
resource for your service.

Use the following App Runner API actions to manage your VPC Connector resources.

- [CreateVpcConnector](../api/API_CreateVpcConnector.md "../api/API_CreateVpcConnector.md")
  – Creates a new VPC connector.
- [ListVpcConnectors](../api/API_ListVpcConnectors.md "../api/API_ListVpcConnectors.md")
  – Returns a list of the VPC connectors that are associated with your
  AWS account. The list includes full descriptions.
- [DescribeVpcConnector](../api/API_DescribeVpcConnector.md "../api/API_DescribeVpcConnector.md") – Returns a full description of a VPC
  connector.
- [DeleteVpcConnector](../api/API_DeleteVpcConnector.md "../api/API_DeleteVpcConnector.md")
  – Deletes a VPC connector. If you reach the VPC connector
  quota for your AWS account, you might need to delete unnecessary VPC
  connectors.

To deploy an application on App Runner that has outbound access to a VPC, you must first
create a VPC Connector. You can do this by specifying one or more subnets and security
groups to associate with the application. You can then reference the VPC Connector in
the **Create** or **UpdateService** through the CLI,
as illustrated in the following example:

```

            cat > vpc-connector.json <<EOF
{
"VpcConnectorName": "my-vpc-connector",
"Subnets": [
"subnet-a",
"subnet-b",
"subnet-c"
],
"SecurityGroups": [
"sg-1",
"sg-2"
]
}
EOF

aws apprunner create-vpc-connector \
--cli-input-json file:///vpc-connector.json

cat > service.json <<EOF

{
"ServiceName": "my-vpc-connected-service",
"SourceConfiguration": {
"ImageRepository": {
"ImageIdentifier": "<ecr-image-identifier> ",
"ImageConfiguration": {
"Port": "8000"
},
"ImageRepositoryType": "ECR"
}
},
"NetworkConfiguration": {
"EgressConfiguration": {
"EgressType": "VPC",
"VpcConnectorArn": "arn:aws:apprunner:..../my-vpc-connector"
}
}
}
EOF

aws apprunner create-service \
--cli-input-json file:///service.js

```

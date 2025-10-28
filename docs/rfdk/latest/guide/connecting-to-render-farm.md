# Connecting To Render Farm

##

###### Important

On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/ "https://aws.amazon.com/deadline-cloud/") for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com "mailto:support@awsthinkbox.zendesk.com") or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html "https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html").

There are different ways to securely connect to your render farm from your network.
Please visit [Network-to-Amazon VPC connectivity options](../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md") to find the option that suits you best.

We recommend setting up [AWS Site-to-Site VPN](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md") for site connectivity,
[AWS Client VPN](../../../vpn/latest/clientvpn-admin/what-is.md "../../../vpn/latest/clientvpn-admin/what-is.md") for individual machine connectivity,
and [AWS Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/") for customers that need extremely high-throughput low-latency connectivity.

Also, you can use [VPC peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") if you are working on an EC2 instance and want to connect to your render farm from there.

## Connecting With Site-to-Site VPN

To set up a VPN connection between your network and the VPC created with RFDK you need to add the options listed below to the `Vpc` construct in your RFDK application code.
Substitute `customer-prefix-cidr-range` with an IP range of your network and `rfdk-vpc-cidr-range` with a CIDR range of the VPC you use in your RFDK application.
Also, substitute `customer-gateway-ip` with a public IP address of the gateway of your network.

###### Important

Ensure that your network and VPC do not have overlapping IPv4 CIDR blocks. Otherwise, a Site-to-Site VPN connection may not work.
See [Site-to-Site VPN limitations](../../../vpn/latest/s2svpn/VPC_VPN.md#site-to-site-limitations "../../../vpn/latest/s2svpn/VPC_VPN.md#site-to-site-limitations") for more details.

Python

```
vpc = ec2.Vpc(self, "Vpc",
    # for example, replace rfdk-vpc-cidr-range with 10.100.0.0/16
    cidr="`rfdk-vpc-cidr-range`",
    vpn_gateway=True,
    vpn_connections={
        "static": ec2.VpnConnectionOptions(
            # for example, replace customer-gateway-ip with 10.200.0.10
            ip="`customer-gateway-ip`",
            static_routes=[
                # for example, replace customer-prefix-cidr-range with 10.200.0.0/16
                "`customer-prefix-cidr-range`"
            ]
        )
    },
    vpn_route_propagation=[
        ec2.SubnetSelection(
            subnet_type=ec2.SubnetType.PRIVATE
        )
    ]
)
```

TypeScript

```
const vpc = new ec2.Vpc(this, 'Vpc', {
  // for example, replace rfdk-vpc-cidr-range with 10.100.0.0/16
  cidr: "`rfdk-vpc-cidr-range`",
  vpnGateway: true,
  vpnConnections: {
      static: {
        // for example, replace customer-gateway-ip with 10.200.0.10
        ip: "`customer-gateway-ip`",
        staticRoutes: [
          // for example, replace customer-prefix-cidr-range with 10.200.0.0/16
          "`customer-prefix-cidr-range`",
        ],
      },
  },
  vpnRoutePropagation: [
    {
      subnetType: ec2.SubnetType.PRIVATE,
    },
  ],
});
```

The above code creates a VPC which acts as an AWS end of the VPN tunnel with CIDR range `rfdk-vpc-cidr-range`.
Besides of creating the VPC it will:

- Create private subnets and route tables associated with these subnets. These subnets will be used by the render queue load balancer.
- Create [Virtual Private Gateway](../../../vpn/latest/s2svpn/SetUpVPNConnections.md#vpn-create-target-gateway "../../../vpn/latest/s2svpn/SetUpVPNConnections.md#vpn-create-target-gateway") (let’s call it `VGW-RFDK`) and attach it to the VPC.
- Create [Customer Gateway](../../../vpn/latest/s2svpn/how_it_works.md#CustomerGateway "../../../vpn/latest/s2svpn/how_it_works.md#CustomerGateway") (let’s call it `CGW-RFDK`) with static routing and customer end public IP as `customer-gateway-ip`.
- Create a `Site-to-Site VPN Connection` with:
  - `Target Type` as `Virtual Private Gateway`.
  - Selected `VGW-RFDK` and `CGW-RFDK`.
  - `Static` routing and `IP Prefix` range `customer-prefix-cidr-range`.

- Enable `Route Propagation` to `VGW-RFDK` for route tables associated with private subnets in VPC.

###### Note

You can download configuration for the software VPN you use.
Once your app is deployed, log into AWS Web Console and navigate to VPC service in the region where you deployed the render farm.
Go to `Site-to-Site VPN Connections`, select the connection created by RFDK and press `Download Configuration`.
Alternatively, you can use `CloudFormation` service and select the stack deployed with RFDK. Switch to `Resources` tab and search for `VPNConnection`.
From there you can navigate directly to the deployed VPN Connection in the VPC console.

You can modify the above code to best meet your specific needs.
See [Vpc construct API](../../../cdk/api/latest/docs/@aws-cdk_aws-ec2.md "../../../cdk/api/latest/docs/@aws-cdk_aws-ec2.md") to learn how to configure your VPC.

Also, you should [allow the connection from the machines in your network to the render queue](#allowing-connection-to-the-render-queue "#allowing-connection-to-the-render-queue").

## Connecting With AWS Client VPN

You can use a few CDK constructs to establish the connection to the render farm with AWS Client VPN.
This tutorial provides some CDK code examples similar to the corresponding steps in the [Getting started with Client VPN](../../../vpn/latest/clientvpn-admin/cvpn-getting-started.md "../../../vpn/latest/clientvpn-admin/cvpn-getting-started.md") guide.

Use [CfnClientVpnEndpoint](../../../cdk/api/latest/python/aws_cdk.aws_ec2/CfnClientVpnEndpoint.md "../../../cdk/api/latest/python/aws_cdk.aws_ec2/CfnClientVpnEndpoint.md") to create a Client VPN endpoint.
The following example assumes that you have already [generated server and client certificates and keys](../../../vpn/latest/clientvpn-admin/cvpn-getting-started.md#cvpn-getting-started-certs "../../../vpn/latest/clientvpn-admin/cvpn-getting-started.md#cvpn-getting-started-certs") and uploaded them to AWS Certificate Manager (ACM).
Substitute `client-certificate-arn` and `server-certificate-arn` with the ARN of your client and server certificates, respectively.
Also, substitute `customer-prefix-cidr-range` with an IP range of your network.

Below, we explicitly create a security group that is applied to the Client VPN endpoint.
Later, you will allow connection to the render queue from this security group.

Python

```
AuthReq = ec2.CfnClientVpnEndpoint.ClientAuthenticationRequestProperty

security_group = ec2.SecurityGroup(self, 'SG-VPN-RFDK', vpc=vpc)

endpoint = ec2.CfnClientVpnEndpoint(self, 'ClientVpnEndpointRFDK',
    authentication_options=[
        ec2.CfnClientVpnEndpoint.ClientAuthenticationRequestProperty(
            type="certificate-authentication",
            mutual_authentication=AuthReq(
                client_root_certificate_chain_arn="`client-certificate-arn`"
            )
        )
    ],
    # for example, replace customer-prefix-cidr-range with 10.200.0.0/16
    client_cidr_block="`customer-prefix-cidr-range`",
    connection_log_options=ec2.CfnClientVpnEndpoint.ConnectionLogOptionsProperty(
        enabled=False
    ),
    security_group_ids=[
        security_group.security_group_id
    ],
    server_certificate_arn="`server-certificate-arn`",
    vpc_id=vpc.vpc_id
);
```

TypeScript

```
import { CfnClientVpnTargetNetworkAssociation, CfnClientVpnEndpoint, CfnClientVpnAuthorizationRule, CfnClientVpnRoute, SecurityGroup, Vpc } from '@aws-cdk/aws-ec2';
...
const securityGroup = new SecurityGroup(this, 'SG-VPN-RFDK', {
  vpc,
});

const endpoint = new CfnClientVpnEndpoint(this, 'ClientVpnEndpointRFDK', {
  authenticationOptions: [{
    type: "certificate-authentication",
    mutualAuthentication: {
      clientRootCertificateChainArn: '`client-certificate-arn`',
    },
  }],
  // for example, replace customer-prefix-cidr-range with 10.200.0.0/16
  clientCidrBlock: '`customer-prefix-cidr-range`',
  connectionLogOptions: {
    enabled: false,
  },
  securityGroupIds: [
    securityGroup.securityGroupId
  ],
  serverCertificateArn: '`server-certificate-arn`',
  vpcId: vpc.vpcId,
});
```

To create network associations for the subnets of the VPN use [CfnClientVpnTargetNetworkAssociation](../../../cdk/api/latest/python/aws_cdk.aws_ec2/CfnClientVpnTargetNetworkAssociation.md "../../../cdk/api/latest/python/aws_cdk.aws_ec2/CfnClientVpnTargetNetworkAssociation.md").

Python

```
for i, subnet in enumerate(vpc.private_subnets):
    ec2.CfnClientVpnTargetNetworkAssociation(self, 'ClientVpnNetworkAssociation' + str(i),
        client_vpn_endpoint_id=endpoint.ref,
        subnet_id=subnet.subnet_id
    )
```

TypeScript

```
let i = 0;
vpc.privateSubnets.map(subnet => {
  new CfnClientVpnTargetNetworkAssociation(this, `ClientVpnNetworkAssociation${i}`, {
    clientVpnEndpointId: endpoint.ref,
    subnetId: subnet.subnetId,
  });
  i++;
});
```

Finally, use [CfnClientVpnAuthorizationRule](../../../cdk/api/latest/python/aws_cdk.aws_ec2/CfnClientVpnAuthorizationRule.md "../../../cdk/api/latest/python/aws_cdk.aws_ec2/CfnClientVpnAuthorizationRule.md") to create VPN authorization rules.

Substitute `target_network-cidr-block` with the CIDR of the network for which you want to allow access.
For example, to allow access to the entire VPC, specify the IPv4 CIDR block of the VPC.

Python

```
authorization_rule = ec2.CfnClientVpnAuthorizationRule(self, 'ClientVpnAuthRule',
    authorize_all_groups=True,
    client_vpn_endpoint_id=endpoint.ref,
    # for example, replace target_network-cidr-block with 10.100.0.0/16
    target_network_cidr="`target_network-cidr-block`"
)
```

TypeScript

```
new CfnClientVpnAuthorizationRule(this, 'ClientVpnAuthRule', {
  authorizeAllGroups: true,
  clientVpnEndpointId: endpoint.ref,
  // for example, replace target_network-cidr-block with 10.100.0.0/16
  targetNetworkCidr: "`target_network-cidr-block`",
});
```

Also, you should [allow the connection to the render queue](#allowing-connection-to-the-render-queue "#allowing-connection-to-the-render-queue") from the security group created earlier.
This will allow the machines that use Client VPN to connect to the render queue.

You will be able to [download the Client VPN endpoint configuration file](../../../vpn/latest/clientvpn-admin/cvpn-getting-started.md#cvpn-getting-started-config "../../../vpn/latest/clientvpn-admin/cvpn-getting-started.md#cvpn-getting-started-config") after you deploy your RFDK application.
Then you will be able to [connect to the Client VPN endpoint](../../../vpn/latest/clientvpn-admin/cvpn-getting-started.md#cvpn-getting-started-connect "../../../vpn/latest/clientvpn-admin/cvpn-getting-started.md#cvpn-getting-started-connect") using the configuration file.

## Connecting With VPC peering

You can use CDK to create a VPC peering connection between the VPC created by RFDK and the VPC in which you have your running instances.
Substitute `customer-prefix-cidr-range` with an IP range of your own VPC.

###### Important

Ensure that your VPCs do not have overlapping IPv4 CIDR blocks. Otherwise, a VPC peering connection will not work.
See [Creating and accepting a VPC peering connection](../../../vpc/latest/peering/create-vpc-peering-connection.md "../../../vpc/latest/peering/create-vpc-peering-connection.md") for more details.

Substitute `peer-vpc-region` and `peer-vpc-id` with the region and the VPC ID from where you will connect to the render farm deployed with RFDK.

For example, if you are working on an EC2 instance in `us-east-1` region, you can use the following commands to get these values:

```
PEER_VPC_REGION=us-east-1
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
INTERFACE=$(curl -H "X-aws-ec2-metadata-token: ${TOKEN}" --silent http://169.254.169.254/latest/meta-data/network/interfaces/macs/)
PEER_VPC_ID=$(curl -H "X-aws-ec2-metadata-token: ${TOKEN}" --silent http://169.254.169.254/latest/meta-data/network/interfaces/macs/${INTERFACE}/vpc-id)
echo $PEER_VPC_ID
```

Now you can use a CDK construct `CfnVPCPeeringConnection` to create a VPC peering connection in your RFDK application.

Python

```
vpc_peering_connection = ec2.CfnVPCPeeringConnection(self, 'VPCPeeringConnection',
    vpc_id=vpc.vpc_id,
    peer_vpc_id="`peer-vpc-id`",
    peer_region="`peer-vpc-region`"
)
```

TypeScript

```
const vpcPeeringConnection = new ec2.CfnVPCPeeringConnection(this, 'VPCPeeringConnection', {
  vpcId: vpc.vpcId,
  peerVpcId: "`peer-vpc-id`",
  peerRegion: "`peer-vpc-region`",
});
```

You will also need to update all the route tables associated with the subnets in both VPCs.
This can be done manually in the AWS Web Console after you deploy the RFDK application following the instructions in [Updating your Route tables for a VPC peering connection](../../../vpc/latest/peering/vpc-peering-routing.md "../../../vpc/latest/peering/vpc-peering-routing.md").
Alternatively, you can again use CDK and AWS CLI to simplify the process.

To update all the route tables in the RFDK VPC, add the following code to your RFDK application:

Python

```
for i, subnet in enumerate(vpc.private_subnets):
    ec2.CfnRoute(self, 'PeerRoute' + str(i),
        route_table_id=subnet.route_table.route_table_id,
        # for example, replace customer-prefix-cidr-range with 10.200.0.0/16
        destination_cidr_block="`customer-prefix-cidr-range`",
        vpc_peering_connection_id=vpc_peering_connection.ref
    )
```

TypeScript

```
let i = 0;
vpc.privateSubnets.map(subnet => {
  new ec2.CfnRoute(this, `PeerRoute${i}`, {
    routeTableId: subnet.routeTable.routeTableId,
    // for example, replace customer-prefix-cidr-range with 10.200.0.0/16
    destinationCidrBlock: "`customer-prefix-cidr-range`",
    vpcPeeringConnectionId: vpcPeeringConnection.ref,
  });
  i++;
});
```

Also, you should [allow the connection from the machines in your VPC to the render queue](#allowing-connection-to-the-render-queue "#allowing-connection-to-the-render-queue").

In order to update the route table in your other VPC, you can use AWS CLI commands.

There are multiple ways to get the id of the VPC peering connection:

- Use CloudFormation service and select the stack deployed with RFDK.
  Switch to Resources tab and search for `VPCPeeringConnection`.
  Copy the `Physical ID` and save it in the shell variable.
- Navigate directly to the deployed Peering Connection in the VPC console and copy the physical ID from there.
- Use AWS CLI command [describe-vpc-peering-connections](../../../cli/latest/reference/ec2/describe-vpc-peering-connections.md "../../../cli/latest/reference/ec2/describe-vpc-peering-connections.md") to view your VPC peering connections and find the connection id in the output.

```
aws --region PEER_VPC_REGION ec2 describe-vpc-peering-connections
VPC_PEERING_CONNECTION_ID=`peering-connection-id`

```

Now save the id of the route table in the shell variable as well:

```
PEER_SUBNET_ID=`peer-subnet-id`

```

For example, if you want to use AWS CLI:

```
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
INTERFACE=$(curl -H "X-aws-ec2-metadata-token: ${TOKEN}" --silent http://169.254.169.254/latest/meta-data/network/interfaces/macs/)
PEER_SUBNET_ID=$(curl -H "X-aws-ec2-metadata-token: ${TOKEN}" --silent http://169.254.169.254/latest/meta-data/network/interfaces/macs/${INTERFACE}/subnet-id)
echo $PEER_SUBNET_ID
```

Finally, substitute `rfdk-vpc-cidr-range` with a CIDR range of the VPC created by RFDK application and create a route:

```
RFDK_VPC_CIDR_RANGE=<replaceable>rfdk-vpc-cidr-range</replaceable>
ROUTING_TABLE=$(aws --region $PEER_VPC_REGION ec2 describe-route-tables --query "RouteTables[*].Associations[?SubnetId=='$PEER_SUBNET_ID'].RouteTableId" --output text)
aws --region $PEER_VPC_REGION ec2 create-route --route-table-id $ROUTING_TABLE --destination-cidr-block $RFDK_VPC_CIDR_RANGE --vpc-peering-connection-id $VPC_PEERING_CONNECTION_ID
```

Your RFDK application will create a peering connection, but you will still need to [accept a VPC peering connection](../../../vpc/latest/peering/create-vpc-peering-connection.md#accept-vpc-peering-connection "../../../vpc/latest/peering/create-vpc-peering-connection.md#accept-vpc-peering-connection") when your app is deployed.
You can accept the request in the AWS Console navigating to VPC service and switching to Peering Connections tab or with AWS CLI.
Accept the request with AWS CLI using `accept-vpc-peering-connection` command:

```
aws --region $PEER_VPC_REGION ec2 accept-vpc-peering-connection --vpc-peering-connection-id $VPC_PEERING_CONNECTION_ID
```

## Allowing connection to the Render Queue

To allow the connection to the render queue from the machines in your network, add the following code to your RFDK application.
Substitute `customer-prefix-cidr-range` with an IP range of your network in CIDR notation, for example, `10.200.0.0/16`.

Python

```
render_queue.connections.allow_default_port_from(ec2.Peer.ipv4("`customer-prefix-cidr-range`"))
```

TypeScript

```
renderQueue.connections.allowDefaultPortFrom(ec2.Peer.ipv4("`customer-prefix-cidr-range`"));
```

You can grant access to the render queue for the security group instead of the IP range:

Python

```
render_queue.connections.allow_default_port_from(security_group);
```

TypeScript

```
renderQueue.connections.allowDefaultPortFrom(securityGroup);
```

See [Connections construct API](../../../cdk/api/latest/docs/@aws-cdk_aws-ec2.md "../../../cdk/api/latest/docs/@aws-cdk_aws-ec2.md") for more details.

## Getting remote connection server address

Once your RFDK application is deployed, you can obtain the address of the remote connection server.

Navigate to the CloudFormation service in your AWS Web Console.
Find the stack deployed with RFDK and click on its name (for example, `hello-rfdk`).
Switch to the `Outputs` tab and find the `Key` of the Load Balancer. It should start with `RenderQueueAlbEc2ServicePatternLoadBalancer`.
Copy the `Value`, which is a DNS name of the load balancer.
This DNS name is the address of the remote connection server and you can use it to connect to your render farm.

Alternatively, you could find the same DNS name by navigating to the EC2 service and finding the newly deployed load balancer in the `Load Balancers` tab.

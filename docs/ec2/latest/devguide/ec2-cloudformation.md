# Create Amazon EC2 resources using AWS CloudFormation

Amazon EC2 is integrated with AWS CloudFormation, a service that helps you to model and set up your
AWS resources so that you can spend less time creating and managing your resources and
infrastructure. You create a template that describes the AWS resources that you need (such as
instances and subnets), and AWS CloudFormation provisions and configures those resources for you.

When you use AWS CloudFormation, you can reuse your template to set up your Amazon EC2 resources
consistently and repeatedly. Describe your resources once, and then provision the same
resources over and over in multiple AWS accounts and Regions.

## Amazon EC2 and AWS CloudFormation templates

To provision and configure resources for Amazon EC2 and related services, you must understand
[AWS CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md"). Templates are
formatted text files in JSON or YAML. These templates describe the resources you'll
provision in your AWS CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use AWS CloudFormation
Designer to help you get started with AWS CloudFormation templates. For more information, see [What is AWS CloudFormation Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the _AWS CloudFormation User Guide_.

## Resources for Amazon EC2

- [AWS::EC2::CapacityReservation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.md")
- [AWS::EC2::CapacityReservationFleet](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservationfleet.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservationfleet.md")
- [AWS::EC2::EC2Fleet](../../../AWSCloudFormation/latest/UserGuide.md "../../../AWSCloudFormation/latest/UserGuide.md")
- [AWS::EC2::EC2Fleet](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.md")
- [AWS::EC2::Host](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.md")
- [AWS::EC2::Instance](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instance.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instance.md")
- [AWS::EC2::InstanceConnectEndpoint](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instanceconnectendpoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instanceconnectendpoint.md")
- [AWS::EC2::LaunchTemplate](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.md")
- [AWS::EC2::PlacementGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-placementgroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-placementgroup.md")
- [AWS::EC2::SpotFleet](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-spotfleet.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-spotfleet.md")

- [AWS::EC2::CarrierGateway](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-carriergateway.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-carriergateway.md")
- [AWS::EC2::ClientVpnAuthorizationRule](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.md")
- [AWS::EC2::ClientVpnEndpoint](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.md")
- [AWS::EC2::ClientVpnRoute](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.md")
- [AWS::EC2::ClientVpnTargetNetworkAssociation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpntargetnetworkassociation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpntargetnetworkassociation.md")
- [AWS::EC2::CustomerGateway](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customergateway.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customergateway.md")
- [AWS::EC2::DHCPOptions](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcpoptions.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcpoptions.md")
- [AWS::EC2::EgressOnlyInternetGateway](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-egressonlyinternetgateway.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-egressonlyinternetgateway.md")
- [AWS::EC2::EIP](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eip.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eip.md")
- [AWS::EC2::EIPAssociation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eipassociation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eipassociation.md")
- [AWS::EC2::FlowLog](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.md")
- [AWS::EC2::GatewayRouteTableAssociation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-gatewayroutetableassociation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-gatewayroutetableassociation.md")
- [AWS::EC2::InternetGateway](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-internetgateway.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-internetgateway.md")
- [AWS::EC2::IPAM](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipam.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipam.md")
- [AWS::EC2::IPAMAllocation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamallocation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamallocation.md")
- [AWS::EC2::IPAMPool](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.md")
- [AWS::EC2::IPAMPoolCidr](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampoolcidr.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampoolcidr.md")
- [AWS::EC2::IPAMResourceDiscovery](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamresourcediscovery.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamresourcediscovery.md")
- [AWS::EC2::IPAMResourceDiscoveryAssociation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamresourcediscoveryassociation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamresourcediscoveryassociation.md")
- [AWS::EC2::IPAMScope](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamscope.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamscope.md")
- [AWS::EC2::LocalGatewayRoute](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.md")
- [AWS::EC2::LocalGatewayRouteTable](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetable.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetable.md")
- [AWS::EC2::LocalGatewayRouteTableVirtualInterfaceGroupAssociation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevirtualinterfacegroupassociation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevirtualinterfacegroupassociation.md")
- [AWS::EC2::LocalGatewayRouteTableVPCAssociation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevpcassociation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevpcassociation.md")
- [AWS::EC2::NatGateway](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.md")
- [AWS::EC2::NetworkInterface](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.md")
- [AWS::EC2::NetworkInsightsAccessScope](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsaccessscope.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsaccessscope.md")
- [AWS::EC2::NetworkInsightsAccessScopeAnalysis](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsaccessscopeanalysis.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsaccessscopeanalysis.md")
- [AWS::EC2::NetworkInsightsAnalysis](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.md")
- [AWS::EC2::NetworkInsightsPath](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightspath.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightspath.md")
- [AWS::EC2::NetworkInterfaceAttachment](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfaceattachment.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfaceattachment.md")
- [AWS::EC2::NetworkInterfacePermission](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfacepermission.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfacepermission.md")
- [AWS::EC2::NetworkPerformanceMetricSubscription](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkperformancemetricsubscription.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkperformancemetricsubscription.md")
- [AWS::EC2::PrefixList](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-prefixlist.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-prefixlist.md")
- [AWS::EC2::Route](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.md")
- [AWS::EC2::RouteTable](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-routetable.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-routetable.md")
- [AWS::EC2::Subnet](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.md")
- [AWS::EC2::SubnetCidrBlock](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetcidrblock.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetcidrblock.md")
- [AWS::EC2::SubnetNetworkAclAssociation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetnetworkaclassociation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetnetworkaclassociation.md")
- [AWS::EC2::SubnetRouteTableAssociation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetroutetableassociation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetroutetableassociation.md")
- [AWS::EC2::TrafficMirrorFilter](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilter.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilter.md")
- [AWS::EC2::TrafficMirrorFilterRule](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.md")
- [AWS::EC2::TrafficMirrorSession](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorsession.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorsession.md")
- [AWS::EC2::TrafficMirrorTarget](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrortarget.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrortarget.md")
- [AWS::EC2::TransitGateway](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.md")
- [AWS::EC2::TransitGatewayAttachment](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.md")
- [AWS::EC2::TransitGatewayConnect](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayconnect.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayconnect.md")
- [AWS::EC2::TransitGatewayMulticastDomain](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomain.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomain.md")
- [AWS::EC2::TransitGatewayMulticastDomainAssociation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomainassociation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomainassociation.md")
- [AWS::EC2::TransitGatewayMulticastGroupMember](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupmember.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupmember.md")
- [AWS::EC2::TransitGatewayMulticastGroupSource](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.md")
- [AWS::EC2::TransitGatewayPeeringAttachment](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.md")
- [AWS::EC2::TransitGatewayRoute](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.md")
- [AWS::EC2::TransitGatewayRouteTable](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetable.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetable.md")
- [AWS::EC2::TransitGatewayRouteTableAssociation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetableassociation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetableassociation.md")
- [AWS::EC2::TransitGatewayRouteTablePropagation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetablepropagation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetablepropagation.md")
- [AWS::EC2::TransitGatewayVpcAttachment](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayvpcattachment.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayvpcattachment.md")
- [AWS::EC2::VPC](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.md")
- [AWS::EC2::VPCCidrBlock](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.md")
- [AWS::EC2::VPCDHCPOptionsAssociation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcdhcpoptionsassociation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcdhcpoptionsassociation.md")
- [AWS::EC2::VPCEndpoint](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md")
- [AWS::EC2::VPCEndpointConnectionNotification](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.md")
- [AWS::EC2::VPCEndpointService](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.md")
- [AWS::EC2::VPCEndpointServicePermissions](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.md")
- [AWS::EC2::VPCGatewayAttachment](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcgatewayattachment.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcgatewayattachment.md")
- [AWS::EC2::VPCPeeringConnection](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.md")
- [AWS::EC2::VPNConnection](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpnconnection.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpnconnection.md")
- [AWS::EC2::VPNConnectionRoute](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpnconnectionroute.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpnconnectionroute.md")
- [AWS::EC2::VPNGateway](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpngateway.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpngateway.md")
- [AWS::EC2::VPNGatewayRoutePropagation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpngatewayroutepropagation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpngatewayroutepropagation.md")

- [AWS::EC2::KeyPair](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-keypair.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-keypair.md")
- [AWS::EC2::NetworkAcl](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkacl.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkacl.md")
- [AWS::EC2::NetworkAclEntry](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkaclentry.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkaclentry.md")
- [AWS::EC2::SecurityGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-securitygroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-securitygroup.md")
- [AWS::EC2::SecurityGroupEgress](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-securitygroupegress.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-securitygroupegress.md")
- [AWS::EC2::SecurityGroupIngress](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-securitygroupingress.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-securitygroupingress.md")
- [AWS::EC2::VerifiedAccessEndpoint](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.md")
- [AWS::EC2::VerifiedAccessGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessgroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessgroup.md")
- [AWS::EC2::VerifiedAccessInstance](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessinstance.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessinstance.md")
- [AWS::EC2::VerifiedAccessTrustProvider](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccesstrustprovider.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccesstrustprovider.md")

- [AWS::EC2::SnapshotBlockPublicAccess](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-snapshotblockpublicaccess.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-snapshotblockpublicaccess.md")
- [AWS::EC2::Volume](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.md")
- [AWS::EC2::VolumeAttachment](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volumeattachment.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volumeattachment.md")

## Learn more about AWS CloudFormation

To learn more about AWS CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide.md "../../../AWSCloudFormation/latest/UserGuide.md")

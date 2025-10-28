# AwsEc2 resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsEc2` resources.

AWS Security Hub normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsEc2ClientVpnEndpoint

The `AwsEc2ClientVpnEndpoint` object provides information about an AWS Client VPN endpoint. A Client VPN endpoint
is the resource that you create and configure to enable and manage client VPN sessions. It's the termination point for
all client VPN sessions.

The following example shows the AWS Security Finding Format (ASFF) for the `AwsEc2ClientVpnEndpoint` object.
To view descriptions of `AwsEc2ClientVpnEndpoint` attributes, see [AwsEc2ClientVpnEndpointDetails](../../1.0/APIReference/API_AwsEc2ClientVpnEndpointDetails.md "../../1.0/APIReference/API_AwsEc2ClientVpnEndpointDetails.md") in the _AWS Security Hub API Reference_.

**Example**

```
"AwsEc2ClientVpnEndpoint": {
    "AuthenticationOptions": [
        {
            "MutualAuthentication": {
                "ClientRootCertificateChainArn": "arn:aws:acm:us-east-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
            },
            "Type": "certificate-authentication"
        }
    ],
    "ClientCidrBlock": "10.0.0.0/22",
    "ClientConnectOptions": {
        "Enabled": false
    },
    "ClientLoginBannerOptions": {
        "Enabled": false
    },
    "ClientVpnEndpointId": "cvpn-endpoint-00c5d11fc4729f2a5",
    "ConnectionLogOptions": {
        "Enabled": false
    },
    "Description": "test",
    "DnsServer": ["10.0.0.0"],
    "ServerCertificateArn": "arn:aws:acm:us-east-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "SecurityGroupIdSet": [
        "sg-0f7a177b82b443691"
    ],
    "SelfServicePortalUrl": "https://self-service.clientvpn.amazonaws.com/endpoints/cvpn-endpoint-00c5d11fc4729f2a5",
    "SessionTimeoutHours": 24,
    "SplitTunnel": false,
    "TransportProtocol": "udp",
    "VpcId": "vpc-1a2b3c4d5e6f1a2b3",
    "VpnPort": 443
}
```

## AwsEc2Eip

The `AwsEc2Eip` object provides information about an Elastic IP
address.

The following example shows the AWS Security Finding Format (ASFF) for the `AwsEc2Eip` object.
To view descriptions of `AwsEc2Eip` attributes, see [AwsEc2EipDetails](../../1.0/APIReference/API_AwsEc2EipDetails.md "../../1.0/APIReference/API_AwsEc2EipDetails.md") in the _AWS Security Hub API Reference_.

**Example**

```
"AwsEc2Eip": {
    "InstanceId": "instance1",
    "PublicIp": "192.0.2.04",
    "AllocationId": "eipalloc-example-id-1",
    "AssociationId": "eipassoc-example-id-1",
    "Domain": "vpc",
    "PublicIpv4Pool": "anycompany",
    "NetworkBorderGroup": "eu-central-1",
    "NetworkInterfaceId": "eni-example-id-1",
    "NetworkInterfaceOwnerId": "777788889999",
    "PrivateIpAddress": "192.0.2.03"
}
```

## AwsEc2Instance

The `AwsEc2Instance` object provides details about an Amazon EC2
instance.

The following example shows the AWS Security Finding Format (ASFF) for the `AwsEc2Instance`
object. To view descriptions of `AwsEc2Instance` attributes, see [AwsEc2InstanceDetails](../../1.0/APIReference/API_AwsEc2InstanceDetails.md "../../1.0/APIReference/API_AwsEc2InstanceDetails.md") in the _AWS Security Hub API Reference_.

**Example**

```
"AwsEc2Instance": {
    "IamInstanceProfileArn": "arn:aws:iam::123456789012:instance-profile/AdminRole",
    "ImageId": "ami-1234",
    "IpV4Addresses": [ "1.1.1.1" ],
    "IpV6Addresses": [ "2001:db8:1234:1a2b::123" ],
    "KeyName": "my_keypair",
    "LaunchedAt": "2018-05-08T16:46:19.000Z",
    "MetadataOptions": {
    	"HttpEndpoint": "enabled",
    	"HttpProtocolIpv6": "enabled",
    	"HttpPutResponseHopLimit": 1,
    	"HttpTokens": "optional",
    	"InstanceMetadataTags": "disabled",
    },
    "Monitoring": {
    	"State": "disabled"
    },
    "NetworkInterfaces": [
      {
         "NetworkInterfaceId": "eni-e5aa89a3"
      }
    ],
    "SubnetId": "subnet-123",
    "Type": "i3.xlarge",
    "VpcId": "vpc-123"
}
```

## AwsEc2LaunchTemplate

The `AwsEc2LaunchTemplate` object contains details about an Amazon Elastic Compute Cloud
launch template that specifies instance configuration information.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsEc2LaunchTemplate` object. To view descriptions of
`AwsEc2LaunchTemplate` attributes, see [AwsEc2LaunchTemplateDetails](../../1.0/APIReference/API_AwsEc2LaunchTemplateDetals.md "../../1.0/APIReference/API_AwsEc2LaunchTemplateDetals.md") in the
_AWS Security Hub API Reference_.

**Example**

```
"AwsEc2LaunchTemplate": {
    "DefaultVersionNumber": "1",
    "ElasticGpuSpecifications": ["string"],
    "ElasticInferenceAccelerators": ["string"],
    "Id": "lt-0a16e9802800bdd85",
    "ImageId": "ami-0d5eff06f840b45e9",
    "LatestVersionNumber": "1",
    "LaunchTemplateData": {
    	"BlockDeviceMappings": [{
    		"DeviceName": "/dev/xvda",
    		"Ebs": {
    			"DeleteonTermination": true,
    			"Encrypted": true,
    			"SnapshotId": "snap-01047646ec075f543",
    			"VolumeSize": 8,
    			"VolumeType:" "gp2"
    		}
    	}],
    	"MetadataOptions": {
    		"HttpTokens": "enabled",
    		"HttpPutResponseHopLimit" : 1
    	},
    	"Monitoring": {
    		"Enabled": true,
    	"NetworkInterfaces": [{
    		"AssociatePublicIpAddress" : true,
    	}],
    "LaunchTemplateName": "string",
    "LicenseSpecifications": ["string"],
    "SecurityGroupIds": ["sg-01fce87ad6e019725"],
    "SecurityGroups": ["string"],
    "TagSpecifications": ["string"]
}
```

## AwsEc2NetworkAcl

The `AwsEc2NetworkAcl` object contains details about an Amazon EC2 network
access control list (ACL).

The following example shows the AWS Security Finding Format (ASFF) for the `AwsEc2NetworkAcl`
object. To view descriptions of `AwsEc2NetworkAcl` attributes, see [AwsEc2NetworkAclDetails](../../1.0/APIReference/API_AwsEc2NetworkAclDetails.md "../../1.0/APIReference/API_AwsEc2NetworkAclDetails.md") in the _AWS Security Hub API Reference_.

**Example**

```
"AwsEc2NetworkAcl": {
    "IsDefault": false,
    "NetworkAclId": "acl-1234567890abcdef0",
    "OwnerId": "123456789012",
    "VpcId": "vpc-1234abcd",
    "Associations": [{
        "NetworkAclAssociationId": "aclassoc-abcd1234",
        "NetworkAclId": "acl-021345abcdef6789",
        "SubnetId": "subnet-abcd1234"
   }],
   "Entries": [{
        "CidrBlock": "10.24.34.0/23",
        "Egress": true,
        "IcmpTypeCode": {
            "Code": 10,
            "Type": 30
        },
        "Ipv6CidrBlock": "2001:DB8::/32",
        "PortRange": {
            "From": 20,
            "To": 40
        },
        "Protocol": "tcp",
        "RuleAction": "allow",
        "RuleNumber": 100
   }]
}
```

## AwsEc2NetworkInterface

The `AwsEc2NetworkInterface` object provides information about an Amazon EC2
network interface.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsEc2NetworkInterface` object. To view descriptions of
`AwsEc2NetworkInterface` attributes, see [AwsEc2NetworkInterfaceDetails](../../1.0/APIReference/API_AwsEc2NetworkInterfaceDetails.md "../../1.0/APIReference/API_AwsEc2NetworkInterfaceDetails.md") in the
_AWS Security Hub API Reference_.

**Example**

```
"AwsEc2NetworkInterface": {
    "Attachment": {
        "AttachTime": "2019-01-01T03:03:21Z",
        "AttachmentId": "eni-attach-43348162",
        "DeleteOnTermination": true,
        "DeviceIndex": 123,
        "InstanceId": "i-1234567890abcdef0",
        "InstanceOwnerId": "123456789012",
        "Status": 'ATTACHED'
    },
    "SecurityGroups": [
        {
            "GroupName": "my-security-group",
            "GroupId": "sg-903004f8"
        },
    ],
    "NetworkInterfaceId": 'eni-686ea200',
    "SourceDestCheck": false
}
```

## AwsEc2RouteTable

The `AwsEc2RouteTable` object provides information about an Amazon EC2 route
table.

The following example shows the AWS Security Finding Format (ASFF) for the `AwsEc2RouteTable`
object. To view descriptions of `AwsEc2RouteTable` attributes, see [AwsEc2RouteTableDetails](../../1.0/APIReference/API_AwsEc2RouteTableDetails.md "../../1.0/APIReference/API_AwsEc2RouteTableDetails.md") in the _AWS Security Hub API Reference_.

**Example**

```
"AwsEc2RouteTable": {
    "AssociationSet": [{
    	"AssociationSet": {
    		"State": "associated"
    				},
    	"Main": true,
    	"RouteTableAssociationId": "rtbassoc-08e706c45de9f7512",
    	"RouteTableId": "rtb-0a59bde9cf2548e34",
    }],
    "PropogatingVgwSet": [],
    "RouteTableId": "rtb-0a59bde9cf2548e34",
    "RouteSet": [
    	{
    		"DestinationCidrBlock": "10.24.34.0/23",
    		"GatewayId": "local",
    		"Origin": "CreateRouteTable",
    		"State": "active"
    	},
    	{
    		"DestinationCidrBlock": "10.24.34.0/24",
    		"GatewayId": "igw-0242c2d7d513fc5d3",
    		"Origin": "CreateRoute",
    		"State": "active"
    	}
    ],
    "VpcId": "vpc-0c250a5c33f51d456"
}
```

## AwsEc2SecurityGroup

The `AwsEc2SecurityGroup` object describes an Amazon EC2 security group.

The following example shows the AWS Security Finding Format (ASFF) for the `AwsEc2SecurityGroup`
object. To view descriptions of `AwsEc2SecurityGroup` attributes, see [AwsEc2SecurityGroupDetails](../../1.0/APIReference/API_AwsEc2SecurityGroupDetails.md "../../1.0/APIReference/API_AwsEc2SecurityGroupDetails.md") in the
_AWS Security Hub API Reference_.

**Example**

```
"AwsEc2SecurityGroup": {
    "GroupName": "MySecurityGroup",
    "GroupId": "sg-903004f8",
    "OwnerId": "123456789012",
    "VpcId": "vpc-1a2b3c4d",
    "IpPermissions": [
        {
            "IpProtocol": "-1",
            "IpRanges": [],
            "UserIdGroupPairs": [
                {
                    "UserId": "123456789012",
                    "GroupId": "sg-903004f8"
                }
            ],
            "PrefixListIds": [
                {"PrefixListId": "pl-63a5400a"}
            ]
        },
        {
            "PrefixListIds": [],
            "FromPort": 22,
            "IpRanges": [
                {
                    "CidrIp": "203.0.113.0/24"
                }
            ],
            "ToPort": 22,
            "IpProtocol": "tcp",
            "UserIdGroupPairs": []
        }
    ]
}
```

## AwsEc2Subnet

The `AwsEc2Subnet` object provides information about a subnet in
Amazon EC2.

The following example shows the AWS Security Finding Format (ASFF) for the `AwsEc2Subnet`
object. To view descriptions of `AwsEc2Subnet` attributes, see [AwsEc2SubnetDetails](../../1.0/APIReference/API_AwsEc2SubnetDetails.md "../../1.0/APIReference/API_AwsEc2SubnetDetails.md") in the _AWS Security Hub API Reference_.

**Example**

```
AwsEc2Subnet: {
    "AssignIpv6AddressOnCreation": false,
    "AvailabilityZone": "us-west-2c",
    "AvailabilityZoneId": "usw2-az3",
    "AvailableIpAddressCount": 8185,
    "CidrBlock": "10.0.0.0/24",
    "DefaultForAz": false,
    "MapPublicIpOnLaunch": false,
    "OwnerId": "123456789012",
    "State": "available",
    "SubnetArn": "arn:aws:ec2:us-west-2:123456789012:subnet/subnet-d5436c93",
    "SubnetId": "subnet-d5436c93",
    "VpcId": "vpc-153ade70",
    "Ipv6CidrBlockAssociationSet": [{
        "AssociationId": "subnet-cidr-assoc-EXAMPLE",
        "Ipv6CidrBlock": "2001:DB8::/32",
        "CidrBlockState": "associated"
   }]
}
```

## AwsEc2TransitGateway

The `AwsEc2TransitGateway` object provides details about an Amazon EC2 transit
gateway that interconnects your virtual private clouds (VPCs) and on-premises
networks.

The following is an example `AwsEc2TransitGateway` finding in the AWS Security Finding Format
(ASFF). To view descriptions of `AwsEc2TransitGateway` attributes, see [AwsEc2TransitGatewayDetails](../../1.0/APIReference/API_AwsEc2TransitGatewayDetails.md "../../1.0/APIReference/API_AwsEc2TransitGatewayDetails.md") in the
_AWS Security Hub API Reference_.

**Example**

```
"AwsEc2TransitGateway": {
	"AmazonSideAsn": 65000,
	"AssociationDefaultRouteTableId": "tgw-rtb-099ba47cbbea837cc",
	"AutoAcceptSharedAttachments": "disable",
	"DefaultRouteTableAssociation": "enable",
	"DefaultRouteTablePropagation": "enable",
	"Description": "sample transit gateway",
	"DnsSupport": "enable",
	"Id": "tgw-042ae6bf7a5c126c3",
	"MulticastSupport": "disable",
	"PropagationDefaultRouteTableId": "tgw-rtb-099ba47cbbea837cc",
	"TransitGatewayCidrBlocks": ["10.0.0.0/16"],
	"VpnEcmpSupport": "enable"
}
```

## AwsEc2Volume

The `AwsEc2Volume` object provides details about an Amazon EC2 volume.

The following example shows the AWS Security Finding Format (ASFF) for the `AwsEc2Volume`
object. To view descriptions of `AwsEc2Volume` attributes, see [AwsEc2VolumeDetails](../../1.0/APIReference/API_AwsEc2VolumeDetails.md "../../1.0/APIReference/API_AwsEc2VolumeDetails.md") in the _AWS Security Hub API Reference_.

**Example**

```
"AwsEc2Volume": {
    "Attachments": [
      {
        "AttachTime": "2017-10-17T14:47:11Z",
        "DeleteOnTermination": true,
        "InstanceId": "i-123abc456def789g",
        "Status": "attached"
      }
     ],
    "CreateTime": "2020-02-24T15:54:30Z",
    "Encrypted": true,
    "KmsKeyId": "arn:aws:kms:us-east-1:111122223333:key/wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "Size": 80,
    "SnapshotId": "",
    "Status": "available"
}
```

## AwsEc2Vpc

The `AwsEc2Vpc` object provides details about an Amazon EC2 VPC.

The following example shows the AWS Security Finding Format (ASFF) for the `AwsEc2Vpc` object.
To view descriptions of `AwsEc2Vpc` attributes, see [AwsEc2VpcDetails](../../1.0/APIReference/API_AwsEc2VpcDetails.md "../../1.0/APIReference/API_AwsEc2VpcDetails.md") in the _AWS Security Hub API Reference_.

**Example**

```
"AwsEc2Vpc": {
    "CidrBlockAssociationSet": [
        {
            "AssociationId": "vpc-cidr-assoc-0dc4c852f52abda97",
            "CidrBlock": "192.0.2.0/24",
            "CidrBlockState": "associated"
        }
    ],
    "DhcpOptionsId": "dopt-4e42ce28",
    "Ipv6CidrBlockAssociationSet": [
        {
            "AssociationId": "vpc-cidr-assoc-0dc4c852f52abda97",
            "CidrBlockState": "associated",
            "Ipv6CidrBlock": "192.0.2.0/24"
       }

    ],
    "State": "available"
}
```

## AwsEc2VpcEndpointService

The `AwsEc2VpcEndpointService` object contains details about the service
configuration for a VPC endpoint service.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsEc2VpcEndpointService` object. To view descriptions of
`AwsEc2VpcEndpointService` attributes, see [AwsEc2VpcEndpointServiceDetails](../../1.0/APIReference/API_AwsEc2VpcEndpointServiceDetails.md "../../1.0/APIReference/API_AwsEc2VpcEndpointServiceDetails.md") in the
_AWS Security Hub API Reference_.

**Example**

```
"AwsEc2VpcEndpointService": {
    "ServiceType": [
      {
        "ServiceType": "Interface"
      }
    ],
    "ServiceId": "vpce-svc-example1",
    "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-example1",
    "ServiceState": "Available",
    "AvailabilityZones": [
      "us-east-1"
    ],
    "AcceptanceRequired": true,
    "ManagesVpcEndpoints": false,
    "NetworkLoadBalancerArns": [
      "arn:aws:elasticloadbalancing:us-east-1:444455556666:loadbalancer/net/my-network-load-balancer/example1"
    ],
    "GatewayLoadBalancerArns": [],
    "BaseEndpointDnsNames": [
      "vpce-svc-04eec859668b51c34.us-east-1.vpce.amazonaws.com"
    ],
    "PrivateDnsName": "my-private-dns"
}
```

## AwsEc2VpcPeeringConnection

The `AwsEc2VpcPeeringConnection` object provides details about the
networking connection between two VPCs.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsEc2VpcPeeringConnection` object. To view descriptions of
`AwsEc2VpcPeeringConnection` attributes, see [AwsEc2VpcPeeringConnectionDetails](../../1.0/APIReference/API_AwsEc2VpcPeeringConnectionDetails.md "../../1.0/APIReference/API_AwsEc2VpcPeeringConnectionDetails.md") in the
_AWS Security Hub API Reference_.

**Example**

```
"AwsEc2VpcPeeringConnection": {
	"AccepterVpcInfo": {
		"CidrBlock": "10.0.0.0/28",
		"CidrBlockSet": [{
			"CidrBlock": "10.0.0.0/28"
		}],
		"Ipv6CidrBlockSet": [{
			"Ipv6CidrBlock": "2002::1234:abcd:ffff:c0a8:101/64"
		}],
		"OwnerId": "012345678910",
		"PeeringOptions": {
			"AllowDnsResolutionFromRemoteVpc": true,
			"AllowEgressFromLocalClassicLinkToRemoteVpc": false,
			"AllowEgressFromLocalVpcToRemoteClassicLink": true
		},
		"Region": "us-west-2",
		"VpcId": "vpc-i123456"
	},
	"ExpirationTime": "2022-02-18T15:31:53.161Z",
	"RequesterVpcInfo": {
		"CidrBlock": "192.168.0.0/28",
		"CidrBlockSet": [{
			"CidrBlock": "192.168.0.0/28"
		}],
		"Ipv6CidrBlockSet": [{
			"Ipv6CidrBlock": "2002::1234:abcd:ffff:c0a8:101/64"
		}],
		"OwnerId": "012345678910",
		"PeeringOptions": {
			"AllowDnsResolutionFromRemoteVpc": true,
			"AllowEgressFromLocalClassicLinkToRemoteVpc": false,
			"AllowEgressFromLocalVpcToRemoteClassicLink": true
		},
		"Region": "us-west-2",
		"VpcId": "vpc-i123456"
	},
	"Status": {
		"Code": "initiating-request",
		"Message": "Active"
	},
	"VpcPeeringConnectionId": "pcx-1a2b3c4d"
}
```

# AWS Cloud WAN example: Insert firewalls between on-premises and VPCs

In this policy, the goal is to send all traffic from on-premises to AWS through a
 firewall. The customer has a VPC with a firewall (AWS Network Firewall, Gateway Load Balancer, or EC2/Marketplace
 offering) already configured in the VPC. The firewall is responsible for inspecting traffic
 from on-premises to AWS, and from AWS VPCs in the internalApps segment to the
 internet.

Similar to [Example: Edge
 consolidation](cloudwan-policy-examples-edge-consolidation.md "cloudwan-policy-examples-edge-consolidation.md"), the VPC and VPNs are mapped to segments based on the attachment
 type. The one exception is the firewall VPC, which needs its own specific segment so that it
 can be shared separately with the other segments. In order to force the traffic coming in
 from the VPN to a firewall, static routes are configured that point to the firewall. In this
 case, the AWS VPCs in the internalApps segment are using the `172.16.0.0/16`
 CIDR space. All other private (RFC1918) space is advertised from the VPN connection. In this
 case, the policy uses the share and static-route options to define how each of the three
 segments receive the correct routes to send traffic through a middle box.


```
{
	"version": "2021.12",
	"core-network-configuration": {
		"asn-ranges": [
			"64512-65534"
		],
		"edge-locations": [
			{
				"location": "us-east-1"
			},
			{
				"location": "us-west-2"
			}
		]
	},
	"segments": [
		{
			"name": "internalApps"
		},
		{
			"name": "firewall"
		},
		{
			"name": "onPremises"
		}
	],
	"segment-actions": [
		{
			"action": "create-route",
			"destination-cidr-blocks": [
				"0.0.0.0/0"
			],
			"segment": "internalApps",
			"destinations": [
				"attachment-deadbeef901234567",
				"attachment-eeeeee00000000000"
			],
			"description": "Send all internet headed on-premises through the firewall"
		},
		{
			"action": "create-route",
			"destination-cidr-blocks": [
				"0.0.0.0/0"
			],
			"segment": "onPremises",
			"destinations": [
				"attachment-deadbeef901234567",
				"attachment-eeeeee00000000000"
			],
			"description": "Send all traffic received from the VPN through the firewall"
		},
		{
			"action": "share",
			"mode": "attachment-route",
			"segment": "firewall",
			"share-with": [
				"internalAapps",
				"onPremises"
			]
		}
	],
	"attachment-policies": [
		{
			"rule-number": 500,
			"description": "We’ll do our specific policies before we do attachment types.",
			"conditions": [
				{
					"type": "tag-value",
					"key": "core-network",
					"operator": "equals",
					"value": "firewall"
				}
			],
			"action": {
				"association-method": "constant",
				"segment": "firewall"
			}
		},
		{
			"rule-number": 1000,
			"description": "Let’s assume all VPCs are internal apps",
			"conditions": [
				{
					"type": "attachment-type",
					"operator": "equals",
					"value": "vpc"
				}
			],
			"action": {
				"association-method": "constant",
				"segment": "internalApps"
			}
		},
		{
			"rule-number": 1500,
			"description": "Let’s also assume all VPNs are from on-premises",
			"conditions": [
				{
					"type": "attachment-type",
					"operator": "equals",
					"value": "site-to-site-vpn"
				}
			],
			"action": {
				"association-method": "constant",
				"segment": "onPremises"
			}
		}
	]
}
```

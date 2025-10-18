# AWS Cloud WAN example: Three-stage development environment using both tag values and manual shared services mapping

This policy creates a common software development lifecycle policy. It includes three
 development stages: development, testing, and production. VPCs in any one of these segments
 can’t talk to each other because `isolate-attachments` is set to true. These VPC
 attachments are tagged with their stage, which directly maps to the name of the segment that
 they should belong to. If developers use the Development or Testing stages, the VPC is
 automatically mapped without approval, but Production requires approval. There is an
 additional `sharedservices` segment, which includes both a VPC and a site-to-site
 VPN. These attachments don’t use tags, but are instead mapped by their explicit resource-ID.
 The `sharedservices` segment is shared with the isolated development environments
 so that they can reach on-premises through VPN and can also reach the shared services
 VPC.


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
			"name": "development",
			"isolate-attachments": true,
			"require-attachment-acceptance": false
		},
		{
			"name": "testing",
			"isolate-attachments": true,
			"require-attachment-acceptance": false
		},
		{
			"name": "production",
			"isolate-attachments": true,
			"require-attachment-acceptance": true
		},
		{
			"name": "sharedServices"
		}
	],
	"segment-actions": [
		{
			"action": "share",
			"mode": "attachment-route",
			"segment": "sharedservices",
			"share-with": "*"
		}
	],
	"attachment-policies": [
		{
			"rule-number": 1000,
			"conditions": [
				{
					"type": "tag-exists",
					"key": "Stage"
				}
			],
			"action": {
				"association-method": "tag",
				"tag-value-of-key": "Stage"
			}
		},
		{
			"rule-number": 1500,
			"conditions": [
				{
					"type": "resource-id",
					"operator": "equals",
					"value": "vpc-1234567890123456"
				}
			],
			"action": {
				"association-method": "constant",
				"segment": "sharedservices"
			}
		},
		{
			"rule-number": 1600,
			"conditions": [
				{
					"type": "resource-id",
					"operator": "equals",
					"value": "vpn-1234567890123456"
				}
			],
			"action": {
				"association-method": "constant",
				"segment": "sharedservices"
			}
		}
	]
}
```

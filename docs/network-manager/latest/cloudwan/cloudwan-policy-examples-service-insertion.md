# AWS Cloud WAN example: Service insertion firewalls

between on-premises and VPCs

In this policy, traffic on a segment named _development_ is first sent
to an Inspection VPC before being sent to a segment named _production_ using
a network function group named _InspectionVPC_. The on-premises attachment
has already been set up and mapped to either the `development` or
`production` segments. The segment action uses `send-via`, indicating
that this is east-west traffic. The attachment policy rule uses the `and` condition
logic with `InspectionVpcs` as the value of the key-value pair associated with the
attachment.

```
{
    "version": "2021.12",
    "core-network-configuration": {
        "vpn-ecmp-support": true,
        "inside-cidr-blocks": [
            "10.0.0.0/16"
        ],
        "asn-ranges": [
            "64512-65534"
        ],
        "edge-locations": [
            {
                "location": "us-east-2"
            },
            {
                "location": "us-west-2"
            }
        ]
    },
    "segments": [
        {
            "name": "development",
            "edge-locations": [
                "us-east-2"
            ],
            "require-attachment-acceptance": true,
            "isolate-attachments": true
        },
        {
            "name": "production",
            "edge-locations": [
                "us-east-2"
            ],
            "require-attachment-acceptance": true,
            "isolate-attachments": true
        }
    ],
    "network-function-groups": [
        {
            "name": "InspectionVPC",
            "description": "Route segment traffic to the inspection VPC",
            "require-attachment-acceptance": true
        }
    ],
    "segment-actions": [
        {
            "action": "send-via",
            "segment": "development",
            "mode": "single-hop",
            "when-sent-to": {
                "segments": [
                    "production"
                ]
            },
            "via": {
                "network-function-groups": [
                    "InspectionVPC"
                ]
            }
        }
    ],
    "attachment-policies": [
        {
            "rule-number": 125,
            "condition-logic": "and",
            "conditions": [
                {
                    "type": "tag-exists",
                    "key": "InspectionVpcs"
                }
            ],
            "action": {
                "add-to-network-function-group": "InspectionVPC"
            }
        }
    ]
}
```

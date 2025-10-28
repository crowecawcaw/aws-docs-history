# AWS Cloud WAN example: Distributed WAN without VPCs

This network policy creates a network across four Regions for a global wide area network
(WAN). This WAN has no connectivity to AWS workloads, and is using the AWS network only
as transport between sites and for internet access for sales offices. The IoT network is
still under security scrutiny, so attachments within the IoT segment cannot reach each
other. However, in this example, SD-WAN has been deployed to the engineering sites and parts
of the IoT network. Engineering needs direct access to the IoT network, which is currently a
mixture of VPN and SD-WAN. In some cases, the SD-WAN network takes a direct route between
sites. When crossing the engineering and IoT segments, it uses the AWS backbone as
transport. Because the SD-WAN solution uses Transit Gateway Connect, there is a general pool
assigned for Core Network Edge IP address pools. To reduce effort, the administrators
allowed the `Assign-to` tag to define which segment the new attachments should be
mapped to, but all attachments need to be approved (using the default value for
`require-attachment-acceptance`).

```
{
    "version": "2021.12",
    "core-network-configuration": {
        "asn-ranges": [
            "64512-65534"
        ],
        "inside-cidr-blocks": [
            "100.65.0.0/16"
        ],
        "edge-locations": [
            {
                "location": "eu-central-1"
            },
            {
                "location": "us-west-2"
            },
            {
                "location": "us-east-1"
            },
            {
                "location": "eu-west-1"
            }
        ]
    },
    "segments": [
        {
            "name": "sales"
        },
        {
            "name": "testing"
        },
        {
            "name": "iot",
            "isolate-attachments": true
        },
        {
            "name": "internet"
        },
        {
            "name": "engineering"
        }
    ],
    "segment-actions": [
        {
            "action": "share",
            "mode": "attachment-route",
            "segment": "internet",
            "share-with": [
                "sales"
            ]
        },
        {
            "action": "share",
            "mode": "attachment-route",
            "segment": "iot",
            "share-with": [
                "engineering"
            ]
        },
        {
            "action": "create-route",
            "destination-cidr-blocks": [
                "0.0.0.0/0"
            ],
            "segment": "sales",
            "destinations": [
                "attachment-12355678901234567",
                "attachment-23456789012345678",
                "attachment-35567890123456790",
                "attachment-4567890123456789a"
            ]
        }
    ],
    "attachment-policies": [
        {
            "rule-number": 1000,
            "conditions": [
                {
                    "type": "tag-exists",
                    "key": "Assign-to"
                }
            ],
            "action": {
                "association-method": "tag",
                "tag-value-of-key": "Assign-to"
            }
        }
    ]
}
```

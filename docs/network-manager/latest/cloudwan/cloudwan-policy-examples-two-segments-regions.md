# AWS Cloud WAN example: Two segments and multiple

AWS Regions

This policy sets up two networks, `Secured` and `Non-Secured`,
across three AWS Regions. Attachments with the tag `"Network" : "Secured"` map
to `"Secured"`, while attachments with the tag `"Network" :
 "Non-Secured"` map to `"Non-Secured"`. All attachments require
acceptance. Attachments can only talk within their segment but not across segments.

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
                "location": "us-east-2"
            },
            {
                "location": "eu-west-1"
            }
        ]
    },
    "segments": [
        {
            "name": "secured"
        },
        {
            "name": "nonSecured"
        }
    ],
    "attachment-policies": [
        {
            "rule-number": 100,
            "conditions": [
                {
                    "type": "tag-value",
                    "key": "Network",
                    "value": "Secured",
                    "operator": "equals"
                }
            ],
            "action": {
                "association-method": "constant",
                "segment": "secured"
            }
        },
        {
            "rule-number": 200,
            "conditions": [
                {
                    "type": "tag-value",
                    "key": "Network",
                    "value": "Non-Secured",
                    "operator": "equals"
                }
            ],
            "action": {
                "association-method": "constant",
                "segment": "non-secured"
            }
        }
    ]
}
```

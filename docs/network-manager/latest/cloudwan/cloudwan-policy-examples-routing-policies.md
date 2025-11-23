# AWS Cloud WAN example: Routing Policies

In this policy example, there are three segments `hybrid`, `production` and `development` with on-premises
networks onboarding to `hybrid` segment via VPN or Direct Connect attachments and VPCs onboarding to `production` and `development` segments.
There are two routing policies defined for filtering routes. Routing policy `100` only allows inbound routes from CIDR ranges
`10.10.0.0/16` and `172.16.0.0/16` and is applied via label `inboundRouteFilterHybrid` to all VPN and Direct Connect attachments
that connect to remote sites and onboard to the `hybrid` segment. Routing policy `200` only allows inbound routes from CIDR range
`10.10.0.0/16` and is applied to the segment share between `production` and `hybrid` segment. As a result only `10.10.0.0/16` network
routes from on-premises networks are learnt in the `production` segment and all other routes are filtered. Routing policy `300` will drop all routes contained in the prefix list
referenced by the alias `prefixListAlias` see [AWS Cloud WAN prefix list associations](cloudwan-prefix-lists.md "cloudwan-prefix-lists.md") on how to setup a core network prefix list association. Routing policy `300`
is applied to the segment `production` across the edge locations `us-east-2` and `us-west-2` since `us-east-2` is the first edge location in the segment action definition
and the routing policy is inbounds the drop action will affect all routes coming from `us-west-2` going `us-east-2`.

```
{
  "version": "2025.11",
  "core-network-configuration": {
    "vpn-ecmp-support": true,
    "dns-support": true,
    "security-group-referencing-support": false,
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
      "name": "hybrid",
      "require-attachment-acceptance": false
    },
    {
      "name": "production",
      "require-attachment-acceptance": true
    },
    {
      "name": "development",
      "require-attachment-acceptance": false
    }
  ],
  "network-function-groups": [],
  "segment-actions": [
    {
      "action": "share",
      "mode": "attachment-route",
      "segment": "production",
      "share-with": [
        "hybrid"
      ],
      "routing-policy-names": [
        "inboundRouteFilterProduction"
      ]
    },
    {
      "action": "associate-routing-policy",
      "segment": "production",
      "edge-location-association": {
        "routing-policy-names": [
          "edgeToEdgeRouteFilterProduction"
        ],
        "edge-location": "us-east-2",
        "peer-edge-location": "us-west-2"
      }
    }
  ],
  "attachment-routing-policy-rules": [
    {
      "rule-number": 500,
      "description": "Attachment Route Filters",
      "conditions": [
        {
          "type": "routing-policy-label",
          "value": "hybridAttachmentsRouteFilter" // associate this label to all attachments on the hybrid segment
        }
      ],
      "action": {
        "associate-routing-policies": [
          "inboundRouteFilterHybrid"
        ]
      }
    }
  ],
  "routing-policies": [
    {
      "routing-policy-name": "inboundRouteFilterHybrid",
      "routing-policy-description": "Filter routes landing in hybrid segment from on-premises network",
      "routing-policy-direction": "inbound",
      "routing-policy-number": 100,
      "routing-policy-rules": [
        {
          "rule-number": 100,
          "rule-definition": {
            "match-conditions": [
              {
                "type": "prefix-equals",
                "value": "172.16.0.0/16"
              },
              {
                "type": "prefix-in-cidr",
                "value": "10.10.0.0/16"
              }
            ],
            "condition-logic": "or",
            "action": {
              "type": "allow"
            }
          }
        }
      ]
    },
    {
      "routing-policy-name": "inboundRouteFilterProduction",
      "routing-policy-description": "Filter routes landing in production segment from hybrid segment",
      "routing-policy-direction": "inbound",
      "routing-policy-number": 200,
      "routing-policy-rules": [
        {
          "rule-number": 100,
          "rule-definition": {
            "match-conditions": [
              {
                "type": "prefix-in-cidr",
                "value": "10.10.0.0/16"
              }
            ],
            "condition-logic": "or",
            "action": {
              "type": "allow"
            }
          }
        }
      ]
    },
    {
      "routing-policy-name": "edgeToEdgeRouteFilterProduction",
      "routing-policy-description": "Filter routes between edge locations us-east-1 and us-west-2",
      "routing-policy-direction": "inbound",
      "routing-policy-number": 300,
      "routing-policy-rules": [
        {
          "rule-number": 100,
          "rule-definition": {
            "match-conditions": [
              {
                "type": "prefix-in-prefix-list",
                "value": "prefixListAlias"
              }
            ],
            "condition-logic": "or",
            "action": {
              "type": "drop"
            }
          }
        }
      ]
    }
  ]
}
```

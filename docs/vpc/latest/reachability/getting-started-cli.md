# Getting started with Reachability Analyzer using the AWS CLI

You can use Reachability Analyzer to determine whether a destination resource in your virtual private cloud
(VPC) is reachable from a source resource. To get started, you specify a source and a
destination. For example, you can run a reachability analysis between two network interfaces
or between a network interface and a gateway. If there is a reachable path between the
source and destination, Reachability Analyzer displays the details. Otherwise, Reachability Analyzer identifies the blocking
component.

###### Tasks

- [Step 1: Create a path](#create-path-cli "#create-path-cli")
- [Step 2: Analyze the path](#analyze-path-cli "#analyze-path-cli")
- [Step 3: Get the results of the path analysis](#view-results-cli "#view-results-cli")
- [Step 4: Delete the path](#delete-path-cli "#delete-path-cli")

## Step 1: Create a path

Use the following [create-network-insights-path](../../../cli/latest/reference/ec2/create-network-insights-path.md "../../../cli/latest/reference/ec2/create-network-insights-path.md") command to create a path. In this example, the source
is an internet gateway and the destination is an EC2 instance.

```
aws ec2 create-network-insights-path
    --source `igw-0797cccdc9d73b0e5`
    --destination `i-0495d385ad28331c7`
    --protocol `TCP`
    --filter-at-source file://source-filter.json
```

The following is an example `source-filter.json`.

```
{
    "DestinationPortRange": {
        "FromPort": `22`,
        "ToPort": `22`
    }
}
```

The following is example output.

```
{
    "NetworkInsightsPaths": {
        "NetworkInsightsPathId": "nip-0b26f224f1d131fa8",
        "NetworkInsightsPathArn": "arn:aws:ec2:us-east-1:123456789012:network-insights-path/nip-0b26f224f1d131fa8",
        "CreatedDate": "2023-03-20T22:43:46.933Z",
        "Source": "igw-0797cccdc9d73b0e5",
        "Destination": "i-0495d385ad28331c7",
        "SourceArn": "arn:aws:ec2:us-east-1:123456789012:internet-gateway/0797cccdc9d73b0e5",
        "DestinationArn": "arn:aws:ec2:us-east-1:123456789012:instance/0495d385ad28331c7",
        "Protocol": "tcp"
    }
}
```

To specify an IP address as the destination resource, omit the
`--destination` parameter and filter on the destination address as
follows.

```
aws ec2 create-network-insights-path
    --source `igw-0797cccdc9d73b0e5`
    --protocol `TCP`
    --filter-at-source file://source-filter.json
```

The following is an example of `source-filter.json`.

```
{
    "DestinationAddress": "`34.230.71.227`",
    "DestinationPortRange": {
        "FromPort": `22`,
        "ToPort": `22`
    }
}
```

## Step 2: Analyze the path

Use the following [start-network-insights-analysis](../../../cli/latest/reference/ec2/start-network-insights-analysis.md "../../../cli/latest/reference/ec2/start-network-insights-analysis.md") command to determine whether the destination is
reachable using the protocol and port that you specified for the path. The analysis can
take a few minutes to complete.

```
aws ec2 start-network-insights-analysis --network-insights-path-id `nip-0abc123def456789`
```

The following is example output.

```
{
    "NetworkInsightsAnalysis": {
        "NetworkInsightsAnalysisId": "nia-0abc123def456789",
        "NetworkInsightsAnalysisArn": "arn:aws:ec2:us-east-1:123456789012:network-insights-analysis/nia-02207aa13eb480c7a",
        "NetworkInsightsPathId": "nip-0abc123def456789",
        "StartDate": "2023-03-20T22:58:37.495Z",
        "Status": "running"
    }
}
```

## Step 3: Get the results of the path analysis

After the path analysis completes, you can view the results using the [describe-network-insights-analyses](../../../cli/latest/reference/ec2/describe-network-insights-analyses.md "../../../cli/latest/reference/ec2/describe-network-insights-analyses.md")
command.

```
aws ec2 describe-network-insights-analyses --network-insights-analysis-ids `nia-0abc123def456789`
```

###### Example 1: Not reachable

The following is example output where the path is not reachable. When a path is
not reachable, `NetworkPathFound` is `false` and
`ExplanationCode` contains an explanation code. For descriptions of
the explanation codes, see [Reachability Analyzer explanation codes](explanation-codes.md "explanation-codes.md"). In this example,
`ENI_SG_RULES_MISMATCH`, indicates that the security group does not
allow the traffic. After you add a rule to the security group to allow the traffic,
you can reanalyze the same path and confirm that it is reachable.

```
{
    "NetworkInsightsAnalyses": [
        {
            "NetworkInsightsAnalysisId": "nia-0abc123def456789",
            "NetworkInsightsAnalysisArn": "arn:aws:ec2:us-west-2:123456789012:network-insights-analysis/nia-0abc123def456789",
            "NetworkInsightsPathId": "nip-0abc123def456789",
            "FilterInArns": [
                "arn:aws:ec2:us-west-2:123456789012:vpc/vpc-0abc123def456789"
            ],
            "FilterOutArns": [
                "arn:aws:ec2:us-west-2:123456789012:internet-gateway/igw-0abc123def456789"
            ],
            "StartDate": "2025-03-15T14:30:00.000Z",
            "Status": "succeeded",
            "StatusMessage": "Analysis completed successfully",
            "NetworkPathFound": false,
            "ForwardPathComponents": [
                {
                    "SequenceNumber": 1,
                    "Component": {
                        "Id": "i-0abc123def456789",
                        "Arn": "arn:aws:ec2:us-west-2:123456789012:instance/i-0abc123def456789",
                        "Name": "Source Instance"
                    }
                },
                {
                    "SequenceNumber": 2,
                    "Component": {
                        "Id": "eni-0abc123def456789",
                        "Arn": "arn:aws:ec2:us-west-2:123456789012:network-interface/eni-0abc123def456789",
                        "Name": "Source ENI"
                    }
                },
                {
                    "SequenceNumber": 3,
                    "Component": {
                        "Id": "subnet-0abc123def456789",
                        "Arn": "arn:aws:ec2:us-west-2:123456789012:subnet/subnet-0abc123def456789",
                        "Name": "Private Subnet"
                    }
                }
            ],
            "Explanations": [
                {
                    "Direction": "ingress",
                    "ExplanationCode": "ENI_SG_RULES_MISMATCH",
                    "NetworkInterface": {
                        "Id": "eni-0def456789abc0123",
                        "Arn": "arn:aws:ec2:us-west-2:123456789012:network-interface/eni-0def456789abc0123",
                        "Name": "Destination ENI"
                    },
                    "SecurityGroups": [
                        {
                            "Id": "sg-0abc123def456789",
                            "Arn": "arn:aws:ec2:us-west-2:123456789012:security-group/sg-0abc123def456789",
                            "Name": "Source Security Group"
                        },
                        {
                            "Id": "sg-0def456789abc0123",
                            "Arn": "arn:aws:ec2:us-west-2:123456789012:security-group/sg-0def456789abc0123",
                            "Name": "Destination Security Group"
                        }
                    ],
                    "Vpc": {
                        "Id": "vpc-0abc123def456789",
                        "Arn": "arn:aws:ec2:us-west-2:123456789012:vpc/vpc-0abc123def456789",
                        "Name": "Main VPC"
                    },
                    "PacketField": "destination-port",
                    "Port": 443,
                    "Protocol": "tcp"
                }
            ],
            "AlternatePathHints": [
                {
                    "ComponentId": "sg-0fff111222333444",
                    "ComponentArn": "arn:aws:ec2:us-west-2:123456789012:security-group/sg-0fff111222333444"
                }
            ],
            "Tags": [
                {
                    "Key": "Project",
                    "Value": "NetworkTroubleshooting"
                },
                {
                    "Key": "Environment",
                    "Value": "Production"
                }
            ]
        },
        {
            "NetworkInsightsAnalysisId": "nia-0def456789abc0123",
            "NetworkInsightsAnalysisArn": "arn:aws:ec2:us-west-2:123456789012:network-insights-analysis/nia-0def456789abc0123",
            "NetworkInsightsPathId": "nip-0abc123def456789",
            "FilterInArns": [
                "arn:aws:ec2:us-west-2:123456789012:vpc/vpc-0abc123def456789"
            ],
            "FilterOutArns": [
                "arn:aws:ec2:us-west-2:123456789012:internet-gateway/igw-0abc123def456789"
            ],
            "StartDate": "2025-04-10T09:45:00.000Z",
            "Status": "succeeded",
            "StatusMessage": "Analysis completed successfully",
            "NetworkPathFound": false,
            "ForwardPathComponents": [
                {
                    "SequenceNumber": 1,
                    "Component": {
                        "Id": "i-0def456789abc0123",
                        "Arn": "arn:aws:ec2:us-west-2:123456789012:instance/i-0def456789abc0123",
                        "Name": "Source Instance"
                    }
                },
                {
                    "SequenceNumber": 2,
                    "Component": {
                        "Id": "eni-0def456789abc0123",
                        "Arn": "arn:aws:ec2:us-west-2:123456789012:network-interface/eni-0def456789abc0123",
                        "Name": "Source ENI"
                    }
                }
            ],
            "Explanations": [
                {
                    "Direction": "ingress",
                    "ExplanationCode": "ENI_SG_RULES_MISMATCH",
                    "NetworkInterface": {
                        "Id": "eni-0fff111222333444",
                        "Arn": "arn:aws:ec2:us-west-2:123456789012:network-interface/eni-0fff111222333444",
                        "Name": "Target Load Balancer ENI"
                    },
                    "SecurityGroupRule": {
                        "SecurityGroupId": "sg-0def456789abc0123",
                        "Direction": "ingress",
                        "PortRange": {
                            "From": 80,
                            "To": 80
                        },
                        "Protocol": "tcp",
                        "Cidr": "10.0.0.0/16"
                    },
                    "PacketField": "source-address",
                    "Vpc": {
                        "Id": "vpc-0abc123def456789",
                        "Arn": "arn:aws:ec2:us-west-2:123456789012:vpc/vpc-0abc123def456789",
                        "Name": "Main VPC"
                    }
                }
            ],
            "Tags": [
                {
                    "Key": "Purpose",
                    "Value": "SecurityAudit"
                }
            ]
        }
    ],
    "NextToken": "eyJOZXh0VG9rZW4iOiJwYWdlLTIifQ=="
}
```

###### Example 2: Reachable

The following is example output where the path is reachable. When a path is reachable,
`NetworkPathFound` is `true`, `ForwardPathComponents` contains
component-by-component details about the shortest reachable path from source to destination, and
`ReturnPathComponents` contains component-by-component details about the shortest
reachable path from destination to source.

```
{
    "NetworkInsightsAnalyses": [
        {
            "NetworkInsightsAnalysisId": "nia-076744f74a04c3c7f",
            "NetworkInsightsAnalysisArn": "arn:aws:ec2:us-east-1:123456789012:network-insights-analysis/nia-076744f74a04c3c7f",
            "NetworkInsightsPathId": "nip-0614b9507b4e3e989",
            "StartDate": "2023-03-20T23:47:08.080Z",
            "Status": "succeeded",
            "NetworkPathFound": true,
            "ForwardPathComponents": [
                {
                    "SequenceNumber": 1,
                    "Component": {
                        "Id": "igw-0797cccdc9d73b0e5",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:internet-gateway/igw-0797cccdc9d73b0e5",
                    },
                    "OutboundHeader": {
                        "DestinationAddresses": ["10.0.2.87/32"]
                    },
                    "InboundHeader": {
                        "DestinationAddresses": ["34.230.71.227/32"],
                        "DestinationPortRanges": [{
                            "From": 22,
                            "To": 22
                        }],
                        "Protocol": "6",
                        "SourceAddresses": ["0.0.0.0/5", "11.0.0.0/8", "12.0.0.0/6", ...],
                        "SourcePortRanges": [{
                            "From": 0,
                            "To": 65535
                        }]
                    },
                    "Vpc": {
                        "Id": "vpc-f1663d98ad28331c7",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-f1663d98ad28331c7"
                    },
                    "AdditionalDetails": [],
                    "Explanations": []
                },
                {
                    "SequenceNumber": 2,
                    "AclRule": {
                        "Cidr": "0.0.0.0/0",
                        "Egress": false,
                        "Protocol": "all",
                        "RuleAction": "allow",
                        "RuleNumber": 100
                    },
                    "Component": {
                        "Id": "acl-04fbcfb79260f6c5b",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:network-acl/acl-04fbcfb79260f6c5b"
                    },
                    "AdditionalDetails": [],
                    "Explanations": []
                },
                {
                    "SequenceNumber": 3,
                    "Component": {
                        "Id": "sg-02f0d35a850ba727f",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:security-group/sg-02f0d35a850ba727f"
                    },
                    "SecurityGroupRule": {
                        "Cidr": "0.0.0.0/0",
                        "Direction": "ingress",
                        "PortRange": {
                            "From": 22,
                            "To": 22
                        },
                        "Protocol": "tcp"
                    },
                    "AdditionalDetails": [],
                    "Explanations": []
                },
                {
                    "SequenceNumber": 4,
                    "AttachedTo": {
                        "Id": "i-0495d385ad28331c7",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:instance/i-0495d385ad28331c7"
                    },
                    "Component": {
                        "Id": "eni-0a25edef15a6cc08c",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:network-interface/eni-0a25edef15a6cc08c"
                    },
                    "Subnet": {
                        "Id": "subnet-004ff41eccb4d1194",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:subnet/subnet-004ff41eccb4d1194"
                    },
                    "Vpc": {
                        "Id": "vpc-f1663d98ad28331c7",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-f1663d98ad28331c7"
                    },
                    "AdditionalDetails": [],
                    "Explanations": []
                },
                {
                    "SequenceNumber": 5,
                    "Component": {
                        "Id": "i-0626d4edd54f1286d",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:instance/i-0626d4edd54f1286d"
                    },
                    "InboundHeader": {
                        "DestinationAddresses": ["10.0.4.120/32"],
                        "DestinationPortRanges": [{
                            "From": 22,
                            "To": 22
                        }],
                        "Protocol": "6",
                        "SourceAddresses": ["0.0.0.0/5", "11.0.0.0/8", "12.0.0.0/6", ...],
                        "SourcePortRanges": [{
                            "From": 0,
                            "To": 65535
                        }]
                    },
                    "AdditionalDetails": [],
                    "Explanations": []
                }
            ],
            "ReturnPathComponents": [
                {
                    "SequenceNumber": 1,
                    "Component": {
                        "Id": "i-0626d4edd54f1286d",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:instance/i-0626d4edd54f1286d"
                    },
                    "OutboundHeader": {
                        "DestinationAddresses": ["0.0.0.0/5", "11.0.0.0/8", "12.0.0.0/6", ...],
                        "DestinationPortRanges": [{
                            "From": 0,
                            "To": 65535
                        }],
                        "Protocol": "6",
                        "SourceAddresses": ["10.0.2.87/32"],
                        "SourcePortRanges": [{
                            "From": 22,
                            "To": 22
                        }]
                    },
                    "AdditionalDetails": [],
                    "Explanations": []
                },
                {
                    "SequenceNumber": 2,
                    "AttachedTo": {
                        "Id": "i-0495d385ad28331c7",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:instance/i-0495d385ad28331c7"
                    },
                    "Component": {
                        "Id": "eni-0a25edef15a6cc08c",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:network-interface/eni-0a25edef15a6cc08c"
                    },
                    "Subnet": {
                        "Id": "subnet-004ff41eccb4d1194",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:subnet/subnet-004ff41eccb4d1194"
                    },
                    "Vpc": {
                        "Id": "vpc-f1663d98ad28331c7",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-f1663d98ad28331c7"
                    },
                    "AdditionalDetails": [],
                    "Explanations": []
                },
                {
                    "SequenceNumber": 3,
                    "Component": {
                        "Id": "sg-02f0d35a850ba727f",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:security-group/sg-02f0d35a850ba727f"
                    },
                    "AdditionalDetails": [],
                    "Explanations": []
                },
                {
                    "SequenceNumber": 4,
                    "AclRule": {
                        "Cidr": "0.0.0.0/0",
                        "Egress": true,
                        "Protocol": "all",
                        "RuleAction": "allow",
                        "RuleNumber": 100
                    },
                    "Component": {
                        "Id": "acl-0a8e20a0a9f144d36",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:network-acl/acl-0a8e20a0a9f144d36"
                    },
                    "AdditionalDetails": [],
                    "Explanations": []
                },
                {
                    "SequenceNumber": 5,
                    "Component": {
                        "Id": "rtb-0d49a54c0a8c0bd9b",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:route-table/rtb-0d49a54c0a8c0bd9b"
                    },
                    "RouteTableRoute": {
                        "DestinationCidr": "0.0.0.0/0",
                        "GatewayId": "igw-0797cccdc9d73b0e5",
                        "Origin": "createroute",
                        "State": "active"
                    },
                    "AdditionalDetails": [],
                    "Explanations": []
                },
                {
                    "SequenceNumber": 6,
                    "Component": {
                        "Id": "igw-0797cccdc9d73b0e5",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:internet-gateway/igw-0797cccdc9d73b0e5"
                    },
                    "OutboundHeader": {
                        "DestinationAddresses": ["0.0.0.0/5", "11.0.0.0/8", "12.0.0.0/6", ...],
                        "DestinationPortRanges": [{
                            "From": 0,
                            "To": 65535
                        }],
                        "Protocol": "6",
                        "SourceAddresses": ["34.230.71.227/32"],
                        "SourcePortRanges": [{
                            "From": 22,
                            "To": 22
                        }]
                    },
                    "Vpc": {
                        "Id": "vpc-f1663d98ad28331c7",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-f1663d98ad28331c7"
                    },
                    "AdditionalDetails": [],
                    "Explanations": []
                }
            ],
            "Tags": []
        }
    ]
}
```

## Step 4: Delete the path

If you no longer need the path, you can delete it. Before you can delete the path, you
must delete its analyses.

###### To delete the path

1. Use the following [delete-network-insights-analysis](../../../cli/latest/reference/ec2/delete-network-insights-analysis.md "../../../cli/latest/reference/ec2/delete-network-insights-analysis.md") command to delete the path analysis.

```
aws ec2 delete-network-insights-analysis --network-insights-analysis-id `nia-02207aa13eb480c7a`
```

2. Use the following [delete-network-insights-path](../../../cli/latest/reference/ec2/delete-network-insights-path.md "../../../cli/latest/reference/ec2/delete-network-insights-path.md") to delete the path.

```
aws ec2 delete-network-insights-path --network-insights-path-id `nip-0b26f224f1d131fa8`
```

If you keep the path, note that Reachability Analyzer will automatically delete the analysis 120
days after its creation date.

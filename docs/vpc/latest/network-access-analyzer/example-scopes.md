# Example Network Access Scopes in Network Access Analyzer

The following are examples of Network Access Scopes.

###### Example: Identify all traffic between two subnets

To identify traffic between two subnets that are intended to be isolated from each
other, create an access scope with two match conditions. The first condition identifies paths
from network interfaces in the first subnet to network interfaces in the second subnet. The
second condition identifies paths from network interfaces in second subnet to network interfaces
in the first subnet.

```
{
    "MatchPaths": [
        {
            "Source": {
                "ResourceStatement": {
                    "Resources": [ "`subnet-1-id`" ]
                }
            },
            "Destination": {
                "ResourceStatement": {
                    "Resources": [ "`subnet-2-id`" ]
                }
            }
        },
        {
            "Source": {
                "ResourceStatement": {
                    "Resources": [ "`subnet-2-id`" ]
                }
            },
            "Destination": {
                "ResourceStatement": {
                    "Resources": [ "`subnet-1-id`" ]
                }
            }
        }
    ]
}
```

###### Example: Use resource groups with Network Access Scopes

To identify paths to or from resources with specific resource tags, you can use AWS
resource groups. With resource groups, you define a set of resources that contain a specific
tag. For more information, see [Build a tag-based query and create a
group](../../../ARG/latest/userguide/gettingstarted-query.md "../../../ARG/latest/userguide/gettingstarted-query.md").

The following example identifies inbound paths to any Amazon EC2 instances in the specified
resource group.

```
{
    "MatchPaths": [
        {
            "Destination": {
                "ResourceStatement": {
                    "Resources": [
                        "arn:aws:resource-groups:us-east-1:123456789012:group/bastions"
                    ]
                }
            }
        }
    ]
}
```

To identify inbound paths to bastion hosts that use a port other than port 22 (SSH),
combine the match condition in the previous example with an exclude condition that specifies
destination port 22.

```
{
    "MatchPaths": [
        {
            "Destination": {
                "ResourceStatement": {
                    "Resources": [
                        "arn:aws:resource-groups:us-east-1:123456789012:group/bastions"
                    ]
                }
            }
        }
    ],
    "ExcludePaths": [
        {
            "Destination": {
                "PacketHeaderStatement": {
                    "DestinationPorts": [
                        "22"
                    ]
                }
            }
        }
    ]
}
```

###### Example: Identify all inbound traffic from the public internet, except for a trusted CIDR range

The following example identifies traffic from the internet while excluding paths that
start from a trusted address range.

```
{
    "MatchPaths": [
        {
            "Source": {
                "ResourceStatement": {
                    "ResourceTypes": [
                        "AWS::EC2::InternetGateway"
                    ]
                }
            }
        }
    ],
    "ExcludePaths": [
        {
            "Source": {
                "PacketHeaderStatement": {
                    "SourceAddresses": [
                        "`55.3.0.0/16`"
                    ]
                }
            }
        }
    ]
}
```

###### Example: Exclude traffic that originates at the addresses in a prefix list

The following example identifies traffic to the public internet while excluding traffic
that originates at the addresses in the specified prefix list.

```
{
    "MatchPaths": [
        {
            "Source": {
                "ResourceStatement": {
                    "ResourceTypes": [
                        "AWS::EC2::InternetGateway"
                    ]
                }
            }
        }
    ],
    "ExcludePaths": [
        {
            "Source": {
                "PacketHeaderStatement": {
                    "SourcePrefixLists": [
                        "`pl-02cd2c6b`"
                    ]
                }
            }
        }
    ]
}
```

###### Example: Identify all outbound traffic to the public internet, excluding a trusted CIDR range

The following example identifies traffic to the public internet while excluding a
trusted address range.

```
{
    "MatchPaths": [
        {
            "Destination": {
                "ResourceStatement": {
                    "ResourceTypes": [
                        "AWS::EC2::InternetGateway"
                    ]
                }
            }
        }
    ],
    "ExcludePaths": [
        {
            "Destination": {
                "PacketHeaderStatement": {
                    "DestinationAddresses": [
                        "`55.3.0.0/16`"
                    ]
                }
            }
        }
    ]
}
```

###### Example: Identify inbound traffic that bypasses a network firewall

The following example identifies inbound traffic to network interfaces in a subnet that
bypasses a network firewall.

```
{
    "MatchPaths": [
        {
            "Source": {
                "ResourceStatement": {
                    "ResourceTypes": [
	                  "AWS::EC2::InternetGateway"
                    ]
                }
            },
            "Destination": {
                "ResourceStatement": {
                    "Resources": [
                        "`subnet-814424dd`"
                    ]
                }
            }
        }
    ],
    "ExcludePaths": [
        {
            "ThroughResources": [
                {
                    "ResourceStatement": {
                        "ResourceTypes": [
                            "AWS::NetworkFirewall::Firewall"
                        ]
                    }
                }
            ]
        }
    ]
}
```

###### Example: Identify traffic to network interface with a specific security group

The following example identifies traffic to network interfaces with a specific security
group.

```
{
    "MatchPaths": [
        {
            "Source": {
                "ResourceStatement": {
                    "ResourceTypes": [
                        "AWS::EC2::InternetGateway"
                    ]
                }
            },
	      "Destination": {
	          "ResourceStatement": {
	              "Resources": [
	                  "`sg-f15d59b3`"
	              ]
	          }
	      }
	  }
    ]
}
```

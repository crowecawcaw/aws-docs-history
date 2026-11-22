

# Writing context-aware rules

You author rules that match on the context of a flow's source or destination: its VPC, subnet, transit gateway attachment, or Amazon VPC security group. This works in the firewall and IPS rule groups of a Next Generation Firewall policy, including rule groups that you embed directly in the policy, and in the Suricata compatible rule strings (`RulesString`) and structured stateful rules (`StatefulRules`) of a Classic stateful rule group.

**Note**  
When you update a rule group, provide the full rule group object, including `RuleVariables`. An update that omits the variables removes your context sets.

The following examples show common context-aware rule patterns, first in firewall rule groups and then in IPS rule groups.

**Example: Allow HTTPS from application subnets to database subnets**  
The following firewall rule group allows HTTPS from application subnets to database subnets. The context sets in `RuleVariables` group the subnet IDs that `$APP_SUBNETS` and `$DB_SUBNETS` reference. The rule group definition is in a local file named `firewall-rules.json`:

```
{
    "RuleVariables": {
        "ContextSets": {
            "APP_SUBNETS": {
                "Definition": [
                    "subnet-1234567890abcdef0",
                    "subnet-021345abcdef6789a"
                ]
            },
            "DB_SUBNETS": {
                "Definition": [
                    "subnet-0abc123def4567890"
                ]
            }
        }
    },
    "RulesSource": {
        "RulesString": "accept:flow tcp:all $APP_SUBNETS any -> $DB_SUBNETS 443 (sid:1001;)"
    }
}
```

```sh
aws network-firewall create-rule-group \
--type FIREWALL --capacity 100 \
--rule-group-name example-context-firewall-rule-group \
--firewall-rule-group file://firewall-rules.json \
--region us-west-2
```

**Example: Block SSH from production resources**  
The following firewall rule group blocks SSH from a set of production VPCs and an Amazon VPC security group to anywhere outside your home networks. The context set mixes resource types:

```
{
    "RuleVariables": {
        "ContextSets": {
            "PROD_RESOURCES": {
                "Definition": [
                    "vpc-1234567890abcdef0",
                    "vpc-021345abcdef6789a",
                    "sg-1234567890abcdef0"
                ]
            }
        }
    },
    "RulesSource": {
        "RulesString": "drop:flow tcp:all $PROD_RESOURCES any -> $EXTERNAL_NET 22 (msg:\"Block SSH from production to external\"; sid:2001;)"
    }
}
```

**Example: Combine context sets with IP sets and port sets**  
Context sets, IP sets, and port sets can appear together in one firewall rule. The following rule blocks administrative ports from production VPCs to a restricted IP range:

```
{
    "RuleVariables": {
        "IPSets": {
            "RESTRICTED_IPS": {
                "Definition": [
                    "203.0.113.0/24",
                    "198.51.100.0/24"
                ]
            }
        },
        "PortSets": {
            "ADMIN_PORTS": {
                "Definition": [
                    "22",
                    "3389"
                ]
            }
        },
        "ContextSets": {
            "PROD_VPCS": {
                "Definition": [
                    "vpc-1234567890abcdef0",
                    "vpc-021345abcdef6789a"
                ]
            }
        }
    },
    "RulesSource": {
        "RulesString": "drop:flow tcp:all $PROD_VPCS any -> $RESTRICTED_IPS $ADMIN_PORTS (msg:\"Block admin access from production to restricted ranges\"; sid:2002;)"
    }
}
```

**Example: Segment application tiers by security group**  
The following firewall rule allows HTTPS from a web tier Amazon VPC security group set to an application tier Amazon VPC security group set:

```
{
    "RuleVariables": {
        "ContextSets": {
            "WEB_TIER": {
                "Definition": [
                    "sg-1234567890abcdef0",
                    "sg-0abc123def4567890"
                ]
            },
            "APP_TIER": {
                "Definition": [
                    "sg-0123456789abcdef0",
                    "sg-0fedcba9876543210"
                ]
            }
        }
    },
    "RulesSource": {
        "RulesString": "accept:flow tcp:all $WEB_TIER any -> $APP_TIER 443 (msg:\"Allow HTTPS from web tier to application tier\"; sid:2003;)"
    }
}
```

**Example: Isolate database subnets**  
The following firewall rules allow only application subnets to reach database subnets on database ports, and block all other access to those ports:

```
accept:flow tcp:all $APP_SUBNETS any -> $DB_SUBNETS [3306,5432] (msg:"Allow application to database subnets"; sid:2004;)
drop:flow tcp:all any any -> $DB_SUBNETS [3306,5432] (msg:"Block all other access to database subnets"; sid:2005;)
```

**Example: Block UDP from on-premises attachments**  
In an IPS rule group, context IDs work the same way: reference the set by name in a Suricata compatible rule. You can use transit gateway attachment IDs to match traffic by where it enters your network. The following IPS rule blocks UDP from your Direct Connect attachments. Context IDs in the source position work with any protocol:

```
drop udp $ON_PREM any -> any any (msg:"Block UDP from on-premises attachments"; sid:2006;)
```

**Example: Alert on admin paths from application subnets**  
The following IPS rule combines a source context ID with application-layer matching. It alerts on HTTP requests for an admin path from your application subnets:

```
alert http $APP_SUBNETS any -> any any (http.uri; content:"/admin"; msg:"HTTP request to an admin path from application subnets"; sid:2007;)
```

Keep the following in mind when you write context-aware rules:
+ Context set names start with a letter, use only letters, digits, and underscores, and can be up to 32 characters. Use a name that is unique across `ContextSets`, `IPSets`, and `PortSets`.
+ The context IDs in your rules must be IDs that `ListResourcesInContextStore` returns for the context store. See [Listing context stores and their resources](context-aware-rules-getting-started.md#context-aware-rules-list-apis). The supported ID formats are `vpc-`, `sg-`, `subnet-`, and `tgw-attach-` IDs, and Network Firewall validates the format when you create or update the rule group. Network Firewall resolves the IDs when the policy deploys to each firewall, not when you create the rule group. An ID that the store doesn't recognize matches nothing. See [My rule references a context ID that isn't in the context store](troubleshooting-context-aware-rules.md#troubleshoot-context-unknown-id).
+ If you delete a resource that a rule references, for example an Amazon VPC security group, the rule keeps matching the remaining IDs in the set. You don't need to update the rule right away. The context store sync state shows that some referenced resources no longer resolve, and you can remove those IDs from the rule when convenient. This is safe because a deleted ID can't come back, so no traffic carries it. For help, see [How do I check the context store sync state?](troubleshooting-context-aware-rules.md#troubleshoot-context-sync-state).
+ Context IDs in the source position work with any protocol. Rules that place a context ID in the destination position must use TCP or a TCP-based application protocol. For the reasons and the behavior details, see [Matching on destination context](context-aware-rules-destination.md).
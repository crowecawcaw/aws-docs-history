# Network Firewall | Create Firewall Policy (Managed Automation)

Create a network firewall policy with specified configuration and rule group references.

**Full classification:** Management | Managed firewall | Network firewall | Create firewall policy (managed automation)

## Change Type Details

|                             |                           |
| --------------------------- | ------------------------- |
| Change type ID              | ct-16c7yzpkb2a6n          |
| Current version             | 1.0                       |
| Expected execution duration | 60 minutes                |
| AWS approval                | Required                  |
| Customer approval           | Not required if submitter |
| Execution mode              | Manual                    |

## Additional Information

Info not available.

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-16c7yzpkb2a6n](schemas.md#ct-16c7yzpkb2a6n-schema-section "schemas.md#ct-16c7yzpkb2a6n-schema-section").

## Example: Required Parameters

```
{
  "FirewallPolicyName": "MyFirewallPolicy",
  "StatelessDefaultActions": [
    "aws:pass"
  ],
  "StatelessFragmentDefaultActions": [
    "aws:drop"
  ]
}
```

## Example: All Parameters

```
{
  "FirewallPolicyName": "ComprehensiveFirewallPolicy",
  "Description": "Complete network firewall policy with all parameters configured.",
  "StreamExceptionPolicy": "DROP",
  "StatelessDefaultActions": [
    "aws:pass"
  ],
  "StatelessFragmentDefaultActions": [
    "aws:forward_to_sfe"
  ],
  "StatelessRuleGroupReferences": [
    {
      "Priority": 100,
      "ResourceArn": "arn:aws:network-firewall:us-east-1:123456789012:stateless-rulegroup/MyStatelessRuleGroup"
    }
  ],
  "StatefulRuleOrder": "DEFAULT_ACTION_ORDER",
  "StatefulRuleGroupReferences": [
    {
      "ResourceArn": "arn:aws:network-firewall:us-east-1:123456789012:stateful-rulegroup/MyStatefulRuleGroup"
    }
  ],
  "Priority": "High"
}
```

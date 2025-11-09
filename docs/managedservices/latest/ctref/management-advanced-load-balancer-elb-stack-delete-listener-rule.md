# Load Balancer (ELB) Stack | Delete Listener Rule

Delete the specified listener rule for Application Load Balancers. Default rules canÆt be deleted. This change performs direct API actions regardless of whether the ALB is part of a stack as it might cause stack drift.

**Full classification:** Management | Advanced stack components | Load balancer (ELB) stack | Delete listener rule

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-2qsgbfmrw92zw |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

Info not available.

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-2qsgbfmrw92zw](schemas.md#ct-2qsgbfmrw92zw-schema-section "schemas.md#ct-2qsgbfmrw92zw-schema-section").

## Example: Required Parameters

```
Example not available.
```

## Example: All Parameters

```
{
  "DocumentName": "AWSManagedServices-DeleteListenerRule",
  "Region": "us-east-1",
  "Parameters": {
    "ListenerRuleArn": [
      "arn:aws:elasticloadbalancing:us-east-1:123456789012:listener-rule/app/my-alb/abc01234abc01234/abc01234abc01234/abc01234abc01234"
    ]
  }
}
```

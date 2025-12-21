# Load Balancer (ELB) Stack | Update Deletion Protection

Update the deletion protection setting for Elastic Load Balancers (Application, Network, Gateway Load Balancers) through direct API calls regardless of if the ELB is part of a CloudFormation stack.

**Full classification:** Management | Advanced stack components | Load Balancer (ELB) stack | Update deletion protection

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-28yh0fnzhubnh |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

Info not available.

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-28yh0fnzhubnh](schemas.md#ct-28yh0fnzhubnh-schema-section "schemas.md#ct-28yh0fnzhubnh-schema-section").

## Example: Required Parameters

```
{
  "DocumentName": "AWSManagedServices-UpdateELBDeletionProtectionV2",
  "Region": "us-east-1",
  "Parameters": {
    "ElasticLoadBalancerArns": [
      "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188"
    ],
    "DeletionProtection": "true"
  }
}

```

## Example: All Parameters

```
{
  "DocumentName": "AWSManagedServices-UpdateELBDeletionProtectionV2",
  "Region": "us-west-2",
  "Parameters": {
    "ElasticLoadBalancerArns": [
      "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-app-lb/50dc6c495c0c9188",
      "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/net/my-net-lb/50dc6c495c0c9189"
    ],
    "DeletionProtection": "false"
  }
}

```

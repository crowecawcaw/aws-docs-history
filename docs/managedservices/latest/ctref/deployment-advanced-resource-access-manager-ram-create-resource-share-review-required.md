# Resource Access Manager (RAM) | Create Resource Share (Review Required)

Create a resource share through Resource Access Manager (RAM) to share supported AWS resources. You can share resources with AWS accounts that come under the same customer contract. If you are in an organization, you can share with that organization's organizational units or with the entire organization. You can also share with IAM Roles, IAM Users, and Service Principals using their respective ARNs.

**Full classification:** Deployment | Advanced stack components | Resource Access Manager (RAM) | Create resource share (review required)

## Change Type Details

|                             |                           |
| --------------------------- | ------------------------- |
| Change type ID              | ct-054ysptoo4gyk          |
| Current version             | 1.0                       |
| Expected execution duration | 240 minutes               |
| AWS approval                | Required                  |
| Customer approval           | Not required if submitter |
| Execution mode              | Manual                    |

## Additional Information

Info not available.

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-054ysptoo4gyk](schemas.md#ct-054ysptoo4gyk-schema-section "schemas.md#ct-054ysptoo4gyk-schema-section").

## Example: Required Parameters

```
Example not available.
```

## Example: All Parameters

```
{
  "Region": "us-east-1",
  "ResourceShareName": "TestResourceShare",
  "Resources": [
    "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-12345",
    "arn:aws:ec2:us-east-1:123456789012:subnet/subnet-0abc123def456789a"
  ],
  "Principals": [
    "111122223333"
  ]
}
```

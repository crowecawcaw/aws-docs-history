

# Resource: Restrict the Amazon EC2 tags a principal can set on compute resources
<a name="iam-example-restrict-compute-environment-tags"></a>

Use the following policy to control the tags a principal sets when they create or update a compute environment. The policy requires the principal to always set a `CostCenter` compute resource tag with an approved value and a `Team` compute resource tag. This policy demonstrates how to use the `batch:ComputeResourcesTag/{{tag-key}}` condition key to enforce a tagging convention on the Amazon EC2 instances that a compute environment manages. For more information, see [Control access to compute resource tags with condition keys](compute-resources-tag-access-policy.md). To also restrict which tag keys a principal can set, use the complementary `batch:ComputeResourcesTagKeys` condition key. For an example, see [Example: Restrict the compute resource tag keys a principal can set](compute-resources-tag-access-policy-tagkeys-example.md).

The first statement allows the compute environment actions when the `CostCenter` tag is `engineering`. The second statement denies the actions whenever a request omits the `Team` compute resource tag, whether or not the request sets any other compute resource tags.

**Requires a Team tag on every request**  
This policy denies every compute environment create or update that doesn't include a `Team` compute resource tag. AWS Batch evaluates `batch:ComputeResourcesTag/{{tag-key}}` only when your request includes `computeResources.tags`. The `Null` condition operator in the second statement matches whenever the `Team` compute resource tag is absent. This includes a request that sets no compute resource tags at all.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowApprovedCostCenterTag",
      "Effect": "Allow",
      "Action": [
        "batch:CreateComputeEnvironment",
        "batch:UpdateComputeEnvironment"
      ],
      "Resource": "arn:aws:batch:*:*:compute-environment/*",
      "Condition": {
        "StringEquals": {
          "batch:ComputeResourcesTag/CostCenter": "engineering"
        }
      }
    },
    {
      "Sid": "DenyMissingTeamTag",
      "Effect": "Deny",
      "Action": [
        "batch:CreateComputeEnvironment",
        "batch:UpdateComputeEnvironment"
      ],
      "Resource": "arn:aws:batch:*:*:compute-environment/*",
      "Condition": {
        "Null": {
          "batch:ComputeResourcesTag/Team": "true"
        }
      }
    }
  ]
}
```


# Example: Allow compute resource tags for specific keys and values
<a name="compute-resources-tag-access-policy-example"></a>

The following identity-based policy allows a principal to create and update compute environments only when the request sets the `CostCenter` compute resource tag to `engineering`. The `Allow` statement requires that value, and the `Deny` statement uses the `Null` operator on `batch:ComputeResourcesTag/CostCenter` to reject any request that omits the `CostCenter` tag. AWS Batch populates `batch:ComputeResourcesTag/{{tag-key}}` only when a request includes `computeResources.tags`.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowComputeEnvironmentManagement",
      "Effect": "Allow",
      "Action": [
        "batch:CreateComputeEnvironment",
        "batch:UpdateComputeEnvironment"
      ],
      "Resource": "arn:aws:batch:us-east-1:123456789012:compute-environment/*",
      "Condition": {
        "StringEquals": {
          "batch:ComputeResourcesTag/CostCenter": "engineering"
        }
      }
    },
    {
      "Sid": "DenyMissingCostCenterTag",
      "Effect": "Deny",
      "Action": [
        "batch:CreateComputeEnvironment",
        "batch:UpdateComputeEnvironment"
      ],
      "Resource": "arn:aws:batch:us-east-1:123456789012:compute-environment/*",
      "Condition": {
        "Null": {
          "batch:ComputeResourcesTag/CostCenter": "true"
        }
      }
    }
  ]
}
```

To prevent a principal from setting a specific compute resource tag while still allowing them to create and update compute environments that don't set that tag, attach a policy with an explicit `Deny` that matches on the tag key:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "batch:CreateComputeEnvironment",
        "batch:UpdateComputeEnvironment"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "batch:ComputeResourcesTag/CostCenter": "*"
        }
      }
    }
  ]
}
```
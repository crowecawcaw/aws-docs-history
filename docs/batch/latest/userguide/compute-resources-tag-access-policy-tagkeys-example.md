

# Example: Restrict the compute resource tag keys a principal can set
<a name="compute-resources-tag-access-policy-tagkeys-example"></a>

The following identity-based policy, which you attach to an IAM user or role, allows a principal to create and update compute environments, but only when every tag key in `computeResources.tags` is `CostCenter`, `Team`, or `Project`. Requests that set any other tag key are denied.

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
        "ForAllValues:StringEquals": {
          "batch:ComputeResourcesTagKeys": ["CostCenter", "Team", "Project"]
        }
      }
    }
  ]
}
```

This policy restricts the request to the allowed tag keys, but it doesn't require the request to set any of them. The `ForAllValues` set operator is satisfied even when the request sets no compute resource tags. To also require that a specific tag key is always present, add a statement that uses the `Null` operator on `batch:ComputeResourcesTag/{{tag-key}}`. For an example, see [Resource: Restrict the Amazon EC2 tags a principal can set on compute resources](iam-example-restrict-compute-environment-tags.md).

You can combine both condition keys in a single statement to restrict the allowed tag keys and the value permitted for one of those keys at the same time. The following policy allows a principal to create and update compute environments only when the `CostCenter` tag value is `engineering`, and only when no tag key other than `CostCenter`, `Team`, or `Project` is used.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowComputeEnvironmentManagementWithApprovedTags",
      "Effect": "Allow",
      "Action": [
        "batch:CreateComputeEnvironment",
        "batch:UpdateComputeEnvironment"
      ],
      "Resource": "arn:aws:batch:us-east-1:123456789012:compute-environment/*",
      "Condition": {
        "StringEquals": {
          "batch:ComputeResourcesTag/CostCenter": "engineering"
        },
        "ForAllValues:StringEquals": {
          "batch:ComputeResourcesTagKeys": ["CostCenter", "Team", "Project"]
        }
      }
    }
  ]
}
```
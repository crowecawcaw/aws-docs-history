

# Example: Allow capacity tags for specific keys and values
<a name="capacity-tags-access-policy-example"></a>

The following identity-based policy, which you attach to an IAM user or role, allows a principal to create and update compute environments and to set capacity tags, but only when the `CostCenter` tag value is `engineering` or `ops` and no tag keys other than `CostCenter` and `Team` are used. Requests that include any other tag key or a different `CostCenter` value are denied.

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
      "Resource": "arn:aws:batch:us-east-1:123456789012:compute-environment/*"
    },
    {
      "Sid": "AllowSetCapacityTagsForApprovedTags",
      "Effect": "Allow",
      "Action": "batch:SetCapacityTags",
      "Resource": "arn:aws:batch:us-east-1:123456789012:compute-environment/*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/CostCenter": ["engineering", "ops"]
        },
        "ForAllValues:StringEquals": {
          "aws:TagKeys": ["CostCenter", "Team"]
        }
      }
    }
  ]
}
```

To deny capacity tagging entirely while still permitting compute environment creation and updates, attach a policy with an explicit `Deny` on `batch:SetCapacityTags`:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "batch:SetCapacityTags",
      "Resource": "*"
    }
  ]
}
```
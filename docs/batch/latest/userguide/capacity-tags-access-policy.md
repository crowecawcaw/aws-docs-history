# Control access to capacity tags with `batch:SetCapacityTags`

When you create or update an Amazon ECS Managed Instances compute environment, you can specify
`computeResources.capacityTags` to apply tags to the Amazon ECS capacity provider and the
Amazon EC2 instances that the compute environment manages. To set this field, your IAM principal
must have permission for the `batch:SetCapacityTags` action on the compute environment
resource. For more information about the field, see [Compute environments on Amazon ECS Managed Instances](ecs-managed-instances-compute-environments.md "ecs-managed-instances-compute-environments.md").

###### Important

Capacity tags are currently only applicable to Amazon ECS Managed Instances compute
environments. The `capacityTags` field and the `batch:SetCapacityTags`
action do not apply to Fargate, Amazon EC2, or Amazon EKS compute environments.

`batch:SetCapacityTags` is a permission-only action. It is not a standalone API
operation. Instead, AWS Batch evaluates it as an additional authorization check whenever a
`CreateComputeEnvironment` or `UpdateComputeEnvironment` request includes
`capacityTags`. If the request does not include `capacityTags`, the check
is not performed.

The action supports the following condition keys, which let you control exactly which tags a
principal can apply:

- `aws:RequestTag/`tag-key`` — Restricts the values
  that can be set for a given tag key.
- `aws:TagKeys` — Restricts the set of tag keys that can be
  specified.

###### Important

Because `batch:SetCapacityTags` is evaluated only when `capacityTags`
is present, an explicit `Deny` on this action prevents a principal from setting
capacity tags while still allowing them to create and update compute environments that do not
use `capacityTags`.

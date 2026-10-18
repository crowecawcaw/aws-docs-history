

# Control access to compute resource tags with condition keys
<a name="compute-resources-tag-access-policy"></a>

The following actions support both the `batch:ComputeResourcesTag/{{tag-key}}` and `batch:ComputeResourcesTagKeys` condition keys:
+ `batch:CreateComputeEnvironment`
+ `batch:UpdateComputeEnvironment`

Before you write a policy that controls compute resource tags, note the following:
+ When you create or update a AWS Batch compute environment, you can specify `computeResources.tags` to apply Amazon EC2 tags to the instances that the compute environment launches.
+ To control which tags a principal can set in this field, use the `batch:ComputeResourcesTag/{{tag-key}}` condition key in an IAM policy.
+ When your `CreateComputeEnvironment` or `UpdateComputeEnvironment` request includes `computeResources.tags`, AWS Batch evaluates this condition key.

The `batch:ComputeResourcesTag/{{tag-key}}` condition key is the compute resource equivalent of the global `aws:RequestTag/{{tag-key}}` condition key. For each tag in the `computeResources.tags` map, AWS Batch provides a single-valued `batch:ComputeResourcesTag/{{tag-key}}` entry whose value is that tag's value. Because the entry is single-valued, compare it against one string value with an operator such as `StringEquals` or `StringLike`. Use these entries to allow or deny a request based on the keys and values that the request sets.

With AWS Batch, you can also use the `batch:ComputeResourcesTagKeys` condition key, the compute resource equivalent of the global `aws:TagKeys` condition key. Instead of matching tag values, `batch:ComputeResourcesTagKeys` matches against the set of tag *keys* present in the `computeResources.tags` map. Use it with the `ForAllValues` or `ForAnyValue` set operators to control which tag keys a principal is allowed to set, independent of the values assigned to those keys.

The two condition keys are complementary: `batch:ComputeResourcesTag/{{tag-key}}` restricts the *values* allowed for a given tag key, and `batch:ComputeResourcesTagKeys` restricts the *set of keys* allowed in the request. Use them together to control both which tag keys a principal can set and which values those keys can take. If a tag in `computeResources.tags` has a null value, its key still appears in the `batch:ComputeResourcesTagKeys` set.

**These condition keys evaluate only computeResources.tags**  
The Amazon EC2 tags that these condition keys authorize must be set in the compute environment's `computeResources.tags` field. These condition keys don't evaluate tags in the Amazon EC2 launch template of the compute environment. To control the tags that principals can apply through launch templates, restrict access to the launch templates themselves and to the `ec2:CreateLaunchTemplate` and `ec2:CreateLaunchTemplateVersion` actions.  
AWS Batch merges launch template tags and `computeResources.tags` before applying them to the launched Amazon EC2 instances. `computeResources.tags` takes precedence when a tag key is present in both `computeResources.tags` and the launch template. For more information about how AWS Batch merges launch template and compute environment tags, see [Use Amazon EC2 launch templates with AWS Batch](launch-templates.md).
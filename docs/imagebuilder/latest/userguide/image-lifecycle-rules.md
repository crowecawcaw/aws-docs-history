# How lifecycle management rules work for Image Builder image resources

Image lifecycle policies use the lifecycle rules that you define to implement your overall
resource management strategy. The rules that you define help ensure the freshness of your available
images and minimize costs for underlying infrastructure such as snapshot storage for output AMIs, or
ECR repository storage and data transfer rates for container images.

You can configure the following types of rules for your policies.

**Deprecate rule**

Sets the Image Builder image resource status to `Deprecated`. Image Builder pipelines still
run for deprecated images. You can optionally set the deprecation time for associated AMIs without
affecting your ability to launch new instances.

When an AMI is deprecated, it's ignored by general searches. For example, if you run the
Amazon EC2 **describe-images** command in the AWS CLI, it would not return deprecated
AMIs in the result set. However, you can still find deprecated AMIs with their AMI ID.

_This rule is not available for container images._

**Disable rule**

Sets the Image Builder image resource status to `Disabled`. This prevents Image Builder
pipelines from running for this image. You can optionally disable the associated AMI
to prevent new instance launches.

When an AMI is disabled, it becomes private and can't be used to launch new instances. If
you shared the AMI with any accounts, organizations, or organizational units, they lose access
to your AMI when it becomes private.

_This rule is not available for container images._

**Delete rule**

Deletes the image resources by age or by count. You define the threshold that meets your
needs. When an Image Builder image resource passes the threshold, it's removed. You can optionally
deregister associated AMIs or delete the snapshots for those AMIs. You can also specify tags
for resources that you want to retain past the threshold.

For container images, this rule deletes the Image Builder container image resource. You can optionally
remove container images that were distributed to ECR repositories to prevent them from being
used to run new containers.

###### Contents

- [AMI lifecycle exclusion rules](#image-lifecle-rules-exclusions "#image-lifecle-rules-exclusions")
- [View lifecycle management rule details for a policy](#image-lifecycle-rule-view "#image-lifecycle-rule-view")

## AMI lifecycle exclusion rules

The following exclusion rules define exceptions to the lifecycle rules for AMIs. AMIs that
meet the criteria specified by the exclusion rules are
excluded from lifecycle actions. Exclusion rules are not available in the AWS Management Console.

The following terms use API notation from the `LifecyclePolicyDetailExclusionRules` data type.

###### Exclusion rules

amis

Contains the settings in `LifecyclePolicyDetailExclusionRulesAmis`
shown in the list that follows.

tagMap

You can provide a list of up to 50 tags that skip lifecycle actions for
any type of resource.

The following terms use API notation from the `LifecyclePolicyDetailExclusionRulesAmis` data type.

###### AMI exclusion rules

isPublic

Configures whether public AMIs are excluded from the lifecycle action.

lastLaunched

Specifies configuration details for Image Builder to exclude the most recent resources from lifecycle actions.

regions

Configures AWS Regions that are excluded from the lifecycle action.

sharedAccounts

Specifies AWS accounts whose resources are excluded from the lifecycle action.

tagMap

Lists tags that should be excluded from lifecycle actions for the AMIs that have them.

## View lifecycle management rule details for a policy

Rules are defined within the lifecycle management policies that you create for your Image Builder image resources.
In the console, the lifecycle policy details page has a [Rules tab](view-lifecycle-policy.md#view-lifecycle-policy-console-rules-tab "view-lifecycle-policy.md#view-lifecycle-policy-console-rules-tab") that shows the details of the rules that you
configured for the policy.

To get policy details in the AWS CLI, you can run the [get-lifecycle-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-lifecycle-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-lifecycle-policy.html") command. The policy details in
the response contain a list of the actions (rules) that you defined for the policy, that include all of
your configured settings.

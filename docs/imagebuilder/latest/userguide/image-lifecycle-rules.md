

# How lifecycle management rules work for Image Builder image resources
<a name="image-lifecycle-rules"></a>

Lifecycle rules keep your images fresh and reduce infrastructure costs, such as snapshot storage for output AMIs and Amazon ECR repository storage for containers.

Lifecycle policies support these rule types:

**Deprecate rule**  
Sets the Image Builder image resource status to `Deprecated`. Image Builder pipelines still run for deprecated images. You can optionally set the deprecation time for associated AMIs without affecting your ability to launch new instances.  
Deprecated AMIs do not appear in general searches. For example, the Amazon EC2 **describe-images** command excludes deprecated AMIs from results. To find a deprecated AMI, specify its AMI ID directly.  
This rule does not apply to container-based images.

**Disable rule**  
Sets the Image Builder image resource status to `Disabled`. This prevents Image Builder pipelines from running for this image. You can optionally disable the associated AMI to prevent new instance launches.  
A disabled AMI becomes private and no longer launches new instances. Accounts, organizations, or organizational units that previously had shared access lose that access.  
This rule does not apply to container-based images.

**Delete rule**  
Deletes the image resources by age or by count. You define the threshold that meets your needs. When an Image Builder image resource passes the threshold, it's removed. You can optionally deregister associated AMIs or delete the snapshots for those AMIs. You can also specify tags for resources that you want to retain past the threshold.  
For container images, this rule deletes the Image Builder container image resource. You can also remove container images from ECR repositories to prevent new container launches.

## Rule priority and evaluation order
<a name="image-lifecycle-rule-priority"></a>

When a policy has multiple rule types, Image Builder evaluates each resource in this order:

1. Deprecate rule

1. Disable rule

1. Delete rule

**Important**  
Only one action applies to each resource per execution. If a resource matches a deprecate rule, Image Builder deprecates it and skips the disable and delete rules for that resource during the same run. In subsequent executions, Image Builder evaluates the resource against other rules if it meets their criteria.

This priority order supports a progressive lifecycle strategy. For example, you can configure a policy to deprecate images after 90 days, disable them after 120 days, and delete them after 180 days. Each execution applies only the highest-priority matching action.

**Image states that skip rule evaluation**  
Image Builder skips images in certain states to prevent duplicate actions:
+ **Deprecate rule** – Image Builder skips images that are already deprecated, disabled, failed, or canceled.
+ **Disable rule** – Image Builder skips images that are already disabled, failed, or canceled.
+ **Delete rule** – Image Builder evaluates images in any state for deletion, subject to retention rules and exclusions.

**Topics**
+ [Rule priority and evaluation order](#image-lifecycle-rule-priority)
+ [AMI lifecycle exclusion rules](#image-lifecycle-rules-exclusions)
+ [Tags as resource selectors vs. exclusion rules](#image-lifecycle-tags-selector-vs-exclusion)
+ [How retention is calculated](#image-lifecycle-rules-retention)
+ [How lifecycle actions affect associated resources](#image-lifecycle-action-scope)
+ [Allowed resource state transitions](#image-lifecycle-state-transitions)
+ [View rule details for a lifecycle policy](#image-lifecycle-rule-view)

## AMI lifecycle exclusion rules
<a name="image-lifecycle-rules-exclusions"></a>

Exclusion rules protect specific AMIs from lifecycle actions. Configure exclusion rules in the AWS Management Console, the API, or the AWS CLI.

Lifecycle policies support these exclusion rule types:
+ **Tag-based exclusion** – Excludes Image Builder image resources with specific tags (up to 50 tags). For more information about how tags work at different resource levels, see [Tags as resource selectors vs. exclusion rules](#image-lifecycle-tags-selector-vs-exclusion).
+ **Public AMI exclusion** – Excludes publicly shared AMIs.
+ **Last launched exclusion** – Excludes AMIs that launched an instance within a specified time period.
**Note**  
Amazon EC2 reports the last launched time with a 24-hour delay. Launches within the last 24 hours might not be reflected when the exclusion check runs.
+ **Region exclusion** – Excludes AMIs in specific AWS Regions.
+ **Shared account exclusion** – Excludes AMIs shared with specific AWS accounts.

**Note**  
Image Builder skips images with a build in progress (pending, creating, building, importing, testing, distributing, or integrating state). Image Builder evaluates these images in the next scheduled run.

**AMI exclusion rule evaluation order**  
EC2 Image Builder evaluates AMI-level exclusion rules (`exclusionRules.amis`) on the output AMI after determining eligibility for a lifecycle action. These rules apply to the Amazon EC2 AMI resource, not the Image Builder image resource. Retention counting runs separately. An excluded AMI does not consume a retention slot. Image Builder checks conditions in order and skips the AMI at the first match:

1. **Region exclusion** – Checks whether the AMI is in an excluded Region.

1. **Public AMI exclusion** – Checks whether the AMI is public and `isPublic` exclusion is enabled.

1. **Tag exclusion** – Checks whether the AMI has tags matching the exclusion tag map.

1. **Shared account exclusion** – Checks whether the AMI is shared with accounts listed in the exclusion.

1. **Last launched exclusion** – Checks whether the AMI launched within the excluded time window.

In execution resource details, skipped AMIs display a `SKIPPED` status with a reason that indicates which exclusion condition matched.

## Tags as resource selectors vs. exclusion rules
<a name="image-lifecycle-tags-selector-vs-exclusion"></a>

Tags serve two distinct purposes in lifecycle policies. Each tag mechanism operates on a specific resource level:
+ **Image Builder image** – The Image Builder resource that tracks a build (ARN format: `arn:aws:imagebuilder:{{region}}:{{account}}:image/{{name}}/{{version}}`). Manage tags on this resource through Image Builder.
+ **Output AMI or container image** – The underlying Amazon EC2 AMI or Amazon ECR container image that Image Builder produces. Manage tags on these resources through Amazon EC2 or Amazon ECR respectively.

**Tags as resource selectors** (policy scope)  
Tag-based resource selection evaluates tags on the *Image Builder image resource only*, not on output AMIs or containers. Image Builder uses these tags to *find* resources the policy applies to.  
Configure tag-based resource selection in the `resourceSelection.tagMap` field. Each entry is a key-value pair. The policy selects Image Builder images matching *any* specified tag key-value pair (OR logic). Image Builder does not evaluate images without matching tags.

**Tags as exclusion rules** (rule-level exceptions)  
Exclusion tags work in the opposite direction. After Image Builder selects resources based on the policy scope, it checks each resource against exclusion rules *before* taking any action. Configure exclusion tags at two levels, each operating on a different resource type:    
`exclusionRules.tagMap`  
Evaluates tags on the *Image Builder image resource only*. Does *not* check tags on underlying AMIs or containers. If an Image Builder image tag matches an entry (exact key and value match), Image Builder skips the image and all associated output resources.  
`exclusionRules.amis.tagMap`  
Evaluates tags on the *output AMI* (the Amazon EC2-level resource) during associated resource processing. Use this to exclude specific output AMIs based on their Amazon EC2 tags (for example, tags applied through distribution settings or directly through Amazon EC2).

**Important**  
Resource selection and `exclusionRules.tagMap` do not evaluate tags on output AMIs (Amazon EC2 tags) or containers (Amazon ECR tags). To exclude output AMIs based on Amazon EC2 tags, use `exclusionRules.amis.tagMap`.

**Example Tag selector and exclusion working together**  
A policy with these settings:  
+ Resource selection tag: `Environment: Production` (evaluated on Image Builder image resources)
+ Image-level exclusion tag (`exclusionRules.tagMap`): `Retain: True` (evaluated on Image Builder image resources)
+ AMI-level exclusion tag (`exclusionRules.amis.tagMap`): `SharedWith: Partner` (evaluated on output AMIs)
Image Builder performs these steps:  

1. **Resource selection** – Image Builder finds all Image Builder image resources tagged `Environment: Production`.

1. **Image-level exclusion** – Image Builder checks each selected Image Builder image for the tag `Retain: True`. Image Builder skips images with this tag, including their output resources.

1. **AMI-level exclusion** – Image Builder checks output AMIs (Amazon EC2 resources) of remaining images for the tag `SharedWith: Partner`. AMIs with this tag are skipped.

## How retention is calculated
<a name="image-lifecycle-rules-retention"></a>

When you configure retention settings for delete rules, the AGE and COUNT filters evaluate against your *Image Builder image resources*, not directly against output AMIs or containers.

**Important**  
The AGE filter uses the Image Builder image resource creation date (set once the build completes), not the output AMI or container creation date. The COUNT filter counts Image Builder image resources per recipe version, not output AMIs or containers.

Retention calculation depends on how you specify recipe versions in your policy scope:

Specific version (for example, `1.0.0`)  
Retention count applies to Image Builder images built with that exact recipe version. Image Builder retains the newest images (by creation date) first.

Wildcard version pattern (for example, `1.x.x`)  
Retention count applies independently per matching recipe version. For example, `1.x.x` with a retention count of 5 retains the 5 newest images for `1.0.0`, the 5 newest for `1.1.0`, and so on.

Tag-based resource selection  
With tag-based resource selection (see [Tags as resource selectors vs. exclusion rules](#image-lifecycle-tags-selector-vs-exclusion)), retention is also calculated per recipe version. Image Builder sorts images newest-first within each version and applies retention counts independently per version group.

**Age-based vs. count-based delete filters**  
Delete rules use one of two filter types to determine deletion eligibility:

`AGE` filter  
Retains Image Builder images newer than the specified age threshold (in days, weeks, months, or years from the Image Builder image creation date). You can set `retainAtLeast` to keep a minimum number of the newest images per recipe version, regardless of age.

`COUNT` filter  
Retains the newest N Image Builder images per recipe version. All images beyond the specified count qualify for deletion.

Additional retention behaviors apply:
+ Failed or canceled Image Builder images do not count toward retention limits and always qualify for deletion.
+ Image Builder processes images newest-first and applies retention counts before evaluating deletion eligibility.

## How lifecycle actions affect associated resources
<a name="image-lifecycle-action-scope"></a>

Lifecycle actions on an Image Builder image affect associated output AMIs or containers, depending on rule type and configuration:

Deprecate  
Sets the Image Builder image resource status to `Deprecated`. You can also deprecate associated output AMIs. Deprecated AMIs do not appear in general searches but remain usable by AMI ID. Image Builder adds a `DeprecatedBy: EC2 Image Builder` tag to each deprecated AMI.  
Applies to AMI-based images only, not containers.

Disable  
Sets the Image Builder image resource status to `Disabled`. You can also disable associated output AMIs. Disabled AMIs become private and no longer launch new instances.  
Applies to AMI-based images only, not containers.

Delete  
Deletes the Image Builder image resource. You can also remove:  
+ Output AMIs distributed to other AWS Regions and accounts
+ Snapshots associated with those AMIs
+ Containers distributed to Amazon ECR repositories
Applies to both AMI-based and container-based images.

**Note**  
Image Builder makes lifecycle action decisions at the image level. Associated output resources (AMIs, snapshots, containers) change only if you configured the rule to include them.

## Allowed resource state transitions
<a name="image-lifecycle-state-transitions"></a>

Lifecycle policies and the `StartResourceStateUpdate` API transition image resources between these states:

Available → Deprecated  
Marks an available image as deprecated. The image remains usable by AMI ID but does not appear in general searches. Image Builder adds a `DeprecatedBy: EC2 Image Builder` tag for tracking.

Available or Deprecated → Disabled  
Makes the AMI private and prevents new instance launches. If the AMI was previously deprecated, Image Builder removes the deprecated tag because the image moved to a more restrictive state.

Any non-building state → Deleted  
Deregisters the AMI or deletes the container image from ECR. You can include associated snapshots or underlying containers for deletion.

Deprecated or Disabled → Available  
The `StartResourceStateUpdate` API returns a deprecated or disabled image to available state. This reverses deprecation, re-enables the AMI, and removes the deprecation date and DeprecatedBy tag. This transition works only through the manual API, not automated policy execution.

**Note**  
Images currently being built (in pending, creating, building, importing, testing, distributing, or integrating state) do not change state. A manual state update on an image with an active build fails with an error.

## View rule details for a lifecycle policy
<a name="image-lifecycle-rule-view"></a>

In the console, the lifecycle policy details page has a [Rules tab](view-lifecycle-policy.md#view-lifecycle-policy-console-rules-tab) that shows rule details for the policy.

In the AWS CLI, run the [get-lifecycle-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-lifecycle-policy.html) command. The response includes all configured actions (rules) with their settings.
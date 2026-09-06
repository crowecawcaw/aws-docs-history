

# Create lifecycle policies
<a name="create-lifecycle-policies"></a>

When you create a new EC2 Image Builder lifecycle policy, the configuration depends on what kind of image the policy is for. The API action to create a lifecycle policy for AMI image resources and container image resources is the same ([CreateLifecyclePolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateLifecyclePolicy.html)). However, the configuration for the image resources and associated resources is different. This section shows you how to create lifecycle management policies for both.

**Note**  
Before you create a lifecycle policy, make sure that you've met all [Prerequisites](image-lifecycle-prerequisites.md).

## Create lifecycle management policies for Image Builder AMI image resources
<a name="create-lifecycle-policy-ami"></a>

You can use one of the following methods to create an AMI image lifecycle policy with the AWS Management Console or AWS CLI. You can also use the [CreateLifecyclePolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateLifecyclePolicy.html) API action. For the associated SDK request, you can refer to the [See Also](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateLifecyclePolicy.html#API_CreateLifecyclePolicy_SeeAlso) link for that command in the *EC2 Image Builder API Reference*.

------
#### [ AWS Management Console ]

To create a lifecycle policy for AMI image resources in the AWS Management Console, follow these steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Lifecycle policies** from the navigation pane.

1. Choose **Create lifecycle policy**.

1. Configure policy settings described in the following procedures.

1. To create the lifecycle policy after you've configured settings, choose **Create policy**.

Configure **General** settings for your policy.

1. Select the **AMI** option from **Policy type**.

1. Enter the **Policy name**.

1. Optionally enter a **Description** for your lifecycle policy.

1. By default, **Activate** is turned on. The default setting activates the lifecycle policy and adds it to the schedule right away. To create a policy that's initially deactivated, you can turn **Activate** off.

1. For the **IAM role**, select one of the following options:
   + **Create lifecycle execution role using service defaults** – Generates a pre-configured role with the `EC2ImageBuilderLifecycleExecutionPolicy` managed policy attached. This is the recommended option if you don't have specific custom permission requirements.
   + **Choose an existing role** – Select an existing IAM role from the dropdown list. The list filters out Service-Linked Roles (SLRs) that are not compatible with lifecycle policy execution.
   + **Create a new lifecycle execution role** – Opens the IAM console with pre-filled trust policy and lifecycle execution policy settings for one-click role creation. For step-by-step instructions, see [Create an IAM role for Image Builder lifecycle management](image-lifecycle-prerequisites.md#image-lifecycle-prereq-role).
**Note**  
Service-Linked Roles are not compatible with lifecycle policy execution and are automatically filtered from the role selection. If you previously created a lifecycle policy with a Service-Linked Role, you can update the policy to use a compatible execution role.

Configure the **Rule scope** for your policy.

This section configures the resource selection for your lifecycle policy, based on the type of filter that you use.

1. **Filter type: Recipes** – To apply lifecycle rules to image resources based on the recipe that created them, select up to 50 recipe versions for the policy. You can use the split panel browser to search for recipes and select specific versions.

   You can also use wildcard patterns for the semantic version to target multiple versions of a recipe with a single policy. The following wildcard patterns are supported:
   + `x.x.x` – Matches all versions of the recipe.
   + `1.x.x` – Matches all minor and patch versions within major version 1.
   + `1.0.x` – Matches all patch versions within version 1.0.

   Wildcard patterns are resolved to all matching recipe versions at execution time. This means that new recipe versions created after you set up the policy are automatically included in the next scheduled execution.
**Note**  
Recipe versions created or deleted after a policy execution begins are not included until the next scheduled execution.

1. **Filter type: Tags** – To apply lifecycle rules to image resources based on resource tags, enter a list of up to 50 key value pairs for the policy to match on. Image Builder discovers resources through tag scanning and applies lifecycle rules to matching resources.
**Note**  
Resources tagged or untagged after a policy execution begins are not included until the next scheduled execution.

Configure **Exclusion rules** for your policy (optional).

Exclusion rules define exceptions to the lifecycle rules. Resources that meet the criteria specified by the exclusion rules are excluded from lifecycle actions.

1. For AMI image policies, you can configure the following AMI exclusion rules:
   + **Exclude public AMIs** – Select this option to exclude public AMIs from lifecycle actions.
   + **Exclude AMIs by Region** – Specify AWS Regions to exclude from lifecycle actions.
   + **Exclude AMIs shared with accounts** – Specify AWS accounts whose shared AMIs should be excluded from lifecycle actions.
   + **Exclude recently launched AMIs** – Specify a time period to exclude AMIs that were recently used to launch instances.
   + **Exclude AMIs by tags** – Specify tags for AMIs that should be excluded from lifecycle actions.

1. For tag-based Image Builder image policies, you can specify tags for Image Builder image resources that should be excluded from lifecycle actions.

Turn on one or more of the following **Lifecycle rules** to apply to the resources that the lifecycle policy selects. If a resource matches on more than one lifecycle rule when the policy runs, Image Builder performs rule actions in the following order: 1) Deprecate, 2) Disable, 3) Delete.

**Deprecate rule**  
Sets the Image Builder image resource status to `Deprecated`. Image Builder pipelines still run for deprecated images. You can optionally set the deprecation time for associated AMIs without affecting your ability to launch new instances.
+ **Unit count** – Specify the integer value for the period of time that must pass after an image resource is created before it's marked as `Deprecated`.
+ **Unit** – Select the time range to use. The range can be `Days`, `Weeks`, `Months`, or `Years`.
+ **Deprecate AMIs** – Select the checkbox to mark associated Amazon EC2 AMIs with a deprecation date. The AMIs remain available, and you can still launch new instances from them.

**Disable rule**  
Sets the Image Builder image resource status to `Disabled`. This prevents Image Builder pipelines from running for this image. You can optionally disable the associated AMI to prevent new instance launches.
+ **Unit count** – Specify the integer value for the period of time that must pass after an image resource is created before it's marked as `Disabled`.
+ **Unit** – Select the time range to use. The range can be `Days`, `Weeks`, `Months`, or `Years`.
+ **Disable AMIs** – Select the checkbox to disable associated Amazon EC2 AMIs. You can no longer use the AMIs or launch new instances from them.

**Delete rule**  
Deletes the image resources by age or by count. You define the threshold that meets your needs. When an Image Builder image resource passes the threshold, it's removed. You can optionally deregister associated AMIs or delete the snapshots for those AMIs. You can also specify tags for resources that you want to retain past the threshold.

When you configure the **Delete rule** by age, Image Builder deletes the image resource after a period of time that you configure. For example, delete image resources after 6 months. When you configure by count, Image Builder retains the most recent number of images that you specify, or as close to that number as possible, and deletes earlier versions.
+ 

**By age**
  + **Unit count** – Specify the integer value for the period of time that must pass after an image resource is created before it's deleted.
  + **Unit** – Select the time range to use. The range can be `Days`, `Weeks`, `Months`, or `Years`.
  + **Retain at least one image per recipe** – Select the check box to keep the latest available image resource for each recipe version that this rule affects.

**By count**
  + **Image count** – Specify the integer value for the number of recent image resources to keep for each recipe version.
+ **Deregister AMIs** – Select the check box to deregister associated Amazon EC2 AMIs. You can no longer use the AMIs or launch new instances from them.
+ **Retain images, AMIs, and snapshots with associated tags** – Select the checkbox to enter a list of tags for image resources that you want to keep. Tags apply to image resources and Amazon EC2 AMIs. You can enter up to 50 key value pairs.

**Tags (optional)**  
Add tags to your lifecycle policy.

------
#### [ AWS CLI ]

To create a new Image Builder lifecle policy, you can use the **[create-lifecycle-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-lifecycle-policy.html)** command in the AWS CLI.

------

## Create lifecycle management policies for Image Builder container image resources
<a name="create-lifecycle-policy-container"></a>

You can use one of the following methods to create a container image lifecycle policy with the AWS Management Console or AWS CLI. You can also use the [CreateLifecyclePolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateLifecyclePolicy.html) API action. For the associated SDK request, you can refer to the [See Also](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateImage.html#API_CreateLifecyclePolicy_SeeAlso) link for that command in the *EC2 Image Builder API Reference*.

------
#### [ AWS Management Console ]

To create a lifecycle policy for container image resources in the AWS Management Console, follow these steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Lifecycle policies** from the navigation pane.

1. Choose **Create lifecycle policy**.

1. Configure policy settings described in the following procedures.

1. To create the lifecycle policy after you've configured settings, choose **Create policy**.

**Policy configuration: General settings**

Configure **General** settings for your policy.

1. Select the **Container image** option from **Policy type**.

1. Enter the **Policy name**.

1. Optionally enter a **Description** for your lifecycle policy.

1. By default, **Activate** is turned on. The default setting activates the lifecycle policy and adds it to the schedule right away. To create a policy that's initially deactivated, you can turn **Activate** off.

1. For the **IAM role**, select one of the following options:
   + **Create lifecycle execution role using service defaults** – Generates a pre-configured role with the `EC2ImageBuilderLifecycleExecutionPolicy` managed policy attached. This is the recommended option if you don't have specific custom permission requirements.
   + **Choose an existing role** – Select an existing IAM role from the dropdown list. The list filters out Service-Linked Roles (SLRs) that are not compatible with lifecycle policy execution.
   + **Create a new lifecycle execution role** – Opens the IAM console with pre-filled trust policy and lifecycle execution policy settings for one-click role creation. For step-by-step instructions, see [Create an IAM role for Image Builder lifecycle management](image-lifecycle-prerequisites.md#image-lifecycle-prereq-role).
**Note**  
Service-Linked Roles are not compatible with lifecycle policy execution and are automatically filtered from the role selection. If you previously created a lifecycle policy with a Service-Linked Role, you can update the policy to use a compatible execution role.

Configure the **Rule scope** for your policy.

This section configures the resource selection for your lifecycle policy, based on the type of filter that you use.

1. **Filter type: Recipes** – To apply lifecycle rules to image resources based on the recipe that created them, select up to 50 recipe versions for the policy. You can use the split panel browser to search for recipes and select specific versions.

   You can also use wildcard patterns for the semantic version to target multiple versions of a recipe with a single policy. The following wildcard patterns are supported:
   + `x.x.x` – Matches all versions of the recipe.
   + `1.x.x` – Matches all minor and patch versions within major version 1.
   + `1.0.x` – Matches all patch versions within version 1.0.

   Wildcard patterns are resolved to all matching recipe versions at execution time. This means that new recipe versions created after you set up the policy are automatically included in the next scheduled execution.
**Note**  
Recipe versions created or deleted after a policy execution begins are not included until the next scheduled execution.

1. **Filter type: Tags** – To apply lifecycle rules to image resources based on resource tags, enter a list of up to 50 key value pairs for the policy to match on. Image Builder discovers resources through tag scanning and applies lifecycle rules to matching resources.
**Note**  
Resources tagged or untagged after a policy execution begins are not included until the next scheduled execution.

Configure **Exclusion rules** for your policy (optional).

Exclusion rules define exceptions to the lifecycle rules. Resources that meet the criteria specified by the exclusion rules are excluded from lifecycle actions.

1. For AMI image policies, you can configure the following AMI exclusion rules:
   + **Exclude public AMIs** – Select this option to exclude public AMIs from lifecycle actions.
   + **Exclude AMIs by Region** – Specify AWS Regions to exclude from lifecycle actions.
   + **Exclude AMIs shared with accounts** – Specify AWS accounts whose shared AMIs should be excluded from lifecycle actions.
   + **Exclude recently launched AMIs** – Specify a time period to exclude AMIs that were recently used to launch instances.
   + **Exclude AMIs by tags** – Specify tags for AMIs that should be excluded from lifecycle actions.

1. For tag-based Image Builder image policies, you can specify tags for Image Builder image resources that should be excluded from lifecycle actions.

**Delete rule**  
For container images, this rule deletes the Image Builder container image resource. You can optionally remove Docker images that were distributed to ECR repositories to prevent them from being used to run new containers.

When you configure the **Delete rule** by age, Image Builder deletes the image resource after a period of time that you configure. For example, delete image resources after 6 months. When you configure by count, Image Builder retains the most recent number of images that you specify, or as close to that number as possible, and deletes earlier versions.
+ 

**By age**
  + **Unit count** – Specify the integer value for the period of time that must pass after an image resource is created before it's deleted.
  + **Unit** – Select the time range to use. The range can be `Days`, `Weeks`, `Months`, or `Years`.
  + **Retain at least one image** – Select the checkbox to keep only the latest available image resource for each recipe version that this rule affects.

**By count**
  + **Image count** – Specify the integer value for the number of recent image resources to keep for each recipe version.
+ **Delete ECR container images** – Select the check box to delete associated container images stored in an ECR repository. You can no longer use the container image as a base to create new images, or to run new containers.
+ **Retain images with associated tags** – Select the checkbox to enter a list of tags for image resources that you want to keep.

**Tags (optional)**  
Add tags to your lifecycle policy.

------
#### [ AWS CLI ]

To create a new Image Builder lifecle policy, you can use the **[create-lifecycle-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-lifecycle-policy.html)** command in the AWS CLI.

------
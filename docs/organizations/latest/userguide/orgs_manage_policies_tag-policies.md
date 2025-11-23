# Tag policies

Tag policies allow you to standardize the tags attached to the AWS resources in your organization's accounts.

You can use tag policies to maintain consistent tags, including the preferred case treatment of tag keys and tag values.

## What are tags?

_Tags_ are custom attribute labels that you assign or that AWS
assigns to AWS resources. Each tag has two parts:

- A _tag key_ (for example, `CostCenter`,
  `Environment`, or `Project`). Tag keys are case
  sensitive.
- An optional field known as a _tag value_ (for example,
  `111122223333` or `Production`). Omitting
  the tag value is the same as using an empty string. Like tag keys, tag values
  are case sensitive.

The rest of this page describes tag policies. For more information about tags, see the
following sources:

- For general information about tagging, including naming and usage
  conventions, see the [_Tagging AWS Resources
  User Guide_](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").
- For a list of services that support using tags, see the [_Resource Groups Tagging API
  Reference_](../../../resourcegroupstagging/latest/APIReference/Welcome.md "../../../resourcegroupstagging/latest/APIReference/Welcome.md").
- For information about using tags to categorize resources, see the [_Best Practices for Tagging AWS Resources Whitepaper_](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md").
- For information on tagging Organizations resources, see [Tagging AWS Organizations resources](orgs_tagging.md "orgs_tagging.md").
- For information on tagging resources in other AWS services, see the
  documentation for that service.

## What are tag policies?

_Tag policies_ are a type of policy that can help you standardize
tags across resources in your organization's accounts. In a tag policy, you specify
tagging rules applicable to resources when they are tagged.

For example, a tag policy can specify that when the `CostCenter` tag is
attached to a resource, it must use the case treatment and tag values that the tag
policy defines. A tag policy can also specify that noncompliant tagging operations on
specified resource types are _enforced_. In other words, noncompliant
tagging requests on specified resource types are prevented from completing. Untagged
resources or tags that aren't defined in the tag policy aren't evaluated for compliance
with the tag policy.

Using tag policies involves working with multiple AWS services:

- Use **AWS Organizations** to manage _tag
  policies_. When you sign in to the organization's management
  account, you use Organizations to enable the tag policies feature. You must sign in as an
  IAM user, assume an IAM role, or sign in as the root user ([not
  recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization's management account. Then you can
  create tag policies and attach them to the organization entities to put those
  tagging rules in effect.
- Use **AWS Resource Groups** to manage
  _compliance_ with tag policies. When you sign in to an
  account in your organization, you use Resource Groups to find noncompliant tags on
  resources in the account. You can correct noncompliant tags in the AWS service
  where you created the resource. You can also use the [Tag
  Editor](../../../tag-editor/latest/userguide/tag-editor.md "../../../tag-editor/latest/userguide/tag-editor.md") and the [Resource Groups Tagging](../../../resourcegroupstagging/latest/APIReference/overview.md "../../../resourcegroupstagging/latest/APIReference/overview.md") API to tag and
  untag resources from multiples services.

If you sign in to the management account in your organization, you can view
compliance information for all your organization's accounts.

Tag policies are available only in an organization that has [all features enabled](orgs_manage_org_support-all-features.md "orgs_manage_org_support-all-features.md"). For more
information on what's required to use tag policies, see [Prerequisites and permissions for
management policies for AWS Organizations](orgs_manage_policies_prereqs.md "orgs_manage_policies_prereqs.md").

###### Important

To get started with tag policies, AWS strongly recommends that you follow the
example workflow described in [Getting started with tag
policies](orgs_manage_policies_tag-policies-getting-started.md "orgs_manage_policies_tag-policies-getting-started.md") before
moving on to more advanced tag policies. It's best to understand the effects of
attaching a simple tag policy to a single account before expanding tag policies to
an entire OU or organization. It's especially important to understand a tag policy's
effects before you _enforce_ compliance with any tag policy. The
tables on the [Getting started with tag
policies](orgs_manage_policies_tag-policies-getting-started.md "orgs_manage_policies_tag-policies-getting-started.md") page also
provide links to instructions for more advanced policy-related tasks.



# Best practices for using tag policies
<a name="orgs_manage_policies_tag-policies-best-practices"></a>

AWS recommends the following best practices for using tag policies.

## Decide on a tag capitalization strategy
<a name="bp-tag-cap"></a>

Determine how you want to capitalize tags and consistently implement that strategy across all resource types. For example, decide whether to use `Costcenter`, `costcenter`, or `CostCenter`, and use the same convention for all tags. For consistent results in compliance reports, avoid using similar tags with inconsistent case treatment. This strategy will help you define tag policies for your organization. 

## Use the recommended workflow
<a name="bp-tag-workflow"></a>

Start small by creating a simple tag policy. Then attach it to a member account that you can use for testing purposes. Use the workflows described in [Getting started with tag policies](orgs_manage_policies_tag-policies-getting-started.md).

## Determine tagging rules
<a name="bp-tag-rules"></a>

This will depend on your organization's needs. For example, you may want to specify that when a `CostCenter` tag is attached to AWS Secrets Manager secrets, it must use the specified case treatment. Create tag policies that define compliant tags and attach them to the organization entities where you want those tagging rules to be in effect.

## Educate account administrators
<a name="bp-tag-educate"></a>

When you're ready to expand your use of tag policies, educate account administrators as follows:
+ Communicate your tagging strategy.
+ Emphasize that administrators need to use tags on specific resource types.

  This is important, as untagged resources don't show as noncompliant in compliance results.
+ Provide guidance on checking compliance with tag policies. Instruct administrators to find and correct noncompliant tags on resources in their account using the procedure described in [Evaluating Compliance for an Account](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs-finding-noncompliant-tags.html) in the *Tagging AWS Resource User Guide.* Let them know how often you want them to check for compliance.

## Use caution in enforcing compliance
<a name="bp-tag-compliance"></a>

 Enforcing compliance could prevent users in your organization's accounts from tagging the resources they need. Review the information in [Enforce tagging consistency](orgs_manage_policies_tag-policies-enforcement.md). Also see the workflows described in [Getting started with tag policies](orgs_manage_policies_tag-policies-getting-started.md).

## Be aware of tagging limits
<a name="bp-tag-limits"></a>

 AWS services generally have a limit of 50 user-defined tags that cannot be modified. When using features like Report Required Tags, ensure your organization's effective policies don't exceed 50 required tags for any given resource type. Exceeding this limit can cause two issues: resources may be unable to achieve compliance status in compliance summaries, and Infrastructure as Code (IaC) platforms may fail to create resources when more than 50 tags are defined as required. 

## Consider creating an SCP to set guardrails around resource creation requests
<a name="bp-tag-guardrails"></a>

Resources that have never had tags attached to them don't show as noncompliant in reports. Account administrators can still create untagged resources. In some cases, you can use a service control policy (SCP) to set guardrails around resource creation requests.

To learn whether an AWS service supports controlling access using tags, see [AWS services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*. Look for the services that have **Yes **in the **ABAC (authorization based on tags)** column. Choose the name of the service to view the authorization and access control documentation for that service.
# Best practices for using

tag policies

AWS recommends the following best practices for using tag policies.

## Decide on a tag capitalization strategy

Determine how you want to capitalize tags and consistently implement that strategy
across all resource types. For example, decide whether to use `Costcenter`,
`costcenter`, or `CostCenter`, and use the same convention for
all tags. For consistent results in compliance reports, avoid using similar tags with
inconsistent case treatment. This strategy will help you define tag policies for your
organization.

## Use the recommended workflow

Start small by creating a simple tag policy. Then attach it to a member account that
you can use for testing purposes. Use the workflows described in [Getting started with tag
policies](orgs_manage_policies_tag-policies-getting-started.md "orgs_manage_policies_tag-policies-getting-started.md").

## Determine tagging rules

This will depend on your organization's needs. For example, you may want to specify
that when a `CostCenter` tag is attached to AWS Secrets Manager secrets, it must use
the specified case treatment. Create tag policies that define compliant tags and attach
them to the organization entities where you want those tagging rules to be in
effect.

## Educate account administrators

When you're ready to expand your use of tag policies, educate account administrators
as follows:

- Communicate your tagging strategy.
- Emphasize that administrators need to use tags on specific resource
  types.

This is important, as untagged resources don't show as noncompliant in
compliance results.

- Provide guidance on checking compliance with tag policies. Instruct
  administrators to find and correct noncompliant tags on resources in their
  account using the procedure described in [Evaluating Compliance for an Account](../../../tag-editor/latest/userguide/tag-policies-orgs-finding-noncompliant-tags.md "../../../tag-editor/latest/userguide/tag-policies-orgs-finding-noncompliant-tags.md")
  in the _Tagging AWS Resource User Guide._ Let them know how often you want them to check for
  compliance.

## Use caution in enforcing compliance

Enforcing compliance could prevent users in your organization's accounts from tagging
the resources they need. Review the information in [Enforce tagging consistency](orgs_manage_policies_tag-policies-enforcement.md "orgs_manage_policies_tag-policies-enforcement.md"). Also see the
workflows described in [Getting started with tag
policies](orgs_manage_policies_tag-policies-getting-started.md "orgs_manage_policies_tag-policies-getting-started.md").

## Consider creating an SCP to set guardrails around

resource creation requests

Resources that have never had tags attached to them don't show as noncompliant in
reports. Account administrators can still create untagged resources. In some cases, you
can use a service control policy (SCP) to set guardrails around resource creation
requests. For an example SCP, see [Require a tag on specified
created resources](orgs_manage_policies_scps_examples_tagging.md#example-require-tag-on-create "orgs_manage_policies_scps_examples_tagging.md#example-require-tag-on-create").

To learn whether an AWS service
supports controlling access using tags, see [AWS services
That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_. Look for
the services that have **Yes** in the **ABAC (authorization based on tags)** column. Choose the name of the service to
view the authorization and access control documentation for that service.

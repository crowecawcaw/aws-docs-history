# Checks for validating

policies

IAM Access Analyzer provides policy checks that help validate your IAM policies before you
attach them to an entity. These include basic policy checks provided by policy validation to
validate your policy against [policy
grammar](reference_policies_grammar.md "reference_policies_grammar.md") and [AWS best practices](best-practices.md "best-practices.md"). You can
view policy validation check findings that include security warnings, errors, general
warnings, and suggestions for your policy.

You can use custom policy checks to check for new access based on your security standards.
A charge is associated with each check for new access. For more details about pricing, see
[IAM Access Analyzer
pricing](https://aws.amazon.com/iam/access-analyzer/pricing "https://aws.amazon.com/iam/access-analyzer/pricing").

## How custom policy checks

work

You can validate your policies against your specified security standards using
AWS Identity and Access Management Access Analyzer custom policy checks. You can run the following types of custom
policy checks:

- **Check against a reference policy**: When
  editing a policy, you can check whether the updated policy grants new access
  compared to a reference policy, such as an existing version of the policy. You
  can run this check when you edit a policy using the AWS Command Line Interface (AWS CLI),
  IAM Access Analyzer API (API), or JSON policy editor in the IAM console.

###### Note

IAM Access Analyzer custom policy checks allow wildcards in the
`Principal` element for reference resource policies.

- **Check against a list of IAM actions or
  resources**: You can check to ensure that specific IAM actions or
  resources are not allowed by your policy. If only actions are specified,
  IAM Access Analyzer checks for access of the actions on all resources in the policy.
  If only resources are specified, then IAM Access Analyzer checks which actions have
  access to the specified resources. If both actions and resources are specified,
  then IAM Access Analyzer checks which of the specified actions have access to the
  specified resources. You can run this check when you create or edit a policy
  using the AWS CLI or the API.
- **Check for public access**: You can check
  whether a resource policy can grant public access to a specified resource type.
  You can run this check when you create or edit a policy using the AWS CLI or the
  API. This type of custom policy check differs from [previewing
  access](access-analyzer-access-preview.md "access-analyzer-access-preview.md") because the check doesn't require any account or external
  access analyzer context. Access previews allow you to preview IAM Access Analyzer
  findings before deploying resource permissions, while the custom check
  determines whether public access might be granted by a policy.

A charge is associated with each custom policy check. For more details about pricing,
see [IAM Access Analyzer
pricing](https://aws.amazon.com/iam/access-analyzer/pricing "https://aws.amazon.com/iam/access-analyzer/pricing").

You can run custom policy checks on identity and resource-based policies. Custom
policy checks don't rely on pattern-matching techniques or examining access logs to
determine whether new or a specified access is allowed by a policy. Similar to external
access findings, custom policy checks are built on [Zelkova](https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/ "https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/"). Zelkova translates IAM policies into equivalent logical
statements, and runs a suite of general-purpose and specialized logical solvers
(satisfiability modulo theories) against the problem. To check for new or specified
access, IAM Access Analyzer applies Zelkova repeatedly to a policy. Queries become
increasingly specific to characterize classes of behaviors that the policy allows based
on the content of the policy. For more information about satisfiability modulo theories,
see [Satisfiability Modulo Theories](https://people.eecs.berkeley.edu/~sseshia/pubdir/SMT-BookChapter.pdf "https://people.eecs.berkeley.edu/~sseshia/pubdir/SMT-BookChapter.pdf").

In rare cases, IAM Access Analyzer isn't able to fully determine whether a policy statement
grants new or specified access. In those cases, it errs on the side of declaring a false
positive by failing the custom policy check. IAM Access Analyzer is designed to provide a
comprehensive policy evaluation and strives to minimize false negatives. This approach
means that IAM Access Analyzer provides a high degree of assurance that a passed check means
access wasn't granted by the policy. You can inspect failed checks manually by reviewing
the policy statement that's reported in the response from IAM Access Analyzer.

## Examples of reference

policies to check for new access

You can find examples for reference policies and learn how to set up and run a custom
policy check for new access in the [IAM Access Analyzer custom policy checks samples](https://github.com/aws-samples/iam-access-analyzer-custom-policy-check-samples "https://github.com/aws-samples/iam-access-analyzer-custom-policy-check-samples") repository on GitHub.

###### Before using these examples

Before you use these sample reference policies, do the following:

- Carefully review and customize the reference policies for your unique
  requirements.
- Thoroughly test the reference policies in your environment with the
  AWS services that you use.

The reference policies demonstrate the implementation and use of custom
policy checks. They're **_not_** intended to be interpreted as official
AWS recommendations or best practices to be implemented exactly as shown.
It is your responsibility to carefully test reference policies for their
suitability to solve the security requirements for your environment.

- Custom policy checks are environment-agnostic in their analysis. Their
  analysis only considers information contained within the input policies. For
  example, custom policy checks can't check whether an account is a member of
  a specific AWS organization. Therefore, the custom policy checks can't
  compare new access based on condition key values for the [`aws:PrincipalOrgId`](reference_policies_condition-keys.md#condition-keys-principalorgid "reference_policies_condition-keys.md#condition-keys-principalorgid") and [`aws:PrincipalAccount`](reference_policies_condition-keys.md#condition-keys-principalaccount "reference_policies_condition-keys.md#condition-keys-principalaccount") condition keys.

## Inspect failed

custom policy checks

When a custom policy check fails, the response from IAM Access Analyzer includes the [statement ID (`Sid`)](reference_policies_elements_sid.md "reference_policies_elements_sid.md") of the policy statement that caused the
check to fail. Although the statement ID is an optional policy element, we recommend
that you add a statement ID for every policy statement. The custom policy check also
returns a statement index to help identify the reason for the check failure. The
statement index follows zero-based numbering, where the first statement is referenced as 0. When there are multiple statements that cause a check to fail, the check returns only
one statement ID at a time. We recommend that you fix the statement highlighted in the
reason and rerun the check until it passes.

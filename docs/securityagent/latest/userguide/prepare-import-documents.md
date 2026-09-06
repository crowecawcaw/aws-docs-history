

# Prepare documents for requirement generation
<a name="prepare-import-documents"></a>

When you generate security requirements from documents, AWS Security Agent reads your documents and produces structured requirements from the security-relevant content it finds. You do not need to format your documents in any particular way or pre-write the applicability, compliance criteria, and remediation guidance. AWS Security Agent derives those from the content you provide. Upload the security documentation you already have, written in your own words.

This page describes what to include so that AWS Security Agent generates accurate, useful requirements. For the upload procedure and file limits, see [Generate security requirements from documents](import-security-requirements.md).

## What to include
<a name="_what_to_include"></a>

 AWS Security Agent looks for content that describes your security expectations. Documents that cover the following topics produce the strongest requirements:
+ Access control and authorization
+ Authentication
+ Data protection and encryption
+ Network security
+ Logging and audit
+ Incident response
+ Vulnerability and patch management
+ Compliance obligations that apply to your workloads

Good source documents include security policies, engineering standards, control catalogs, architecture guidelines, and secure coding standards.

## Write at the workload level
<a name="_write_at_the_workload_level"></a>

 AWS Security Agent generates requirements that apply to an individual workload or application, the same scope it evaluates during design and code reviews. Content that describes how to build and operate a secure workload generates requirements. Organization-wide governance topics, such as multi-account strategy, root user management, and account-level logging setup, are outside this scope and do not generate workload requirements.

## Describe the outcome, not a single implementation
<a name="_describe_the_outcome_not_a_single_implementation"></a>

State the security outcome you expect rather than a single prescribed product or configuration. AWS Security Agent generates requirements that focus on the security capability needed and allow more than one valid implementation. For example, "data at rest is encrypted" generates a clearer, more broadly applicable requirement than a statement that names one specific service or setting.

## Be specific about what good looks like
<a name="_be_specific_about_what_good_looks_like"></a>

The more concretely your documents describe expected behavior, the better AWS Security Agent can define compliance criteria. Where you can, describe what a compliant design demonstrates and what indicates a violation. Vague or purely aspirational statements generate fewer and weaker requirements than concrete, workload-relevant ones.

## Review what you get back
<a name="_review_what_you_get_back"></a>

Each generated requirement includes a name, applicability, compliance criteria, and remediation guidance that AWS Security Agent derived from your documents. Review the generated requirements, edit any that need refinement, and enable the ones you want AWS Security Agent to evaluate. For more information, see [Manage security requirements](security-requirements.md).
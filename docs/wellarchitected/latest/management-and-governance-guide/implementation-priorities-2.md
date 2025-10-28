# Implementation priorities

Having secure and scalable mechanisms to manage identities is a
critical component of a cloud ready environment. As such, the
following items should be prioritized.

## Establish a centralized identity provider for human identities

Implementation of a centralized identity provider is a foundational capability for
enterprises of all sizes and interwoven across all environments, systems, workloads, and
processes. For workforce identities, restrict the use of individual users and instead rely
on an identity provider that enables you to manage identities in a centralized place. This
makes it easier to manage access across multiple applications and services, because you are
creating, managing, and revoking access from a single location. Use existing HR processes to
manage creation, update, and removal of access to include your AWS environments. Federate
access into your AWS environments by integrating the identity provider with a SAML 2.0
compliant SSO solution. Incorporate multi-factor authentication (MFA) in AWS for the root
user, and use your identity provider MFA solution for other privileged roles.

## Define job functions and codify IAM roles

Define the IAM roles to be granted to human and machine identities and strive to follow
the principles of least privilege and separation of responsibilities. Verify that runbooks
and playbooks reference identity constructs with sufficient permissions to run support
activities (for example, emergency access). This might include “break glass” access in the
event that your SSO solution becomes inaccessible. Optimizing your IAM permissions is a
journey. Refine permissions over time and employ controls as an additional layer of
protection while still enabling developer agility.

Consider that permissions will be variable by environment type.
For instance, permissions defined for production accounts should
be more restrictive than those defined in development or sandbox
accounts. Use resource tags and IAM conditional statements to
create more fine-grained access policies and apply permissions
boundaries to allow safe delegation of administrative functions
while protecting against privilege escalation. Attribute-based
access control (ABAC) is an authorization strategy that defines
permissions based on attributes. For AWS services that support
tagging, ABAC policies can be designed to allow operations when
the principal's tag matches the resource tag. ABAC is helpful in
environments that are growing rapidly because it helps scale
policy management with reusable attributes from your identity
provider.

## Continually collect, review, and refine permissions

Changes to identity roles and permissions are recorded in
CloudTrail and detective guardrails should alert on deviations
from your expected configuration state. With the centralized
collection of events, you can use aggregated and pattern
identification tools to review and refine permissions as required.

AWS Identity and Access Management (IAM)
[access
advisor](../../../IAM/latest/UserGuide/access_policies_access-advisor.md "../../../IAM/latest/UserGuide/access_policies_access-advisor.md") uses data analysis to help you set permission
guardrails confidently by providing service last accessed
information for your accounts, organizational units (OUs), and
your organization managed by AWS Organizations. Use this feature
to analyze service last accessed information and determine
services not used and reduce permissions where appropriate.

Use [IAM Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md") to guide you to least privilege by helping
you set, verify, and refine permissions. This includes identifying
S3 buckets or IAM roles that are shared with an external entity
outside of your organization or account. Establish a regular
attestation process to help ensure permissions are still
appropriate as personnel change roles within your organization.
Review the IAM credential report for stale or unused account users
and credentials.

## Manage credential use

The M&G Guide recommends the use of IAM roles and temporary
credentials. Use AWS Systems Manager to manage remote access to
instances or on-premises systems using a pre-installed agent
without the need for stored secrets. Reduce reliance on long-term
credentials, and scan for hardcoded credentials in your
infrastructure as code templates. In situations where you cannot
use temporary credentials, use programmatic tools such as AWS Secrets Manager to automate credential rotation and management,
such as application tokens and database passwords.

## Source and distribute identity constructs with automation

Codify and version identity constructs such as roles, policies,
and templates with infrastructure as code. Employ testing and
linting to ensure coding standards are met within your continuous
integration and continuous delivery (CI/CD) pipelines with tools
like
[cfn-guard](https://aws.amazon.com/blogs/mt/introducing-aws-cloudformation-guard-2-0/ "https://aws.amazon.com/blogs/mt/introducing-aws-cloudformation-guard-2-0/").
Use
[IAM
Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md") policy validation to check for findings
that include security warnings, errors, general warnings, and
suggested changes to your IAM policies. Where appropriate, deploy
and remove identity constructs for temporary access to the
environment in an automated manner and prohibit deployment by
individuals using the console.

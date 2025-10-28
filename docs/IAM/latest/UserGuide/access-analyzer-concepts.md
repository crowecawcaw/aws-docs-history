# Understand how IAM Access Analyzer findings work

This topic describes the concepts and terms that are used in IAM Access Analyzer to help you
become familiar with how IAM Access Analyzer monitors access to your AWS resources.

## External access findings

External access findings are generated only once for each instance of a resource that is
shared outside of your zone of trust. Each time a resource-based policy is modified,
IAM Access Analyzer analyzes the policy. If the updated policy shares a resource that is already
identified in a finding, but with different permissions or conditions, a new finding is
generated for that instance of the resource sharing. Changes to a resource control policy that
impact the **Resource control policy (RCP) restriction** also generate a new
finding. IAM Access Analyzer also evaluates access control configurations established by [declarative
policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md"). If the access in the first finding is removed, that finding is updated to
a status of **Resolved**.

The status of all findings remains **Active** until you archive them or
remove the access that generated the finding. When you remove the access, the finding status
is updated to **Resolved**.

###### Note

It may take up to 30 minutes after a policy is modified for IAM Access Analyzer to analyze the
resource and then update the external access finding. Changes to a resource control policy
(RCP) do not trigger a rescan of the resource reported in the finding. IAM Access Analyzer
analyzes the new or updated policy during the next periodic scan, which is within 24
hours.

## How IAM Access Analyzer generates findings for

external access

AWS Identity and Access Management Access Analyzer uses a technology called [Zelkova](https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/ "https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/") to analyze IAM policies and identify external access to resources.

Zelkova translates IAM policies into equivalent logical statements and runs them through
a suite of general-purpose and specialized logical solvers (satisfiability modulo theories).
IAM Access Analyzer applies Zelkova repeatedly to a policy, using increasingly specific queries to
characterize the types of access the policy allows based on its content. For more information
about satisfiability modulo theories, see [Satisfiability
Modulo Theories](https://people.eecs.berkeley.edu/~sseshia/pubdir/SMT-BookChapter.pdf "https://people.eecs.berkeley.edu/~sseshia/pubdir/SMT-BookChapter.pdf").

For external access analyzers, IAM Access Analyzer does not examine access logs to determine
whether an external entity has actually accessed a resource within your zone of trust.
Instead, it generates a finding when a resource-based policy allows access to a resource,
regardless of whether the resource was accessed by the external entity.

Additionally, IAM Access Analyzer does not consider the state of any external accounts when
making its determinations. If it indicates that account 111122223333 can access your
Amazon S3 bucket, it doesn't have any information about the users, roles, service control policies
(SCP), or other relevant configurations in that account. This is for customer privacy, as
IAM Access Analyzer doesn't know who owns the other account. This is also for security, as it's
important to know about potential external access even if there are currently no active
principals that can use it.

IAM Access Analyzer only considers certain IAM condition keys that external users can't
directly influence or that are otherwise impactful to authorization. For examples of condition
keys IAM Access Analyzer considers, see [IAM Access Analyzer filter keys](access-analyzer-reference-filter-keys.md "access-analyzer-reference-filter-keys.md").

IAM Access Analyzer doesn't currently report findings from AWS service principals or internal
service accounts. In rare cases where it can't fully determine whether a policy statement
grants access to an external entity, it errs on the side of declaring a false positive
finding. This is because IAM Access Analyzer is designed to provide a comprehensive view of the
resource sharing in your account and to minimize false negatives.

## Internal access findings

To use internal access analysis, you must first configure the analyzer by selecting the
specific resources you want to monitor. Once configured, internal access findings are
generated when a principal (IAM user or role) within your organization or account has access
to your selected resources. A new finding is generated the next time the analyzer scans the
specified resources and identifies a principal that has access to the resources. If an updated
policy allows a principal that is already identified in a finding, but with different
permissions or conditions, a new finding is generated for that instance of the principal and
resource. This updated policy could be a resource-based policy, identity-based policy, service
control policy (SCP), or resource control policy (RCP). IAM Access Analyzer also evaluates access
control configurations established by [declarative
policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md").

###### Note

Internal access findings are only available using the [ListFindingsV2](../../../access-analyzer/latest/APIReference/API_ListFindingsV2.md "../../../access-analyzer/latest/APIReference/API_ListFindingsV2.md")
API action.

## How IAM Access Analyzer generates findings for

internal access

To analyze internal access, you must create a separate analyzer for internal access
findings for your resources, even if you’ve already created an analyzer to generate external
access findings or unused access findings.

After creating the internal access analyzer, IAM Access Analyzer evaluates all resource-based
policies, identity-based policies, service control policies (SCPs), resource control policies
(RCPs), and permissions boundaries within your specified account or organization.

By creating an analyzer dedicated to internal access to your selected resources, you can
identify:

- When a principal in your organization or account can access your selected
  resources
- The total effective permissions allowed for a principal based on the intersection of
  all applicable policies
- Complex access paths where a principal gains access based on the combination of
  identity policies and resource policies

###### Note

IAM Access Analyzer cannot generate internal access findings for organizations that contain
more than 70,000 principals (IAM users and roles combined).

## Unused access findings

Unused access findings are generated for IAM entities (principals) within the selected
account or organization based on the number of days specified while creating the analyzer. A
new finding is generated the next time the analyzer scans the entities if one of the following
conditions is met:

- A role is inactive for the specified number of days.
- An unused permission, unused user password, or unused user access key surpasses the
  specified number of days.

###### Note

Unused access findings are only available using the [ListFindingsV2](../../../access-analyzer/latest/APIReference/API_ListFindingsV2.md "../../../access-analyzer/latest/APIReference/API_ListFindingsV2.md")
API action.

## How IAM Access Analyzer generates findings for

unused access

To analyze unused access, you must create a separate analyzer for unused access findings
for your roles, even if you’ve already created an analyzer to generate external or internal
access findings for your resources.

After creating the unused access analyzer, IAM Access Analyzer reviews access activity to
identify unused access. IAM Access Analyzer examines the last accessed information for all
IAM users, IAM roles including service roles, user access keys, and user passwords across
your AWS organization and accounts. This helps you identify unused access.

###### Note

A [service-linked
role](id_roles.md#id_roles_terms-and-concepts "id_roles.md#id_roles_terms-and-concepts") is a special type of service role that is linked to an AWS service and
owned by the service. Service-linked roles are not analyzed by unused access
analyzers.

For active IAM roles and users, IAM Access Analyzer uses last accessed information for IAM
services and actions to identify unused permissions. This allows you to scale your review
process at the AWS organization and account level. You can also use the action last accessed
information for deeper investigation of individual roles. This provides more granular insights
into which specific permissions are not being utilized.

By creating an analyzer dedicated to unused access, you can comprehensively review and
identify unused access across your AWS environment, complementing the findings generated by
your existing external access analyzer.

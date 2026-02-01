# DSOPS01-BP02 Delegate compliance responsibilities

Effective compliance at scale requires distributing responsibilities
across teams while maintaining centralized oversight and standards.
Traditional centralized compliance models create bottlenecks that
slow business velocity and limit an organization's ability to
respond quickly to regulatory changes.

By delegating compliance responsibilities to individual teams while
providing them with common guardrails and automated tools,
organizations can achieve both compliance consistency and
operational agility.

**Desired outcome:** Teams inherit
common organizational controls but are also empowered to address
regulatory requirements independently.

**Common anti-patterns:**

- Organizations entrust responsibility and accountability of
  addressing compliance requirements to a handful of experts only.
- The belief that centralizing compliance functions leads to more
  consistent and efficient implementations.
- Teams view compliance as a post-deployment concern.

**Benefits of establishing this best
practice:**

- Every team is responsible, capable, and adequately empowered to
  detect and remediate compliance issues independently.
- Teams inherit common guardrails while being empowered to add or
  customize workload-specific guardrails.
- Reduced compliance bottlenecks through distributed
  decision-making authority.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Compliance is a shared responsibility and is scaled through
empowerment. This is a five step process. It involves deploying a
suite of integrated compliance and security tooling, defining key
roles and responsibilities, setting up guardrails, delegating
responsibilities, and supporting continuous training.

### Implementation steps

1. **Deploy foundational
   tools**: Start by setting up foundational security
   and compliance tooling to create a robust compliance
   governance framework from day one. The decision guide
   [Choosing
   AWS security, identity, and governance services](../../../decision-guides/latest/security-on-aws-how-to-choose/choosing-aws-security-services.md "../../../decision-guides/latest/security-on-aws-how-to-choose/choosing-aws-security-services.md")
   assists customers in selecting services that best fit their
   needs. For more detail, see
   [AWS Security Reference Architecture (AWS SRA)](../../../prescriptive-guidance/latest/security-reference-architecture/security-tooling.md "../../../prescriptive-guidance/latest/security-reference-architecture/security-tooling.md"). The AWS
   SRA provides detailed guidelines for deploying a full
   complement of AWS security services in a multi-account
   environment. It recommends setting up a dedicated Security
   Tooling Account to co-locate your security tooling at one
   place.
2. **Define roles and
   responsibilities**: Having a set of clearly defined
   roles is essential to delegating compliance responsibilities
   at scale. Here are a few example roles:
   - Central cloud team roles. Responsibilities may include:
     - Defining organization-wide compliance policies (for
       example, encryption or logging).
     - Deploying common guardrails and provisioning
       services to individual member accounts.
     - Monitoring compliance centrally (using for example,
       [AWS Security Hub Cloud Security Posture Management](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md")).

   - Account team roles. Responsibilities may include:
     - Implementing account-specific controls (for example,
       [IAM](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md")
       policies or resource tagging).
     - Remediating resources that don't meet compliance
       requirements.
     - Reporting compliance status to the central team.

3. **Establish guardrails**:
   Guardrails provide developers with an approved method of
   self-provisioning and self-managing resources and
   environments, but within pre-set limits. For example,
   guardrails allow you to pre-set the type, size, capacity,
   and the environment within which a resource can be
   provisioned. Using
   [AWS Control Tower](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md"), you can activate common guardrails
   from your management account and attach those guardrails
   widely and consistently to member accounts. Here are some of
   the ways you set those guardrails:
   - **Service control policies
     (SCP):** By implementing
     [SCPs](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md"),
     organizations can set preventative guardrails at an
     Organizational Unit (OU) level, at the level of an
     Account, or both. SCPs are written with the same syntax
     used to define IAM policies. They apply by inheritance,
     meaning that accounts under an OU automatically inherit
     the same guardrails as set for that OU. Each OU inherits
     the same guardrails as set in the root organizational
     account. SCPs do not grant permissions to the IAM users
     and IAM roles. An SCP defines a permission guardrail, or
     sets limits, on the actions that the IAM users and IAM
     roles in your organization can perform. Common use cases
     include:
     - Restrict access to unapproved AWS Regions.
     - Block deletion of compliance-related resources.
     - Enforce encryption requirements.
     - Block unauthorized API calls.
     - Mandate resource tagging.

   - **Resource control policies
     (RCP):** While SCPs control which AWS services
     and actions can be used,
     [RCPs](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md")
     focus on controlling the configuration of specific
     resources and resource types. RCPs are applied at the
     organization root, organizational unit (OU), or at the
     account level, allowing for granular control over
     resource configurations. Common use cases of RCP
     include:
     - Restrict access to only HTTPS connections to your
       resources.
     - Consistent Amazon S3 bucket policy controls (for
       example, enforce KMS Encryption).

   - **AWS CloudFormation guard
     rules:**
     [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md") guard rules are an effective way
     to establish what a well-configured resource looks like
     and how it should behave. Develop guard rules and use
     cfn-validate and
     cfn-test to verify CloudFormation
     templates locally as well with your CI/CD pipelines.
   - **AWS Firewall Manager
     policies:** Use
     [AWS Firewall Manager](../../../waf/latest/developerguide/fms-chapter.md "../../../waf/latest/developerguide/fms-chapter.md") to administer and maintain
     ingress and egress controls across
     [multiple
     accounts and resources](../../../waf/latest/developerguide/working-with-policies.md "../../../waf/latest/developerguide/working-with-policies.md").
   - **Additional network
     controls:** Consider
     [AWS Web Application Firewall (AWS WAF)](../../../waf/latest/developerguide/what-is-aws-waf.md "../../../waf/latest/developerguide/what-is-aws-waf.md"),
     [AWS Shield Advanced](../../../waf/latest/developerguide/shield-chapter.md "../../../waf/latest/developerguide/shield-chapter.md"),
     [Amazon Virtual Private Cloud (VPC)](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") security groups,
     network ACLs,
     [AWS Network Firewall](../../../network-firewall/latest/developerguide/what-is-aws-network-firewall.md "../../../network-firewall/latest/developerguide/what-is-aws-network-firewall.md"), and
     [Amazon Route 53 Resolver DNS Firewall](https://aws.amazon.com/route53/resolver-dns-firewall/ "https://aws.amazon.com/route53/resolver-dns-firewall/") to control traffic
     across your environments.
   - **Backup and retention
     policies:** Use
     [AWS Backup](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md") to
     [set
     up organization-wide](https://repost.aws/knowledge-center/backup-organization-backups "https://repost.aws/knowledge-center/backup-organization-backups") backup and retention
     policies aligning with your regulatory requirements.
   - **Tagging policies:**
     Tags play an important role in defining the context
     under which a resource operates. By enforcing tags, you
     can apply selective behavioral controls without
     interrupting feature delivery. For more detail, see
     [Best
     Practices for Tagging AWS Resources](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md").

4. **Delegate
   responsibilities**: While SCPs, RCPs, and firewall
   policies apply consistent guardrails, they are effectively a
   form of denylisting. To empower teams, we must also think of
   allowlisting. To do this, set up delegated admin roles by
   developing IAM policies and setting up IAM permission
   boundaries:
   - Delegated admin roles enable organizations to distribute
     governance responsibilities while maintaining
     centralized oversight and compliance standards. This
     allows security, compliance, and infrastructure teams to
     independently manage their respective domains. For
     example, security teams can manage
     [Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md") findings across the organization, while
     compliance teams can monitor Config rules and Security Hub controls. AWS Services integrated with AWS Organizations support delegated administration roles.
   - Identity and access management (IAM) policies and
     resource-based policies provide the foundation for
     delegation by establishing granular access controls and
     automated policy enforcement. As a strategy, consider
     setting up broad allow lists in development and test
     environments, and then scoping them down as you move up
     to production environments. You can use
     [AWS IAM Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md") to observe permission usage
     patterns across development and test environments. By
     monitoring actual access patterns and generating policy
     recommendations based on observed usage, you can
     progressively scope down permissions without impacting
     functionality. To do this:
     - Enable IAM Access Analyzer across environments.
     - Review findings regularly as part of the code
       promotion process.
     - Integrate analyzer recommendations into your CI/CD
       pipeline and progressively reduce permissions.
     - Document justifications for deliberately broad
       permissions.
     - Use the generated policies as templates for
       production roles.

   - [IAM
     permission boundaries](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") act as a guardrail to
     define the maximum permissions an IAM entity (user or
     role) can have, regardless of the permissions granted by
     their identity-based policies. Think of them as a
     security fence that blocks privilege escalation by
     setting an upper limit on what actions can be performed.
     Permission boundaries don't grant permissions
     themselves; instead, they work in conjunction with
     identity-based policies where the effective permissions
     become the intersection of what's allowed by both the
     identity-based policy and the permission boundary. This
     provides defense-in-depth and enables secure delegation
     of IAM management tasks. Common use cases include:
     - Blocking IAM privilege escalation.
     - Limiting developer permissions in production or
       other accounts holding sensitive data. For example,
       you can create your own
       [permission
       boundaries](https://github.com/aws-samples/example-permissions-boundary "https://github.com/aws-samples/example-permissions-boundary").

5. **Train teams and document
   processes**: Prepare teams to become
   self-sufficient by providing the necessary knowledge and
   tools required to become successful.
   - Train teams on compliance tools.
   - Provide on-demand sandbox environments for teams to gain
     hands-on experience in building simple instruction
     driven solutions. Consider subscribing to
     [immersive
     learning offerings](https://aws.amazon.com/training/digital/immersive-learning/ "https://aws.amazon.com/training/digital/immersive-learning/") from AWS Skill Builder such as
     AWS Cloud Quest, SimuLearn and Industry Quest.
   - Publish compliance playbooks with step-by-step guidance
     around technical and operational capabilities required
     to support existing and emerging regulations. Allow
     teams to find playbooks on common challenges such as
     securing personally identifiable information (PII) and
     financial data.

**Example workflow**: The
following is an example of a workflow you can expect after
effective delegation of responsibilities.

1. A member account deploys an unencrypted S3 bucket.
2. AWS Config rule
   s3-bucket-server-side-encryption-enabled
   triggers a non-compliance alert.
3. AWS Security Hub aggregates the finding and notifies the
   account owner using
   [Amazon Simple Notification Service (Amazon SNS)](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md").
4. The account team uses a pre-approved
   [AWS Systems Manager](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md") runbook to enable encryption
   automatically.
5. Compliance status updates in the central dashboard.

By combining automation, delegation, and education, this model
scales seamlessly across your AWS organization.

## Resources

**Related best practices:**

- [[AG.SAD.2] Delegate identity and access management responsibilities](../devops-guidance/ag.sad.md "../devops-guidance/ag.sad.md")
- [OPS03-BP02
  Team members are empowered to take action when outcomes are at risk](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_emp_take_action.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_emp_take_action.md")
- [OPS03-BP03
  Escalation is encouraged](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_escalation.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_escalation.md")
- [OPS03-BP04
  Communications are timely, clear, and actionable](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_effective_comms.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_effective_comms.md")
- [OPS03-BP06
  Team members are encouraged to maintain and grow their skill sets](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_learn.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_learn.md")

**Related documents:**

- [Two-Pizza Teams Are Just the Start, Part 1: Accountability and
  Empowerment Are Key to High-Performing Agile Organizations](https://aws.amazon.com/blogs/enterprise-strategy/two-pizza-teams-are-just-the-start-accountability-and-empowerment-are-key-to-high-performing-agile-organizations-part-1/ "https://aws.amazon.com/blogs/enterprise-strategy/two-pizza-teams-are-just-the-start-accountability-and-empowerment-are-key-to-high-performing-agile-organizations-part-1/")
- [Two-Pizza Teams Are Just the Start, Part 2: Accountability and
  Empowerment Are Key to High-Performing Agile Organizations](https://aws.amazon.com/blogs/enterprise-strategy/two-pizza-teams-are-just-the-start-accountability-and-empowerment-are-key-to-high-performing-agile-organizations-part-2/ "https://aws.amazon.com/blogs/enterprise-strategy/two-pizza-teams-are-just-the-start-accountability-and-empowerment-are-key-to-high-performing-agile-organizations-part-2/")
- [Compliance
  validation for AWS Organizations](../../../organizations/latest/userguide/orgs_security_compliance-validation.md "../../../organizations/latest/userguide/orgs_security_compliance-validation.md")
- [Delegating
  responsibility to others using permissions boundaries](../../../IAM/latest/UserGuide/access_policies_boundaries.md#access_policies_boundaries-delegate "../../../IAM/latest/UserGuide/access_policies_boundaries.md#access_policies_boundaries-delegate")
- [Setting
  a delegated administrator account in Security Hub](../../../securityhub/latest/userguide/designate-orgs-admin-account.md "../../../securityhub/latest/userguide/designate-orgs-admin-account.md")
- [Managing
  GuardDuty accounts with AWS Organizations](../../../guardduty/latest/ug/guardduty_organizations.md "../../../guardduty/latest/ug/guardduty_organizations.md")
- [Managing
  multiple Macie accounts with AWS Organizations](../../../macie/latest/user/accounts-mgmt-ao.md "../../../macie/latest/user/accounts-mgmt-ao.md")
- [Using
  Organizations to manage behavior graph accounts](../../../detective/latest/userguide/accounts-orgs-transition.md "../../../detective/latest/userguide/accounts-orgs-transition.md")
- [Delegated
  administrator for IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-delegated-administrator.md "../../../IAM/latest/UserGuide/access-analyzer-delegated-administrator.md")
- [Designating
  a delegated administrator account for Amazon Inspector](../../../inspector/latest/user/designating-admin.md "../../../inspector/latest/user/designating-admin.md")
- [Adding
  a delegated administrator in AWS Audit Manager](../../../audit-manager/latest/userguide/add-delegated-admin.md "../../../audit-manager/latest/userguide/add-delegated-admin.md")

**Related videos:**

- [AWS re:Inforce 2022 - Deep dive into compliance and auditing at scale (GRC402)](https://www.youtube.com/watch?v=w6_xOwFYlk8&t=307s "https://www.youtube.com/watch?v=w6_xOwFYlk8&t=307s")

**Related examples:**

- [When
  and where to use IAM permissions boundaries](https://aws.amazon.com/blogs/security/when-and-where-to-use-iam-permissions-boundaries/ "https://aws.amazon.com/blogs/security/when-and-where-to-use-iam-permissions-boundaries/")

# SEC01-BP01 Separate workloads using accounts

Establish common guardrails and isolation between environments
(such as production, development, and test) and workloads through
a multi-account strategy. Account-level separation is strongly
recommended, as it provides a strong isolation boundary for
security, billing, and access.

**Desired outcome:** An account structure that isolates cloud
operations, unrelated workloads, and environments into separate accounts, increasing security
across the cloud infrastructure.

**Common anti-patterns:**

- Placing multiple unrelated workloads with different data sensitivity levels into the
  same account.
- Poorly defined organizational unit (OU) structure.
  **Benefits of establishing this best practice:**

- Decreased scope of impact if a workload is inadvertently accessed.
- Central governance of access to AWS services, resources, and Regions.
- Maintain security of the cloud infrastructure with policies and centralized
  administration of security services.
- Automated account creation and maintenance process.
- Centralized auditing of your infrastructure for compliance and regulatory
  requirements.

**Level of risk exposed if this best practice is not established**:
High

## Implementation guidance

AWS accounts provide a security isolation boundary between
workloads or resources that operate at different sensitivity
levels. AWS provides tools to manage your cloud workloads at
scale through a multi-account strategy to leverage this
isolation boundary. For guidance on the concepts, patterns,
and implementation of a multi-account strategy on AWS, see
[Organizing
Your AWS Environment Using Multiple Accounts](../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md "../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md").

When you have multiple AWS accounts under central management,
your accounts should be organized into a hierarchy defined by
layers of organizational units (OUs). Security controls can
then be organized and applied to the OUs and member accounts,
establishing consistent preventative controls on member
accounts in the organization. The security controls are
inherited, allowing you to filter permissions available to
member accounts located at lower levels of an OU hierarchy. A
good design takes advantage of this inheritance to reduce the
number and complexity of security policies required to achieve
the desired security controls for each member account.

[AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") and
[AWS Control Tower](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md") are two services that you can use to
implement and manage this multi-account structure in your AWS
environment. AWS Organizations allows you to organize accounts
into a hierarchy defined by one or more layers of OUs, with
each OU containing a number of member accounts.
[Service
control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") (SCPs) allow the organization
administrator to establish granular preventative controls on
member accounts, and
[AWS Config](../../../config/latest/developerguide/config-rule-multi-account-deployment.md "../../../config/latest/developerguide/config-rule-multi-account-deployment.md") can be used to establish proactive and detective
controls on member accounts. Many AWS services
[integrate
with AWS Organizations](../../../organizations/latest/userguide/orgs_integrate_services_list.md "../../../organizations/latest/userguide/orgs_integrate_services_list.md") to provide delegated
administrative controls and performing service-specific tasks
across all member accounts in the organization.

Layered on top of AWS Organizations,
[AWS Control Tower](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md") provides a one-click best practices setup
for a multi-account AWS environment with a
[landing
zone](../../../controltower/latest/userguide/aws-multi-account-landing-zone.md "../../../controltower/latest/userguide/aws-multi-account-landing-zone.md"). The landing zone is the entry point to the
multi-account environment established by Control Tower.
Control Tower provides several
[benefits](https://aws.amazon.com/blogs/architecture/fast-and-secure-account-governance-with-customizations-for-aws-control-tower/ "https://aws.amazon.com/blogs/architecture/fast-and-secure-account-governance-with-customizations-for-aws-control-tower/")
over AWS Organizations. Three benefits that provide improved
account governance are:

- Integrated mandatory security controls that are automatically applied to accounts
  admitted into the organization.
- Optional controls that can be turned on or off for a given set of OUs.
- [AWS Control Tower Account Factory](../../../controltower/latest/userguide/account-factory.md "../../../controltower/latest/userguide/account-factory.md") provides automated
  deployment of accounts containing pre-approved baselines and
  configuration options inside your organization.

**Implementation steps**

1. **Design an organizational unit
   structure:** A properly designed organizational
   unit structure reduces the management burden required to
   create and maintain service control policies and other
   security controls. Your organizational unit structure should
   be
   [aligned
   with your business needs, data sensitivity, and workload
   structure](https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/ "https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/").
2. **Create a landing zone for your
   multi-account environment:** A landing zone
   provides a consistent security and infrastructure foundation
   from which your organization can quickly develop, launch,
   and deploy workloads. You can use a
   [custom-built
   landing zone or AWS Control Tower](../../../prescriptive-guidance/latest/migration-aws-environment/building-landing-zones.md "../../../prescriptive-guidance/latest/migration-aws-environment/building-landing-zones.md") to orchestrate your
   environment.
3. **Establish guardrails:**
   Implement consistent security guardrails for your
   environment through your landing zone. AWS Control Tower
   provides a list of
   [mandatory](../../../controltower/latest/userguide/mandatory-controls.md "../../../controltower/latest/userguide/mandatory-controls.md")
   and
   [optional](../../../controltower/latest/userguide/optional-controls.md "../../../controltower/latest/userguide/optional-controls.md")
   controls that can be deployed. Mandatory controls are
   automatically deployed when implementing Control Tower.
   Review the list of highly recommended and optional controls,
   and implement controls that are appropriate to your needs.
4. **Restrict access to newly added
   Regions**: For new AWS Regions, IAM resources such
   as users and roles are only propagated to the Regions that
   you specify. This action can be performed through the
   [console
   when using Control Tower](../../../controltower/latest/userguide/region-deny.md "../../../controltower/latest/userguide/region-deny.md"), or by adjusting
   [IAM
   permission policies in AWS Organizations](https://aws.amazon.com/blogs/security/setting-permissions-to-enable-accounts-for-upcoming-aws-regions/ "https://aws.amazon.com/blogs/security/setting-permissions-to-enable-accounts-for-upcoming-aws-regions/").
5. **Consider AWS
   [CloudFormation
   StackSets](../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md "../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md")**: StackSets help you deploy
   resources including IAM policies, roles, and groups into
   different AWS accounts and Regions from an approved
   template.

## Resources

**Related best practices:**

- [SEC02-BP04 Rely on a centralized identity provider](sec_identities_identity_provider.md "sec_identities_identity_provider.md")

**Related documents:**

- [AWS Control Tower](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md")
- [AWS Security Audit Guidelines](../../../general/latest/gr/aws-security-audit-guide.md "../../../general/latest/gr/aws-security-audit-guide.md")
- [IAM
  Best Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
- [Use
  CloudFormation StackSets to provision resources across
  multiple AWS accounts and regions](https://aws.amazon.com/blogs/aws/use-cloudformation-stacksets-to-provision-resources-across-multiple-aws-accounts-and-regions/ "https://aws.amazon.com/blogs/aws/use-cloudformation-stacksets-to-provision-resources-across-multiple-aws-accounts-and-regions/")
- [Organizations
  FAQ](https://aws.amazon.com/organizations/faqs/ "https://aws.amazon.com/organizations/faqs/")
- [AWS Organizations terminology and concepts](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md")
- [Best
  Practices for Service Control Policies in an AWS Organizations Multi-Account Environment](https://aws.amazon.com/blogs/industries/best-practices-for-aws-organizations-service-control-policies-in-a-multi-account-environment/ "https://aws.amazon.com/blogs/industries/best-practices-for-aws-organizations-service-control-policies-in-a-multi-account-environment/")
- [AWS Account Management Reference Guide](../../../accounts/latest/reference/accounts-welcome.md "../../../accounts/latest/reference/accounts-welcome.md")
- [Organizing
  Your AWS Environment Using Multiple Accounts](../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md "../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md")

**Related videos:**

- [Enable AWS
  adoption at scale with automation and governance](https://youtu.be/GUMSgdB-l6s "https://youtu.be/GUMSgdB-l6s")
- [Security
  Best Practices the Well-Architected Way](https://youtu.be/u6BCVkXkPnM "https://youtu.be/u6BCVkXkPnM")
- [Building
  and Governing Multiple Accounts using AWS Control Tower](https://www.youtube.com/watch?v=agpyuvRv5oo "https://www.youtube.com/watch?v=agpyuvRv5oo")
- [Enable Control Tower for Existing
  Organizations](https://www.youtube.com/watch?v=CwRy0t8nfgM "https://www.youtube.com/watch?v=CwRy0t8nfgM")

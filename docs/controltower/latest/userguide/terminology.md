# Terminology

Here’s a quick review of some terms you'll see in the AWS Control Tower documentation.

First, it's good to know that AWS Control Tower shares a lot of terminology with the AWS Organizations service, including the terms _organization_
and _organizational unit (OU)_, which appear throughout
this document.

- For more information about organizations and OUs, see [AWS Organizations terminology and concepts](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md"). If you're new to AWS Control Tower, that
  terminology is a good place to begin.
- [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") is
  an AWS service that helps you centrally govern your environment as you grow and
  scale your workloads on AWS. AWS Control Tower relies on AWS Organizations to create accounts, to
  enforce preventive controls at the OU level, and to provide centralized
  billing.
- An [AWS Account Factory
  account](account-factory.md "account-factory.md") is an AWS account provisioned using Account Factory in
  AWS Control Tower. Sometimes, Account Factory is referred to informally as a “vending
  machine” for accounts.
- Your AWS Control Tower [home Region](best-practices.md#tips-for-admin-setup "best-practices.md#tips-for-admin-setup") is the AWS Region in which your AWS Control Tower landing zone was
  deployed. You can view your home Region in your landing zone settings.
- [AWS Service Catalog](../../../servicecatalog/latest/adminguide/introduction.md "../../../servicecatalog/latest/adminguide/introduction.md")
  allows you to manage commonly deployed IT services, centrally. In the context of
  this document, Account Factory uses AWS Service Catalog to provision new AWS accounts,
  including accounts from customized blueprints.
- [AWS
  CloudFormation StackSets](../../../AWSCloudFormation/latest/UserGuide/stacksets-concepts.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-concepts.md") are a type of resource that extends the
  functionality of stacks so that you can create, update, or delete stacks across
  multiple accounts and Regions with a single operation and a single CloudFormation
  template.
- A  [stack instance](../../../AWSCloudFormation/latest/UserGuide/stacksets-concepts.md#stacksets-concepts-stackinstances "../../../AWSCloudFormation/latest/UserGuide/stacksets-concepts.md#stacksets-concepts-stackinstances") is a reference to a stack in a target account within a
  Region.
- A [stack](../../../AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.md#w2ab1b5c15b "../../../AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.md#w2ab1b5c15b") is a collection of AWS resources that you can manage as a
  single unit.
- An [aggregator](../../../config/latest/developerguide/aggregate-data.md "../../../config/latest/developerguide/aggregate-data.md") is an
  AWS Config resource type that collects AWS Config configuration and compliance data from
  multiple accounts and Regions within the organization, allowing you to view and
  query this compliance data within a single account.
- A [conformance
  pack](../../../config/latest/developerguide/conformance-packs.md "../../../config/latest/developerguide/conformance-packs.md") is a collection of AWS Config rules and remediation actions that can be
  deployed as a single entity in an account and a Region, or across an organization in
  AWS Organizations. You can use a conformance pack to help customize your AWS Control Tower
  environment. For technical blogs that provide more details, see [Related information](related-information.md#working-existing-organizations "related-information.md#working-existing-organizations").
- A [baseline](types-of-baselines.md "types-of-baselines.md") in
  AWS Control Tower is a group of resources and specific configurations that you can apply to a
  target. The most common baseline target may be an organizational unit (OU). For
  example, the baseline called `AWSControlTowerBaseline` is available to
  help register your OUs with AWS Control Tower. During landing zone setup and update, the
  baseline target may be a shared account, or a specific setting for the landing zone
  as a whole.
- **Blueprint:** A blueprint is an artifact that
  encapsulates some metadata, which describes infrastructure components that are
  deployed within an account. For example, an AWS CloudFormation template can serve as a blueprint
  for an AWS Control Tower account.
- **Drift:** A change in a resource installed by and
  configured by AWS Control Tower. Resources without drift enable AWS Control Tower to function
  properly.
- **Non-compliant resource:** A resource that is in
  violation of an AWS Config rule that defines a particular detective control.
- **Shared account:** One of the three accounts that
  AWS Control Tower creates automatically when you set up your landing zone: the management
  account, the log archive account, and the audit account. You can choose customized
  names for the log archive account and the audit account, during setup.
- **Member account:** A member account belongs to the
  AWS Control Tower organization. The member account can be _enrolled_ or _unenrolled_ in
  AWS Control Tower. When a registered OU contains a mix of enrolled and unenrolled
  accounts:

      + Preventive controls enabled on (or inherited by) the OU apply to all
       accounts within it, including unenrolled ones. This is true because
       preventive controls are enforced with SCPs, RCPS, or declarative policies at the OU level, not the account
       level. For more information, see [Inheritance for service control policies](../../../organizations/latest/userguide/orgs_manage_policies_inheritance_auth.md "../../../organizations/latest/userguide/orgs_manage_policies_inheritance_auth.md") in the AWS Organizations
       documentation.
      + Detective controls enabled on the OU do not apply to unenrolled
       accounts.
      + Proactive controls are implmented by AWS CloudFormation hooks. These controls do not apply to unenrolled
       accounts in an OU.

  An account can be a member of only one organization at a time, and its charges are
  billed to the management account for that organization. A member account can be
  moved to the root container of an organization.

- **AWS account:** An AWS account acts as a
  resource container and resource isolation boundary. An AWS account can be
  associated with billing and payment. An AWS account is different than a user
  account (sometimes called an [IAM user
  account](setting-up.md#setting-up-iam "setting-up.md#setting-up-iam")) in AWS Control Tower. Accounts created through the Account Factory
  provisioning process are AWS accounts. AWS accounts also can be added to
  AWS Control Tower by means of an account enrollment or OU registration process.
- **Control:** A control (also known as a _guardrail_) is a high-level rule that provides ongoing
  governance for your overall AWS Control Tower environment. Each control enforces a single
  rule. Preventive controls are implemented with SCPs. Detective controls are
  implemented with AWS Config rules. Proactive controls are implemented with AWS CloudFormation hooks.
  For more information, see [How controls work](how-controls-work.md "how-controls-work.md").
- **Control Catalog:** The AWS Control Tower control catalog is the compendium of all controls that are available through AWS Control Tower, in the console and APIs. It formerly was called the Control Library. We aligned the terminology to the name of the namespace, _controlcatalog_.
- **Landing zone:** A landing zone is a cloud
  environment that offers a recommended starting point, including default accounts,
  account structure, network and security layouts, and so forth. From a landing zone,
  you can deploy workloads that utilize your solutions and applications.
- **Framework:** A framework is a specific regulatory standard or industry requirement. In the Control Catalog ontology, a framework is represented by a Standard control. For more information, see the Control Catalog [Ontology overview](../../../controlcatalog/latest/userguide/ontology-overview.md "../../../controlcatalog/latest/userguide/ontology-overview.md").
- **Nested OU:** A nested OU in AWS Control Tower is an OU
  contained within another OU. A nested OU can have exactly one parent OU, and each
  account can be a member of exactly one OU. Nested OUs create a hierarchy. When you
  attach a policy to one of the OUs in the hierarchy, it flows down and affects all
  the OUs and accounts beneath it. A nested OU hierarchy in AWS Control Tower can be a maximum
  of five levels deep.
- **Parent OU:** The OU immediately above the current
  OU in the hierarchy. Each OU can have exactly one parent OU.
- **Child OU:**
  Any OU below the
  current OU in the hierarchy. An OU can have many child OUs.
- **OU hierarchy:** In AWS Control Tower, the hierarchy of
  nested OUs can have up to five levels. The order of nesting is referred to as
  **Levels**. The top of the hierarchy is designated as
  **Level 1**.
- **Top-level OU:** A top-level OU is any OU that's
  directly under the Root, not the Root itself. The Root is not considered an
  OU.
- **Governed:** A governed Region is managed and
  controlled in your environment by AWS Control Tower, according to the governance policies set
  by your organization. These AWS Regions are monitored to adhere to best practices
  and organizational policies. Your resources in these Regions are protected when you enable AWS Control Tower controls.
- **Not governed:** Regions that show **Not
  governed** status are not controlled or monitored by AWS Control Tower. These
  AWS Regions usually do not adhere to the same governance policies that AWS Control Tower
  enforces. You can create resources in these Regions, but those resources are not protected by AWS Control Tower controls.
- **Denied:** A denied Region is blocked specifically by
  AWS Control Tower. Within your AWS Control Tower environment, you cannot provision resources in these
  AWS Regions.

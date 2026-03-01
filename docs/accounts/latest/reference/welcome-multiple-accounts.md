# Benefits of using multiple AWS accounts

AWS accounts form the foundational security boundary in the AWS Cloud. They serve as a
container for resources, providing a critical layer of isolation that is essential for
creating a secure, well-governed environment. For more information, see [What is an AWS account?](accounts-welcome.md "accounts-welcome.md").

Separating your resources into separate AWS accounts helps you to support the following
principles in your cloud environment:

- **Security control** – Different applications
  can have different security profiles, requiring different control policies and
  mechanisms around them. For example, it’s far easier to talk to an auditor and be
  able to point to a single AWS account that hosts all elements of your workload
  that are subject to [Payment Card Industry (PCI) Security Standards](https://www.pcisecuritystandards.org/pci_security/ "https://www.pcisecuritystandards.org/pci_security/").
- **Isolation** – An AWS account is a unit of
  security protection. Potential risks and security threats should be contained within
  an AWS account without affecting others. There could be different security needs
  due to different teams or different security profiles.
- **Many teams** – Different teams have their
  different responsibilities and resource needs. You can prevent teams from
  interfering with each other by moving them to separate AWS accounts.
- **Data isolation** – In addition to isolating
  the teams, it's important to isolate the data stores to an account. This can help
  limit the number of people that can access and manage that data store. This helps
  contain exposure to highly private data and therefore can help in compliance with
  the [European Union's General Data Protection Regulation
  (GDPR)](https://gdpr.eu "https://gdpr.eu").
- **Business process** – Different business
  units or products may have completely different purposes and processes. With
  multiple AWS accounts, you can support a business unit's specific needs.
- **Billing** – An account is the only true way
  to separate items at a billing level. Multiple accounts help separate items at a
  billing level across business units, functional teams, or individual users. You can
  still get all of your bills consolidated to a single payer (using AWS Organizations and
  consolidated billing) while having line items separated by AWS account.
- **Quota allocation** – AWS service quotas
  are enforced separately for each AWS account. Separating workloads into different
  AWS accounts prevents them from consuming quotas for each other.
  All of the recommendations and procedures described in this document are in compliance
  with the [AWS
  Well-Architected Framework](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected"). This framework is intended to help you design a
  flexible, resilient, and scalable cloud infrastructure. Even when you are starting small, we
  recommend that you proceed in compliance with this guidance in the framework. Doing so can
  help you scale your environment securely and without impacting your ongoing operations as
  you grow.

## Managing multiple AWS accounts

Before you start adding multiple accounts, you'll want to develop a plan to manage
them. For that, we recommend that you use [AWS Organizations](https://aws.amazon.com/organizations "https://aws.amazon.com/organizations"), which is a free AWS service to manage all of the AWS accounts
in your organization.

AWS also offers AWS Control Tower, which adds layers of AWS managed automation to Organizations
and automatically integrates it with other AWS services like AWS CloudTrail, AWS Config,
Amazon CloudWatch, AWS Service Catalog, and others. These services can incur additional costs. For more
information, see [AWS Control Tower
pricing](https://aws.amazon.com/controltower/pricing "https://aws.amazon.com/controltower/pricing").

### See also

- [When to use AWS Organizations](using-orgs.md "using-orgs.md")
- [When to use AWS Control Tower](when-to-use-control-tower.md "when-to-use-control-tower.md")

# MALZ network architecture

## About multi-account landing zone network architecture

Before you start the onboarding process to AWS Managed Services (AMS) Multi-account landing zone (MALZ), it is important to understand the baseline
architecture, or landing zone, that AMS creates on your behalf, its components, and functions.

AMS multi-account landing zone is a multi-account architecture, pre-configured with the
infrastructure to facilitate authentication, security, networking, and logging.

###### Note

For estimates of costs, see
[AMS multi-account landing zone environment basic components](../userguide/ams-sd.md#basic-components-malz "../userguide/ams-sd.md#basic-components-malz").

###### Topics

- [Service region](#service-region "#service-region")
- [Organizational units](#malz-ous "#malz-ous")
- [Service control policies and AWS Organization](#malz-scps "#malz-scps")

The following diagram outlines at a high level the account structure and how infrastructure is segregated into each of
the accounts:

![AWS account structure diagram showing management, shared services, network, security, and log archive accounts.](images/MALZ-high-level-Nov2022.png)

### Service region

All resources within an AMS multi-account landing zone are deployed within a single AWS Region
of your choice, due to current cross region limitation with Active Directory and Transit Gateway.

### Organizational units

A typical AMS multi-account landing zone consists of four top-level organizational units (OUs):

- The core Organizational unit (OU) (used to group accounts together to administer as a single unit)
- The applications OU
- The customer-managed OU
- The accelerate OU

AMS-managed multi-account landing zone also enables you to create custom OUs for grouping and organizing
AWS Accounts and to associate custom SCPs with them; for examples on doing this, see

[Management account | Create Custom OUs](../ctref/deployment-managed-management-account-create-custom-ous.md "../ctref/deployment-managed-management-account-create-custom-ous.md") and
[Management account | Create Custom SCP (managed automation)](../ctref/deployment-managed-management-account-create-custom-scp-review-required.md "../ctref/deployment-managed-management-account-create-custom-scp-review-required.md"),

respectively. AMS provides four existing OUs under which new OUs and accounts
can be requested: accelerate, applications > managed, applications > development, and customer-managed.

- accelerate OU:

This is a top-level OU in AMS multi-account landing zone (MALZ). Accounts under this OU are provisioned by AMS with an RFC
(Deployment | Managed landing zone | Management account | Create Accelerate account, change type ID: ct-2p93tyd5angmi).
In these accelerate application accounts, you can benefit from accelerate operational services such as monitoring and alerting,
incident management, security management, and backup management. For more details, see
[AMS Accelerate accounts](../userguide/malz-accelerate-account.md "../userguide/malz-accelerate-account.md").

- applications > managed OU:

In this sub organizational unit of the Application OU, accounts are fully managed by AMS including
all operational tasks. The operational tasks include service request management, incident management,
security management, continuity management, patch management, cost optimization, monitoring and event
management. These tasks are carried out for your infrastructure's management.
Multiple child OUs can be created as needed, until a maximum limit of nested OUs is reached for
AWS organizations. For details, see
[Quotas for AWS Organizations](../../../organizations/latest/userguide/orgs_reference_limits.md "../../../organizations/latest/userguide/orgs_reference_limits.md").

- applications > development OU:

Under this sub-OU of the application OU in AMS-managed landing zone, accounts are
[Developer mode](../userguide/developer-mode-section.md "../userguide/developer-mode-section.md") accounts that provide you
with elevated permissions to provision and update AWS resources outside
of the AMS change management process. This OU also supports the creation of new children
OU as needed.

- customer-managed OU:

This is a top-level OU in AMS multi-account landing zone. Accounts under this OU are provisioned
by AMS with an RFC. In these accounts, the operations of workloads and AWS resources are
your responsibility. This OU also supports the creation of new children OU as needed.

As a best practice, we recommend that accounts under these OUs and custom-requested sub-OUs be grouped based
on their functionalities and policies.

### Service control policies and AWS Organization

AWS provides service control policies (SCPs) for permissions management in an AWS Organization.
SCPs are used to define additional guardrails for what actions users can perform in which OUs.
By default, AMS provides a set of SCPs deployed in management accounts which provide protections at
different default OU levels. For SCP restrictions, please contact your CSDM.

You can also create custom SCPs and attach them to specific OUs. They can be requested from your Management account
using change type ct-33ste5yc7hprs. AMS then reviews the custom SCPs requested before applying them to the
target OUs. For examples, see

[Management account | Create Custom OUs](../ctref/deployment-managed-management-account-create-custom-ous.md "../ctref/deployment-managed-management-account-create-custom-ous.md") and
[Management account | Create Custom SCP (managed automation)](../ctref/deployment-managed-management-account-create-custom-scp-review-required.md "../ctref/deployment-managed-management-account-create-custom-scp-review-required.md").

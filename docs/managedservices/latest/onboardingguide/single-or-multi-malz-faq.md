# Single multi-account landing zone vs. Multiple multi-account landing zone FAQs

Some commonly asked questions when choosing to set up a single multi-account landing zone or multiple multi-account landing zones:

**Q1**: Can I start with a single multi-account landing zone and move to multiple multi-account landing zone,
if any account limits or business constraints are encountered?

**A**: Yes. You can choose to set up another multi-account landing zone at any given time:

- A new billing payer account will be required to be setup (currently
  AWS doesn’t support multi-payer accounts in a single AWS org).
- Multi-Account Landing Zone base build takes up to 2 weeks lead time once the multi-account landing zone questionnaire is filled out.
- Every multi-account landing zone means an addition of ~3K USD / month running cost.
- N/W, AD, DNS, and SSO integration will be required to establish for new MALZ.
- Any Reserved Instances (RIs), Cost Saving plans will be needed to be setup for the new multi-account landing zone
  (RIs are not transferrable).
- AMS multi-account landing zone doesn't support migration of an account across multi-account landing zone accounts; for example, across
  AWS Orgs. However, to move applications from one account to another is possible using standard
  migration methods.
  **Q2**: What is AMS approach to MALZ updates/changes to underlying/shared
  infrastructure and quantify the risk to customers? Provide details on what assurances are wrapped into
  the process. How do Customers get comfortable that MALZ updates/changes will not impact customers?
  Is there any measures Customer need to take to prevent disruption?

**A**: AMS follows a strict change methodology using internal tools that
enables us to define, review, schedule and execute changes to customers' environments.

The process to release updates enforces code reviews, integration testing, deployment in gamma and beta
environments, and additional baking time and testing in beta and gamma environments before releasing to
customers environments. All releases include rollback procedures and are closely monitored by the releases
team and the team who created and requested the change. The scope of the releases are confined to stacks
owned and provisioned by AMS. On average, we execute at least one release per week.

In addition:

- AMS SLA are applicable. As per AMS service description any incident raised post shared
  infra maintenance activity would adhere to entitled SLA for resolution or credits.
- No special preventive measures are required by Customers to prevent disruption to common
  infrastructure. Customers have Read-Only permissions at AWS Org or Core OU accounts, so customers
  can’t make any destructive changes to the MALZ core env. All customer’s requests to Core infrastructure
  requires AMS review and approval.
- Customers can test certain Org level changes like SCPs/Roles at individual non-prod account
  levels before propagating changes at App OU level. It is on the AMS roadmap to allow multiple APP OUs
  (Q2 2020), which would further alleviate risk in making some of the ORG level changes. MALZ team has
  already released separate OU for “Build Mode” accounts, to ensure clear segregation of customer
  ownership and separate controls.
- Most of these are changes that allow AMS to operate the workload in effective and efficient
  manner and does not necessarily impact customers workload. Where AMS believes a shared infra change can
  have an impact to customers’ workload they are then aligned with customers’ change window.
  **High level recommendation**, start with multiple multi-account landing zones if:

- If it helps you achieve any specific compliance.
- If you need to use Multi-Region.
- If you have different on-prem ADs and Networks for Prod/Material vs Non-Prod/Non-Material
  workloads, to clearly segregate b/w the workloads.

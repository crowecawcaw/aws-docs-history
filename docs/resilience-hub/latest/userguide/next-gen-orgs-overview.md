

# Overview of multi-account governance in the next generation of Resilience Hub
<a name="next-gen-orgs-overview"></a>

Next generation Resilience Hub enables centralized resilience governance across your AWS organization. With Organizations integration, you can:
+ View resilience posture across all accounts from a single dashboard.
+ Create and publish organization-wide resilience policies.
+ Monitor compliance across hundreds of accounts and services.
+ Filter by account, AWS Region, organizational unit (OU), and policy.

The following core concepts apply to the Organizations integration model:


| Concept | Description | 
| --- | --- | 
| Delegated administrator | A member account designated to manage the next generation of Resilience Hub across the organization | 
| Org-level policies | Resilience policies created by the DA, visible and assignable across all member accounts | 
| Service-Linked Roles | Automatically created in member accounts for read-only cross-account access | 

In AWS Organizations, the delegated administrator:
+ Has visibility into all systems and services across all member accounts.
+ Creates and publishes organization-wide resilience policies by associating them with user journeys on shared systems.
+ Views aggregated resilience posture dashboards.

Service-Linked Roles (SLRs) are automatically created in all member accounts when trusted access is enabled, providing the DA with read-only cross-account visibility without manual IAM setup.
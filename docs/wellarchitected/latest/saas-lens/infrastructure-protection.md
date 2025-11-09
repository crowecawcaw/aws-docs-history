# Infrastructure protection

| SaaS SEC 2: How are you ensuring that tenant resources are<br>protected from cross-tenant access? |
| ------------------------------------------------------------------------------------------------- |
|                                                                                                   |

Tenant isolation is one of the foundational topics that every
SaaS provider must address. As independent software vendors
(ISVs) make the shift toward SaaS and adopt a shared
infrastructure model to achieve cost and operational
efficiency, they also take on the challenge of determining how
their multi-tenant environments will ensure that tenants are
prevented from accessing another tenant’s resources. Crossing
this boundary in any form would represent a significant and
potentially unrecoverable event for a SaaS business.

While the need for tenant isolation is viewed as essential to
SaaS providers, the strategies and approaches to achieving
this isolation are not universal. There are a wide range of
factors that can influence how tenant isolation is realized in
any SaaS environment. The domain, compliance, deployment
model, and the selection of AWS services all bring their own
unique set of considerations to the tenant isolation story.

###### Topics

- [The isolation mindset](isolation-mindset.md "isolation-mindset.md")
- [Core isolation concepts](core-isolation-concepts.md "core-isolation-concepts.md")

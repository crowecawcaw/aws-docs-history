# Tenant Isolation

Tenant isolation is one of the foundational topics that every SaaS
provider must address. As independent software vendors (ISVs) make
the shift toward SaaS and adopt a shared infrastructure model to
achieve cost and operational efficiency, they also have to take on
the challenge of determining how their multi-tenant environments
will ensure that each tenant is prevented from accessing another
tenant’s resources. Crossing this boundary in any form would
represent a significant and potentially unrecoverable event for a
SaaS business.

While the need for tenant isolation is viewed as essential to SaaS
providers, the strategies and approaches to achieving this
isolation are not universal. There are a wide range of factors
that can influence how tenant isolation is realized in any SaaS
environment. The domain, compliance, deployment model, and the
selection of AWS services all bring their own unique set of
considerations to the tenant isolation story.

Regardless of how the isolation is implemented, each SaaS
architecture needs to ensure that it has put in place the
constructs that are needed to ensure that each tenant’s resources
have been effectively isolated.

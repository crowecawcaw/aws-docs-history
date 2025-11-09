# Software and architecture patterns

| SaaS SUS 1: How do you use deployment models (silo, bridge, pool)<br>to align tenant consumption with resource utilization? |
| --------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                             |

- **Best Practice–01:** Have a good understanding of the key
  value and principles behind the silo, pool, and bridge models, including awareness how silo
  and pool strategies can be applied more granularly across the layers and services of your solution.
- **Best Practice–02:** Understand the operational tradeoffs
  of each model. Build a unified onboarding, operations, and analytics experience spanning
  any of these models.
- **Best Practice–03:** Have a complete end-to-end automated
  tenant onboarding process that maps the tenancy models to the resources that are
  provisioned at each architecture layer or component. Also have detailed insights into
  the footprint and consumption costs and tradeoffs associated with each of these models
  SaaS applications can be built using a variety of different architectural models.
  Regulatory, competitive, strategic, cost efficiency, and market considerations all influence
  the shape of your SaaS architecture. At the same time, there are strategies and patterns
  that can be applied when defining the footprint of the components within a SaaS application.
  These patterns—silo, bridge, and pool—can be applied in combinations to enable the most
  efficient consumption of infrastructure resources.

  **AWS services recommendation:**

- AWS WA SaaS Lens guidance on [Architectural
  model](silo-pool-and-bridge-models.md "silo-pool-and-bridge-models.md")
- [SaaS Tenant Isolation Strategies whitepaper](../../../whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.md "../../../whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.md")
- Amazon EKS SaaS reference solution [https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/amazon-eks-saas.html](amazon-eks-saas.md "amazon-eks-saas.md")
- Serverless SaaS reference solution [https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/serverless-saas.html](serverless-saas.md "serverless-saas.md")

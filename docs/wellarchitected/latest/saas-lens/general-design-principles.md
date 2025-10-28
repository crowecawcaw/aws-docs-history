# General design principles

The Well-Architected Framework identifies a set of general design
principles to facilitate good design in the cloud for SaaS
applications:

- **There’s no one-size-fits-all SaaS
  architecture**: The needs of SaaS businesses, the
  nature of their domain, their compliance requirements, the
  segments of their market, the nature of their solution—all of
  these factors have a distinct influence on the architecture of a
  SaaS environment. Every SaaS architecture should be surrounded
  with an operational and customer experience that realizes the
  agility and software as a service tenets that are core to
  succeeding as a SaaS offering. Regardless of how the system is
  architected, the system should enable tenants to be onboarded,
  managed, and operated through a single pane of glass that allows
  the SaaS organization to achieve the agility and economies of
  scale that are foundational to building a SaaS business.
- **Decompose each service based on its
  multi-tenant load and isolation profile**: If you’re
  decomposing your system into services, your decomposition
  strategy should consider how multi-tenant loads, tenant tiers,
  and isolation requirements will influence the services that are
  part of your system. In these scenarios, each service needs to
  be considered separately. Some services might be able to pool
  data, for example, while others might need to silo the data they
  manage based on compliance or noisy neighbor considerations. You
  might also find that some services will be deployed in a silo
  model to enable tiering strategies. Premium tenants, for
  example, might have some services that are available in a silo
  model as part of the value story of the premium tier.
- **Isolate all tenant resources**:
  The success of a SaaS system relies heavily on a security model
  that ensures that tenant resources are always protected from any
  cross-tenant access. A robust SaaS architecture will introduce
  isolation strategies across all layers of the architecture,
  providing specific constructs that ensure that any attempt to
  access a tenant resource is valid for the current tenant
  context.
- **Design for growth**: The move
  to a SaaS model is often about growth for SaaS organizations. As
  you define the architectural and operational footprint of your
  SaaS offering, you must continually be thinking about how your
  environment will be able to support an accelerating wave of new
  tenants. SaaS architects must build a highly agile, frictionless
  environment that can accommodate spikes in tenant onboarding
  without adding significant operational overhead. The idea here
  is to allow for growth in your customer base that doesn’t expand
  the operational or infrastructure footprint of your SaaS
  environment.
- **Instrument, capture, and analyze tenant
  metrics**: When you put multiple tenants into an
  environment—especially a shared environment—it can be
  challenging to have a clear view of how tenants are using your
  system. SaaS teams need to invest in metrics instrumentation
  that can surface insights into the features tenants are using,
  the load they are putting on your system, the bottlenecks they
  are facing, the cost profile of their activities, and so on.
  This data is core to analyzing tenant trends that directly
  impact the business, architectural, and operational health of a
  SaaS company and inform its strategy.
- **Onboard tenants through a single,
  automated, repeatable process**: SaaS is all about
  agility. A key piece of this agility story is the tenant
  onboarding process. A robust SaaS system will include a
  frictionless, repeatable process for onboarding new tenants to
  your system. This promotes scale and is core to enabling growth.
  It also ensures that new customers will have a faster path to
  value.
- **Plan to support multiple tenant
  experiences**: SaaS markets and customers don’t all fit
  into a single profile. SaaS companies often need to support a
  range of tenant profiles that can place different demands on
  your architecture and operations. As a SaaS provider and
  architect, it’s essential to model these tenant personas and
  build a single environment that includes the constructs and
  mechanisms needed to span a range of tenant experiences without
  requiring one-off versions of your product. It’s important to
  identify the value boundaries of your system to enable the
  business to create tiers of your offering that can reach
  multiple segments and promote a customer’s advancement through
  these tiers.
- **Support one-off requirements through
  global customization**: SaaS agility and innovation are
  achieved by having a single environment that is run by all
  customers. Being able to update, manage, and operate all
  customers collectively is foundational to SaaS. The reality is,
  though, some customers may request customizations. These
  customizations should be introduced as configuration options
  that are available to any customer. Keeping these features in
  the core of the offering enables a SaaS company to support
  one-off needs without undermining the agility, operational
  efficiency, and innovation goals of the business.
- **Bind user identity to tenant
  identity**: Every layer of your architecture is likely
  to need some notion of tenant context to be able to log data,
  record metrics, access data, and so on. This means that tenant
  context needs to become a first-class construct that can be
  resolved and easily accessed by the layers of your application
  without invoking another service. The authentication and
  authorization experience of your solution should bind the tenant
  identity (and potentially other tenant attributes) to the
  identity of the authenticated user. This will yield a
  _SaaS identity_ that is passed through all
  the layers of your system, enabling easy access to tenant
  context.
- **Align infrastructure consumption with
  tenant activity**: The activity of tenants in a SaaS
  environment is often unpredictable. Which resources tenants are
  consuming, how they’re consuming them, and when they are
  consuming them can vary significantly. The number of tenants in
  your system can also change regularly. While these factors can
  present scaling challenges, a robust SaaS architecture will
  employ policies that limit over-provisioning and align an
  application’s infrastructure consumption with the real-time
  trends in tenant activity. This promotes tighter alignment
  between tenant workloads and the cost profile of your overall
  SaaS infrastructure.
- **Limit developer awareness of
  multi-tenant concepts**: While tenancy will flow though
  the layers of your architecture, it should be your goal to limit
  the degree to which developers have exposure to tenancy. As a
  rule of thumb, a developer’s experience writing a multi-tenant
  service should not be all that different from writing a service
  that has no notion of tenancy. If developers need to introduce
  tenancy throughout their code, this will make it challenging to
  manage and enforce compliance with your application’s
  multi-tenant policies and mechanisms. This means providing
  libraries and reusable constructs to developers that hide the
  details of tenancy.
- **SaaS is a business strategy—not a
  technical implementation**: SaaS environments and their
  underlying technology choices are shaped directly by the
  agility, innovation, and competitive needs of the business. The
  emphasis and mindset here centers around the creation of a
  service experience for customers that focuses on zero downtime,
  regular updates, and closer connection with customers. This
  means designing an architectural and operational footprint that
  can promote continual evolution and rapid response to market
  demands. A technically solid architecture that doesn’t enable
  agility, innovation, and operational efficiency will be unlikely
  to keep pace with the competitive landscape of the
  market—especially if you’re competing with other SaaS providers.
- **Create tenant-aware operational
  views**: Operations teams are presented with a new set
  of challenges in a multi-tenant environment. While having a
  global view of a system’s health and activity remains important
  in SaaS environments, a robust SaaS operational footprint will
  also include insights into how specific tenants or tenant tiers
  are exercising your system. SaaS operations teams should
  construct dashboards and views that enable them to analyze and
  profile the activity and load of individual tenants. Being able
  to view and troubleshoot usage through the lens of individual
  tenants is essential to building a proactive, efficient
  multi-tenant operations experience.
- **Measure the cost impact of individual
  tenants**: The business, architects, and operations
  teams for a SaaS company often need to have a clear picture of
  how tenants are impacting the cost footprint of a SaaS
  environment. For example, are tenants in the basic tier imposing
  higher costs than tenants in the premium tier? Are tenant
  consumption patterns or features changing the cost profile of
  your environment? These are among the questions that can best be
  answered by have a clear view into tenant cost profiles. This is
  especially important to understand in environments where tenant
  resources are shared by multiple tenants. Collecting and
  surfacing this data often provides a SaaS business with valuable
  insights that can shape the architecture and business model of a
  SaaS company.

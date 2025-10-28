# Silo, Pool, and Bridge Models

SaaS applications can be built with a variety of different
architectural models. Regulatory, competitive, strategic, cost
efficiency, and market considerations all have some influence on
the shape of your SaaS architecture. At the same time, there are
strategies and patterns that are applied when defining the
footprint of a SaaS application. These patterns fall into one of
three categories—silo, bridge, and pool.

The **silo model** refers to an
architecture where tenants are provided dedicated resources.
Imagine, for example, as SaaS environment where each tenant of
your system has a fully independent infrastructure stack. Or,
perhaps each tenant of your system has a separate database.
When some or all of a tenant’s resources are deployed
in this dedicated fashion, we refer to this as a silo model. It’s
important to note that—even though the silo has dedicated
resources—a silo environment still relies on a shared identity,
onboarding, and operational experience where all tenants are
managed and deployed via a shared construct. This differentiates
SaaS from a managed service model where customers might be running
separate versions of your product with separate onboarding,
management, and operational experiences.

In contrast, the **pool model** of
SaaS refers to a scenario where tenants share resources. This is
the more classic notion of multi-tenancy where tenants rely on
shared, scalable infrastructure to achieve economies of scale,
manageability, agility, and so on. These shared resources can
apply to some or all of the elements of your SaaS architecture,
including compute, storage, messaging, etc.

The final pattern is the **bridge
model**. _Bridge_ is meant to
acknowledge the reality that SaaS businesses aren’t always
exclusively silo or pool. Instead, many systems have a mixed mode
where some of the system is implemented in a silo model and some
is in a pooled model. For example, some microservices in your
architecture might be implemented with silo and others might use
pool. The regulatory profile of a service’s data and its noisy
neighbor attributes might steer a microservice to a silo model.
Meanwhile the agility, access patterns, and cost profile of
another microservice could tip it toward a pool model.

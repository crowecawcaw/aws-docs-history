# The isolation mindset

At the conceptual level, many SaaS providers would agree on
the importance and value of protecting and isolating tenant
resources. However, as you dig into the details of
implementing an isolation strategy, you’ll often find that
each SaaS ISV has their own definition of what is
_enough_ isolation.

Given these varying perspectives, we have outlined some tenets
below that will help guide your overall value system for
tenant isolation. Every SaaS provider should establish a clear
set of high-level isolation requirements that will guide their
teams as they define the isolation footprint of their SaaS
environment. The following are some key tenets that typically
shape the overall SaaS tenant isolation model:

**Isolation is not optional** –
Isolation is a foundational element of SaaS and every system
that delivers a solution in a multi-tenant model should ensure
that their systems take measures to ensure that tenant
resources are isolated.

**Authentication and authorization are
not equal to isolation** – While it is expected that
you will control access to your SaaS environments through
authentication and authorization, getting beyond the entry
points of a login screen or an API does not mean you have
achieved isolation. This is just one piece of the isolation
puzzle and is not enough on its own.

**Isolation enforcement should not be
left to service developers** – While developers are
never expected to introduce code that might violate isolation,
it’s unrealistic to expect that they will never
unintentionally cross a tenant boundary. To mitigate this,
scoping of access to resources should be controlled through
some shared mechanism that is responsible for applying
isolation rules (outside the view of developers).

**If there’s not an out-of-the box
isolation solution, you may have to build it
yourself** – There are a number of security
mechanisms, such as AWS Identity and Access Management (IAM),
that can help you simplify the path to tenant isolation.
Combining these tools with your broader security scheme can
help make isolation an easier process.. However, there might
be scenarios where your isolation model is not directly
addressed by a corresponding tool or technology. The absence
of a clear solution should not represent an opportunity to
lower your isolation requirements—even if that means building
something of your own.

**Isolation is not a resource-level
construct** – In the world of multi-tenancy and
isolation, some will view isolation as a way to draw a hard
boundary between concrete infrastructure resources. This often
translates into isolation model where you might have separate
databases, compute instances, accounts, or virtual private
clouds (VPCs) for each tenant. While these are common forms of
isolation, they are not the only way to isolate tenants. Even
in scenarios where resources are shared—in fact, especially in
environments where resources are shared—there are ways to
achieve isolation. In this shared resource model, isolation
can be a logical construct that is enforced by runtime applied
policies. The key point here is that isolation should not be
equated to having siloed resources.

**Domains may impose specific isolation
requirements** – While there are many approaches to
achieving tenant isolation, the realities of a given domain
might impose constraints that will require a specific flavor
of isolation. For example, some high compliance industries may
require that every tenant have its own database. In these
cases, the shared, policy-based approaches to isolation may
not be adequate.

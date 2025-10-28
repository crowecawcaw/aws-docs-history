# Sourcing and distribution

Your sourcing and distribution strategy defines how you procure and
deploy software and distribute infrastructure as code in a
hub-and-spoke model across your cloud environment. Integration
between sourcing systems, like AWS Marketplace, and your procurement
system helps centralize governance for your software purchasing.
With this integration, you can also use your existing workflows for
procurement approval. AWS Marketplace provides for this integration
using Commerce XML (cXML), an open standard communication protocol.
With this feature, builders can find, buy, and deploy solutions,
where IT administrators and procurement teams streamline approvals
and spend directly from their procurement systems. We recommend that
you further simplify your software procurement to work with your
distribution systems so that software can be provisioned across your
environments. This can be achieved by distributing infrastructure as
code templates via a hub and spoke model.

Infrastructure as code templates are the cornerstone for agility in
the cloud. These templates allow you to rapidly iterate and
provision workloads and environments to meet your evolving customer
needs. In the same manner, a consistent application of governance
controls should be used to help meet ongoing and changing compliance
requirements for internal enterprise standards and controls, as well
as regulatory compliance frameworks. This applies to how you source
software and distribute your templates across your multi-account
strategy. Governance functions should be implemented proactively in
order to verify you scale without introducing workflow bottlenecks.
Having resources preconfigured for compliance (either with internal
or external standards) allows you to reuse and scale your cloud
assets without introducing manual review and reaction processes.

After you have obtained your software, or built your infrastructure
as code templates, you then centrally manage and distribute these
services, applications, resources, and metadata (tags). We recommend
creating and recording these assets into a catalog, and distributing
access to a curated assortment from the catalog in a hub and spoke
manner. Meaning, all templates are stored at a top-level repository,
and then replicated and shared as required in spoke repositories
with permissions granted as required. This helps ensure that not
only have you preconfigured and created immutable infrastructure as
code assets, but that by curating the assortment you are introducing
efficiencies as well for your builder teams. Providing the right
template, preconfigured for governance controls, at the right time,
in the right accounts, helps ensure that your teams can self-service
any provisioning (including updating and shutting down) they require
on an as-needed basis.

For example, you might have a collection of infrastructure as code
templates in your hub catalog that have been preconfigured with
Amazon S3, Amazon EC2, and Amazon RDS. In your member accounts, you
would select the appropriate parameters for each AWS service in such
a way that each team or end user would only see the templates that
they require, with the preconfigured options for each parameter
defined for their specific use. Your tagging strategy should be well
defined and enforced at the Organization level, and a reusable
repository of tag options should be available during the
self-service provisioning of resources from the central catalog.
This will help you achieve consistent governance, while also
enabling users to quickly provision the approved assets with the
right tags included. This self-service model is a core component of
operating efficiently. With the ability to provision resources
pre-configured for compliance, your development teams will be
empowered, and able to move at their own pace or agility.

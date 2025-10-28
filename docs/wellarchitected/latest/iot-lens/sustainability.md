# Sustainability

The sustainability pillar includes the ability to continually
improve sustainability impacts by reducing energy consumption and
increasing efficiency across all components of a workload by
maximizing the benefits from the provisioned resources and
minimizing the total resources required.

The term sustainability encompasses a wide range of factors such as
economic viability, social equity, biodiversity, resilience, and
environmental impact.  We focus specifically on how to design your
IoT solutions to improve sustainability by lowering their
[carbon
footprint](https://css.umich.edu/publications/factsheets/sustainability-indicators/carbon-footprint-factsheet "https://css.umich.edu/publications/factsheets/sustainability-indicators/carbon-footprint-factsheet") while simultaneously reducing operational costs.  

Reducing carbon footprint is a key aspect of mitigating climate
change, which is a pressing global environmental challenge. One way
to achieve this is to use resources in a responsible and efficient
manner, minimize waste and maximize the use of renewable
resources. As described later in this paper, the actions taken to
improve sustainability usually have a positive effect on operational
costs, not just through resource efficiency, but also by optimizing
operational processes.

While IoT solutions span the range from sensors and devices at the
edge to applications in the cloud, this paper focuses largely on
sustainability at the edge. Sustainability of and through the cloud
is covered in the
[Sustainability
Pillar of the AWS Well-Architected Framework](../sustainability-pillar/sustainability-pillar.md "../sustainability-pillar/sustainability-pillar.md").

It is important to recognize that the carbon footprint of an IoT
device is distributed across its entire lifecycle, consisting of the
design and build phase, the operational (in-use) phase, and the
disposal phase.

- The design and build phase deals with design, component
  sourcing, manufacturing, and other supply chain activities. This
  phase usually accounts for most of the carbon footprint
  associated with a device, often referred to as the
  _embodied carbon_.
- The operational phase of the device lifecycle has a significant
  carbon footprint impact as well. 
  [Reaching
  Net-Zero Carbon by 2040: Decarbonizing and Neutralizing the Use
  Phase of Connected Devices](https://sustainability.aboutamazon.com/devices-use-phase-decarbonization.pdf "https://sustainability.aboutamazon.com/devices-use-phase-decarbonization.pdf") shows that this phase accounts
  for 10-15% of the entire lifecycle carbon footprint for
  re-chargeable battery powered devices and 60-80% for plugged-in
  devices.
- The disposal phase of IoT devices refers to the stage when a
  device is no longer needed or usable in operation.

Implementing the best practices outlined here involves trade-offs
between cost, reliability, performance, carbon footprint, and any
current or future regulatory requirements. Your organization should
examine these best practices, both holistically and individually,
and agree on how to best meet your sustainability goals for each use
case.

###### Focus areas

- [Design principles](design-principles-sus.md "design-principles-sus.md")
- [Definitions](definitions-sus.md "definitions-sus.md")
- [Region selection](region-selection.md "region-selection.md")
- [Alignment to demand](alignment-to-demand.md "alignment-to-demand.md")
- [Software and architecture optimization](software-and-architecture-optimization.md "software-and-architecture-optimization.md")
- [Software and architecture – Cloud](software-and-architecture-cloud.md "software-and-architecture-cloud.md")
- [Data management](data-management-sus.md "data-management-sus.md")
- [Hardware and services - Hardware optimization](hardware-and-services-optimization.md "hardware-and-services-optimization.md")
- [Hardware and services - Power management](hardware-and-services-power-management.md "hardware-and-services-power-management.md")
- [Process and culture - User guidance](process-and-culture-user-guidance.md "process-and-culture-user-guidance.md")
- [Key AWS services](key-aws-services-sus.md "key-aws-services-sus.md")
- [Resources](resources-sus.md "resources-sus.md")

# Design principles

The Well-Architected Framework identifies a set of general design principles to
facilitate superior design in the cloud. In addition, the following design principles should
also be considered for designing and operating telco workloads:

- **Organization-wide goals:** Organizations should have
  long-term sustainability goals established based on each workload; types of resources
  being used for infrastructure and planning for growth. Designing workloads keeping in mind
  these goals and what future growth gives individual application owners benchmarks to work
  back from. Telecommunications organizations should keep the following in mind when
  establishing sustainability goals:
- **Center of sustainability:** Creating a Center of
  Sustainability within the organization will create a team and a one-threaded leader that
  can work towards establishing these goals and accelerating achievement of those. They will
  be responsible for aligning workloads to these goals, reducing current carbon footprint by
  exploring innovative technologies and optimizing upon existing infrastructure.
- **Network energy efficiency:** Telecommunications
  Organizations should have guardrails in place to optimize energy consumption of the RAN,
  transport, core network, and IT infrastructure. Organizations should also consider
  developing depreciation schedules for legacy networks that are no longer being utilized
  and that are not energy efficient.
- **Use O-RAN:** With Open RAN, it is possible for telecom
  operators to leverage multiple RAN technologies. This gives telecom operators the
  opportunity to leverage more efficient RAN capabilities from different vendors and
  suppliers. It allows us to deploy new innovations, like miniaturization of radios, at a
  much more rapid scale.
- **Monitoring and observability:** Progressing towards
  sustainability goals is difficult without having visibility across the entire network and
  IT infrastructure's carbon emissions. Having a robust monitoring system, which provides a
  single pane of glass on each component's carbon footprint would provide actionable
  insights that drive sustainability plans. Utilize AWS's carbon footprint measurement
  tools which provides customers with tools to measure and report on GHG emissions from
  AWS usage, which complement sustainability frameworks.
- **Renewable energy and green network:** Utilizing renewable
  energy to power telecom networks can go a long way in reducing carbon emissions. For
  example, instead of using diesel generators, operators might consider solar power, wind
  power, lithium-ion batteries, and renewable electricity from a renewable source.
- **Use managed and serverless services:** Enables
  organizations to automatically scale resources based on actual demand while reducing idle
  compute time and maximizing resource utilization. This architectural approach shifts
  compute resources to centralized data centers and leverages cloud efficiencies to
  significantly reduce power consumption and operating costs while maintaining high
  availability for telecom operations. The event-driven nature of serverless computing
  maintains optimal resource allocation by blocking unnecessary resource consumption during
  low traffic periods and automatic scaling during peak demands.
- **Maximize utilization:** Right-sizing compute, storage,
  network infrastructure to support an end-to-end telecom network is key to optimizing its
  footprint. Energy efficient designs to verify high utilization and maximize the energy
  efficiency of the underlying hardware. Two hosts running at 30% utilization are less
  efficient than one host running at 60% due to baseline power consumption per host. At the
  same time, minimize idle resources, processing, and storage to reduce the total energy
  required to power your workload.
- **Anticipate and adopt new, more efficient hardware and software
  offerings:** Support the upstream improvements your partners and suppliers make
  to assist you to reduce the impact of your cloud workloads. Continually monitor and
  evaluate new, more efficient hardware and software offerings. Design for flexibility to
  allow for the rapid adoption of new efficient technologies**.**
- **Retire legacy networks (2G/3G) and migrate customers to more energy
  efficient technologies such as 5G:** Dated hardware and legacy networks lead to
  more energy consumption and higher carbon footprint. Moving away from them and towards
  newer technologies can assist CSPs to be more energy efficient.

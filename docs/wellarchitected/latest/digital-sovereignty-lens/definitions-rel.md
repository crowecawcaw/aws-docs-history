# Definitions

The following are reliability-specific definitions:

- **Cross-region replication:** An automatic, asynchronous
  copying of data from a source location in one geographic region to a destination in a
  different geographic region.
- **Regulatory boundaries:** Legal, geographic, or
  jurisdictional limits imposed by laws, regulations, and compliance requirements that
  dictate where data can be stored, how it must be processed, and who can access it.
- **Jurisdictional boundaries:** Legal and geographic limits
  that define where specific laws, regulations, and governmental authority apply. They
  determine which legal system has the power to enforce rules, adjudicate disputes, and
  govern activities within a particular territory.
- **Sovereign boundaries:** The geographic borders that define
  the territorial limits of a nation-state's supreme authority and legal control, within
  which that government has exclusive power to create and enforce laws without external
  interference. Delineate the physical territory over which a nation exercises complete and
  independent governmental authority, including control over people, resources, data, and
  legal matters within those borders.
- **Regional isolation:** the practice of keeping data,
  systems, and resources physically and logically separated within specific geographic
  regions to verify that they operate independently without cross-region dependencies. This
  approach blocks failures, security breaches, or regulatory violations in one region from
  affecting operations in other regions.
- **ICT Business Continuity Management (BCM):** Specific
  compliance area under sovereignty regulations (such as EU DORA Chapter IV) requiring
  documented resilience and recovery capabilities that respect jurisdictional boundaries.
- **Data replication:** Copying data between sites while
  respecting jurisdictional boundaries to keep replicas within approved regions. Must be
  carefully designed to avoid inadvertent cross-border transfers.
- **Data perimeters:** The technical implementation of
  sovereignty requirements that block unauthorized cross-border data flows that define and
  enforce where data can reside, how it can be accessed, and who can interact with it based
  on attributes like location, identity, network, and resource type. They establish explicit
  controls to block unauthorized data access, movement, or processing outside defined
  geographic, organizational, or regulatory boundaries.
- **Sovereign-compliant failure prevention:** Resilience
  strategies designed to maintain compliance during incidents by keeping data and operations
  within approved boundaries during failures. Integrates sovereignty requirements into
  resilience planning from the design phase.
- **Hub-and-spoke (in sovereignty context):** Architectural
  pattern with centralized core services (hub) and regionally-isolated implementations
  (spokes) that balances global consistency with local sovereignty requirements while
  maintaining compliance boundaries. Network architecture where a central hub location
  manages and controls resources, with multiple spoke regions connecting to it for services,
  creating potential sovereignty issues when data must transit through the hub's
  jurisdiction.
- **Fault isolation:** The practice of containing failures
  within defined boundaries to block them from cascading across a system. It uses techniques
  like bulkheads, cell-based architectures, and failure domains to verify that when one
  component fails, the impact is limited and other parts of the system continue operating
  normally. This approach minimizes blast radius and improves overall system resilience by
  treating failures as inevitable and designing explicit containment strategies.
- **Foreign:** Belonging to, located in, or coming from another
  country or external source.

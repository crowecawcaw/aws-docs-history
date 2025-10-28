# ADVREL01-BP02 Architect your system with appropriate recovery objectives

Avoid over- or under-architecting your services by
[working
backwards](https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes "https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes") from your services' recovery objectives, striking
a balance with adjacent pillars such as cost optimization and
operational excellence. KPIs established in the operational
excellence pillar should inform approaches to reliability.

## Implementation guidance

Identify critical parts of the architecture and individually
confirm their reliability and recovery point and time objectives
(RPO and RTO). For example, with real-time bidding (RTB),
delivery services have increased RPO and RTO requirements as
compared to creative services. On close inspection, certain
architectures also have variable availability and recovery
requirements, operating on a spectrum from multiple layers of
redundancy to entirely non-redundant. Advertising customers
accept ranges from milliseconds to hours as appropriate
recovery. For example, enrichment and auction layers often have
the most stringent requirements, while analytics or as necessary
reporting can see reduced requirements. 

## Key AWS services

- [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/ "https://aws.amazon.com/resilience-hub/")

## Resources

- [Establishing
  RPO and RTO Targets for Cloud Applications](\aws.amazon.md "\\aws.amazon.md")

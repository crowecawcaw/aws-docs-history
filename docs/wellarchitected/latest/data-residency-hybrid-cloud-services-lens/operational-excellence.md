# Operational excellence

Operational excellence includes the ability to support development
and run workloads effectively, gain insight into their operations,
and to continuously improve supporting processes and procedures to
deliver business value. This section provides an overview of design
principles, questions, best practices, and guidance on
implementation. For more information, see
[Operational
Excellence Pillar whitepaper](../operational-excellence-pillar/welcome.md "../operational-excellence-pillar/welcome.md").

## Definitions

This whitepaper covers operational excellence in the cloud, describing best practices in the following areas:

- Organization
- Prepare
- Operate
- Evolve

## Design principles

- **Local Zones:** Operational
  design principles for Local Zones should focus on seamless
  integration with cloud-based monitoring and management tools,
  same as for deployments in an AWS Region. Implement robust
  incident response plans tailored to the specific metropolitan
  area, ensuring continuous service availability and
  [regulatory
  compliance](https://aws.amazon.com/blogs/compute/best-practices-for-managing-data-residency-in-aws-local-zones-using-landing-zone-controls/ "https://aws.amazon.com/blogs/compute/best-practices-for-managing-data-residency-in-aws-local-zones-using-landing-zone-controls/"). For more information, see
  [Connectivity
  options for Local Zones](../../../local-zones/latest/ug/local-zones-connectivity.md "../../../local-zones/latest/ug/local-zones-connectivity.md").
- **Outposts:** Operational
  design principles for Outposts should focus on automating
  deployment and configuration processes and aligning with
  existing on-premises operational procedures and governance
  frameworks. Implement centralized monitoring, logging, and
  incident response mechanisms to maintain consistent
  compliance, as AWS Outposts requires additional accountability
  within the shared responsibility model.

# DRHCOPS08-BP01 Build feedback loops to adapt to changing data residency requirements

Data residency requirements can change over time. As AWS expands
its Local Zones and Region footprint, new options may become
available that allow you to move your data closer to AWS-managed
infrastructure while still meeting your residency needs.

For example, if a new Local Zone launches in a location that meets
your data residency requirements, you can move data that was
previously hosted on Outposts into the Local Zone, which is an
AWS-managed environment. Similarly, if a new AWS Region launches
in a country or region where you previously had to use a Local
Zone or Outposts to meet data residency needs, you can move that
data into the new AWS Region.

**Desired outcome:** Establish
feedback loops to continuously adapt to evolving data residency
requirements for Outposts and Local Zones.

**Benefits of establishing this best
practice:** Enables proactive compliance with data
sovereignty and localization mandates by facilitating timely
adjustments to deployments.

**Level of risk exposed if this best
practice is not established:** Low

## Implementation guidance

Regularly checking for updates on new Local Zone and AWS Region
launches, and assessing how they align with your data residency
requirements, can help you optimize your architecture and
potentially move workloads closer to AWS-managed infrastructure
while still complying with your data residency needs.

# GENREL05-BP03 Verify that agent capabilities are available

across all regions of availability

Agents require supporting infrastructure to service requests from
foundation models. Using agents across a region of availability
requires the supporting infrastructure to be available in that
region.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by verifying that agents have access to the
appropriate supporting infrastructure such as APIs or functions, so
they may service a wider region of availability.

**Benefits of establishing this best
practice:**
[Scale
horizontally to increase aggregate workload availability](../framework/rel-dp.md "../framework/rel-dp.md") -
Data replication across a region of availability horizontally scales
data access infrastructure, enabling foundation models to
consistently service inference requests across a region of
availability.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Agents for Amazon Bedrock can be made available across regions, so
long as the models and supporting infrastructure exist in the
desired regions. Amazon Bedrock Agents make API calls on behalf of
a user. Once deployed to a new region, these agents must have
access to the same or regionally-equivalent API. Consider
deploying your APIs across multiple regions behind a CloudFront
distribution with latency-based routing. When possible, leverage
Amazon Route 53 with latency-based routing to direct traffic
within your VPC (and on the Amazon backbone) rather than taking
private traffic public to route to an internal service. If your
agent is not making calls to a foundation model using a
cross-region inference profile, be sure to configure model access
in all required regions.

### Implementation steps

1. Deploy supporting agent infrastructure in the primary region
   or Availability Zone.
2. Deploy supporting agent infrastructure in the secondary
   region or Availability Zone.
3. Configure latency-based routing or a similar routing
   protocol which will distribute your load accordingly.

## Resources

**Related practices:**

- [REL04-BP01](../reliability-pillar/rel_prevent_interaction_failure_identify.md "../reliability-pillar/rel_prevent_interaction_failure_identify.md")
- [REL07-BP01](../reliability-pillar/rel_adapt_to_changes_autoscale_adapt.md "../reliability-pillar/rel_adapt_to_changes_autoscale_adapt.md")
- [REL10-BP01](../reliability-pillar/rel_fault_isolation_multiaz_region_system.md "../reliability-pillar/rel_fault_isolation_multiaz_region_system.md")

**Related guides, videos, and documentation:**

- [Latency-based
  routing](../../../Route%C2%A053/latest/DeveloperGuide/routing-policy-latency.md "../../../Route%C2%A053/latest/DeveloperGuide/routing-policy-latency.md")

**Related examples:**

- [Using
  latency-based routing with Amazon CloudFront for a
  multi-Region active-active architecture](https://aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html/ "https://aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html/")

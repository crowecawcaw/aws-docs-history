# GENREL05-BP02 Replicate embedding data across all regions of

availability

Inference to a foundation model may be available over a local availability region, or could
be a large region of availability. Make sure your data is available across all regions of
availability to adequately service inference requests.

**Desired outcome:** When implemented, this best practice improves
the reliability of your generative AI workload by validating that models have access to the
appropriate data to service inference requests across an entire Region of availability.

**Benefits of establishing this best
practice:**
[Scale
horizontally to increase aggregate workload availability](../framework/rel-dp.md "../framework/rel-dp.md") -
Data replication across a region of availability enables horizontal
scaling of the data access infrastructure and supports consistent
serving of inference requests.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Validate that data sources for your generative AI workloads are
replicated and made available across all of the designated regions
of availability. Configure data replication pipelines which
replicate data creation, updates, and deletions across data
sources, providing a consistent experience for users. Customers
should leverage a durable storage layer which is available across
all desired regions.

Amazon S3 is a common choice since it is a durable, scalable, and
reliable storage layer which integrates simply with several data
analytics and vector storage solutions. A modern data architecture
backed by Amazon S3 is a recommended choice for multi-region data
availability at scale. Consider using Amazon S3 or a similar
storage layer. Develop data pipelines to distribute data across
regions. Amazon S3's bucket replication capability is a managed
version of a data pipeline which replicates data across regions.

Alternatively, data pipelines can be developed and orchestrated
manually using Amazon Glue. These data pipelines should run
frequently enough to satisfy data availability requirements across
regions. Once replicated, verify that the data is processed by a
replicated vector storage layer.

### Implementation steps

1. Create two OpenSearch clusters across two regions, where one
   is a leader and one is a follower.
2. Create a request for an outbound connection from the
   follower to the leader.
3. Accept the inbound request from the leader.
4. Modify the leader security configuration to facilitated
   cluster replication.
5. Create an index for replication on the leader cluster.
6. Run cluster replication from the follower cluster.
7. Index documents on the leader cluster.
8. Test document replication on the follower cluster.

## Resources

**Related practices:**

- [REL04-BP01](../reliability-pillar/rel_prevent_interaction_failure_identify.md "../reliability-pillar/rel_prevent_interaction_failure_identify.md")
- [REL07-BP01](../reliability-pillar/rel_adapt_to_changes_autoscale_adapt.md "../reliability-pillar/rel_adapt_to_changes_autoscale_adapt.md")
- [REL10-BP01](../reliability-pillar/rel_fault_isolation_multiaz_region_system.md "../reliability-pillar/rel_fault_isolation_multiaz_region_system.md")

**Related guides, videos, and documentation:**

- [Supported
  Regions and Models for inference profiles](../../../bedrock/latest/userguide/inference-profiles-support.md "../../../bedrock/latest/userguide/inference-profiles-support.md")

**Related examples:**

- [Ensure
  availability of your data using cross-cluster replication with
  Amazon OpenSearch Service](https://aws.amazon.com/blogs/big-data/ensure-availability-of-your-data-using-cross-cluster-replication-with-amazon-opensearch-service/ "https://aws.amazon.com/blogs/big-data/ensure-availability-of-your-data-using-cross-cluster-replication-with-amazon-opensearch-service/")

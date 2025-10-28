# GENREL05-BP01 Load-balance inference requests across all regions of

availability

Inference to a foundation model may be available over a local or
large area of availability. Verify that you have resources available
across that area to service inference requests reliably regardless
of where they are coming from.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by creating a highly available environment
for serving inference requests.

**Benefits of establishing this best
practice:**
[Scale
horizontally to increase aggregate workload availability](../framework/rel-dp.md "../framework/rel-dp.md") -
Load-balanced inference requests across horizontally scaled
infrastructure enable inference requests to be serviced evenly
across a region of availability.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Load-balance model requests across multiple Availability Zones by
creating a highly available environment for serving inference
requests. Consider using managed or serverless options for model
hosting. For example, Amazon Bedrock hosts several
industry-leading first and third-party models in a serverless
paradigm. This capability abstracts the need to load-balance model
inference requests across multiple Availability Zones.

Consider using managed or serverless solutions for supporting
infrastructure like vector search databases or agentic compute.
Amazon OpenSearch Service Serverless and AWS Lambda functions can be
deployed across multiple Availability Zones, which provides a high
degree of reliability for supporting infrastructure.

### Implementation steps

1. For multi-AZ inference, verify that model endpoint
   availability exists across each availability zone.
   - In Amazon Bedrock, access model endpoints through the
     subnets corresponding to the Availability Zones which
     support inference.
   - For self-hosted models, such as an Amazon SageMaker AI
     Inference Endpoint, consider deploying highly-available
     infrastructure across multiple Availability Zones, with
     network load balancing that routes requests
     appropriately.
   - Alternatively, consider using Amazon Bedrock's Custom
     Model Import feature to offload model hosting
     considerations to the managed service.

2. For multi-Region inference, navigate to the model catalog in
   Amazon Bedrock and choose Cross-Region Inference.
3. Select the appropriate inference profile for your inference
   requirements.
4. Validate each Region listed in the inference profile has
   reliable access to the same supporting infrastructure such
   as vector databases or agent APIs.
5. Consult a network specialist for multi-Region deployments of self-hosted models
   that suit your architecture requirements. Consider using Amazon VPC Lattice, Amazon Transit
   Gateway, or other cross-Region networking solutions to facilitate cross-region network
   traffic for model inference.

## Resources

**Related practices:**

- [REL04-BP01](../reliability-pillar/rel_prevent_interaction_failure_identify.md "../reliability-pillar/rel_prevent_interaction_failure_identify.md")
- [REL10-BP01](../reliability-pillar/rel_fault_isolation_multiaz_region_system.md "../reliability-pillar/rel_fault_isolation_multiaz_region_system.md")

**Related guides, videos, and documentation:**

- [Supported Regions and models for inference profiles](../../../bedrock/latest/userguide/inference-profiles-support.md "../../../bedrock/latest/userguide/inference-profiles-support.md")

**Related examples:**

- [Getting Started with cross-Region inference in Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/getting-started-with-cross-region-inference-in-amazon-bedrock/ "https://aws.amazon.com/blogs/machine-learning/getting-started-with-cross-region-inference-in-amazon-bedrock/")

# LSPERF02-BP01 Data-aware storage

tiering

Implement intelligent storage tiering strategies that align storage
performance characteristics with data access patterns. Place
frequently accessed reference data on high-performance tiers, move
aging research data to cost-optimized tiers, and archive completed
study data to deep storage, while maintaining appropriate encryption
and access controls based on data sensitivity classification.

**Desired outcome:** Implement a
comprehensive, data-driven storage management system that
automatically places data on the most appropriate storage tier based
on access patterns, age, and sensitivity classification.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Working backward from your research data needs, design an
intelligent storage architecture that aligns with actual access
patterns to optimize both performance and cost.

Start by classifying data based on access frequency and
sensitivity. Deploy high-performance options like Amazon EFS with
provisioned throughput or Amazon FSx for Lustre for frequently
accessed data requiring low-latency retrieval.

As access patterns decrease, implement automated lifecycle
policies that transition data to cost-optimized tiers such as S3
Standard-Infrequent Access or S3 Intelligent-Tiering.

For rarely accessed audit data, use S3 Glacier Deep Archive to
minimize costs while maintaining accessibility.

Maintain consistent encryption and access controls across each
tier, with appropriate keys and permissions based on sensitivity
classification. Use S3 Analytics to continuously monitor access
patterns and refine tiering policies, while implementing object
tagging to preserve context across tiers.

For domain-specific optimization, consider purpose-built solutions
like AWS HealthOmics, AWS HealthImaging, and AWS HealthLake.

### Implementation steps

1. Configure S3 Intelligent-Tiering for scientific dataset
   storage.
2. Store sensitive data in encrypted Amazon RDS instances.
3. Implement Amazon S3 Lifecycle policies for data archival.
4. Implement AWS Lambda for auto scaling data processing.
5. Consider purpose-built storage such as HealthLake,
   HealthOmics, and HealthImaging.

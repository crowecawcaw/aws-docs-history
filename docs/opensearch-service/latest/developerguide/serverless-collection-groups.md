# Amazon OpenSearch Serverless collection groups

_Collection groups_ in Amazon OpenSearch Serverless organize multiple
collections and enable compute resource sharing across collections with different KMS keys.
This shared compute model reduces costs by eliminating the need for separate OpenSearch
Compute Units (OCUs) for each KMS key.

Each OpenSearch Serverless collection you create is protected with encryption of data at rest using AWS KMS
to store and manage your encryption keys. Collections within the same collection group share
compute resources and OCU memory space, even when they use different KMS keys for
encryption.

Collection groups provide isolation for security and performance requirements. You can
group collections with the same KMS key into a single collection group for security
isolation, or combine collections with different KMS keys in the same group for cost
optimization. This flexibility lets you balance security requirements with resource
efficiency.

When you add a collection to a collection group, OpenSearch Serverless assigns it to the group's shared
compute resources. The system automatically manages the distribution of workloads across
these resources while maintaining security by encrypting each collection's data with its
designated KMS key. Access controls continue to apply at the collection level, and the
shared compute resources access multiple KMS keys as needed to serve the collections in the
group.

You control resource allocation by setting minimum and maximum OCU limits at the
collection group level. These limits apply to all collections in the group and help you
manage costs while ensuring consistent performance.

By default, there is a service quota (limit) for the number of collections in a collection
group, the number of indexes in a collection, and the number of OCUs in a collection group.
For more information, see [OpenSearch Serverless quotas](limits.md "limits.md").

## Key concepts

Collection group

An AWS resource that acts as a container for one or more collections.
Each collection group has a unique identifier and can have its own capacity
limits and configuration settings.

Shared compute

Collections within the same collection group share the same set of OCUs,
regardless of the KMS keys they use. This sharing reduces costs by
eliminating the need for separate compute resources for each KMS key.

Capacity limits

You can set minimum and maximum OCU limits for both indexing and search
operations at the collection group level. These limits help control costs
and ensure consistent performance.

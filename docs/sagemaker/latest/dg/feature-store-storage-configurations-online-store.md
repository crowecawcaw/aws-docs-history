# Online store

The online store is a low-latency, high-availability data store that provides
real-time lookup of features. It is typically used for machine learning (ML) model
serving. You can chose between the standard online store (`Standard`) or an
in-memory tier online store (`InMemory`), at the point when you create a
feature group. In this way, you can select the storage type that best matches the read
and write patterns for a particular application, while considering performance and cost.
For more details about pricing, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

The online store contains the following `StorageType` options. For more
information about the online store contents, see [`OnlineStoreConfig`](../APIReference/API_OnlineStoreConfig.md "../APIReference/API_OnlineStoreConfig.md").

## Standard tier storage type

The `Standard` tier is a managed low-latency data store for online
store feature groups. It provides fast data retrieval for ML model service for your
applications. `Standard` is the default storage type.

## In-memory tier storage type

The `InMemory` tier is a managed data store for online store feature
groups that supports very low-latency retrieval. It provides large-scale real-time
data retrieval for ML model serving used for high throughput applications. The
`InMemory` tier is powered by Amazon ElastiCache (Redis OSS). For more information, see
[What is Amazon ElastiCache (Redis OSS)?](../../../AmazonElastiCache/latest/red-ug/WhatIs.md "../../../AmazonElastiCache/latest/red-ug/WhatIs.md").

The online store `InMemory` tier supports collection types, namely
list, set, and vector. For more information about the `InMemory`
collection types, see [Collection types](feature-store-collection-types.md "feature-store-collection-types.md").

Feature Store provides low latency read and writes to the online store. The application
latency is primarily made up of two primary components: infrastructure or network
latency and Feature Store API latency. Reduction of network latency helps with getting the
lowest latency reads and writes to Feature Store. You can reduce the network latency to Feature Store
by deploying AWS PrivateLink to Feature Store Runtime endpoint. With AWS PrivateLink, you can
privately access all Feature Store Runtime API operations from your Amazon Virtual Private Cloud (VPC) in a
scalable manner by using interface VPC endpoints. An AWS PrivateLink deployment with
the `privateDNSEnabled` option set as true:

- It keeps all Feature Store read/write traffic within your VPC.
- It keeps traffic in the same AZ as the client that originated it when
  using Feature Store. This avoids the “hops” between AZs reducing the network
  latency.

Follow the steps in [Access an AWS
service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") to setup AWS PrivateLink to Feature Store.
The service name for Feature Store Runtime in AWS PrivateLink is
`com.amazonaws.region.sagemaker.featurestore-runtime`.

The `InMemory` tier online store scales automatically based about
storage usage and requests. The automated scaling can take a few minutes to adapt to
a new usage pattern if it changes rapidly. During automated scaling:

- Write operations to the feature group may receive throttling errors. You
  should retry your requests a few minutes later.
- Read operations to the feature group may receive throttling errors.
  Standard retry strategies are suitable in this case.
- Read operations may see elevated latency.

The default `InMemory` tier feature group maximum size is 50
GiB.

Note that the `InMemory` tier currently supports online feature groups
only, not online+offline feature groups, so there is not replication between online
and offline stores for the `InMemory` tier. Also, the
`InMemory` tier does not currently support customer managed
KMS keys.



# Online store
<a name="feature-store-storage-configurations-online-store"></a>

The online store is a low-latency, high-availability data store that provides real-time lookup of features. It is typically used for machine learning (ML) model serving. When you create a feature group, choose an online store type: the standard online store (`Standard`), the standard V2 online store (`Standard_V2`), or an in-memory tier online store (`InMemory`). In this way, you can select the storage type that best matches the read and write patterns for a particular application, while considering performance and cost. For more details about pricing, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/).

The online store contains the following `StorageType` options. For more information about the online store contents, see [`OnlineStoreConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfig.html). 

## Standard tier storage type
<a name="feature-store-storage-configurations-online-store-standard-tier"></a>

The `Standard` tier is a managed low-latency data store for online store feature groups. It provides fast data retrieval for ML model service for your applications. `Standard` is the default storage type.

## Standard V2 tier storage type
<a name="feature-store-storage-configurations-online-store-standard-v2-tier"></a>

The `Standard_V2` tier is a managed low-latency data store for online store feature groups that supports partial updates to individual features using the [UpdateRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_UpdateRecord.html) operation. Unlike the `Standard` tier, `Standard_V2` allows you to update specific feature values in a record without rewriting the entire record.

This unlocks several benefits for feature groups that change frequently:
+ **Update features in a single call** – Skip the read-modify-write pattern. Call [UpdateRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_UpdateRecord.html) with just the features you want to change, and Feature Store preserves the rest.
+ **Lower write cost and latency for feature-level updates** – Write only the features that changed instead of the full record. For wide records where only a few features update often (for example, `last_login` or a running `click_count`), this avoids sending and rewriting unchanged data.
+ **Safe concurrent updates** – Use the `EventTime` of each update to detect and reject out-of-order writes, so a slow or stale update can't overwrite newer feature values.

Choose `Standard_V2` at feature group creation time when your workload updates specific features frequently and you want efficient, partial writes. To create a new `Standard_V2` feature group, call [CreateFeatureGroup](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateFeatureGroup.html) and set the `StorageType` in `OnlineStoreConfig` to `Standard_V2`.

### Migrate a `Standard` feature group to Standard V2
<a name="feature-store-storage-configurations-online-store-standard-v2-migrate"></a>

Already have a `Standard` feature group? You can migrate it to Standard V2 in place, without recreating the feature group or reingesting your data. To migrate, call the [UpdateFeatureGroup](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateFeatureGroup.html) operation with the following:
+ Set `FeatureGroupName` to the name or Amazon Resource Name (ARN) of the feature group you want to migrate.
+ In the `OnlineStoreConfig` object, set the `StorageType` to `Standard_V2`.

The following AWS Command Line Interface example migrates a feature group named `my-feature-group` to Standard V2:

```
aws sagemaker update-feature-group \
    --feature-group-name my-feature-group \
    --online-store-config '{"StorageType": "Standard_V2"}'
```

After the migration completes, it takes several minutes for the [UpdateRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_UpdateRecord.html) operation to become available on the feature group. Once it is enabled, you can use `UpdateRecord` to update individual features in the feature group's records.

**Important**  
Migration from `Standard` to Standard V2 is a one-way operation and cannot be reversed.

## In-memory tier storage type
<a name="feature-store-storage-configurations-online-store-in-memory-tier"></a>

The `InMemory` tier is a managed data store for online store feature groups that supports very low-latency retrieval. It provides large-scale real-time data retrieval for ML model serving used for high throughput applications. The `InMemory` tier is powered by Amazon ElastiCache (Redis OSS). For more information, see [What is Amazon ElastiCache (Redis OSS)?](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html).

The online store `InMemory` tier supports collection types, namely list, set, and vector. For more information about the `InMemory` collection types, see [Collection types](feature-store-collection-types.md).

Feature Store provides low latency read and writes to the online store. The application latency is primarily made up of two primary components: infrastructure or network latency and Feature Store API latency. Reduction of network latency helps with getting the lowest latency reads and writes to Feature Store. You can reduce the network latency to Feature Store by deploying AWS PrivateLink to Feature Store Runtime endpoint. With AWS PrivateLink, you can privately access all Feature Store Runtime API operations from your Amazon Virtual Private Cloud (VPC) in a scalable manner by using interface VPC endpoints. An AWS PrivateLink deployment with the `privateDNSEnabled` option set as true:
+ It keeps all Feature Store read/write traffic within your VPC.
+ It keeps traffic in the same AZ as the client that originated it when using Feature Store. This avoids the “hops” between AZs reducing the network latency.

Follow the steps in [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) to setup AWS PrivateLink to Feature Store. The service name for Feature Store Runtime in AWS PrivateLink is `com.amazonaws.region.sagemaker.featurestore-runtime`.

The `InMemory` tier online store scales automatically based about storage usage and requests. The automated scaling can take a few minutes to adapt to a new usage pattern if it changes rapidly. During automated scaling:
+ Write operations to the feature group may receive throttling errors. You should retry your requests a few minutes later.
+ Read operations to the feature group may receive throttling errors. Standard retry strategies are suitable in this case.
+ Read operations may see elevated latency.

The default `InMemory` tier feature group maximum size is 50 GiB.

Note that the `InMemory` tier currently supports online feature groups only, not online\+offline feature groups, so there is not replication between online and offline stores for the `InMemory` tier. Also, the `InMemory` tier does not currently support customer managed KMS keys.
# Feature Store storage configurations

Amazon SageMaker Feature Store consists of an online store and an offline store. The online store enables
real-time lookup of features for inference, while the offline store contains historical data
for model training and batch inference. When creating a feature group, you have the option
of enabling either the online store, offline store, or both. When you enable both, they sync
to avoid discrepancies between training and serving data. For more information about the
online and offline stores and other Feature Store concepts, see [Feature Store concepts](feature-store-concepts.md "feature-store-concepts.md").

The following topics discuss online store storage types and offline store table formats.

###### Topics

- [Online store](feature-store-storage-configurations-online-store.md "feature-store-storage-configurations-online-store.md")
- [Offline
  store](feature-store-storage-configurations-offline-store.md "feature-store-storage-configurations-offline-store.md")
- [Throughput modes](feature-store-throughput-mode.md "feature-store-throughput-mode.md")

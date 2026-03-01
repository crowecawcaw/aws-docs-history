# Versioning, conflict detection, and sync operations for DynamoDB data sources in AWS AppSync

AWS AppSync's advanced data management capabilities for DynamoDB leverages three key features:
versioned data sources, conflict detection and resolution, and sync operations. These tools
enable robust, scalable applications that efficiently handle concurrent data modifications and
synchronization in distributed environments.

Versioned data sources form the foundation of AWS AppSync's data management system. This
feature automatically enhances DynamoDB items with versioning metadata, records changes made by
AWS AppSync mutations to a Delta table, and maintains "tombstones" for deleted items. Developers
can configure retention periods for deleted items and change logs, optimizing storage while
ensuring data consistency. Versioned data sources streamline the implementation of conflict
detection and sync operations, providing a solid base for advanced data handling.

Conflict detection and resolution mechanisms safeguard data integrity when concurrent
writes occur. AWS AppSync offers three strategies: Optimistic Concurrency, Automerge, and
Lambda-based resolution. Optimistic Concurrency rejects conflicting mutations, allowing clients
to retry with updated data. Automerge automatically resolves conflicts based on data types,
merging lists, performing set unions, and preserving existing scalar values. Lambda-based
resolution enables custom logic for complex conflict scenarios. These options give developers
flexibility in handling data conflicts, ensuring consistency across distributed systems.

Sync operations enable efficient data retrieval and updates in client applications. This
feature allows clients to fetch all results from a DynamoDB table and subsequently retrieve only
data altered since their last query. AWS AppSync determines whether to access the Base table or
Delta table based on the provided sync token, optimizing performance and reducing data
transfer.

###### Topics

- [Versioning DynamoDB data sources](versioned-data-sources.md "versioned-data-sources.md")
- [Conflict detection and resolution](conflict-detection-and-resolution.md "conflict-detection-and-resolution.md")
- [Using DynamoDB sync operations on versioned data sources](aws-appsync-conflict-detection-and-sync-sync-operations.md "aws-appsync-conflict-detection-and-sync-sync-operations.md")

# KCL concepts

This section explains the core concepts and interactions of Kinesis Client Library
(KCL). These concepts are fundamental to developing and managing
KCL consumer applications.

- **KCL consumer application** – a custom-built
  application designed to read and process records from Kinesis data streams using
  the Kinesis Client Library.
- **Worker** – KCL consumer applications
  are typically distributed, with one or more workers running simultaneously.
  KCL coordinates workers to consume data from the stream in a
  distributed manner and balances the load evenly across multiple workers.
- **Scheduler** – a high-level class that a
  KCL worker uses to start processing data. Each KCL worker has
  one scheduler. The scheduler initializes and oversees various tasks, including
  syncing shard information from Kinesis data streams, tracking shard assignments
  among workers, and processing data from the stream based on the assigned shards
  to the worker. Scheduler can take various configurations that affect the
  scheduler's behavior, such as the name of the stream to process and AWS
  credentials. Scheduler initiates the delivery of data records from the stream to
  the record processors.
- **Record processor** – defines the logic for how
  your KCL consumer application processes the data it receives from the
  data streams. You must implement your own custom data processing logic in the
  record processor. A KCL worker instantiates a scheduler. The scheduler
  then instantiates one record processor for every shard to which it holds a
  lease. A worker can run multiple record processors.
- **Lease** – defines the assignment between a
  worker and a shard. KCL consumer applications use leases to distribute
  data record processing across multiple workers. Each shard is bound to only one
  worker by a lease at any given time and each worker can hold one or more leases
  simultaneously. When a worker stops holding a lease due to stopping or failing,
  KCL assigns another worker to take the lease. To learn more about the
  lease, see [Github documentation: Lease Lifecycle](https://github.com/awslabs/amazon-kinesis-client/blob/master/docs/lease-lifecycle.md#lease-lifecycle "https://github.com/awslabs/amazon-kinesis-client/blob/master/docs/lease-lifecycle.md#lease-lifecycle").
- **Lease table** – is a unique Amazon DynamoDB table
  used to track all leases for the KCL consumer application. Each
  KCL consumer application creates its own lease table. The lease table
  is used to maintain state across all workers to coordinate data processing. For
  more information, see [DynamoDB metadata tables and load balancing in
  KCL](kcl-dynamoDB.md "kcl-dynamoDB.md").
- **Checkpointing** – is the process of
  persistently storing the position of the last successfully processed record in a
  shard. KCL manages checkpointing to make sure that processing can be
  resumed from the last checkpointed position if a worker fails or the application
  restarts. Checkpoints are stored in the DynamoDB lease table as part of the
  metadata of the lease. This allows workers to continue processing from where the
  previous worker stopped.

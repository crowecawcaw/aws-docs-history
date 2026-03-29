# Using Amazon DocumentDB serverless

Amazon DocumentDB serverless is an on-demand, auto scaling configuration that automates the processes of dynamically adjusting the capacity of your Amazon DocumentDB database based on application demand.
You're charged only for the resources that your clusters consume.
Thus, DocumentDB serverless can help you to stay within budget and avoid paying for computer resources that you don't use.

This type of automation is especially valuable for environments with highly variable and unpredictable workloads, such as multitenant databases, distributed databases, and development and test systems.

###### Topics

- [Serverless use cases](#docdb-serverless-use-cases "#docdb-serverless-use-cases")
- [Advantages of Amazon DocumentDB serverless](#docdb-serverless-advantages "#docdb-serverless-advantages")
- [How serverless works](docdb-serverless-how-it-works.md "docdb-serverless-how-it-works.md")
- [Serverless requirements and limitations](docdb-serverless-limitations.md "docdb-serverless-limitations.md")
- [Creating a cluster that uses serverless](docdb-serverless-create-cluster.md "docdb-serverless-create-cluster.md")
- [Migrating to serverless](docdb-serverless-migrating.md "docdb-serverless-migrating.md")
- [Managing serverless](docdb-serverless-managing.md "docdb-serverless-managing.md")
- [Serverless instance limits](docdb-serverless-instance-limits.md "docdb-serverless-instance-limits.md")
- [Serverless scaling configuration](docdb-serverless-scaling-config.md "docdb-serverless-scaling-config.md")
- [Monitoring serverless](docdb-serverless-monitoring.md "docdb-serverless-monitoring.md")

## DocumentDB serverless use cases

Both Amazon DocumentDB provisioned clusters and DocumentDB serverless support many types of database workloads, from development and testing environments to the most demanding, business-critical applications that require high scale and availability.
But DocumentDB serverless adds another dimension to customer workloads, namely the ability to support websites and applications that have unpredictable workloads.

DocumentDB serverless is especially useful for the following use cases:

- **Variable workloads** — You're running workloads that have sudden and unpredictable increases in activity.
  An example is a traffic site that sees a surge of activity when it starts raining.
  Another is an e-commerce site with increased traffic when you offer sales or special promotions.
  With DocumentDB serverless, your database automatically scales capacity to meet the needs of the application's peak load and scales back down when the surge of activity is over.
  With DocumentDB serverless, you no longer need to provision for peak or average capacity.
  You can specify an upper capacity limit to handle the worst-case situation, and that capacity isn't used unless it's needed.
  - The granularity of scaling in DocumentDB serverless helps you to match capacity closely to your database's needs.
    For a provisioned cluster, scaling up requires adding a whole new instance.
    DocumentDB serverless can add half a DCU when only a little more capacity is needed.
    It can add 0.5, 1, 1.5, 2, or additional half-DCUs based on the additional capacity needed to handle an increase in workload.
    And it can remove 0.5, 1, 1.5, 2, or additional half-DCUs when the workload decreases and that capacity is no longer needed.

- **Multi-tenant applications** — With DocumentDB serverless, you don't have to individually manage database capacity for each application in your fleet.
  DocumentDB serverless manages individual database capacity for you.
  - You can create a cluster for each tenant.
    That way, you can use features such as cloning and snapshot restore to enhance high availability and disaster recovery as appropriate for each tenant.
  - Each tenant might have specific busy and idle periods depending on the time of day, time of year, promotional events, and so on.
    Each cluster can have a wide capacity range.
    That way, clusters with low activity incur minimal instance charges.
    Any cluster can quickly scale up to handle periods of high activity.

- **New applications** — You're deploying a new application and you're unsure about the instance size you need.
  By using DocumentDB serverless, you can set up a cluster with one or many instances and have the database autoscale to the capacity requirements of your application.
- **Mixed-use applications** — Suppose that you have an online transaction processing (OLTP) application, but you periodically experience spikes in query traffic.
  By specifying promotion tiers for the DocumentDB serverless instances in a cluster, you can configure your cluster so that the reader instances can scale independently of the writer instance to handle the additional load.
  When the usage spike subsides, the reader instances scale back down to match the capacity of the writer instance.
- **Capacity planning** — Suppose that you usually adjust your database capacity, or verify the optimal database capacity for your workload, by modifying the instance classes of all the instances in a cluster.
  With DocumentDB serverless, you can avoid this administrative overhead.
  You can determine the appropriate minimum and maximum capacity by running the workload and checking how much the instances actually scale.
  - You can modify existing instances from provisioned to DocumentDB serverless or from DocumentDB serverless to provisioned.
    You don't need to create a new cluster or a new instance in such cases.

- **Development and testing** — In addition to running your most demanding applications, you can also use DocumentDB serverless for development and testing environments.
  With DocumentDB serverless, you can create instances with a low minimum capacity instead of using burstable db.t\* instance classes.
  You can set the maximum capacity high enough that those instances can still run substantial workloads without running low on memory.
  When the database isn't in use, all of the instances scale down to avoid unnecessary charges.

### Using Amazon DocumentDB serverless for existing provisioned workloads

Suppose that you already have an DocumentDB application running on a provisioned cluster.
You can check how the application would work with DocumentDB serverless by adding one or more DocumentDB serverless instances to the existing cluster as reader instances.
You can check how often the reader instances scale up and down.
You can use the DocumentDB failover mechanism to promote an DocumentDB serverless instance to be the writer and check how it handles the read/write workload.
That way, you can switch over with minimal downtime and without changing the endpoint that your client applications use.
For details on the procedure to convert existing clusters to DocumentDB serverless, see [Migrating to Amazon DocumentDB serverless](docdb-serverless-migrating.md "docdb-serverless-migrating.md").

## Advantages of Amazon DocumentDB serverless

DocumentDB serverless is intended for variable or "spiky" workloads.
With such unpredictable workloads, you might have difficulty planning when to change your database capacity.
You might also have trouble making capacity changes quickly enough using the familiar mechanisms such as adding instances or changing instance classes.
DocumentDB serverless provides the following advantages to help with such use cases:

- **Simpler capacity management than provisioned** — DocumentDB serverless reduces the effort for planning instance sizes and resizing instances as the workload changes.
  It also reduces the effort for maintaining consistent capacity for all the instances in a cluster.

- **Faster and easier scaling during periods of high activity** — DocumentDB serverless scales compute and memory capacity as needed, with no disruption to client transactions or your overall workload.
  The ability to use reader instances with DocumentDB serverless helps you to take advantage of horizontal scaling in addition to vertical scaling.

- **Cost-effective during periods of low activity** — DocumentDB serverless helps you to avoid overprovisioning your instances.
  DocumentDB serverless adds resources in granular increments when instances scale up.
  You pay only for the database resources that you consume.
  DocumentDB serverless resource usage is measured on a per-second basis.
  That way, when a instance scales down, the reduced resource usage is registered right away.

- **Feature parity with provisioned** — You can use all DocumentDB features with DocumentDB serverless.
  For example, with DocumentDB serverless you can use reader instances, AWS Identity and Access Management (IAM) database authentication, and Performance Insights.

In particular, with DocumentDB serverless you can take advantage of the following features from provisioned clusters:

    + **Reader instances** — DocumentDB serverless can take advantage of reader instances to scale horizontally.
     When a cluster contains one or more reader instances, the cluster can fail over immediately in case of problems with the writer instance.
    + **Multi-AZ clusters** — You can distribute the DocumentDB serverless instances of a cluster across multiple Availability Zones (AZs).
     Setting up a Multi-AZ cluster helps to ensure business continuity even in the rare case of issues that affect an entire AZ.

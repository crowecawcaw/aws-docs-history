Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Resilience in Amazon Managed Service for Apache Flink

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated
Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and
operate applications and databases that automatically fail over between Availability Zones without interruption. Availability Zones are more highly
available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, a Managed Service for Apache Flink offers several features to help support your data resiliency and backup needs.

## Disaster recovery

Managed Service for Apache Flink runs in a serverless mode, and takes care of host degradations, Availability Zone availability, and other
infrastructure related issues by performing automatic migration.
Managed Service for Apache Flink achieves this through multiple, redundant mechanisms. Each Managed Service for Apache Flink application
runs in a single-tenant Apache Flink cluster. The Apache Flink cluster is run with the JobMananger
in high availability mode using Zookeeper across multiple availability zones. Managed Service for Apache Flink deploys Apache
Flink using Amazon EKS. Multiple Kubernetes pods are used in Amazon EKS for each AWS region across availability zones.
In the event of a failure, Managed Service for Apache Flink first tries to recover the application within the running Apache Flink
cluster using your application’s checkpoints, if available.

Managed Service for Apache Flink backs up application state using _Checkpoints_ and _Snapshots_:

- _Checkpoints_ are backups of application state that Managed Service for Apache Flink automatically creates periodically and uses to restore from faults.
- _Snapshots_ are backups of application state that you create and restore from manually.

For more information about checkpoints and snapshots, see [Implement fault tolerance](how-fault.md "how-fault.md").

## Versioning

Stored versions of application state are versioned as follows:

- _Checkpoints_ are versioned automatically by the service. If the service uses a checkpoint to restart the application, the latest checkpoint will
  be used.
- _Savepoints_ are versioned using the **SnapshotName** parameter of the
  [CreateApplicationSnapshot](../apiv2/API_CreateApplicationSnapshot.md "../apiv2/API_CreateApplicationSnapshot.md") action.

Managed Service for Apache Flink encrypts data stored in checkpoints and savepoints.

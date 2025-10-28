# Amazon MSK: How it works

Amazon MSK is a fully managed Apache Kafka service that makes it easy to build and run applications that use Apache Kafka to process streaming data. This guide provides information to help developers understand how Amazon MSK works and how to use it effectively in their applications.

At a high level, Amazon MSK provides a fully managed Apache Kafka cluster that is provisioned and operated by AWS. This means that you don't have to worry about provisioning EC2 instances, configuring network settings, managing Kafka brokers, or performing ongoing maintenance tasks. Instead, you can focus on building your application and let Amazon MSK handle the infrastructure. Amazon MSK automatically provisions the necessary compute, storage, and network resources, and provides features like automatic scaling, high availability, and failover to ensure that your Kafka cluster is reliable and highly available. This guide covers the key components of Amazon MSK and how you can use it to build streaming data applications.

## Manage your Provisioned cluster

An Amazon MSK cluster is the primary Amazon MSK resource that you can create in your account. The topics in this section describe how to perform common Amazon MSK operations. For a list of all the operations that you can perform on an MSK cluster, see the following:

- The [AWS Management Console](https://console.aws.amazon.com/msk "https://console.aws.amazon.com/msk")
- The [Amazon MSK API
  Reference](../../1.0/apireference.md "../../1.0/apireference.md")
- The [Amazon MSK CLI Command Reference](../../../cli/latest/reference/kafka/index.md "../../../cli/latest/reference/kafka/index.md")

###### Topics

- [Create an MSK Provisioned cluster](msk-create-cluster.md "msk-create-cluster.md")
- [List Amazon MSK clusters](msk-list-clusters.md "msk-list-clusters.md")
- [Connect to an Amazon MSK Provisioned cluster](client-access.md "client-access.md")
- [Get the bootstrap brokers for an
  Amazon MSK cluster](msk-get-bootstrap-brokers.md "msk-get-bootstrap-brokers.md")
- [Monitor an Amazon MSK Provisioned cluster](monitoring.md "monitoring.md")
- [Update security settings of a Amazon MSK cluster](msk-update-security.md "msk-update-security.md")
- [Expand the number of brokers in an Amazon MSK cluster](msk-update-broker-count.md "msk-update-broker-count.md")
- [Remove a broker from an Amazon MSK cluster](msk-remove-broker.md "msk-remove-broker.md")
- [Provision storage throughput for Standard brokers in a Amazon MSK cluster](msk-provision-throughput.md "msk-provision-throughput.md")
- [Update the Amazon MSK cluster broker size](msk-update-broker-type.md "msk-update-broker-type.md")
- [Use LinkedIn's Cruise Control for Apache Kafka with Amazon MSK](cruise-control.md "cruise-control.md")
- [Update the configuration of an Amazon MSK cluster](msk-update-cluster-config.md "msk-update-cluster-config.md")
- [Reboot a broker for an Amazon MSK cluster](msk-reboot-broker.md "msk-reboot-broker.md")
- [Tag an Amazon MSK cluster](msk-tagging.md "msk-tagging.md")
- [Migrate Kafka workloads to an Amazon MSK cluster](migration.md "migration.md")
- [Delete an Amazon MSK Provisioned cluster](msk-delete-cluster.md "msk-delete-cluster.md")

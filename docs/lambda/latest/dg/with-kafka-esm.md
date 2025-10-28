# Using Lambda with Apache Kafka

Lambda supports [Apache Kafka](https://kafka.apache.org/ "https://kafka.apache.org/") as an
[event source](invocation-eventsourcemapping.md "invocation-eventsourcemapping.md"). Apache Kafka is an open-source event
streaming platform designed to handle high-throughput, real-time data pipelines and streaming applications.
There are two main ways to use Lambda with Apache Kafka:

- [Using Lambda with Amazon MSK](with-msk.md "with-msk.md") – Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a fully-managed service by AWS.
  Amazon MSK helps automate management of your Kafka infrastructure, including provisioning, patching,
  and scaling.
- [Using Lambda with self-managed Apache Kafka](with-kafka.md "with-kafka.md") – In AWS terminology, a self-managed cluster includes
  non-AWS hosted Kafka clusters. For example, you can still use Lambda with a Kafka cluster hosted
  with a non-AWS cloud provider such as [Confluent Cloud](https://www.confluent.io/confluent-cloud/ "https://www.confluent.io/confluent-cloud/") or [Redpanda](https://www.redpanda.com/ "https://www.redpanda.com/").
  When deciding between Amazon MSK and self-managed Apache Kafka, consider your operational needs and control requirements. Amazon MSK
  is a better choice if you want AWS to quickly help you manage a scalable, production-ready Kafka setup
  with minimal operational overhead. It simplifies security, monitoring, and high availability, helping you
  focus on application development rather than infrastructure management. On the other hand, self-managed Apache Kafka is
  better suited for use cases running on non-AWS hosted environments, including on-premises clusters.

###### Topics

- [Using Lambda with Amazon MSK](with-msk.md "with-msk.md")
- [Using Lambda with self-managed Apache Kafka](with-kafka.md "with-kafka.md")
- [Using schema registries with Kafka event sources in Lambda](services-consume-kafka-events.md "services-consume-kafka-events.md")
- [Low latency processing for Kafka event
  sources](with-kafka-low-latency.md "with-kafka-low-latency.md")

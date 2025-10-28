# Express broker configurations

Apache Kafka has hundreds of broker configurations that you can use to tune the performance of your MSK Provisioned cluster. Setting erroneous or sub-optimal values can affect cluster reliability and performance. Express brokers improve the availability and durability of your MSK Provisioned clusters by setting optimal values for critical configurations and protecting them from common misconfiguration. There are three categories of configurations based on read and write access: [read/write (editable)](msk-configuration-express-read-write.md "msk-configuration-express-read-write.md"), [read only](msk-configuration-express-read-only.md "msk-configuration-express-read-only.md"), and non-read/write configurations. Some configurations still use Apache Kafka’s default value for the Apache Kafka version the cluster is running. We mark those as Apache Kafka Default.

###### Topics

- [Custom MSK Express broker configurations (Read/Write access)](msk-configuration-express-read-write.md "msk-configuration-express-read-write.md")
- [Express brokers read-only
  configurations](msk-configuration-express-read-only.md "msk-configuration-express-read-only.md")

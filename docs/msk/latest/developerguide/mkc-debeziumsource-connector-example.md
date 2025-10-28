# Use Debezium source connector

with configuration provider

This example shows how to use the Debezium MySQL connector plugin with a
MySQL-compatible [Amazon Aurora](https://aws.amazon.com/rds/aurora/ "https://aws.amazon.com/rds/aurora/")
database as the source. In this example, we also set up the open-source [AWS Secrets
Manager Config Provider](https://github.com/jcustenborder/kafka-config-provider-aws "https://github.com/jcustenborder/kafka-config-provider-aws") to externalize database credentials in AWS Secrets Manager. To
learn more about configuration providers, see [Tutorial: Externalizing sensitive information using config
providers](msk-connect-config-provider.md "msk-connect-config-provider.md").

###### Important

The Debezium MySQL connector plugin [supports only one task](https://debezium.io/documentation/reference/stable/connectors/mysql.html#mysql-property-tasks-max "https://debezium.io/documentation/reference/stable/connectors/mysql.html#mysql-property-tasks-max") and does not work with autoscaled capacity mode
for Amazon MSK Connect. You should instead use provisioned capacity mode and set
`workerCount` equal to one in your connector configuration. To learn
more about the capacity modes for MSK Connect, see [Understand connector capacity](msk-connect-capacity.md "msk-connect-capacity.md").

For a Debezium connector example with detailed steps, see [Introducing Amazon MSK Connect - Stream Data to and from Your Apache Kafka Clusters Using Managed Connectors](https://aws.amazon.com/blogs/aws/introducing-amazon-msk-connect-stream-data-to-and-from-your-apache-kafka-clusters-using-managed-connectors/ "https://aws.amazon.com/blogs/aws/introducing-amazon-msk-connect-stream-data-to-and-from-your-apache-kafka-clusters-using-managed-connectors/").

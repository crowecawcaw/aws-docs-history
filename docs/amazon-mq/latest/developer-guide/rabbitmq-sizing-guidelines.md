# Amazon MQ for RabbitMQ sizing guidelines

You can choose the broker instance type that best supports your application.
When choosing an instance type, consider factors
that will affect broker performance:

- the number of clients and queues
- the volume of messages sent
- messages kept in memory
- redundant messages

Smaller broker instance types `m7g.medium` are recommended only for testing application performance.
We recommend larger broker instance types `m7g.large` and above or production levels of clients and queues,
high throughput, messages in memory, and redundant messages.

###### Important

You cannot downgrade a broker from an `mq.m5` or `mq.m7g` instance type to an `mq.t3.micro` instance type.

It is important to test your brokers to determine the appropriate instance type and size for
your workload messaging requirements.

Always use the default resource limits on RabbitMQ 4
broker to determine the appropriate instance size for your application according to
Amazon MQ best practices. These default resource limits are based on types `m7g` instance type and quorum queues.

- [Default resource limits for m7g single-instance deployment](rabbitmq-resource-limits-configuration.md#default-values-single-instance "rabbitmq-resource-limits-configuration.md#default-values-single-instance")
- [Default resource limits for m7g cluster deployment](rabbitmq-resource-limits-configuration.md#default-values-cluster-brokers "rabbitmq-resource-limits-configuration.md#default-values-cluster-brokers")

You can increase the value of any limit up to the maximum values as defined by instance type and deployment mode.
However, we strongly recommend you test the broker performance with the increased values before using in production.

- [Maximum resource limits for m7g single-instance deployment](rabbitmq-resource-hard-limit.md#sizing-guidelines-m7g-single-instance "rabbitmq-resource-hard-limit.md#sizing-guidelines-m7g-single-instance")
- [Maximum resource limits for m7g cluster deployment](rabbitmq-resource-hard-limit.md#sizing-guidelines-m7g-cluster "rabbitmq-resource-hard-limit.md#sizing-guidelines-m7g-cluster")
- [Maximum resource limits for m5 single-instance deployment](rabbitmq-resource-hard-limit.md#sizing-guidelines-single-instance "rabbitmq-resource-hard-limit.md#sizing-guidelines-single-instance")
- [Maximum resource limits for m5 cluster deployment](sizing-guidelines-cluster.md "sizing-guidelines-cluster.md")
- [Error messages](rabbitmq-resource-hard-limit.md#sizing-guidelines-limits-error-messages "rabbitmq-resource-hard-limit.md#sizing-guidelines-limits-error-messages")

###### Note

RabbitMQ 3.13 brokers do not come with default resource limits, but we recommend you use the suggested defaults.

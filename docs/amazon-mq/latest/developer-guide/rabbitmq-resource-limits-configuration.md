# Default resource limits

Amazon MQ for RabbitMQ supports configuring the broker resource limits from RabbitMQ 4 onwards. When you create a broker, Amazon MQ automatically applies default values to these resource limits. These defaults act as guardrails to protect your broker availability while accommodating common customer usage patterns. You can customize your broker behavior by changing the limit configuration values to better match your specific workload requirements.

Before making changes, please note:

###### Important

1. Configuration changes can impact broker performance and availability
2. Understand the impact before changing any default configuration options
3. Test configuration changes in non-production environments first
4. Monitor broker health after applying changes

###### Important

Default values and supported ranges for these configurations vary by RabbitMQ version, instance type, and broker deployment mode.

###### Important

_Note: Associating or creating a broker with configuration values outside the supported range will result in an error response._

The default resource limits applied for RabbitMQ 4.2 brokers are

- [Default resource limits for m7g single-instance deployment](#default-values-single-instance "#default-values-single-instance")
- [Default resource limits for m7g cluster deployment](#default-values-cluster-brokers "#default-values-cluster-brokers")

## Default resource limits

###### Important

Amazon MQ for RabbitMQ 3 brokers, the default is configured with the maximum resource limit and Amazon MQ does not provide the ability to override resource limit configuration.

### Default values for single instance brokers

| Instance type   | Connections per Node | Channels per Node | Consumers per channel | Queues | vhosts | Shovels | Exchanges | Message size in Bytes |
| --------------- | -------------------- | ----------------- | --------------------- | ------ | ------ | ------- | --------- | --------------------- |
| mq.m7g.medium   | 100                  | 500               | 10                    | 500    | 10     | 30      | 500       | 524288                |
| mq.m7g.large    | 1,500                | 4,500             | 10                    | 1,000  | 50     | 50      | 1,000     | 524288                |
| mq.m7g.xlarge   | 3,000                | 9,000             | 10                    | 2,000  | 100    | 100     | 2,000     | 524288                |
| mq.m7g.2xlarge  | 6,000                | 18,000            | 10                    | 4,000  | 150    | 200     | 4,000     | 524288                |
| mq.m7g.4xlarge  | 12,000               | 36,000            | 10                    | 8,000  | 200    | 400     | 8,000     | 524288                |
| mq.m7g.8xlarge  | 24,000               | 72,000            | 10                    | 16,000 | 250    | 800     | 16,000    | 524288                |
| mq.m7g.12xlarge | 36,000               | 108,000           | 10                    | 24,000 | 300    | 1,200   | 24,000    | 524288                |
| mq.m7g.16xlarge | 48,000               | 144,000           | 10                    | 32,000 | 350    | 1,600   | 32,000    | 524288                |

### Default values for cluster brokers

| Instance type   | Connections per Node | Channels per Node | Consumers per channel | Queues | vhosts | Shovels | Exchanges | Message size in Bytes |
| --------------- | -------------------- | ----------------- | --------------------- | ------ | ------ | ------- | --------- | --------------------- |
| mq.m7g.medium   | 100                  | 300               | 10                    | 100    | 10     | 10      | 100       | 524288                |
| mq.m7g.large    | 500                  | 1500              | 10                    | 1,000  | 50     | 30      | 1,000     | 524288                |
| mq.m7g.xlarge   | 1000                 | 3000              | 10                    | 2,000  | 100    | 60      | 2,000     | 524288                |
| mq.m7g.2xlarge  | 2000                 | 6000              | 10                    | 4,000  | 150    | 120     | 4,000     | 524288                |
| mq.m7g.4xlarge  | 4000                 | 12,000            | 10                    | 8,000  | 200    | 240     | 8,000     | 524288                |
| mq.m7g.8xlarge  | 8000                 | 24,000            | 10                    | 16,000 | 250    | 480     | 16,000    | 524288                |
| mq.m7g.12xlarge | 12000                | 36,000            | 10                    | 24,000 | 300    | 720     | 24000     | 524288                |
| mq.m7g.16xlarge | 16,000               | 48,000            | 10                    | 32,000 | 350    | 960     | 32,000    | 524288                |

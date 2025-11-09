# Amazon MQ for ActiveMQ Throughput benchmarks

Benchmarking can help you choose the correct instance type and size for your workload
messaging requirements. Scenarios for benchmarking include:

- **Cluster Stability**:
  understanding how stable your cluster is during increasing, fluctuating, and stable load types.
- **Defining performance limits**:
  approximating the maximum performance and throughput capabilities (i.e. cluster limits) of your cluster
  to help better scale your broker nodes when the number of messages published to your broker increases.
- **Optimal architecture and parameters**:
  determining the most suitable architecture/parameters for your clusters, such as the number of destinations, persistent mode, message size, etc.

Amazon MQ provides benchmarking figures for the different instance types and sizes available for Amazon MQ for ActiveMQ.

Amazon MQ uses the [ActiveMQ Maven 2
Performance Test](https://activemq.apache.org/activemq-performance-module-users-manual "https://activemq.apache.org/activemq-performance-module-users-manual") to calculate benchmarks. Amazon MQ tests with an active/stanby deployment
broker with an EFS volume as a storage type. The results are from a performance test conducted on
a ECS cluster with a Fargate deployment which consists of a configuration of 4vCPUs and 16 GiBs of
memory (equivalent to an EC2 m5.xlarge instance). Concurrent Store And Dispatch Queues (CSAD) are
set to true for all tests performed. The duration for each test conducted is 5 minutes.

###### Note

When run in your own environment, results may differ by 3-6%.

The following tables provide performance and throughput benchmarks for
Amazon MQ supported instance types to help you choose the correct instance sizes for your messaging workload.

###### Topics

- [mq.m4.large](#amazon-mq-broker-instance-mq.m4.large "#amazon-mq-broker-instance-mq.m4.large")
- [mq.m5.large](#amazon-mq-broker-instance-mq.m5.large "#amazon-mq-broker-instance-mq.m5.large")
- [mq.m5.xlarge](#amazon-mq-broker-instance-mq.m5.xlarge "#amazon-mq-broker-instance-mq.m5.xlarge")
- [mq.m5.2xlarge](#amazon-mq-broker-instance-mq.m5.2xlarge "#amazon-mq-broker-instance-mq.m5.2xlarge")
- [mq.m5.4xlarge](#amazon-mq-broker-instance-mq.m5.4xlarge "#amazon-mq-broker-instance-mq.m5.4xlarge")

## `mq.m4.large`

Configuration options:

- **Broker Instance -** `mq.m4.large`
- **Persistent -** `TRUE`
- **Client -** `m5.xlarge`
- **CSAD -** `TRUE`
- **Protocol -** Openwire

|              | Producers/Consumers |
| ------------ | ------------------- | ---- | ---- | ---- |
| Message size | Metrics             | 25   | 50   | 100  |
| 1KB          | TPS                 | 1849 | 3335 | 4665 |
| CPU%         | 29%                 | 37%  | 47%  |
| 5KB          | TPS                 | 1672 | 2561 | 2970 |
| CPU%         | 33%                 | 47%  | 76%  |
| 10KB         | TPS                 | 1586 | 1670 | 2268 |
| CPU%         | 44%                 | 87%  | 89%  |

## `mq.m5.large`

Configuration options:

- **Broker Instance -** `mq.m5.large`
- **Persistent -** `TRUE`
- **Client -** `m5.xlarge`
- **CSAD -** `TRUE`
- **Protocol -** Openwire

|              | Producers/Consumers |
| ------------ | ------------------- | ---- | ---- | ---- |
| Message size | Metrics             | 25   | 50   | 100  |
| 1KB          | TPS                 | 2247 | 4041 | 7566 |
| CPU%         | 26%                 | 32%  | 48%  |
| 5KB          | TPS                 | 1636 | 3205 | 4443 |
| CPU%         | 37%                 | 63%  | 58%  |
| 10KB         | TPS                 | 1668 | 3104 | 3227 |
| CPU%         | 40%                 | 53%  | 86%  |

## `mq.m5.xlarge`

Configuration options:

- **Broker Instance -** `mq.m5.xlarge`
- **Persistent -** `TRUE`
- **Client -** `m5.xlarge`
- **CSAD -** `TRUE`
- **Protocol -** Openwire

|              | Producers/Consumers |
| ------------ | ------------------- | ---- | ---- | ---- |
| Message size | Metrics             | 25   | 50   | 100  |
| 1KB          | TPS                 | 2255 | 3932 | 7453 |
| CPU%         | 28%                 | 32%  | 54%  |
| 5KB          | TPS                 | 1766 | 3495 | 6215 |
| CPU%         | 29%                 | 51%  | 82%  |
| 10KB         | TPS                 | 1641 | 3240 | 5613 |
| CPU%         | 36%                 | 61%  | 89%  |

## `mq.m5.2xlarge`

Configuration options:

- **Broker Instance -** `mq.m5.2xlarge`
- **Persistent -** `TRUE`
- **Client -** `m5.xlarge`
- **CSAD -** `TRUE`
- **Protocol -** Openwire

|              | Producers/Consumers |
| ------------ | ------------------- | ---- | ---- | ---- |
| Message size | Metrics             | 25   | 50   | 100  |
| 1KB          | TPS                 | 2025 | 4089 | 8093 |
| CPU%         | 12%                 | 18%  | 35%  |
| 5KB          | TPS                 | 1865 | 3736 | 6845 |
| CPU%         | 15%                 | 27%  | 54%  |
| 10KB         | TPS                 | 1747 | 3511 | 7057 |
| CPU%         | 18%                 | 36%  | 67%  |

## `mq.m5.4xlarge`

Configuration options:

- **Broker Instance -** `mq.m5.4xlarge`
- **Persistent -** `TRUE`
- **Client -** `m5.xlarge`
- **CSAD -** `TRUE`
- **Protocol -** Openwire

|              | Producers/Consumers |
| ------------ | ------------------- | ---- | ---- | ---- |
| Message size | Metrics             | 25   | 50   | 100  |
| 1KB          | TPS                 | 2094 | 4055 | 8153 |
| CPU%         | 6%                  | 9%   | 17%  |
| 5KB          | TPS                 | 1742 | 3586 | 7158 |
| CPU%         | 7%                  | 13%  | 25%  |
| 10KB         | TPS                 | 1733 | 3288 | 6671 |
| CPU%         | 9%                  | 16%  | 31%  |

# Troubleshooting Amazon MQ

This section describes common issues you might encounter when using Amazon MQ brokers, and the steps you can take to resolve them.
For general troubleshooting, see [Troubleshooting: General Amazon MQ](general.md "general.md"). For troubleshooting your specific
engine version, see the following sections.

## Troubleshooting ActiveMQ on Amazon MQ

| Troubleshooting topic                                                                                                                           | Description                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [General troubleshooting](troubleshooting-activemq.md "troubleshooting-activemq.md")                                                            | Use the information in this section to help you diagnose<br>and resolve common issues you might encounter when working with ActiveMQ on Amazon MQ brokers. |
| [BROKER_ENI_DELETED](troubleshooting-action-required-codes-broker-eni-deleted.md "troubleshooting-action-required-codes-broker-eni-deleted.md") | ActiveMQ on Amazon MQ will raise a `BROKER_ENI_DELETED` alarm when you delete a broker’s Elastic Network Interface (ENI).                                  |
| [BROKER_OOM](troubleshooting-action-required-codes-broker-out-of-memory.md "troubleshooting-action-required-codes-broker-out-of-memory.md")     | ActiveMQ on Amazon MQ will raise a BROKER_OOM alarm when the broker undergoes a restart loop due to<br>the insufficient memory capacity                    |

## Troubleshooting RabbitMQ on Amazon MQ

| Troubleshooting topic                                                                                                                                    | Description                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [General troubleshooting](troubleshooting-rabbitmq.md "troubleshooting-rabbitmq.md")                                                                     | Diagnose common issues<br>you might encounter when working with RabbitMQ brokers.                                                                                                                                      |
| [RABBITMQ_MEMORY_ALARM](troubleshooting-action-required-codes-rabbitmq-memory-alarm.md "troubleshooting-action-required-codes-rabbitmq-memory-alarm.md") | RabbitMQ will raise a high memory alarm when the broker's memory usage, identified by CloudWatch metric<br>`RabbitMQMemUsed`, exceeds the memory limit, identified by `RabbitMQMemLimit`.                              |
| [RABBITMQ_INVALID_KMS_KEY](troubleshooting-action-required-codes-invalid-kms-key.md "troubleshooting-action-required-codes-invalid-kms-key.md")          | RabbitMQ on Amazon MQ will raise an INVALID_KMS_KEY critical action required code when a broker created<br>with a customer managed AWS KMS key(CMK) detects that the AWS Key Management Service (KMS) key is disabled. |
| [RABBITMQ_DISK_ALARM](troubleshooting-action-required-codes-disk-limit-alarm.md "troubleshooting-action-required-codes-disk-limit-alarm.md")             | Disk limit alarm is an indication that the volume of disk used by a RabbitMQ node has decreased due to<br>a high number of messages not consumed while new messages were added.                                        |

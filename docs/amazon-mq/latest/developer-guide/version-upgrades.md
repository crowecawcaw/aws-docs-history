# Version upgrades

You can manually upgrade your broker at any time to the next supported major or minor version. For more information about manually upgrading your broker, see [Upgrading an Amazon MQ broker engine version](upgrading-brokers.md "upgrading-brokers.md").

Amazon MQ manages upgrades to the latest supported patch version for all RabbitMQ brokers using version 3.13 and above. Both manual and automatic version upgrades occur during the scheduled maintenance window or after you reboot your broker.

###### Important

RabbitMQ only allows incremental version updates (ex: 3.9.x to 3.10.x). You cannot skip minor versions when updating (ex: 3.8.x to 3.11.x).

Single instance brokers will be offline while being rebooted. For cluster brokers, the mirrored queues must be synced during reboot. With longer queues, the queue-sync process can take longer. During the queue-sync process, the queue is unavailable to consumers and producer. When the queue-sync process is complete, the broker becomes available again. To minimize the impact, we recommend upgrading during a low traffic time. For more information on best practices for version upgrades, see [Amazon MQ for RabbitMQ best practices](best-practices-rabbitmq.md "best-practices-rabbitmq.md").



# Upgrading Amazon MQ for RabbitMQ 3 broker to 4
<a name="upgrading-rabbitmq-v3-to-v4"></a>

 Amazon MQ supports in-place upgrades from RabbitMQ 3.13 to RabbitMQ 4.2. An in-place upgrade requires no application code changes. During the upgrade, Amazon MQ blocks all connections to the broker. 

 Amazon MQ does not provide a managed blue-green deployment option. If you choose to perform a blue-green deployment independently, see [Blue-green deployment.](https://www.rabbitmq.com/docs/blue-green-upgrade) 

**Important**  
Review the feature deprecations, breaking changes, and new functionality introduced in [RabbitMQ 4](rabbitmq-4.md) before upgrading to ensure smooth post-upgrade operation.

The following table compares the two upgrade approaches.


**Comparison of upgrade approaches**  

| Consideration | In-place upgrade (Recommended) | Blue-green deployment | 
| --- | --- | --- | 
| Downtime | Yes, Amazon MQ blocks all connections to the broker during the upgrade. The downtime depends on queue depth. Keeping your queues short will reduce the downtime. | No, you can migrate producers and consumers to the new broker without downtime. | 
| Application code changes | No changes required. The broker endpoint remains the same after the upgrade. | Yes, you must update your application code to redirect producers and consumers to the new broker. | 
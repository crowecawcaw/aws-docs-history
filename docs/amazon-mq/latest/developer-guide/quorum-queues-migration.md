

# Migrating from classic queues to quorum queues on Amazon MQ for RabbitMQ
<a name="quorum-queues-migration"></a>

You can migrate your classic mirrored queues to quorum queues on Amazon MQ brokers on version 3.13 or above by creating a new virtual host on the same cluster, or by migrating in place. 

## Option 1: Migrating from classic mirrored queues to quorum queues with Amazon MQ for RabbitMQ queue migration tool
<a name="migrating-quorum-queues-with-amazon-mq-queue-migration-tool"></a>

 Amazon MQ provides a queue migration tool to migrate classic queues to quorum queues. The tool is accessible through the RabbitMQ web console under **Admin** > **Queue Migration**, or through the HTTP API. 

 To use the tool see, [Amazon MQ queue migration tool](https://github.com/amazon-mq/rabbitmq-queue-migration). 

## Option 2: Migrating from classic mirrored queues to quorum queues with a new virtual host
<a name="migrating-quorum-queues-with-vhost"></a>

 You can migrate your classic mirrored queues to quorum queues on Amazon MQ brokers on version 3.13 or above by creating a new virtual host on the same cluster. 

1. In your existing cluster, create a new virtual host (vhost) with the default queue type as quorum.

1. Create the [Federation plugin](rabbitmq-basic-elements-plugins.md#rabbitmq-federation-plugin) from the new vhost with the URI pointing to the old vhost using classic mirrored queues.

1. Using `rabbitmqadmin`, export the definitions from the old vhost to a new file. You must make changes to the schema file so it is compatible with quorum queues. For the full list of changes you need to make to the file, see [Moving definitions](https://www.rabbitmq.com/blog/2023/03/02/quorum-queues-migration#moving-definitions) in the RabbitMQ quorum queues documentation. After applying the necessary changes to the file, reimport the definitions to the new vhost. 

1.  Create a new policy in the new vhost. For recommendations on Amazon MQ policy configurations for quorum queues, see [Policy configurations for quorum queues for Amazon MQ for RabbitMQ](quorum-queues-policy-configurations.md) . Then, start the Federation you created earlier from the old vhost to the new vhost. 

1.  Point consumers and producers to the new vhost.

1. Configure the Shovel plug in to move any remaining messages. Once a queue is empty, delete the Shovel.

## Migrating from classic mirrored queues to quorum queues in place
<a name="migrating-quorum-queues-in-place"></a>

 You can migrate your classic mirrored queues to quorum queues on Amazon MQ brokers on version 3.13 or above by migrating in place. 

1. Stop the consumers and producers.

1. Create a new temporary quorum queue.

1. Configure the Shovel plug in to move any messages from the old classic mirrored queue to the new temporary quorum queue. After all messages are moved to the temporary quorum queue, delete the Shovel.

1. Delete the source classic mirrored queue. Then, recreate a quorum queue with the same name and bindings as the source classic mirrored queue.

1. Create a new Shovel to move the messages from the temporary quorum queue to the new quorum queue.
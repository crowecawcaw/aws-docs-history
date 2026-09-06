

# Blue-green deployment from RabbitMQ 3 to 4
<a name="upgrading-rabbitmq-v3-to-v4-blue-green"></a>

 Amazon MQ does not provide a managed blue-green deployment option for upgrading from RabbitMQ 3.13 to RabbitMQ 4.2. If you choose to perform a blue-green deployment independently, this approach requires application code changes to redirect producers and consumers to the new broker. 

 For detailed instructions, see [Blue-green deployment](https://www.rabbitmq.com/docs/blue-green-upgrade) in the RabbitMQ documentation. 
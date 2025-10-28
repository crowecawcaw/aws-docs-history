# Understand MSK Connect workers

A worker is a Java virtual machine (JVM) process that runs the connector logic. Each
worker creates a set of tasks that run in parallel threads and do the work of copying the
data. Tasks don't store state, and can therefore be started, stopped, or restarted at any
time in order to provide a resilient and scalable data pipeline. Changes to the number of
workers, whether due to a scaling event or due to unexpected failures, are automatically
detected by the remaining workers. They coordinate to rebalance tasks across the set of
remaining workers. Connect workers use Apache Kafka's consumer groups to coordinate and
rebalance.

If your connector's capacity requirements are variable or difficult to estimate, you can
let MSK Connect scale the number of workers as needed between a lower limit and an upper
limit that you specify. Alternatively, you can specify the exact number of workers that you
want to run your connector logic. For more information, see [Understand connector capacity](msk-connect-capacity.md "msk-connect-capacity.md").

###### MSK Connect workers consume IP addresses

MSK Connect workers consume IP addresses in the customer-provided subnets. Each worker uses one IP address from one of the customer-provided subnets. You should ensure that you have enough available IP addresses in the subnets provided to a CreateConnector request to account for their specified capacity, especially when autoscaling connectors where the number of workers can fluctuate.

## Default worker configuration

MSK Connect provides the following default worker configuration:

```
key.converter=org.apache.kafka.connect.storage.StringConverter
value.converter=org.apache.kafka.connect.storage.StringConverter
```

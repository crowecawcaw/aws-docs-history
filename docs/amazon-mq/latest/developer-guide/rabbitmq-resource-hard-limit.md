# Amazon MQ for RabbitMQ maximum resource limit

## Sizing guidelines for m7g with quorum queues for single instance deployment

The following table shows the **maximum** limit values for each instance type for single instance brokers.

| Instance Type   | Connections | Channels | Consumers per channel | Queues  | Vhosts | Shovels | Exchanges | Message Size in Bytes |
| --------------- | ----------- | -------- | --------------------- | ------- | ------ | ------- | --------- | --------------------- |
| mq.m7g.medium   | 300         | 900      | 1,000                 | 2,500   | 10     | 150     | 12500     | 134217728             |
| mq.m7g.large    | 5,000       | 15,000   | 1,000                 | 20,000  | 1500   | 250     | 100,000   | 134217728             |
| mq.m7g.xlarge   | 10,000      | 30,000   | 1,000                 | 30,000  | 1,500  | 500     | 150,000   | 134217728             |
| mq.m7g.2xlarge  | 20,000      | 60,000   | 1,000                 | 40,000  | 1,500  | 1,000   | 200,000   | 134217728             |
| mq.m7g.4xlarge  | 40,000      | 120,000  | 1,000                 | 60,000  | 1,500  | 2000    | 300,000   | 134217728             |
| mq.m7g.8xlarge  | 80,000      | 240,000  | 1,000                 | 80,000  | 1,500  | 4000    | 400,000   | 134217728             |
| mq.m7g.12xlarge | 120,000     | 360,000  | 1,000                 | 100,000 | 1,500  | 6,000   | 500,000   | 134217728             |
| mq.m7g.16xlarge | 160,000     | 480,000  | 1,000                 | 120,000 | 1,500  | 8,000   | 600,000   | 134217728             |

## Sizing guidelines for m7g with quorum queues for cluster deployment

The following table shows the **maximum** limit values for each instance type for cluster brokers.

| Instance Type   | Connections per Node | Channels per Node | Consumers per channel | Queues | Vhosts | Shovels | Exchanges | Message Size in Bytes |
| --------------- | -------------------- | ----------------- | --------------------- | ------ | ------ | ------- | --------- | --------------------- |
| mq.m7g.medium   | 300                  | 900               | 1,000                 | 500    | 10     | 50      | 500       | 134217728             |
| mq.m7g.large    | 5,000                | 15,000            | 1,000                 | 10,000 | 1,500  | 150     | 50,000    | 134217728             |
| mq.m7g.xlarge   | 10,000               | 30,000            | 1,000                 | 15,000 | 1,500  | 300     | 75,000    | 134217728             |
| mq.m7g.2xlarge  | 20,000               | 60,000            | 1,000                 | 20,000 | 1,500  | 600     | 100,000   | 134217728             |
| mq.m7g.4xlarge  | 40,000               | 120,000           | 1,000                 | 30,000 | 1,500  | 1200    | 150,000   | 134217728             |
| mq.m7g.8xlarge  | 80,000               | 240,000           | 1,000                 | 40,000 | 1,500  | 2,400   | 200,000   | 134217728             |
| mq.m7g.12xlarge | 120,000              | 360,000           | 1,000                 | 50,000 | 1,500  | 3,600   | 250,000   | 134217728             |
| mq.m7g.16xlarge | 160,000              | 480,000           | 1,000                 | 60,000 | 1,500  | 4,800   | 300,000   | 134217728             |

The following table shows the **maximum** limit values for each instance type for single instance brokers.

| Instance Type | Connections | Channels | Consumers per channel | Queues  | Vhosts | Shovels |
| ------------- | ----------- | -------- | --------------------- | ------- | ------ | ------- |
| m5.large      | 5,000       | 15,000   | 1,000                 | 30,000  | 1500   | 250     |
| m5.xlarge     | 10,000      | 30,000   | 1,000                 | 60,000  | 1500   | 500     |
| m5.2xlarge    | 20,000      | 60,000   | 1,000                 | 120,000 | 1500   | 1,000   |
| m5.4xlarge    | 40,000      | 120,000  | 1000                  | 240,000 | 1,000  | 2,000   |

The following table shows the **maximum** limit values for each instance type for cluster brokers.

| Instance Type | Queues | Consumers per channel | Shovels |
| ------------- | ------ | --------------------- | ------- |
| m5.large      | 10,000 | 1,000                 | 150     |
| m5.xlarge     | 15,000 | 1,000                 | 300     |
| m5.2xlarge    | 20,000 | 1,000                 | 600     |
| m5.4xlarge    | 30,000 | 1,000                 | 1200    |

The following connection and channel limits are applied per node:

| Instance Type | Connections | Channels |
| ------------- | ----------- | -------- |
| m5.large      | 5000        | 15,000   |
| m5.xlarge     | 10,000      | 30,000   |
| m5.2xlarge    | 20,000      | 60,000   |
| m5.4xlarge    | 40,000      | 120,000  |

The exact limit values for a cluster broker
may be lower than the indicated value depending on the number of available nodes
and how RabbitMQ distributes resources among the available nodes.
If you exceed the limit values, you can create a new connection to a different node and try again,
or you can upgrade the instance size to increase the maximum limits

## Error messages

The following error messages are returned when limits are exceeded.
All values are based on the `m7.large` single instance limits.

###### Note

The error codes for the following messages may change based on the client library you are using.

**Connection**

`ConnectionClosedByBroker 500 "NOT_ALLOWED - connection refused: node connection limit (5000) is reached"`

**Channel**

`ConnectionClosedByBroker 1500 "NOT_ALLOWED - number of channels opened on node
 'rabbit@ip-10-0-23-173.us-west-2.compute.internal' has reached the maximum allowed limit of (15,000)"`

**Consumer**

`ConnectionClosedByBroker: (530, 'NOT_ALLOWED - reached maximum (1,000) of consumers per channel')`

**Maximum message size**

`(406, 'PRECONDITION_FAILED - message size 524289 is larger than configured max size 524288')`

**Exchange**

`(406, "PRECONDITION_FAILED - cannot declare exchange 'limit_test_3' in vhost '/': exchange limit of 10 is reached")`

###### Note

The following error messages use the HTTP Management API format.

**Queue**

`{"error":"bad_request","reason":"cannot declare queue 'my_queue': queue limit in cluster (10,000) is reached"}]`

**Shovel**

`{"error":"bad_request","reason":"Validation failed\n\ncomponent shovel is limited to 150 per node\n"}`

**Vhost**

`{"error":"bad_request","reason":"cannot create vhost 'my_vhost': vhost limit of 1500 is reached"}`

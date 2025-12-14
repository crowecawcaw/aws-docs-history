# `pcluster describe-cluster-instances`

Describe the instances in a cluster.

```
pcluster describe-cluster-instances [-h]
                 --cluster-name `CLUSTER_NAME`
                [--debug]
                [--next-token `NEXT_TOKEN`]
                [--node-type {`HeadNode`,`ComputeNode`,`LoginNode`}]
                [--query `QUERY`]
                [--queue-name `QUEUE_NAME`]
                [--region `REGION`]
```

## Named arguments

`-h, --help`

Shows the help text for `pcluster describe-cluster-instances`.

`--cluster-name, -n `CLUSTER_NAME``

Specifies the name of the cluster.

`--debug`

Enables debug logging.

`--next-token `NEXT_TOKEN``

The token for the next set of results.

`--node-type {`HeadNode`,`ComputeNode`,`LoginNode`}`

Specifies the node types to list. Supported values are `HeadNode`, `ComputeNode` and `LoginNode`.
If this parameter is not specified, the `HeadNode`, `ComputeNode` and `LoginNode`a instances are
described.

`--query `QUERY``

Specifies the JMESPath query to perform on the output.

`--queue-name `QUEUE_NAME``

Specifies the name of the queue to list. If this parameter is not specified, instances in all queues are
described.

`--region, -r `REGION``

Specifies the AWS Region to use. The AWS Region must be specified, using the `AWS_DEFAULT_REGION`
environment variable, the `region` setting in the `[default]` section of the
`~/.aws/config` file, or the `--region` parameter.

**Example using AWS ParallelCluster version 3.1.4:**

````
`$` `pcluster describe-cluster-instances -n `cluster-v3```{
 "instances": [
 {
 "launchTime": "2022-07-12T17:22:21.000Z",
 "instanceId": "i-1234567890abcdef0",
 "publicIpAddress": "198.51.100.44",
 "instanceType": "t2.micro",
 "state": "running",
 "nodeType": "HeadNode",
 "privateIpAddress": "192.0.2.0.196"
 },
 {
 "launchTime": "2022-07-12T17:37:42.000Z",
 "instanceId": "i-021345abcdef6789",
 "queueName": "queue1",
 "publicIpAddress": "198.51.100.44",
 "instanceType": "t2.micro",
 "state": "pending",
 "nodeType": "ComputeNode",
 "privateIpAddress": "192.0.2.0.196"
 },
 {
 "launchTime": "2022-07-12T17:37:42.000Z",
 "instanceId": "i-021345abcdef6789",
 "poolName": "pool1",
 "publicIpAddress": "198.51.100.44",
 "instanceType": "t2.micro",
 "state": "pending",
 "nodeType": "loginNode",
 "privateIpAddress": "192.0.2.0.196"
 }
 ]
}`
````

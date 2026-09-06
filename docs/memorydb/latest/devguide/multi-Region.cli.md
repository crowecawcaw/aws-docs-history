

# Using MemoryDB Multi-Region with the CLI
<a name="multi-Region.cli"></a>

Below are ways to use MemoryDB Multi-Region with the CLI

**Note**  
MemoryDB Multi-Region only supports node type db.r7g.xlarge and above.

## Creating clusters with MemoryDBMulti Region
<a name="multi-Region.cli.create"></a>

**Create a Multi Region cluster**

```
aws memorydb create-multi-region-cluster \
	--multi-region-cluster-name-suffix my-multi-region-cluster \
	--node-type db.r7g.xlarge \
	--engine valkey \
	--region us-east-1
```

**Create a regional cluster in US East (N. Virginia) Region**

```
aws memorydb create-cluster \
	--cluster-name my-cluster \
	--multi-region-cluster-name my-multi-region-cluster \
	--node-type db.r7g.xlarge \
	--acl-name open-access \
	--region us-east-1 \
```

**Create a Region cluster in Europe (Ireland) Region**

```
aws memorydb create-cluster \
	--cluster-name my-cluster \
	--multi-region-cluster-name my-multi-region-cluster \
	--node-type db.r7g.xlarge \
	--acl-name open-access \
	--region eu-west-1 \
```

**Describe the Multi Region cluster from any Region**

```
aws memorydb describe-multi-region-cluster \
	--multi-region-cluster-name my-multi-region-cluster \
	--region eu-west-1
```

## Update a Multi Region cluster
<a name="multi-Region.cli.update"></a>

**Modifying Node Type**

```
aws memorydb update-multi-region-cluster \
	--multi-region-cluster-name my-multi-region-cluster \
	--node-type db.r7g.4xlarge \
	--region us-east-1
```

**Modifying shard count**

```
aws memorydb update-multi-region-cluster \
	--multi-region-cluster-name my-multi-region-cluster \
	--shard-configuration \
	ShardCount=3 \
	--update-strategy COORDINATED \
	--region us-east-1
```

## Scaling MemoryDB clusters
<a name="multi-Region.cli.scaling"></a>

First, list the nodes that can scale up or down with the `list-allowed-node-type-updates` command:

```
aws memorydb list-allowed-node-type-updates \
	--cluster-name my-cluster-name
```

This will provide a list of nodes that can be scaled up or down. To then update them, you can use the `update-cluster` command:

```
aws memorydb update-cluster  \
	--cluster-name my-cluster \
	--node-type db.r6g.2xlarge
```

For more information on scaling with Multi-Region see [Scaling with MemoryDB Multi-Region](multi-Region.Scaling.md).

## Deleting clusters in MemoryDB Multi-Region
<a name="multi-Region.cli.update"></a>

**Delete a regional cluster**

```
aws memorydb delete-cluster \	
	--cluster-name my-cluster \
	--multi-region-cluster-name my-multi-region-cluster \
	--region us-east-1
```

**Delete a Multi Region cluster**

```
aws memorydb delete-multi-region-cluster \
	--multi-region-cluster-name my-multi-region-cluster \
	--region us-east-1
```
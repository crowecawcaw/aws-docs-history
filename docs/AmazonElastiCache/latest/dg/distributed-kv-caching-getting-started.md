

# Getting started with distributed KV caching

In this tutorial, you create a distributed key-value (KV) caching cluster in the same Availability Zone as your graphics processing unit (GPU) inference fleet. Then you set up your client hosts, connect your inference engine to the cluster with LMCache, and confirm that the cluster serves requests.

**Important**  
A `cache.i8ge.48xlarge` node is billed per hour until you delete the cluster. Deleting the cluster permanently removes all data in it, and you can't back up this data. To delete the cluster, see [Deleting a replication group](Replication.DeletingRepGroup.md).

**Topics**
+ [Prerequisites](#distributed-kv-caching-getting-started.prerequisites)
+ [Step 1: Create a cache subnet group](#distributed-kv-caching-getting-started.subnet-group)
+ [Step 2: Create a security group](#distributed-kv-caching-getting-started.security-group)
+ [Step 3: Create a parameter group](#distributed-kv-caching-getting-started.parameter-group)
+ [Step 4: Create the cluster](#distributed-kv-caching-getting-started.create)
+ [Step 5: Get the configuration endpoint](#distributed-kv-caching-getting-started.endpoint)
+ [Step 6: Set up the client hosts](#distributed-kv-caching-getting-started.clients)
+ [Step 7: Verify the cluster](#distributed-kv-caching-getting-started.verify-cluster)
+ [Step 8: Connect your inference engine](#distributed-kv-caching-getting-started.configure)
+ [Step 9: Confirm that the cache serves requests](#distributed-kv-caching-getting-started.verify)
+ [Next steps](#distributed-kv-caching-getting-started.next-steps)

## Prerequisites
<a name="distributed-kv-caching-getting-started.prerequisites"></a>

Before you create a distributed KV caching cluster, make sure that you have the following:
+ An AWS account, and the AWS CLI configured with permissions to create ElastiCache and Amazon EC2 resources.
+ A VPC with a private subnet in the Availability Zone where your client hosts run.
+ For remote direct memory access (RDMA) over Elastic Fabric Adapter (EFA), client hosts that support EFA RDMA write, in the Availability Zone where you create the cluster. For the setup, see [Step 6: Set up the client hosts](#distributed-kv-caching-getting-started.clients).
+ For RDMA, the EFA software on each client host. Install it with the EFA installer, which provides the kernel driver, rdma-core, and libfabric. Many Deep Learning AMIs include it. valkey-glide-sync requires libfabric 2.4 or later. To check the version, run `/opt/amazon/efa/bin/fi_info --version`.
+ An autoregressive model that is served by vLLM or SGLang.
+ (Optional) An estimate of the benefit and of the number of shards, from KVTrace. You can't change the number of shards later. For more information, see [Sizing and scaling](distributed-kv-caching-limits.md#distributed-kv-caching-limits.scaling).

## Step 1: Create a cache subnet group
<a name="distributed-kv-caching-getting-started.subnet-group"></a>

ElastiCache requires all shards of the cluster to be in one Availability Zone. Use a private subnet in the Availability Zone of your GPU hosts. For the placement rules, see [Cache placement and sharing](distributed-kv-caching-how-it-works.md#distributed-kv-caching-how-it-works.placement).

The following command creates a cache subnet group with that one subnet. Replace {{subnet-1234567890abcdef0}} with the ID of your subnet.

```
aws elasticache create-cache-subnet-group \
  --cache-subnet-group-name kv-cache-subnet-group \
  --cache-subnet-group-description "Distributed KV caching, single AZ" \
  --subnet-ids subnet-1234567890abcdef0
```

## Step 2: Create a security group
<a name="distributed-kv-caching-getting-started.security-group"></a>

EFA requires a security group that allows all traffic to and from itself. You attach the same group to the cluster and to your client hosts. The following commands create the group, and add an inbound rule and an outbound rule that reference the group itself. Replace {{vpc-1234567890abcdef0}} with the ID of your VPC.

```
SG_ID=$(aws ec2 create-security-group \
  --group-name kv-cache-efa \
  --description "Distributed KV caching EFA and Valkey" \
  --vpc-id vpc-1234567890abcdef0 \
  --query GroupId --output text)

aws ec2 authorize-security-group-ingress --group-id $SG_ID \
  --ip-permissions "IpProtocol=-1,UserIdGroupPairs=[{GroupId=$SG_ID}]"

aws ec2 authorize-security-group-egress --group-id $SG_ID \
  --ip-permissions "IpProtocol=-1,UserIdGroupPairs=[{GroupId=$SG_ID}]"
```

You need both rules. If one of them is missing, `BLOB.RDMA_HELLO` still succeeds because it uses the Transport Layer Security (TLS) connection, but every RDMA transfer fails.

## Step 3: Create a parameter group
<a name="distributed-kv-caching-getting-started.parameter-group"></a>

Create a custom parameter group in the `valkey9` family. A new group has `cluster-enabled` set to `no`, which makes a cluster mode create fail, so set it to `yes`. Set `maxmemory-policy` to `allkeys-lru` so that writes can evict any key when a node is full. Use a dedicated cluster, because `allkeys-lru` can evict the keys of other applications.

```
aws elasticache create-cache-parameter-group \
  --cache-parameter-group-name kv-cache-params \
  --cache-parameter-group-family valkey9 \
  --description "Distributed KV caching parameters"

aws elasticache modify-cache-parameter-group \
  --cache-parameter-group-name kv-cache-params \
  --parameter-name-values "ParameterName=cluster-enabled,ParameterValue=yes" \
    "ParameterName=maxmemory-policy,ParameterValue=allkeys-lru"
```

For the other eviction options, see [Eviction and memory management](distributed-kv-caching-configuration.md#distributed-kv-caching-configuration.tiering).

## Step 4: Create the cluster
<a name="distributed-kv-caching-getting-started.create"></a>

The following command creates the cluster with the AWS CLI `create-replication-group` command (the `CreateReplicationGroup` API operation). You can also create the cluster with the ElastiCache console or CloudFormation. Use the subnet group, security group, and parameter group from the previous steps.

The command enables cluster mode, sets zero replicas, and sets encryption in transit with `TransitEncryptionMode` set to `required`. Because cluster mode requires automatic failover, include `--automatic-failover-enabled`, also with zero replicas. Encryption in transit is required, and you can't turn it off or change it. Encryption at rest is always on, and you can't turn it off. In the console, Multi-AZ and automatic backups are off by default, and you can't turn them on for this node type. For all required settings, see [Cluster requirements](distributed-kv-caching-limits.md#distributed-kv-caching-limits.requirements).

```
aws elasticache create-replication-group \
  --replication-group-id my-kv-cache \
  --replication-group-description "Distributed KV cache" \
  --engine valkey \
  --engine-version 9.1 \
  --cache-node-type cache.i8ge.48xlarge \
  --cache-parameter-group-name kv-cache-params \
  --cluster-mode enabled \
  --num-node-groups 1 \
  --replicas-per-node-group 0 \
  --automatic-failover-enabled \
  --cache-subnet-group-name kv-cache-subnet-group \
  --security-group-ids $SG_ID \
  --transit-encryption-enabled \
  --transit-encryption-mode required \
  --at-rest-encryption-enabled
```

This example creates one shard. To create more shards, set `--num-node-groups` to the number of shards that you need. To control access with users and user groups, add `--user-group-ids`. LMCache requires a Valkey user with a password (see [Step 8: Connect your inference engine](#distributed-kv-caching-getting-started.configure)). For more information, see [Large object ACLs](large-objects.md#large-objects-acl). To encrypt the data at rest with a customer managed key, add `--kms-key-id`.

Cluster creation takes several minutes. The following command waits until the cluster status is `available`.

```
aws elasticache wait replication-group-available \
  --replication-group-id my-kv-cache
```

## Step 5: Get the configuration endpoint
<a name="distributed-kv-caching-getting-started.endpoint"></a>

Your clients and your inference engine connect to the cluster with its configuration endpoint. The following command returns the configuration endpoint address.

```
aws elasticache describe-replication-groups \
  --replication-group-id my-kv-cache \
  --query "ReplicationGroups[0].ConfigurationEndpoint.Address" --output text
```

## Step 6: Set up the client hosts
<a name="distributed-kv-caching-getting-started.clients"></a>

Clients that use only TCP, for example with `BLOB.TCP_SET` and `BLOB.TCP_GET`, or with `SET` and `GET`, need only TLS and network access to the cluster on port 6379, through the security group from [Step 2: Create a security group](#distributed-kv-caching-getting-started.security-group). This is the simplest setup for development. Clients that use remote direct memory access (RDMA) also need the following:
+ **An instance type that supports EFA RDMA write.** RDMA write requires an EFA-enabled instance on Nitro version 4 or later. After you install the EFA software, run the following command to confirm that the efa-direct fabric supports write.

  ```
  /opt/amazon/efa/bin/fi_info -p efa -f efa-direct -c 'FI_RMA|FI_WRITE'
  ```

  If the output is empty or shows `No data available`, the instance doesn't support RDMA write. For the list of instance types, see [Supported instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types) in the Amazon EC2 User Guide.
+ **The EFA software.** Install it with the EFA installer, which provides the kernel driver, rdma-core, and libfabric. Many Deep Learning AMIs include it. valkey-glide-sync requires libfabric 2.4 or later. To check the version, run `/opt/amazon/efa/bin/fi_info --version`.
+ **An unlimited locked-memory limit.** Set `memlock` to unlimited for the user that runs the client, for example in `/etc/security/limits.conf`. Otherwise, memory registration fails with `fi_mr_reg: Cannot allocate memory`.
+ **The security group on every network interface.** Attach the security group from [Step 2: Create a security group](#distributed-kv-caching-getting-started.security-group) to the primary interface and to every `efa` and `efa-only` interface on the client host. `modify-instance-attribute --groups` changes only the primary interface, so use `modify-network-interface-attribute` for each interface. Its `--groups` option replaces the whole group list of the interface, so include the groups that the interface already has.

  Replace {{eni-1234567890abcdef0}} with the ID of the interface. Run the commands for each interface.

  To see the current security groups of the interface, run the following command.

  ```
  aws ec2 describe-network-interfaces \
    --network-interface-ids eni-1234567890abcdef0 \
    --query "NetworkInterfaces[0].Groups[].GroupId" --output text
  ```

  Then run the following command. Replace {{existing-group-ids}} with the group IDs from the previous command, separated by spaces. The command adds the new security group to them.

  ```
  aws ec2 modify-network-interface-attribute \
    --network-interface-id eni-1234567890abcdef0 \
    --groups existing-group-ids $SG_ID
  ```
+ **A client library with RDMA support.** valkey-glide-sync 2.6.0 or later supports RDMA in the Python sync client. In cluster mode, the client must send `BLOB.RDMA_HELLO` on its connection to each node, also after a `MOVED` or `ASK` redirect. The client library does this for you. For more information, see [Cluster mode](https://valkey.io/topics/large-object/#cluster-mode) on the valkey.io website.

## Step 7: Verify the cluster
<a name="distributed-kv-caching-getting-started.verify-cluster"></a>

From a client host, store and read a test object, and then check that the module is loaded. Replace {{configuration-endpoint}} with the configuration endpoint from [Step 5: Get the configuration endpoint](#distributed-kv-caching-getting-started.endpoint). Use valkey-cli 8.0 or later, built with TLS.

```
valkey-cli -c --tls -h {{configuration-endpoint}} -p 6379
> BLOB.TCP_SET test-key hello
OK
> BLOB.TCP_GET test-key
"hello"
> INFO largeobj
> DEL test-key
```

`INFO` returns data for only the node that you're connected to. For more information, see [Node-level detail with INFO largeobj](distributed-kv-caching-monitoring.md#distributed-kv-caching-monitoring.info). If you use role-based access control (RBAC), add `--user {{user-name}} --askpass`.

## Step 8: Connect your inference engine
<a name="distributed-kv-caching-getting-started.configure"></a>

The following example connects vLLM or SGLang to the cluster with LMCache in multiprocess mode, with the `rdma` transport. For how LMCache uses host memory (L1) and the cluster (L2), and for the transports, see [Inference engine connectors](distributed-kv-caching-how-it-works.md#distributed-kv-caching-how-it-works.connectors).

1. Create a Valkey user with a password for LMCache, and add it to a user group of the cluster. Limit the user to the LMCache keys and to the commands of its transport. Replace {{key-prefix}} with the `key_prefix` value that LMCache uses. For the `rdma` transport, use the following access string.

   ```
   on ~{{key-prefix}}@* +@largeobj +EXISTS +DEL +EXPIRE +INFO +PING +client|setinfo +client|setname +cluster|slots +cluster|info
   ```

   For the access strings of the `blob-tcp` and `tcp` transports, see [Valkey user for LMCache](distributed-kv-caching-security.md#distributed-kv-caching-security.lmcache-user).

   Store the password in AWS Secrets Manager, as plain text. Give the instance role of each GPU host permission to read only this secret (`secretsmanager:GetSecretValue`). For more information, see [Role-Based Access Control (RBAC)](Clusters.RBAC.md).

1. On each GPU host, install LMCache 0.5.8rc1 or later, valkey-glide-sync, and the AWS SDK for Python (Boto3) in a virtual environment. Use the same LMCache version on every host and in the engine image.

   ```
   python3.12 -m venv /opt/lmcache/venv
   /opt/lmcache/venv/bin/pip install --upgrade 'lmcache>=0.5.8rc1' valkey-glide-sync boto3
   ```

   The version specifier allows a version that is not a stable release for LMCache only. Don't use `--pre`, because it allows such versions for every dependency. To confirm that the installed version supports RDMA, run the following commands. The first command must list `rdma_worker_pool.py`, and the second command must print `True True`.

   ```
   /opt/lmcache/venv/bin/python -c "import lmcache, pathlib; p = pathlib.Path(lmcache.__file__).parent / 'v1/distributed/l2_adapters/valkey'; print(sorted(f.name for f in p.glob('*worker_pool.py')))"
   /opt/lmcache/venv/bin/python -c 'import glide_sync as g; print(g.GlideClient.rdma_available(), g.GlideClient.rdma_usable())'
   ```

   Some LMCache versions send the user name and the password to valkey-glide in the wrong order, and the connection fails with `WRONGPASS`. A future LMCache release will fix this order. After each install or upgrade of LMCache or valkey-glide, run the following commands to compare the two orders.

   ```
   /opt/lmcache/venv/bin/python -c 'import inspect, glide_sync; print(inspect.signature(glide_sync.ServerCredentials.__init__))'
   grep -n -A3 "ServerCredentials(" "$(/opt/lmcache/venv/bin/python -c 'import lmcache, os; print(os.path.dirname(lmcache.__file__))')/v1/distributed/l2_adapters/valkey/worker_pool.py"
   ```

   If LMCache passes the user name first by position (for example `ServerCredentials(self._username, self._password)`) and the signature starts with `password`, swap the `username` and `password` values in the launcher of the next step. If LMCache uses keyword arguments, or the two orders agree, don't swap them.

1. Create an API key file for the LMCache server. The key protects the request channel and the HTTP API of the server. Make the file readable only by the users that run LMCache and the engine.

   ```
   sudo install -d -m 0750 /etc/lmcache
   head -c 32 /dev/urandom | base64 | tr -d '\n' | sudo tee /etc/lmcache/api.key >/dev/null
   sudo chmod 0440 /etc/lmcache/api.key
   ```

1. Create a launcher script that reads the password from Secrets Manager and starts the LMCache server with the Valkey L2 adapter. Other users of the host can read the command line of a process, so the password must not be on the command line or in a file. Replace the following values:
   + {{region}} and {{secret-id}} – The Region and the ID of the secret.
   + {{lmcache-user}} – The user name of the Valkey user.
   + {{configuration-endpoint}} – The configuration endpoint from [Step 5: Get the configuration endpoint](#distributed-kv-caching-getting-started.endpoint).
   + {{efa-device-1}}, {{efa-device-2}} – The EFA devices on the non-uniform memory access (NUMA) node of the LMCache server, from the `domain:` values of `/opt/amazon/efa/bin/fi_info -p efa -f efa-direct`.
   + {{key-prefix}} – The prefix from the access string of substep 1. For the prefix rules, see [LMCache connector settings](distributed-kv-caching-configuration.md#distributed-kv-caching-configuration.connector).

   ```python
   #!/usr/bin/env python3
   # lmcache-launch.py: start the LMCache server without the password on the command line.
   import json
   import sys
   
   import boto3
   from lmcache.cli.main import main
   
   password = boto3.client("secretsmanager", region_name="region").get_secret_value(
       SecretId="secret-id"
   )["SecretString"]
   
   adapter = {
       "type": "valkey",
       "transport": "rdma",
       "cluster_mode": True,
       "startup_nodes": "configuration-endpoint:6379",
       "username": "lmcache-user",
       "password": password,
       "tls_enable": True,
       "num_workers": 8,
       "rdma_provider": "efa-direct",
       "rdma_interface": ["efa-device-1", "efa-device-2"],
       "key_prefix": "key-prefix",
       "max_capacity_gb": 0,
   }
   sys.exit(main(["server", *sys.argv[1:], "--l2-adapter", json.dumps(adapter)]))
   ```

   The example uses a custom parameter group with `allkeys-lru`. If you use the default parameter group, also add the `ttl_seconds` field. For more information, see [Eviction and memory management](distributed-kv-caching-configuration.md#distributed-kv-caching-configuration.tiering).

1. Start the LMCache server with the launcher. Run it as a dedicated user with an unlimited locked-memory limit, for example with a systemd unit. Replace {{l1-size-gb}} with the size of the L1 tier, in GB. Start with about half of the memory of the NUMA node, below the pinned-memory limit of the host.

   ```
   PYTHONHASHSEED=0 /opt/lmcache/venv/bin/python lmcache-launch.py \
       --host 127.0.0.1 --port 5555 --l1-size-gb {{l1-size-gb}} \
       --no-l1-use-lazy --eviction-policy LRU \
       --eviction-trigger-watermark 0.6 --eviction-ratio 0.2 \
       --chunk-size 256 --hash-algorithm sha256_cbor \
       --supported-transfer-mode auto \
       --api-key-file /etc/lmcache/api.key
   ```

   With the `rdma` transport in LMCache 0.5.8rc1 or later, each worker registers the whole L1 tier with its EFA device. If the log shows `Registering the L1 arena ... with the fabric failed`, see [Troubleshooting distributed KV caching](distributed-kv-caching-troubleshooting.md). Before you start the engine, make sure that the LMCache log shows `ValkeyL2Adapter ready: transport=rdma`.

1. Start the engine with the LMCache multiprocess connector. Replace {{model-name}} with your model. For vLLM, set `kv_load_failure_policy` to `recompute` or `fail`, because the default changes between vLLM versions.

   ```
   PYTHONHASHSEED=0 LMCACHE_API_KEY_FILE=/etc/lmcache/api.key vllm serve {{model-name}} \
       --enable-prefix-caching \
       --kv-transfer-config '{
           "kv_connector": "LMCacheMPConnector",
           "kv_connector_module_path": "lmcache.integration.vllm.lmcache_mp_connector",
           "kv_role": "kv_both",
           "kv_load_failure_policy": "{{recompute}}",
           "kv_connector_extra_config": {
               "lmcache.mp.host": "tcp://127.0.0.1",
               "lmcache.mp.port": 5555
           }
       }'
   ```

   For SGLang 0.5.13 or later, create a file `lmcache_config.yaml` that contains `mp_host: 127.0.0.1` and `mp_port: 5555`, and start SGLang as follows. Don't set `--enable-hierarchical-cache` or `--hicache-storage-backend`.

   ```
   PYTHONHASHSEED=0 LMCACHE_API_KEY_FILE=/etc/lmcache/api.key python -m sglang.launch_server \
       --model-path {{model-name}} \
       --enable-lmcache --lmcache-config-file lmcache_config.yaml
   ```

   Keep your existing engine options for the listen address, API key, and TLS. The example shows only the options that LMCache needs.

All GPU hosts that share the cluster must use the same settings. For the list, see [LMCache connector settings](distributed-kv-caching-configuration.md#distributed-kv-caching-configuration.connector). On each host, start the LMCache server before the engine. To stop, stop the engine first. Then wait (at most 5 minutes) until `lmcache_mp_num_inflight_l2_stores` is 0 or absent in `/metrics`, and then stop the LMCache server. The metric updates about every 10 seconds, so wait at least 15 seconds before you read it. For all options, see [Installation](https://docs.lmcache.ai/getting_started/installation.html) and [Valkey L2 adapter](https://docs.lmcache.ai/mp/l2_storage/valkey.html) on the LMCache website.

## Step 9: Confirm that the cache serves requests
<a name="distributed-kv-caching-getting-started.verify"></a>

ElastiCache doesn't publish a KV cache hit rate metric. LMCache reports it on the `/metrics` endpoint of its HTTP API on the GPU host (by default `http://127.0.0.1:8080/metrics`, with the API key as a bearer token). For the hit-rate formula, see [Monitoring distributed KV caching](distributed-kv-caching-monitoring.md).

To test that the engine reads KV state from the cluster, do the following:

1. Send prompts that are longer than the chunk size, for example 1,000 tokens or more.

1. Restart the engine and the LMCache server, in the start and stop order of [Step 8: Connect your inference engine](#distributed-kv-caching-getting-started.configure). This empties GPU memory and the L1 tier.

1. Send the same prompts again. Make sure that `lmcache_mp_lookup_hit_l2_tokens_total` increases.

Then use the following Amazon CloudWatch metrics to confirm that the inference engine uses the cluster. These metrics apply to every transport:
+ `CurrConnections` is greater than 0. This shows that clients are connected to the node.
+ `CurrItems` increases. This shows that the node stores KV state.

Also check the metrics for your transport:
+ With the `rdma` or `blob-tcp` transport, `LargeObjectBasedCmds` is greater than 0. This shows that LMCache sends large object commands.
+ With the `rdma` transport, `EFABytesIn` and `EFABytesOut` are greater than 0. This shows that data moves over EFA.
+ With the `tcp` transport, `SetTypeCmds` and `GetTypeCmds` are greater than 0, and `NetworkBytesIn` and `NetworkBytesOut` are greater than 0. This shows that LMCache writes and reads KV state over TCP.
+ With the `rdma` transport, the RDMA error counters in `INFO largeobj` stay at 0. If they don't, check the security group rules and the Availability Zone.

For more information, see [Monitoring distributed KV caching](distributed-kv-caching-monitoring.md).

## Next steps
<a name="distributed-kv-caching-getting-started.next-steps"></a>
+ [Configuring distributed KV caching](distributed-kv-caching-configuration.md)
+ [Security in distributed KV caching](distributed-kv-caching-security.md)
+ [Monitoring distributed KV caching](distributed-kv-caching-monitoring.md)
+ [Troubleshooting distributed KV caching](distributed-kv-caching-troubleshooting.md)
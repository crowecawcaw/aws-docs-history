

# Large object module reference for distributed KV caching

A large object is a binary value that a node keeps in dynamic random-access memory (DRAM) and on local Non-Volatile Memory Express (NVMe) storage. Distributed key-value (KV) caching stores KV cache blocks as large objects when LMCache uses the `rdma` or `blob-tcp` transport. For the size limits, see [Size limits](distributed-kv-caching-limits.md#distributed-kv-caching-limits.sizes).

This page describes the large object data type, its commands, and the limits of the module. For the cluster requirements and setup, see [Distributed KV caching](distributed-kv-caching.md).

**Topics**
+ [Large object data type overview](#large-objects-datatype)
+ [Large object commands overview](#large-objects-commands)
+ [Transactions and scripts](#large-objects-transactions)
+ [Core commands on large object keys](#large-objects-core-commands)
+ [Large object ACLs](#large-objects-acl)
+ [Module configuration](#large-objects-configuration)

## Large object data type overview
<a name="large-objects-datatype"></a>

The main source of documentation for large objects is the [large object documentation](https://valkey.io/topics/large-object/) on the valkey.io website. The valkey.io website has the following pages:
+ [Large object overview](https://valkey.io/topics/large-object/) on the valkey.io website: key concepts, transports, supported commands, and limitations such as cluster mode, replication, and core commands on large object keys
+ [Getting started](https://valkey.io/topics/large-object-getting-started/) on the valkey.io website: first commands, and errors at load time and run time
+ [Configuration](https://valkey.io/topics/large-object-configuration/) on the valkey.io website: module configs, memory and eviction, ACLs, security, what to watch, and INFO fields
+ [RDMA](https://valkey.io/topics/large-object-rdma/) on the valkey.io website: the session model, memory region triples, CRC behavior, and RDMA errors
+ [Use cases](https://valkey.io/topics/large-object-use-cases/) on the valkey.io website: large language model (LLM) inference KV caches, model artifacts, and examples over TCP and RDMA

## Large object commands overview
<a name="large-objects-commands"></a>

Distributed KV caching with ElastiCache uses the Valkey [large object module](https://github.com/valkey-io/valkey-large-object). The large object module adds the following commands. The `BLOB.TCP_*` commands send data inline over the Transport Layer Security (TLS) connection. The `BLOB.RDMA_*` commands move data with remote direct memory access (RDMA) over Elastic Fabric Adapter (EFA). Each command name links to its page on the valkey.io website.


**Large object commands**  

| Name | Description | 
| --- | --- | 
| [BLOB.INFO](https://valkey.io/commands/blob.info/) | Returns the length, CRC32C checksum, and storage tier of a large object. | 
| [BLOB.RDMA\_GET](https://valkey.io/commands/blob.rdma_get/) | Writes a large object into client memory regions with RDMA. | 
| [BLOB.RDMA\_HELLO](https://valkey.io/commands/blob.rdma_hello/) | Opens an RDMA session between the connection and the server. | 
| [BLOB.RDMA\_SET](https://valkey.io/commands/blob.rdma_set/) | Stores a large object, read from client memory regions with RDMA. | 
| [BLOB.TCP\_GET](https://valkey.io/commands/blob.tcp_get/) | Returns a large object, sent inline over the connection. | 
| [BLOB.TCP\_SET](https://valkey.io/commands/blob.tcp_set/) | Stores a large object, sent inline over the connection. | 

For the full syntax, replies, and errors of each command, see the command page on the valkey.io website, or the [large object command list](https://valkey.io/commands/#large-object) on the valkey.io website.

## Transactions and scripts
<a name="large-objects-transactions"></a>

`BLOB.TCP_SET`, `BLOB.TCP_GET`, `BLOB.RDMA_SET`, and `BLOB.RDMA_GET` can't run inside a `MULTI`/`EXEC` block, a Lua script, or a function. For more information, see [Core commands on large object keys](https://valkey.io/topics/large-object/#core-commands-on-large-object-keys) on the valkey.io website.

## Core commands on large object keys
<a name="large-objects-core-commands"></a>

`DUMP` returns a value without the object data, and `RESTORE` of that value fails with `ERR Bad data format`, so `MIGRATE` fails on large object keys. For information about how `DEL`, `EXPIRE`, `COPY`, `RENAME`, `TYPE`, and other core commands behave, see [Core commands on large object keys](https://valkey.io/topics/large-object/#core-commands-on-large-object-keys) on the valkey.io website.

## Large object ACLs
<a name="large-objects-acl"></a>

Similar to the existing per-data-type access control list (ACL) categories, such as `@string` and `@hash`, the `@largeobj` category makes it easier to manage access to large object commands and data. No other Valkey or Redis OSS commands are in the `@largeobj` category.

The large object commands are also in four existing ACL categories: `@read`, `@write`, `@fast`, and `@connection`. The following table shows the categories of each large object command.


**Large object ACL categories**  

| Large object command | @read | @write | @fast | @connection | @largeobj | 
| --- | --- | --- | --- | --- | --- | 
| BLOB.TCP\_GET | Yes | No | Yes | No | Yes | 
| BLOB.TCP\_SET | No | Yes | Yes | No | Yes | 
| BLOB.RDMA\_HELLO | No | No | Yes | Yes | Yes | 
| BLOB.RDMA\_GET | Yes | No | Yes | No | Yes | 
| BLOB.RDMA\_SET | No | Yes | Yes | No | Yes | 
| BLOB.INFO | Yes | No | Yes | No | Yes | 

To create role-based access control (RBAC) users and user groups, see [Role-Based Access Control (RBAC)](Clusters.RBAC.md). For example access strings, see [ACL](https://valkey.io/topics/large-object-configuration/#acl) on the valkey.io website.

## Module configuration
<a name="large-objects-configuration"></a>

ElastiCache manages the settings of the large object module. For the parameters that you can change, see [Parameters](distributed-kv-caching-configuration.md#distributed-kv-caching-configuration.parameters).
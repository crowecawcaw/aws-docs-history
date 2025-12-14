# Supported and restricted Valkey, Memcached, and Redis OSS commands

## Supported Valkey and Redis OSS commands

**Supported Valkey and Redis OSS commands**

The following Valkey and Redis OSS commands are supported by serverless caches.
In addition to these commands, these [Supported Valkey and Redis OSS commands](json-list-commands.md "json-list-commands.md") are also supported.

For information on Bloom Filter commands see [Bloom filter commands](BloomFilters.md#SupportedCommandsBloom "BloomFilters.md#SupportedCommandsBloom")

**Bitmap Commands**

- `BITCOUNT`

Counts the number of set bits (population counting) in a string.

[Learn more](https://valkey.io/commands/bitcount/ "https://valkey.io/commands/bitcount/")

- `BITFIELD`

Performs arbitrary bitfield integer operations on strings.

[Learn more](https://valkey.io/commands/bitfield/ "https://valkey.io/commands/bitfield/")

- `BITFIELD_RO`

Performs arbitrary read-only bitfield integer operations on strings.

[Learn more](https://valkey.io/commands/bitfield_ro/ "https://valkey.io/commands/bitfield_ro/")

- `BITOP`

Performs bitwise operations on multiple strings, and stores the result.

[Learn more](https://valkey.io/commands/bitop/ "https://valkey.io/commands/bitop/")

- `BITPOS`

Finds the first set (1) or clear (0) bit in a string.

[Learn more](https://valkey.io/commands/bitpos/ "https://valkey.io/commands/bitpos/")

- `GETBIT`

Returns a bit value by offset.

[Learn more](https://valkey.io/commands/getbit/ "https://valkey.io/commands/getbit/")

- `SETBIT`

Sets or clears the bit at offset of the string value. Creates the key if it doesn't exist.

[Learn more](https://valkey.io/commands/setbit/ "https://valkey.io/commands/setbit/")

**Cluster Management Commands**

- `CLUSTER COUNTKEYSINSLOT`

Returns the number of keys in a hash slot.

[Learn more](https://valkey.io/commands/cluster-countkeysinslot/ "https://valkey.io/commands/cluster-countkeysinslot/")

- `CLUSTER GETKEYSINSLOT`

Returns the key names in a hash slot.

[Learn more](https://valkey.io/commands/cluster-getkeysinslot/ "https://valkey.io/commands/cluster-getkeysinslot/")

- `CLUSTER INFO`

Returns information about the state of a node.
In a serverless cache, returns state about the single virtual “shard” exposed to the client.

[Learn more](https://valkey.io/commands/cluster-info/ "https://valkey.io/commands/cluster-info/")

- `CLUSTER KEYSLOT`

Returns the hash slot for a key.

[Learn more](https://valkey.io/commands/cluster-keyslot/ "https://valkey.io/commands/cluster-keyslot/")

- `CLUSTER MYID`

Returns the ID of a node.
In a serverless cache, returns state about the single virtual “shard” exposed to the client.

[Learn more](https://valkey.io/commands/cluster-myid/ "https://valkey.io/commands/cluster-myid/")

- `CLUSTER NODES`

Returns the cluster configuration for a node.
In a serverless cache, returns state about the single virtual “shard” exposed to the client.

[Learn more](https://valkey.io/commands/cluster-nodes/ "https://valkey.io/commands/cluster-nodes/")

- `CLUSTER REPLICAS`

Lists the replica nodes of a master node.
In a serverless cache, returns state about the single virtual “shard” exposed to the client.

[Learn more](https://valkey.io/commands/cluster-replicas/ "https://valkey.io/commands/cluster-replicas/")

- `CLUSTER SHARDS`

Returns the mapping of cluster slots to shards.
In a serverless cache, returns state about the single virtual “shard” exposed to the client.

[Learn more](https://valkey.io/commands/cluster-shards/ "https://valkey.io/commands/cluster-shards/")

- `CLUSTER SLOTS`

Returns the mapping of cluster slots to nodes.
In a serverless cache, returns state about the single virtual “shard” exposed to the client.

[Learn more](https://valkey.io/commands/cluster-slots/ "https://valkey.io/commands/cluster-slots/")

- `CLUSTER SLOT-STATS`

Allows tracking of per slot metrics for key count, CPU utilization, network bytes in, and network bytes out.

[Learn more](https://valkey.io/commands/cluster-slot-stats/ "https://valkey.io/commands/cluster-slot-stats/")

- `READONLY`

Enables read-only queries for a connection to a Valkey or Redis OSS Cluster replica node.

[Learn more](https://valkey.io/commands/readonly/ "https://valkey.io/commands/readonly/")

- `READWRITE`

Enables read-write queries for a connection to a Valkey or Redis OSS Cluster replica node.

[Learn more](https://valkey.io/commands/readwrite/ "https://valkey.io/commands/readwrite/")

- `SCRIPT SHOW`

Returns the original source code of a script in the script cache.

[Learn more](https://valkey.io/commands/script-show/ "https://valkey.io/commands/script-show/")

**Connection Management Commands**

- `AUTH`

Authenticates the connection.

[Learn more](https://valkey.io/commands/auth/ "https://valkey.io/commands/auth/")

- `CLIENT GETNAME`

Returns the name of the connection.

[Learn more](https://valkey.io/commands/client-getname/ "https://valkey.io/commands/client-getname/")

- `CLIENT REPLY`

Instructs the server whether to reply to commands.

[Learn more](https://valkey.io/commands/client-reply/ "https://valkey.io/commands/client-reply/")

- `CLIENT SETNAME`

Sets the connection name.

[Learn more](https://valkey.io/commands/client-setname/ "https://valkey.io/commands/client-setname/")

- `ECHO`

Returns the given string.

[Learn more](https://valkey.io/commands/echo/ "https://valkey.io/commands/echo/")

- `HELLO`

Handshakes with the Valkey or Redis OSS server.

[Learn more](https://valkey.io/commands/hello/ "https://valkey.io/commands/hello/")

- `PING`

Returns the server's liveliness response.

[Learn more](https://valkey.io/commands/ping/ "https://valkey.io/commands/ping/")

- `QUIT`

Closes the connection.

[Learn more](https://valkey.io/commands/quit/ "https://valkey.io/commands/quit/")

- `RESET`

Resets the connection.

[Learn more](https://valkey.io/commands/reset/ "https://valkey.io/commands/reset/")

- `SELECT`

Changes the selected database.

[Learn more](https://valkey.io/commands/select/ "https://valkey.io/commands/select/")

**Generic Commands**

- `COPY`

Copies the value of a key to a new key.

[Learn more](https://valkey.io/commands/copy/ "https://valkey.io/commands/copy/")

- `DEL`

Deletes one or more keys.

[Learn more](https://valkey.io/commands/del/ "https://valkey.io/commands/del/")

- `DUMP`

Returns a serialized representation of the value stored at a key.

[Learn more](https://valkey.io/commands/dump/ "https://valkey.io/commands/dump/")

- `EXISTS`

Determines whether one or more keys exist.

[Learn more](https://valkey.io/commands/exists/ "https://valkey.io/commands/exists/")

- `EXPIRE`

Sets the expiration time of a key in seconds.

[Learn more](https://valkey.io/commands/expire/ "https://valkey.io/commands/expire/")

- `EXPIREAT`

Sets the expiration time of a key to a Unix timestamp.

[Learn more](https://valkey.io/commands/expireat/ "https://valkey.io/commands/expireat/")

- `EXPIRETIME`

Returns the expiration time of a key as a Unix timestamp.

[Learn more](https://valkey.io/commands/expiretime/ "https://valkey.io/commands/expiretime/")

- `PERSIST`

Removes the expiration time of a key.

[Learn more](https://valkey.io/commands/persist/ "https://valkey.io/commands/persist/")

- `PEXPIRE`

Sets the expiration time of a key in milliseconds.

[Learn more](https://valkey.io/commands/pexpire/ "https://valkey.io/commands/pexpire/")

- `PEXPIREAT`

Sets the expiration time of a key to a Unix milliseconds timestamp.

[Learn more](https://valkey.io/commands/pexpireat/ "https://valkey.io/commands/pexpireat/")

- `PEXPIRETIME`

Returns the expiration time of a key as a Unix milliseconds timestamp.

[Learn more](https://valkey.io/commands/pexpiretime/ "https://valkey.io/commands/pexpiretime/")

- `PTTL`

Returns the expiration time in milliseconds of a key.

[Learn more](https://valkey.io/commands/pttl/ "https://valkey.io/commands/pttl/")

- `RANDOMKEY`

Returns a random key name from the database.

[Learn more](https://valkey.io/commands/randomkey/ "https://valkey.io/commands/randomkey/")

- `RENAME`

Renames a key and overwrites the destination.

[Learn more](https://valkey.io/commands/rename/ "https://valkey.io/commands/rename/")

- `RENAMENX`

Renames a key only when the target key name doesn't exist.

[Learn more](https://valkey.io/commands/renamenx/ "https://valkey.io/commands/renamenx/")

- `RESTORE`

Creates a key from the serialized representation of a value.

[Learn more](https://valkey.io/commands/restore/ "https://valkey.io/commands/restore/")

- `SCAN`

Iterates over the key names in the database.

[Learn more](https://valkey.io/commands/scan/ "https://valkey.io/commands/scan/")

- `SORT`

Sorts the elements in a list, a set, or a sorted set, optionally storing the result.

[Learn more](https://valkey.io/commands/sort/ "https://valkey.io/commands/sort/")

- `SORT_RO`

Returns the sorted elements of a list, a set, or a sorted set.

[Learn more](https://valkey.io/commands/sort_ro/ "https://valkey.io/commands/sort_ro/")

- `TOUCH`

Returns the number of existing keys out of those specified after updating the time they were last accessed.

[Learn more](https://valkey.io/commands/touch/ "https://valkey.io/commands/touch/")

- `TTL`

Returns the expiration time in seconds of a key.

[Learn more](https://valkey.io/commands/ttl/ "https://valkey.io/commands/ttl/")

- `TYPE`

Determines the type of value stored at a key.

[Learn more](https://valkey.io/commands/type/ "https://valkey.io/commands/type/")

- `UNLINK`

Asynchronously deletes one or more keys.

[Learn more](https://valkey.io/commands/unlink/ "https://valkey.io/commands/unlink/")

**Geospatial Commands**

- `GEOADD`

Adds one or more members to a geospatial index. The key is created if it doesn't exist.

[Learn more](https://valkey.io/commands/geoadd/ "https://valkey.io/commands/geoadd/")

- `GEODIST`

Returns the distance between two members of a geospatial index.

[Learn more](https://valkey.io/commands/geodist/ "https://valkey.io/commands/geodist/")

- `GEOHASH`

Returns members from a geospatial index as geohash strings.

[Learn more](https://valkey.io/commands/geohash/ "https://valkey.io/commands/geohash/")

- `GEOPOS`

Returns the longitude and latitude of members from a geospatial index.

[Learn more](https://valkey.io/commands/geopos/ "https://valkey.io/commands/geopos/")

- `GEORADIUS`

Queries a geospatial index for members within a distance from a coordinate, optionally stores the result.

[Learn more](https://valkey.io/commands/georadius/ "https://valkey.io/commands/georadius/")

- `GEORADIUS_RO`

Returns members from a geospatial index that are within a distance from a coordinate.

[Learn more](https://valkey.io/commands/georadius_ro/ "https://valkey.io/commands/georadius_ro/")

- `GEORADIUSBYMEMBER`

Queries a geospatial index for members within a distance from a member, optionally stores the result.

[Learn more](https://valkey.io/commands/georadiusbymember/ "https://valkey.io/commands/georadiusbymember/")

- `GEORADIUSBYMEMBER_RO`

Returns members from a geospatial index that are within a distance from a member.

[Learn more](https://valkey.io/commands/georadiusbymember_ro/ "https://valkey.io/commands/georadiusbymember_ro/")

- `GEOSEARCH`

Queries a geospatial index for members inside an area of a box or a circle.

[Learn more](https://valkey.io/commands/geosearch/ "https://valkey.io/commands/geosearch/")

- `GEOSEARCHSTORE`

Queries a geospatial index for members inside an area of a box or a circle, optionally stores the result.

[Learn more](https://valkey.io/commands/geosearchstore/ "https://valkey.io/commands/geosearchstore/")

**Hash Commands**

- `HDEL`

Deletes one or more fields and their values from a hash. Deletes the hash if no fields remain.

[Learn more](https://valkey.io/commands/hdel/ "https://valkey.io/commands/hdel/")

- `HEXISTS`

Determines whether a field exists in a hash.

[Learn more](https://valkey.io/commands/hexists/ "https://valkey.io/commands/hexists/")

- `HGET`

Returns the value of a field in a hash.

[Learn more](https://valkey.io/commands/hget/ "https://valkey.io/commands/hget/")

- `HGETALL`

Returns all fields and values in a hash.

[Learn more](https://valkey.io/commands/hgetall/ "https://valkey.io/commands/hgetall/")

- `HINCRBY`

Increments the integer value of a field in a hash by a number. Uses 0 as initial value if the field doesn't exist.

[Learn more](https://valkey.io/commands/hincrby/ "https://valkey.io/commands/hincrby/")

- `HINCRBYFLOAT`

Increments the floating point value of a field by a number. Uses 0 as initial value if the field doesn't exist.

[Learn more](https://valkey.io/commands/hincrbyfloat/ "https://valkey.io/commands/hincrbyfloat/")

- `HKEYS`

Returns all fields in a hash.

[Learn more](https://valkey.io/commands/hkeys/ "https://valkey.io/commands/hkeys/")

- `HLEN`

Returns the number of fields in a hash.

[Learn more](https://valkey.io/commands/hlen/ "https://valkey.io/commands/hlen/")

- `HMGET`

Returns the values of all fields in a hash.

[Learn more](https://valkey.io/commands/hmget/ "https://valkey.io/commands/hmget/")

- `HMSET`

Sets the values of multiple fields.

[Learn more](https://valkey.io/commands/hmset/ "https://valkey.io/commands/hmset/")

- `HRANDFIELD`

Returns one or more random fields from a hash.

[Learn more](https://valkey.io/commands/hrandfield/ "https://valkey.io/commands/hrandfield/")

- `HSCAN`

Iterates over fields and values of a hash.

[Learn more](https://valkey.io/commands/hscan/ "https://valkey.io/commands/hscan/")

- `HSET`

Creates or modifies the value of a field in a hash.

[Learn more](https://valkey.io/commands/hset/ "https://valkey.io/commands/hset/")

- `HSETNX`

Sets the value of a field in a hash only when the field doesn't exist.

[Learn more](https://valkey.io/commands/hsetnx/ "https://valkey.io/commands/hsetnx/")

- `HSTRLEN`

Returns the length of the value of a field.

[Learn more](https://valkey.io/commands/hstrlen/ "https://valkey.io/commands/hstrlen/")

- `HVALS`

Returns all values in a hash.

[Learn more](https://valkey.io/commands/hvals/ "https://valkey.io/commands/hvals/")

**HyperLogLog Commands**

- `PFADD`

Adds elements to a HyperLogLog key. Creates the key if it doesn't exist.

[Learn more](https://valkey.io/commands/pfadd/ "https://valkey.io/commands/pfadd/")

- `PFCOUNT`

Returns the approximated cardinality of the set(s) observed by the HyperLogLog key(s).

[Learn more](https://valkey.io/commands/pfcount/ "https://valkey.io/commands/pfcount/")

- `PFMERGE`

Merges one or more HyperLogLog values into a single key.

[Learn more](https://valkey.io/commands/pfmerge/ "https://valkey.io/commands/pfmerge/")

**List Commands**

- `BLMOVE`

Pops an element from a list, pushes it to another list and returns it.
Blocks until an element is available otherwise. Deletes the list if the last element was moved.

[Learn more](https://valkey.io/commands/blmove/ "https://valkey.io/commands/blmove/")

- `BLMPOP`

Pops the first element from one of multiple lists. Blocks until an element
is available otherwise. Deletes the list if the last element was popped.

[Learn more](https://valkey.io/commands/blmpop/ "https://valkey.io/commands/blmpop/")

- `BLPOP`

Removes and returns the first element in a list. Blocks until an element is
available otherwise. Deletes the list if the last element was popped.

[Learn more](https://valkey.io/commands/blpop/ "https://valkey.io/commands/blpop/")

- `BRPOP`

Removes and returns the last element in a list. Blocks until an element is available otherwise. Deletes the list if the last element was popped.

[Learn more](https://valkey.io/commands/brpop/ "https://valkey.io/commands/brpop/")

- `BRPOPLPUSH`

Pops an element from a list, pushes it to another list and returns it. Block until an element is available otherwise. Deletes the list if the last element was popped.

[Learn more](https://valkey.io/commands/brpoplpush/ "https://valkey.io/commands/brpoplpush/")

- `LINDEX`

Returns an element from a list by its index.

[Learn more](https://valkey.io/commands/lindex/ "https://valkey.io/commands/lindex/")

- `LINSERT`

Inserts an element before or after another element in a list.

[Learn more](https://valkey.io/commands/linsert/ "https://valkey.io/commands/linsert/")

- `LLEN`

Returns the length of a list.

[Learn more](https://valkey.io/commands/llen/ "https://valkey.io/commands/llen/")

- `LMOVE`

Returns an element after popping it from one list and pushing it to another. Deletes the list if the last element was moved.

[Learn more](https://valkey.io/commands/lmove/ "https://valkey.io/commands/lmove/")

- `LMPOP`

Returns multiple elements from a list after removing them. Deletes the list if the last element was popped.

[Learn more](https://valkey.io/commands/lmpop/ "https://valkey.io/commands/lmpop/")

- `LPOP`

Returns the first elements in a list after removing it. Deletes the list if the last element was popped.

[Learn more](https://valkey.io/commands/lpop/ "https://valkey.io/commands/lpop/")

- `LPOS`

Returns the index of matching elements in a list.

[Learn more](https://valkey.io/commands/lpos/ "https://valkey.io/commands/lpos/")

- `LPUSH`

Prepends one or more elements to a list. Creates the key if it doesn't exist.

[Learn more](https://valkey.io/commands/lpush/ "https://valkey.io/commands/lpush/")

- `LPUSHX`

Prepends one or more elements to a list only when the list exists.

[Learn more](https://valkey.io/commands/lpushx/ "https://valkey.io/commands/lpushx/")

- `LRANGE`

Returns a range of elements from a list.

[Learn more](https://valkey.io/commands/lrange/ "https://valkey.io/commands/lrange/")

- `LREM`

Removes elements from a list. Deletes the list if the last element was removed.

[Learn more](https://valkey.io/commands/lrem/ "https://valkey.io/commands/lrem/")

- `LSET`

Sets the value of an element in a list by its index.

[Learn more](https://valkey.io/commands/lset/ "https://valkey.io/commands/lset/")

- `LTRIM`

Removes elements from both ends a list. Deletes the list if all elements were trimmed.

[Learn more](https://valkey.io/commands/ltrim/ "https://valkey.io/commands/ltrim/")

- `RPOP`

Returns and removes the last elements of a list. Deletes the list if the last element was popped.

[Learn more](https://valkey.io/commands/rpop/ "https://valkey.io/commands/rpop/")

- `RPOPLPUSH`

Returns the last element of a list after removing and pushing it to another list. Deletes the list if the last element was popped.

[Learn more](https://valkey.io/commands/rpoplpush/ "https://valkey.io/commands/rpoplpush/")

- `RPUSH`

Appends one or more elements to a list. Creates the key if it doesn't exist.

[Learn more](https://valkey.io/commands/rpush/ "https://valkey.io/commands/rpush/")

- `RPUSHX`

Appends an element to a list only when the list exists.

[Learn more](https://valkey.io/commands/rpushx/ "https://valkey.io/commands/rpushx/")

**Pub/Sub Commands**

###### Note

PUBSUB commands internally use sharded PUBSUB, so channel names will be mixed.

- `PUBLISH`

Posts a message to a channel.

[Learn more](https://valkey.io/commands/publish/ "https://valkey.io/commands/publish/")

- `PUBSUB CHANNELS`

Returns the active channels.

[Learn more](https://valkey.io/commands/pubsub-channels/ "https://valkey.io/commands/pubsub-channels/")

- `PUBSUB NUMSUB`

Returns a count of subscribers to channels.

[Learn more](https://valkey.io/commands/pubsub-numsub/ "https://valkey.io/commands/pubsub-numsub/")

- `PUBSUB SHARDCHANNELS`

Returns the active shard channels.

[Learn more](https://valkey.io/commands/pubsub-shardchannels/ "https://valkey.io/commands/pubsub-shardchannels/")

- `PUBSUB SHARDNUMSUB`

Returns the count of subscribers of shard channels.

[Learn more](https://valkey.io/commands/pubsub-shardnumsub/ "https://valkey.io/commands/pubsub-shardnumsub/")

- `SPUBLISH`

Post a message to a shard channel

[Learn more](https://valkey.io/commands/spublish/ "https://valkey.io/commands/spublish/")

- `SSUBSCRIBE`

Listens for messages published to shard channels.

[Learn more](https://valkey.io/commands/ssubscribe/ "https://valkey.io/commands/ssubscribe/")

- `SUBSCRIBE`

Listens for messages published to channels.

[Learn more](https://valkey.io/commands/subscribe/ "https://valkey.io/commands/subscribe/")

- `SUNSUBSCRIBE`

Stops listening to messages posted to shard channels.

[Learn more](https://valkey.io/commands/sunsubscribe/ "https://valkey.io/commands/sunsubscribe/")

- `UNSUBSCRIBE`

Stops listening to messages posted to channels.

[Learn more](https://valkey.io/commands/unsubscribe/ "https://valkey.io/commands/unsubscribe/")

**Scripting Commands**

- `EVAL`

Executes a server-side Lua script.

[Learn more](https://valkey.io/commands/eval/ "https://valkey.io/commands/eval/")

- `EVAL_RO`

Executes a read-only server-side Lua script.

[Learn more](https://valkey.io/commands/eval_ro/ "https://valkey.io/commands/eval_ro/")

- `EVALSHA`

Executes a server-side Lua script by SHA1 digest.

[Learn more](https://valkey.io/commands/evalsha/ "https://valkey.io/commands/evalsha/")

- `EVALSHA_RO`

Executes a read-only server-side Lua script by SHA1 digest.

[Learn more](https://valkey.io/commands/evalsha_ro/ "https://valkey.io/commands/evalsha_ro/")

- `SCRIPT EXISTS`

Determines whether server-side Lua scripts exist in the script cache.

[Learn more](https://valkey.io/commands/script-exists/ "https://valkey.io/commands/script-exists/")

- `SCRIPT FLUSH`

Currently a no-op, script cache is managed by the service.

[Learn more](https://valkey.io/commands/script-flush/ "https://valkey.io/commands/script-flush/")

- `SCRIPT LOAD`

Loads a server-side Lua script to the script cache.

[Learn more](https://valkey.io/commands/script-load/ "https://valkey.io/commands/script-load/")

**Server Management Commands**

###### Note

When using node-based ElastiCache clusters for Valkey and Redis OSS, flush commands must be sent to every primary by the client to flush all keys. ElastiCache Serverless for Valkey and Redis OSS works differently, because it abstracts away the underlying cluster topology. The result is that in ElastiCache Serverless, `FLUSHDB` and `FLUSHALL` commands will always flush all keys across the cluster. For this reason, flush commands cannot be included inside a Serverless transaction.

- `ACL CAT`

Lists the ACL categories, or the commands inside a category.

[Learn more](https://valkey.io/commands/acl-cat/ "https://valkey.io/commands/acl-cat/")

- `ACL GENPASS`

Generates a pseudorandom, secure password that can be used to identify ACL users.

[Learn more](https://valkey.io/commands/acl-genpass/ "https://valkey.io/commands/acl-genpass/")

- `ACL GETUSER`

Lists the ACL rules of a user.

[Learn more](https://valkey.io/commands/acl-getuser/ "https://valkey.io/commands/acl-getuser/")

- `ACL LIST`

Dumps the effective rules in ACL file format.

[Learn more](https://valkey.io/commands/acl-list/ "https://valkey.io/commands/acl-list/")

- `ACL USERS`

Lists all ACL users.

[Learn more](https://valkey.io/commands/acl-users/ "https://valkey.io/commands/acl-users/")

- `ACL WHOAMI`

Returns the authenticated username of the current connection.

[Learn more](https://valkey.io/commands/acl-whoami/ "https://valkey.io/commands/acl-whoami/")

- `DBSIZE`

Return the number of keys in the currently-selected database.
This operation is not guaranteed to be atomic across all slots.

[Learn more](https://valkey.io/commands/dbsize/ "https://valkey.io/commands/dbsize/")

- `COMMAND`

Returns detailed information about all commands.

[Learn more](https://valkey.io/commands/command/ "https://valkey.io/commands/command/")

- `COMMAND COUNT`

Returns a count of commands.

[Learn more](https://valkey.io/commands/command-count/ "https://valkey.io/commands/command-count/")

- `COMMAND DOCS`

Returns documentary information about one, multiple or all commands.

[Learn more](https://valkey.io/commands/command-docs/ "https://valkey.io/commands/command-docs/")

- `COMMAND GETKEYS`

Extracts the key names from an arbitrary command.

[Learn more](https://valkey.io/commands/command-getkeys/ "https://valkey.io/commands/command-getkeys/")

- `COMMAND GETKEYSANDFLAGS`

Extracts the key names and access flags for an arbitrary command.

[Learn more](https://valkey.io/commands/command-getkeysandflags/ "https://valkey.io/commands/command-getkeysandflags/")

- `COMMAND INFO`

Returns information about one, multiple or all commands.

[Learn more](https://valkey.io/commands/command-info/ "https://valkey.io/commands/command-info/")

- `COMMAND LIST`

Returns a list of command names.

[Learn more](https://valkey.io/commands/command-list/ "https://valkey.io/commands/command-list/")

- `COMMANDLOG`

A container for command log commands.

[Learn more](https://valkey.io/commands/commandlog/ "https://valkey.io/commands/commandlog/")

- `COMMANDLOG GET`

Returns the specified command log's entries.

[Learn more](https://valkey.io/commands/commandlog-get/ "https://valkey.io/commands/commandlog-get/")

- `COMMANDLOG HELP`

Show helpful text about the different subcommands.

[Learn more](https://valkey.io/commands/commandlog-help/ "https://valkey.io/commands/commandlog-help/")

- `COMMANDLOG LEN`

Returns the number of entries in the specified type of command log.

[Learn more](https://valkey.io/commands/commandlog-len/ "https://valkey.io/commands/commandlog-len/")

- `COMMANDLOG RESET`

Clears all entries from the specified type of command log.

[Learn more](https://valkey.io/commands/commandlog-reset/ "https://valkey.io/commands/commandlog-reset/")

- `FLUSHALL`

Removes all keys from all databases.
This operation is not guaranteed to be atomic across all slots.

[Learn more](https://valkey.io/commands/flushall/ "https://valkey.io/commands/flushall/")

- `FLUSHDB`

Remove all keys from the current database.
This operation is not guaranteed to be atomic across all slots.

[Learn more](https://valkey.io/commands/flushdb/ "https://valkey.io/commands/flushdb/")

- `INFO`

Returns information and statistics about the server.

[Learn more](https://valkey.io/commands/info/ "https://valkey.io/commands/info/")

- `LOLWUT`

Displays computer art and the Valkey or Redis OSS version.

[Learn more](https://valkey.io/commands/lolwut/ "https://valkey.io/commands/lolwut/")

- `ROLE`

Returns the replication role.

[Learn more](https://valkey.io/commands/role/ "https://valkey.io/commands/role/")

- `TIME`

Returns the server time.

[Learn more](https://valkey.io/commands/time/ "https://valkey.io/commands/time/")

**Set Commands**

- `SADD`

Adds one or more members to a set. Creates the key if it doesn't exist.

[Learn more](https://valkey.io/commands/sadd/ "https://valkey.io/commands/sadd/")

- `SCARD`

Returns the number of members in a set.

[Learn more](https://valkey.io/commands/scard/ "https://valkey.io/commands/scard/")

- `SDIFF`

Returns the difference of multiple sets.

[Learn more](https://valkey.io/commands/sdiff/ "https://valkey.io/commands/sdiff/")

- `SDIFFSTORE`

Stores the difference of multiple sets in a key.

[Learn more](https://valkey.io/commands/sdiffstore/ "https://valkey.io/commands/sdiffstore/")

- `SINTER`

Returns the intersect of multiple sets.

[Learn more](https://valkey.io/commands/sinter/ "https://valkey.io/commands/sinter/")

- `SINTERCARD`

Returns the number of members of the intersect of multiple sets.

[Learn more](https://valkey.io/commands/sintercard/ "https://valkey.io/commands/sintercard/")

- `SINTERSTORE`

Stores the intersect of multiple sets in a key.

[Learn more](https://valkey.io/commands/sinterstore/ "https://valkey.io/commands/sinterstore/")

- `SISMEMBER`

Determines whether a member belongs to a set.

[Learn more](https://valkey.io/commands/sismember/ "https://valkey.io/commands/sismember/")

- `SMEMBERS`

Returns all members of a set.

[Learn more](https://valkey.io/commands/smembers/ "https://valkey.io/commands/smembers/")

- `SMISMEMBER`

Determines whether multiple members belong to a set.

[Learn more](https://valkey.io/commands/smismember/ "https://valkey.io/commands/smismember/")

- `SMOVE`

Moves a member from one set to another.

[Learn more](https://valkey.io/commands/smove/ "https://valkey.io/commands/smove/")

- `SPOP`

Returns one or more random members from a set after removing them. Deletes the set if the last member was popped.

[Learn more](https://valkey.io/commands/spop/ "https://valkey.io/commands/spop/")

- `SRANDMEMBER`

Get one or multiple random members from a set

[Learn more](https://valkey.io/commands/srandmember/ "https://valkey.io/commands/srandmember/")

- `SREM`

Removes one or more members from a set. Deletes the set if the last member was removed.

[Learn more](https://valkey.io/commands/srem/ "https://valkey.io/commands/srem/")

- `SSCAN`

Iterates over members of a set.

[Learn more](https://valkey.io/commands/sscan/ "https://valkey.io/commands/sscan/")

- `SUNION`

Returns the union of multiple sets.

[Learn more](https://valkey.io/commands/sunion/ "https://valkey.io/commands/sunion/")

- `SUNIONSTORE`

Stores the union of multiple sets in a key.

[Learn more](https://valkey.io/commands/sunionstore/ "https://valkey.io/commands/sunionstore/")

**Sorted Set Commands**

- `BZMPOP`

Removes and returns a member by score from one or more sorted sets.
Blocks until a member is available otherwise. Deletes the sorted set if the last element was popped.

[Learn more](https://valkey.io/commands/bzmpop/ "https://valkey.io/commands/bzmpop/")

- `BZPOPMAX`

Removes and returns the member with the highest score from one or more sorted sets. Blocks until a member available otherwise. Deletes the sorted set if the last element was popped.

[Learn more](https://valkey.io/commands/bzpopmax/ "https://valkey.io/commands/bzpopmax/")

- `BZPOPMIN`

Removes and returns the member with the lowest score from one or more sorted sets. Blocks until a member is available otherwise. Deletes the sorted set if the last element was popped.

[Learn more](https://valkey.io/commands/bzpopmin/ "https://valkey.io/commands/bzpopmin/")

- `ZADD`

Adds one or more members to a sorted set, or updates their scores. Creates the key if it doesn't exist.

[Learn more](https://valkey.io/commands/zadd/ "https://valkey.io/commands/zadd/")

- `ZCARD`

Returns the number of members in a sorted set.

[Learn more](https://valkey.io/commands/zcard/ "https://valkey.io/commands/zcard/")

- `ZCOUNT`

Returns the count of members in a sorted set that have scores within a range.

[Learn more](https://valkey.io/commands/zcount/ "https://valkey.io/commands/zcount/")

- `ZDIFF`

Returns the difference between multiple sorted sets.

[Learn more](https://valkey.io/commands/zdiff/ "https://valkey.io/commands/zdiff/")

- `ZDIFFSTORE`

Stores the difference of multiple sorted sets in a key.

[Learn more](https://valkey.io/commands/zdiffstore/ "https://valkey.io/commands/zdiffstore/")

- `ZINCRBY`

Increments the score of a member in a sorted set.

[Learn more](https://valkey.io/commands/zincrby/ "https://valkey.io/commands/zincrby/")

- `ZINTER`

Returns the intersect of multiple sorted sets.

[Learn more](https://valkey.io/commands/zinter/ "https://valkey.io/commands/zinter/")

- `ZINTERCARD`

Returns the number of members of the intersect of multiple sorted sets.

[Learn more](https://valkey.io/commands/zintercard/ "https://valkey.io/commands/zintercard/")

- `ZINTERSTORE`

Stores the intersect of multiple sorted sets in a key.

[Learn more](https://valkey.io/commands/zinterstore/ "https://valkey.io/commands/zinterstore/")

- `ZLEXCOUNT`

Returns the number of members in a sorted set within a lexicographical range.

[Learn more](https://valkey.io/commands/zlexcount/ "https://valkey.io/commands/zlexcount/")

- `ZMPOP`

Returns the highest- or lowest-scoring members from one or more sorted sets after removing them. Deletes the sorted set if the last member was popped.

[Learn more](https://valkey.io/commands/zmpop/ "https://valkey.io/commands/zmpop/")

- `ZMSCORE`

Returns the score of one or more members in a sorted set.

[Learn more](https://valkey.io/commands/zmscore/ "https://valkey.io/commands/zmscore/")

- `ZPOPMAX`

Returns the highest-scoring members from a sorted set after removing them. Deletes the sorted set if the last member was popped.

[Learn more](https://valkey.io/commands/zpopmax/ "https://valkey.io/commands/zpopmax/")

- `ZPOPMIN`

Returns the lowest-scoring members from a sorted set after removing them. Deletes the sorted set if the last member was popped.

[Learn more](https://valkey.io/commands/zpopmin/ "https://valkey.io/commands/zpopmin/")

- `ZRANDMEMBER`

Returns one or more random members from a sorted set.

[Learn more](https://valkey.io/commands/zrandmember/ "https://valkey.io/commands/zrandmember/")

- `ZRANGE`

Returns members in a sorted set within a range of indexes.

[Learn more](https://valkey.io/commands/zrange/ "https://valkey.io/commands/zrange/")

- `ZRANGEBYLEX`

Returns members in a sorted set within a lexicographical range.

[Learn more](https://valkey.io/commands/zrangebylex/ "https://valkey.io/commands/zrangebylex/")

- `ZRANGEBYSCORE`

Returns members in a sorted set within a range of scores.

[Learn more](https://valkey.io/commands/zrangebyscore/ "https://valkey.io/commands/zrangebyscore/")

- `ZRANGESTORE`

Stores a range of members from sorted set in a key.

[Learn more](https://valkey.io/commands/zrangestore/ "https://valkey.io/commands/zrangestore/")

- `ZRANK`

Returns the index of a member in a sorted set ordered by ascending scores.

[Learn more](https://valkey.io/commands/zrank/ "https://valkey.io/commands/zrank/")

- `ZREM`

Removes one or more members from a sorted set. Deletes the sorted set if all members were removed.

[Learn more](https://valkey.io/commands/zrem/ "https://valkey.io/commands/zrem/")

- `ZREMRANGEBYLEX`

Removes members in a sorted set within a lexicographical range. Deletes the sorted set if all members were removed.

[Learn more](https://valkey.io/commands/zremrangebylex/ "https://valkey.io/commands/zremrangebylex/")

- `ZREMRANGEBYRANK`

Removes members in a sorted set within a range of indexes. Deletes the sorted set if all members were removed.

[Learn more](https://valkey.io/commands/zremrangebyrank/ "https://valkey.io/commands/zremrangebyrank/")

- `ZREMRANGEBYSCORE`

Removes members in a sorted set within a range of scores. Deletes the sorted set if all members were removed.

[Learn more](https://valkey.io/commands/zremrangebyscore/ "https://valkey.io/commands/zremrangebyscore/")

- `ZREVRANGE`

Returns members in a sorted set within a range of indexes in reverse order.

[Learn more](https://valkey.io/commands/zrevrange/ "https://valkey.io/commands/zrevrange/")

- `ZREVRANGEBYLEX`

Returns members in a sorted set within a lexicographical range in reverse order.

[Learn more](https://valkey.io/commands/zrevrangebylex/ "https://valkey.io/commands/zrevrangebylex/")

- `ZREVRANGEBYSCORE`

Returns members in a sorted set within a range of scores in reverse order.

[Learn more](https://valkey.io/commands/zrevrangebyscore/ "https://valkey.io/commands/zrevrangebyscore/")

- `ZREVRANK`

Returns the index of a member in a sorted set ordered by descending scores.

[Learn more](https://valkey.io/commands/zrevrank/ "https://valkey.io/commands/zrevrank/")

- `ZSCAN`

Iterates over members and scores of a sorted set.

[Learn more](https://valkey.io/commands/zscan/ "https://valkey.io/commands/zscan/")

- `ZSCORE`

Returns the score of a member in a sorted set.

[Learn more](https://valkey.io/commands/zscore/ "https://valkey.io/commands/zscore/")

- `ZUNION`

Returns the union of multiple sorted sets.

[Learn more](https://valkey.io/commands/zunion/ "https://valkey.io/commands/zunion/")

- `ZUNIONSTORE`

Stores the union of multiple sorted sets in a key.

[Learn more](https://valkey.io/commands/zunionstore/ "https://valkey.io/commands/zunionstore/")

**Stream Commands**

- `XACK`

Returns the number of messages that were successfully acknowledged by the consumer group member of a stream.

[Learn more](https://valkey.io/commands/xack/ "https://valkey.io/commands/xack/")

- `XADD`

Appends a new message to a stream. Creates the key if it doesn't exist.

[Learn more](https://valkey.io/commands/xadd/ "https://valkey.io/commands/xadd/")

- `XAUTOCLAIM`

Changes, or acquires, ownership of messages in a consumer group, as if the messages were delivered to as consumer group member.

[Learn more](https://valkey.io/commands/xautoclaim/ "https://valkey.io/commands/xautoclaim/")

- `XCLAIM`

Changes, or acquires, ownership of a message in a consumer group, as if the message was delivered a consumer group member.

[Learn more](https://valkey.io/commands/xclaim/ "https://valkey.io/commands/xclaim/")

- `XDEL`

Returns the number of messages after removing them from a stream.

[Learn more](https://valkey.io/commands/xdel/ "https://valkey.io/commands/xdel/")

- `XGROUP CREATE`

Creates a consumer group.

[Learn more](https://valkey.io/commands/xgroup-create/ "https://valkey.io/commands/xgroup-create/")

- `XGROUP CREATECONSUMER`

Creates a consumer in a consumer group.

[Learn more](https://valkey.io/commands/xgroup-createconsumer/ "https://valkey.io/commands/xgroup-createconsumer/")

- `XGROUP DELCONSUMER`

Deletes a consumer from a consumer group.

[Learn more](https://valkey.io/commands/xgroup-delconsumer/ "https://valkey.io/commands/xgroup-delconsumer/")

- `XGROUP DESTROY`

Destroys a consumer group.

[Learn more](https://valkey.io/commands/xgroup-destroy/ "https://valkey.io/commands/xgroup-destroy/")

- `XGROUP SETID`

Sets the last-delivered ID of a consumer group.

[Learn more](https://valkey.io/commands/xgroup-setid/ "https://valkey.io/commands/xgroup-setid/")

- `XINFO CONSUMERS`

Returns a list of the consumers in a consumer group.

[Learn more](https://valkey.io/commands/xinfo-consumers/ "https://valkey.io/commands/xinfo-consumers/")

- `XINFO GROUPS`

Returns a list of the consumer groups of a stream.

[Learn more](https://valkey.io/commands/xinfo-groups/ "https://valkey.io/commands/xinfo-groups/")

- `XINFO STREAM`

Returns information about a stream.

[Learn more](https://valkey.io/commands/xinfo-stream/ "https://valkey.io/commands/xinfo-stream/")

- `XLEN`

Return the number of messages in a stream.

[Learn more](https://valkey.io/commands/xlen/ "https://valkey.io/commands/xlen/")

- `XPENDING`

Returns the information and entries from a stream consumer group's pending entries list.

[Learn more](https://valkey.io/commands/xpending/ "https://valkey.io/commands/xpending/")

- `XRANGE`

Returns the messages from a stream within a range of IDs.

[Learn more](https://valkey.io/commands/xrange/ "https://valkey.io/commands/xrange/")

- `XREAD`

Returns messages from multiple streams with IDs greater than the ones requested. Blocks until a message is available otherwise.

[Learn more](https://valkey.io/commands/xread/ "https://valkey.io/commands/xread/")

- `XREADGROUP`

Returns new or historical messages from a stream for a consumer in a group. Blocks until a message is available otherwise.

[Learn more](https://valkey.io/commands/xreadgroup/ "https://valkey.io/commands/xreadgroup/")

- `XREVRANGE`

Returns the messages from a stream within a range of IDs in reverse order.

[Learn more](https://valkey.io/commands/xrevrange/ "https://valkey.io/commands/xrevrange/")

- `XTRIM`

Deletes messages from the beginning of a stream.

[Learn more](https://valkey.io/commands/xtrim/ "https://valkey.io/commands/xtrim/")

**String Commands**

- `APPEND`

Appends a string to the value of a key. Creates the key if it doesn't exist.

[Learn more](https://valkey.io/commands/append/ "https://valkey.io/commands/append/")

- `DECR`

Decrements the integer value of a key by one. Uses 0 as initial value if the key doesn't exist.

[Learn more](https://valkey.io/commands/decr/ "https://valkey.io/commands/decr/")

- `DECRBY`

Decrements a number from the integer value of a key. Uses 0 as initial value if the key doesn't exist.

[Learn more](https://valkey.io/commands/decrby/ "https://valkey.io/commands/decrby/")

- `GET`

Returns the string value of a key.

[Learn more](https://valkey.io/commands/get/ "https://valkey.io/commands/get/")

- `GETDEL`

Returns the string value of a key after deleting the key.

[Learn more](https://valkey.io/commands/getdel/ "https://valkey.io/commands/getdel/")

- `GETEX`

Returns the string value of a key after setting its expiration time.

[Learn more](https://valkey.io/commands/getex/ "https://valkey.io/commands/getex/")

- `GETRANGE`

Returns a substring of the string stored at a key.

[Learn more](https://valkey.io/commands/getrange/ "https://valkey.io/commands/getrange/")

- `GETSET`

Returns the previous string value of a key after setting it to a new value.

[Learn more](https://valkey.io/commands/getset/ "https://valkey.io/commands/getset/")

- `INCR`

Increments the integer value of a key by one. Uses 0 as initial value if the key doesn't exist.

[Learn more](https://valkey.io/commands/incr/ "https://valkey.io/commands/incr/")

- `INCRBY`

Increments the integer value of a key by a number. Uses 0 as initial value if the key doesn't exist.

[Learn more](https://valkey.io/commands/incrby/ "https://valkey.io/commands/incrby/")

- `INCRBYFLOAT`

Increment the floating point value of a key by a number. Uses 0 as initial value if the key doesn't exist.

[Learn more](https://valkey.io/commands/incrbyfloat/ "https://valkey.io/commands/incrbyfloat/")

- `LCS`

Finds the longest common substring.

[Learn more](https://valkey.io/commands/lcs/ "https://valkey.io/commands/lcs/")

- `MGET`

Atomically returns the string values of one or more keys.

[Learn more](https://valkey.io/commands/mget/ "https://valkey.io/commands/mget/")

- `MSET`

Atomically creates or modifies the string values of one or more keys.

[Learn more](https://valkey.io/commands/mset/ "https://valkey.io/commands/mset/")

- `MSETNX`

Atomically modifies the string values of one or more keys only when all keys don't exist.

[Learn more](https://valkey.io/commands/msetnx/ "https://valkey.io/commands/msetnx/")

- `PSETEX`

Sets both string value and expiration time in milliseconds of a key. The key is created if it doesn't exist.

[Learn more](https://valkey.io/commands/psetex/ "https://valkey.io/commands/psetex/")

- `SET`

Sets the string value of a key, ignoring its type. The key is created if it doesn't exist.

[Learn more](https://valkey.io/commands/set/ "https://valkey.io/commands/set/")

- `SETEX`

Sets the string value and expiration time of a key. Creates the key if it doesn't exist.

[Learn more](https://valkey.io/commands/setex/ "https://valkey.io/commands/setex/")

- `SETNX`

Set the string value of a key only when the key doesn't exist.

[Learn more](https://valkey.io/commands/setnx/ "https://valkey.io/commands/setnx/")

- `SETRANGE`

Overwrites a part of a string value with another by an offset. Creates the key if it doesn't exist.

[Learn more](https://valkey.io/commands/setrange/ "https://valkey.io/commands/setrange/")

- `STRLEN`

Returns the length of a string value.

[Learn more](https://valkey.io/commands/strlen/ "https://valkey.io/commands/strlen/")

- `SUBSTR`

Returns a substring from a string value.

[Learn more](https://valkey.io/commands/substr/ "https://valkey.io/commands/substr/")

**Transaction Commands**

- `DISCARD`

Discards a transaction.

[Learn more](https://valkey.io/commands/discard/ "https://valkey.io/commands/discard/")

- `EXEC`

Executes all commands in a transaction.

[Learn more](https://valkey.io/commands/exec/ "https://valkey.io/commands/exec/")

- `MULTI`

Starts a transaction.

[Learn more](https://valkey.io/commands/multi/ "https://valkey.io/commands/multi/")

## Restricted Valkey and Redis OSS commands

To deliver a managed service experience, ElastiCache restricts access to certain cache
engine-specific commands that require advanced privileges. For caches running
Redis OSS, the following commands are unavailable:

- `acl setuser`
- `acl load`
- `acl save`
- `acl deluser`
- `bgrewriteaof`
- `bgsave`
- `cluster addslot`
- `cluster addslotsrange`
- `cluster bumpepoch`
- `cluster delslot`
- `cluster delslotsrange`
- `cluster failover`
- `cluster flushslots`
- `cluster forget`
- `cluster links`
- `cluster meet`
- `cluster setslot`
- `config`
- `debug`
- `migrate`
- `psync`
- `replicaof`
- `save`
- `slaveof`
- `shutdown`
- `sync`

In addition, the following commands are unavailable for serverless caches:

- `acl log`
- `client caching`
- `client getredir`
- `client id`
- `client info`
- `client kill`
- `client list`
- `client no-evict`
- `client pause`
- `client tracking`
- `client trackinginfo`
- `client unblock`
- `client unpause`
- `cluster count-failure-reports`
- `commandlog`
- `commandlog get`
- `commandlog help`
- `commandlog len`
- `commandlog reset`
- `fcall`
- `fcall_ro`
- `function`
- `function delete`
- `function dump`
- `function flush`
- `function help`
- `function kill`
- `function list`
- `function load`
- `function restore`
- `function stats`
- `keys`
- `lastsave`
- `latency`
- `latency doctor`
- `latency graph`
- `latency help`
- `latency histogram`
- `latency history`
- `latency latest`
- `latency reset`
- `memory`
- `memory doctor`
- `memory help`
- `memory malloc-stats`
- `memory purge`
- `memory stats`
- `memory usage`
- `monitor`
- `move`
- `object`
- `object encoding`
- `object freq`
- `object help`
- `object idletime`
- `object refcount`
- `pfdebug`
- `pfselftest`
- `psubscribe`
- `pubsub numpat`
- `punsubscribe`
- `script kill`
- `slowlog`
- `slowlog get`
- `slowlog help`
- `slowlog len`
- `slowlog reset`
- `swapdb`
- `wait`

## Supported Memcached commands

ElastiCache Serverless for Memcached supports all of the memcached
[commands](https://github.com/memcached/memcached/wiki/Commands "https://github.com/memcached/memcached/wiki/Commands") in open source memcached 1.6 except for
the following:

- Client connections require TLS, as a result UDP protocol is not supported.
- Binary protocol is not supported, as it is officially
  [deprecated](https://github.com/memcached/memcached/wiki/ReleaseNotes160 "https://github.com/memcached/memcached/wiki/ReleaseNotes160") in memcached 1.6.
- `GET/GETS` commands are limited to 16KB to avoid potential DoS attack to the server with fetching large number of keys.
- Delayed `flush_all` command will be rejected with `CLIENT_ERROR`.
- Commands that configure the engine or reveal internal information about engine state or logs
  are not supported, such as:
  - For `STATS` command, only `stats` and `stats reset` are supported. Other variations will return `ERROR`
  - `lru / lru_crawler` - modification for LRU and LRU crawler settings
  - `watch` - watches memcached server logs
  - `verbosity` - configures the server log level
  - `me` - meta debug (me) command is not supported

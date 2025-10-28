# Getting started with JSON

MemoryDB supports the native JavaScript Object Notation (JSON) format, a simple, schemaless way to encode complex datasets
inside Valkey or Redis OSS clusters. You can natively store and access data using the JavaScript Object Notation (JSON) format inside clusters and update JSON data stored in those clusters, without needing to manage custom code to serialize and deserialize it.

In addition to leveraging Valkey or Redis OSS APIs for applications that operate over JSON, you can now efficiently retrieve and update specific portions of a JSON document without needing to manipulate the entire object, which can improve performance and reduce cost.
You can also search your JSON document contents using the [Goessner-style](https://goessner.net/articles/JsonPath/ "https://goessner.net/articles/JsonPath/") `JSONPath` query.

After creating a cluster with a supported engine version, the JSON data type and associated commands are automatically available. This is API-compatible and RDB-compatible with version 2 of the RedisJSON module, so you can easily migrate
existing JSON-based Valkey or Redis OSS applications into MemoryDB. For more information on the supported commands, see [Supported commands](json-list-commands.md "json-list-commands.md").

JSON-related metric `JsonBasedCmds` is incorporated into CloudWatch to monitor the usage of this datatype. For more information,
see [Metrics for MemoryDB](metrics.md "metrics.md").

###### Note

To use JSON, you must be running Valkey 7.2 or later, or Redis OSS engine version 6.2.6 or later.

###### Topics

- [JSON Datatype overview](json-document-overview.md "json-document-overview.md")
- [Supported commands](json-list-commands.md "json-list-commands.md")

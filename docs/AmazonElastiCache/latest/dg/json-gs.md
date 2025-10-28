# Getting started with JSON for Valkey and Redis OSS

ElastiCache supports the native JavaScript Object Notation (JSON) format, which is a simple,
schemaless way to encode complex datasets inside Valkey and Redis OSS clusters. You can natively store
and access data using the JavaScript Object Notation (JSON) format inside the clusters, and update JSON data stored in those clusters—without needing to manage
custom code to serialize and deserialize it.

In addition to using Valkey and Redis OSS API operations for applications that operate over JSON, you can
now efficiently retrieve and update specific portions of a JSON document without needing
to manipulate the entire object. This can improve performance and reduce cost. You can
also search your JSON document contents using the [Goessner-style](https://goessner.net/articles/JsonPath/ "https://goessner.net/articles/JsonPath/")
`JSONPath` query.

After you create a cluster with a supported engine version, the JSON data type and
associated commands are automatically available.
API compatible and RDB compatible with version 2 of the JSON
module, so you can easily migrate existing JSON-based Valkey and Redis OSS applications into ElastiCache.
For more information on the supported commands, see [Supported Valkey and Redis OSS commands](json-list-commands.md "json-list-commands.md").

The JSON-related metrics `JsonBasedCmds` and `JsonBasedCmdsLatency`
are incorporated into CloudWatch to monitor the usage of this data type.
For more information, see [Metrics for
Valkey and Redis OSS](CacheMetrics.md "CacheMetrics.md").

###### Note

To use JSON, you must be running Valkey 7.2 and later, or Redis OSS 6.2.6 or later.

###### Topics

- [JSON data type overview](json-document-overview.md "json-document-overview.md")
- [Supported Valkey and Redis OSS commands](json-list-commands.md "json-list-commands.md")

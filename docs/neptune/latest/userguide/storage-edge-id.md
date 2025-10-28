# Neptune inlined server-generated edge ID

Neptune supports inline Server-Generated Edge IDs. It can be enabled via the Neptune configuration
[parameter](parameters.md "parameters.md")
`neptune_enable_inline_server_generated_edge_id` when `neptune_streams` is not enabled. This
feature is available for Gremlin queries starting with engine release
[1.4.3.0](../../../releases/release-1.4.3.0.md "../../../releases/release-1.4.3.0.md"), and will be available for OpenCypher
queries in a future release.

Edge ID is a unique identifier for an edge. An edge ID can be provided when inserting an edge. If no ID is provided,
the server generates and assigns a UUID based ID to the edge by default. Like the user-defined ID, the UUID-based
server-generated ID is stored in the dictionary.

When the `neptune_enable_inline_server_generated_edge_id` feature is enabled, the server generates a unique
inlined ID when no ID is provided in the query. The inlined edge IDs are not stored in the dictionary, improving the
storage efficiency. The server-generated inlined IDs begin with the reserved prefix `neptune_reserved`.

###### Warning

Neptune reserves the `'neptune_reserved'` prefix for server generated inlined IDs. An error will be shown
for queries attempting to insert data with a user-defined ID that begins with the reserved prefix.

The inlined server-generated edge ID feature can be enabled by setting the cluster-level parameter
`neptune_enable_inline_server_generated_edge_id` to `1`. A reboot of the instance is required. The
following example enables the server-generated edge ID feature:

```
"ParameterName=neptune_enable_inline_server_generated_edge_id,ParameterValue=1,ApplyMethod=pending-reboot"
```

To verify if the feature is enabled, you can check the features in the engine status. This feature is automatically
disabled if `neptune_streams` is enabled. The following example output shows the engine status for the enabled
feature:

```
"features":{"InlineServerGeneratedEdgeId":"enabled"}
```

The following Gremlin example adds an edge without a user-defined ID when the inline server-generated edge ID feature is
enabled:

```
curl - X POST--url https: //<neptune-cluster-endpoint>:8182/gremlin/ --data '{"gremlin":"g.withSideEffect(\"Neptune#disablePushdownOptimization\", true).addV().property(id, \"a\").addV().property(id, \"b\").addE(\"el\").to(V(\"a\"))"}'
{
    "requestId": "b6b84605-53ad-4c04-baf1-7f0f31a3aeaf",
    "status": {
        "message": "",
        "code": 200,
        "attributes": {
            "@type": "g:Map",
            "@value": []
        }
    },
    "result": {
        "data": {
            "@type": "g:List",
            "@value": [{
                "@type": "g:Edge",
                "@value": {
                    "id": "neptune_reserved_231850767",
                    "label": "el",
                    "inVLabel": "vertex",
                    "outVLabel": "vertex",
                    "inV": "a",
                    "outV": "b"
                }
            }]
        },
        "meta": {
            "@type": "g:Map",
            "@value": []
        }
    }
}
```

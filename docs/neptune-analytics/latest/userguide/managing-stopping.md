# Stopping a Neptune Analytics graph

You can temporarily stop a Neptune Analytics graph when it's not actively in use to reduce costs. When you stop a graph,
Neptune Analytics removes the underlying compute infrastructure while preserving all graph data, configurations, and
identifiers.

While stopped, you're charged only 10% of the normal rate instead of the
[full compute costs](https://aws.amazon.com/neptune/pricing/ "https://aws.amazon.com/neptune/pricing/"). This can result
in significant cost savings for graphs that are used intermittently, such as development environments or
analytics workloads with discrete processing periods.

Neptune Analytics only allows you to stop a graph that is in the `AVAILABLE` state. This design choice helps
ensure data consistency and prevents conflicts with other ongoing operations.

AWS Console

Choose the graph you want to stop, then choose **Stop graph** from the drop-down
**Actions** menu. The graph must be in `AVAILABLE` state to be stopped.

The graph status will change from `AVAILABLE` to `STOPPING`, and finally to
`STOPPED` when the operation has completed.

CLI/API

You can call the `stop-graph` CLI command, or the
[StopGraph](../apiref/API_StopGraph.md "../apiref/API_StopGraph.md")
API operation. The graph must be in the `AVAILABLE` state to be stopped.

```
aws neptune-graph stop-graph --graph-identifier g-sample
```

The graph status will change from `AVAILABLE` to `STOPPING`, and finally to
`STOPPED` when the operation has completed.

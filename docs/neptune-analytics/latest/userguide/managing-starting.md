# Starting a Neptune Analytics graph

You can start a Neptune Analytics graph that has been stopped to resume normal operations. The started graph automatically
deploys with the latest engine version, ensuring you benefit from the newest capabilities and security updates.

All graph data, configurations, and identifiers are preserved during the start operation. The graph endpoint
remains the same, so your applications can reconnect without configuration changes.

AWS Console

Choose the graph you want to start, then choose **Start graph** from the drop-down
**Actions** menu. The graph must be in `STOPPED` state to be started.

The graph status will change from `STOPPED` to `STARTING`, and finally to
`AVAILABLE` when the operation has completed.

CLI/API

You can call the `start-graph` CLI command, or the
[StartGraph](../apiref/API_StartGraph.md "../apiref/API_StartGraph.md")
API operation. The graph must be in the `STOPPED` state to be started.

```
aws neptune-graph start-graph --graph-identifier g-sample
```

The graph status will change from `STOPPED` to `STARTING`, and finally to
`AVAILABLE` when the operation has completed.

# Alert instances

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Grafana managed alerts support multi-dimensional alerting. Each alert rule can
create multiple alert instances. This is powerful if you are
observing multiple series in a single expression.

Consider the following PromQL expression:

```
sum by(cpu) (
  rate(node_cpu_seconds_total{mode!="idle"}[1m])
)
```

A rule using this expression will create as many alert instances as the amount
of CPUs we are observing after the first evaluation, allowing a single rule to
report the status of each CPU.

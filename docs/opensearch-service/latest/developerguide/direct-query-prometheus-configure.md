# Querying Prometheus metrics

Amazon OpenSearch Service allows you to query your Prometheus data using PromQL (Prometheus Query Language) directly from the Observability interface. When you execute a PromQL query against the Prometheus data source, OpenSearch Service passes the query directly to your workspace API for execution.

## Running a PromQL query

To run a query:

1. Open your OpenSearch UI application and observability workspace.
2. Navigate to **Observability** and select **Discover Metrics**.
3. In the data source drop-down, select your Prometheus data source.
4. Enter your PromQL query in the query bar.

For example, to find the average per-second CPU usage over a 5-minute window for a specific pod:

```
avg(rate(container_cpu_usage_seconds_total{pod="payment-service-pod"}[5m])) by (pod)
```

###### Note

Set your time picker to a narrow, relevant window (for example, the last 1 hour) to optimize API performance and prevent timeouts.

## Visualizing metrics in dashboards

You can add PromQL-driven metric visualizations to your existing observability dashboards to correlate them with your log and trace data.

1. Navigate to **Discover Metrics**, select your Prometheus workspace from the data source drop-down, and run your PromQL query.
2. Use the visualization tab in **Discover Metrics** to create a visualization and define your visualization type.
3. Save the visualization to your dashboard.

###### Note

Metric visualizations can only be added from **Discover Metrics**. Visualizations found on the visualizations tab are only optimized for logs.

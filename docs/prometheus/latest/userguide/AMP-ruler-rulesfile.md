# Create a rules file

To use rules in Amazon Managed Service for Prometheus, you create a rules file that defines the rules. An
Amazon Managed Service for Prometheus rules file is a YAML text file that has the same format as a rules file in
standalone Prometheus. For more information, see [Defining Recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/ "https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/") and [Alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/ "https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/") in the _Prometheus_ documentation.

The following is a basic example of a rules file:

```
groups:
  - name: cpu_metrics
     interval: 60s
     rules:
      - record: avg_cpu_usage
        expr: avg(rate(node_cpu_seconds_total[5m])) by (instance)
      - alert: HighAverageCPU
        expr: avg_cpu_usage > 0.8
        for: 10m
        keep_firing_for: 20m
        labels:
          severity: critical
        annotations:
          summary: "Average CPU usage across cluster is too high"
```

This example creates a rule group `cpu_metrics` which is evaluated every 60
seconds. This rule group creates a new metric using a recording rule, called `avg_cpu_usage` and then uses that in an alert. The following describes
some of the properties used. For more information about alerting rules and other
properties you can include, see [Alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/ "https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/") in the _Prometheus_ documentation.

- `record: avg_cpu_usage` – This recording rule creates a new
  metric called `avg_cpu_usage`.
- The default evaluation interval of rule groups is 60 seconds if the
  `interval` property is not specified.
- `expr: avg(rate(node_cpu_seconds_total[5m])) by (instance)`
  – This expression for the recording rule calculates the average rate of
  CPU usage over the last 5 minutes for each node, grouping by the
  `instance` label.
- `alert: HighAverageCPU` – This alert rule creates a new
  alert called `HighAverageCPU`
- `expr: avg_cpu_usage > 0.8` – This expression tells the
  alert to look for samples where the average CPU usage goes over 80%.
- `for: 10m` – The alert will only fire if the average CPU usage exceeds 80% for at least 10 minutes.

In this case, the metric is calculated as an average over the last 5 minutes. So the alert will only fire if there are at least two consecutive 5-minute samples (10 minutes total) where the average CPU usage is above 80%.

- `keep_firing_for: 20m` – This alert will continue to fire
  until the samples are below the threshold for at least 20 minutes. This can be
  useful to avoid the alert going up and down repeatedly in succession.

###### Note

You can create a rules definition file locally and then upload it to Amazon Managed Service for Prometheus, or
you can create, edit and upload the definition directly within the Amazon Managed Service for Prometheus
console. Either way, the same formatting rules apply. To learn more about uploading
and editing your file, see [Upload a rules configuration file to
Amazon Managed Service for Prometheus](AMP-rules-upload.md "AMP-rules-upload.md").

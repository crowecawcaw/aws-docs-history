# Slurm metrics in AWS PCS

AWS PCS supports Slurm metrics, which expose real-time cluster data through HTTP
endpoints compatible with Prometheus and other monitoring systems. For details, including
performance impact and security considerations, see the
[Metrics Guide](https://slurm.schedmd.com/metrics.html "https://slurm.schedmd.com/metrics.html") on the
Slurm website.

## Prerequisites

Before enabling Slurm metrics, verify that you have:

- **Cluster version**: Slurm version 25.11
  or higher.
- **Security group**: Rules allowing HTTP traffic on port 6817
  from your desired sources.

## Enable the metrics endpoint

Set the following cluster-level custom Slurm settings:

- `MetricsType` – Must specify a supported metrics plugin, such as `metrics/openmetrics`.
- `CommunicationParameters` – Must include `enable_http`.

###### Important

Enabling `enable_http` exposes an unauthenticated HTTP endpoint.
Anyone with network access to port 6817 can read cluster, job, and node metrics.
Use security group rules to restrict access to trusted sources only.

- `PrivateData` – Must _not_ be set.

For more information about custom Slurm settings, see
[Configuring custom Slurm settings in AWS PCS](slurm-custom-settings.md "slurm-custom-settings.md").

## Use the metrics endpoint

Query the metrics endpoint from a host with network access to the controller:

```
curl http://`controller-ip`:6817/metrics
```

For more information about available metrics and scraping configuration, see the
[Metrics Guide](https://slurm.schedmd.com/metrics.html "https://slurm.schedmd.com/metrics.html") on the
Slurm website.

To collect these metrics using a managed Prometheus collector, see
[Collect Slurm metrics with a managed Prometheus collector](slurm-metrics-prometheus.md "slurm-metrics-prometheus.md").

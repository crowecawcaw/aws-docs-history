# Scraper configuration

Amazon CloudWatch managed Prometheus collectors use a Prometheus-compatible YAML configuration to
define how the collector scrapes metrics. You provide this configuration as a base64-encoded
blob when creating or updating a scraper. The configuration uses standard Prometheus
scrape configuration format, with some limitations specific to managed collectors.

You can use [GetDefaultScraperConfiguration](../../../prometheus/latest/APIReference/API_GetDefaultScraperConfiguration.md "../../../prometheus/latest/APIReference/API_GetDefaultScraperConfiguration.md") to retrieve a general-purpose
scraper configuration, or provide your own.

## Supported configuration sections

The following top-level sections of the Prometheus scrape configuration are
supported:

- `global` — Global settings including
  `scrape_interval`, `scrape_timeout`, and
  `external_labels`.
- `scrape_configs` — A list of scrape jobs, each defining
  targets and how to scrape them.

Within each `scrape_configs` entry, the following fields are
supported:

- `job_name` — A unique name for the scrape job.
- `metrics_path` — The HTTP path to scrape (defaults to
  `/metrics`).
- `scheme` — The protocol scheme (`http` or
  `https`).
- `scrape_interval` — Per-job override of the global scrape
  interval.
- `scrape_timeout` — Per-job override of the global scrape
  timeout.
- `static_configs` — Static list of targets.
- `dns_sd_configs` — DNS-based service discovery.
- `relabel_configs` — Relabeling rules applied before
  scraping.
- `metric_relabel_configs` — Relabeling rules applied after
  scraping.
- `tls_config` — TLS configuration for HTTPS
  targets.

## Example configuration

The following example demonstrates a basic scrape configuration:

```
global:
  scrape_interval: 60s
  scrape_timeout: 10s
  external_labels:
    environment: production

scrape_configs:
  - job_name: 'my-service'
    metrics_path: /metrics
    scheme: http
    static_configs:
      - targets:
          - '`10.0.1.10`:9090'
          - '`10.0.1.11`:9090'
        labels:
          team: platform
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance
    metric_relabel_configs:
      - source_labels: [__name__]
        regex: 'go_.*'
        action: drop
```

## Limitations

- The minimum `scrape_interval` is 30 seconds.
- Managed collectors do not support file-based service discovery
  (`file_sd_configs`).
- Managed collectors do not support Consul, Eureka, or other external service
  discovery mechanisms.
- Remote write and remote read configurations do not apply, because the
  collector handles delivery to CloudWatch.
- The maximum configuration size is 256 KB.

## Troubleshooting

If your scraper is not collecting metrics as expected, check the following:

- Verify that the security group attached to the scraper allows outbound
  traffic to your target ports.
- Confirm that your targets are reachable from the subnets that you specified in
  the scraper configuration.
- Check that DNS names used in `dns_sd_configs` resolve correctly
  within the VPC.
- Ensure your targets respond on the configured
  `metrics_path` with valid Prometheus exposition format.

For additional troubleshooting guidance, see [Troubleshooting
managed collectors](../../../prometheus/latest/userguide/AMP-troubleshooting.md "../../../prometheus/latest/userguide/AMP-troubleshooting.md") in the _Amazon Managed Service for Prometheus User
Guide_.

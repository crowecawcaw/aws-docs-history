

# Scrape Prometheus metrics on Amazon EC2 instances

The CloudWatch agent can scrape applications that expose metrics in the Prometheus format and send the metrics to the CloudWatch OTLP endpoint. You can then query the metrics with PromQL. Both Linux and Windows Server instances are supported.

To scrape Prometheus metrics, you need two files: a standard Prometheus scrape configuration file, and a CloudWatch agent configuration file whose `opentelemetry` section has a `prometheus` source that points to the scrape configuration file.

**Topics**
+ [Prerequisites](#CloudWatch-Agent-PrometheusEC2-install)
+ [Creating the Prometheus scrape configuration](#CloudWatch-Agent-PrometheusEC2-configure-scrape)
+ [Configuring and starting the agent](#CloudWatch-Agent-PrometheusEC2-configure-agent)
+ [Example: Scrape JVM metrics with the Prometheus JMX exporter](#CloudWatch-Agent-Prometheus-Java)

## Prerequisites
<a name="CloudWatch-Agent-PrometheusEC2-install"></a>
+ Install CloudWatch agent version 1.300070.0 or later on the instance. For more information, see [Prerequisites](CloudWatch-Agent-OpenTelemetry-config.md#CloudWatch-Agent-OpenTelemetry-config-prereqs).
+ If the agent scrapes other instances, the security groups of those instances must allow inbound traffic on the Prometheus port from the agent's private IP address. The agent's security group must allow outbound traffic to that port.
+ If you use `ec2_sd_configs` to discover targets, the IAM role of the instance where the agent runs must allow `ec2:DescribeInstances`.

## Creating the Prometheus scrape configuration
<a name="CloudWatch-Agent-PrometheusEC2-configure-scrape"></a>

The agent supports the standard Prometheus scrape configuration. For more information about the scrape configuration, see [<scrape\_config>](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config) on the Prometheus website. Save the file in the agent's `etc` directory, for example `/opt/aws/amazon-cloudwatch-agent/etc/prometheus.yaml` on Linux or `C:\ProgramData\Amazon\AmazonCloudWatchAgent\prometheus.yaml` on Windows Server.

The following example scrapes a local application every minute:

```yaml
global:
  scrape_interval: 1m
  scrape_timeout: 10s
scrape_configs:
  - job_name: my-app
    sample_limit: 10000
    static_configs:
      - targets: ['127.0.0.1:9404']
        labels:
          team: payments
```

The file contains the following sections:
+ `global` – Defaults for all scrape jobs. `scrape_interval` sets how often to scrape targets, and `scrape_timeout` sets how long to wait before a scrape request times out.
+ `scrape_configs` – One entry for each scrape job. `job_name` names the job. The agent sets the `@resource.service.name` label on the scraped metrics to this value. `sample_limit` limits the number of samples that the agent accepts from each scrape.

To tell the agent which targets to scrape, use one of the following service discovery types in each job:
+ `static_configs` – A fixed list of targets, and labels to add to all metrics from those targets, as in the previous example.
+ `file_sd_configs` – Reads targets from one or more files. The agent rereads the files when they change, so you can update targets without restarting the agent.

  ```yaml
  scrape_configs:
    - job_name: my-app
      file_sd_configs:
        - files: ['/opt/aws/amazon-cloudwatch-agent/etc/prometheus_sd_1.yaml']
  ```

  Each file lists targets and labels:

  ```yaml
  - targets:
      - 127.0.0.1:9404
    labels:
      team: payments
  ```
+ `ec2_sd_configs` – Discovers targets from the Amazon EC2 API. The following example scrapes port 9404 on two instances. If you omit `region`, the agent uses the Region from the instance metadata.

  ```yaml
  scrape_configs:
    - job_name: my-app
      ec2_sd_configs:
        - region: {{us-east-1}}
          port: 9404
          filters:
            - name: instance-id
              values:
                - {{i-98765432109876543}}
                - {{i-12345678901234567}}
  ```

  For more information about the filters that you can use, see [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html) in the *Amazon EC2 API Reference*.

## Configuring and starting the agent
<a name="CloudWatch-Agent-PrometheusEC2-configure-agent"></a>

1. In the agent configuration file, add a `prometheus` source to the `opentelemetry` section, and set `config_path` to the scrape configuration file.

   ```json
   {
     "opentelemetry": {
       "collect": {
         "host_metrics": {},
         "prometheus": {
           "config_path": "/opt/aws/amazon-cloudwatch-agent/etc/prometheus.yaml"
         }
       }
     }
   }
   ```

   For the other sources that you can add, see [Create a CloudWatch agent configuration for OpenTelemetry](CloudWatch-Agent-OpenTelemetry-config.md).

1. Start the agent with the configuration file. On Linux:

   ```
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:{{/path/to/config.json}} -s
   ```

   For other platforms, see [Starting the CloudWatch agent](start-CloudWatch-Agent-on-premise-SSM-onprem.md).

1. In the CloudWatch console, open Query Studio and run a PromQL query for a metric that your application exposes, filtered by the job name. For example:

   ```
   {"{{my_metric}}", "@resource.service.name"="my-app"}
   ```

   Metrics typically appear within 1–2 minutes. For more information, see [Running PromQL queries in Query Studio](CloudWatch-PromQL-QueryStudio.md).

## Example: Scrape JVM metrics with the Prometheus JMX exporter
<a name="CloudWatch-Agent-Prometheus-Java"></a>

This example runs a Java application with the Prometheus JMX exporter, which exposes JVM metrics such as memory, garbage collection, and threads in the Prometheus format. The agent scrapes the exporter and sends the metrics to CloudWatch.

1. Download the JMX exporter Java agent from the [jmx\_exporter](https://github.com/prometheus/jmx_exporter) project on the GitHub website.

1. Create an exporter configuration file, for example `config.yaml`. The following configuration exports all MBeans:

   ```yaml
   rules:
     - pattern: ".*"
   ```

1. Start the application with the exporter as a Java agent that listens on port 9404:

   ```
   java -javaagent:{{/path/to/jmx_prometheus_javaagent.jar}}=9404:{{/path/to/config.yaml}} -jar {{my-app.jar}}
   ```

1. Confirm that the exporter returns metrics:

   ```
   curl http://localhost:9404/metrics
   ```

   The output is plain text in the Prometheus exposition format, with lines that start with `jvm_`.

1. Create a scrape configuration with a job for the exporter, and then configure and start the agent as described in [Configuring and starting the agent](#CloudWatch-Agent-PrometheusEC2-configure-agent).

   ```yaml
   global:
     scrape_interval: 1m
   scrape_configs:
     - job_name: java-app
       static_configs:
         - targets: ['127.0.0.1:9404']
   ```

1. In Query Studio, query a JVM metric from the exporter with `"@resource.service.name"="java-app"`.

For Java applications, you can also use the `jmx` source in the Classic configuration. For more information, see [Collect Java Management Extensions (JMX) metrics](CloudWatch-Agent-JMX-metrics.md).
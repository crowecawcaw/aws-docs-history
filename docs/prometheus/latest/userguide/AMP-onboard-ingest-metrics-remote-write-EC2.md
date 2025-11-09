# Set up metrics

ingestion from an Amazon EC2 instance using remote write

This section explains how to run a Prometheus server with remote write in an
Amazon Elastic Compute Cloud (Amazon EC2) instance. It explains how to collect metrics from a demo
application written in Go and send them to an Amazon Managed Service for Prometheus workspace.

## Prerequisites

###### Important

Before you start, you must have installed Prometheus v2.26 or later. We
assume that you're familiar with Prometheus, Amazon EC2, and Amazon Managed Service for Prometheus. For
information about how to install Prometheus, see [Getting started](https://prometheus.io/docs/prometheus/latest/getting_started/ "https://prometheus.io/docs/prometheus/latest/getting_started/") on the Prometheus website.

If you're unfamiliar with Amazon EC2 or Amazon Managed Service for Prometheus, we recommend that you start
by reading the following sections:

- [What is Amazon Elastic Compute Cloud?](../../../AWSEC2/latest/UserGuide/concepts.md "../../../AWSEC2/latest/UserGuide/concepts.md")
- [What is Amazon Managed Service for Prometheus?](what-is-Amazon-Managed-Service-Prometheus.md "what-is-Amazon-Managed-Service-Prometheus.md")

## Create an

IAM role for Amazon EC2

To stream metrics, you must first create an IAM role with the AWS managed
policy **AmazonPrometheusRemoteWriteAccess**. Then, you can
launch an instance with the role and stream metrics into your Amazon Managed Service for Prometheus
workspace.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. From the navigation pane, choose **Roles**, and then
   choose **Create role**.
3. For the type of trusted entity, choose **AWS
   service**. For the use case, choose
   **EC2**. Choose **Next:
   Permissions**.
4. In the search bar, enter
   **AmazonPrometheusRemoteWriteAccess**. For
   **Policy name**, select
   **AmazonPrometheusRemoteWriteAccess**, and then
   choose **Attach policy**. Choose
   **Next:Tags**.
5. (Optional) Create IAM tags for your IAM role. Choose
   **Next: Review**.
6. Enter a name for your role. Choose **Create
   policy**.

## Launch an

Amazon EC2 instance

To launch an Amazon EC2 instance, follow the instructions at [Launch an instance](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#launch-instance-with-role "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#launch-instance-with-role") in the _Amazon Elastic Compute Cloud
User Guide for Linux Instances_.

## Run the demo

application

After creating your IAM role, and launching an EC2 instance with the role, you
can run a demo application to see it work.

###### To run a demo application and test metrics

1. Use the following template to create a Go file named
   `main.go`.

```
package main

import (
    "github.com/prometheus/client_golang/prometheus/promhttp"
    "net/http"
)

func main() {
    http.Handle("/metrics", promhttp.Handler())

    http.ListenAndServe(":8000", nil)
}
```

2. Run the following commands to install the correct dependencies.

```
sudo yum update -y
sudo yum install -y golang
go get github.com/prometheus/client_golang/prometheus/promhttp
```

3. Run the demo application.

```
go run main.go
```

The demo application should run on port 8000 and show all of the
exposed Prometheus metrics. The following is an example of these
metrics.

```
curl -s http://localhost:8000/metrics
...
process_max_fds 4096# HELP process_open_fds Number of open file descriptors.# TYPE process_open_fds gauge
process_open_fds 10# HELP process_resident_memory_bytes Resident memory size in bytes.# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 1.0657792e+07# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.61131955899e+09# HELP process_virtual_memory_bytes Virtual memory size in bytes.# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 7.77281536e+08# HELP process_virtual_memory_max_bytes Maximum amount of virtual memory available in bytes.# TYPE process_virtual_memory_max_bytes gauge
process_virtual_memory_max_bytes -1# HELP promhttp_metric_handler_requests_in_flight Current number of scrapes being served.# TYPE promhttp_metric_handler_requests_in_flight gauge
promhttp_metric_handler_requests_in_flight 1# HELP promhttp_metric_handler_requests_total Total number of scrapes by HTTP status code.# TYPE promhttp_metric_handler_requests_total counter
promhttp_metric_handler_requests_total{code="200"} 1
promhttp_metric_handler_requests_total{code="500"} 0
promhttp_metric_handler_requests_total{code="503"} 0
```

## Create

an Amazon Managed Service for Prometheus workspace

To create an Amazon Managed Service for Prometheus workspace, follow the instructions at [Create a workspace](AMP-create-workspace.md "AMP-create-workspace.md").

## Run a

Prometheus server

1. Use the following example YAML file as a template to create a new file
   named `prometheus.yaml`. For `url`,
   replace `my-region` with your Region value and
   `my-workspace-id` with the workspace ID
   that Amazon Managed Service for Prometheus generated for you. For `region`, replace
   `my-region` with your Region value.

**Example: YAML file**

```
global:
  scrape_interval: 15s
  external_labels:
    monitor: 'prometheus'

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:8000']

remote_write:
  -
    url: https://aps-workspaces.`my-region`.amazonaws.com/workspaces/`my-workspace-id`/api/v1/remote_write
    queue_config:
        max_samples_per_send: 1000
        max_shards: 200
        capacity: 2500
    sigv4:
         region: `my-region`
```

2. Run the Prometheus server to send the demo application’s metrics to
   your Amazon Managed Service for Prometheus workspace.

```
prometheus --config.file=prometheus.yaml
```

The Prometheus server should now send the demo application’s metrics to your
Amazon Managed Service for Prometheus workspace.

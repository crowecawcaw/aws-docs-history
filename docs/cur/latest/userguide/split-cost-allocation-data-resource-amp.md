# Using split cost

allocation data with Amazon Managed Service for Prometheus

Splitting the cost data for Amazon EKS requires that you collect and store metrics from
your clusters, including memory and CPU usage. Amazon Managed Service for Prometheus
can be used for this purpose.

Once you're opted in to split cost allocation data and your Amazon Managed Service
for Prometheus workspace starts receiving the two required metrics
(`container_cpu_usage_seconds_total` and
`container_memory_working_set_bytes`), split cost allocation data
recognizes the metrics and uses them automatically.

###### Note

The two required metrics (`container_cpu_usage_seconds_total` and
`container_memory_working_set_bytes`) are present in the default
Prometheus scrape configuration and the default configuration provided with an
AWS managed collector. However, if you customize these configurations, do not
relabel, modify, or remove the following labels from the
`container_cpu_usage_seconds_total` and
`container_memory_working_set_bytes` metrics: `name`,
`namespace`, and `pod`. If you relabel, modify, or
remove these labels, it can impact the ingestion of your metrics.

You can use Amazon Managed Service for Prometheus to collect EKS metrics from a
single usage account, in a single Region. The Amazon Managed Service for Prometheus
workspace must be in that account and Region. You need one Amazon Managed Service
for Prometheus instance for each usage account and Region for which you want to
monitor the costs. You can collect metrics for multiple clusters in the Amazon
Managed Service for Prometheus workspace, as long as they're in the same usage
account and Region.

The following sections describe how to send the correct metrics from your EKS
cluster to the Amazon Managed Service for Prometheus workspace.

## Prerequisites

As prerequisites for using Amazon Managed Service for Prometheus with split
cost allocation data:

- You need to enable split cost allocation data in the AWS Billing and
  Cost Management console. For details, see [Enabling split cost allocation data](enabling-split-cost-allocation-data.md "enabling-split-cost-allocation-data.md").
  Opting in to split cost allocation data creates a service-linked role in
  each usage account to query Amazon Managed Service for Prometheus for
  the Amazon EKS cluster metrics in that account. For more information, see
  [Service-linked roles for split cost allocation
  data](../../../cost-management/latest/userguide/split-cost-allocation-data-SLR.md "../../../cost-management/latest/userguide/split-cost-allocation-data-SLR.md").
- You need an EKS cluster for which you want to track split cost
  allocation data. This can be an existing cluster, or you can create a
  new one. For more information, see [Create an Amazon EKS cluster](../../../eks/latest/userguide/create-cluster.md "../../../eks/latest/userguide/create-cluster.md") in the _Amazon EKS User
  Guide_.

###### Note

You will need the `EKS cluster ARN`, `security
 group IDs`, and at least two `subnet IDs` (in
different availability zones) for use in later steps.

(optional) Set your EKS cluster’s authentication mode to either
`API` or `API_AND_CONFIG_MAP`.

- You need an Amazon Managed Service for Prometheus instance in the same
  account and Region as your EKS cluster. If you do not already have one,
  you can create one. For more information on creating an Amazon Managed
  Service for Prometheus instance, see [Create a workspace](../../../prometheus/latest/userguide/AMP-onboard-create-workspace.md "../../../prometheus/latest/userguide/AMP-onboard-create-workspace.md") in the
  _Amazon Managed Service for Prometheus User
  Guide_.

###### Note

You will need the `Amazon Managed Service for Prometheus
 workspace ARN` for use in later steps.

## Forwarding EKS metrics to

Amazon Managed Service for Prometheus

Once you have an EKS cluster and an Amazon Managed Service for Prometheus
instance, you can forward the metrics from the cluster to the instance. You can
send metrics in two ways.

- [Option 1: Use an AWS managed
  collector.](split-cost-allocation-data-resource-amp.md#use-managed-collector "split-cost-allocation-data-resource-amp.md#use-managed-collector") This is the simplest way to send metrics from an
  EKS cluster to Amazon Managed Service for Prometheus. However, it does
  have a limit of only scraping metrics every 30 seconds at most.
- [Option 2: Create your own Prometheus
  agent.](split-cost-allocation-data-resource-amp.md#create-prometheus-agent "split-cost-allocation-data-resource-amp.md#create-prometheus-agent") In this case, you have more control over the scraping
  configuration, but you must manage the agent after creating it.

### Option 1: Using an AWS managed

collector

Using an AWS managed collector (a _scraper_) is the simplest way to send metrics from an EKS
cluster to an Amazon Managed Service for Prometheus instance. The following
procedure steps you through creating an AWS managed collector. For more
detailed information, see [AWS managed collectors](../../../prometheus/latest/userguide/AMP-collector.md "../../../prometheus/latest/userguide/AMP-collector.md") in the _Amazon Managed Service for Prometheus User
Guide_.

###### Note

AWS managed collectors have a minimum scrape interval of 30 seconds.
If you have short-lived pods, the recommendation is to set your scraper
interval to 15 seconds. To use a 15 second scraper interval, use option
2 to [create your own Prometheus
agent](split-cost-allocation-data-resource-amp.md#create-prometheus-agent "split-cost-allocation-data-resource-amp.md#create-prometheus-agent").

There are three steps to create an AWS managed collector:

1. Create a scraper configuration.
2. Create the scraper.
3. Configure your EKS cluster to allow the scraper to access
   metrics.

_Step 1: Create a scraper configuration_

In order to create a scraper, you must have a scraper configuration. You
can use a default configuration, or create your own. The following are three
ways to get a scraper configuration:

- Get the default configuration using the AWS CLI, by
  calling:

```
aws amp get-default-scraper-configuration
```

- Create your own configuration. For details, see the [Scraper configuration](../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-configuration "../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-configuration") instructions
  in the _Amazon Managed Service for Prometheus User
  Guide_.
- Copy the sample configuration provided in that same [Scraper configuration](../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-configuration "../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-configuration") instructions
  in the _Amazon Managed Service for Prometheus User
  Guide_.

You can edit the scraper configuration, to modify the scrape interval or
to filter the metrics that are scraped, for example.

To filter the metrics that are scraped to just include the two that are
needed for split cost allocation data, use the following scraper
configuration:

```
global:
   scrape_interval: 30s
   #external_labels:
     #clusterArn: <REPLACE_ME>
scrape_configs:
  - job_name: kubernetes-nodes-cadvisor
    scrape_interval: 30s
    scrape_timeout: 10s
    scheme: https
    authorization:
      type: Bearer
      credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    kubernetes_sd_configs:
    - role: node
    relabel_configs:
    - regex: (.+)
      replacement: /api/v1/nodes/$1/proxy/metrics/cadvisor
      source_labels:
      - __meta_kubernetes_node_name
      target_label: __metrics_path__
    - replacement: kubernetes.default.svc:443
      target_label: __address__
    metric_relabel_configs:
    - source_labels: [__name__]
      regex: 'container_cpu_usage_seconds_total|container_memory_working_set_bytes'
      action: keep
```

Once you have the scraper configuration, you must base64 encode it for use
in _step 2_. The configuration is a text YAML file. To
encode the file, use a website such as [https://www.base64encode.org/](https://www.base64encode.org/ "https://www.base64encode.org/").

_Step 2: Create the scraper_

Now that you have a configuration file, you need to create your scraper.
Create a scraper using the following AWS CLI command, based on the
variables outlined in the prerequisites section. You must use information
from your EKS cluster for the
`<EKS-CLUSTER-ARN>`,
`<SG-SECURITY-GROUP-ID>`, and
`<SUBNET-ID>` fields, replace
`<BASE64-CONFIGURATION-BLOB>` with the
scraper configuration you created in the previous step, and replace
`<AMP_WORKSPACE_ARN>` with your Amazon
Managed Service for Prometheus workspace ARN.

```
aws amp create-scraper \
--source eksConfiguration="{clusterArn=`<EKS-CLUSTER-ARN>`,securityGroupIds=[`<SG-SECURITY-GROUP-ID>`],subnetIds=[`<SUBNET-ID>`]}" \
--scrape-configuration configurationBlob=`<BASE64-CONFIGURATION-BLOB>` \
--destination ampConfiguration={workspaceArn="`<AMP_WORKSPACE_ARN>`"}
```

Note down the `scraperId` that is returned for use in
_step 3_.

_Step 3: Configure your EKS cluster to allow the scraper to
access metrics_

If your EKS cluster’s authentication mode is set to either
`API` or `API_AND_CONFIG_MAP`, then your scraper
will automatically have the correct in-cluster access policy, and the
scrapers will have access to your cluster. No further configuration is
required, and metrics should be flowing to Amazon Managed Service for
Prometheus.

If your EKS cluster’s authentication mode is not set to `API`
or `API_AND_CONFIG_MAP`, you will need to manually configure the
cluster to allow the scraper to access your metrics through a ClusterRole
and ClusterRoleBinding. To learn how to enable these permissions, see [Manually configuring an EKS cluster for scraper
access](../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-eks-setup "../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-eks-setup") in the _Amazon Managed Service for Prometheus
User Guide_.

Once the scraper is active, verify that both metrics
(`container_cpu_usage_seconds_total` and
`container_memory_working_set_bytes`) are being pushed to
your Amazon Managed Service for Prometheus workspace.

```
awscurl --service="aps" --region="<REGION>" "https://aps-workspaces.<REGION>.amazonaws.com/workspaces/<WorkSpace_ID>/api/v1/label/__name__/values"
```

Output:

```
{
"status": "success",
"data": [
"container_cpu_usage_seconds_total",
"container_memory_working_set_bytes",
"scrape_duration_seconds",
"scrape_samples_post_metric_relabeling",
"scrape_samples_scraped",
"scrape_series_added",
"up"
]
}
```

### Option 2: Creating your own

Prometheus agent

If you can’t use the AWS managed collector, or already have your own
Prometheus server, you can use your own Prometheus instance as an agent to
scrape metrics from your EKS cluster and send them to Amazon Managed Service
for Prometheus.

For detailed instructions on how to use your own Prometheus instance as an
agent, see [Using a Prometheus instance as a collector](../../../prometheus/latest/userguide/AMP-ingest-with-prometheus.md "../../../prometheus/latest/userguide/AMP-ingest-with-prometheus.md")
in the _Amazon Managed Service for Prometheus User
Guide_.

The following is a sample Prometheus scrape configuration that includes
the Prometheus server scrape interval and the container metrics required for
split cost allocation data. If you have short-lived pods, the recommendation
is to lower the default Prometheus server scrape interval from 30 seconds to
15 seconds. Note that this can result in high Prometheus server memory
usage.

```
global:
   scrape_interval: 30s
   #external_labels:
     #clusterArn: <REPLACE_ME>
scrape_configs:
  - job_name: kubernetes-nodes-cadvisor
    scrape_interval: 30s
    scrape_timeout: 10s
    scheme: https
    authorization:
      type: Bearer
      credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    kubernetes_sd_configs:
    - role: node
    relabel_configs:
    - regex: (.+)
      replacement: /api/v1/nodes/$1/proxy/metrics/cadvisor
      source_labels:
      - __meta_kubernetes_node_name
      target_label: __metrics_path__
    - replacement: kubernetes.default.svc:443
      target_label: __address__
    metric_relabel_configs:
    - source_labels: [__name__]
      regex: 'container_cpu_usage_seconds_total|container_memory_working_set_bytes'
      action: keep
```

If you followed [Set up ingestion from a new Prometheus server using
Helm](../../../prometheus/latest/userguide/AMP-onboard-ingest-metrics-new-Prometheus.md "../../../prometheus/latest/userguide/AMP-onboard-ingest-metrics-new-Prometheus.md") in the in the _Amazon Managed Service for
Prometheus User Guide_, then you can update your scrape
configuration.

###### To update your scrape configuration

1. Edit `my_prometheus_values_yaml` from the guide and
   include the sample scrape config in the `server`
   block.
2. Run the following command, using
   `prometheus-chart-name` and
   `prometheus-namespace` from the _Amazon
   Managed Service for Prometheus User Guide_.

```
helm upgrade prometheus-chart-name prometheus-community/prometheus -n prometheus-namespace -f my_prometheus_values_yaml
```

To learn more about `scrape_interval`or how to use a non-global
scrape_interval, refer to [Prometheus scrape configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config "https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config").

Alternatively, you can use the AWS Distro for OpenTelemetry collector
that has a Prometheus Receiver, a Prometheus Remote Write Exporter, and the
AWS Sigv4 Authentication Extension to achieve remote write access to
Amazon Managed Service for Prometheus.

###### Note

Once you have set up your Prometheus agent, unlike AWS managed
collectors, you are responsible for keeping the agent up to date and
running to collect metrics.

## Estimating your Amazon Managed

Service for Prometheus costs

You can use AWS Pricing Calculator to estimate the cost of using Amazon
Managed Service for Prometheus for split cost allocation data.

###### To configure Amazon Managed Service for Prometheus for your

estimate

1. Open AWS Pricing Calculator at [https://calculator.aws/#/](https://calculator.aws/#/ "https://calculator.aws/#/").
2. Choose **Create estimate**.
3. On the **Add service** page, enter **Amazon
   Managed Service for Prometheus** in the search field, and
   then choose **Configure**.
4. In the **Description** field, enter a description for
   your estimate.
5. Choose a **Region**.
6. Select **Calculate the cost using your infrastructure
   details**. This option allows you to estimate your
   ingestion, storage, and query sample costs based on your current or
   proposed infrastructure setup.
7. For **Number of EC2 instances**, enter the total
   number of EC2 instances across all your clusters for your entire
   consolidated billing family (including all accounts and Regions). If you
   use AWS Fargate, use the number of Fargate tasks as a proxy for your
   EC2 instance count.
8. Split cost allocation data requires two metrics:
   `container_cpu_usage_seconds_total` and
   `container_memory_working_set_bytes`. For
   **Prometheus metrics per EC2 instances**, enter
9.
10. Split cost allocation data suggests a scrape interval of 15 seconds.
    For **Metric collection interval (in seconds)**, enter
11. If you used a different interval (for example, 30 seconds), change
    this to the interval you set up.
12. Split cost allocation data does not impose any specific requirements
    for the other parameters so enter appropriate values for the rest of the
    input parameters as per your business requirements.
13. Choose **Save and add service**.

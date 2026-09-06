

# Collect Slurm metrics with a managed Prometheus collector
<a name="slurm-metrics-prometheus"></a>

After you enable Slurm metrics on your AWS PCS cluster (see [Slurm metrics in AWS PCS](slurm-metrics.md)), you can use a managed Prometheus collector to automatically scrape the metrics endpoints and deliver the data for PromQL querying. The managed collector creates elastic network interfaces in your VPC subnets to reach the cluster controller's metrics endpoints on port 6817.

The collector can deliver metrics to either of the following destinations:
+ **Amazon Managed Service for Prometheus workspace** – A dedicated Prometheus-compatible metrics store with configurable retention (150 days by default). You can query through Prometheus-compatible APIs or Grafana.
+ **CloudWatch dataset** – Your account's default CloudWatch dataset with 15 months of included retention. You can query through CloudWatch Query Studio or the Prometheus-compatible HTTP API.

The cluster-side configuration (Slurm settings, controller target, security groups, and scrape configuration) is the same regardless of which destination you choose. Only the `destination` block in the create-scraper request and the query endpoint differ.

You create the collector with the `aws amp create-scraper` command. Although this command belongs to the `amp` CLI namespace, it supports both destinations.

For more information about VPC-connected managed collectors, see [Set up a VPC-connected managed collector](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/managed-prometheus-collectors-vpc-setup.html) in the *Amazon CloudWatch User Guide*.

## Prerequisites
<a name="slurm-metrics-prometheus-prerequisites"></a>

Before you configure the managed collector, verify the following:
+ **Slurm metrics enabled** – The metrics endpoint must be active on your cluster. You enable it by setting the `MetricsType` and `CommunicationParameters` custom Slurm settings. For instructions on enabling Slurm metrics, see [Slurm metrics in AWS PCS](slurm-metrics.md). For more information about custom Slurm settings, see [Configuring custom Slurm settings in AWS PCS](slurm-custom-settings.md).
+ **Slurm version 25.11 or higher** – The cluster must run Slurm 25.11 or higher to expose the metrics endpoint.
+ **Destination resource** – Create the destination for your metrics:
  + *Amazon Managed Service for Prometheus workspace* – Create a workspace and wait for it to reach `ACTIVE` status. For instructions on creating a workspace, see [Create a workspace](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-create-workspace.html) in the *Amazon Managed Service for Prometheus User Guide*.
  + *CloudWatch dataset* – Every account has a `default` dataset in each Region. You do not need to create it.
+ **VPC subnets and networking** – You need at least two subnets in different Availability Zones within the same VPC as the cluster controller. Include the Availability Zone where the controller's network interface resides. The VPC must have DNS support and DNS hostnames enabled. For detailed networking requirements, see [Set up a VPC-connected managed collector](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/managed-prometheus-collectors-vpc-setup.html) in the *Amazon CloudWatch User Guide*.
+ **Security groups** – A dedicated security group for the collector is required. For instructions on configuring security groups, see [Configure security groups for the collector](#slurm-metrics-prometheus-security-groups).
+ **IAM permissions** – The IAM principal that creates the scraper needs `aps:CreateScraper` and `iam:CreateServiceLinkedRole` permissions. The service automatically creates a service-linked role (`AWSServiceRoleForAmazonPrometheusScraper`). This role grants the collector permission to access your VPC resources and write to your chosen destination. No manual role setup is required. For more information, see [Using service-linked roles](https://docs.aws.amazon.com/prometheus/latest/userguide/using-service-linked-roles.html) in the *Amazon Managed Service for Prometheus User Guide*.
+ **Internet or VPC endpoint** – The collector subnets must be able to reach the destination service. If your subnets have no internet access, create an interface VPC endpoint in the same VPC and subnets. Use `com.amazonaws.{{region}}.aps-workspaces` for an Amazon Managed Service for Prometheus workspace destination, or `com.amazonaws.{{region}}.monitoring` for a CloudWatch dataset destination.

## Configure security groups for the collector
<a name="slurm-metrics-prometheus-security-groups"></a>

We recommend creating a dedicated security group for the managed collector rather than reusing an existing security group. A dedicated group gives you explicit, auditable rules that follow the principle of least privilege.

**Important**  
The `enable_http` setting exposes an unauthenticated HTTP endpoint on port 6817. Restrict inbound access on this port to the collector's security group only. Do not allow broad network access (such as a CIDR range) to this port.

The following procedure uses shell variables for security group IDs. Set these variables before you run the commands:
+ `VPC_ID` – The ID of the VPC where your AWS PCS cluster resides.
+ `CLUSTER_SG_ID` – The ID of the security group attached to your cluster (the one you specified when you created the cluster).
+ `VPCE_SG_ID` – The ID of the security group attached to your interface VPC endpoint. This variable is only needed if your collector subnets reach the destination service through an interface VPC endpoint rather than through internet or NAT egress. The endpoint is `com.amazonaws.{{region}}.aps-workspaces` for an Amazon Managed Service for Prometheus workspace destination or `com.amazonaws.{{region}}.monitoring` for a CloudWatch dataset destination.

**To configure security groups for the managed Prometheus collector**

1. Create a dedicated security group for the collector and capture the group ID:

   ```
   COLLECTOR_SG_ID=$(aws ec2 create-security-group \
       --group-name "{{pcs-prometheus-collector}}" \
       --description "Security group for managed Prometheus collector" \
       --vpc-id "$VPC_ID" \
       --query 'GroupId' \
       --output text)
   ```

1. Add an inbound rule to the cluster's security group that allows TCP traffic on port 6817 from the collector's security group. This rule permits the collector to scrape the Slurm metrics endpoint on the controller.

   Use the `--ip-permissions` form to include a rule description for auditability:

   ```
   aws ec2 authorize-security-group-ingress \
       --group-id "$CLUSTER_SG_ID" \
       --ip-permissions \
       'IpProtocol=tcp,FromPort=6817,ToPort=6817,UserIdGroupPairs=[{GroupId='"$COLLECTOR_SG_ID"',Description="Prometheus collector scrapes Slurm metrics"}]'
   ```

   Alternatively, you can use the shorter form without a rule description:

   ```
   aws ec2 authorize-security-group-ingress \
       --group-id "$CLUSTER_SG_ID" \
       --protocol tcp \
       --port 6817 \
       --source-group "$COLLECTOR_SG_ID"
   ```

1. (Optional) Lock down outbound traffic on the collector's security group. By default, a newly created security group allows all outbound traffic. If you want to enforce explicit-only egress for a higher security posture, revoke the default allow-all rule and add only the egress rules that the collector requires.

   Revoke the default allow-all egress rule:

   ```
   aws ec2 revoke-security-group-egress \
       --group-id "$COLLECTOR_SG_ID" \
       --ip-permissions '[{"IpProtocol":"-1","IpRanges":[{"CidrIp":"0.0.0.0/0"}]}]'
   ```

   Add an explicit egress rule to allow the collector to reach the controller on TCP 6817:

   ```
   aws ec2 authorize-security-group-egress \
       --group-id "$COLLECTOR_SG_ID" \
       --ip-permissions \
       'IpProtocol=tcp,FromPort=6817,ToPort=6817,UserIdGroupPairs=[{GroupId='"$CLUSTER_SG_ID"',Description="Egress to Slurm controller for metrics scraping"}]'
   ```

   Add an explicit egress rule for HTTPS (TCP 443) to reach the metrics delivery destination (Amazon Managed Service for Prometheus or CloudWatch):

   ```
   aws ec2 authorize-security-group-egress \
       --group-id "$COLLECTOR_SG_ID" \
       --ip-permissions \
       'IpProtocol=tcp,FromPort=443,ToPort=443,IpRanges=[{CidrIp=0.0.0.0/0,Description="HTTPS egress for metrics delivery"}]'
   ```

   For tighter control in subnets that use a VPC endpoint for delivery, replace the CIDR range with the VPC endpoint's security group:

   ```
   aws ec2 authorize-security-group-egress \
       --group-id "$COLLECTOR_SG_ID" \
       --ip-permissions \
       'IpProtocol=tcp,FromPort=443,ToPort=443,UserIdGroupPairs=[{GroupId='"$VPCE_SG_ID"',Description="HTTPS egress to VPC endpoint for metrics delivery"}]'
   ```
**Note**  
If you did not revoke the default egress rule, you can skip this step. The default rule already permits all outbound traffic, including traffic to port 6817 and port 443.

1. (Isolated clusters) If your collector subnets have no internet access and use an interface VPC endpoint to reach the destination service, add an inbound rule to the VPC endpoint's security group. This rule allows the collector's HTTPS traffic to reach the endpoint network interfaces. This is a commonly missed step.

   ```
   aws ec2 authorize-security-group-ingress \
       --group-id "$VPCE_SG_ID" \
       --ip-permissions \
       'IpProtocol=tcp,FromPort=443,ToPort=443,UserIdGroupPairs=[{GroupId='"$COLLECTOR_SG_ID"',Description="Managed collector reaches service endpoint"}]'
   ```

**Note**  
As a simpler but less restrictive alternative, you can attach the controller's existing security group to the collector if that security group contains a self-referencing rule that allows traffic from itself. This satisfies the connectivity requirement without creating a dedicated group.  
For example, if your cluster's security group (`sg-0abc1234def56789a`) already allows all TCP traffic from itself, pass that security group ID in the `--security-group-ids` parameter when you create the scraper:  

```
aws amp create-scraper \
    --source '{"vpcConfiguration":{"subnetIds":["{{subnet-id-1}}","{{subnet-id-2}}"],"securityGroupIds":["sg-0abc1234def56789a"]}}' \
    ...
```
However, the dedicated security group approach described in the preceding procedure provides a higher security bar with explicit, auditable rules.

For more information about security group rules, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html) in the *Amazon VPC User Guide*.

## Create the managed collector
<a name="slurm-metrics-prometheus-create-scraper"></a>

Use the AWS CLI to create a VPC-connected managed collector that scrapes your cluster controller and delivers metrics to your chosen destination.

**To create a managed collector for Slurm metrics**

1. Save the scrape configuration to a local YAML file named `scrape-config.yaml`. For a suggested configuration, see [Suggested scrape configuration](#slurm-metrics-prometheus-scrape-config).

1. Create a JSON input file named `create-scraper-input.json` with the following structure. Choose the `destination` block that matches your target.

   ```
   {
     "source": {
       "vpcConfiguration": {
         "subnetIds": ["{{subnet-1}}", "{{subnet-2}}"],
         "securityGroupIds": ["{{sg-collector}}"]
       }
     },
     "destination": { ... },
     "scrapeConfiguration": {
       "configurationBlob": "{{raw-yaml-contents}}"
     }
   }
   ```

   Replace:
   + {{subnet-1}} and {{subnet-2}} – At least two subnet IDs in different Availability Zones within the same VPC as the cluster controller.
   + {{sg-collector}} – The security group ID for the managed collector.
   + {{raw-yaml-contents}} – The full text of your `scrape-config.yaml` file, pasted as a single JSON string value. The AWS CLI base64-encodes the value on the wire automatically.

   For the `destination` field, use one of the following:

   **Destination: Amazon Managed Service for Prometheus workspace**

   ```
   "destination": {
     "ampConfiguration": {
       "workspaceArn": "arn:aws:aps:{{region}}:{{account-id}}:workspace/{{workspace-id}}"
     }
   }
   ```

   **Destination: CloudWatch dataset**

   ```
   "destination": {
     "cloudWatchConfiguration": {
       "datasetArn": "arn:aws:cloudwatch:{{region}}:{{account-id}}:dataset/default"
     }
   }
   ```

   For the full set of parameters, see [create-scraper](https://docs.aws.amazon.com/cli/latest/reference/amp/create-scraper.html) in the *AWS CLI Command Reference*.

1. Create the scraper:

   ```
   aws amp create-scraper --cli-input-json file://create-scraper-input.json
   ```

   The command returns a `scraperId` and a status of `CREATING`.

1. Wait for the scraper status to change to `ACTIVE` (typically 5–15 minutes):

   ```
   aws amp describe-scraper --scraper-id {{scraper-id}}
   ```

   Replace {{scraper-id}} with the ID returned in the previous step. You cannot delete a scraper until it reaches `ACTIVE` status.

## Find the cluster controller endpoint
<a name="slurm-metrics-prometheus-controller-endpoint"></a>

The scrape configuration requires the private IP address of your AWS PCS cluster controller. Use one of the following methods to find it.

------
#### [ AWS Management Console ]

1. Open the AWS PCS console at [https://console.aws.amazon.com/pcs/](https://console.aws.amazon.com/pcs/).

1. Choose your cluster from the list.

1. In the cluster configuration details, locate the **Endpoints** section.

1. Note the private IP address and port for **Slurm controller (slurmctld)**. The port is 6817.

------
#### [ AWS CLI ]

1. Run the following command. Replace {{cluster-identifier}} with your cluster name or ID.

   ```
   aws pcs get-cluster --cluster-identifier {{cluster-identifier}}
   ```

   In the response, locate the `SLURMCTLD` entry in the `endpoints` array. The `privateIpAddress` value is the controller endpoint you need for the scrape configuration. Here is an example:

   ```
   "endpoints": [
       {
           "type": "SLURMCTLD",
           "privateIpAddress": "192.0.2.1",
           "port": "6817"
       },
       {
           "type": "SLURMRESTD",
           "privateIpAddress": "192.0.2.1",
           "port": "6820"
       }
   ]
   ```

   Use the `privateIpAddress` from the `SLURMCTLD` entry (port 6817) as the {{controller-endpoint}} value in your scrape configuration.

1. Alternatively, extract only the controller IP address directly:

   ```
   aws pcs get-cluster --cluster-identifier {{cluster-identifier}} \
       --query 'cluster.endpoints[?type==`SLURMCTLD`].privateIpAddress' \
       --output text
   ```

------

## Suggested scrape configuration
<a name="slurm-metrics-prometheus-scrape-config"></a>

The following YAML configuration scrapes four Slurm metrics endpoints (jobs, nodes, scheduler, and partitions) from the cluster controller. Each endpoint is defined as a separate job so that you can identify metrics by source in your queries.

```
global:
  scrape_interval: 60s
  scrape_timeout: 30s

scrape_configs:
  - job_name: 'slurm-jobs'
    metrics_path: /metrics/jobs
    static_configs:
      - targets:
          - '{{controller-endpoint}}:6817'
    relabel_configs:
      - target_label: cluster
        replacement: '{{my-cluster-name}}'

  - job_name: 'slurm-nodes'
    metrics_path: /metrics/nodes
    static_configs:
      - targets:
          - '{{controller-endpoint}}:6817'
    relabel_configs:
      - target_label: cluster
        replacement: '{{my-cluster-name}}'

  - job_name: 'slurm-scheduler'
    metrics_path: /metrics/scheduler
    static_configs:
      - targets:
          - '{{controller-endpoint}}:6817'
    relabel_configs:
      - target_label: cluster
        replacement: '{{my-cluster-name}}'

  - job_name: 'slurm-partitions'
    metrics_path: /metrics/partitions
    static_configs:
      - targets:
          - '{{controller-endpoint}}:6817'
    relabel_configs:
      - target_label: cluster
        replacement: '{{my-cluster-name}}'
```

Replace:
+ {{controller-endpoint}} – The private IP address of your AWS PCS cluster controller. For instructions on finding this value, see [Find the cluster controller endpoint](#slurm-metrics-prometheus-controller-endpoint).
+ {{my-cluster-name}} – A label that identifies your cluster. The `relabel_configs` block stamps a `cluster` label on every metric from this scraper. Always filter queries on the `cluster` label. Series from a scraper that did not stamp the label appear as duplicate unlabeled series until they age out.

The minimum `scrape_interval` for a managed collector is 30 seconds. This configuration uses 60 seconds because scraping places load on the Slurm controller (slurmctld). Querying metrics acquires internal locks and reads in-memory data structures. This activity can affect scheduler performance on busy clusters. The Slurm Metrics Guide recommends a scrape interval of 60–120 seconds to minimize performance impact.

**Note**  
This configuration does not include the `/metrics/jobs-users-accts` endpoint. Slurm documentation warns that this endpoint produces an unbounded number of series and is unsuitable for stored monitoring. Do not scrape the bare `/metrics` index either, because it combines all sub-endpoint data into a single response.

For more information about supported scrape configuration options, see [Scraper configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/managed-prometheus-collectors-scraper-configuration.html) in the *Amazon CloudWatch User Guide*.

## Verify metrics delivery
<a name="slurm-metrics-prometheus-verify"></a>

After the scraper reaches `ACTIVE` status, the first datapoints appear approximately one scrape interval plus delivery time later. Use the verification method that matches your destination.

### Verify delivery to an Amazon Managed Service for Prometheus workspace
<a name="slurm-metrics-prometheus-verify-amp"></a>

Send a SigV4-signed request to list available metric names from your workspace:

```
awscurl --service aps --region {{region}} \
    "https://aps-workspaces.{{region}}.amazonaws.com/workspaces/{{workspace-id}}/api/v1/label/__name__/values"
```

The calling principal needs `aps:QueryMetrics` and `aps:GetLabels` permissions (or the `AmazonPrometheusQueryAccess` managed policy).

### Verify delivery to a CloudWatch dataset
<a name="slurm-metrics-prometheus-verify-cw"></a>

Send a SigV4-signed request to list available metric names from your CloudWatch dataset:

```
awscurl --service monitoring --region {{region}} \
    "https://monitoring.{{region}}.amazonaws.com/api/v1/label/__name__/values"
```

The calling principal needs `cloudwatch:GetMetricData` and `cloudwatch:ListMetrics` permissions.

**Important**  
Metrics delivered to a CloudWatch dataset are stored as OpenTelemetry (OTel) metrics. They do *not* appear in the classic CloudWatch Metrics namespace browser or in the output of `aws cloudwatch list-metrics`. You must query them with PromQL.

For either destination, look for metric names that begin with `slurm_`, such as `slurm_nodes`, `slurm_jobs_running`, or `slurm_node_cpus`. If no Slurm metrics appear, verify the following:
+ The scraper status is `ACTIVE`.
+ Security group rules allow the collector to reach port 6817 on the controller.
+ The Slurm metrics endpoint is enabled on the cluster.

## Query Slurm metrics with PromQL
<a name="slurm-metrics-prometheus-query"></a>

You query the collected Slurm metrics using PromQL. The same queries work against either destination. The query method depends on where you delivered the metrics.

### Query an Amazon Managed Service for Prometheus workspace
<a name="slurm-metrics-prometheus-query-amp"></a>
+ **HTTP API** – Send SigV4-signed requests (service name `aps`) to `https://aps-workspaces.{{region}}.amazonaws.com/workspaces/{{workspace-id}}/api/v1/query` or `/api/v1/query_range`.
+ **Grafana** – Add a Prometheus data source with SigV4 authentication and service name `aps`. For instructions on querying with Grafana, see [Query using Grafana](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-query-standalone-grafana.html) in the *Amazon Managed Service for Prometheus User Guide*.

The following example uses `awscurl` to query running jobs from an Amazon Managed Service for Prometheus workspace:

```
awscurl --service aps --region {{region}} \
    -X POST "https://aps-workspaces.{{region}}.amazonaws.com/workspaces/{{workspace-id}}/api/v1/query" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "query=slurm_jobs_running"
```

The calling principal needs `aps:QueryMetrics`, `aps:GetMetricMetadata`, `aps:GetSeries`, and `aps:GetLabels` permissions (or the `AmazonPrometheusQueryAccess` managed policy).

### Query a CloudWatch dataset
<a name="slurm-metrics-prometheus-query-cw"></a>
+ **CloudWatch console** – Open CloudWatch, choose **Query Studio**, and select **PromQL** from the query language menu.
+ **HTTP API** – Send SigV4-signed requests (service name `monitoring`) to `https://monitoring.{{region}}.amazonaws.com/api/v1/query` or `/api/v1/query_range`.
+ **Grafana** – Add a Prometheus data source with URL `https://monitoring.{{region}}.amazonaws.com`, SigV4 authentication, and service name `monitoring`. For instructions on querying CloudWatch metrics with PromQL in Grafana, see [Query CloudWatch metrics with PromQL in Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/cloudwatch-promql.html) in the *Amazon Managed Grafana User Guide*.

The following example uses `awscurl` to query running jobs from a CloudWatch dataset:

```
awscurl --service monitoring --region {{region}} \
    -X POST "https://monitoring.{{region}}.amazonaws.com/api/v1/query" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "query=slurm_jobs_running"
```

The calling principal needs `cloudwatch:GetMetricData` and `cloudwatch:ListMetrics` permissions.

### Example PromQL queries
<a name="slurm-metrics-prometheus-query-examples"></a>

The following queries work against either destination. Replace {{my-cluster-name}} with the value you set in your scrape configuration's `cluster` relabel.

CPU utilization percentage  

```
100 * slurm_node_cpus_alloc{cluster="{{my-cluster-name}}"} / slurm_node_cpus{cluster="{{my-cluster-name}}"}
```

Pending jobs (queue backlog)  

```
slurm_jobs_pending{cluster="{{my-cluster-name}}"}
```

Running jobs  

```
slurm_jobs_running{cluster="{{my-cluster-name}}"}
```

Job throughput  

```
slurm_jobs_completed{cluster="{{my-cluster-name}}"}
```

For more information about available metrics and scraping configuration, see the [Metrics Guide](https://slurm.schedmd.com/metrics.html) on the Slurm website.
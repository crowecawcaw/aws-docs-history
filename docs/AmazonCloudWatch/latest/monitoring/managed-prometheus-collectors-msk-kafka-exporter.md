

# Collect Amazon MSK consumer-group metrics in CloudWatch
<a name="managed-prometheus-collectors-msk-kafka-exporter"></a>

With an Amazon CloudWatch managed Prometheus collector and a managed Kafka exporter, you can collect consumer-group metrics from your Amazon MSK Provisioned clusters, such as consumer lag, committed offsets, and the number of members in each consumer group. The collector runs the exporter for you and delivers the metrics directly to CloudWatch, so you do not deploy or operate an exporter yourself. The collector connects to your cluster with AWS Identity and Access Management (IAM) authentication, and you grant it access with an Amazon MSK cluster policy.

Consumer-group metrics do not require Open Monitoring. If you also collect JMX or Node Exporter metrics, keep the jobs from [Integrate Amazon MSK](managed-prometheus-collectors-msk-setup.md).

## Prerequisites
<a name="managed-prometheus-collectors-msk-kafka-exporter-prerequisites"></a>

Before you create a scraper, make sure that you have the following:
+ An active Amazon MSK Provisioned cluster with Standard brokers and Apache Kafka version 3.6.0 or later. The cluster must have IAM authentication turned on and be in the same account and AWS Region as the scraper.
+ At least two subnets in different Availability Zones in the cluster's VPC, with DNS enabled.
+ An inbound rule on the cluster's security group that allows TCP traffic on port 9098 from the security group that you provide for the scraper.
+ Permission to create a scraper and to read and change the cluster policy (`kafka:GetClusterPolicy` and `kafka:PutClusterPolicy`).

For additional caller-permission and AWS CLI requirements, see [Prerequisites](https://docs.aws.amazon.com/prometheus/latest/userguide/prom-msk-kafka-exporter.html#prom-msk-kafka-exporter-prerequisites) in the Amazon Managed Service for Prometheus User Guide.

This exporter does not support Amazon MSK Serverless. Use the [metrics that Amazon MSK sends to CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/metrics-details.html) for Serverless.

## Step 1: Create a scraper with a CloudWatch destination
<a name="managed-prometheus-collectors-msk-kafka-exporter-create"></a>

Save the following YAML scrape configuration as `msk-consumer.yaml`. Replace the cluster ARN. For an existing scraper, add this job to its full configuration and keep any existing jobs. Then update the scraper as described in [Update or remove the exporter](https://docs.aws.amazon.com/prometheus/latest/userguide/prom-msk-kafka-exporter.html#prom-msk-kafka-exporter-update).

```
global:
  scrape_interval: 30s
scrape_configs:
  - job_name: kafka-exporter
    relabel_configs:
      - target_label: clusterArn
        replacement: 'arn:aws:kafka:{{us-west-2}}:{{111122223333}}:cluster/{{my-cluster}}/{{cluster-id}}'
    metric_relabel_configs:
      - source_labels: [__name__]
        regex: kafka_consumergroup_(current_offset|members|lag)
        action: keep
```

Keep the job name `kafka-exporter`. The collector configures its scrape target automatically. The `clusterArn` label keeps metrics from different clusters apart when you query them. Its value must match the cluster ARN in your request. The `metric_relabel_configs` rule keeps three consumer-group metrics: lag, committed offsets, and members. The exporter can send more metrics, and Amazon MSK already provides some of that information. For details, see [Create a scrape configuration](https://docs.aws.amazon.com/prometheus/latest/userguide/prom-msk-kafka-exporter.html#prom-msk-kafka-exporter-configure).

Run the following AWS CLI command to create the scraper. Replace the Region, account ID, cluster ARN, subnets, security group, and both filters. The example selects topics that start with `orders` and consumer groups that start with `payments`. To select all topics or all consumer groups, omit the filter. Consumer-group metrics can also include other topics that a selected consumer group consumes. To control which metrics reach CloudWatch, use `metric_relabel_configs` in your scrape configuration.

```
aws amp create-scraper \
  --region {{us-west-2}} \
  --alias msk-consumer-metrics \
  --source '{"vpcConfiguration":{"subnetIds":["{{subnet-subnet-id-1}}","{{subnet-subnet-id-2}}"],"securityGroupIds":["{{sg-security-group-id}}"]}}' \
  --exporters '[{"kafkaConfiguration":{"clusterArn":"arn:aws:kafka:{{us-west-2}}:{{111122223333}}:cluster/{{my-cluster}}/{{cluster-id}}","topicFilter":"{{^orders.*$}}","consumerGroupFilter":"{{^payments.*$}}"}}]' \
  --cli-binary-format base64 \
  --scrape-configuration "configurationBlob=$(base64 < msk-consumer.yaml | tr -d '\n')" \
  --destination '{"cloudWatchConfiguration":{"datasetArn":"arn:aws:cloudwatch:{{us-west-2}}:{{111122223333}}:dataset/default"}}'
```

Record the scraper ID. Check its status with the `aws amp describe-scraper` AWS CLI command, and continue when `scraper.status.statusCode` is `ACTIVE`. The scraper collects no Kafka metrics until you grant it access to the cluster in the next step.

## Step 2: Grant the scraper access to the cluster
<a name="managed-prometheus-collectors-msk-kafka-exporter-access"></a>

Add an Amazon MSK cluster policy that allows the scraper's service-linked role to connect to the cluster and to describe its topics and consumer groups. After you add the policy, collection starts on its own, and the first metrics can take a few minutes to appear. You do not need to update the scraper.

Grant the scraper's service-linked role. Do not use an account root principal or a role ARN with a wildcard. Amazon MSK accepts a root principal, but it grants the scraper nothing, and it rejects a wildcard role ARN.

**To add the cluster policy**

1. Get the scraper's role ARN:

   ```
   aws amp describe-scraper \
     --region {{us-west-2}} \
     --scraper-id {{scraper-id}} \
     --query scraper.roleArn --output text
   ```

1. Save the following policy as `policy.json`. Replace the role ARN, Region, account ID, cluster name, and cluster ID.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": { "AWS": "{{scraper-role-arn}}" },
         "Action": "kafka-cluster:Connect",
         "Resource": "arn:aws:kafka:{{us-west-2}}:{{111122223333}}:cluster/{{my-cluster}}/{{cluster-id}}"
       },
       {
         "Effect": "Allow",
         "Principal": { "AWS": "{{scraper-role-arn}}" },
         "Action": "kafka-cluster:DescribeTopic",
         "Resource": "arn:aws:kafka:{{us-west-2}}:{{111122223333}}:topic/{{my-cluster}}/{{cluster-id}}/*"
       },
       {
         "Effect": "Allow",
         "Principal": { "AWS": "{{scraper-role-arn}}" },
         "Action": "kafka-cluster:DescribeGroup",
         "Resource": "arn:aws:kafka:{{us-west-2}}:{{111122223333}}:group/{{my-cluster}}/{{cluster-id}}/*"
       }
     ]
   }
   ```

1. Check whether the cluster already has a policy:

   ```
   aws kafka get-cluster-policy \
     --region {{us-west-2}} \
     --cluster-arn arn:aws:kafka:{{us-west-2}}:{{111122223333}}:cluster/{{my-cluster}}/{{cluster-id}}
   ```

   A `NotFoundException` error means that the cluster has no policy.

1. If the cluster has no policy, add yours:

   ```
   aws kafka put-cluster-policy \
     --region {{us-west-2}} \
     --cluster-arn arn:aws:kafka:{{us-west-2}}:{{111122223333}}:cluster/{{my-cluster}}/{{cluster-id}} \
     --policy file://policy.json
   ```

   If the cluster already has a policy, `put-cluster-policy` replaces it. The `Policy` value from `get-cluster-policy` is the existing policy as a JSON string. Add its statements to the `Statement` list in `policy.json`. Then run `put-cluster-policy` with `--current-version` and the `CurrentVersion` value from `get-cluster-policy`.

To grant every scraper in the account, to limit the topics and groups, or to see the full merge command, see [Grant the scraper access to the cluster](https://docs.aws.amazon.com/prometheus/latest/userguide/prom-msk-kafka-exporter.html#prom-msk-kafka-exporter-access) in the Amazon Managed Service for Prometheus User Guide.

## Step 3: Validate metrics collection
<a name="managed-prometheus-collectors-msk-kafka-exporter-check"></a>

To confirm that the collector is delivering consumer-group metrics, choose the scraper's Region and run each of the following queries separately in CloudWatch with [Query Studio](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL-QueryStudio.html). Replace the cluster ARN.

```
kafka_consumergroup_members{"@instrumentation.cloudwatch.managed-collector.scraper-type"="msk", clusterArn="arn:aws:kafka:{{us-west-2}}:{{111122223333}}:cluster/{{my-cluster}}/{{cluster-id}}"}
```

```
kafka_consumergroup_current_offset{"@instrumentation.cloudwatch.managed-collector.scraper-type"="msk", clusterArn="arn:aws:kafka:{{us-west-2}}:{{111122223333}}:cluster/{{my-cluster}}/{{cluster-id}}"}
```

```
kafka_consumergroup_lag{"@instrumentation.cloudwatch.managed-collector.scraper-type"="msk", clusterArn="arn:aws:kafka:{{us-west-2}}:{{111122223333}}:cluster/{{my-cluster}}/{{cluster-id}}"}
```

A matching group must exist for its metrics to appear. The first metrics can take a few minutes to appear after you add the cluster policy.

If the scraper is `ACTIVE` but no `kafka_consumergroup_*` metrics appear under the service name `kafka-exporter`, check the cluster policy. Confirm that it grants the three actions to the scraper's current service-linked role ARN. If you re-created the scraper, its role ARN changed. If you use the account-wide policy, confirm that every statement keeps both `StringEquals` on `aws:PrincipalAccount` and `ArnLike` on `aws:PrincipalArn`. You do not need to update the scraper after you fix the policy.

For other checks, see [Validate metrics collection](https://docs.aws.amazon.com/prometheus/latest/userguide/prom-msk-kafka-exporter.html#prom-msk-kafka-exporter-verify). Those checks cover the cluster policy, caller permissions, IAM broker connectivity, collection filters, and metric labels. The `up` query on that page applies only to an Amazon Managed Service for Prometheus workspace destination. If the cluster policy is correct and metrics still do not appear on a cluster with many topics and consumer groups, try narrowing `topicFilter` and `consumerGroupFilter`.

For information about these metrics, including the `-1` value when a group has no committed offset for a topic and partition, see [Consumer-group metrics](https://docs.aws.amazon.com/prometheus/latest/userguide/prom-msk-consumer-metrics.html).

## Update or remove the exporter
<a name="managed-prometheus-collectors-msk-kafka-exporter-update"></a>

Omitting `exporters` in an `update-scraper` request keeps the current exporter. An empty list removes it. Removing the cluster policy does not stop collection right away. First remove the exporter or delete the scraper, and confirm with `aws amp describe-scraper` that the scraper status is `ACTIVE` and the exporter is gone, or that the scraper no longer exists. Then remove the policy statements. For the commands, see [Update or remove the exporter](https://docs.aws.amazon.com/prometheus/latest/userguide/prom-msk-kafka-exporter.html#prom-msk-kafka-exporter-update).
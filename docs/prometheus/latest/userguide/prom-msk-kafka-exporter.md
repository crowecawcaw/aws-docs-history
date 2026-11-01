

# Collect Amazon MSK consumer-group metrics
<a name="prom-msk-kafka-exporter"></a>

With a managed Kafka exporter, an Amazon Managed Service for Prometheus collector collects consumer-group metrics from your Amazon MSK cluster, such as consumer lag, committed offsets, and the number of members in each consumer group. Amazon Managed Service for Prometheus runs the exporter for you, so you do not have to install or operate an exporter yourself. Your destination can be an Amazon Managed Service for Prometheus workspace or Amazon CloudWatch. These metrics complement the JMX and Node Exporter metrics that the collector scrapes from Open Monitoring.

The scraper connects to your cluster with AWS Identity and Access Management (IAM) authentication. You grant the scraper access to the cluster with an Amazon MSK cluster policy. To collect consumer-group metrics, create a scrape configuration, create a scraper, and then grant the scraper access to your cluster, as described in the following sections.

For information about the metrics, see [Consumer-group metrics](prom-msk-consumer-metrics.md). To send the metrics to Amazon CloudWatch, see [Collect Amazon MSK consumer-group metrics in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/managed-prometheus-collectors-msk-kafka-exporter.html).

## Prerequisites
<a name="prom-msk-kafka-exporter-prerequisites"></a>

There are a few prerequisites for collecting consumer-group metrics:
+ An active Amazon MSK Provisioned cluster with Standard brokers and Apache Kafka version 3.6.0 or later, in the same account and AWS Region as the scraper.
+ IAM access control turned on for the cluster. You can keep TLS client authentication turned on at the same time, so clients that use certificates can continue to connect.
+ At least two subnets in different Availability Zones in the cluster's Amazon VPC, with DNS enabled.
+ Security groups that allow the scraper to reach the cluster's private IAM broker endpoints on port 9098. Add an inbound rule to the cluster's security group that allows TCP traffic on port 9098 from the security group that you provide for the scraper.
+ An Amazon Managed Service for Prometheus workspace in the scraper's Region, and an AWS CLI version that supports `kafkaConfiguration` in `create-scraper` and `update-scraper`.
+ Permission to create or update a scraper and to validate the cluster: `kafka:DescribeClusterV2`, `kafka:GetBootstrapBrokers`, `kafka-cluster:Connect`, and `kafka-cluster:DescribeTopic`. To add the cluster policy, you also need `kafka:GetClusterPolicy` and `kafka:PutClusterPolicy`. For the permissions to create the scraper's service-linked role, see [Service-linked role permissions](using-service-linked-roles.md#service-linked-role-permissions-prom-scraper).

The scraper uses its service-linked role to connect to the cluster, so you do not provide a role for the exporter. By default, the role has no permissions for your cluster. You grant them in [Grant the scraper access to the cluster](#prom-msk-kafka-exporter-access).

The managed Kafka exporter does not support the following clusters:
+ Amazon MSK Serverless clusters. Serverless clusters do not accept cluster policies with `kafka-cluster` actions. Use the [metrics that Amazon MSK sends to CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/metrics-details.html) instead.
+ Clusters that do not have IAM authentication turned on.
+ Clusters in a different account or Region from the scraper.

Open Monitoring and broker ports 11001 and 11002 are needed only if you also collect JMX and Node Exporter metrics.

## Create a scrape configuration
<a name="prom-msk-kafka-exporter-configure"></a>

You provide a scrape configuration when you create the scraper. The managed collector connects to the cluster that you specify and collects its metrics automatically, so you do not specify scrape targets in the configuration. The configuration must include a `scrape_configs` section with a job whose `job_name` is exactly `kafka-exporter`. A configuration that does not contain a job named `kafka-exporter` is rejected. The collector sets the scrape interval for this job.

Use the scrape configuration to add labels and to filter the collected metrics. The following example keeps consumer lag, committed offsets, and group membership. It also adds a `clusterArn` label so that you can tell clusters apart when you query. Replace the cluster ARN with your cluster's ARN, and save the configuration as `msk-consumer.yaml`. Use the same cluster ARN when you create the scraper.

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

The exporter can also send other metrics, such as topic and partition offsets and partition counts. Amazon MSK already provides some of this information through Open Monitoring and the [metrics that Amazon MSK sends to CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/metrics-details.html). To collect more exporter metrics, add them to the `regex`, for example `kafka_consumergroup_(current_offset|members|lag)|kafka_topic_partitions`. Each metric that you add increases the number of series that you ingest.

To add the exporter to an existing scraper, add the `kafka-exporter` job to the scraper's full scrape configuration, and keep its other jobs. Then update the scraper as described in [Update or remove the exporter](#prom-msk-kafka-exporter-update). You can relabel metrics in this job, but you cannot use relabel rules to change how the collector connects to the exporter.

## Create a scraper
<a name="prom-msk-kafka-exporter-create"></a>

To tell the scraper which cluster to collect from, you specify the cluster in the `exporters` field of the request. For an Amazon MSK cluster, provide a `kafkaConfiguration` with the `clusterArn` of the cluster. You can also set a `topicFilter` and a `consumerGroupFilter` to select topics and consumer groups by name. You provide the networking (subnets and security group) separately in the `source` field.

Use the `create-scraper` command to create a scraper using the AWS Command Line Interface. The following example selects topics that start with `orders` and consumer groups that start with `payments`. Replace the {{example}} content, including both filters, with your own cluster, networking, workspace, and filter values. To select all topics or all consumer groups, omit the filter.

**Note**  
Configure the security group and subnets to match the Amazon VPC of your Amazon MSK cluster. Include at least two subnets across two Availability Zones.

```
aws amp create-scraper \
  --region {{us-west-2}} \
  --alias msk-consumer-metrics \
  --source '{"vpcConfiguration":{"subnetIds":["{{subnet-subnet-id-1}}","{{subnet-subnet-id-2}}"],"securityGroupIds":["{{sg-security-group-id}}"]}}' \
  --exporters '[{"kafkaConfiguration":{"clusterArn":"arn:aws:kafka:{{us-west-2}}:{{111122223333}}:cluster/{{my-cluster}}/{{cluster-id}}","topicFilter":"{{^orders.*$}}","consumerGroupFilter":"{{^payments.*$}}"}}]' \
  --cli-binary-format base64 \
  --scrape-configuration "configurationBlob=$(base64 < msk-consumer.yaml | tr -d '\n')" \
  --destination '{"ampConfiguration":{"workspaceArn":"arn:aws:aps:{{us-west-2}}:{{111122223333}}:workspace/{{workspace-id}}"}}'
```

Both filters are optional. If you omit a filter, the scraper selects all topics or all consumer groups. Each filter must be a regular expression that starts with `^` and ends with `$`, with a maximum length of 256 characters. A scraper can have one exporter.

The `topicFilter` selects the topics that the exporter reads topic metrics for. Consumer-group metrics can also include other topics that a selected consumer group consumes. To control which metrics reach your destination, use `metric_relabel_configs` in your scrape configuration.

Record the scraper ID. Check its status with the following command, and continue when the status is `ACTIVE`:

```
aws amp describe-scraper \
  --region {{us-west-2}} \
  --scraper-id {{scraper-id}} \
  --query 'scraper.status.statusCode' --output text
```

The scraper does not collect Kafka metrics until you grant it access to the cluster.

## Grant the scraper access to the cluster
<a name="prom-msk-kafka-exporter-access"></a>

The scraper needs permission to connect to your cluster and to read its topic and consumer-group metadata. Add an Amazon MSK cluster policy that allows the scraper's service-linked role the following actions:
+ `kafka-cluster:Connect` on the cluster
+ `kafka-cluster:DescribeTopic` on its topics
+ `kafka-cluster:DescribeGroup` on its consumer groups

Without this policy, the scraper is `ACTIVE` but does not collect Kafka metrics. After you add the policy, the scraper starts collecting automatically, and the first metrics can take a few minutes to appear. You do not need to update the scraper.

Grant the scraper's service-linked role, even if the scraper uses `roleConfiguration` to send metrics to a workspace in another account. Do not grant the source role or the target role.

### Grant one scraper
<a name="prom-msk-kafka-exporter-access-role"></a>

Get the scraper's role ARN with the following AWS CLI command:

```
aws amp describe-scraper \
  --region {{us-west-2}} \
  --scraper-id {{scraper-id}} \
  --query scraper.roleArn --output text
```

Each scraper has its own role, `AWSServiceRoleForAmazonPrometheusScraper_{{suffix}}`. If you re-create a scraper, grant the new role.

Save the following policy as `policy.json`. Replace the role ARN, Region, account ID, cluster name, and cluster ID.

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

To grant another scraper, add the three statements again with that scraper's role ARN. To grant fewer topics or consumer groups, edit the policy as described in [Limit the topics and consumer groups](#prom-msk-kafka-exporter-access-narrow) before you apply it.

### Apply the policy
<a name="prom-msk-kafka-exporter-access-apply"></a>

**Important**  
Do not use an account root principal, such as `arn:aws:iam::{{111122223333}}:root`. Amazon MSK accepts it, but it grants the scraper nothing. Do not use a wildcard in a role ARN as the principal. Amazon MSK rejects it with the error `The cluster policy is not valid`. To grant every scraper in the account, see [Optional: Grant every scraper in the account](#prom-msk-kafka-exporter-access-account).

To read and change the cluster policy, you need `kafka:GetClusterPolicy` and `kafka:PutClusterPolicy`.

**To add the cluster policy**

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

1. If the cluster already has a policy, merge the statements. `put-cluster-policy` replaces the whole policy document. The `Policy` value from `get-cluster-policy` is the existing policy as a JSON string. Add its statements to the `Statement` list in `policy.json`, so that the file has both the existing statements and the new ones. Then pass the `CurrentVersion` value from `get-cluster-policy`:

   ```
   aws kafka put-cluster-policy \
     --region {{us-west-2}} \
     --cluster-arn arn:aws:kafka:{{us-west-2}}:{{111122223333}}:cluster/{{my-cluster}}/{{cluster-id}} \
     --current-version {{current-version}} \
     --policy file://policy.json
   ```

### Optional: Grant every scraper in the account
<a name="prom-msk-kafka-exporter-access-account"></a>

We recommend that you grant access to individual scraper role ARNs. If you need to grant every current and future scraper in the account, you can use the following policy instead. You can add it before you create a scraper, and it keeps working when you replace one. Keep both conditions in every statement. Save the following policy as `policy.json`. Replace the Region, account ID, cluster name, and cluster ID in each statement, and apply it as described in [Apply the policy](#prom-msk-kafka-exporter-access-apply).

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "AWS": "*" },
      "Action": "kafka-cluster:Connect",
      "Resource": "arn:aws:kafka:{{us-west-2}}:{{111122223333}}:cluster/{{my-cluster}}/{{cluster-id}}",
      "Condition": {
        "StringEquals": { "aws:PrincipalAccount": "{{111122223333}}" },
        "ArnLike": { "aws:PrincipalArn": "arn:aws:iam::{{111122223333}}:role/aws-service-role/scraper.aps.amazonaws.com/AWSServiceRoleForAmazonPrometheusScraper_*" }
      }
    },
    {
      "Effect": "Allow",
      "Principal": { "AWS": "*" },
      "Action": "kafka-cluster:DescribeTopic",
      "Resource": "arn:aws:kafka:{{us-west-2}}:{{111122223333}}:topic/{{my-cluster}}/{{cluster-id}}/*",
      "Condition": {
        "StringEquals": { "aws:PrincipalAccount": "{{111122223333}}" },
        "ArnLike": { "aws:PrincipalArn": "arn:aws:iam::{{111122223333}}:role/aws-service-role/scraper.aps.amazonaws.com/AWSServiceRoleForAmazonPrometheusScraper_*" }
      }
    },
    {
      "Effect": "Allow",
      "Principal": { "AWS": "*" },
      "Action": "kafka-cluster:DescribeGroup",
      "Resource": "arn:aws:kafka:{{us-west-2}}:{{111122223333}}:group/{{my-cluster}}/{{cluster-id}}/*",
      "Condition": {
        "StringEquals": { "aws:PrincipalAccount": "{{111122223333}}" },
        "ArnLike": { "aws:PrincipalArn": "arn:aws:iam::{{111122223333}}:role/aws-service-role/scraper.aps.amazonaws.com/AWSServiceRoleForAmazonPrometheusScraper_*" }
      }
    }
  ]
}
```

This policy allows every current and future scraper in the account. The `aws:PrincipalAccount` and `ArnLike` conditions are what limit it. Do not remove either condition.

### Limit the topics and consumer groups
<a name="prom-msk-kafka-exporter-access-narrow"></a>

Both policies grant all topics and consumer groups in the cluster. To grant fewer, replace the final `*` in the topic and group ARNs, for example `topic/{{my-cluster}}/{{cluster-id}}/orders-*`. These ARN patterns are IAM wildcards, not the `topicFilter` or `consumerGroupFilter` regular expressions. If the policy grants fewer topics or groups than the filters select, the scraper reports fewer topics and offsets.

To narrow a policy that you already applied, replace your earlier statements with the narrowed ones. Do not merge them, because the earlier statements still grant all topics and groups.

## Validate metrics collection
<a name="prom-msk-kafka-exporter-verify"></a>

To confirm that the scraper is collecting metrics, run each of the following PromQL queries separately against your workspace. For more information, see [Query your Prometheus metrics](AMP-query.md). Replace the cluster ARN. Metrics appear only for consumer groups that match your consumer-group filter and that have members or committed offsets.

```
kafka_consumergroup_members{clusterArn="arn:aws:kafka:{{us-west-2}}:{{111122223333}}:cluster/{{my-cluster}}/{{cluster-id}}"}
```

```
kafka_consumergroup_current_offset{clusterArn="arn:aws:kafka:{{us-west-2}}:{{111122223333}}:cluster/{{my-cluster}}/{{cluster-id}}"}
```

```
kafka_consumergroup_lag{clusterArn="arn:aws:kafka:{{us-west-2}}:{{111122223333}}:cluster/{{my-cluster}}/{{cluster-id}}"}
```

The first metrics can take a few minutes to appear after you add the cluster policy. If no metrics appear after that, check the following. An empty result does not mean that consumer lag is zero.
+ If the scraper is `ACTIVE`, but `up{job="kafka-exporter"}` is `0` and no `kafka_*` metrics appear, check the cluster policy. A successful create or update request does not mean that the scraper can access the cluster. Run `aws kafka get-cluster-policy`, and confirm that the policy grants `kafka-cluster:Connect`, `kafka-cluster:DescribeTopic`, and `kafka-cluster:DescribeGroup` to the scraper's current service-linked role ARN. If you re-created the scraper, its role ARN changed. If you use the account-wide policy, confirm that every statement keeps both `StringEquals` on `aws:PrincipalAccount` and `ArnLike` on `aws:PrincipalArn`. You do not need to update the scraper after you fix the policy.
+ If creation or update fails with a permissions error, give the caller the scraper and cluster permissions in [Prerequisites](#prom-msk-kafka-exporter-prerequisites), then retry the command.
+ If the scraper cannot connect to the brokers, turn on IAM authentication for the cluster. Check VPC DNS and allow the scraper's security group to reach the private IAM broker endpoints on port 9098.
+ If the scraper is `ACTIVE` but the queries return no metrics, check that `consumerGroupFilter` matches an existing consumer group. Keep the metric names and the `clusterArn`, `consumergroup`, `topic`, and `partition` labels in the scrape configuration. Use the same cluster ARN in the configuration and query. If the cluster policy grants fewer topics or groups than the filters select, fewer topics and offsets appear.
+ If the cluster policy is correct but `up{job="kafka-exporter"}` is still `0` on a cluster with many topics and consumer groups, try narrowing `topicFilter` and `consumerGroupFilter`.

## Update or remove the exporter
<a name="prom-msk-kafka-exporter-update"></a>

To change the filters, update the scraper with its full scrape configuration. The following command selects one topic and one consumer group. Keep the `kafka-exporter` job and the `clusterArn` label in your scrape configuration.

```
aws amp update-scraper \
  --region {{us-west-2}} \
  --scraper-id {{scraper-id}} \
  --exporters '[{"kafkaConfiguration":{"clusterArn":"arn:aws:kafka:{{us-west-2}}:{{111122223333}}:cluster/{{my-cluster}}/{{cluster-id}}","topicFilter":"{{^orders$}}","consumerGroupFilter":"{{^payments$}}"}}]' \
  --cli-binary-format base64 \
  --scrape-configuration "configurationBlob=$(base64 < msk-consumer.yaml | tr -d '\n')"
```

Omitting `exporters` in an update keeps the current exporter. To remove it, pass an empty list, `--exporters '[]'`, and send the full scrape configuration with the `kafka-exporter` job removed. Keep any other jobs that you still need.

The following AWS CLI command deletes the scraper and stops all of its metric collection. It does not delete the Amazon MSK cluster or the destination workspace.

```
aws amp delete-scraper \
  --region {{us-west-2}} \
  --scraper-id {{scraper-id}}
```

### Remove the scraper's access to the cluster
<a name="prom-msk-kafka-exporter-revoke"></a>

Removing the cluster policy does not stop collection right away. To stop collection, remove the exporter or delete the scraper first. Then remove the policy statements.

**To remove the scraper's access**

1. Note the scraper's role ARN. Then remove the exporter or delete the scraper, as described earlier in this section.

1. Run `aws amp describe-scraper`. Confirm that the scraper status is `ACTIVE` and that the scraper has no exporter, or that the scraper no longer exists. Other scrapers can continue to send metrics for the same cluster.

1. Run `aws kafka get-cluster-policy`. Remove only the statements that you added for the scraper. Keep statements that grant access to other clients. If you used the account-wide policy and other scrapers still need access, replace its statements with statements that name the role ARN of each scraper that keeps access.

1. Run `aws kafka put-cluster-policy` with the remaining statements and the `CurrentVersion` value, as in [Apply the policy](#prom-msk-kafka-exporter-access-apply). If no statements remain, delete the policy instead with `aws kafka delete-cluster-policy`. This command needs the `kafka:DeleteClusterPolicy` permission.
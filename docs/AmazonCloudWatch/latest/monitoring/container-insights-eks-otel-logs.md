# Sending logs to Amazon CloudWatch

OTel Container Insights collects and sends container logs to Amazon CloudWatch Logs by using the
OpenTelemetry Collector's log pipeline. The Amazon CloudWatch Observability EKS add-on deploys an
OpenTelemetry Collector as a DaemonSet that uses the filelog receiver to tail container log files,
enrich them with Kubernetes metadata, and export them to CloudWatch Logs through the CloudWatch Logs
exporter.

No additional setup is required for basic log collection. Log collection is enabled by
default when you follow the [Quick start: OTel Container Insights on Amazon EKS](container-insights-eks-otel-quickstart.md "container-insights-eks-otel-quickstart.md").

## Prerequisites

Before you configure log collection, verify that you meet the following
requirements.

- OTel Container Insights installed and the `amazon-cloudwatch-observability`
  add-on active on your cluster
- IAM permissions: `logs:CreateLogGroup`,
  `logs:CreateLogStream`, `logs:PutLogEvents`,
  `logs:DescribeLogGroups`, and `logs:DescribeLogStreams` (included
  in the `CloudWatchAgentServerPolicy` managed policy)
- Node access: the collector requires access to `/var/log/pods` on each
  node

## Log groups and sources

The following table describes the log group that OTel Container Insights creates and the
source it collects from.

| Log group                                           | Source                   | Contents                             |
| --------------------------------------------------- | ------------------------ | ------------------------------------ |
| `/aws/containerinsights/`cluster-name`/application` | `/var/log/pods/**/*.log` | All container stdout and stderr logs |

###### Note

Host and dataplane logs will be available in a future release.

## How the OTel log pipeline works

The add-on's OpenTelemetry Collector runs a log pipeline with the following
components.

- **Receivers** – The `filelog` receiver
  tails container log files from `/var/log/pods/`.
- **Processors** – The
  `k8sattributes` processor enriches logs with Kubernetes metadata. The
  `batch` processor batches log records before export. The
  `resource` processor appends resource attributes.
- **Exporters** – The
  `awscloudwatchlogs` exporter sends log records to CloudWatch Logs.

### Log enrichment

The pipeline enriches every log record with the following attributes.

- **Kubernetes resource attributes** –
  `k8s.pod.name`, `k8s.namespace.name`,
  `k8s.container.name`, `k8s.node.name`, and
  `k8s.deployment.name`
- **Pod labels** – All pod labels as
  `k8s.pod.label.*` attributes
- **Cloud attributes** –
  `cloud.region`, `cloud.account.id`, and
  `cloud.platform`
- **Cluster attributes** –
  `k8s.cluster.name`

## Customizing log collection

You can customize log collection by updating the add-on configuration values. The
following sections describe common customization options.

### Disable log collection

To disable log collection entirely, update the add-on configuration with container logs
disabled.

###### To disable log collection

- Run the following command. Replace `cluster-name` with the
  name of your Amazon EKS cluster.

```
aws eks update-addon \
  --cluster-name `cluster-name` \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"containerLogs":{"enabled":false}}' \
  --resolve-conflicts OVERWRITE
```

### Set log retention

By default, CloudWatch Logs retains log data indefinitely. To control storage costs, you can set
a retention policy on the log group.

###### To set log retention

- Run the following command. Replace `cluster-name` with the
  name of your Amazon EKS cluster. Replace `30` with the number of
  days to retain logs.

```
aws logs put-retention-policy \
  --log-group-name "/aws/containerinsights/`cluster-name`/application" \
  --retention-in-days `30`
```

## Verification

To verify that log collection is working, check that the expected log groups exist and
contain data.

###### To verify log collection

- Run the following command. Replace `cluster-name` with the
  name of your Amazon EKS cluster.

```
aws logs describe-log-groups \
  --log-group-name-prefix "/aws/containerinsights/`cluster-name`" \
  --query "logGroups[].{Name:logGroupName,StoredBytes:storedBytes}" \
  --output table
```

The output displays the log group names and the number of stored bytes. A non-zero
value for `StoredBytes` confirms that the pipeline is delivering logs.

## Troubleshooting

Use the following guidance to resolve common log collection issues.

### Log groups not created after 5 minutes

**Symptom:** The
`/aws/containerinsights/`cluster-name`/application`
log group does not appear in CloudWatch Logs after 5 minutes.

**Cause:** The collector does not have the required IAM
permissions to create log groups and log streams.

**Solution:** Verify that the IAM role associated with
the collector has the `CloudWatchAgentServerPolicy` managed policy attached. This
policy includes the `logs:CreateLogGroup` and
`logs:CreateLogStream` permissions.

### Application log group exists but is empty

**Symptom:** The application log group exists in CloudWatch Logs, but
it contains no log streams or log events.

**Cause:** This issue occurs when containers are not writing
to stdout or stderr, or the filelog receiver cannot access `/var/log/pods/` on the
node.

**Solution:** Complete the following steps to resolve this
issue.

1. Verify that your application containers write logs to stdout or stderr.
2. Check that the collector DaemonSet pod has a volume mount for
   `/var/log/pods`.

```
kubectl get daemonset -n amazon-cloudwatch -o yaml | grep -A 5 "var/log/pods"
```

3. Check the collector logs for file access errors.

```
kubectl logs -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent --tail=50 | grep -i "error\|permission"
```

### High CloudWatch Logs costs

**Symptom:** CloudWatch Logs ingestion or storage costs are higher
than expected.

**Cause:** High-volume namespaces (such as load testing or
monitoring namespaces) generate large volumes of logs.

**Solution:** Set a retention policy on the log group to
automatically delete older logs. For instructions, see [Set log retention](#container-insights-eks-otel-logs-retention "#container-insights-eks-otel-logs-retention").

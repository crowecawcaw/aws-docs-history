# Configure CloudWatch agent for Amazon EMR 7.0.0

You can configure the Amazon CloudWatch agent to use additional system metrics beyond those
that [the default CloudWatch agent configuration](AmazonCloudWatchAgent-metrics.md "AmazonCloudWatchAgent-metrics.md")
provides. The configuration for 7.0.0 requires the use of bootstrap actions, which
we've provided examples for in the following sections. In an upcoming release, Amazon EMR
will provide additional configuration options through the Amazon EMR API.

###### Topics

- [Configure additional system
  metrics with Amazon EMR 7.0.0](#AmazonCloudWatchAgent-config-700-add-metrics "#AmazonCloudWatchAgent-config-700-add-metrics")
- [Configure application metrics
  with Amazon EMR 7.0.0](#AmazonCloudWatchAgent-config-700-app-metrics "#AmazonCloudWatchAgent-config-700-app-metrics")
- [Configure Amazon Managed Service for Prometheus as cloud
  storage for metrics with Amazon EMR 7.0.0](#AmazonCloudWatchAgent-config-700-prometheus "#AmazonCloudWatchAgent-config-700-prometheus")

## Configure additional system

metrics with Amazon EMR 7.0.0

Use the following steps to configure the agent to use a different set of
system metrics in Amazon EMR 7.0.0:

1. Create or choose a bucket in your Amazon S3 account where you want to store
   the configuration files that specify the CloudWatch agent metrics.
2. Create the `emr-amazon-cloudwatch-agent.json`
   configuration file with your preferred metrics specified. To do this,
   use one of the methods explained in [Create the CloudWatch agent configuration file](../../../AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file.md "../../../AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file.md"). For more
   information about the structure of the CloudWatch agent configuration file, see
   [Manually create or edit the CloudWatch agent configuration file](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.md") in
   the _Amazon CloudWatch User Guide_.
3. Next, navigate to the aws-emr-utilities repo on GitHub and
   download the following system metrics scripts:
   - [`install_system_metrics_launcher.sh`](https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/system-metrics/install_system_metrics_launcher.sh "https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/system-metrics/install_system_metrics_launcher.sh")
     – A script that downloads and then runs
     `install_system_metrics.sh` in the
     background so that the node can finish bootstrapping.
   - [`install_system_metrics.sh`](https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/system-metrics/install_system_metrics.sh "https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/system-metrics/install_system_metrics.sh")
     – A script that waits for the instance it runs on to
     finish bootstrapping, then downloads and applies the
     configuration in the JSON file.

4. Open each SH file and replace
   `amzn-s3-demo-bucket`
   with the name of your bucket from Step 1.
5. Upload the one JSON and two SH files to your S3 bucket.
6. Now, you can navigate to the Amazon EMR console and create a new cluster
   with the CloudWatch agent. Under **EMR on EC2** in the left
   navigation, select **Clusters** and then
   **Create cluster**.
7. In the **Name and applications** section, choose an
   Amazon EMR release of 7.0.0 or higher.
8. Under **Application bundle**, select the bundle or
   apps that you want to install to your cluster, and include
   **Amazon CloudWatch Agent** with your
   selections.
9. In the **Bootstrap actions** section, select
   **Add**.
   - For the **Name**, insert
     `install_system_metrics_launcher.sh`.
   - For the **Script location**, insert
     `s3://`amzn-s3-demo-bucket`/install_system_metrics_launcher.sh`.
     Replace `amzn-s3-demo-bucket`
     with the path to your S3 bucket.
   - Leave the **Arguments** block empty.

10. Select **Add bootstrap action**.
11. Continue to create the cluster to serve your workload needs.

When your cluster launches, the CloudWatch agent publishes the system metrics that
you specified in the configuration file to CloudWatch.

## Configure application metrics

with Amazon EMR 7.0.0

You can configure the Amazon CloudWatch agent to publish application metrics for HDFS
and YARN in addition to system metrics. Use the following steps to configure the
agent to publish application metrics:

1. Create or choose a bucket in your Amazon S3 account where you want to store
   the configuration files that specify the CloudWatch agent metrics.
2. Next, navigate to the aws-emr-utilities repo on GitHub and
   download the following scripts:
   - [`install_app_metrics_launcher.sh`](https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/application-metrics/install_app_metrics_launcher.sh "https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/application-metrics/install_app_metrics_launcher.sh")
     – A script that downloads and then runs
     `install_app_metrics.sh` in the
     background so that the node can finish bootstrapping.
   - [`install_app_metrics.sh`](https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/application-metrics/install_app_metrics.sh "https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/application-metrics/install_app_metrics.sh")
     – A script that waits for the instance it runs on to
     finish bootstrapping, then downloads and applies the
     configuration in the YAML files that you'll download in an
     upcoming step.

3. Open each file and replace
   `amzn-s3-demo-bucket`
   with the name of your bucket from Step 1.
4. Next, download the following YAML mapping files. For information about
   how these YAML files are structured, see [`javaagent`](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/jmx-metrics/javaagent "https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/jmx-metrics/javaagent") in the
   _OpenTelemetry Instrumentation for
   Java_ GitHub repo.
   - [`datanode-metrics.yaml`](https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/application-metrics/mappings/datanode-metrics.yaml "https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/application-metrics/mappings/datanode-metrics.yaml")
     – The configuration for Hadoop DataNode
     metrics.
   - [`namenode-metrics.yaml`](https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/application-metrics/mappings/namenode-metrics.yaml "https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/application-metrics/mappings/namenode-metrics.yaml")
     – The configuration for Hadoop NameNode
     metrics.
   - [`nodemanager-metrics.yaml`](https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/application-metrics/mappings/nodemanager-metrics.yaml "https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/application-metrics/mappings/nodemanager-metrics.yaml")
     – The configuration for Yarn NodeManager
     metrics.
   - [`resourcemanager-metrics.yaml`](https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/application-metrics/mappings/resourcemanager-metrics.yaml "https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/application-metrics/mappings/resourcemanager-metrics.yaml")
     – The configuration for Yarn
     ResourceManager metrics.

5. Upload the two SH and four YAML files to your S3 bucket.
6. Now, you can navigate to the Amazon EMR console and create a new cluster
   with the CloudWatch agent. Under **EMR on EC2** in the left
   navigation, select **Clusters** and then
   **Create cluster**.
7. In the **Name and applications** section, choose an
   Amazon EMR release of 7.0.0 or higher.
8. Under **Application bundle**, select the bundle or
   custom group of apps that you want to install to your cluster, and
   include **CloudWatch agent** with your selections.
9. In the **Bootstrap actions** section, select
   **Add**.
   - For the **Name**, insert
     `install_app_metrics_launcher.sh`.
   - For the **Script location**, insert
     `s3://`amzn-s3-demo-bucket`/install_app_metrics_launcher.sh`.
     Replace `amzn-s3-demo-bucket`
     with the path to your S3 bucket.
   - Leave the **Arguments** block empty.

10. Select **Add bootstrap action**.
11. Continue to create the cluster to serve your workload needs.

When your cluster launches, The CloudWatch agent publishes the application metrics
that you specified along with the system metrics to CloudWatch.

## Configure Amazon Managed Service for Prometheus as cloud

storage for metrics with Amazon EMR 7.0.0

You can configure the Amazon CloudWatch agent to publish metrics to Amazon Managed Service for Prometheus instead of
CloudWatch.

###### Note

You can publish metrics from the Amazon CloudWatch agent to either Amazon Managed Service for Prometheus or to
Amazon CloudWatch, but you can't publish the metrics to both services for the same
cluster.

To configure the agent to publish metrics to Amazon Managed Service for Prometheus, you must add the
`aps:RemoteWrite` AWS Identity and Access Management (IAM) permission to the Amazon EC2
instance profile for Amazon EMR. The following example policy contains the required
permission:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "aps:RemoteWrite"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowAPSRemotewrite"
 }
 ]
}`

```

###### Use the CloudWatch agent on an EMR cluster to publish metrics to Amazon Managed Service for Prometheus

Once the service policy has the correct permissions, use the following
steps to launch a cluster that uses the CloudWatch agent to publish metrics to
Amazon Managed Service for Prometheus.

1. Use the AWS Management Console or AWS CLI to create an Amazon Managed Service for Prometheus workspace. For more
   information, see [Create a workspace](../../../prometheus/latest/userguide/AMP-onboard-create-workspace.md "../../../prometheus/latest/userguide/AMP-onboard-create-workspace.md") in the _Amazon Managed Service for Prometheus User
   Guide_.
2. Create or choose a bucket in your Amazon S3 account where you want to store
   the launch files that specify Amazon Managed Service for Prometheus as cloud storage.
3. Next, navigate to the aws-emr-utilities repo on GitHub and
   download the following scripts:
   - [`add_prometheus_endpoint_launcher.sh`](https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/prometheus/add_prometheus_endpoint_launcher.sh "https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/prometheus/add_prometheus_endpoint_launcher.sh")
     – A script that downloads and then runs
     `add_prometheus_endpoint.sh` in the
     background so that the node can finish bootstrapping.
   - [`add_prometheus_endpoint.sh`](https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/prometheus/add_prometheus_endpoint.sh "https://github.com/aws-samples/aws-emr-utilities/blob/main/applications/cloudwatch-agent/configuration/7.0/prometheus/add_prometheus_endpoint.sh")
     – A script that waits for the instance it runs on to
     finish bootstrapping, then configures CloudWatch agent to publish to
     the Amazon Managed Service for Prometheus endpoint that you provide as an argument when you
     launch your cluster.

4. Open each file and replace
   `amzn-s3-demo-bucket`
   with the name of your bucket from Step 2.
5. Use the AWS CLI to create an EMR cluster with the
   `add_prometheus_endpoint_launcher.sh` bootstrap
   action. In the following command, replace
   `amzn-s3-demo-bucket` with the
   bucket that holds the bootstrap action, and replace
   `managedpro-remote-write-workspace-url`
   with the remote write endpoint for your Amazon Managed Service for Prometheus workspace. Be sure to
   specify an Amazon EMR release label of `emr-7.0.0` or
   higher.

```
aws emr create-cluster --name managedpro-cluster \
    --release-label emr-7.0.0 \
    --applications Name=Hadoop Name=AmazonCloudWatchAgent \
    --ec2-attributes KeyName=`myKey` --instance-type m7g.2xlarge \
    --instance-count 3 --use-default-roles
   --bootstrap-actions Name='Add Prometheus Endpoint',Path=s3://`amzn-s3-demo-bucket`/add_prometheus_endpoint_launcher.sh,Args='`managedpro-remote-write-workspace-url`'
```

When your cluster launches, the CloudWatch agent publishes the metrics it collects to
Amazon Managed Service for Prometheus.

###### Use Amazon Managed Service for Prometheus as a data source for Amazon Managed Grafana

Once Amazon EMR has published the cluster metrics to Amazon Managed Service for Prometheus, you can use the
following steps to visualize the metrics with Amazon Managed Grafana:

1. Use the AWS Management Console to create an Amazon Managed Grafana workspace and user with
   appropriate permissions. For more information, see [Create a
   workspace](../../../grafana/latest/userguide/AMG-create-workspace.md "../../../grafana/latest/userguide/AMG-create-workspace.md") in the _Amazon Managed Grafana User
   Guide_.
2. Add your Amazon Managed Service for Prometheus workspace as a data source to Amazon Managed Grafana. For more
   information, see [Use AWS
   data source configuration to add Amazon Managed Service for Prometheus as a data source](../../../grafana/latest/userguide/AMP-adding-AWS-config.md "../../../grafana/latest/userguide/AMP-adding-AWS-config.md") in
   the _Amazon Managed Grafana User Guide_.

###### Note

The CloudWatch agent has a Prometheus exporter that renames certain attributes.
For the default metrics labels, Amazon Managed Service for Prometheus uses underscore characters in place of
the periods that Amazon CloudWatch uses. So if you use Amazon Managed Grafana to visualize the default
metrics in Amazon Managed Service for Prometheus, the labels appear as `jobflow_id`,
`instance_id`, and `service_name`.

Also, any **application** metrics that the
CloudWatch agent publishes to Amazon Managed Service for Prometheus use the label `job` instead of
`service_name`. However, **system** metrics continue to use the `service_name`
label.

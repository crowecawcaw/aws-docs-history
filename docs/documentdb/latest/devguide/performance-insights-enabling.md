

# Enabling and disabling Performance Insights
<a name="performance-insights-enabling"></a>

To use Performance Insights, enable it on your DB instance. You can disable it later if necessary. Enabling and disabling Performance Insights doesn't cause downtime, a reboot, or a failover.

The Performance Insights agent consumes limited CPU and memory on the DB host. When the DB load is high, the agent limits the performance impact by collecting data less frequently.

## Enabling Performance Insights when creating a cluster
<a name="performance-insights-enabling-create-instance"></a>

In the console, you can enable or disable Performance Insights when you create or modify a new DB instance.

### Using the AWS Management Console
<a name="create-instance-console"></a>

In the console, you can enable Performance Insights when you create an Amazon DocumentDB cluster. When you create a new Amazon DocumentDB cluster, enable Performance Insights by choosing **Enable Performance Insights** in the **Performance Insights** section.

**Console instructions**

1. To create a cluster, follow the instructions for [Creating an Amazon DocumentDB cluster.](https://docs.aws.amazon.com/documentdb/latest/devguide/db-cluster-create.html)

1. Select **Enable Performance Insights** in the Performance Insights section.  
![The Performance Insights section with Enable Performance Insights selected.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/performance-insights/select-performance-insights.png)
**Note**  
The Performance Insights data retention period will be seven days.

   ** AWS KMS key** — Specify your AWS KMS key. Performance Insights encrypts all potentially sensitive data using your AWS KMS key. Data is encrypted in flight and at rest. For more information, see Configuring an AWS AWS KMS policy for Performance Insights.

## Enabling and disabling when modifying an instance
<a name="performance-insights-enabling-modify-instance"></a>

You can modify a DB instance to enable or disable Performance Insights using the console or AWS CLI.

------
#### [ Using the AWS Management Console ]

**Console instructions**

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb).

1. Choose **Clusters**.

1. Choose a DB instance, and choose **Modify**.

1. In the Performance Insights section, choose either **Enable Performance Insights** or **Disable Performance Insights**.
**Note**  
If you choose **Enable Performance Insights**, you can specify your AWS AWS KMS key. Performance Insights encrypts all potentially sensitive data using your AWS KMS key. Data is encrypted in flight and at rest. For more information, see [Encrypting Amazon DocumentDB Data at Rest](https://docs.aws.amazon.com/documentdb/latest/devguide/encryption-at-rest.html).

1. Choose **Continue**.

1. For **Scheduling of Modifications**, choose **Apply immediately**. If you choose **Apply during the next scheduled maintenance window**, your instance ignores this setting and enables Performance Insights immediately.

1. Choose **Modify instance**.

------
#### [ Using the AWS CLI ]

When you use the `create-db-instance` or `modify-db-instance` AWS AWS CLI commands, you can enable Performance Insights by specifying `--enable-performance-insights`, or disable it by specifying `--no-enable-performance-insights`.

The following procedure describes how to enable or disable Performance Insights for a DB instance using the AWS AWS CLI.



**AWS AWS CLI instructions**

Call the `modify-db-instance` AWS AWS CLI command and provide the following values:
+ `--db-instance-identifer` — The name of the DB instance
+ `--enable-performance-insights` to enable or `--no-enable-performance-insights` to disable

**Example**  
The following example enables Performance Insights for `sample-db-instance`:  

```
aws docdb modify-db-instance \
    --db-instance-identifier sample-db-instance \
    --enable-performance-insights
```

```
aws docdb modify-db-instance ^
    --db-instance-identifier sample-db-instance ^
    --enable-performance-insights
```

------
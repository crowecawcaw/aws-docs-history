# Rebooting a DB instance within an Aurora cluster

This procedure is the most important operation that you take when performing reboots with Aurora. Many of the
maintenance procedures involve rebooting one or more Aurora DB instances in a particular order.

###### To reboot a DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the DB instance that
   you want to reboot.
3. For **Actions**, choose **Reboot**.

The **Reboot DB Instance** page appears. 4. Choose **Reboot** to reboot your DB instance.

Or choose **Cancel**.

To reboot a DB instance by using the AWS CLI, call the
[`reboot-db-instance`](../../../cli/latest/reference/rds/reboot-db-instance.md "../../../cli/latest/reference/rds/reboot-db-instance.md") command.

For Linux, macOS, or Unix:

```
aws rds reboot-db-instance \
    --db-instance-identifier `mydbinstance`
```

For Windows:

```
aws rds reboot-db-instance ^
    --db-instance-identifier `mydbinstance`
```

To reboot a DB instance by using the Amazon RDS API, call the
[`RebootDBInstance`](../APIReference/API_RebootDBInstance.md "../APIReference/API_RebootDBInstance.md") operation.

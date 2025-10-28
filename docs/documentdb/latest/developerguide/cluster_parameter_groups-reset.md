# Resetting Amazon DocumentDB cluster parameter groups

You can reset some or all of an Amazon DocumentDB cluster parameter group's parameter values to
their default values by using the AWS Management Console or the AWS Command Line Interface (AWS CLI) to reset the cluster
parameter group.

Using the AWS Management Console
Follow these steps to reset some or all of a cluster parameter group's parameter
values to their default values.

###### To reset a cluster parameter group's parameter values

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane on the left side of the console, choose **Parameter
   groups**.
3. In the **Cluster parameter groups** pane, choose the name of the cluster
   parameter group that you want to reset.
4. Choose **Actions**, and then choose **Reset** to reset that
   parameter group.
5. On the resulting **Cluster parameter group reset confirmation** page, confirm
   that you want to reset all cluster parameters for that parameter group to their
   defaults. Then choose **Reset** to reset your parameter group.
   You can also choose **Cancel** to discard your changes.

Using the AWS CLI
To reset some or all of a cluster parameter group's parameter values to their default values, use the
`reset-db-cluster-parameter-group` operation with the following parameters.

- `--db-cluster-parameter-group-name`
  — Required. The name of the cluster parameter group to reset.
- `--parameters` — Optional. A list
  of `ParameterName` and `ApplyMethod` in the cluster
  parameter group to reset to their default values. Static parameters must be set
  to `pending-reboot` to take effect on the next instance restart or
  `reboot-db-instance` request. You must call
  `reboot-db-instance` for every instance in your cluster that you
  want the updated static parameter to apply to.

This parameter and `--reset-all-parameters` are mutually exclusive: you can use either one but not both.

- `--reset-all-parameters` or
  `--no-reset-all-parameters` —
  Optional. Specifies whether to reset all parameters
  (`--reset-all-parameters` or only some of the parameters
  (`--no-reset-all-parameters`) to their default values. The
  `--reset-all-parameters` parameter and `--parameters`
  are mutually exclusive: you can use either one but not both.

When you reset the entire group, dynamic parameters are updated immediately.
Static parameters are set to `pending-reboot` to take effect on the
next instance restart or `reboot-db-instance` request. You must call
`reboot-db-instance` for every instance in your cluster that you
want the updated static parameter applied to.

###### Example 1: Resetting all parameters to their default values

The following code resets all parameters in the cluster parameter group `sample-parameter-group` their default values.

For Linux, macOS, or Unix:

```
aws docdb reset-db-cluster-parameter-group \
       --db-cluster-parameter-group-name `sample-parameter-group` \
       --reset-all-parameters
```

For Windows:

```
aws docdb reset-db-cluster-parameter-group ^
       --db-cluster-parameter-group-name `sample-parameter-group` ^
       --reset-all-parameters
```

###### Example 2: Resetting specified parameters to their default values

The following code resets the `tls` parameter in the cluster parameter group `sample-parameter-group` to its default
value.

For Linux, macOS, or Unix:

```
aws docdb reset-db-cluster-parameter-group \
       --db-cluster-parameter-group-name `sample-parameter-group` \
       --no-reset-all-parameters \
       --parameters ParameterName=tls,ApplyMethod=pending-reboot
```

For Windows:

```
aws docdb reset-db-cluster-parameter-group ^
       --db-cluster-parameter-group-name `sample-parameter-group` ^
       --no-reset-all-parameters ^
       --parameters ParameterName=tls,ApplyMethod=pending-reboot
```

Output from this operation looks something like the following (JSON format).

```
{
       "DBClusterParameterGroupName": "sample-parameter-group"
   }
```

###### Rebooting a cluster instance

Before a static parameter's value is changed, the cluster instance must be rebooted. Reboot each instance in your cluster that you want the
updated static parameter to apply to.

For Linux, macOS, or Unix:

```
aws docdb reboot-db-instance \
       --db-instance-identifier `sample-cluster-instance`
```

For Windows:

```
aws docdb reboot-db-instance ^
       --db-instance-identifier `sample-cluster-instance`
```

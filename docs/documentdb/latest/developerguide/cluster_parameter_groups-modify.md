# Modifying Amazon DocumentDB cluster parameter groups

This section explains how to modify a _custom_ Amazon DocumentDB parameter group.
In Amazon DocumentDB, you cannot modify a `default` cluster parameter group which is created when you first create a cluster with new engine version in a new region.
If your Amazon DocumentDB cluster is using the default cluster parameter group and you want to modify a value in it, you must first [create a new parameter group](cluster_parameter_groups-create.md "cluster_parameter_groups-create.md") or [copy an existing parameter group](cluster_parameter_groups-copy.md "cluster_parameter_groups-copy.md"), modify it, and then apply the modified parameter group to your cluster.

Complete the following steps to modify a custom cluster parameter group.
Modify actions could take a while to propagate.
Please wait for the modified cluster paramater group to be available before attaching it to your cluster.
You can use the AWS Management Console or the AWS CLI `describe-db-cluster-parameters` operation to verify that your cluster parameter group has been modified.
For more information, see [Describing cluster parameter groups](cluster_parameter_groups-describe.md "cluster_parameter_groups-describe.md").

Using the AWS Management Console
Follow these steps to modify a custom Amazon DocumentDB parameter group. You can't modify a `default` parameter group. If you want to modify a value in the `default` parameter group, you can [copy the default cluster parameter group](cluster_parameter_groups-copy.md "cluster_parameter_groups-copy.md"), modify it, and then apply the modified parameter group to your cluster. For more information about applying parameter groups to your cluster, see [Modifying an Amazon DocumentDB cluster](db-cluster-modify.md "db-cluster-modify.md").

###### To modify a custom cluster parameter group

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane on the left side of the console, choose **Parameter groups**. In the list of parameter groups, choose the name of the parameter group that you want to modify.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. For each parameter in the parameter group that you want to modify, do the following:

    1. Locate the parameter that you want to modify, and verify that it is modifiable by checking if it is listed as `true` under the **Modifiable** column.
    2. If it is modifiable, select the parameter and choose **Edit** from the top right of the console page.
    3. In the **Modify `<parameter-name>`** dialog box, make the changes that you want. Then choose **Modify cluster parameter**, or choose **Cancel** to discard the changes.

Using the AWS CLI
You can modify the `ParameterValue`, `Description`, or `ApplyMethod` of any modifiable parameter in a custom Amazon DocumentDB cluster parameter group using the AWS CLI. You can't make modifications directly to a default cluster parameter group.

To modify a custom cluster parameter group's parameters, use the `modify-db-cluster-parameter-group` operation with the following parameters.

- `--db-cluster-parameter-group-name`
  — Required. The name of the cluster parameter group that you are
  modifying.
- `--parameters` — Required. The
  parameters that you are modifying. For a list of the parameters that apply to
  all instances in an Amazon DocumentDB cluster, see the [Amazon DocumentDB cluster parameters reference](cluster_parameter_groups-list_of_parameters.md "cluster_parameter_groups-list_of_parameters.md"). Each
  parameter entry must include the following:
  - `ParameterName` — The name
    of the parameter that you are modifying.
  - `ParameterValue` — The new
    value for this parameter.
  - `ApplyMethod` — How you
    want changes to this parameter applied. Permitted values are
    `immediate` and `pending-reboot`.

  ###### Note

  Parameters with the `ApplyType` of `static` must have an `ApplyMethod` of `pending-reboot`.

###### Example - Modifying a parameter's value

In this example, you list the parameter values of `sample-parameter-group` and modify the `tls` parameter. Then, after
waiting 5 minutes, you again list the parameter values of `sample-parameter-group` to see the changed parameter values.

1. List the parameters and their values of
   `sample-parameter-group`.

For Linux, macOS, or Unix:

```
aws docdb describe-db-cluster-parameters \
       --db-cluster-parameter-group-name `sample-parameter-group`
```

For Windows:

```
aws docdb describe-db-cluster-parameters ^
       --db-cluster-parameter-group-name `sample-parameter-group`
```

Output from this operation looks something like the following (JSON format).

```
{
       "Parameters": [
           {
               "Source": "system",
               "ApplyType": "static",
               "AllowedValues": "disabled,enabled",
               "ParameterValue": "enabled",
               "ApplyMethod": "pending-reboot",
               "DataType": "string",
               "ParameterName": "tls",
               "IsModifiable": true,
               "Description": "Config to enable/disable TLS"
           },
           {
               "Source": "user",
               "ApplyType": "dynamic",
               "AllowedValues": "disabled,enabled",
               "ParameterValue": "enabled",
               "ApplyMethod": "pending-reboot",
               "DataType": "string",
               "ParameterName": "ttl_monitor",
               "IsModifiable": true,
               "Description": "Enables TTL Monitoring"
           }
       ]
}
```

2. Modify the `tls` parameter so that its value is
   `disabled` .

You can't modify the `ApplyMethod` because the
`ApplyType` is `static`.

For Linux, macOS, or Unix:

```
aws docdb modify-db-cluster-parameter-group \
       --db-cluster-parameter-group-name `sample-parameter-group` \
       --parameters "ParameterName"=tls,"ParameterValue"=disabled,"ApplyMethod"=pending-reboot
```

For Windows:

```
aws docdb modify-db-cluster-parameter-group ^
       --db-cluster-parameter-group-name `sample-parameter-group` ^
       --parameters "ParameterName"=tls,"ParameterValue"=disabled,"ApplyMethod"=pending-reboot
```

Output from this operation looks something like the following (JSON format).

```
{
       "DBClusterParameterGroupName": "sample-parameter-group"
   }
```

3. Wait at least 5 minutes.
4. List the parameter values of `sample-parameter-group` to
   verify that the `tls` parameter was modified.

For Linux, macOS, or Unix:

```
aws docdb describe-db-cluster-parameters \
       --db-cluster-parameter-group-name `sample-parameter-group`
```

For Windows:

```
aws docdb describe-db-cluster-parameters ^
       --db-cluster-parameter-group-name `sample-parameter-group`
```

Output from this operation looks something like the following (JSON format).

```
{
       "Parameters": [
           {
               "ParameterValue": "false",
               "ParameterName": "enable_audit_logs",
               "ApplyType": "dynamic",
               "DataType": "string",
               "Description": "Enables auditing on cluster.",
               "AllowedValues": "true,false",
               "Source": "system",
               "IsModifiable": true,
               "ApplyMethod": "pending-reboot"
           },
           {
               `"ParameterValue": "disabled"`,
               `"ParameterName": "tls"`,
               "ApplyType": "static",
               "DataType": "string",
               "Description": "Config to enable/disable TLS",
               "AllowedValues": "disabled,enabled",
               "Source": "system",
               "IsModifiable": true,
               "ApplyMethod": "pending-reboot"
           }
       ]
}
```

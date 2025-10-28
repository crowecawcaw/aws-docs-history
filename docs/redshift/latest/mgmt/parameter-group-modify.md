Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Modifying a parameter group

You can view any of your parameter groups to see a summary of the values for
parameters and workload management (WLM) configuration. You can modify parameters to
change the parameter settings and WLM configuration properties.

###### Note

You can't modify the default parameter group.

AWS Management Console
In the console, group parameters appear on the
**Parameters** tab, and **Workload
queues** appear on the **Workload Management**
tab.

###### To modify a parameter group

1.  Sign in to the AWS Management Console and open the Amazon Redshift console at
    [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2.  On the navigation menu, choose
    **Configurations**, then choose **Workload
    management** to display the **Workload
    management** page.
3.  Choose the parameter group that you want to modify to display the
    details page, with tabs for **Parameters** and
    **Workload management**.
4.  Choose the **Parameters** tab to view the current
    parameter settings.
5.  Choose **Edit parameters** to enable changing
    settings for these parameters:

        * `auto_analyze`
        * `auto_mv`
        * `datestyle`
        * `enable_case_sensitive_identifier`
        * `enable_user_activity_logging`
        * `extra_float_digits`
        * `max_concurrency_scaling_clusters`
        * `max_cursor_result_set_size`
        * `query_group`
        * `require_ssl`
        * `search_path`
        * `statement_timeout`
        * `use_fips_ssl`

    For more information about these parameters, see [Amazon Redshift parameter groups](working-with-parameter-groups.md "working-with-parameter-groups.md").

6.  Enter your changes and then choose **Save** to
    update the parameter group.

###### To modify the WLM configuration for a parameter group

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose
   **Configurations**, then choose **Workload
   management** to display the **Workload
   management** page.
3. Choose the parameter group that you want to modify to display the
   details page with tabs for **Parameters** and
   **Workload management**.
4. Choose the **Workload management** tab to view
   the current WLM configuration.
5. Choose **Edit workload queues** to edit the WLM
   configuration.
6. (Optional) Select **Enable short query
   acceleration** to enable short query acceleration
   (SQA).

When you enable SQA, **Maximum run time for short queries
(1 to 20 seconds)** is set to
**Dynamic** by default. To set the maximum
runtime to a fixed value, choose a value of 1–20. 7. Do one or more of the following to modify the queue configuration:

    * Choose **Switch WLM mode** to choose
     between **Automatic WLM** and
     **Manual WLM**.


    With **Automatic WLM**, the
     **Memory** and **Concurrency on
     main** values are set to
     **auto**.
    * To create a queue, choose **Edit workload
     queues**, then choose **Add
     Queue**.
    * To modify a queue, change property values in the table.
     Depending on the type of queue, properties can include the
     following:




    	+ **Queue name** can be changed.
    	+ **Memory (%)**
    	+ **Concurrency on main**
    	 cluster
    	+ **Concurrency scaling mode** can
    	 be **off** or
    	 **auto**
    	+ **Timeout (ms)**
    	+ **User groups**
    	+ **Query groups**
    	+ **User roles**
    For more information about these properties, see [Properties for the WLM configuration
     parameter](workload-mgmt-config.md#wlm-json-config-properties "workload-mgmt-config.md#wlm-json-config-properties").


    ###### Important

    If you change a queue name, the `QueueName`
     dimension value of WLM queue metrics (such as,
     WLMQueueLength, WLMQueueWaitTime,
     WLMQueriesCompletedPerSecond, WLMQueryDuration,
     WLMRunningQueries, and so on) also changes. So, if you
     change the name of a queue, you might need to change
     CloudWatch alarms you have set up.
    * To change the order of queues, choose the
     **Up** and **Down**
     arrow buttons.
    * To delete a queue, choose **Delete** in
     the queue's row in the table.

8. (Optional) Select **Defer dynamic changes until
   reboot** to have the changes applied to clusters after
   their next reboot.

###### Note

Some changes require a cluster reboot regardless of this
setting. For more information, see [WLM dynamic and static
properties](workload-mgmt-config.md#wlm-dynamic-and-static-properties "workload-mgmt-config.md#wlm-dynamic-and-static-properties"). 9. Choose **Save**.

AWS CLI
To configure Amazon Redshift parameters by using the AWS CLI, you use the [modify-cluster-parameter-group](../../../cli/latest/reference/redshift/modify-cluster-parameter-group.md "../../../cli/latest/reference/redshift/modify-cluster-parameter-group.md") command for a specific parameter
group. You specify the parameter group to modify in
`parameter-group-name`. You use the `parameters`
parameter (for the `modify-cluster-parameter-group` command) to
specify name/value pairs for each parameter that you want to modify in the
parameter group.

###### Note

There are special considerations when configuring the
`wlm_json_configuration` parameter by using the AWS CLI.
The examples in this section apply to all of the parameters except
`wlm_json_configuration`. For more information about
configuring `wlm_json_configuration` by using the AWS CLI, see
[Workload management](workload-mgmt-config.md "workload-mgmt-config.md").

After you modify parameter values, you must reboot any clusters that are
associated with the modified parameter group. The cluster status displays
`applying` for `ParameterApplyStatus` while the
values are being applied, and then `pending-reboot` after the
values have been applied. After you reboot, the databases in your cluster
begin to use the new parameter values. For more information about rebooting
clusters, see [Rebooting a cluster](reboot-cluster.md "reboot-cluster.md").

###### Note

The `wlm_json_configuration` parameter contains some
properties that are dynamic and do not require you to reboot associated
clusters for the changes to be applied. For more information about
dynamic and static properties, see [WLM dynamic and static
properties](workload-mgmt-config.md#wlm-dynamic-and-static-properties "workload-mgmt-config.md#wlm-dynamic-and-static-properties").

The following syntax shows how to use the
`modify-cluster-parameter-group` command to configure a
parameter. You specify `parameter_group_name` and
replace both `parameter_name` and
`parameter_value` with an actual parameter to
modify and a value for that parameter. If you want to modify more than one
parameter at the same time, separate each parameter and value set from the
next with a space.

```
aws redshift modify-cluster-parameter-group --parameter-group-name `parameter_group_name` --parameters ParameterName=`parameter_name`,ParameterValue=`parameter_value`
```

The following example shows how to configure the
`statement_timeout` and
`enable_user_activity_logging` parameters for the
`myclusterparametergroup` parameter group.

###### Note

For readability purposes, the example is displayed on several lines,
but in the actual AWS CLI this is one line.

```
aws redshift modify-cluster-parameter-group
--parameter-group-name myclusterparametergroup
--parameters ParameterName=statement_timeout,ParameterValue=20000 ParameterName=enable_user_activity_logging,ParameterValue=true
```

Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Amazon Redshift parameter groups

In Amazon Redshift, you associate a parameter group with each cluster that you create. A
_parameter group_ is a group of parameters that apply to all of the
databases that you create in the cluster. These parameters configure database settings such
as query timeout and date style. When you launch a cluster, you must associate it with a
parameter group. If you want to change the parameter group later, you can modify the cluster
and choose a different parameter group.

Each parameter group has several parameters to configure settings for the database. The
list of available parameters depends on the parameter group family to which the parameter
group belongs. The default parameter group family is `redshift-2.0`.

Amazon Redshift provides one default parameter group for each parameter group family. The default
parameter group has preset values for each of its parameters, and it cannot be modified. The
format of the default parameter group name is
`default.`parameter_group_family``. For example, the default parameter group for the
`redshift-2.0` parameter group family is `default.redshift-2.0`.

If you want to use different parameter values than the default parameter group, you must
create a custom parameter group and then associate your cluster with it. Initially, the
parameter values in a custom parameter group are the same as in the default parameter group.
The initial `source` for all of the parameters is `engine-default`
because the values are preset by Amazon Redshift. After you change a parameter value, the
`source` changes to `user` to indicate that the value has been
modified from its default value.

###### Note

The Amazon Redshift console does not display the `source` of each parameter. You
must use the Amazon Redshift API, the AWS CLI, or one of the AWS SDKs to view the
`source`.

For parameter groups that you create, you can modify a parameter value at any time, or you
can reset all parameter values to their defaults. You can also associate a different
parameter group with a cluster. In some cases, you might modify parameter values in a
parameter group that is already associated with a cluster or associate a different parameter
group with a cluster. In these cases, you might need to restart the cluster for the updated
parameter values to take effect. If the cluster fails and is restarted by Amazon Redshift, your changes
are applied at that time. Changes aren't applied if your cluster is restarted during
maintenance. For more information, see [WLM dynamic and static properties](workload-mgmt-config.md#wlm-dynamic-and-static-properties "workload-mgmt-config.md#wlm-dynamic-and-static-properties").

## Default parameter values

###### Note

As of January 10, 2025, the default value for the `require_ssl` parameter is true.
If you don’t want your cluster to require SSL, you can use a custom parameter group when
creating the cluster, or modify the cluster to associate it with a custom parameter
group after creating the cluster with the default.

The following table shows the default parameter values at a glance with links to more
in-depth information about each parameter. These are the default values for the
`redshift-2.0` parameter group family.

| Parameter name                      | Value                | More information                                                                                                                                                                             |
| ----------------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| auto\_analyze                       | true                 | [auto\_analyze](../dg/t_Analyzing_tables.md#t_Analyzing_tables-auto-analyze "../dg/t_Analyzing_tables.md#t_Analyzing_tables-auto-analyze") in the _Amazon Redshift Database Developer Guide_ |
| auto\_mv                            | true                 | [Automated<br>materialized views](../dg/materialized-view-auto-mv.md "../dg/materialized-view-auto-mv.md") in the Amazon Redshift Database Developer<br>Guide                                |
| datestyle                           | ISO, MDY             | [datestyle](../dg/r_datestyle.md "../dg/r_datestyle.md") in the<br>_Amazon Redshift Database Developer Guide_                                                                                |
| enable\_case\_sensitive\_identifier | false                | [enable\_case\_sensitive\_identifier](../dg/r_enable_case_sensitive_identifier.md "../dg/r_enable_case_sensitive_identifier.md") in the<br>_Amazon Redshift Database Developer Guide_        |
| enable\_user\_activity\_logging     | false                | [Database audit logging](db-auditing.md "db-auditing.md") in this guide                                                                                                                      |
| extra\_float\_digits                | 0                    | [extra\_float\_digits](../dg/r_extra_float_digits.md "../dg/r_extra_float_digits.md") in the<br>_Amazon Redshift Database Developer Guide_                                                   |
| max\_concurrency\_scaling\_clusters | 1                    | [max\_concurrency\_scaling\_clusters](../dg/r_max_concurrency_scaling_clusters.md "../dg/r_max_concurrency_scaling_clusters.md") in the<br>_Amazon Redshift Database Developer Guide_        |
| query\_group                        | default              | [query\_group](../dg/r_query_group.md "../dg/r_query_group.md") in the<br>_Amazon Redshift Database Developer Guide_                                                                         |
| require\_ssl                        | true                 | [Configuring security options for connections](connecting-ssl-support.md "connecting-ssl-support.md") in this guide                                                                          |
| search\_path                        | $user, public        | [search\_path](../dg/r_search_path.md "../dg/r_search_path.md") in the<br>_Amazon Redshift Database Developer Guide_                                                                         |
| statement\_timeout                  | 0                    | [statement\_timeout](../dg/r_statement_timeout.md "../dg/r_statement_timeout.md") in the<br>_Amazon Redshift Database Developer Guide_                                                       |
| wlm\_json\_configuration            | [{"auto\_wlm":true}] | [Workload management](workload-mgmt-config.md "workload-mgmt-config.md") in this guide                                                                                                       |
| use\_fips\_ssl                      | false                | Enable FIPS-compliant SSL mode only if your system is required to<br>be FIPS-compliant.                                                                                                      |

###### Note

The `max_cursor_result_set_size` parameter is deprecated. For more
information about cursor result set size, see [Cursor constraints](../dg/declare.md#declare-constraints "../dg/declare.md#declare-constraints")
in the _Amazon Redshift Database Developer Guide_.

You can temporarily override a parameter by using the `SET` command in the
database. The `SET` command overrides the parameter for the duration of your
current session only. In addition to the parameters listed in the preceding table, you
can also temporarily adjust the slot count by setting `wlm_query_slot_count`
in the database. The `wlm_query_slot_count` parameter is not available for
configuration in parameter groups. For more information about adjusting the slot count,
see [wlm\_query\_slot\_count](../dg/r_wlm_query_slot_count.md "../dg/r_wlm_query_slot_count.md") in
the _Amazon Redshift Database Developer Guide_. For more information about temporarily
overriding the other parameters, see [Modifying the server
configuration](../dg/t_Modifying_the_default_settings.md "../dg/t_Modifying_the_default_settings.md") in the _Amazon Redshift Database Developer Guide_.

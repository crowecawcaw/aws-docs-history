Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Configuration reference

You can use configurations to help customize your environment. With Amazon Redshift, you can
customize and optimize your data warehousing environment by configuring various parameters and
settings. The configuration reference outlines the available cluster properties, database
parameters, and workload management (WLM) configuration options. You can consult this
reference to fine-tune performance, security, and resource allocation based on their specific
requirements. The following reference provides detailed guidance on modifying these
configurations to achieve your desired data warehousing setup.

###### Topics

- [Modifying the server
  configuration](#t_Modifying_the_default_settings "#t_Modifying_the_default_settings")
- [analyze_threshold_percent](r_analyze_threshold_percent.md "r_analyze_threshold_percent.md")
- [cast_super_null_on_error](r_cast_super_null_on_error.md "r_cast_super_null_on_error.md")
- [datashare_break_glass_session_var](r_datashare_break_glass_session_var.md "r_datashare_break_glass_session_var.md")
- [datestyle](r_datestyle.md "r_datestyle.md")
- [default_array_search_null_handling](r_default_array_search_null_handling.md "r_default_array_search_null_handling.md")
- [default_geometry_encoding](r_default_geometry_encoding.md "r_default_geometry_encoding.md")
- [describe_field_name_in_uppercase](r_describe_field_name_in_uppercase.md "r_describe_field_name_in_uppercase.md")
- [downcase_delimited_identifier](r_downcase_delimited_identifier.md "r_downcase_delimited_identifier.md")
- [enable_case_sensitive_identifier](r_enable_case_sensitive_identifier.md "r_enable_case_sensitive_identifier.md")
- [enable_case_sensitive_super_attribute](r_enable_case_sensitive_super_attribute.md "r_enable_case_sensitive_super_attribute.md")
- [enable_numeric_rounding](r_enable_numeric_rounding.md "r_enable_numeric_rounding.md")
- [enable_result_cache_for_session](r_enable_result_cache_for_session.md "r_enable_result_cache_for_session.md")
- [enable_vacuum_boost](r_enable_vacuum_boost.md "r_enable_vacuum_boost.md")
- [error_on_nondeterministic_update](r_error_on_nondeterministic_update.md "r_error_on_nondeterministic_update.md")
- [extra_float_digits](r_extra_float_digits.md "r_extra_float_digits.md")
- [interval_forbid_composite_literals](r_interval_forbid_composite_literals.md "r_interval_forbid_composite_literals.md")
- [json_serialization_enable](r_json_serialization_enable.md "r_json_serialization_enable.md")
- [json_serialization_parse_nested_strings](r_json_serialization_parse_nested_strings.md "r_json_serialization_parse_nested_strings.md")
- [max_concurrency_scaling_clusters](r_max_concurrency_scaling_clusters.md "r_max_concurrency_scaling_clusters.md")
- [max_cursor_result_set_size](max_cursor_result_set_size.md "max_cursor_result_set_size.md")
- [mv_enable_aqmv_for_session](r_mv_enable_aqmv_for_session.md "r_mv_enable_aqmv_for_session.md")
- [navigate_super_null_on_error](r_navigate_super_null_on_error.md "r_navigate_super_null_on_error.md")
- [parse_super_null_on_error](r_parse_super_null_on_error.md "r_parse_super_null_on_error.md")
- [pg_federation_repeatable_read](r_pg_federation_repeatable_read.md "r_pg_federation_repeatable_read.md")
- [query_group](r_query_group.md "r_query_group.md")
- [search_path](r_search_path.md "r_search_path.md")
- [spectrum_enable_pseudo_columns](r_spectrum_enable_pseudo_columns.md "r_spectrum_enable_pseudo_columns.md")
- [enable_spectrum_oid](r_spectrum_enable_spectrum_oid.md "r_spectrum_enable_spectrum_oid.md")
- [spectrum_query_maxerror](r_spectrum_query_maxerror.md "r_spectrum_query_maxerror.md")
- [statement_timeout](r_statement_timeout.md "r_statement_timeout.md")
- [stored_proc_log_min_messages](r_stored_proc_log_min_messages.md "r_stored_proc_log_min_messages.md")
- [timezone](r_timezone_config.md "r_timezone_config.md")
- [use_fips_ssl](use_fips_ssl.md "use_fips_ssl.md")
- [wlm_query_slot_count](r_wlm_query_slot_count.md "r_wlm_query_slot_count.md")

## Modifying the server

configuration

You can change the server configuration in the following ways:

- By using a [SET](r_SET.md "r_SET.md") command to override a
  setting for the duration of the current session only.

For example:

```
set extra_float_digits to 2;
```

- By modifying the parameter group settings for the cluster. The parameter group
  settings include additional parameters that you can configure. For more information,
  see [Amazon Redshift Parameter
  Groups](../mgmt/working-with-parameter-groups.md "../mgmt/working-with-parameter-groups.md") in the _Amazon Redshift Management Guide_.
- By using the [ALTER USER](r_ALTER_USER.md "r_ALTER_USER.md") command
  to set a configuration parameter to a new value for all sessions run by the specified
  user.

```
ALTER USER *username* SET *parameter* { TO | = } { *value* | DEFAULT }
```

Use the SHOW command to view the current parameter settings. Use SHOW ALL to view all
the settings that you can configure by using the [SET](r_SET.md "r_SET.md") command.

```
`SHOW ALL;`

`name | setting
--------------------------+--------------
analyze_threshold_percent | 10
datestyle | ISO, MDY
extra_float_digits | 2
query_group | default
search_path | $user, public
statement_timeout | 0
timezone | UTC
wlm_query_slot_count | 1`
```

###### Note

Note that configuration parameters are applied to the database you are connected to in your data warehouse.

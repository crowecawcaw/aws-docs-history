

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Configuration reference
<a name="cm_chap_ConfigurationRef"></a>

You can use configurations to help customize your environment. With Amazon Redshift, you can customize and optimize your data warehousing environment by configuring various parameters and settings. The configuration reference outlines the available cluster properties, database parameters, and workload management (WLM) configuration options. You can consult this reference to fine-tune performance, security, and resource allocation based on their specific requirements. The following reference provides detailed guidance on modifying these configurations to achieve your desired data warehousing setup.

**Topics**
+ [Modifying the server configuration](#t_Modifying_the_default_settings)
+ [analyze\_threshold\_percent](r_analyze_threshold_percent.md)
+ [cast\_super\_null\_on\_error](r_cast_super_null_on_error.md)
+ [datashare\_break\_glass\_session\_var](r_datashare_break_glass_session_var.md)
+ [datestyle](r_datestyle.md)
+ [default\_array\_search\_null\_handling](r_default_array_search_null_handling.md)
+ [default\_geometry\_encoding](r_default_geometry_encoding.md)
+ [describe\_field\_name\_in\_uppercase](r_describe_field_name_in_uppercase.md)
+ [downcase\_delimited\_identifier](r_downcase_delimited_identifier.md)
+ [enable\_case\_sensitive\_identifier](r_enable_case_sensitive_identifier.md)
+ [enable\_case\_sensitive\_super\_attribute](r_enable_case_sensitive_super_attribute.md)
+ [enable\_numeric\_rounding](r_enable_numeric_rounding.md)
+ [enable\_result\_cache\_for\_session](r_enable_result_cache_for_session.md)
+ [enable\_vacuum\_boost](r_enable_vacuum_boost.md)
+ [error\_on\_nondeterministic\_update](r_error_on_nondeterministic_update.md)
+ [extra\_float\_digits](r_extra_float_digits.md)
+ [interval\_forbid\_composite\_literals](r_interval_forbid_composite_literals.md)
+ [json\_serialization\_enable](r_json_serialization_enable.md)
+ [json\_serialization\_parse\_nested\_strings](r_json_serialization_parse_nested_strings.md)
+ [max\_concurrency\_scaling\_clusters](r_max_concurrency_scaling_clusters.md)
+ [max\_cursor\_result\_set\_size](max_cursor_result_set_size.md)
+ [max\_failed\_login\_attempts](max_failed_login_attempts.md)
+ [mv\_enable\_aqmv\_for\_session](r_mv_enable_aqmv_for_session.md)
+ [navigate\_super\_null\_on\_error](r_navigate_super_null_on_error.md)
+ [parse\_super\_null\_on\_error](r_parse_super_null_on_error.md)
+ [pg\_federation\_repeatable\_read](r_pg_federation_repeatable_read.md)
+ [query\_group](r_query_group.md)
+ [search\_path](r_search_path.md)
+ [spectrum\_enable\_pseudo\_columns](r_spectrum_enable_pseudo_columns.md)
+ [enable\_spectrum\_oid](r_spectrum_enable_spectrum_oid.md)
+ [spectrum\_query\_maxerror](r_spectrum_query_maxerror.md)
+ [statement\_timeout](r_statement_timeout.md)
+ [stored\_proc\_log\_min\_messages](r_stored_proc_log_min_messages.md)
+ [timezone](r_timezone_config.md)
+ [use\_fips\_ssl](use_fips_ssl.md)
+ [wlm\_query\_slot\_count](r_wlm_query_slot_count.md)

## Modifying the server configuration
<a name="t_Modifying_the_default_settings"></a>

You can change the server configuration in the following ways: 
+ By using a [SET](r_SET.md) command to override a setting for the duration of the current session only.

  For example: 

  ```
  set extra_float_digits to 2;
  ```
+ By modifying the parameter group settings for the cluster. The parameter group settings include additional parameters that you can configure. For more information, see [Amazon Redshift Parameter Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Management Guide*.
+ By using the [ALTER USER](r_ALTER_USER.md) command to set a configuration parameter to a new value for all sessions run by the specified user.

  ```
  ALTER USER username SET parameter { TO | = } { value | DEFAULT }
  ```

Use the SHOW command to view the current parameter settings. Use SHOW ALL to view all the settings that you can configure by using the [SET](r_SET.md) command.

```
SHOW ALL;

name                      | setting      
--------------------------+--------------
analyze_threshold_percent | 10           
datestyle                 | ISO, MDY     
extra_float_digits        | 2            
query_group               | default      
search_path               | $user, public
statement_timeout         | 0            
timezone                  | UTC            
wlm_query_slot_count      | 1
```

**Note**  
Note that configuration parameters are applied to the database you are connected to in your data warehouse.
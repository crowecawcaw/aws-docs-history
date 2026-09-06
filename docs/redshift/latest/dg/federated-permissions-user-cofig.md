

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Federated user configuration
<a name="federated-permissions-user-cofig"></a>

With Amazon Redshift federated permissions, users authenticated with IAM or IAM Identity Center (IdC) credentials can get a consistent experience across all their Amazon Redshift warehouses.

When a user connects to any Redshift cluster, their configuration parameters—such as date format, search path, and time zone preferences—are automatically applied to their session. This ensures that the same user experience is maintained across all clusters, without requiring manual reconfiguration, providing a seamless and personalized experience.

**Example**

Consider **Alex**, a data analyst who has configured their preferred date format and time zone in their primary Redshift database. When Alex runs queries there, all date values appear in the preferred format.

Now, when Alex connects to a **shared** or **auto-mounted** database on another Redshift warehouse, those same preferences are consistently applied. Alex sees results in the same date format and time zone, ensuring a consistent experience across environments.

## User Configs that are consistent across Amazon Redshift Warehouses
<a name="federated-user-config-settings"></a>

The following **user-level [configurations](https://docs.aws.amazon.com/redshift/latest/dg/cm_chap_ConfigurationRef.html)** are automatically synchronized across Redshift clusters for users authenticated with **IAM** or **AWS IAM Identity Center (IdC)** credentials:
+ [datestyle](https://docs.aws.amazon.com/redshift/latest/dg/r_datestyle.html)
+ [enable\_case\_sensitive\_identifier](https://docs.aws.amazon.com/redshift/latest/dg/r_enable_case_sensitive_identifier.html)
+ [extra\_float\_digits](https://docs.aws.amazon.com/redshift/latest/dg/r_extra_float_digits.html)
+ [search\_path](https://docs.aws.amazon.com/redshift/latest/dg/r_search_path.html)
+ [cast\_super\_null\_on\_error](https://docs.aws.amazon.com/redshift/latest/dg/r_cast_super_null_on_error.html)
+ [default\_geometry\_encoding](https://docs.aws.amazon.com/redshift/latest/dg/r_default_geometry_encoding.html)
+ [describe\_field\_name\_in\_uppercase](https://docs.aws.amazon.com/redshift/latest/dg/r_describe_field_name_in_uppercase.html)
+ [downcase\_delimited\_identifier](https://docs.aws.amazon.com/redshift/latest/dg/r_downcase_delimited_identifier.html)
+ [enable\_case\_sensitive\_super\_attribute](https://docs.aws.amazon.com/redshift/latest/dg/r_enable_case_sensitive_super_attribute.html)
+ [enable\_numeric\_rounding](https://docs.aws.amazon.com/redshift/latest/dg/r_enable_numeric_rounding.html)
+ [enable\_result\_cache\_for\_session](https://docs.aws.amazon.com/redshift/latest/dg/r_enable_result_cache_for_session.html)
+ [error\_on\_nondeterministic\_update](https://docs.aws.amazon.com/redshift/latest/dg/r_error_on_nondeterministic_update.html)
+ [interval\_forbid\_composite\_literals](https://docs.aws.amazon.com/redshift/latest/dg/r_interval_forbid_composite_literals.html)
+ [json\_serialization\_enable](https://docs.aws.amazon.com/redshift/latest/dg/r_json_serialization_enable.html)
+ [json\_serialization\_parse\_nested\_strings](https://docs.aws.amazon.com/redshift/latest/dg/r_json_serialization_parse_nested_strings.html)
+ [mv\_enable\_aqmv\_for\_session](https://docs.aws.amazon.com/redshift/latest/dg/r_mv_enable_aqmv_for_session.html)
+ [navigate\_super\_null\_on\_error](https://docs.aws.amazon.com/redshift/latest/dg/r_navigate_super_null_on_error.html)
+ [parse\_super\_null\_on\_error](https://docs.aws.amazon.com/redshift/latest/dg/r_parse_super_null_on_error.html)
+ [spectrum\_enable\_pseudo\_columns](https://docs.aws.amazon.com/redshift/latest/dg/r_spectrum_enable_pseudo_columns.html)
+ [enable\_spectrum\_oid](https://docs.aws.amazon.com/redshift/latest/dg/r_spectrum_enable_spectrum_oid.html)
+ [spectrum\_query\_maxerror](https://docs.aws.amazon.com/redshift/latest/dg/r_spectrum_query_maxerror.html)
+ [stored\_proc\_log\_min\_messages](https://docs.aws.amazon.com/redshift/latest/dg/r_stored_proc_log_min_messages.html)
+ [analyze\_threshold\_percent](https://docs.aws.amazon.com/redshift/latest/dg/r_analyze_threshold_percent.html)
+ [enable\_vacuum\_boost](https://docs.aws.amazon.com/redshift/latest/dg/r_enable_vacuum_boost.html)
+ [pg\_federation\_repeatable\_read](https://docs.aws.amazon.com/redshift/latest/dg/r_pg_federation_repeatable_read.html)

## Connection and Configuration Management
<a name="federated-user-config-management"></a>
+ When connecting to Amazon Redshiftusing **JDBC**, some **session-level configurations** may also be automatically applied. For more details, refer to the JDBC session-level configuration documentation.
+ Users can also define persistent **user-level configurations** using the [ALTER USER](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_USER.html).
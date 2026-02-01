Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Federated user configuration

With Amazon Redshift federated permissions, users authenticated with IAM or IAM Identity Center (IdC) credentials can get a consistent experience across all their Amazon Redshift warehouses.

When a user connects to any Redshift cluster, their configuration parameters—such as date format, search path, and time zone preferences—are automatically
applied to their session. This ensures that the same user experience is maintained across all clusters, without requiring manual reconfiguration, providing a seamless and personalized experience.

**Example**

Consider **Alex**, a data analyst who has configured their preferred date format and time zone in their primary Redshift database.
When Alex runs queries there, all date values appear in the preferred format.

Now, when Alex connects to a **shared** or **auto-mounted** database on another Redshift warehouse,
those same preferences are consistently applied. Alex sees results in the same date format and time zone, ensuring a consistent experience across environments.

## User Configs that are consistent across Amazon Redshift Warehouses

The following **user-level [configurations](cm_chap_ConfigurationRef.md "cm_chap_ConfigurationRef.md")** are
automatically synchronized across Redshift clusters for users authenticated with **IAM** or **AWS IAM Identity Center (IdC)** credentials:

- [datestyle](r_datestyle.md "r_datestyle.md")
- [enable_case_sensitive_identifier](r_enable_case_sensitive_identifier.md "r_enable_case_sensitive_identifier.md")
- [extra_float_digits](r_extra_float_digits.md "r_extra_float_digits.md")
- [search_path](r_search_path.md "r_search_path.md")
- [cast_super_null_on_error](r_cast_super_null_on_error.md "r_cast_super_null_on_error.md")
- [default_geometry_encoding](r_default_geometry_encoding.md "r_default_geometry_encoding.md")
- [describe_field_name_in_uppercase](r_describe_field_name_in_uppercase.md "r_describe_field_name_in_uppercase.md")
- [downcase_delimited_identifier](r_downcase_delimited_identifier.md "r_downcase_delimited_identifier.md")
- [enable_case_sensitive_super_attribute](r_enable_case_sensitive_super_attribute.md "r_enable_case_sensitive_super_attribute.md")
- [enable_numeric_rounding](r_enable_numeric_rounding.md "r_enable_numeric_rounding.md")
- [enable_result_cache_for_session](r_enable_result_cache_for_session.md "r_enable_result_cache_for_session.md")
- [error_on_nondeterministic_update](r_error_on_nondeterministic_update.md "r_error_on_nondeterministic_update.md")
- [interval_forbid_composite_literals](r_interval_forbid_composite_literals.md "r_interval_forbid_composite_literals.md")
- [json_serialization_enable](r_json_serialization_enable.md "r_json_serialization_enable.md")
- [json_serialization_parse_nested_strings](r_json_serialization_parse_nested_strings.md "r_json_serialization_parse_nested_strings.md")
- [mv_enable_aqmv_for_session](r_mv_enable_aqmv_for_session.md "r_mv_enable_aqmv_for_session.md")
- [navigate_super_null_on_error](r_navigate_super_null_on_error.md "r_navigate_super_null_on_error.md")
- [parse_super_null_on_error](r_parse_super_null_on_error.md "r_parse_super_null_on_error.md")
- [spectrum_enable_pseudo_columns](r_spectrum_enable_pseudo_columns.md "r_spectrum_enable_pseudo_columns.md")
- [enable_spectrum_oid](r_spectrum_enable_spectrum_oid.md "r_spectrum_enable_spectrum_oid.md")
- [spectrum_query_maxerror](r_spectrum_query_maxerror.md "r_spectrum_query_maxerror.md")
- [stored_proc_log_min_messages](r_stored_proc_log_min_messages.md "r_stored_proc_log_min_messages.md")
- [analyze_threshold_percent](r_analyze_threshold_percent.md "r_analyze_threshold_percent.md")
- [enable_vacuum_boost](r_enable_vacuum_boost.md "r_enable_vacuum_boost.md")
- [pg_federation_repeatable_read](r_pg_federation_repeatable_read.md "r_pg_federation_repeatable_read.md")

## Connection and Configuration Management

- When connecting to Amazon Redshiftusing **JDBC**, some **session-level configurations** may also be automatically applied. For more details, refer to the JDBC session-level configuration documentation.
- Users can also define persistent **user-level configurations** using the [ALTER USER](r_ALTER_USER.md "r_ALTER_USER.md").

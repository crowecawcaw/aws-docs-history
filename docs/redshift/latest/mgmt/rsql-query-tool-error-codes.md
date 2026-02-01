Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift RSQL error codes

Success messages, warnings, and exceptions:

| Error Code | Error Class                               | Condition Name                                      |
| ---------- | ----------------------------------------- | --------------------------------------------------- |
| 00000      | Class 00 — Successful Completion          | successful_completion                               |
| 01000      | Class 01 — Warning                        | warning                                             |
| 0100C      | Class 01 — Warning                        | dynamic_result_sets_returned                        |
| 01008      | Class 01 — Warning                        | implicit_zero_bit_padding                           |
| 01003      | Class 01 — Warning                        | null_value_eliminated_in_set_function               |
| 01007      | Class 01 — Warning                        | privilege_not_granted                               |
| 01006      | Class 01 — Warning                        | privilege_not_revoked                               |
| 01004      | Class 01 — Warning                        | string_data_right_truncation                        |
| 01P01      | Class 01 — Warning                        | deprecated_feature                                  |
| 02000      | Class 02 — No Data                        | no_data                                             |
| 02001      | Class 02 — No Data                        | no_additional_dynamic_result_sets_returned          |
| 03000      | Class 03 — SQL Statement Not Yet Complete | sql_statement_not_yet_complete                      |
| 08000      | Class 08 — Connection Exception           | connection_exception                                |
| 08003      | Class 08 — Connection Exception           | connection_does_not_exist                           |
| 08006      | Class 08 — Connection Exception           | connection_failure                                  |
| 08001      | Class 08 — Connection Exception           | sqlclient_unable_to_establish_sqlconnection         |
| 08004      | Class 08 — Connection Exception           | sqlserver_rejected_establishment_of_sqlconnection   |
| 08007      | Class 08 — Connection Exception           | transaction_resolution_unknown                      |
| 08P01      | Class 08 — Connection Exception           | protocol_violation                                  |
| 09000      | Class 09 — Triggered Action Exception     | triggered_action_exception                          |
| 0A000      | Class 0A — Feature Not Supported          | feature_not_supported                               |
| 0A000      | Class 0A — Feature Not Supported          | feature_not_supported                               |
| 0B000      | Class 0B — Invalid Transaction Initiation | invalid_transaction_initiation                      |
| 0F000      | Class 0F — Locator Exception              | locator_exception                                   |
| 0F001      | Class 0F — Locator Exception              | invalid_locator_specification                       |
| 0L000      | Class 0L — Invalid Grantor                | invalid_grantor                                     |
| 0LP01      | Class 0L — Invalid Grantor                | invalid_grant_operation                             |
| 0P000      | Class 0P — Invalid Role Specification     | invalid_role_specification                          |
| 0Z000      | Class 0Z — Diagnostics Exception          | diagnostics_exception                               |
| 0Z002      | Class 0Z — Diagnostics Exception          | stacked_diagnostics_accessed_without_active_handler |
| 20000      | Class 20 — Case Not Found                 | case_not_found                                      |
| 21000      | Class 21 — Cardinality Violation          | cardinality_violation                               |

Data exceptions:

| Error Code | Error Class               | Condition Name                             |
| ---------- | ------------------------- | ------------------------------------------ |
| 22000      | Class 22 — Data Exception | data_exception                             |
| 2202E      | Class 22 — Data Exception | array_subscript_error                      |
| 22021      | Class 22 — Data Exception | character_not_in_repertoire                |
| 22008      | Class 22 — Data Exception | datetime_field_overflow                    |
| 22012      | Class 22 — Data Exception | division_by_zero                           |
| 22005      | Class 01 — Warning        | error_in_assignment                        |
| 2200B      | Class 01 — Warning        | escape_character_conflict                  |
| 22022      | Class 01 — Warning        | indicator_overflow                         |
| 22015      | Class 01 — Warning        | interval_field_overflow                    |
| 2201E      | Class 01 — Warning        | invalid_argument_for_logarithm             |
| 2201F      | Class 01 — Warning        | invalid_argument_for_power_function        |
| 2201G      | Class 01 — Warning        | invalid_argument_for_width_bucket_function |
| 22018      | Class 01 — Warning        | invalid_character_value_for_cast           |
| 22007      | Class 01 — Warning        | invalid_datetime_format                    |
| 22019      | Class 01 — Warning        | invalid_escape_character                   |
| 2200D      | Class 01 — Warning        | invalid_escape_octet                       |
| 22025      | Class 01 — Warning        | invalid_escape_sequence                    |
| 22P06      | Class 01 — Warning        | nonstandard_use_of_escape_character        |
| 22010      | Class 01 — Warning        | invalid_indicator_parameter_value          |
| 22023      | Class 01 — Warning        | invalid_parameter_value                    |
| 2201B      | Class 01 — Warning        | invalid_regular_expression                 |
| 22009      | Class 01 — Warning        | invalid_time_zone_displacement_value       |
| 2200C      | Class 01 — Warning        | invalid_use_of_escape_character            |
| 2200G      | Class 01 — Warning        | most_specific_type_mismatch                |
| 22004      | Class 01 — Warning        | null_value_not_allowed                     |
| 22002      | Class 01 — Warning        | null_value_no_indicator_parameter          |
| 22003      | Class 01 — Warning        | numeric_value_out_of_range                 |
| 22026      | Class 01 — Warning        | string_data_length_mismatch                |
| 22001      | Class 01 — Warning        | string_data_right_truncation               |
| 22011      | Class 01 — Warning        | substring_error                            |
| 22027      | Class 01 — Warning        | trim_error                                 |
| 22024      | Class 01 — Warning        | unterminated_c_string                      |
| 2200F      | Class 01 — Warning        | zero_length_character_string               |
| 22P01      | Class 01 — Warning        | floating_point_exception                   |
| 22P02      | Class 01 — Warning        | invalid_text_representation                |
| 22P03      | Class 01 — Warning        | invalid_binary_representation              |
| 22P04      | Class 01 — Warning        | bad_copy_file_format                       |
| 22P05      | Class 01 — Warning        | untranslatable_character                   |

Integrity constraint violations:

| Error Code | Error Class                                                | Condition Name                                       |
| ---------- | ---------------------------------------------------------- | ---------------------------------------------------- |
| 23000      | Class 23 — Integrity Constraint Violation                  | integrity_constraint_violation                       |
| 23001      | Class 23 — Integrity Constraint Violation                  | restrict_violation                                   |
| 23502      | Class 23 — Integrity Constraint Violation                  | not_null_violation                                   |
| 23503      | Class 23 — Integrity Constraint Violation                  | foreign_key_violation                                |
| 23505      | Class 23 — Integrity Constraint Violation                  | unique_violation                                     |
| 23514      | Class 23 — Integrity Constraint Violation                  | check_violation                                      |
| 24000      | Class 24 — Invalid Cursor State                            | invalid_cursor_state                                 |
| 01004      | Class 01 — Warning                                         | string_data_right_truncation                         |
| 25000      | Class 25 — Invalid Transaction State                       | invalid_transaction_state                            |
| 25001      | Class 25 — Invalid Transaction State                       | active_sql_transaction                               |
| 25002      | Class 25 — Invalid Transaction State                       | invalid_transaction_state                            |
| 25008      | Class 25 — Invalid Transaction State                       | held_cursor_requires_same_isolation_level            |
| 25003      | Class 25 — Invalid Transaction State                       | inappropriate_access_mode_for_branch_transaction     |
| 25004      | Class 25 — Invalid Transaction State                       | inappropriate_isolation_level_for_branch_transaction |
| 25005      | Class 25 — Invalid Transaction State                       | no_active_sql_transaction_for_branch_transaction     |
| 25006      | Class 25 — Invalid Transaction State                       | read_only_sql_transaction                            |
| 25007      | Class 25 — Invalid Transaction State                       | no_active_sql_transaction_for_branch_transaction     |
| 25P01      | Class 25 — Invalid Transaction State                       | no_active_sql_transaction                            |
| 25P02      | Class 25 — Invalid Transaction State                       | in_failed_sql_transaction                            |
| 26000      | Class 26 — Invalid SQL Statement Name                      | invalid_sql_statement_name                           |
| 28000      | Class 28 — Invalid Authorization<br>Specification          | invalid_authorization_specification                  |
| 2B000      | Class 2B — Dependent Privilege Descriptors Still<br>Exist  | dependent_privilege_descriptors_still_exist          |
| 2BP01      | Class 2B — Dependent Privilege Descriptors Still<br>Exist  | dependent_objects_still_exist                        |
| 2D000      | Class 2D — Invalid Transaction Termination                 | invalid_transaction_termination                      |
| 2F000      | Class 2F — SQL Routine Exception                           | sql_routine_exception                                |
| 2F005      | Class 2F — SQL Routine Exception                           | function_executed_no_return_statement                |
| 2F002      | Class 2F — SQL Routine Exception                           | modifying_sql_data_not_permitted                     |
| 2F003      | Class 2F — SQL Routine Exception                           | prohibited_sql_statement_attempted                   |
| 2F004      | Class 2F — SQL Routine Exception                           | reading_sql_data_not_permitted                       |
| 34000      | Class 34 — Invalid Cursor Name                             | invalid_cursor_name                                  |
| 38000      | Class 38 — External Routine Exception                      | external_routine_exception                           |
| 38001      | Class 38 — External Routine Exception                      | containing_sql_not_permitted                         |
| 38002      | Class 38 — External Routine Exception                      | modifying_sql_data_not_permitted                     |
| 38003      | Class 38 — External Routine Exception                      | prohibited_sql_statement_attempted                   |
| 38004      | Class 38 — External Routine Exception                      | reading_sql_data_not_permitted                       |
| 39000      | Class 39 — External Routine Invocation<br>Exception        | external_routine_invocation_exception                |
| 39001      | Class 39 — External Routine Invocation<br>Exception        | invalid_sqlstate_returned                            |
| 39004      | Class 39 — External Routine Invocation<br>Exception        | null_value_not_allowed                               |
| 39P01      | Class 39 — External Routine Invocation<br>Exception        | trigger_protocol_violated                            |
| 39P02      | Class 39 — External Routine Invocation<br>Exception        | srf_protocol_violated                                |
| 3D000      | Class 3D — Invalid Catalog Name                            | invalid_catalog_name                                 |
| 3F000      | Class 3F — Invalid Schema Name                             | invalid_schema_name                                  |
| 42000      | Class 42 — Syntax Error or Access Rule<br>Violation        | syntax_error_or_access_rule_violation                |
| 42601      | Class 42 — Syntax Error or Access Rule<br>Violation        | syntax_error                                         |
| 42501      | Class 42 — Syntax Error or Access Rule<br>Violation        | insufficient_privilege                               |
| 42846      | Class 42 — Syntax Error or Access Rule<br>Violation        | cannot_coerce                                        |
| 42803      | Class 42 — Syntax Error or Access Rule<br>Violation        | grouping_error                                       |
| 42830      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid_foreign_key                                  |
| 42602      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid_name                                         |
| 42622      | Class 42 — Syntax Error or Access Rule<br>Violation        | name_too_long                                        |
| 42939      | Class 42 — Syntax Error or Access Rule<br>Violation        | reserved_name                                        |
| 42804      | Class 42 — Syntax Error or Access Rule<br>Violation        | datatype_mismatch                                    |
| 42P18      | Class 42 — Syntax Error or Access Rule<br>Violation        | indeterminate_datatype                               |
| 42809      | Class 42 — Syntax Error or Access Rule<br>Violation        | wrong_object_type                                    |
| 42703      | Class 42 — Syntax Error or Access Rule<br>Violation        | undefined_column                                     |
| 42883      | Class 42 — Syntax Error or Access Rule<br>Violation        | undefined_function                                   |
| 42P01      | Class 42 — Syntax Error or Access Rule<br>Violation        | undefined_table                                      |
| 42P02      | Class 42 — Syntax Error or Access Rule<br>Violation        | undefined_parameter                                  |
| 42704      | Class 42 — Syntax Error or Access Rule<br>Violation        | undefined_object                                     |
| 42701      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate_column                                     |
| 42P03      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate_cursor                                     |
| 42P04      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate_database                                   |
| 42723      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate_function                                   |
| 42P05      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate_prepared_statement                         |
| 42P06      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate_schema                                     |
| 42P07      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate_table                                      |
| 42712      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate_alias                                      |
| 42710      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate_object                                     |
| 42702      | Class 42 — Syntax Error or Access Rule<br>Violation        | ambiguous_column                                     |
| 42725      | Class 42 — Syntax Error or Access Rule<br>Violation        | ambiguous_function                                   |
| 42P08      | Class 42 — Syntax Error or Access Rule<br>Violation        | ambiguous_parameter                                  |
| 42P09      | Class 42 — Syntax Error or Access Rule<br>Violation        | ambiguous_alias                                      |
| 42P10      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid_column_reference                             |
| 42611      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid_column_definition                            |
| 42P11      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid_cursor_definition                            |
| 42P12      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid_database_definition                          |
| 42P13      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid_function_definition                          |
| 42P14      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid_prepared_statement_definition                |
| 42P15      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid_schema_definition                            |
| 42P16      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid_table_definition                             |
| 42P17      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid_object_definition                            |
| 44000      | Class 44 — WITH CHECK OPTION Violation                     | with_check_option_violation                          |
| 53000      | Class 53 — Insufficient Resources                          | insufficient_resources                               |
| 53100      | Class 53 — Insufficient Resources                          | disk_full                                            |
| 53200      | Class 53 — Insufficient Resources                          | out_of_memory                                        |
| 53300      | Class 53 — Insufficient Resources                          | too_many_connections                                 |
| 54000      | Class 54 — Program Limit Exceeded                          | program_limit_exceeded                               |
| 54001      | Class 54 — Program Limit Exceeded                          | statement_too_complex                                |
| 54011      | Class 54 — Program Limit Exceeded                          | too_many_columns                                     |
| 54023      | Class 54 — Program Limit Exceeded                          | too_many_arguments                                   |
| 55000      | Class 55 — Object Not In Prerequisite<br>State             | object_not_in_prerequisite_state                     |
| 55006      | Class 55 — Object Not In Prerequisite<br>State             | object_in_use                                        |
| 55P02      | Class 55 — Object Not In Prerequisite<br>State             | cant_change_runtime_param                            |
| 55P03      | Class 55 — Object Not In Prerequisite<br>State             | lock_not_available                                   |
| 57000      | Class 57 — Operator Intervention                           | operator_intervention                                |
| 57014      | Class 57 — Operator Intervention                           | query_canceled                                       |
| 57P01      | Class 57 — Operator Intervention                           | admin_shutdown                                       |
| 57P02      | Class 57 — Operator Intervention                           | crash_shutdown                                       |
| 57P03      | Class 57 — Operator Intervention                           | cannot_connect_now                                   |
| 58000      | Class 58 — System Error (errors external to<br>PostgreSQL) | system_error                                         |
| 58030      | Class 58 — System Error (errors external to<br>PostgreSQL) | io_error                                             |
| 58P01      | Class 58 — System Error (errors external to<br>PostgreSQL) | undefined_file                                       |
| 58P02      | Class 58 — System Error (errors external to<br>PostgreSQL) | duplicate_file                                       |
| F0000      | Class F0 — Configuration File Error                        | duplicate_file                                       |
| F0001      | Class F0 — Configuration File Error                        | lock_file_exists                                     |
| P0000      | Class P0 — PL/pgSQL Error                                  | plpgsql_error                                        |
| P0001      | Class P0 — PL/pgSQL Error                                  | raise_exception                                      |
| P0002      | Class P0 — PL/pgSQL Error                                  | no_data_found                                        |
| P0003      | Class P0 — PL/pgSQL Error                                  | too_many_rows                                        |
| XX000      | Class XX — Internal Error                                  | internal_error                                       |
| XX001      | Class XX — Internal Error                                  | data_corrupted                                       |
| XX002      | Class XX — Internal Error                                  | index_corrupted                                      |

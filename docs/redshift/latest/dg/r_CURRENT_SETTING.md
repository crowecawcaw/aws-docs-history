Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CURRENT_SETTING

CURRENT_SETTING returns the current value of the specified configuration
parameter.

This function is equivalent to the [SHOW](r_SHOW.md "r_SHOW.md")
command.

## Syntax

```
current_setting('*parameter*')
```

The following statement returns the current value of the specified session context variable.

```
current_setting('*variable\_name*')
current_setting('*variable\_name*'[, *error\_if\_undefined*])
```

## Arguments

_parameter_

Parameter value to display. For a list of configuration parameters, see
[Configuration reference](cm_chap_ConfigurationRef.md "cm_chap_ConfigurationRef.md")

_variable_name_

The name of the variable to display. This must be a string constant for session context variables.

_error_if_undefined_

(Optional) A boolean value that specifies the behavior if the variable name doesn't exist. When error_if_undefined is set to `TRUE`, which is the default, Amazon Redshift throws an error. When error_if_undefined is set to `FALSE`, Amazon Redshift returns `NULL`. Amazon Redshift supports the _error_if_undefined_ parameter only for session context variables. This can't be used when the input is a configuration parameter.

## Return type

Returns a `CHAR` or `VARCHAR` string.

## Examples

To return the current setting for the `query_group`
parameter, use the following example.

````
`SELECT CURRENT_SETTING('query_group');`

`+-----------------+
| current_setting | +-----------------+
| unset | +-----------------+` ``` To return the current setting for the variable `app_context.user_id`, use the following example. ``` `SELECT CURRENT_SETTING('app_context.user_id', FALSE);` ```
````

Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# CURRENT\_SETTING

CURRENT\_SETTING returns the current value of the specified configuration
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

_variable\_name_

The name of the variable to display. This must be a string constant for session context variables.

_error\_if\_undefined_

(Optional) A boolean value that specifies the behavior if the variable name doesn't exist. When error\_if\_undefined is set to `TRUE`, which is the default, Amazon Redshift throws an error. When error\_if\_undefined is set to `FALSE`, Amazon Redshift returns `NULL`. Amazon Redshift supports the _error\_if\_undefined_ parameter only for session context variables. This can't be used when the input is a configuration parameter.

## Return type

Returns a `CHAR` or `VARCHAR` string.

## Examples

To return the current setting for the `query_group`
parameter, use the following example.

```
`SELECT CURRENT_SETTING('query_group');`

`+-----------------+
| current_setting |
+-----------------+
| unset |
+-----------------+`
```

To return the current setting for the variable `app_context.user_id`, use the following example.

```
`SELECT CURRENT_SETTING('app_context.user_id', FALSE);`
```

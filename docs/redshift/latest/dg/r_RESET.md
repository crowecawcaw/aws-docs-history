Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# RESET

Restores the value of a configuration parameter to its default value.

You can reset either a single specified parameter or all parameters at once. To set a
parameter to a specific value, use the [SET](r_SET.md "r_SET.md")
command. To display the current value of a parameter, use the [SHOW](r_SHOW.md "r_SHOW.md") command.

## Syntax

```
RESET { *parameter\_name* | ALL }
```

The following statement sets the value of a session context variable to NULL.

```
RESET { *variable\_name* | ALL }
```

## Parameters

_parameter_name_

Name of the parameter to reset. See [Modifying the server
configuration](cm_chap_ConfigurationRef.md#t_Modifying_the_default_settings "cm_chap_ConfigurationRef.md#t_Modifying_the_default_settings") for more documentation
about parameters.

ALL

Resets all runtime parameters, including all the session context
variables.

_variable_

The name of the variable to reset. If the value to RESET is a session
context variable, Amazon Redshift sets it to NULL.

## Examples

The following example resets the `query_group` parameter to its default
value:

```
reset query_group;

```

The following example resets all runtime parameters to their default values.

```
reset all;

```

The following example resets the context variable.

```
RESET app_context.user_id;
```

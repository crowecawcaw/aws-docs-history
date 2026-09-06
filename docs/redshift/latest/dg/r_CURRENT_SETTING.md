

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# CURRENT\_SETTING
<a name="r_CURRENT_SETTING"></a>

 CURRENT\_SETTING returns the current value of the specified configuration parameter.

This function is equivalent to the [SHOW](r_SHOW.md) command.

## Syntax
<a name="r_CURRENT_SETTING-synopsis"></a>

```
current_setting('parameter')
```

The following statement returns the current value of the specified session context variable.

```
current_setting('variable_name')
current_setting('variable_name'[, error_if_undefined])
```

## Arguments
<a name="r_CURRENT_SETTING-argument"></a>

 *parameter*   
Parameter value to display. For a list of configuration parameters, see [Configuration reference](cm_chap_ConfigurationRef.md)

 *variable\_name *   
The name of the variable to display. This must be a string constant for session context variables.

 *error\_if\_undefined*   
(Optional) A boolean value that specifies the behavior if the variable name doesn't exist. When error\_if\_undefined is set to `TRUE`, which is the default, Amazon Redshift throws an error. When error\_if\_undefined is set to `FALSE`, Amazon Redshift returns `NULL`. Amazon Redshift supports the *error\_if\_undefined* parameter only for session context variables. This can't be used when the input is a configuration parameter.

## Return type
<a name="r_CURRENT_SETTING-return-type"></a>

Returns a `CHAR` or `VARCHAR` string.

## Examples
<a name="r_CURRENT_SETTING-example"></a>

To return the current setting for the `query_group` parameter, use the following example.

```
SELECT CURRENT_SETTING('query_group');

+-----------------+
| current_setting |
+-----------------+
| unset           |
+-----------------+
```

To return the current setting for the variable `app_context.user_id`, use the following example.

```
SELECT CURRENT_SETTING('app_context.user_id', FALSE);
```
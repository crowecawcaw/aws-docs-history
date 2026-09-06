

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SET\_CONFIG
<a name="r_SET_CONFIG"></a>

Sets a configuration parameter to a new setting.

 This function is equivalent to the SET command in SQL.

## Syntax
<a name="r_SET_CONFIG-synopsis"></a>

```
SET_CONFIG('parameter', 'new_value' , is_local)
```

The following statement sets a session context variable to a new setting.

```
set_config('variable_name', 'new_value' , is_local)
```

## Arguments
<a name="r_SET_CONFIG-parameters"></a>

 *parameter*   
Parameter to set.

 *variable\_name*   
The name of the variable to set.

 *new\_value*   
New value of the parameter.

 *is\_local*   
If true, parameter value applies only to the current transaction. Valid values are `true` or `1` and `false` or `0`. 

## Return type
<a name="r_SET_CONFIG-return-type"></a>

Returns a `CHAR` or `VARCHAR` string.

## Examples
<a name="r_SET_CONFIG-examples"></a>

To set the value of the `query_group` parameter to `test` for the current transaction only, use the following example. 

```
SELECT SET_CONFIG('query_group', 'test', true);

+------------+
| set_config |
+------------+
| test       |
+------------+
```

To set session context variables, use the following example. 

```
SELECT SET_CONFIG(‘app.username’, ‘cuddy’, FALSE);
```
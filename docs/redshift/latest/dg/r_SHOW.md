Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW

Displays the current value of a server configuration parameter. This value may be
specific to the current session if a SET command is in effect. For a list of configuration
parameters, see [Configuration reference](cm_chap_ConfigurationRef.md "cm_chap_ConfigurationRef.md").

## Syntax

```
SHOW { *parameter\_name* | ALL }
```

The following statement displays the current value of a session context variable. If
the variable doesn't exist, Amazon Redshift throws an error.

```
SHOW *variable\_name*
```

## Parameters

_parameter_name_

Displays the current value of the specified parameter.

ALL

Displays the current values of all of the parameters.

_variable_name_

Displays the current value of the specified variable.

## Examples

The following example displays the value for the query_group parameter:

```
show query_group;

query_group

unset
(1 row)
```

The following example displays a list of all parameters and their values:

```
show all;
name        |   setting
--------------------+--------------
datestyle          | ISO, MDY
extra_float_digits | 0
query_group        | unset
search_path        | $user,public
statement_timeout  | 0

```

The following example displays the current value of the specified variable.

```
SHOW app_context.user_id;
```

Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CHANGE_USER_PRIORITY

CHANGE_USER_PRIORITY enables superusers to modify the priority of all queries issued by a user that are either running or waiting in workload management (WLM).
Only one user, session, or query can run with the priority `CRITICAL`.

## Syntax

```
CHANGE_USER_PRIORITY(*user\_name*, *priority*)
```

## Arguments

_user_name_

The database user name whose query priority is changed.

_priority_

The new priority to be assigned to all queries issued by
`user_name`. This argument must be a string with the value
`CRITICAL`, `HIGHEST`, `HIGH`,
`NORMAL`, `LOW`, `LOWEST`, or
`RESET`. Only superusers can change the priority to
`CRITICAL`. Changing the priority to `RESET`
removes the priority setting for `user_name`.

## Return type

None

## Examples

To change the priority for the user
`analysis_user` to `LOWEST`, use the following example.

````
`SELECT CHANGE_USER_PRIORITY('analysis_user', 'lowest');`

`+-------------------------------------------------------------------------------------+
| change_user_priority | +-------------------------------------------------------------------------------------+
| Succeeded to change user priority. Changed user (analysis_user) priority to lowest. | +-------------------------------------------------------------------------------------+` ``` To change the priority to `LOW`, use the following example. ``` `SELECT CHANGE_USER_PRIORITY('analysis_user', 'low');` `+----------------------------------------------------------------------------------------------+
| change_user_priority | +----------------------------------------------------------------------------------------------+
| Succeeded to change user priority. Changed user (analysis_user) priority from Lowest to low. | +----------------------------------------------------------------------------------------------+` ``` To reset the priority, use the following example. ``` `SELECT CHANGE_USER_PRIORITY('analysis_user', 'reset');` `+-------------------------------------------------------+
| change_user_priority | +-------------------------------------------------------+
| Succeeded to reset priority for user (analysis_user). | +-------------------------------------------------------+` ```
````

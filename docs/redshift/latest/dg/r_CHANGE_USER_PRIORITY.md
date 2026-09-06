

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# CHANGE\_USER\_PRIORITY
<a name="r_CHANGE_USER_PRIORITY"></a>

CHANGE\_USER\_PRIORITY enables superusers to modify the priority of all queries issued by a user that are either running or waiting in workload management (WLM). Only one user, session, or query can run with the priority `CRITICAL`.

## Syntax
<a name="r_CHANGE_USER_PRIORITY-synopsis"></a>

```
CHANGE_USER_PRIORITY(user_name, priority)
```

## Arguments
<a name="r_CHANGE_USER_PRIORITY-argument"></a>

 *user\_name*   
The database user name whose query priority is changed. 

 *priority*   
The new priority to be assigned to all queries issued by `user_name`. This argument must be a string with the value `CRITICAL`, `HIGHEST`, `HIGH`, `NORMAL`, `LOW`, `LOWEST`, or `RESET`. Only superusers can change the priority to `CRITICAL`. Changing the priority to `RESET` removes the priority setting for `user_name`.

## Return type
<a name="r_CHANGE_USER_PRIORITY-return-type"></a>

None

## Examples
<a name="r_CHANGE_USER_PRIORITY-example"></a>

To change the priority for the user `analysis_user` to `LOWEST`, use the following example.

```
SELECT CHANGE_USER_PRIORITY('analysis_user', 'lowest');

+-------------------------------------------------------------------------------------+
|                                change_user_priority                                 |
+-------------------------------------------------------------------------------------+
| Succeeded to change user priority. Changed user (analysis_user) priority to lowest. |
+-------------------------------------------------------------------------------------+
```

To change the priority to `LOW`, use the following example.

```
SELECT CHANGE_USER_PRIORITY('analysis_user', 'low');

+----------------------------------------------------------------------------------------------+
|                                     change_user_priority                                     |
+----------------------------------------------------------------------------------------------+
| Succeeded to change user priority. Changed user (analysis_user) priority from Lowest to low. |
+----------------------------------------------------------------------------------------------+
```

To reset the priority, use the following example.

```
SELECT CHANGE_USER_PRIORITY('analysis_user', 'reset');

+-------------------------------------------------------+
|                 change_user_priority                  |
+-------------------------------------------------------+
| Succeeded to reset priority for user (analysis_user). |
+-------------------------------------------------------+
```
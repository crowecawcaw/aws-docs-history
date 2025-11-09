# The

create_passthrough_verify_fcn procedure

The `create_passthrough_verify_fcn` procedure is supported for all
versions of RDS for Oracle.

You can create a custom function to verify passwords by using the Amazon RDS procedure
`rdsadmin.rdsadmin_password_verify.create_passthrough_verify_fcn`. The
`create_passthrough_verify_fcn` procedure has the following parameters.

| Parameter name           | Data type | Default | Required | Description                                                                                                                                                                                                                                 |
| ------------------------ | --------- | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `p_verify_function_name` | varchar2  | —       | Yes      | The name for your custom verification function. This is a<br>wrapper function that is created for you in the SYS schema,<br>and it doesn't contain any verification logic. You assign<br>this function to user profiles.                    |
| `p_target_owner`         | varchar2  | —       | Yes      | The schema owner for your custom verification<br>function.                                                                                                                                                                                  |
| `p_target_function_name` | varchar2  | —       | Yes      | The name of your existing custom function that contains<br>the verification logic. Your custom function must return a<br>boolean. Your function should return `true` if<br>the password is valid and `false` if the password<br>is invalid. |

The following example creates a password verification function that uses the
logic from the function named `PASSWORD_LOGIC_EXTRA_STRONG`.

```
begin
    rdsadmin.rdsadmin_password_verify.create_passthrough_verify_fcn(
        p_verify_function_name => '`CUSTOM_PASSWORD_FUNCTION`',
        p_target_owner         => '`TEST_USER`',
        p_target_function_name => '`PASSWORD_LOGIC_EXTRA_STRONG`');
end;
/
```

To associate the verification function with a user profile, use `alter
 profile`. The following example associates the verification function
with the `DEFAULT` user profile.

```
ALTER PROFILE `DEFAULT` LIMIT PASSWORD_VERIFY_FUNCTION `CUSTOM_PASSWORD_FUNCTION`;
```

# The

create_verify_function procedure

You can create a custom function to verify passwords by using the Amazon RDS
procedure `rdsadmin.rdsadmin_password_verify.create_verify_function`.
The `create_verify_function` procedure is supported for all versions
of RDS for Oracle.

The `create_verify_function` procedure has the following parameters.

| Parameter name              | Data type | Default | Required | Description                                                                                                                             |
| --------------------------- | --------- | ------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `p_verify_function_name`    | varchar2  | —       | Yes      | The name for your custom function. This function is<br>created for you in the SYS schema. You assign this function<br>to user profiles. |
| `p_min_length`              | number    | 8       | No       | The minimum number of characters required.                                                                                              |
| `p_max_length`              | number    | 256     | No       | The maximum number of characters allowed.                                                                                               |
| `p_min_letters`             | number    | 1       | No       | The minimum number of letters required.                                                                                                 |
| `p_min_uppercase`           | number    | 0       | No       | The minimum number of uppercase letters required.                                                                                       |
| `p_min_lowercase`           | number    | 0       | No       | The minimum number of lowercase letters required.                                                                                       |
| `p_min_digits`              | number    | 1       | No       | The minimum number of digits required.                                                                                                  |
| `p_min_special`             | number    | 0       | No       | The minimum number of special characters required.                                                                                      |
| `p_min_different_chars`     | number    | 3       | No       | The minimum number of different characters required<br>between the old and new password.                                                |
| `p_disallow_username`       | boolean   | true    | No       | Set to `true` to disallow the user name in the<br>password.                                                                             |
| `p_disallow_reverse`        | boolean   | true    | No       | Set to `true` to disallow the reverse of the<br>user name in the password.                                                              |
| `p_disallow_db_name`        | boolean   | true    | No       | Set to `true` to disallow the database or<br>server name in the password.                                                               |
| `p_disallow_simple_strings` | boolean   | true    | No       | Set to `true` to disallow simple strings as the<br>password.                                                                            |
| `p_disallow_whitespace`     | boolean   | false   | No       | Set to `true` to disallow white space<br>characters in the password.                                                                    |
| `p_disallow_at_sign`        | boolean   | false   | No       | Set to `true` to disallow the @<br>character in the password.                                                                           |

You can create multiple password verification functions.

There are restrictions on the name of your custom function. Your custom
function can't have the same name as an existing system object. The name can be
no more than 30 characters long. Also, the name must include one of the
following strings: `PASSWORD`, `VERIFY`,
`COMPLEXITY`, `ENFORCE`, or `STRENGTH`.

The following example creates a function named
`CUSTOM_PASSWORD_FUNCTION`. The function requires that a password
has at least 12 characters, 2 uppercase characters, 1 digit, and 1 special
character, and that the password disallows the @ character.

```
begin
    rdsadmin.rdsadmin_password_verify.create_verify_function(
        p_verify_function_name => '`CUSTOM_PASSWORD_FUNCTION`',
        p_min_length           => `12`,
        p_min_uppercase        => `2`,
        p_min_digits           => `1`,
        p_min_special          => `1`,
        p_disallow_at_sign     => `true`);
end;
/
```

To see the text of your verification function, query `DBA_SOURCE`.
The following example gets the text of a custom password function named
`CUSTOM_PASSWORD_FUNCTION`.

```
COL TEXT FORMAT a150

  SELECT TEXT
    FROM DBA_SOURCE
   WHERE OWNER = 'SYS'
     AND NAME = '`CUSTOM_PASSWORD_FUNCTION`'
ORDER BY LINE;
```

To associate your verification function with a user profile, use `ALTER
 PROFILE`. The following example associates a verification PL/SQL function
named `CUSTOM_PASSWORD_FUNCTION` with the `DEFAULT` user profile. `PASSWORD_VERIFY_FUNCTION`
is the Oracle profile resource name.

```
ALTER PROFILE `DEFAULT` LIMIT PASSWORD_VERIFY_FUNCTION `CUSTOM_PASSWORD_FUNCTION`;
```

To see which user profiles are associated with which verification functions,
query `DBA_PROFILES`. The following example gets the profiles that
are associated with the custom verification function named
`CUSTOM_PASSWORD_FUNCTION`.

```
SELECT * FROM DBA_PROFILES WHERE RESOURCE_NAME = 'PASSWORD_VERIFY_FUNCTION' AND LIMIT = '`CUSTOM_PASSWORD_FUNCTION`';


PROFILE                    RESOURCE_NAME                     RESOURCE  LIMIT
-------------------------  --------------------------------  --------  ------------------------
DEFAULT                    PASSWORD_VERIFY_FUNCTION          PASSWORD  CUSTOM_PASSWORD_FUNCTION

```

The following example gets all profiles and the password verification
functions that they are associated with.

```
SELECT * FROM DBA_PROFILES WHERE RESOURCE_NAME = 'PASSWORD_VERIFY_FUNCTION';

PROFILE                    RESOURCE_NAME                     RESOURCE  LIMIT
-------------------------  --------------------------------  --------  ------------------------
DEFAULT                    PASSWORD_VERIFY_FUNCTION          PASSWORD  CUSTOM_PASSWORD_FUNCTION
RDSADMIN                   PASSWORD_VERIFY_FUNCTION          PASSWORD  NULL

```

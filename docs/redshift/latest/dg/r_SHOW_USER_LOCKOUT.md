Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SHOW USER LOCKOUT

Use SHOW USER LOCKOUT to audit which users are currently locked, determine whether each
lockout was automatic or manual, and review recent failed-login activity before you unlock
a user. Federated users aren't included. This command is available only to superusers. For
more information, see [max\_failed\_login\_attempts](max_failed_login_attempts.md "max_failed_login_attempts.md").

## Required privileges

To use SHOW USER LOCKOUT, you must be a superuser.

## Syntax

```
SHOW USER LOCKOUT
```

## Output columns

user\_name

The name of the database user.

is\_locked

Specifies whether the user is currently locked.

lock\_reason

The reason the user was locked. The value is `automatic` when Amazon Redshift
locks the user after reaching the failed-attempt threshold, or
`manual` when a superuser locks the user with ALTER USER NOLOGIN.
This value is null when the user isn't locked.

locked\_at

The timestamp when the user was locked.

last\_failed\_at

The timestamp of the most recent failed login attempt.

failed\_login\_attempts

The number of consecutive failed login attempts.

locked\_by

The ID of the user that locked this user. This value is null for automatic
lockout.

## Examples

The following example displays the lockout status for all password-based users:

```
SHOW USER LOCKOUT;

 user_name    | is_locked | lock_reason      | locked_at           | last_failed_at      | failed_login_attempts | locked_by
--------------+-----------+------------------+---------------------+---------------------+-----------------------+-----------
 data_analyst | true      | automatic        | 2026-08-10 14:02:11 | 2026-08-10 14:02:11 |                     5 |
 sales_user   | true      | manual           | 2026-08-10 09:15:44 |                     |                     0 |       100
 report_user  | false     |                  |                     | 2026-08-09 22:31:07 |                     2 |
(3 rows)
```

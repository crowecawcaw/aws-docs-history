Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# max\_failed\_login\_attempts

## Values (default in bold)

**5**, 2 to 50

## Description

Sets the number of consecutive failed password login attempts that Amazon Redshift allows
before it locks a database user. When the number of consecutive failed attempts reaches
this value, Amazon Redshift locks the user. A locked user remains locked until a superuser or a
user with the ALTER USER privilege unlocks them. A successful login resets the counter.
This parameter applies to password-based authentication only. Federated users aren't
affected.

This parameter is cluster-wide. To set it, you must be a superuser and use an ALTER
SYSTEM SET command. You can't change it with the SET command. The change applies without
a cluster restart. The valid range is 2 to 50; a value outside this range returns an
error.

## Example

```
ALTER SYSTEM SET max_failed_login_attempts = 10;
```

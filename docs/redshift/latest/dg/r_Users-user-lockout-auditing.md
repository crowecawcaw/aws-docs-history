Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Auditing locked users

To review which users are currently locked, see whether each lockout was automatic
or manual, and review recent failed-login activity, a superuser can run the SHOW USER
LOCKOUT command. For more information, see [SHOW USER LOCKOUT](r_SHOW_USER_LOCKOUT.md "r_SHOW_USER_LOCKOUT.md").

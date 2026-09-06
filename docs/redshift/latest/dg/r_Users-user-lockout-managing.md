

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Locking and unlocking users
<a name="r_Users-user-lockout-managing"></a>

In addition to automatic lockout, a superuser or a user with the ALTER USER privilege can lock and unlock a user manually.
+ To lock a user manually, use ALTER USER with the NOLOGIN option. Amazon Redshift then rejects that user's connection attempts. Locking a user doesn't end that user's existing sessions.

  ```
  ALTER USER data_analyst NOLOGIN;
  ```
+ To unlock a user, use ALTER USER with the LOGIN PASSWORD option and provide a new password. Unlocking a user resets that user's failed-login counter.

  ```
  ALTER USER data_analyst LOGIN PASSWORD 'NewStr0ngP@ssword';
  ```

For more information about these options, see [ALTER USER](r_ALTER_USER.md).
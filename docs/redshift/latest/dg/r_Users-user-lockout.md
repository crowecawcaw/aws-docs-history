

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# User lockout for database users
<a name="r_Users-user-lockout"></a>

With Amazon Redshift, you can protect your password-based database users against brute-force password attacks. Amazon Redshift tracks consecutive failed password sign-in attempts for each user you create. When the number of failed attempts reaches a threshold, Amazon Redshift locks the user and rejects further connection attempts until a superuser or a user with the ALTER USER privilege unlocks the user. A successful sign-in resets the counter. This protection is enabled by default.

A superuser sets the threshold for the cluster with the [max\_failed\_login\_attempts](max_failed_login_attempts.md) configuration parameter. The default is 5 consecutive failed attempts, and you can set a value from 2 to 50. You set this parameter by using an ALTER SYSTEM SET command, as shown in the following example.

```
ALTER SYSTEM SET max_failed_login_attempts = 10;
```

User lockout applies to password-based database users only. Federated users aren't affected, including users who authenticate through AWS Identity and Access Management (IAM), AWS IAM Identity Center, or a native identity provider (IdP). Amazon Redshift also doesn't automatically lock the admin user.


 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Regaining access if the admin user is locked
<a name="r_Users-user-lockout-recovery"></a>

A superuser or a user with the ALTER USER privilege unlocks a locked user with the ALTER USER LOGIN PASSWORD command. If the admin user is locked and no other superuser can sign in, you can reset the admin password to regain access. Resetting the admin password restores the admin user's ability to sign in.
+ For a provisioned cluster, use the [ModifyCluster](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyCluster.html) API operation, or the equivalent AWS Management Console or AWS CLI command, to set a new admin password.
+ For Amazon Redshift Serverless, use the [UpdateNamespace](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateNamespace.html) API operation, or the equivalent AWS Management Console or AWS CLI command, to set a new admin password. You must provide both `adminUsername` and `adminUserPassword` in the same request.
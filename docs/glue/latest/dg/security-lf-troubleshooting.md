

# Troubleshooting
<a name="security-lf-troubleshooting"></a>

See the following sections for troubleshooting solutions.

## Logging
<a name="security-lf-troubleshooting-logging"></a>

AWS Glue uses Spark resources profiles to split job execution. AWS Glue uses the user profile to run the code you supplied, while the system profile enforces Lake Formation policies. You can access the logs for the tasks ran as the user profile.

## Live UI and Spark History Server
<a name="security-lf-troubleshooting-live-ui"></a>

The Live UI and the Spark History Server have all Spark events generated from the user profile and redacted events generated from the system driver.

You can see all of the tasks from both the user and system drivers in the **Executors** tab. However, log links are available only for the user profile. Also, some information is redacted from Live UI, such as the number of output records.

## Job failed with insufficient Lake Formation permissions
<a name="security-lf-troubleshooting-insufficient-lf-permissions"></a>

Make sure that your job runtime role has the permissions to run SELECT and DESCRIBE on the table that you are accessing.

## Job with RDD execution failed
<a name="security-lf-troubleshooting-rdd-execution"></a>

AWS Glue currently doesn't support resilient distributed dataset (RDD) operations on Lake Formation-enabled jobs.

## Unable to access data files in Amazon S3
<a name="security-lf-troubleshooting-s3-access-failure"></a>

Make sure you have registered the location of the data lake in Lake Formation.

## Security validation exception
<a name="security-lf-troubleshooting-security-validation"></a>

AWS Glue detected a security validation error. Contact AWS support for assistance.

## Sharing AWS Glue Data Catalog and tables across accounts
<a name="security-lf-troubleshooting-cross-account"></a>

You can share databases and tables across accounts and still use Lake Formation. For more information, see [Cross-account data sharing in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-permissions.html) and [How do I share AWS Glue Data Catalog and tables cross-account using ?](https://repost.aws/knowledge-center/glue-lake-formation-cross-account).
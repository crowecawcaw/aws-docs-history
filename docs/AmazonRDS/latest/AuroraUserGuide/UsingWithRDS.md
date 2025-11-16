# IAM database authentication

You can authenticate to your DB
cluster
using AWS Identity and Access Management (IAM) database authentication. IAM database authentication works with
Aurora MySQL,
and Aurora PostgreSQL. With this authentication method, you don't
need to use a password when you connect to a DB cluster.
Instead, you use an authentication token.

An _authentication token_ is a unique string of characters that
Amazon Aurora
generates on request. Authentication tokens are generated using AWS Signature Version 4.
Each token has a lifetime of 15 minutes. You don't need to store user credentials in
the database, because authentication is managed externally using IAM. You can also still
use standard database authentication. The token is only used for authentication and doesn't
affect the session after it is established.

IAM database authentication provides the following benefits:

- Network traffic to and from the database is encrypted using Secure Socket Layer (SSL)
  or Transport Layer Security (TLS). For more information about using SSL/TLS with
  Amazon Aurora,
  see [Using SSL/TLS to encrypt a connection to a DB
  cluster](UsingWithRDS.md "UsingWithRDS.md").
- You can use IAM to centrally manage access to your database resources, instead of
  managing access individually on each DB cluster.
- For applications running on Amazon EC2, you can use profile credentials specific to
  your EC2 instance to access your database instead of a password, for greater
  security.
  In general, consider using IAM database authentication when your applications create fewer than 200 connections
  per second, and you don't want to manage usernames and passwords directly in your application code.

The Amazon Web Services (AWS) JDBC Driver supports IAM database authentication. For more information, see
[AWS
IAM Authentication Plugin](https://github.com/aws/aws-advanced-jdbc-wrapper/blob/main/docs/using-the-jdbc-driver/using-plugins/UsingTheIamAuthenticationPlugin.md "https://github.com/aws/aws-advanced-jdbc-wrapper/blob/main/docs/using-the-jdbc-driver/using-plugins/UsingTheIamAuthenticationPlugin.md") in the [Amazon Web Services (AWS) JDBC Driver GitHub repository](https://github.com/aws/aws-advanced-jdbc-wrapper "https://github.com/aws/aws-advanced-jdbc-wrapper").

The Amazon Web Services (AWS) Python Driver supports IAM database authentication. For more information, see
[AWS IAM Authentication Plugin](https://github.com/aws/aws-advanced-python-wrapper/blob/main/docs/using-the-python-driver/using-plugins/UsingTheIamAuthenticationPlugin.md "https://github.com/aws/aws-advanced-python-wrapper/blob/main/docs/using-the-python-driver/using-plugins/UsingTheIamAuthenticationPlugin.md") in the [Amazon Web Services (AWS) Python Driver GitHub
repository](https://github.com/aws/aws-advanced-python-wrapper "https://github.com/aws/aws-advanced-python-wrapper").

Navigate through the following topics to learn the process to set IAM for DB authentication:

- [Enabling and disabling IAM database
  authentication](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md")
- [Creating and using an IAM policy for
  IAM database access](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md")
- [Creating a database account using
  IAM authentication](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md")
- [Connecting to your DB cluster using IAM authentication](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md")

## Region and version availability

Feature availability and support varies across specific versions of each Aurora database engine, and across AWS Regions.
For more information on version and Region availability with Aurora and IAM database authentication, see
[Supported
Regions and Aurora DB engines for IAM database
authentication](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").

For Aurora MySQL, all supported DB instance classes support IAM database authentication,
except for db.t2.small and db.t3.small. For information about the supported DB instance classes, see
[Supported DB engines for DB instance classes](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").

## CLI and SDK support

IAM database authentication is available for the [AWS CLI](../../../cli/latest/reference/rds/generate-db-auth-token.md "../../../cli/latest/reference/rds/generate-db-auth-token.md")
and for the following language-specific AWS SDKs:

- [AWS SDK for .NET](../../../sdkfornet/v3/apidocs/items/RDS/TRDSAuthTokenGenerator.md "../../../sdkfornet/v3/apidocs/items/RDS/TRDSAuthTokenGenerator.md")
- [AWS SDK for C++](../../../sdk-for-cpp/latest/api/class_aws_1_1_r_d_s_1_1_r_d_s_client.md#ae134ffffed5d7672f6156d324e7bd392 "../../../sdk-for-cpp/latest/api/class_aws_1_1_r_d_s_1_1_r_d_s_client.md#ae134ffffed5d7672f6156d324e7bd392")
- [AWS SDK for Go](../../../sdk-for-go/api/service/rds.md#pkg-overview "../../../sdk-for-go/api/service/rds.md#pkg-overview")
- [AWS SDK for Java](../../../sdk-for-java/latest/reference/software/amazon/awssdk/services/rds/RdsUtilities.md "../../../sdk-for-java/latest/reference/software/amazon/awssdk/services/rds/RdsUtilities.md")
- [AWS SDK for JavaScript](../../../AWSJavaScriptSDK/v3/latest/modules/_aws_sdk_rds_signer.md "../../../AWSJavaScriptSDK/v3/latest/modules/_aws_sdk_rds_signer.md")
- [AWS SDK for PHP](../../../aws-sdk-php/v3/api/class-Aws.Rds.md "../../../aws-sdk-php/v3/api/class-Aws.Rds.md")
- [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.generate_db_auth_token "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.generate_db_auth_token")
- [AWS SDK for Ruby](../../../sdk-for-ruby/v3/api/Aws/RDS/AuthTokenGenerator.md "../../../sdk-for-ruby/v3/api/Aws/RDS/AuthTokenGenerator.md")

## Limitations for IAM database authentication

When using IAM database authentication, the following limitations apply:

- Currently, IAM database authentication doesn't support all global condition context keys.

For more information about global condition context keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

- For PostgreSQL, if the IAM role (`rds_iam`) is added to a user (including
  the RDS master user), IAM authentication takes precedence over password authentication,
  so the user must log in as an IAM user.
- You cannot use a custom Route 53 DNS record instead of the DB cluster endpoint to generate the authentication token.
- CloudWatch and CloudTrail don't log IAM authentication. These services do not track `generate-db-auth-token`
  API calls that authorize the IAM role to enable database connection.
- IAM DB authentication requires compute resources on the database cluster. You must have between 300 and 1000 MiB
  extra memory on your database for reliable connectivity.
  To see the memory needed for your workload, compare the RES column for RDS processes in the Enhanced Monitoring processlist
  before and after enabling IAM DB authentication.
  See [Viewing OS metrics in the RDS console](USER_Monitoring.OS.md "USER_Monitoring.OS.md").

If you are using a burstable class instance, avoid running out of memory by reducing
the memory used by other parameters like buffers and cache by the same amount.

- For Aurora MySQL, you can't use password based authentication
  for a database user you configure with IAM authentication.
- IAM DB authentication is not supported for RDS on Outposts for any engine.

## Recommendations for IAM database authentication

We recommend the following when using IAM database authentication:

- Use IAM database authentication when your application requires fewer than
  200 new IAM database authentication connections per second.

The database engines that work with Amazon Aurora
don't impose any limits on authentication attempts per second. However, when you use IAM database authentication,
your application must generate an authentication token. Your application then uses that
token to connect to the DB cluster. If you exceed the limit of maximum new
connections per second, then the extra overhead of IAM database authentication can cause
connection throttling.

Consider using connection pooling in your applications to mitigate constant
connection creation. This can reduce the overhead from IAM DB authentication
and allow your applications to reuse existing connections. Alternatively,
consider using RDS Proxy for these use cases. RDS Proxy has additional costs. See
[RDS Proxy
pricing](https://aws.amazon.com/rds/proxy/pricing/ "https://aws.amazon.com/rds/proxy/pricing/").

- The size of an IAM database authentication token depends on many things including the number of IAM tags,
  IAM service policies, ARN lengths, as well as other IAM and database properties. The minimum size of this token is
  generally about 1 KB but can be larger. Since this token is used as the password in the connection string to the database
  using IAM authentication, you should ensure that your database driver (e.g., ODBC) and/or any tools do not limit or otherwise
  truncate this token due to its size. A truncated token will cause the authentication validation done by the database and IAM to fail.
- If you are using temporary credentials when creating an IAM database
  authentication token, the temporary credentials must still be valid when using
  the IAM database authentication token to make a connection request.

## Unsupported AWS global condition context keys

IAM database authentication does not support the following subset of AWS global condition context keys.

- `aws:Referer`
- `aws:SourceIp`
- `aws:SourceVpc`
- `aws:SourceVpce`
- `aws:UserAgent`
- `aws:VpcSourceIp`

For more information, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

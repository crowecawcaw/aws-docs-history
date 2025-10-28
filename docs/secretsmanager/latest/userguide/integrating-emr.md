# How Amazon EMR uses Secrets Manager

Amazon EMR is a platform that simplifies running big data frameworks, such as Apache Hadoop and
Apache Spark, on AWS to process and analyze vast amounts of data. When you use these
frameworks and related open-source projects such as Apache Hive and Apache Pig, you can
process data for analytics and business intelligence workloads. You can also use Amazon EMR to
transform and move large amounts of data into and out of other AWS data stores and
databases, such as Amazon S3 and Amazon DynamoDB.

## How Amazon EMR running on Amazon EC2 uses Secrets Manager

When you create a cluster in Amazon EMR, you can provide application configuration data to
the cluster with a secret in Secrets Manager. For more information, see [Store sensitive configuration
data in Secrets Manager](../../../emr/latest/ReleaseGuide/storing-sensitive-data.md "../../../emr/latest/ReleaseGuide/storing-sensitive-data.md") in the _Amazon EMR Management Guide_.

In addition, when you create an EMR Notebook, you can store your private Git-based
registry credentials using Secrets Manager. For more information, see [Add a Git-based Repository to
Amazon EMR](../../../emr/latest/ManagementGuide/emr-git-repo-add.md "../../../emr/latest/ManagementGuide/emr-git-repo-add.md") in the _Amazon EMR Management Guide_.

## How EMR Serverless uses Secrets Manager

EMR Serverless provides a serverless runtime environment to simplify the operation of
analytics applications so that you don’t have to configure, optimize, secure, or operate
clusters.

You can store your data in AWS Secrets Manager and then use the secret ID in your EMR Serverless
configurations. This way, you don't pass sensitive configuration data in plain text and
expose it to external APIs.

For more information, see [Secrets Manager for data protection
with EMR Serverless](../../../emr/latest/EMR-Serverless-UserGuide/secrets-manager.md "../../../emr/latest/EMR-Serverless-UserGuide/secrets-manager.md") in the _Amazon EMR Serverless User
Guide_.

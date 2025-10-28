# glue-spark-job-supported-version

Checks if an AWS Glue Spark job is running on the specified minimum supported AWS Glue version. The rule is NON_COMPLIANT if the AWS Glue Spark job is not running on the minimum supported AWS Glue version that you specify.

**Identifier:** GLUE_SPARK_JOB_SUPPORTED_VERSION

**Resource Types:** AWS::Glue::Job

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East (Bahrain), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

minimumSupportedGlueVersion
Type: String

String value you must specify of the minimum supported AWS Glue version for the rule to check.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

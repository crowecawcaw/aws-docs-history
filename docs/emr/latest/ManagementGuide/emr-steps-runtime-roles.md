# Runtime roles for Amazon EMR steps

A _runtime role_ is an AWS Identity and Access Management (IAM) role that you can specify when
you submit a job or query to an Amazon EMR cluster. The job or query that you submit to your
Amazon EMR cluster uses the runtime role to access AWS resources, such as objects in
Amazon S3. You can specify runtime roles with Amazon EMR for Spark and Hive jobs.

You can also specify runtime roles when you connect to Amazon EMR clusters in
Amazon SageMaker AI and when you attach an Amazon EMR Studio Workspace to an EMR cluster.
For more information, see [Connect to an Amazon EMR cluster from SageMaker AI
Studio](../../../sagemaker/latest/dg/connect-emr-clusters.md "../../../sagemaker/latest/dg/connect-emr-clusters.md") and [Run an EMR Studio Workspace with a runtime
role](emr-studio-runtime.md "emr-studio-runtime.md").

Previously, Amazon EMR clusters ran Amazon EMR jobs or queries with permissions based on the IAM
policy attached to the instance profile that you used to launch the cluster. This meant that
the policies had to contain the union of all the permissions for all jobs and queries that
ran on an Amazon EMR cluster. With runtime roles, you can now manage access control for each job
or query individually, instead of sharing the Amazon EMR instance profile of the cluster.

On Amazon EMR clusters with runtime roles, you can also apply AWS Lake Formation based access control to
Spark, Hive, and Presto jobs and queries against your data lakes. To learn more on how to
integrate with AWS Lake Formation, see [Integrate Amazon EMR with AWS Lake Formation](emr-lake-formation.md "emr-lake-formation.md").

###### Note

When you specify a runtime role for an Amazon EMR step, the jobs or queries that you submit
can only access AWS resources that the policies attached to the runtime role allow.
These jobs and queries can't access the Instance Metadata Service on the EC2 instances
of the cluster or use the EC2 instance profile of the cluster to access any AWS
resources.

## Prerequisites for launching an Amazon EMR

cluster with a runtime role

###### Topics

- [Step 1: Set up security configurations in
  Amazon EMR](#configure-security "#configure-security")
- [Step 2: Set up an EC2 instance profile for
  the Amazon EMR cluster](#configure-ec2-profile "#configure-ec2-profile")
- [Step 3: Set up a trust policy](#configure-trust-policy "#configure-trust-policy")

### Step 1: Set up security configurations in

Amazon EMR

Use the following JSON structure to create a security configuration on the AWS Command Line Interface (AWS CLI),
and set `EnableApplicationScopedIAMRole` to `true`. For more
information about security configurations, see [Use security configurations to set up Amazon EMR cluster security](emr-security-configurations.md "emr-security-configurations.md").

```
{
    "AuthorizationConfiguration":{
        "IAMConfiguration":{
            "EnableApplicationScopedIAMRole":true
        }
    }
}
```

We recommend that you always enable the in-transit encryption options in the
security configuration, so that data transferred over the internet is encrypted,
rather than in plain text. You can skip these options if you don’t want to connect
to Amazon EMR clusters with runtime roles from SageMaker Runtime Studio or EMR Studio. To configure data
encryption, see [Configure data encryption](emr-create-security-configuration.md#emr-security-configuration-encryption "emr-create-security-configuration.md#emr-security-configuration-encryption").

Alternatively, you can create a security configuration with custom settings with
the [AWS Management Console](https://console.aws.amazon.com/emr/home#/securityConfigs "https://console.aws.amazon.com/emr/home#/securityConfigs").

### Step 2: Set up an EC2 instance profile for

the Amazon EMR cluster

Amazon EMR clusters use the Amazon EC2 instance profile role to assume the runtime roles. To
use runtime roles with Amazon EMR steps, add the following policies to the IAM role
that you plan to use as the instance profile role. To add policies to an IAM role
or edit an existing inline or managed policy, see [Adding and
removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowRuntimeRoleUsage",
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole",
 "sts:TagSession"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/EMRRuntimeRole"
 ]
 }
 ]
}`

```

### Step 3: Set up a trust policy

For each IAM role that you plan to use as a runtime role, set the following
trust policy, replacing `EMR_EC2_DefaultRole` with your instance profile
role. To modify the trust policy of an IAM role, see [Modifying a
role trust policy](../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md "../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md").

```
{
    "Sid":"AllowAssumeRole",
    "Effect":"Allow",
    "Principal":{
        "AWS":"arn:aws:iam::`<AWS_ACCOUNT_ID>`:role/EMR_EC2_DefaultRole"
    },
    "Action":[
             "sts:AssumeRole",
             "sts:TagSession"
            ]
}
```

## Launch an Amazon EMR cluster with role-based

access control

After you set up your configurations, you can launch an Amazon EMR cluster with the
security configuration from [Step 1: Set up security configurations in
Amazon EMR](#configure-security "#configure-security"). To use runtime roles with Amazon EMR steps, use
release label `emr-6.7.0` or later, and select Hive, Spark, or both as your
cluster application. CloudWatchAgent is supported on Runtime Role Clusters for EMR 7.6 and above. To connect from SageMaker AI Studio, use release `emr-6.9.0` or
later, and select Livy, Spark, Hive, or Presto as your cluster application. For
instructions on how to launch your cluster, see [Specify a security configuration
for an Amazon EMR cluster](emr-specify-security-configuration.md "emr-specify-security-configuration.md").

### Submit Spark jobs using Amazon EMR steps

The following is an example of how to run the HdfsTest example included with
Apache Spark. This API call only succeeds if the provided Amazon EMR runtime role can
access the `S3_LOCATION`.

```
RUNTIME_ROLE_ARN=`<runtime-role-arn>`
S3_LOCATION=`<s3-path>`
REGION=`<aws-region>`
CLUSTER_ID=`<cluster-id>`

aws emr add-steps --cluster-id $CLUSTER_ID \
--steps '[{ "Name": "Spark Example", "ActionOnFailure": "CONTINUE", "Jar":"command-runner.jar","Args" : ["spark-example","HdfsTest", "$S3_LOCATION"] }]' \
--execution-role-arn $RUNTIME_ROLE_ARN \
--region $REGION
```

###### Note

We recommend that you turn off SSH access to the Amazon EMR cluster and only allow
the Amazon EMR `AddJobFlowSteps` API to access to the cluster.

### Submit Hive jobs using Amazon EMR steps

The following example uses Apache Hive with Amazon EMR steps to submit a job to run the
`QUERY_FILE.hql` file. This query only succeeds if the provided
runtime role can access the Amazon S3 path of the query file.

```
RUNTIME_ROLE_ARN=`<runtime-role-arn>`
REGION=`<aws-region>`
CLUSTER_ID=`<cluster-id>`

aws emr add-steps --cluster-id $CLUSTER_ID \
--steps '[{ "Name": "Run hive query using command-runner.jar - simple select","ActionOnFailure":"CONTINUE", "Jar": "command-runner.jar","Args" :["hive -
f","s3://`DOC_EXAMPLE_BUCKET`/QUERY_FILE.hql"] }]' \
--execution-role-arn $RUNTIME_ROLE_ARN \
--region $REGION
```

### Connect to Amazon EMR clusters with runtime roles from a SageMaker AI

Studio notebook

You can apply Amazon EMR runtime roles to queries that you run in Amazon EMR clusters from
SageMaker AI Studio. To do so, go through the following steps.

1. Follow the instructions in Launch Amazon SageMaker AI Studio to create
   an SageMaker AI Studio.
2. In the SageMaker AI Studio UI, start a notebook with supported kernels. For
   example, start a SparkMagic image with a PySpark kernel.
3. Choose an Amazon EMR cluster in SageMaker AI Studio, and then choose
   **Connect**.
4. Choose a runtime role, and then choose **Connect**.

This will create an SageMaker AI notebook cell with magic commands to connect to your
Amazon EMR cluster with the chosen Amazon EMR runtime role. In the notebook cell, you can
enter and run queries with runtime role and Lake Formation based access control. For a more
detailed example, see [Apply fine-grained data access controls with AWS Lake Formation and Amazon EMR from Amazon SageMaker AI
Studio](https://aws.amazon.com/blogs/machine-learning/apply-fine-grained-data-access-controls-with-aws-lake-formation-and-amazon-emr-from-amazon-sagemaker-studio "https://aws.amazon.com/blogs/machine-learning/apply-fine-grained-data-access-controls-with-aws-lake-formation-and-amazon-emr-from-amazon-sagemaker-studio").

### Control access to the Amazon EMR runtime role

You can control access to the runtime role with the condition key
`elasticmapreduce:ExecutionRoleArn`. The following policy allows an
IAM principal to use an IAM role named `Caller`, or any IAM role
that begins with the string `CallerTeamRole`, as the runtime role.

###### Important

You must create a condition based on the
`elasticmapreduce:ExecutionRoleArn` context key when you grant a
caller access to call the `AddJobFlowSteps` or
`GetClusterSessionCredentials` APIs, as the following example
shows.

```
{
    "Sid":"AddStepsWithSpecificExecRoleArn",
    "Effect":"Allow",
    "Action":[
        "elasticmapreduce:AddJobFlowSteps"
    ],
    "Resource":"*",
    "Condition":{
        "StringEquals":{
            "elasticmapreduce:ExecutionRoleArn":[
                "arn:aws:iam::`<AWS_ACCOUNT_ID>`:role/Caller"
            ]
        },
        "StringLike":{
            "elasticmapreduce:ExecutionRoleArn":[
                "arn:aws:iam::`<AWS_ACCOUNT_ID>`:role/CallerTeamRole*"
            ]
        }
    }
}
```

### Establish trust between runtime roles and Amazon EMR

clusters

Amazon EMR generates a unique identifier `ExternalId` for each security
configuration with activated runtime role authorization. This authorization allows
every user to own a set of runtime roles to use on clusters that belong to them. For
example, in an enterprise, every department can use their external ID to update the
trust policy on their own set of runtime roles.

You can find the external ID with the Amazon EMR
`DescribeSecurityConfiguration` API, as shown in the following
example.

```
aws emr describe-security-configuration --name 'iamconfig-with-lf'{"Name": "iamconfig-with-lf",
    "SecurityConfiguration":
        "{\"AuthorizationConfiguration\":{\"IAMConfiguration\":{\"EnableApplicationScopedIAMRole\
        ":true,\"ApplicationScopedIAMRoleConfiguration\":{\"PropagateSourceIdentity\":true,\"Exter
        nalId\":\"FXH5TSACFDWUCDSR3YQE2O7ETPUSM4OBCGLYWODSCUZDNZ4Y\"}},\"Lake
        FormationConfiguration\":{\"AuthorizedSessionTagValue\":\"Amazon EMR\"}}}",
    "CreationDateTime": "2022-06-03T12:52:35.308000-07:00"
}
```

For information about how to use an external ID, see [How to use
an external ID when granting access to your AWS resources to a third
party](../../../IAM/latest/UserGuide/id_roles_create_for-user_externalid.md "../../../IAM/latest/UserGuide/id_roles_create_for-user_externalid.md").

### Audit

To monitor and control actions that end users take with IAM roles, you can turn
on the source identity feature. To learn more about source identity, see [Monitor
and control actions taken with assumed roles](../../../IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.md "../../../IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.md").

To track source identity, set
`ApplicationScopedIAMRoleConfiguration/PropagateSourceIdentity` to
`true` in your security configuration, as follows.

```
{
    "AuthorizationConfiguration":{
        "IAMConfiguration":{
            "EnableApplicationScopedIAMRole":true,
            "ApplicationScopedIAMRoleConfiguration":{
                "PropagateSourceIdentity":true
            }
        }
    }
}
```

When you set `PropagateSourceIdentity` to `true`, Amazon EMR
applies the source identity from the calling credentials to a job or query session
that you create with the runtime role. If no source identity is present in the
calling credentials, Amazon EMR doesn't set the source identity.

To use this property, provide `sts:SetSourceIdentity` permissions to
your instance profile, as follows.

```
{ // PropagateSourceIdentity statement
    "Sid":"PropagateSourceIdentity",
    "Effect":"Allow",
    "Action":"sts:SetSourceIdentity",
    "Resource":[
        `<runtime-role-ARN>`
    ],
    "Condition":{
        "StringEquals":{
            "sts:SourceIdentity":`<source-identity>`
        }
    }
}
```

You must also add the `AllowSetSourceIdentity` statement to the trust
policy of your runtime roles.

```
{ // AllowSetSourceIdentity statement
    "Sid":"AllowSetSourceIdentity",
    "Effect":"Allow",
    "Principal":{
        "AWS":"arn:aws:iam::`<AWS_ACCOUNT_ID>`:role/EMR_EC2_DefaultRole"
    },
    "Action":[
        "sts:SetSourceIdentity",
        "sts:AssumeRole"
    ],
    "Condition":{
        "StringEquals":{
            "sts:SourceIdentity":`<source-identity>`
        }
    }
}
```

## Additional

considerations

###### Note

With Amazon EMR release `emr-6.9.0`, you might experience intermittent
failures when you connect to Amazon EMR clusters from SageMaker AI Studio. To address this issue,
you can install the patch with a bootstrap action when you launch the cluster. For
patch details, see [Amazon EMR release 6.9.0 known issues](../ReleaseGuide/emr-690-release.md#emr-690-relnotes "../ReleaseGuide/emr-690-release.md#emr-690-relnotes").

Additionally, consider the following when you configure runtime roles for
Amazon EMR.

- Amazon EMR supports runtime roles in all commercial AWS Regions.
- Amazon EMR steps support Apache Spark and Apache Hive jobs with runtime roles when
  you use release `emr-6.7.0` or later.
- SageMaker AI Studio supports Spark, Hive, and Presto queries with runtime roles when
  you use release `emr-6.9.0` or later.
- The following notebook kernels in SageMaker AI support runtime roles:
  - DataScience – Python 3 kernel
  - DataScience 2.0 – Python 3 kernel
  - DataScience 3.0 – Python 3 kernel
  - SparkAnalytics 1.0 – SparkMagic and PySpark kernels
  - SparkAnalytics 2.0 – SparkMagic and PySpark kernels
  - SparkMagic – PySpark kernel

- Amazon EMR supports steps that use `RunJobFlow` only at the time of
  cluster creation. This API doesn't support runtime roles.
- Amazon EMR doesn't support runtime roles on clusters that you configure to be
  highly-available.
- Starting with Amazon EMR release 7.5.0 and higher, runtime roles support viewing Spark and YARN User Interfaces (UIs), such as the following:
  Spark Live UI, Spark History Server, YARN NodeManager, and YARN ResourceManager. When you navigate to these UIs, there is a username and password prompt. Usernames and
  passwords can be generated through use of the EMR GetClusterSessionCredentials API. For more information regarding usage details for the
  API, see [GetClusterSessionCredentials](../APIReference/API_GetClusterSessionCredentials.md "../APIReference/API_GetClusterSessionCredentials.md").

An example of how to use the EMR GetClusterSessionCredentials API is the following:

```
aws emr  get-cluster-session-credentials --cluster-id `<cluster_ID>` --execution-role-arn `<IAM_role_arn>`
```

- You must escape your Bash command arguments when running commands with the
  `command-runner.jar` JAR file:

```
aws emr add-steps --cluster-id `<cluster-id>` --steps '[{"Name":"sample-step","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"","Args":["bash","-c","\"aws s3 ls\""],"Type":"CUSTOM_JAR"}]' --execution-role-arn `<IAM_ROLE_ARN>`
```

Additionally, you must escape your Bash command arguments when running commands with the script runner. The following is a sample that shows setting Spark properties, with included escape characters:

```
"\"--conf spark.sql.autoBroadcastJoinThreshold=-1\n--conf spark.cradle.RSv2Mode.enabled=true\""
```

- Runtime roles don't provide support for controlling access to on-cluster
  resources, such as HDFS and HMS.
- Runtime roles don't provide support for docker/containers.

# Using monitoring configuration to monitor the Spark Kubernetes operator and Spark jobs

Monitoring configuration lets you easily set up log archiving of your Spark application and operator logs to Amazon S3 or to Amazon CloudWatch. You can choose one or both. Doing
so adds a log agent sidecar to your spark operator pod, driver, and executor pods, and subsequently forwards these components' logs
to your configured sinks.

## Prerequisites

Before you configure monitoring, be sure to complete the following setup tasks:

1. (Optional) If you previously installed an older version of the Spark operator, delete
   the _SparkApplication/ScheduledSparkApplication_ CRD.

```
kubectl delete crd scheduledsparkapplications.sparkoperator.k8s.io
kubectl delete crd sparkapplications.sparkoperator.k8s.io
```

2. Create an operator/job execution role in IAM if you don’t have one already.
3. Run the following command to update the trust policy of the operator/job execution role you just created:

```
aws emr-containers update-role-trust-policy \
--cluster-name `cluster` \
--namespace `namespace` \
--role-name `iam_role_name_for_operator/job_execution_role`
```

4. Edit the IAM role trust policy of your operator/job execution
   role to the following:

```
{
    "Effect": "Allow",
    "Principal": {
        "Federated": "${OIDC-provider}"
    },
    "Action": "sts:AssumeRoleWithWebIdentity",
    "Condition": {
        "StringLike": {
            "OIDC_PROVIDER:sub": "system:serviceaccount:${Namespace}:emr-containers-sa-*"
        }
    }
}
```

5. Create a _monitoringConfiguration_ policy in IAM with following
   permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogStreams",
 "logs:CreateLogStream",
 "logs:CreateLogGroup",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:`log_group_name`",
 "arn:aws:logs:*:*:log-group:`log_group_name`:*"
 ],
 "Sid": "AllowLOGSDescribelogstreams"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowLOGSDescribeloggroups"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket_name`",
 "arn:aws:s3:::`bucket_name`/*"
 ],
 "Sid": "AllowS3Putobject"
 }
 ]
}`

```

6. Attach the above policy to your operator/job execution role.

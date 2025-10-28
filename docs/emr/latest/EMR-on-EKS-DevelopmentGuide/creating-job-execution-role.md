# Create a job execution role

To run workloads on Amazon EMR on EKS, you need to create an IAM role. We refer to this role as
the _job execution role_ in this documentation. For more information about
how to create IAM roles, see [Creating IAM roles](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md") in the IAM user
Guide.

You must also create an IAM policy that specifies the permissions for the job execution
role and then attach the IAM policy to the job execution role.

The following policy for the job execution role allows access to resource targets, Amazon S3,
and CloudWatch. These permissions are necessary to monitor jobs and access logs. To follow the same
process using the AWS CLI:

Create IAM Role for job execution:
Let’s create the role that EMR will use for job execution. This is the role, EMR jobs will assume when they run on EKS.

```
cat <<EoF > ~/environment/emr-trust-policy.json
 {
   "Version": "2012-10-17",
   "Statement": [
     {
       "Effect": "Allow",
       "Principal": {
         "Service": "elasticmapreduce.amazonaws.com"
       },
       "Action": "sts:AssumeRole"
     }
   ]
 }
 EoF

 aws iam create-role --role-name EMRContainers-JobExecutionRole --assume-role-policy-document file://~/environment/emr-trust-policy.json

```

Next, we need to attach the required IAM policies to the role so it can write logs to s3 and cloudwatch.

```
cat <<EoF > ~/environment/EMRContainers-JobExecutionRole.json
 {
     "Version": "2012-10-17",
     "Statement": [
         {
             "Effect": "Allow",
             "Action": [
                 "s3:PutObject",
                 "s3:GetObject",
                 "s3:ListBucket"
             ],
             "Resource": "arn:aws:s3:::amzn-s3-demo-bucket"
         },
         {
             "Effect": "Allow",
             "Action": [
                 "logs:PutLogEvents",
                 "logs:CreateLogStream",
               "logs:DescribeLogGroups",
                 "logs:DescribeLogStreams"
             ],
             "Resource": [
                 "arn:aws:logs:*:*:*"
             ]
         }
     ]
 }
 EoF
 aws iam put-role-policy --role-name EMRContainers-JobExecutionRole --policy-name EMR-Containers-Job-Execution --policy-document file://~/environment/EMRContainers-JobExecutionRole.json

```

###### Note

Access should be appropriately scoped, not granted to all S3 objects in the job
execution role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket"
 ],
 "Sid": "AllowS3Putobject"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:PutLogEvents",
 "logs:CreateLogStream",
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "arn:aws:logs:*:*:*"
 ],
 "Sid": "AllowLOGSPutlogevents"
 }
 ]
}`

```

For more information, see [Using job execution roles](iam-execution-role.md "iam-execution-role.md"), [Configure a job run to use S3 logs](emr-eks-jobs-CLI.md#emr-eks-jobs-s3 "emr-eks-jobs-CLI.md#emr-eks-jobs-s3"), and [Configure a job run to use CloudWatch Logs](emr-eks-jobs-CLI.md#emr-eks-jobs-cloudwatch "emr-eks-jobs-CLI.md#emr-eks-jobs-cloudwatch").

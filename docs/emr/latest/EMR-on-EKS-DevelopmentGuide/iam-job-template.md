# Controlling access to job templates

`StartJobRun` policy lets you enforce that a user or a role can only run jobs
using job templates that you specify and cannot run `StartJobRun` operations
without using the specified job templates. To achieve this, first ensure that you give the
user or role a read permission to the specified job templates as shown below.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "emr-containers:DescribeJobRun"
 ],
 "Resource": [
 "arn:aws:emr-containers:*:*:jobtemplate/`job_template_1_id`",
 "arn:aws:emr-containers:*:*:jobtemplate/`job_template_2_id`"
 ],
 "Sid": "AllowEMRCONTAINERSDescribejobtemplate"
 }
 ]
}`

```

To enforce that a user or role is able to invoke `StartJobRun` operation only
when using specified job templates, you can assign the following `StartJobRun`
policy permission to a given user or role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "emr-containers:StartJobRun"
 ],
 "Resource": [
 "arn:aws:emr-containers:*:*:/virtualclusters/`virtual_cluster_id`"
 ],
 "Condition": {
 "ArnLike": {
 "emr-containers:JobTemplateArn": [
 "arn:aws:emr-containers:*:*:jobtemplate/`job_template_1_id`",
 "arn:aws:emr-containers:*:*:jobtemplate/`job_template_2_id`"
 ]
 }
 },
 "Sid": "AllowEMRCONTAINERSStartjobrun"
 }
 ]
}`

```

If the job template specifies a job template parameter inside the execution role ARN
field, then the user will be able to provide a value for this parameter and thus be able to
invoke `StartJobRun` using an arbitrary execution role. To restrict the execution
roles the user can provide, see **Controlling access to the execution
role** in [Using job execution roles with Amazon EMR on EKS](iam-execution-role.md "iam-execution-role.md").

If no condition is specified in the above `StartJobRun` action policy for a
given user or a role, the user or the role will be allowed to invoke
`StartJobRun` action on the specified virtual cluster using an arbitrary job
template that they have read access to or using an arbitrary execution role.

# Resource: Restrict to POSIX user, Docker image, privilege level,

and role on job submission

The following policy allows a POSIX user to manage their own set of restricted job
definitions.

Use the first and second statements to register and deregister any job definition name whose
name is prefixed with `JobDefA_`.

The first statement also uses conditional context keys to restrict the POSIX user,
privileged status, and container image values within the `containerProperties` of a
job definition. For more information, see [RegisterJobDefinition](../APIReference/API_RegisterJobDefinition.md "../APIReference/API_RegisterJobDefinition.md") in
the _AWS Batch API Reference_. In this example, job definitions can only be
registered when the POSIX user is set to `nobody`. The privileged flag is
set to `false`. Last, the image is set to `myImage` in an Amazon ECR repository.

###### Important

Docker resolves the `user` parameter to that user `uid` from within
the container image. In most cases, this is found in the `/etc/passwd` file
within the container image. This name resolution can be avoided by using direct
`uid` values in both the job definition and any associated IAM policies. Both the
AWS Batch API operations and the `batch:User` IAM conditional keys support numeric
values.

Use the third statement to restrict to only a specific role to a job definition.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "batch:RegisterJobDefinition"
 ],
 "Resource": [
 "arn:aws:batch:`us-east-2`:`999999999999`:job-definition/JobDefA_*"
 ],
 "Condition": {
 "StringEquals": {
 "batch:User": [
 "nobody"
 ],
 "batch:Image": [
 "`999999999999`.dkr.ecr.`us-east-2`.amazonaws.com/myImage"
 ]
 },
 "Bool": {
 "batch:Privileged": "false"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "batch:DeregisterJobDefinition"
 ],
 "Resource": [
 "arn:aws:batch:`us-east-2`:`999999999999`:job-definition/JobDefA_*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::`999999999999`:role/MyBatchJobRole"
 ]
 }
 ]
}`

```

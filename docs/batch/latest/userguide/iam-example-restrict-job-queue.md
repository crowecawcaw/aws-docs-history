# Resource: Restrict to a job queue

Use the following policy to submit jobs to a specific job queue that's named **queue1** with any job definition name.

###### Important

When scoping resource-level access for job submission, you must provide both job queue and job definition
resource types.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "batch:SubmitJob"
 ],
 "Resource": [
 "arn:aws:batch:`us-east-2`:`888888888888`:job-definition/*",
 "arn:aws:batch:`us-east-2`:`888888888888`:job-queue/queue1"
 ]
 }
 ]
}`

```

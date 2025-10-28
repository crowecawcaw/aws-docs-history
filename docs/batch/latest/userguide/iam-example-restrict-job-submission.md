# Resource: Restrict to job definition prefix on job

submission

Use the following policy to submit jobs to any job queue with any job definition name that
starts with `JobDefA`.

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
 "arn:aws:batch:`us-east-2`:`111122223333`:job-definition/JobDefA_*",
 "arn:aws:batch:`us-east-2`:`111122223333`:job-queue/*"
 ]
 }
 ]
}`

```

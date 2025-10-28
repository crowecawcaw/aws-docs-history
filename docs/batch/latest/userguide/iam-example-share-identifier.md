# Resource: Use the `batch:ShareIdentifier` condition key

Use the following policy to submit jobs that use the `jobDefA` job
definition to the `jobqueue1` job queue with the `lowCpu` share
identifier.

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
 "arn:aws:batch:`us-east-2`:`555555555555`:job-definition/JobDefA",
 "arn:aws:batch:`us-east-2`:`555555555555`:job-queue/jobqueue1"
 ],
 "Condition": {
 "StringEquals": {
 "batch:ShareIdentifier": [
 "lowCpu"
 ]
 }
 }
 }
 ]
}`

```

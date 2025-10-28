# Tutorial: Map a running job to a pod and a node

The `podProperties` of a running job have `podName` and `nodeName` parameters
set for the current job attempt. Use the [DescribeJobs](../APIReference/API_DescribeJobs.md "../APIReference/API_DescribeJobs.md") API operation to view these
parameters.

The following is example output.

```
`$` `aws batch describe-jobs --job 2d044787-c663-4ce6-a6fe-f2baf7e51b04`
`{
 "jobs": [
 {
 "status": "RUNNING",
 "jobArn": "arn:aws:batch:us-east-1:123456789012:job/2d044787-c663-4ce6-a6fe-f2baf7e51b04",
 "jobDefinition": "arn:aws:batch:us-east-1:123456789012:job-definition/MyJobOnEks_SleepWithRequestsOnly:1",
 "jobQueue": "arn:aws:batch:us-east-1:123456789012:job-queue/My-Eks-JQ1",
 "jobId": "2d044787-c663-4ce6-a6fe-f2baf7e51b04",
 "eksProperties": {
 "podProperties": {
 "nodeName": "ip-192-168-55-175.ec2.internal",
 "containers": [
 {
 "image": "public.ecr.aws/amazonlinux/amazonlinux:2",
 "resources": {
 "requests": {
 "cpu": "1",
 "memory": "1024Mi"
 }
 }
 }
 ],
 "podName": "aws-batch.b0aca953-ba8f-3791-83e2-ed13af39428c"
 }
 }
 }
 ]
}`
```

For a job with retries enabled, the `podName` and `nodeName` of every completed attempt is
in the `eksAttempts` list parameter of the [DescribeJobs](../APIReference/API_DescribeJobs.md "../APIReference/API_DescribeJobs.md") API operation. The `podName`
and `nodeName` of the current running attempt are in the `podProperties` object.

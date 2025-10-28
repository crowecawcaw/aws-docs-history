# Run a GPU job in your Amazon EKS cluster

The GPU resource is non-compressible. AWS Batch creates a pod spec for GPU jobs where the value of **request** equals the value of **limits**. This is a Kubernetes
requirement.

To submit a GPU job, run the following commands.

```
`$` `aws batch submit-job --job-queue My-Eks-GPU-JQ1 --job-definition MyGPUJobOnEks_Smi --job-name My-Eks-GPU-Job`

`# locate information that can help debug or find logs (if using Amazon CloudWatch Logs with Fluent Bit)`
`$` `aws batch describe-jobs --job `<job-id>` | jq '.jobs[].eksProperties.podProperties | {podName, nodeName}'`
`{
 "podName": "aws-batch.f3d697c4-3bb5-3955-aa6c-977fcf1cb0ca",
 "nodeName": "ip-192-168-59-101.ec2.internal"
}`
```

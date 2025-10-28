# Tutorial: Map a running pod back to its job

A pod has labels that indicate the `jobId` and `uuid` of the compute environment that it
belongs to. AWS Batch injects environment variables so the job’s runtime can reference job information. For more
information, see [AWS Batch job environment variables](job_env_vars.md "job_env_vars.md"). You can view this information by
running the following command. The output is as follows.

```
`$` `kubectl describe pod aws-batch.`14638eb9-d218-372d-ba5c-1c9ab9c7f2a1` -n `my-aws-batch-namespace``
`Name: aws-batch.14638eb9-d218-372d-ba5c-1c9ab9c7f2a1
Namespace: my-aws-batch-namespace
Priority: 0
Node: ip-192-168-45-88.ec2.internal/192.168.45.88
Start Time: Wed, 26 Oct 2022 00:30:48 +0000
Labels: batch.amazonaws.com/compute-environment-uuid=5c19160b-d450-31c9-8454-86cf5b30548f
 batch.amazonaws.com/job-id=f980f2cf-6309-4c77-a2b2-d83fbba0e9f0
 batch.amazonaws.com/node-uid=a4be5c1d-9881-4524-b967-587789094647
...
Status: Running
IP: 192.168.45.88
IPs:
 IP: 192.168.45.88
Containers:
 default:
 Image: public.ecr.aws/amazonlinux/amazonlinux:2
 ...
 Environment:
 AWS_BATCH_JOB_KUBERNETES_NODE_UID: a4be5c1d-9881-4524-b967-587789094647
 AWS_BATCH_JOB_ID: f980f2cf-6309-4c77-a2b2-d83fbba0e9f0
 AWS_BATCH_JQ_NAME: My-Eks-JQ1
 AWS_BATCH_JOB_ATTEMPT: 1
 AWS_BATCH_CE_NAME: My-Eks-CE1

...`
```

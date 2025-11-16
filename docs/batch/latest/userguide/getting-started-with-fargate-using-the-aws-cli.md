# Getting started with AWS Batch and Fargate using the AWS CLI

This tutorial demonstrates how to set up AWS Batch with AWS Fargate orchestration and run a simple "Hello World" job using the AWS Command Line Interface (AWS CLI). You'll learn how to create compute environments, job queues, job definitions, and submit jobs to AWS Batch.

###### Topics

- [Prerequisites](#prerequisites "#prerequisites")
- [Create an IAM execution role](#tutorial-fargate-using-the-aws-cli-create-an-iam-execution-role "#tutorial-fargate-using-the-aws-cli-create-an-iam-execution-role")
- [Create a compute environment](#create-a-compute-environment "#create-a-compute-environment")
- [Create a job queue](#cli-create-a-job-queue "#cli-create-a-job-queue")
- [Create a job definition](#cli-create-a-job-definition "#cli-create-a-job-definition")
- [Submit and monitor a job](#cli-submit-and-monitor-a-job "#cli-submit-and-monitor-a-job")
- [View job output](#cli-view-job-output "#cli-view-job-output")
- [Clean up resources](#cli-clean-up-resources "#cli-clean-up-resources")
- [Going to production](#cli-going-to-production "#cli-going-to-production")
- [Next steps](#cli-next-steps "#cli-next-steps")

## Prerequisites

Before you begin this tutorial, make sure you have the following.

1. The AWS CLI. If you need to install it, follow the [AWS CLI installation guide](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"). You can also [use AWS CloudShell](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md"), which includes the AWS CLI.
2. Configured your AWS CLI with appropriate credentials. Run `aws configure` if you haven't set up your credentials yet.
3. Basic familiarity with command line interfaces and containerization concepts.
4. [How AWS Batch works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md") to create and manage AWS Batch resources, IAM roles, and VPC resources in your AWS account.
5. A subnet ID and security group ID from a VPC in your AWS account. If you don't have a VPC, you can [create one](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md"). For more information about using the AWS CLI to retrieve these resource IDs, see [describe-subnets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-subnets.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-subnets.html") and [describe-security-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-groups.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-groups.html") in the _AWS CLI Command Reference_.

**Time Required**: Approximately 15-20 minutes to complete this tutorial.

**Cost**: This tutorial uses Fargate compute resources. The estimated cost for completing this tutorial is less than $0.01 USD, assuming you follow the cleanup instructions to delete resources immediately after completion. Fargate pricing is based on vCPU and memory resources consumed, charged per second with a 1-minute minimum. For current pricing information, see [AWS Fargate pricing](https://aws.amazon.com/fargate/pricing/ "https://aws.amazon.com/fargate/pricing/").

## Create an IAM execution role

AWS Batch requires an execution role that allows Amazon Elastic Container Service (Amazon ECS) agents to make AWS API calls on your behalf. This role is necessary for Fargate tasks to pull container images and write logs to Amazon CloudWatch.

**Create a trust policy document**

First, create a trust policy that allows the Amazon ECS tasks service to assume the role.

```
cat > batch-execution-role-trust-policy.json << EOF
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "ecs-tasks.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`
EOF
```

**Create the execution role**

The following command creates an IAM role named `BatchEcsTaskExecutionRoleTutorial` using the trust policy you just created.

```
aws iam create-role \
    --role-name BatchEcsTaskExecutionRoleTutorial \
    --assume-role-policy-document file://batch-execution-role-trust-policy.json
```

**Attach the required policy**

Attach the AWS managed policy that provides the necessary permissions for Amazon ECS task execution.

```
aws iam attach-role-policy \
    --role-name BatchEcsTaskExecutionRoleTutorial \
    --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy
```

The role is now ready to be used by AWS Batch for Fargate task execution.

## Create a compute environment

A compute environment defines the compute resources where your batch jobs will run. For this tutorial, you'll create a managed Fargate compute environment that automatically provisions and scales resources based on job requirements.

**Create the compute environment**

The following command creates a Fargate compute environment. Replace the example subnet and security group IDs with your own per the [Prerequisites](#prerequisites "#prerequisites").

```
aws batch create-compute-environment \
    --compute-environment-name my-fargate-compute-env \
    --type MANAGED \
    --state ENABLED \
    --compute-resources type=FARGATE,maxvCpus=128,subnets=`subnet-a123456b`,securityGroupIds=`sg-a12b3456`
```

The following shows how the output looks when the command runs successfully.

```
{
    "computeEnvironmentName": "my-fargate-compute-env",
    "computeEnvironmentArn": "arn:aws:batch:us-west-2:123456789012:compute-environment/my-fargate-compute-env"
}
```

**Wait for the compute environment to be ready**

Check the status of your compute environment to ensure it's ready before proceeding.

```
aws batch describe-compute-environments \
    --compute-environments my-fargate-compute-env \
    --query 'computeEnvironments[0].status'

```

```
"VALID"
```

When the status shows `VALID`, your compute environment is ready to accept jobs.

## Create a job queue

A job queue stores submitted jobs until the AWS Batch scheduler runs them on resources in your compute environment. Jobs are processed in priority order within the queue.

**Create the job queue**

The following command creates a job queue with priority 900 that uses your Fargate compute environment.

```
aws batch create-job-queue \
    --job-queue-name my-fargate-job-queue \
    --state ENABLED \
    --priority 900 \
    --compute-environment-order order=1,computeEnvironment=my-fargate-compute-env
```

The following shows how the output looks when the command runs successfully.

```
{
    "jobQueueName": "my-fargate-job-queue",
    "jobQueueArn": "arn:aws:batch:us-west-2:123456789012:job-queue/my-fargate-job-queue"
}
```

**Verify the job queue is ready**

Check that your job queue is in the `ENABLED` state and ready to accept jobs.

```
aws batch describe-job-queues \
    --job-queues my-fargate-job-queue \
    --query 'jobQueues[0].state' "ENABLED"
```

## Create a job definition

A job definition specifies how jobs are to be run, including the Docker image to use, resource requirements, and other parameters. For Fargate, you'll use resource requirements instead of traditional vCPU and memory parameters.

**Create the job definition**

The following command creates a job definition that runs a simple "hello world" command using the busybox container image. Replace `123456789012` with your actual AWS account ID and replace the example AWS Region with your own.

```
aws batch register-job-definition \
    --job-definition-name my-fargate-job-def \
    --type container \
    --platform-capabilities FARGATE \
    --container-properties '{
        "image": "busybox",
        "resourceRequirements": [
            {"type": "VCPU", "value": "0.25"},
            {"type": "MEMORY", "value": "512"}
        ],
        "command": ["echo", "hello world"],
        "networkConfiguration": {
            "assignPublicIp": "ENABLED"
        },
        "executionRoleArn": "arn:aws:iam::`123456789012`:role/BatchEcsTaskExecutionRoleTutorial"
    },
{
    "jobDefinitionName": "my-fargate-job-def",
    "jobDefinitionArn": "arn:aws:batch:`us-west-2`:`123456789012`:job-definition/my-fargate-job-def:1",
    "revision": 1
}'
```

The job definition specifies 0.25 vCPU and 512 MB of memory, which are the minimum resources for a Fargate task. The `assignPublicIp` setting is enabled so the container can pull the busybox image from Docker Hub.

## Submit and monitor a job

Now that you have all the necessary components, you can submit a job to your queue and monitor its progress.

**Submit a job**

The following command submits a job to your queue using the job definition you created.

```
aws batch submit-job \
    --job-name my-hello-world-job \
    --job-queue my-fargate-job-queue \
    --job-definition my-fargate-job-def
```

The following shows how the output looks when the command runs successfully.

```
{
    "jobArn": "arn:aws:batch:us-west-2:123456789012:job/my-hello-world-job",
    "jobName": "my-hello-world-job",
    "jobId": "1509xmpl-4224-4da6-9ba9-1d1acc96431a"
}
```

Make note of the `jobId` returned in the response, as you'll use it to monitor the job's progress.

**Monitor job status**

Use the job ID to check the status of your job. The job will progress through several states: `SUBMITTED`, `PENDING`, `RUNNABLE`, `STARTING`, `RUNNING`, and finally `SUCCEEDED` or `FAILED`.

```
aws batch describe-jobs --jobs 1509xmpl-4224-4da6-9ba9-1d1acc96431a
```

The following shows how the output looks when the command runs successfully.

```
{
    "jobs": [
        {
            "jobArn": "arn:aws:batch:`us-west-2`:`123456789012`:job/my-hello-world-job",
            "jobName": "my-hello-world-job",
            "jobId": "1509xmpl-4224-4da6-9ba9-1d1acc96431a",
            "jobQueue": "arn:aws:batch:`us-west-2`:`123456789012`:job-queue/my-fargate-job-queue",
            "status": "SUCCEEDED",
            "createdAt": 1705161908000,
            "jobDefinition": "arn:aws:batch:`us-west-2`:`123456789012`:job-definition/my-fargate-job-def:1"
        }
    ]
}
```

When the status shows `SUCCEEDED`, your job has completed successfully.

## View job output

After your job completes, you can view its output in Amazon CloudWatch Logs.

**Get the log stream name**

First, retrieve the log stream name from the job details. Replace the example job ID with your own.

```
aws batch describe-jobs --jobs `1509xmpl-4224-4da6-9ba9-1d1acc96431a` \
    --query 'jobs[0].attempts[0].containers[0].logStreamName' \
    --output text
```

```
my-fargate-job-def/default/1509xmpl-4224-4da6-9ba9-1d1acc96431a
```

**View the job logs**

Use the log stream name to retrieve the job's output from CloudWatch Logs.

```
aws logs get-log-events \
    --log-group-name /aws/batch/job \
    --log-stream-name my-fargate-job-def/default/`1509xmpl-4224-4da6-9ba9-1d1acc96431a` \
    --query 'events[*].message' \
    --output text
```

The output shows "hello world", confirming that your job ran successfully.

## Clean up resources

To avoid ongoing charges, clean up the resources you created in this tutorial. You must delete resources in the correct order due to dependencies.

**Disable and delete the job queue**

First, disable the job queue, then delete it.

```
aws batch update-job-queue \
    --job-queue my-fargate-job-queue \
    --state DISABLED
```

```
aws batch delete-job-queue \
    --job-queue my-fargate-job-queue
```

**Disable and delete the compute environment**

After the job queue is deleted, disable and delete the compute environment.

```
aws batch update-compute-environment \
    --compute-environment my-fargate-compute-env \
    --state DISABLED
```

```
aws batch delete-compute-environment \
    --compute-environment my-fargate-compute-env
```

**Clean up the IAM role**

Remove the policy attachment and delete the IAM role.

```
aws iam detach-role-policy \
    --role-name BatchEcsTaskExecutionRoleTutorial \
    --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy

```

```
aws iam delete-role \
    --role-name BatchEcsTaskExecutionRoleTutorial
```

**Remove temporary files**

Delete the trust policy file you created.

```
rm batch-execution-role-trust-policy.json
```

All resources have been successfully cleaned up.

## Going to production

This tutorial is designed to help you understand how AWS Batch works with Fargate. For production deployments, consider the following additional requirements:

###### Security considerations:

- Create dedicated security groups with minimal required access instead of using default security groups
- Use private subnets with NAT Gateway instead of public IP assignment for containers
- Store container images in Amazon ECR instead of using public repositories
- Implement VPC endpoints for AWS service communication to avoid internet traffic

###### Architecture considerations:

- Deploy across multiple Availability Zones for high availability
- Implement job retry strategies and dead letter queues for error handling
- Use multiple job queues with different priorities for workload management
- Configure auto scaling policies based on queue depth and resource utilization
- Implement monitoring and alerting for job failures and resource utilization

###### Operational considerations:

- Set up CloudWatch dashboards and alarms for monitoring
- Implement proper logging and audit trails
- Use AWS CloudFormation or the AWS CDK for infrastructure as code
- Establish backup and disaster recovery procedures

For comprehensive guidance on production-ready architectures, see the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/") and [AWS Security Best Practices](https://aws.amazon.com/architecture/security-identity-compliance/ "https://aws.amazon.com/architecture/security-identity-compliance/").

## Next steps

Now that you've completed this tutorial, you can explore more advanced AWS Batch features:

- [Job queues](job_queues.md "job_queues.md") – Learn about job queue scheduling and priority management
- [Job definitions](job_definitions.md "job_definitions.md") – Explore advanced job definition configurations including environment variables, volumes, and retry strategies
- [Compute environments for AWS Batch](compute_environments.md "compute_environments.md") – Understand different compute environment types and scaling options
- [Multi-node parallel jobs](multi-node-parallel-jobs.md "multi-node-parallel-jobs.md") – Run jobs that span multiple compute nodes
- [Array jobs](array_jobs.md "array_jobs.md") – Submit large numbers of similar jobs efficiently
- [Best practices for AWS Batch](best-practices.md "best-practices.md") – Learn optimization techniques for production workloads

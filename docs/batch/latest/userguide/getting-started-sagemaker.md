

# Getting started with AWS Batch on SageMaker AI
<a name="getting-started-sagemaker"></a>

AWS Batch service jobs enable you to submit SageMaker Training jobs through AWS Batch job queues with scheduling, prioritization, and queuing capabilities. This tutorial demonstrates how to set up and run a simple SageMaker Training job using AWS Batch service jobs.

**Contents**
+ [Overview](#getting-started-sagemaker-context)
+ [Prerequisites](#getting-started-sagemaker-prerequisites)
+ [Step 1: Create a SageMaker AI execution role](#getting-started-sagemaker-step-1)
+ [Step 2: Create your service environment](#getting-started-sagemaker-step-2)
+ [Step 3: Create your SageMaker job queue](#getting-started-sagemaker-step-3)
+ [Step 4: Create and submit a training job](#getting-started-sagemaker-step-4)
+ [Step 5: Monitor job status](#getting-started-sagemaker-step-5)
+ [Step 6: View job output](#getting-started-sagemaker-step-6)
+ [Step 7: Clean up your tutorial resources](#getting-started-sagemaker-step-7)
+ [Additional resources](#getting-started-sagemaker-additional-resources)

## Overview
<a name="getting-started-sagemaker-context"></a>

This tutorial demonstrates how to setup AWS Batch service jobs for SageMaker Training jobs using the AWS CLI.

**Intended Audience**  
This tutorial is designed for data scientists and developers responsible for setting up and running machine learning training jobs at scale.

**Features Used**  
This tutorial shows you how to use the AWS CLI to:  
+ Create a service environment for SageMaker Training jobs
+ Create a SageMaker Training job queue
+ Submit service jobs using the `SubmitServiceJob` API
+ Monitor job status and view outputs
+ Access CloudWatch logs for training jobs

**Time Required**  
It should take about 15 minutes to complete this tutorial.

**Regional Restrictions**  
This tutorial can be completed in any AWS Region where both AWS Batch and SageMaker AI are available.

**Resource Usage Costs**  
There's no charge for creating an AWS account. However, by implementing this solution, you might incur costs for the following resources:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/batch/latest/userguide/getting-started-sagemaker.html)

## Prerequisites
<a name="getting-started-sagemaker-prerequisites"></a>

Before starting this tutorial, you must install and configure the following tools and resources that you need to create and manage both AWS Batch and SageMaker AI resources.
+ **AWS CLI** – A command line tool for working with AWS services, including AWS Batch and SageMaker AI. This guide requires that you use version 2.8.6 or later. For more information, see [Installing, updating, and uninstalling the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) in the *AWS Command Line Interface User Guide*. After installing the AWS CLI, we recommend that you also configure it. For more information, see [Quick configuration with `aws configure`](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config) in the *AWS Command Line Interface User Guide*.

## Step 1: Create a SageMaker AI execution role
<a name="getting-started-sagemaker-step-1"></a>

SageMaker AI uses execution roles to perform operations on your behalf using other AWS services. You must create an execution role and grant SageMaker AI permissions to use the services and resources needed for training jobs. Use the `AmazonSageMakerFullAccess` managed policy as it includes permissions for Amazon S3. 

**Note**  
Use the following directions to create the SageMaker AI execution role for this tutorial.  
Before you create an execution role for your production environment we recommend you review, [How to use SageMaker AI execution roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html) in the *[SageMaker AI Developer guide](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)*.

1. 

**Create the IAM role**

   Create a JSON file named `sagemaker-trust-policy.json` with the following trust policy:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "sagemaker.amazonaws.com"
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

------

   Create the IAM role using the trust policy:

   ```
   aws iam create-role \
       --role-name SageMakerExecutionRole \
       --assume-role-policy-document file://sagemaker-trust-policy.json \
       --description "Execution role for SageMaker training jobs"
   ```

1. 

**Attach managed policies**

   Attach the required managed policies to the role:

   ```
   aws iam attach-role-policy \
       --role-name SageMakerExecutionRole \
       --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerFullAccess
   ```

   ```
   aws iam attach-role-policy \
       --role-name SageMakerExecutionRole \
       --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
   ```

1. 

**Note the role ARN**

   Get the role ARN, which you'll need in later steps:

   ```
   aws iam get-role --role-name SageMakerExecutionRole --query 'Role.Arn' --output text
   ```

   Save this ARN as you'll use it when creating your training job payload.

## Step 2: Create your service environment
<a name="getting-started-sagemaker-step-2"></a>

A service environment defines the capacity constraints for SageMaker Training jobs. The service environment encapsulates the maximum number of training instances that can run concurrently.

**Important**  
When you create your first service environment for SageMaker Training, AWS Batch automatically creates a service-linked role called `AWSServiceRoleForAWSBatchWithSagemaker` in your account. This role allows AWS Batch to queue and manage SageMaker Training jobs on your behalf. For more information about this service-linked role and its permissions, see [Using roles for AWS Batch with SageMaker AI](using-service-linked-roles-batch-sagemaker.md).

Create a service environment that can handle up to 5 instances:

```
aws batch create-service-environment \
    --service-environment-name {{TutorialServiceEnvironment}} \
    --service-environment-type SAGEMAKER_TRAINING \
    --capacity-limits capacityUnit=NUM_INSTANCES,maxCapacity=5
```

Output:

```
{
    "serviceEnvironmentName": "{{TutorialServiceEnvironment}}",
    "serviceEnvironmentArn": "arn:aws:batch:{{your-region}}:{{your-account-id}}:service-environment/{{TutorialServiceEnvironment}}"
}
```

Verify that your service environment was created successfully:

```
aws batch describe-service-environments --service-environments {{TutorialServiceEnvironment}}
```

Output:

```
{
    "serviceEnvironments": [
        {
            "serviceEnvironmentName": "{{TutorialServiceEnvironment}}",
            "serviceEnvironmentArn": "arn:aws:batch:{{your-region}}:{{your-account-id}}:service-environment/{{TutorialServiceEnvironment}}",
            "serviceEnvironmentType": "SAGEMAKER_TRAINING",
            "state": "ENABLED",
            "status": "VALID",
            "capacityLimits": [
                {
                    "maxCapacity": 5,
                    "capacityUnit": "NUM_INSTANCES"
                }
            ],
            "tags": {}
        }
    ]
}
```

For more information about service environments, see [Service environments for AWS Batch](service-environments.md).

## Step 3: Create your SageMaker job queue
<a name="getting-started-sagemaker-step-3"></a>

A SageMaker job queue manages the scheduling and execution of service jobs. Jobs submitted to this queue will be dispatched to your service environment based on available capacity.

Create a SageMaker Training job queue:

```
aws batch create-job-queue \
    --job-queue-name {{my-sm-training-fifo-jq}} \
    --job-queue-type SAGEMAKER_TRAINING \
    --priority 1 \
    --service-environment-order order=1,serviceEnvironment={{TutorialServiceEnvironment}}
```

Output:

```
{
    "jobQueueName": "{{my-sm-training-fifo-jq}}",
    "jobQueueArn": "arn:aws:batch:{{your-region}}:{{your-account-id}}:job-queue/{{my-sm-training-fifo-jq}}"
}
```

Verify that your job queue was created successfully:

```
aws batch describe-job-queues --job-queues {{my-sm-training-fifo-jq}}
```

Output:

```
{
    "jobQueues": [
        {
            "jobQueueName": "{{my-sm-training-fifo-jq}}",
            "jobQueueArn": "arn:aws:batch:{{your-region}}:{{your-account-id}}:job-queue/{{my-sm-training-fifo-jq}}",
            "state": "ENABLED",
            "status": "VALID",
            "statusReason": "JobQueue Healthy",
            "priority": 1,
            "computeEnvironmentOrder": [],
            "serviceEnvironmentOrder": [
                {
                    "order": 1,
                    "serviceEnvironment": "arn:aws:batch:{{your-region}}:{{your-account-id}}:service-environment/{{TutorialServiceEnvironment}}"
                }
            ],
            "jobQueueType": "SAGEMAKER_TRAINING",
            "tags": {}
        }
    ]
}
```

For more information about SageMaker job queues, see [Create a SageMaker Training job queue in AWS Batch](create-sagemaker-job-queue.md).

## Step 4: Create and submit a training job
<a name="getting-started-sagemaker-step-4"></a>

Now you'll create a simple training job and submit it to your job queue. This example uses a basic "hello world" training job that demonstrates the service job functionality.

Create a file named `{{my_training_job.json}}` with the following content. Replace {{your-account-id}} with your AWS account ID:

**Note**  
`S3OutputPath` is required for creating the SageMaker Training job but the results of this tutorial are not stored in the Amazon S3 bucket and you can use the path in the following JSON. In your production environment you will need a valid Amazon S3 bucket to store output there if you choose to.

```
{
    "TrainingJobName": "{{my-simple-training-job}}",
    "RoleArn": "arn:aws:iam::{{your-account-id}}:role/SageMakerExecutionRole",
    "AlgorithmSpecification": {
        "TrainingInputMode": "File",
        "TrainingImage": "763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-training:2.0.0-cpu-py310",
        "ContainerEntrypoint": [
            "echo",
            "hello world"
        ]
    },
    "ResourceConfig": {
        "InstanceType": "ml.c5.xlarge",
        "InstanceCount": 1,
        "VolumeSizeInGB": 1
    },
    "OutputDataConfig": {
        "S3OutputPath": "s3://your-s3-bucket/output"
    },
    "StoppingCondition": {
        "MaxRuntimeInSeconds": 30
    }
}
```

Submit the training job using the [SubmitServiceJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitServiceJob.html) API:

```
aws batch submit-service-job \
    --job-queue {{my-sm-training-fifo-jq}} \
    --job-name {{my-batch-sm-job}} \
    --service-job-type SAGEMAKER_TRAINING \
    --retry-strategy attempts=1 \
    --timeout-config attemptDurationSeconds=60 \
    --service-request-payload file://{{my_training_job.json}}
```

Output:

```
{
    "jobArn": "arn:aws:batch:{{your-region}}:{{your-account-id}}:service-job/{{your-job-id}}",
    "jobName": "{{my-batch-sm-job}}",
    "jobId": "{{your-job-id}}"
}
```

For more information about service job payloads, see [Service job payloads in AWS Batch](service-job-payload.md). For more information about submitting service jobs, see [Submit a service job in AWS Batch](service-job-submit.md).

## Step 5: Monitor job status
<a name="getting-started-sagemaker-step-5"></a>

You can monitor your training jobs using the following AWS Batch APIs: [DescribeServiceJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeServiceJob.html), [ListServiceJobs](https://docs.aws.amazon.com/batch/latest/APIReference/API_ListServiceJobs.html), and [GetJobQueueSnapshot](https://docs.aws.amazon.com/batch/latest/APIReference/API_GetJobQueueSnapshot.html). This section shows different ways to check job status and queue information.

View running jobs in your queue:

```
aws batch list-service-jobs \
    --job-queue {{my-sm-training-fifo-jq}} --job-status RUNNING
```

Output:

```
{
    "jobSummaryList": [
        {
            "latestAttempt": {
                "serviceResourceId": {
                    "name": "TrainingJobArn",
                    "value": "arn:aws:sagemaker:{{your-region}}:{{your-account-id}}:training-job/AWSBatch{{<my-simple-training-job>}}{{<your-attempt-id>}}"
                }
            },
            "createdAt": 1753718760,
            "jobArn": "arn:aws:batch:{{your-region}}:{{your-account-id}}:service-job/{{your-job-id}}",
            "jobId": "{{your-job-id}}",
            "jobName": "{{my-batch-sm-job}}",
            "serviceJobType": "SAGEMAKER_TRAINING",
            "status": "RUNNING",
            "startedAt": 1753718820
        }
    ]
}
```

View jobs that are in the `RUNNABLE` state:

```
aws batch list-service-jobs \
    --job-queue {{my-sm-training-fifo-jq}} --job-status RUNNABLE
```

Get a snapshot of upcoming jobs in your queue:

```
aws batch get-job-queue-snapshot --job-queue {{my-sm-training-fifo-jq}}
```

Output:

```
{
    "frontOfQueue": {
        "jobs": [
            {
                "jobArn": "arn:aws:batch:{{your-region}}:{{your-account-id}}:service-job/{{your-job-id}}",
                "earliestTimeAtPosition": 1753718880
            },
            {
                "jobArn": "arn:aws:batch:{{your-region}}:{{your-account-id}}:service-job/{{your-job-id-2}}",
                "earliestTimeAtPosition": 1753718940
            }
        ],
        "lastUpdatedAt": 1753718970
    }
}
```

Search for jobs by name:

```
aws batch list-service-jobs \
    --job-queue {{my-sm-training-fifo-jq}} \
    --filters name=JOB_NAME,values="{{my-batch-sm-job}}"
```

Output:

```
{
    "jobSummaryList": [
        {
            "latestAttempt": {
                "serviceResourceId": {
                    "name": "TrainingJobArn",
                    "value": "arn:aws:sagemaker:{{your-region}}:{{your-account-id}}:training-job/AWSBatch{{<my-simple-training-job>}}{{<your-attempt-id>}}"
                }
            },
            "createdAt": 1753718760,
            "jobArn": "arn:aws:batch:{{your-region}}:{{your-account-id}}:service-job/{{your-job-id}}",
            "jobId": "{{your-job-id}}",
            "jobName": "{{my-batch-sm-job}}",
            "serviceJobType": "SAGEMAKER_TRAINING",
            "status": "RUNNING"
        }
    ]
}
```

For more information about job state mapping, see [Mapping AWS Batch service job status to SageMaker AI status](service-job-status.md).

## Step 6: View job output
<a name="getting-started-sagemaker-step-6"></a>

Once your job completes, you can view its output and logs through both AWS Batch and SageMaker AI APIs.

Get detailed information about your job from AWS Batch:

```
aws batch describe-service-job \
    --job-id {{your-job-id}}
```

Output:

```
{
    "attempts": [
        {
            "serviceResourceId": {
                "name": "TrainingJobArn",
                "value": "arn:aws:sagemaker:{{your-region}}:{{your-account-id}}:training-job/AWSBatch{{<my-simple-training-job>}}{{<your-attempt-id>}}"
            },
            "startedAt": 1753718820,
            "stoppedAt": 1753718880,
            "statusReason": "Received status from SageMaker: Training job completed"
        }
    ],
    "createdAt": 1753718760,
    "jobArn": "arn:aws:batch:{{your-region}}:{{your-account-id}}:service-job/{{your-job-id}}",
    "jobId": "{{your-job-id}}",
    "jobName": "{{my-batch-sm-job}}",
    "jobQueue": "arn:aws:batch:{{your-region}}:{{your-account-id}}:job-queue/{{my-sm-training-fifo-jq}}",
    "latestAttempt": {
        "serviceResourceId": {
            "name": "TrainingJobArn",
            "value": "arn:aws:sagemaker:{{your-region}}:{{your-account-id}}:training-job/AWSBatch{{<my-simple-training-job>}}{{<your-attempt-id>}}"
        }
    },
    "retryStrategy": {
        "attempts": 1,
        "evaluateOnExit": []
    },
    "serviceRequestPayload": "{{your-training-job-request-json}}",
    "serviceJobType": "SAGEMAKER_TRAINING",
    "startedAt": 1753718820,
    "status": "SUCCEEDED",
    "statusReason": "Received status from SageMaker: Training job completed",
    "stoppedAt": 1753718880,
    "tags": {},
    "timeoutConfig": {
        "attemptDurationSeconds": 60
    }
}
```

This command returns comprehensive job information including the SageMaker Training job ARN, which you can use to access the job directly through SageMaker AI:

```
aws sagemaker describe-training-job \
    --training-job-name AWSBatch{{<my-simple-training-job>}}{{<your-attempt-id>}}
```

To view the CloudWatch logs for your training job, first get the log stream name:

```
aws logs describe-log-streams \
    --log-group-name /aws/sagemaker/TrainingJobs \
    --log-stream-name-prefix AWSBatch{{my-simple-training-job}}
```

Output:

```
{
    "logStreams": [
        {
            "logStreamName": "{{your-log-stream-name}}",
            "creationTime": 1753718830,
            "firstEventTimestamp": 1753718840,
            "lastEventTimestamp": 1753718850,
            "lastIngestionTime": 1753718860,
            "uploadSequenceToken": {{upload-sequence-token}},
            "arn": "arn:aws:logs:{{your-region}}:{{your-account-id}}:log-group:/aws/sagemaker/TrainingJobs:log-stream:AWSBatch{{<my-simple-training-job>}}{{<your-attempt-id>}}/algo-1-{{algo-id}}",
            "storedBytes": 0
        }
    ]
}
```

Then retrieve the logs using the log stream name from the previous response:

```
aws logs get-log-events \
    --log-group-name /aws/sagemaker/TrainingJobs \
    --log-stream-name {{your-log-stream-name}}
```

Output:

```
{
    "events": [
        {
            "timestamp": 1753718845,
            "message": "hello world",
            "ingestionTime": 1753718865
        }
    ],
    "nextForwardToken": "{{next-forward-token}}",
    "nextBackwardToken": "{{next-backward-token}}"
}
```

The log output shows the "hello world" message from your training job, confirming that the job executed successfully.

## Step 7: Clean up your tutorial resources
<a name="getting-started-sagemaker-step-7"></a>

When you're done with the tutorial, clean up the resources you created to avoid ongoing charges.

First, disable and delete the job queue:

```
aws batch update-job-queue \
    --job-queue {{my-sm-training-fifo-jq}} \
    --state DISABLED
```

Wait for the job queue to be disabled, then delete it:

```
aws batch delete-job-queue \
    --job-queue {{my-sm-training-fifo-jq}}
```

Next, disable and delete the service environment:

```
aws batch update-service-environment \
    --service-environment {{TutorialServiceEnvironment}} \
    --state DISABLED
```

Wait for the service environment to be disabled, then delete it:

```
aws batch delete-service-environment \
    --service-environment {{TutorialServiceEnvironment}}
```

## Additional resources
<a name="getting-started-sagemaker-additional-resources"></a>

After you complete the tutorial, you might want to explore the following topics:
+ We recommend using the PySDK for service job creation and submission to your Job queue because PySDK has helper classes and utilities. For an example of using PySDK, see [SageMaker AI examples](https://github.com/aws/amazon-sagemaker-examples) on GitHub.
+ Learn more about [Service jobs in AWS Batch](service-jobs.md).
+ Explore [Service job payloads in AWS Batch](service-job-payload.md) for more complex training job configurations.
+ Learn about [Submit a service job in AWS Batch](service-job-submit.md) and the `SubmitServiceJob` API.
+ Review [Mapping AWS Batch service job status to SageMaker AI status](service-job-status.md) to understand job state transitions.
+ Visit the [SageMaker AI Python SDK documentation](https://sagemaker.readthedocs.io/en/stable/) for more feature-rich ways to create and submit SageMaker Training jobs using Python.
+ Explore [SageMaker example notebooks](https://github.com/aws/amazon-sagemaker-examples) for more complex machine learning workflows.
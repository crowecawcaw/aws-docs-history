# Jobs stuck in a `RUNNABLE` status

Suppose that your compute environment contains compute resources, but your jobs don't
progress beyond the `RUNNABLE` status. Then, it's likely that something is preventing
the jobs from being placed on a compute resource and causing your job queues to be blocked.
Here's how to know if your job is waiting for its turn or stuck and blocking the queue.

If AWS Batch detects that you have a `RUNNABLE` job at the head and blocking the
queue, you'll receive a [Job queue blocked
events](batch-job-queue-blocked-events.md "batch-job-queue-blocked-events.md") event from Amazon CloudWatch Events with the reason. The same
reason is also updated into the `statusReason` field as a part of `ListJobs`
and `DescribeJobs` API calls.

Optionally, you can configure the `jobStateTimeLimitActions` parameter through
`CreateJobQueue` and [`UpdateJobQueue`](../APIReference/API_UpdateJobQueue.md "../APIReference/API_UpdateJobQueue.md") API
actions.

###### Note

Currently, the only action you can use with `jobStateLimitActions.action` is to
cancel a job.

The `jobStateTimeLimitActions` parameter is used to specify a set of actions
that AWS Batch performs on jobs in a specific state. You can set a time threshold in seconds
through the `maxTimeSeconds` field.

When a job has been in a `RUNNABLE` state with the defined
`statusReason`, AWS Batch performs the action specified after
`maxTimeSeconds` have elapsed.

For example, you can set the `jobStateTimeLimitActions` parameter to wait up to
4 hours for any job in the `RUNNABLE` state that is waiting for sufficient capacity
to become available. You can do this by setting `statusReason` to
`CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY` and `maxTimeSeconds` to 144000
before cancelling the job and allowing the next job to advance to the head of the job
queue.

The following are the reasons that AWS Batch provides when it detects that a job queue is
blocked. This list provides the messages returned from the `ListJobs` and
`DescribeJobs` API actions. These are also the same values you can define for the
`jobStateLimitActions.statusReason` parameter.

1. **Reason:** All connected compute environments have
   insufficient capacity errors. When requested, AWS Batch detects Amazon EC2 instances that experience
   insufficient capacity errors. Manually canceling the job will allow the subsequent job to move
   to the head of the queue but without resolving the service role issue(s), it is likely that
   the next job will also be blocked as well. It's best to manually investigate and resolve this
   issue.
   - **`statusReason` message while the job is
     stuck:**
     `CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY - Service cannot fulfill the capacity
 requested for instance type [instanceTypeName]`
   - **`reason` used for
     `jobStateTimeLimitActions`:**
     `CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY`
   - **`statusReason` message after the job is
     canceled:**
     `Canceled by JobStateTimeLimit action due to reason:
 CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY`

**Note:**

    1. The AWS Batch service role requires `autoscaling:DescribeScalingActivities`
     permission for this detection to work. If you use the [Using service-linked roles for
     AWS Batch](using-service-linked-roles.md "using-service-linked-roles.md") service-linked role (SLR) or the [AWS managed policy:
     AWSBatchServiceRole policy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSBatchServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSBatchServiceRolePolicy") managed policy, then you
     don't need to take any action because their permission policies are updated.
    2. If you use the SLR or the managed policy, you must add the
     `autoscaling:DescribeScalingActivities` and
     `ec2:DescribeSpotFleetRequestHistory` permissions so that you can receive
     blocked job queue events and updated job status when in `RUNNABLE`. In addition,
     AWS Batch needs these permissions to perform `cancellation` actions through the
     `jobStateTimeLimitActions` parameter even if they are configured on the job
     queue.
    3. In the case of a multi-node parallel (MNP) job, if the attached high-priority, Amazon EC2
     compute environment experiences `insufficient capacity` errors, it blocks the
     queue even if a lower priority compute environment does experience this error.

2. **Reason:** All compute environments have a [`maxvCpus`](../APIReference/API_ComputeResource.md#Batch-Type-ComputeResource-maxvCpus "../APIReference/API_ComputeResource.md#Batch-Type-ComputeResource-maxvCpus") parameter that is smaller than the job requirements.
   Canceling the job, either manually or by setting the `jobStateTimeLimitActions`
   parameter on `statusReason`, allows the subsequent job to move to the head of the
   queue. Optionally, you can increase the `maxvCpus` parameter of the primary compute
   environment to meet the needs of the blocked job.
   - **`statusReason` message while the job is
     stuck:**
     `MISCONFIGURATION:COMPUTE_ENVIRONMENT_MAX_RESOURCE - CE(s) associated with the job
 queue cannot meet the CPU requirement of the job.`
   - **`reason` used for
     `jobStateTimeLimitActions`:**
     `MISCONFIGURATION:COMPUTE_ENVIRONMENT_MAX_RESOURCE`
   - **`statusReason` message after the job is
     canceled:**
     `Canceled by JobStateTimeLimit action due to reason:
 MISCONFIGURATION:COMPUTE_ENVIRONMENT_MAX_RESOURCE`

3. **Reason:** None of the compute environments have instances
   that meet the job requirements. When a job requests resources, AWS Batch detects that no
   attached compute environment is able to accommodate the incoming job. Canceling the job,
   either manually or by setting the `jobStateTimeLimitActions` parameter on
   `statusReason`, allows the subsequent job to move to the head of the queue.
   Optionally, you can redefine the compute environment's allowed instance types to add the
   necessary job resources.
   - **`statusReason` message while the job is
     stuck:**
     `MISCONFIGURATION:JOB_RESOURCE_REQUIREMENT - The job resource requirement
(vCPU/memory/GPU) is higher than that can be met by the CE(s) attached to the job
queue.`
   - **`reason` used for
     `jobStateTimeLimitActions`:**
     `MISCONFIGURATION:JOB_RESOURCE_REQUIREMENT`
   - **`statusReason` message after the job is
     canceled:**
     `Canceled by JobStateTimeLimit action due to reason:
 MISCONFIGURATION:JOB_RESOURCE_REQUIREMENT`

4. **Reason:** All compute environments have service role
   issues. To resolve this, compare your service role permissions to the [AWS managed policies for AWS Batch](security-iam-awsmanpol.md "security-iam-awsmanpol.md") and address any
   gaps. Note:You can't configure a programmable action through the `jobStateTimeLimitActions`
   parameter to resolve this error.

It's a best practice to use the [Using service-linked roles for
AWS Batch](using-service-linked-roles.md "using-service-linked-roles.md") to avoid similar errors.

Canceling the job, either manually or by setting the
`jobStateTimeLimitActions` parameter on `statusReason`, allows the
subsequent job to move to the head of the queue. Without resolving the service role issue(s),
it is likely that the next job will also be blocked as well. It's best to manually investigate
and resolve this issue.

    * **`statusReason` message while the job is
     stuck:**
    `MISCONFIGURATION:SERVICE_ROLE_PERMISSIONS – Batch service role has a permission
     issue.`

5. **Reason:** Your compute environment has an unsupported
   instance type configuration. This can occur when instance types are not available in your
   selected Availability Zones, or when your launch template or launch configuration contains
   settings incompatible with the specified instance types. To resolve this, verify that your
   instance types are supported in your specified AWS Region and Availability Zones, check
   that your launch template settings are compatible with your instance types, and consider
   updating to newer generation instance types. For more information about finding supported
   instance types, see [Finding an Amazon EC2 instance type](../../../AWSEC2/latest/UserGuide/instance-discovery.md "../../../AWSEC2/latest/UserGuide/instance-discovery.md") in the _Amazon
   EC2 User Guide_.
   - **`statusReason` message while the job is
     stuck:**
     `MISCONFIGURATION:EC2_INSTANCE_CONFIGURATION_UNSUPPORTED - Your compute environment associated with this job queue has an unsupported instance type configuration.`

6. **Reason:** All compute environments are invalid. For more
   information, see [INVALID compute environment](invalid_compute_environment.md "invalid_compute_environment.md"). Note: You can't configure a programmable
   action through the `jobStateTimeLimitActions` parameter to resolve this error.
   - **`statusReason` message while the job is
     stuck:**
     `ACTION_REQUIRED - CE(s) associated with the job queue are invalid.`

7. **Reason:** AWS Batch has detected a blocked queue, but is
   unable to determine the reason. Note: You can't configure a programmable action through the
   `jobStateTimeLimitActions` parameter to resolve this error. For more information
   about troubleshooting, see [Why is my AWS Batch
   job stuck in RUNNABLE on AWS](https://repost.aws/knowledge-center/batch-job-stuck-runnable-status "https://repost.aws/knowledge-center/batch-job-stuck-runnable-status") in _re:Post_.
   - **`statusReason` message while the job is
     stuck:**
     `UNDETERMINED - Batch job is blocked, root cause is undetermined.`

In case you did not receive an event from CloudWatch Events or you received the unknown reason event,
here are some common causes for this issue.

**The `awslogs` log driver isn't configured on your
compute resources**

AWS Batch jobs send their log information to CloudWatch Logs. To enable this, you must configure
your compute resources to use the `awslogs` log driver. Suppose that you base your
compute resource AMI off of the Amazon ECS optimized AMI (or Amazon Linux). Then, this driver is
registered by default with the `ecs-init` package. Now suppose that you use a
different base AMI. Then, you must verify that the `awslogs` log driver is
specified as an available log driver with the `ECS_AVAILABLE_LOGGING_DRIVERS`
environment variable when the Amazon ECS container agent is started. For more information, see
[Compute resource AMI specification](batch-ami-spec.md "batch-ami-spec.md") and [Tutorial: Create a compute resource AMI](create-batch-ami.md "create-batch-ami.md").

**Insufficient resources**

If your job definitions specify more CPU or memory resources than your compute resources
can allocate, then your jobs aren't ever placed. For example, suppose that your job specifies
4 GiB of memory, and your compute resources have less than that available. Then it's the case
that the job can't be placed on those compute resources. In this case, you must reduce the
specified memory in your job definition or add larger compute resources to your environment.
Some memory is reserved for the Amazon ECS container agent and other critical system processes.
For more information, see [Compute resource memory management](memory-management.md "memory-management.md").

**No internet access for compute resources**
Compute resources need access to communicate with the Amazon ECS
service endpoint. This can be through an interface VPC endpoint or through your
compute resources having public IP addresses.

For more information about interface VPC endpoints, see [Amazon ECS Interface
VPC Endpoints (AWS PrivateLink)](../../../AmazonECS/latest/developerguide/vpc-endpoints.md "../../../AmazonECS/latest/developerguide/vpc-endpoints.md") in the
_Amazon Elastic Container Service Developer Guide_.

If you do not have an interface VPC endpoint configured and your compute
resources do not have public IP addresses, then they must use
network address translation (NAT) to provide this access. For more information,
see [NAT gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the
_Amazon VPC User Guide_. For more information, see
[Create a VPC](create-a-vpc.md "create-a-vpc.md").

**Amazon EC2 instance limit reached**

The number of Amazon EC2 instances that your account can launch in an AWS Region is
determined by your EC2 instance quota. Certain instance types also have a per-instance-type
quota. For more information about your account's Amazon EC2 instance quota including how to
request a limit increase, see [Amazon EC2
Service Limits](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md") in the _Amazon EC2 User Guide_.

**Amazon ECS container agent isn't installed**

The Amazon ECS container agent must be installed on the Amazon Machine Image (AMI) to let
AWS Batch run jobs. The Amazon ECS container agent is installed by default on Amazon ECS optimized
AMIs. For more information about the Amazon ECS container agent, see [Amazon ECS container agent](../../../AmazonECS/latest/developerguide/ECS_agent.md "../../../AmazonECS/latest/developerguide/ECS_agent.md") in the
_Amazon Elastic Container Service Developer Guide_.

For more information, see [Why is my AWS Batch job stuck in `RUNNABLE` status?](https://aws.amazon.com/premiumsupport/knowledge-center/batch-job-stuck-runnable-status/ "https://aws.amazon.com/premiumsupport/knowledge-center/batch-job-stuck-runnable-status/") in
_re:Post_.



# Jobs stuck in RUNNABLE due to misconfiguration
<a name="job_stuck_in_runnable_misconfiguration"></a>

Misconfiguration issues occur when the compute environment or job definition settings prevent AWS Batch from placing jobs on compute resources.

**Compute environment maximum resource too small**  
All compute environments have a [`maxvCpus`](https://docs.aws.amazon.com/batch/latest/APIReference/API_ComputeResource.html#Batch-Type-ComputeResource-maxvCpus) parameter that is smaller than the job requirements. Canceling the job, either manually or by setting the `jobStateTimeLimitActions` parameter on `statusReason`, allows the subsequent job to move to the head of the queue. Optionally, you can increase the `maxvCpus` parameter of the primary compute environment to meet the needs of the blocked job.  
+ **`statusReason` message while the job is stuck:** `MISCONFIGURATION:COMPUTE_ENVIRONMENT_MAX_RESOURCE - CE(s) associated with the job queue cannot meet the CPU requirement of the job.`
+ **`reason` used for `jobStateTimeLimitActions`:** `MISCONFIGURATION:COMPUTE_ENVIRONMENT_MAX_RESOURCE`
+ **`statusReason` message after the job is canceled by `jobStateTimeLimitActions`:** `Canceled by JobStateTimeLimit action due to reason: MISCONFIGURATION:COMPUTE_ENVIRONMENT_MAX_RESOURCE`

**Job resource requirements exceed available instance types**  
None of the compute environments have instances that meet the job requirements. When a job requests resources, AWS Batch detects that no attached compute environment is able to accommodate the incoming job. Canceling the job, either manually or by setting the `jobStateTimeLimitActions` parameter on `statusReason`, allows the subsequent job to move to the head of the queue. Optionally, you can redefine the compute environment's allowed instance types to add the necessary job resources.  
+ **`statusReason` message while the job is stuck:** `MISCONFIGURATION:JOB_RESOURCE_REQUIREMENT - The job resource requirement (vCPU/memory/GPU) is higher than that can be met by the CE(s) attached to the job queue.`
+ **`reason` used for `jobStateTimeLimitActions`:** `MISCONFIGURATION:JOB_RESOURCE_REQUIREMENT`
+ **`statusReason` message after the job is canceled by `jobStateTimeLimitActions`:** `Canceled by JobStateTimeLimit action due to reason: MISCONFIGURATION:JOB_RESOURCE_REQUIREMENT`

**Unsupported instance type configuration**  
Your compute environment has an unsupported instance type configuration. This can occur when instance types are not available in your selected Availability Zones, or when your launch template or launch configuration contains settings incompatible with the specified instance types. To resolve this, verify that your instance types are supported in your specified AWS Region and Availability Zones, check that your launch template settings are compatible with your instance types, and consider updating to newer generation instance types. For more information about finding supported instance types, see [Finding an Amazon EC2 instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-discovery.html) in the *Amazon EC2 User Guide*.  
+ **`statusReason` message while the job is stuck:** `MISCONFIGURATION:EC2_INSTANCE_CONFIGURATION_UNSUPPORTED - Your compute environment associated with this job queue has an unsupported instance type configuration.`

**Service role permission issues**  
All compute environments have service role issues. To resolve this, compare your service role permissions to the [AWS managed policies for AWS Batch](security-iam-awsmanpol.md) and address any gaps. It's a best practice to use the [Using service-linked roles for AWS Batch](using-service-linked-roles.md) to avoid similar errors.  
Canceling the job, either manually or by setting the `jobStateTimeLimitActions` parameter on `statusReason`, allows the subsequent job to move to the head of the queue. Without resolving the service role issue(s), it is likely that the next job will also be blocked as well. It's best to manually investigate and resolve this issue.  
+ **`statusReason` message while the job is stuck:** `MISCONFIGURATION:SERVICE_ROLE_PERMISSIONS – Batch service role has a permission issue.`
Note: You can't configure a programmable action through the `jobStateTimeLimitActions` parameter to resolve this error.


# Common causes of jobs stuck in RUNNABLE without a `statusReason`
<a name="job_stuck_in_runnable_common_causes"></a>

In case you did not receive an event from CloudWatch Events or you received the unknown reason event, here are some common causes for this issue.

**The `awslogs` log driver isn't configured on your compute resources**  
AWS Batch jobs send their log information to CloudWatch Logs. To enable this, you must configure your compute resources to use the `awslogs` log driver. Suppose that you base your compute resource AMI off of the Amazon ECS optimized AMI (or Amazon Linux). Then, this driver is registered by default with the `ecs-init` package. Now suppose that you use a different base AMI. Then, you must verify that the `awslogs` log driver is specified as an available log driver with the `ECS_AVAILABLE_LOGGING_DRIVERS` environment variable when the Amazon ECS container agent is started. For more information, see [Compute resource AMI specification](batch-ami-spec.md) and [Tutorial: Create a compute resource AMI](create-batch-ami.md).

**Insufficient resources**  
If your job definitions specify more CPU or memory resources than your compute resources can allocate, then your jobs aren't ever placed. For example, suppose that your job specifies 4 GiB of memory, and your compute resources have less than that available. Then it's the case that the job can't be placed on those compute resources. In this case, you must reduce the specified memory in your job definition or add larger compute resources to your environment. Some memory is reserved for the Amazon ECS container agent and other critical system processes. For more information, see [Compute resource memory management](memory-management.md).

**No internet access for compute resources**  
Compute resources need access to communicate with the Amazon ECS service endpoint. This can be through an interface VPC endpoint or through your compute resources having public IP addresses.  
For more information about interface VPC endpoints, see [Amazon ECS Interface VPC Endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/vpc-endpoints.html) in the *Amazon Elastic Container Service Developer Guide*.  
If you do not have an interface VPC endpoint configured and your compute resources do not have public IP addresses, then they must use network address translation (NAT) to provide this access. For more information, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon VPC User Guide*. For more information, see [Create a VPC](create-a-vpc.md).

**Amazon EC2 instance limit reached**  
The number of Amazon EC2 instances that your account can launch in an AWS Region is determined by your EC2 instance quota. Certain instance types also have a per-instance-type quota. For more information about your account's Amazon EC2 instance quota including how to request a limit increase, see [Amazon EC2 Service Limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) in the *Amazon EC2 User Guide*.

**Amazon ECS container agent isn't installed**  
The Amazon ECS container agent must be installed on the Amazon Machine Image (AMI) to let AWS Batch run jobs. The Amazon ECS container agent is installed by default on Amazon ECS optimized AMIs. For more information about the Amazon ECS container agent, see [Amazon ECS container agent](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_agent.html) in the *Amazon Elastic Container Service Developer Guide*.

**Long-running user data scripts in a launch template**  
If your launch template includes a user data script that takes a long time to complete, instances can time out before they register with Amazon ECS. When this happens, the instances never become available to pick up jobs, leaving all jobs stuck in `RUNNABLE` status. All user data scripts must finish before an instance can register with Amazon ECS and start running jobs.  
To resolve this, review your launch template user data for long-running or blocking operations. Consider optimizing scripts to reduce execution time, running non-critical operations asynchronously, or moving initialization logic out of user data entirely. For more information, see [Use Amazon EC2 launch templates with AWS Batch](launch-templates.md).

For more information, see [Why is my AWS Batch job stuck in `RUNNABLE` status?](https://aws.amazon.com/premiumsupport/knowledge-center/batch-job-stuck-runnable-status/) in *re:Post*.
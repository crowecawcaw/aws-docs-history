

# Deploying the security agent to Amazon ECS on Fargate
<a name="how-runtime-monitoring-works-ecs-fargate"></a>

GuardDuty Runtime Monitoring monitors your Amazon ECS clusters on Fargate for threats by deploying the GuardDuty security agent to them.

**Note**  
Runtime Monitoring doesn't support applications running on [Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ManagedInstances.html).

GuardDuty manages the agent automatically; manual management isn't available for Fargate. In the GuardDuty console, this configuration appears as *Runtime Monitoring (ECS)*.

## Automated agent configuration (recommended)
<a name="ecsrunmon-manage-security-agent-auto"></a>

GuardDuty manages deployment and updates to the security agent for new Fargate tasks in your Amazon ECS clusters.

For how the security agent connects to GuardDuty, see [How the security agent connects to GuardDuty](runtime-monitoring-agent-connectivity.md).

**Impact of enabling the security agent**

For each new Fargate task, GuardDuty attaches a sidecar container that runs the security agent and collects the runtime events of the containers in the task.

The sidecar image is stored in Amazon Elastic Container Registry (Amazon ECR), with layers in Amazon S3, and is pulled when the task starts. Depending on your network configuration, you might need to allow access to ECR and S3. For example, allow the S3 managed prefix list if you use restricted security groups. For more information, see [Prerequisites for container image access](prereq-runtime-monitoring-ecs-support.md#before-enable-runtime-monitoring-ecs).

If the sidecar can't launch, Runtime Monitoring doesn't prevent the task from running. Fargate tasks can't be modified after they start, so GuardDuty attaches the sidecar at task launch.

**Monitoring scope**

By default, GuardDuty manages the security agent for all Amazon ECS clusters in your account. To stop GuardDuty from managing the agent on a specific cluster, add the tag `GuardDutyManaged`:`false` to that cluster.

For more information about managing the agent for Fargate tasks, see [Managing automated security agent for Fargate (Amazon ECS only)](managing-gdu-agent-ecs-automated.md).

**Considerations**
+ When automated agent configuration is off, GuardDuty manages the security agent only on the Amazon ECS clusters that you tag with `GuardDutyManaged`:`true`.
+ Adding the `GuardDutyManaged`:`false` tag stops GuardDuty from managing the security agent, but doesn't uninstall an agent that is already installed.
+ Protect the `GuardDutyManaged` tag by controlling who can modify it, using service control policies or IAM policies. For more information, see [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide* or [Control access to AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *IAM User Guide*.

## Related topics
<a name="ecsrunmon-related"></a>
+ [How the security agent connects to GuardDuty](runtime-monitoring-agent-connectivity.md)
+ [Tracking Runtime Monitoring coverage](runtime-monitoring-after-configuration.md)
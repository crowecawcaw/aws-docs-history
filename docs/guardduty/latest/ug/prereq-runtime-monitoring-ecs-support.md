# Prerequisites for AWS Fargate (Amazon ECS

only) support

This section includes the prerequisites for monitoring runtime behavior of your
Fargate-Amazon ECS resources. After these prerequisites are met, see [Enabling GuardDuty Runtime Monitoring](runtime-monitoring-configuration.md "runtime-monitoring-configuration.md").

###### Topics

- [Validating architectural requirements](#validating-architecture-req-ecs "#validating-architecture-req-ecs")
- [Prerequisites for container image access](#before-enable-runtime-monitoring-ecs "#before-enable-runtime-monitoring-ecs")
- [Validating your organization service control
  policy in a multi-account environment](#validate-organization-scp-ecs "#validate-organization-scp-ecs")
- [Validating role
  permissions and policy permissions boundary](#guardduty-runtime-monitoring-ecs-permission-boundary "#guardduty-runtime-monitoring-ecs-permission-boundary")
- [CPU and memory limits](#ecs-runtime-agent-cpu-memory-limits "#ecs-runtime-agent-cpu-memory-limits")

## Validating architectural requirements

The platform that you use may impact how GuardDuty security agent supports GuardDuty in receiving
the runtime events from your Amazon ECS clusters. You must validate that you're using one of the
verified platforms.

**Initial considerations:**

The AWS Fargate platform for your Amazon ECS clusters must be Linux. The corresponding
platform version must be at least `1.4.0`, or `LATEST`. For more
information about the platform versions, see [Linux platform
versions](../../../AmazonECS/latest/developerguide/platform-linux-fargate.md "../../../AmazonECS/latest/developerguide/platform-linux-fargate.md") in the _Amazon Elastic Container Service Developer Guide_.

The Windows platform versions are not yet supported.

### Verified platforms

The OS distribution and CPU architecture impacts the support provided by the GuardDuty
security agent. The following table shows the verified configuration for deploying the GuardDuty
security agent and configuring Runtime Monitoring.

| OS distribution**[1](#runtime-monitoring-ecs-os-support "#runtime-monitoring-ecs-os-support")** | Kernel support            | CPU architecture x64 (AMD64) | CPU architecture Graviton (ARM64) |
| ----------------------------------------------------------------------------------------------- | ------------------------- | ---------------------------- | --------------------------------- |
| Linux                                                                                           | eBPF, Tracepoints, Kprobe | Supported                    | Supported                         |

1Support for various operating systems - GuardDuty has verified Runtime Monitoring
support for the operating distribution listed in the preceding table. While the GuardDuty security agent may
run on operating systems not listed in the preceding table, the GuardDuty team cannot guarantee the
expected security value.

## Prerequisites for container image access

The following prerequisites help you access the GuardDuty sidecar container image from the Amazon ECR repository.

### Permissions requirements

The task execution role requires certain Amazon Elastic Container Registry (Amazon ECR) permissions to download the GuardDuty security agent container image:

```
...
      "ecr:GetAuthorizationToken",
      "ecr:BatchCheckLayerAvailability",
      "ecr:GetDownloadUrlForLayer",
      "ecr:BatchGetImage",
...
```

To further restrict the Amazon ECR permissions, you can add the Amazon ECR repository URI that
hosts the GuardDuty security agent for AWS Fargate (Amazon ECS only). For more information, see
[Amazon ECR repository hosting GuardDuty
agent](runtime-monitoring-ecr-repository-gdu-agent.md "runtime-monitoring-ecr-repository-gdu-agent.md").

You can either use the [AmazonECSTaskExecutionRolePolicy](../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md "../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md") managed policy or add the above permissions to
your `TaskExecutionRole` policy.

### Task definition configuration

When creating or updating Amazon ECS services, you need to provide subnet information in your task definition:

Running the [CreateService](../../../AmazonECS/latest/APIReference/API_CreateService.md "../../../AmazonECS/latest/APIReference/API_CreateService.md") and [UpdateService](../../../AmazonECS/latest/APIReference/API_UpdateService.md "../../../AmazonECS/latest/APIReference/API_UpdateService.md") APIs in
the _Amazon Elastic Container Service API Reference_ requires you to pass the subnet information. For
more information, see [Amazon ECS task definitions](../../../AmazonECS/latest/developerguide/task_definitions.md "../../../AmazonECS/latest/developerguide/task_definitions.md")
in the _Amazon Elastic Container Service Developer Guide_.

### Network connectivity requirements

You must ensure network connectivity to download the GuardDuty container image from Amazon ECR. This requirement
is specific to GuardDuty because it uses Amazon ECR to host its security agent. Depending on your network configuration, you need
to implement one of the following options:

**Option 1 - Using public network access (if available)**

If your Fargate tasks run in subnets with outbound internet access, no additional network configuration is required.

**Option 2 - Using Amazon VPC endpoints (for private subnets)**

If your Fargate tasks run in private subnets without internet access, you must configure VPC endpoints for ECR to ensure that the ECR repository URI that hosts the GuardDuty security agent is network accessible. Without these endpoints, tasks in private subnets cannot download the GuardDuty container image.

For VPC endpoint setup instructions, see [Create
the VPC endpoints for Amazon ECR](../../../AmazonECR/latest/userguide/vpc-endpoints.md#ecr-setting-up-vpc-create "../../../AmazonECR/latest/userguide/vpc-endpoints.md#ecr-setting-up-vpc-create") in the
_Amazon Elastic Container Registry User Guide_.

For information about enabling Fargate to download the GuardDuty container, see [Using Amazon ECR images
with Amazon ECS](../../../AmazonECR/latest/userguide/ECR_on_ECS.md "../../../AmazonECR/latest/userguide/ECR_on_ECS.md") in the _Amazon Elastic Container Registry User Guide_.

### Security group configuration

The GuardDuty container images are in Amazon ECR and require Amazon S3 access. This requirement is specific to downloading container images from Amazon ECR.
For tasks with restricted network access, you must configure your security groups to allow access to S3.

Add an outbound rule in your security group that allows traffic to the [S3 managed prefix list
(`pl-xxxxxxxx`) on port 443](../../../vpc/latest/privatelink/gateway-endpoints.md#gateway-endpoint-security "../../../vpc/latest/privatelink/gateway-endpoints.md#gateway-endpoint-security"). To add an outbound rule, see
[Configure security group rules](../../../vpc/latest/userguide/working-with-security-group-rules.md "../../../vpc/latest/userguide/working-with-security-group-rules.md")
in the _Amazon VPC User Guide_.

To view your AWS-managed prefix lists in the console or describe them by using AWS Command Line Interface (AWS CLI), see
[AWS-managed prefix lists](../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md "../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md")
in the _Amazon VPC User Guide_.

## Validating your organization service control

policy in a multi-account environment

This section explains how to validate your service control policy (SCP) settings to ensure
Runtime Monitoring works as expected across your organization.

If you have set up one or more service control policies to manage permissions in your
organization, you must validate that it doesn't deny the
`guardduty:SendSecurityTelemetry` action. For information about how SCPs work, see
[SCP
evaluation](../../../organizations/latest/userguide/orgs_manage_policies_scps_evaluation.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_evaluation.md") in the _AWS Organizations User Guide_.

If you are a member account, connect with the associated delegated administrator. For
information about managing SCPs for your organization, see [Service control policies
(SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_.

Perform the following steps for all the SCPs that you have set up in your multi-account
environment:

###### To validate `guardduty:SendSecurityTelemetry` is not denied in SCP

1. Sign in to the Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/ "https://console.aws.amazon.com/organizations/"). You must sign in as an IAM role, or sign in as the root user
   [(not
   recommended)](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials") in the organization's management account.
2. In the left navigation pane, select **Policies**. Then, under
   **Supported policy types**, select **Service control
   policies**.
3. On the **Service control policies** page, choose the name of the policy
   that you want to validate.
4. On the policy's detail page, view the **Content** of this policy. Make
   sure that it doesn't deny the `guardduty:SendSecurityTelemetry` action.

The following SCP policy is an example for _not denying_ the
`guardduty:SendSecurityTelemetry` action:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "guardduty:SendSecurityTelemetry"
 ],
 "Resource": "*"
 }
 ]
}`

```

If your policy denies this action, you must update the policy. For more information, see
[Update a service
control policy (SCP)](../../../organizations/latest/userguide/orgs_policies_update.md#update_policy "../../../organizations/latest/userguide/orgs_policies_update.md#update_policy") in the _AWS Organizations User Guide_.

## Validating role

permissions and policy permissions boundary

Use the following steps to validate that the permissions boundaries associated with the
role and its policy **doesn't** the restrict
`guardduty:SendSecurityTelemetry` action.

###### To view permissions boundary for roles and its policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, under **Access management**, choose
   **Roles**.
3. On the **Roles** page, select the role
   `TaskExecutionRole` that you may have created.
4. On the selected role's page, under the **Permissions** tab, expand the
   policy name associated with this role. Then, validate that this policy doesn't restrict
   `guardduty:SendSecurityTelemetry`.
5. If the **Permissions boundary** is set, then expand this section. Then,
   expand each policy to review that it doesn't restrict the
   `guardduty:SendSecurityTelemetry` action. The policy should appear similar to this
   [Example SCP policy](#ecs-runtime-scp-not-deny-policy-example "#ecs-runtime-scp-not-deny-policy-example").

As needed, perform one of the following actions:

    * To modify the policy, select **Edit**. On the **Modify
     permissions** page for this policy, update the policy in the **Policy
     editor**. Make sure that the JSON schema remains valid. Then, choose
     **Next**. Then, you can review and save the changes.
    * To change this permissions boundary and choose another boundary, choose
     **Change boundary**.
    * To remove this permissions boundary, choose **Remove
     boundary**.

For information about managing policies, see [Policies and permissions in AWS Identity and Access Management](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md")
in the _IAM User Guide_.

## CPU and memory limits

In the Fargate task definition, you must specify the CPU and memory value at the task
level. The following table shows the valid combinations of task-level CPU and memory values, and
the corresponding GuardDuty security agent maximum memory limit for the GuardDuty container.

| CPU value                                  | Memory value                                | GuardDuty agent maximum memory limit |
| ------------------------------------------ | ------------------------------------------- | ------------------------------------ |
| 256 (.25 vCPU)                             | 512 MiB, 1 GB, 2GB                          | 128 MB                               |
| 512 (.5 vCPU)                              | 1 GB, 2 GB, 3 GB, 4 GB                      |
| 1024 (1 vCPU)                              | 2 GB, 3 GB, 4 GB                            |
| 5 GB, 6 GB, 7 GB, 8 GB                     |
| 2048 (2 vCPU)                              | Between 4 GB and 16 GB in 1 GB increments   |
| 4096 (4 vCPU)                              | Between 8 GB and 20 GB in 1 GB increments   |
| 8192 (8 vCPU)                              | Between 16 GB and 28 GB in 4 GB increments  | 256 MB                               |
| Between 32 GB and 60 GB in 4 GB increments | 512 MB                                      |
| 16384 (16 vCPU)                            | Between 32 GB and 120 GB in 8 GB increments | 1 GB                                 |

After you enable Runtime Monitoring and assess that the coverage status of your cluster is **Healthy**, you can set up and view the Container insight metrics. For more
information, [Setting up monitoring on Amazon ECS
cluster](runtime-monitoring-setting-cpu-mem-monitoring.md#ecs-runtime-cpu-memory-monitoring-agent "runtime-monitoring-setting-cpu-mem-monitoring.md#ecs-runtime-cpu-memory-monitoring-agent").

The next step is to configure Runtime Monitoring and also configure the security agent.

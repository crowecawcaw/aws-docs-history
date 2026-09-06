

# Prerequisites for AWS Fargate (Amazon ECS only) support
<a name="prereq-runtime-monitoring-ecs-support"></a>

This section includes the prerequisites for monitoring runtime behavior of your Fargate-Amazon ECS resources. After these prerequisites are met, see [Enabling GuardDuty Runtime Monitoring](runtime-monitoring-configuration.md).

**Topics**
+ [Validating architectural requirements](#validating-architecture-req-ecs)
+ [Prerequisites for container image access](#before-enable-runtime-monitoring-ecs)
+ [Validating your organization service control policy in a multi-account environment](#validate-organization-scp-ecs)
+ [Validating role permissions and policy permissions boundary](#guardduty-runtime-monitoring-ecs-permission-boundary)
+ [CPU and memory limits](#ecs-runtime-agent-cpu-memory-limits)

## Validating architectural requirements
<a name="validating-architecture-req-ecs"></a>

The platform that you use may impact how GuardDuty security agent supports GuardDuty in receiving the runtime events from your Amazon ECS clusters. You must validate that you're using one of the verified platforms.

**Initial considerations:**  
The AWS Fargate platform for your Amazon ECS clusters must be Linux. The corresponding platform version must be at least `1.4.0`, or `LATEST`. For more information about the platform versions, see [Linux platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform-linux-fargate.html) in the *Amazon Elastic Container Service Developer Guide*.  
The Windows platform versions are not yet supported. 

### Verified platforms
<a name="ecs-verified-platforms-gdu-agent"></a>

The OS distribution and CPU architecture impacts the support provided by the GuardDuty security agent. The following table shows the verified configuration for deploying the GuardDuty security agent and configuring Runtime Monitoring.


| OS distribution**[1](#runtime-monitoring-ecs-os-support)**  | Kernel support | CPU architecture x64 (AMD64) | CPU architecture Graviton (ARM64) | 
| --- | --- | --- | --- | 
| Linux | eBPF, Tracepoints, Kprobe | Supported | Supported | <a name="runtime-monitoring-ecs-os-support"></a>

1Support for various operating systems - GuardDuty has verified Runtime Monitoring support for the operating distribution listed in the preceding table. While the GuardDuty security agent may run on operating systems not listed in the preceding table, the GuardDuty team cannot guarantee the expected security value.

## Prerequisites for container image access
<a name="before-enable-runtime-monitoring-ecs"></a>

The following prerequisites help you access the GuardDuty sidecar container image from the Amazon ECR repository.

### Permissions requirements
<a name="ecs-runtime-permissions-requirements"></a>

The task execution role requires certain Amazon Elastic Container Registry (Amazon ECR) permissions to download the GuardDuty security agent container image:

```
...
      "ecr:GetAuthorizationToken",
      "ecr:BatchCheckLayerAvailability",
      "ecr:GetDownloadUrlForLayer",
      "ecr:BatchGetImage",
...
```

To further restrict the Amazon ECR permissions, you can add the Amazon ECR repository URI that hosts the GuardDuty security agent for AWS Fargate (Amazon ECS only). For more information, see [Amazon ECR repository hosting GuardDuty agent](runtime-monitoring-ecr-repository-gdu-agent.md).

You can either use the [AmazonECSTaskExecutionRolePolicy](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html) managed policy or add the above permissions to your `TaskExecutionRole` policy.

### Task definition configuration
<a name="ecs-runtime-task-definition"></a>

When creating or updating Amazon ECS services, you need to provide subnet information in your task definition:

Running the [CreateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html) and [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) APIs in the *Amazon Elastic Container Service API Reference* requires you to pass the subnet information. For more information, see [Amazon ECS task definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html) in the *Amazon Elastic Container Service Developer Guide*.

### Network connectivity requirements
<a name="ecs-runtime-network-requirements"></a>

You must ensure network connectivity to download the GuardDuty container image from Amazon ECR. This requirement is specific to GuardDuty because it uses Amazon ECR to host its security agent. Depending on your network configuration, you need to implement one of the following options:

**Option 1 - Using public network access (if available)**  
If your Fargate tasks run in subnets with outbound internet access, no additional network configuration is required.

**Option 2 - Using Amazon VPC endpoints (for private subnets)**  
If your Fargate tasks run in private subnets without internet access, you must configure VPC endpoints for ECR to ensure that the ECR repository URI that hosts the GuardDuty security agent is network accessible. Without these endpoints, tasks in private subnets cannot download the GuardDuty container image.  
For VPC endpoint setup instructions, see [Create the VPC endpoints for Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/vpc-endpoints.html#ecr-setting-up-vpc-create) in the *Amazon Elastic Container Registry User Guide*.

For information about enabling Fargate to download the GuardDuty container, see [Using Amazon ECR images with Amazon ECS](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_on_ECS.html) in the *Amazon Elastic Container Registry User Guide*.

### Security group configuration
<a name="ecs-runtime-security-group-requirements"></a>

The GuardDuty container images are in Amazon ECR and require Amazon S3 access. This requirement is specific to downloading container images from Amazon ECR. For tasks with restricted network access, you must configure your security groups to allow access to S3.

Add an outbound rule in your security group that allows traffic to the [S3 managed prefix list (`pl-xxxxxxxx`) on port 443](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html#gateway-endpoint-security). To add an outbound rule, see [Configure security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-security-group-rules.html) in the *Amazon VPC User Guide*.

To view your AWS-managed prefix lists in the console or describe them by using AWS Command Line Interface (AWS CLI), see [AWS-managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-aws-managed-prefix-lists.html) in the *Amazon VPC User Guide*.

## Validating your organization service control policy in a multi-account environment
<a name="validate-organization-scp-ecs"></a>

This section explains how to validate your service control policy (SCP) settings to ensure Runtime Monitoring works as expected across your organization.

If you have set up one or more service control policies to manage permissions in your organization, you must validate that it doesn't deny the `guardduty:SendSecurityTelemetry` action. For information about how SCPs work, see [SCP evaluation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_evaluation.html) in the *AWS Organizations User Guide*.

If your account is a member account, contact the associated delegated administrator. For information about managing SCPs for your organization, see [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide*.

Perform the following steps for all the SCPs that you have set up in your multi-account environment:

**To validate `guardduty:SendSecurityTelemetry` is not denied in SCP**

1. Sign in to the Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/). You must sign in as an IAM role, or sign in as the root user [(not recommended)](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials) in the organization's management account.

1. In the left navigation pane, select **Policies**. Then, under **Supported policy types**, select **Service control policies**.

1. On the **Service control policies** page, choose the name of the policy that you want to validate.

1. On the policy's detail page, view the **Content** of this policy. Make sure that it doesn't deny the `guardduty:SendSecurityTelemetry` action.

   The following SCP policy is an example for *not denying* the `guardduty:SendSecurityTelemetry` action:

------
#### [ JSON ]

****  

   ```
   {
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
   }
   ```

------

   If your policy denies this action, you must update the policy. For more information, see [Update a service control policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_update.html#update_policy) in the *AWS Organizations User Guide*.

## Validating role permissions and policy permissions boundary
<a name="guardduty-runtime-monitoring-ecs-permission-boundary"></a>

Use the following steps to validate that the permissions boundaries associated with the role and its policy **doesn't** restrict `guardduty:SendSecurityTelemetry` action.

**To view permissions boundary for roles and its policy**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, under **Access management**, choose **Roles**.

1. On the **Roles** page, select the role {{`TaskExecutionRole`}} that you may have created.

1. On the selected role's page, under the **Permissions** tab, expand the policy name associated with this role. Then, validate that this policy doesn't restrict `guardduty:SendSecurityTelemetry`.

1. If the **Permissions boundary** is set, then expand this section. Then, expand each policy to review that it doesn't restrict the `guardduty:SendSecurityTelemetry` action. The policy should appear similar to this [Example SCP policy](#ecs-runtime-scp-not-deny-policy-example).

   As needed, perform one of the following actions:
   + To modify the policy, select **Edit**. On the **Modify permissions** page for this policy, update the policy in the **Policy editor**. Make sure that the JSON schema remains valid. Then, choose **Next**. Then, you can review and save the changes.
   + To change this permissions boundary and choose another boundary, choose **Change boundary**.
   + To remove this permissions boundary, choose **Remove boundary**.

   For information about managing policies, see [Policies and permissions in AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.

## CPU and memory limits
<a name="ecs-runtime-agent-cpu-memory-limits"></a>

In the Fargate task definition, you must specify the CPU and memory value at the task level. The following table shows the valid combinations of task-level CPU and memory values, and the corresponding GuardDuty security agent maximum memory limit for the GuardDuty container.



- **256 (.25 vCPU)**
  - **Memory value:** 512 MiB, 1 GB, 2GB
  - **GuardDuty agent maximum memory limit:** 128 MB

- **512 (.5 vCPU)**
  - **Memory value:** 1 GB, 2 GB, 3 GB, 4 GB

- **1024 (1 vCPU)**
  - **Memory value:**
    - 2 GB, 3 GB, 4 GB
    - 5 GB, 6 GB, 7 GB, 8 GB

- **2048 (2 vCPU)**
  - **Memory value:** Between 4 GB and 16 GB in 1 GB increments

- **4096 (4 vCPU)**
  - **Memory value:** Between 8 GB and 20 GB in 1 GB increments

- **8192 (8 vCPU)**
  - **Memory value:** Between 16 GB and 28 GB in 4 GB increments / **GuardDuty agent maximum memory limit:** 256 MB
  - **Memory value:** Between 32 GB and 60 GB in 4 GB increments / **GuardDuty agent maximum memory limit:** 512 MB

- **16384 (16 vCPU)**
  - **Memory value:** Between 32 GB and 120 GB in 8 GB increments
  - **GuardDuty agent maximum memory limit:** 1 GB



After you enable Runtime Monitoring and assess that the coverage status of your cluster is **Healthy**, you can set up and view the Container insight metrics. For more information, see [Setting up monitoring on Amazon ECS cluster](runtime-monitoring-setting-cpu-mem-monitoring.md#ecs-runtime-cpu-memory-monitoring-agent).

The next step is to configure Runtime Monitoring and also configure the security agent.
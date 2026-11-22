

# Run virtual machines in agents on Runtime Instances

Nested virtualization is a capability of the **Instances** compute type of AgentCore Runtime. With nested virtualization, you can give your agents access to hardware virtualization with Kernel-based Virtual Machine (KVM) on their instance. Your agents can then run their own virtual machines and hardware-accelerated emulators inside a session. For example, an agent can run Android emulators to build, test, and automate mobile apps, or run lightweight virtual machines to sandbox the code that it runs.

You turn on nested virtualization on the capacity provider. Every instance that the capacity provider launches then exposes the KVM device, `/dev/kvm`, to the agents that run on it.

**Topics**
+ [Requirements](#runtime-instances-nested-virtualization-requirements)
+ [Create a capacity provider with nested virtualization](#runtime-instances-nested-virtualization-create)
+ [How agents use the KVM device](#runtime-instances-nested-virtualization-agents)

## Requirements
<a name="runtime-instances-nested-virtualization-requirements"></a>

To turn on nested virtualization, your capacity provider needs the following:
+ The `LINUX_X86_64` operating system.
+ Allowed instance types that all come from families that support nested virtualization. You can use instance types from the following families:
  + General purpose – `m7i`, `m8i`, and `m8id` 
  + Compute optimized – `c7i`, `c8i`, and `c8id` 
  + Memory optimized – `r7i`, `r7iz`, `r8i`, and `r8id` 

For more information about nested virtualization on Amazon EC2, see [Nested virtualization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nested-virtualization.html) in the *Amazon EC2 User Guide*.

You set nested virtualization when you create the capacity provider. You can’t turn it on or off for an existing capacity provider. To change it, create a new capacity provider and update your agent runtimes to use it.

## Create a capacity provider with nested virtualization
<a name="runtime-instances-nested-virtualization-create"></a>

Before you begin, you need the following:
+ The IAM roles and the VPC configuration for a capacity provider. For more information, see [Get started with Instances](runtime-instances-getting-started.md).
+ Permission to call `bedrock-agentcore:CreateCapacityProvider`.

To create a capacity provider whose instances support nested virtualization, complete the following steps:

1. Run `create-capacity-provider` with `nestedVirtualization` set to `ENABLED` in the `cpuOptions` of `launchParameters`. The following AWS CLI command creates a capacity provider with nested virtualization turned on:

   ```bash
   aws bedrock-agentcore-control create-capacity-provider \
     --name "my_kvm_capacity_provider" \
     --permissions-configuration '{
       "capacityProviderOperatorRoleArn": "arn:aws:iam::111122223333:role/AgentCoreCapacityProviderOperatorRole"
     }' \
     --compute-configuration '{
       "ec2Configuration": {
         "launchTemplateSource": {
           "launchParameters": {
             "operatingSystem": "LINUX_X86_64",
             "instanceRequirements": {
               "allowedInstanceTypes": ["c8i.2xlarge", "m8i.2xlarge"]
             },
             "cpuOptions": {
               "nestedVirtualization": "ENABLED"
             }
           }
         },
         "vpcConfiguration": {
           "subnets": ["subnet-1234567890abcdef0"],
           "securityGroups": ["sg-1234567890abcdef0"]
         }
       }
     }' \
     --region us-west-2
   ```

   In the example, replace these values with your own:
   +  `my_kvm_capacity_provider` – The name of the capacity provider.
   +  `arn:aws:iam::111122223333:role/AgentCoreCapacityProviderOperatorRole` – The ARN of the infrastructure role.
   +  `c8i.2xlarge` and `m8i.2xlarge` – The instance types that your agents run on.
   +  `subnet-1234567890abcdef0` and `sg-1234567890abcdef0` – Your subnet and security group.

1. Create or update an agent runtime that uses the capacity provider. For more information, see [Get started with Instances using the AWS CLI](runtime-instances-get-started-cli.md).

When an agent starts in a new session of the agent runtime, `/dev/kvm` is available to it.

If the request fails with a `ValidationException`, check the error message:
+  `Nested virtualization is supported only with the LINUX_X86_64 operating system.` – Set `operatingSystem` to `LINUX_X86_64`.
+  `Instance type '<type>' (family '<family>') does not support nested virtualization.` – Remove the instance type from `allowedInstanceTypes`, or replace it with an instance type from a supported family.

## How agents use the KVM device
<a name="runtime-instances-nested-virtualization-agents"></a>

Agents use `/dev/kvm` the same way that they would on any Linux host with KVM. For example, an agent can start a virtual machine with QEMU and KVM acceleration, or start an Android emulator with hardware acceleration.
+  **Container agents** – AgentCore adds `/dev/kvm` to the container, with read and write access. In `STANDARD` mode, the container keeps its other restrictions, so the agent doesn’t need elevated privileges to use the device. In `PRIVILEGED` mode, the container already has access to all devices on the instance, including `/dev/kvm`. For more information, see [Configure the privilege mode for Runtime Instances](runtime-instances-privilege-mode.md).
+  **Direct code agents** – The agent process opens `/dev/kvm` on the instance directly.

All agents in a session share the virtualization capacity of the instance. The virtual machines that an agent starts use the vCPUs and memory of the instance, so choose instance types with enough capacity for your agents and their virtual machines.

The virtual machines run inside the instance. The Amazon EC2 instance remains the isolation unit, and nested virtualization doesn’t give agents access to other sessions or instances. For more information, see [Security model and permissions for Runtime Instances](runtime-instances-security.md).
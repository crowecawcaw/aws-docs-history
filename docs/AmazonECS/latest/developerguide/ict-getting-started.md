

# Getting started
<a name="ict-getting-started"></a>

Isolated and confidential tasks are a trusted execution capability of Amazon ECS Managed Instances that gives each task its own hardware-isolated Nitro Sandbox. This section walks you through enabling them.

## Prerequisites
<a name="ict-prerequisites"></a>

Before you begin, make sure you have the following:
+ An Amazon ECS cluster that uses an Amazon ECS Managed Instances capacity provider. Isolated and confidential tasks are supported only for Amazon ECS Managed Instances; they are not available with the Amazon EC2 or Fargate launch types.
+ A capacity provider whose `InstanceLaunchTemplate` sets `nitroEnclavesEnabled` to `true`. With this setting, you can launch instances that run tasks in the `ISOLATED_SANDBOX` or `CONFIDENTIAL_SANDBOX` isolation mode. For more information about enabling Nitro Sandbox on the capacity provider, see [Enabling Nitro Sandbox on the capacity provider](#ict-enable-nitro-sandbox-on-the-capacity-provider).
+ Tasks must use the `awsvpc` network mode. The `host` network mode is not supported. For more information, see [Considerations and limitations](ict-considerations-and-limitations.md).
+ For confidential tasks: an AWS KMS key whose key policy requires attestation, and the task IAM role permissions needed to call AWS KMS.

## Enabling Nitro Sandbox on the capacity provider
<a name="ict-enable-nitro-sandbox-on-the-capacity-provider"></a>

Isolated and confidential tasks run only on instances launched with Nitro Sandbox enabled. Set `nitroEnclavesEnabled` to `true` in the capacity provider's `InstanceLaunchTemplate`. The default value is `false`.

When you enable this setting:
+ The capacity provider must include at least one instance type that supports Nitro Sandbox.
+ You cannot enable it together with local storage (the `useLocalStorage` setting in `localStorageConfiguration`).

## Enabling isolated tasks
<a name="ict-enable-isolated-tasks"></a>

To enable task isolation, set `isolationMode` to `ISOLATED_SANDBOX` in the task definition's `trustedExecutionConfiguration` when you register the task definition. Then launch services or standalone tasks on Amazon ECS Managed Instances as usual.

Amazon ECS automatically launches compatible Amazon EC2 instances, provisions a fully configured Bottlerocket operating system image, and places tasks in isolated environments. No changes to your application code are required. From the workload's perspective, the environment looks like a normal Linux container.

Amazon ECS Managed Instances always run through a capacity provider. When the capacity provider has Nitro Sandbox enabled, Amazon ECS automatically launches and configures compatible instances for isolated and confidential tasks.

## Enabling confidential tasks
<a name="ict-enable-confidential-tasks"></a>

To enable confidential tasks, set `isolationMode` to `CONFIDENTIAL_SANDBOX` in the task definition's `trustedExecutionConfiguration`, and supply an `attestationPolicy`. The `attestationPolicy` is the base64-encoded attestation policy envelope for the task; it specifies which containers are allowed to run and the runtime configuration that is cryptographically attested. This parameter is **required** to run a confidential task. For more information, see [Confidential policy configuration](ict-confidential-policy-configuration.md).

Amazon ECS automatically selects compatible instance types for isolated and confidential tasks. The same instance types support both isolation and attestation, so no additional instance selection is required when you enable confidential mode. For the full list, see [Considerations and limitations](ict-considerations-and-limitations.md).

After the task launches, confirm its isolation mode and attestation status in the read-only `trustedExecutionSummary` on the task.

### How attestation works
<a name="ict-how-attestation-works"></a>

Each task can use NSM to generate a cryptographic attestation document. At environment launch, the ECS sandbox agent measures the environment and stores the resulting values in Platform Configuration Registers (PCRs). To decrypt data, your application retrieves the attestation document and submits it to AWS KMS as part of the decrypt request. The Nitro System signs the document, and AWS KMS compares the measurements it contains against the expected PCR values in your KMS key policy. Your application does not perform the comparison; it only forwards the attestation document. KMS releases the key material only when the measurements match.

**Important**  
Attestation measurement alone is passive: it records what is running, but does not by itself prevent a modified configuration from being accepted. The trust loop is closed only when an external verifier (AWS KMS) checks the attestation document before releasing secrets. Always configure your KMS key policy to require attestation on any key that protects confidential data. For more information about the security model and policy configuration, see [Security model](ict-security-model.md) and [Confidential policy configuration](ict-confidential-policy-configuration.md).

## What happens when a task starts
<a name="ict-what-happens-when-a-task-starts"></a>

When Amazon ECS schedules an isolated or confidential task on a Managed Instance:

1. Amazon ECS creates a dedicated Nitro Sandbox for the task.

1. Amazon ECS loads the container images into the sandbox.

1. If the task has an attestation policy, the ECS sandbox agent evaluates the policy (required for confidential tasks).

1. The containers start inside the sandbox.

Each task gets its own Nitro Sandbox. Multiple containers within the same task share a single sandbox.

After the task launches, confirm its isolation mode and attestation status in the read-only `trustedExecutionSummary` on the task.

## Reading a task's isolation configuration
<a name="ict-read-a-tasks-isolation-configuration"></a>

After a task launches, you can see its isolation configuration through the read-only `trustedExecutionSummary` on the task, without calling `DescribeTaskDefinition`. `DescribeTasks`, `RunTask`, and `StopTask` return the summary, which contains the `isolationMode` and the `attestationPolicyStatus`. For more information about the task's isolation summary, see [TrustedExecutionSummary](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TrustedExecutionSummary.html) in the *Amazon ECS API Reference*.

## CPU and memory configuration
<a name="ict-cpu-and-memory-configuration"></a>

Specify CPU and memory at the task level. You specify CPU in units, where 1,024 units equal 1 vCPU, up to 256 vCPUs, and you can use fractional vCPUs. You can also leave the task-level CPU value unset (0/null); a task with no CPU value is not pinned to a share and can burst across the host's available cores; this is the mechanism for CPU oversubscription, described later in this section. Memory is independent of CPU, from a minimum of 4 MiB up to the maximum the Amazon EC2 instance supports.

Amazon ECS reserves memory for each isolated environment to run the Linux kernel, the microVM, containerd, and the ECS sandbox agent. This reservation means your application does not compete for system memory.

**CPU oversubscription.** For burstable workloads, such as JVM applications that need extra CPU at startup, you can oversubscribe CPU by leaving the task-level CPU value unset. Tasks without a set CPU value share the host's cores and can burst up to the instance's available capacity.

The Amazon ECS Managed Instances capacity provider controls the oversubscription factor (up to 5 times for each vCPU). This is a coarse control. There is no per-task CPU "reservation" or "limit", so leaving CPU unset is the only way to oversubscribe. It does not let you set a per-task oversubscription level.

No oversubscription (an explicit CPU value) provides native Amazon EC2 CPU performance; higher factors trade CPU performance for density. CPU credits (the T-instance burst model) are not supported.

## Networking
<a name="ict-networking"></a>

Isolated and confidential tasks use the `awsvpc` network mode. Each task gets a dedicated elastic network interface (ENI) with a private IP address, which ensures network-level isolation. The `host` network mode is not supported, because it requires sharing the host network stack, which conflicts with task isolation.

Isolated and confidential tasks retain per-task security groups, VPC Flow Logs, and integrations with Application Load Balancer, Network Load Balancer, and VPC Lattice. Amazon ECS Service Connect is not supported. For more information, see [Considerations and limitations](ict-considerations-and-limitations.md).

## Pricing
<a name="ict-pricing"></a>

There is no additional fee for isolated and confidential tasks. You pay for the underlying Amazon EC2 instances and the standard Amazon ECS management fee. There is no premium charge.

## Next steps
<a name="ict-getting-started-next-steps"></a>
+ [Security model](ict-security-model.md) – Understand the trust boundary and what the parent instance can and cannot do.
+ [Encrypted container images](ict-encrypted-container-images.md) – Encrypt container images so the parent instance never sees plaintext image contents.
+ [Confidential policy configuration](ict-confidential-policy-configuration.md) – Configure the policy that governs a confidential task.
+ [Considerations and limitations](ict-considerations-and-limitations.md) – Review behavioral differences, supported instance types, and resource limits.
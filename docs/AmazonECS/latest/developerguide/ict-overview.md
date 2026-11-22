

# Overview

This section explains what isolated and confidential tasks are, how they work, and how the two isolation modes differ, so you can decide which one fits your workload.

## What are isolated and confidential tasks?
<a name="ict-what-are-isolated-and-confidential-tasks"></a>

In a standard Amazon ECS Managed Instances deployment, multiple tasks can run on the same Amazon EC2 instance, where they share the host's Linux kernel. That shared kernel is also a shared attack surface: a container escape or a kernel vulnerability in one task can expose the memory, processes, or data of other tasks on the same instance.

Isolated and confidential tasks close that gap. Each task runs in its own Nitro Sandbox — a lightweight virtual machine with its own kernel — so a compromise in one task can't reach another task on the same instance. You get this stronger boundary while still bin-packing multiple tasks onto one instance for cost efficiency.

The relationship between a sandbox and its parent instance depends on the isolation mode:
+ In isolated mode (`ISOLATED_SANDBOX`), the goal is to isolate tasks from one another on a shared instance. Each task runs in its own Nitro Sandbox, so a compromised task can't reach the memory or storage of another task, and can't escape to the parent instance. The parent instance is trusted and retains observability and control over the task, such as task exec and log streaming.
+ In confidential mode (`CONFIDENTIAL_SANDBOX`), the parent instance is untrusted. The Nitro Hypervisor prevents the parent from observing the CPU or memory state of the sandbox, and attestation-gated key release ensures the parent cannot obtain the secrets the workload uses. Use confidential mode when your workload's data must stay confidential even from the account or operator running the instance.

Each sandbox runs as a first-level guest with direct hardware-assisted virtualization. The Nitro Hypervisor enforces memory and CPU isolation between sandboxes, providing a hardware trust boundary around every task.

Isolated and confidential tasks are opt-in. You select the feature per task through the task definition's `trustedExecutionConfiguration` and a capacity provider setting; isolation requires no application code changes. Tasks that do not set an isolation mode use the default `SHARED` mode and continue to run on a shared container runtime.

This approach lets you securely colocate multiple tenants or workloads on one Managed Instance while optimizing cost through bin-packing. It helps you align with compliance frameworks that require verifiable data-in-use protection and confidential computing.

Isolated and confidential tasks provide the equivalent VM-level, per-task isolation to AWS Fargate. Unlike Fargate, the tasks run on Amazon ECS Managed Instances in your own account with the broader set of Amazon EC2 capabilities, including the ability to select specific instance types, to run multiple tasks per instance, and to use Capacity Reservations.

## How it works
<a name="ict-how-it-works"></a>

When you enable isolation, Amazon ECS places each task in its own lightweight VM inside an Amazon EC2 instance. The Nitro Hypervisor manages these environments and enforces the isolation boundary between tasks that run on the same instance.

Amazon ECS automatically launches compatible Amazon EC2 instances and provisions a fully configured Bottlerocket operating system image. The ECS sandbox agent (the Amazon ECS agent that runs inside the Nitro Sandbox) and managed components run inside each isolated environment rather than being shared across tasks.

## Isolated tasks compared to confidential tasks
<a name="ict-isolated-tasks-compared-to-confidential-tasks"></a>

You select the type of task through the `isolationMode` field of the task definition's `TrustedExecutionConfiguration`. The `IsolationMode` enum has three values:
+ `SHARED` – The task shares the underlying Amazon EC2 instance with other tasks. This is the default isolation mode and uses the standard shared container runtime.
+ `ISOLATED_SANDBOX` (isolated tasks) – The parent instance is trusted and the guest is untrusted. The goal is to protect the node and other tasks from a compromised workload. The task runs in its own Nitro Sandbox, a lightweight virtual machine isolated by the AWS Nitro System, so one task cannot access another task's memory or storage on the same Amazon EC2 instance. The parent instance retains observability and control (task exec is permitted), and any valid container spec is accepted.
+ `CONFIDENTIAL_SANDBOX` (confidential tasks) – The parent instance is untrusted and the guest is the trust boundary. The goal is to protect the workload's data from the node operator or a compromised parent instance. The task runs in its own Nitro Sandbox with cryptographic attestation: the parent cannot access the sandbox's memory or storage, and only the approved workload can decrypt data that you encrypt with your AWS KMS key. When you use this mode, you must supply an `attestationPolicy` in the `TrustedExecutionConfiguration` and gate AWS KMS access on attestation. For more information, see [Confidential policy configuration](ict-confidential-policy-configuration.md).

## Key features
<a name="ict-key-features"></a>

**Nitro Sandbox isolation.** Each task runs in its own Nitro Sandbox. The AWS Nitro Hypervisor enforces memory and CPU isolation between sandboxes on the same parent instance. A compromised container cannot access memory or storage belonging to another task, and the parent instance cannot observe the CPU or memory state of the sandbox.

**Cryptographic attestation (confidential tasks).** Attestation lets you prove that a Nitro Sandbox is running exactly the code you expect before releasing secrets to it. Each task can use Nitro Security Module (NSM) to generate a cryptographic attestation document. At environment launch, the ECS sandbox agent measures the environment and stores the resulting values in Platform Configuration Registers (PCRs). To decrypt data, your application retrieves the attestation document; the Nitro System signs the document and AWS KMS compares it against the expected PCR values. Amazon ECS provides a tool that generates the expected PCR values for the task. Attestation alone does not enforce anything; a third-party verifier such as AWS KMS must check the measurements before releasing secrets. For more information about attestation, see [Confidential policy configuration](ict-confidential-policy-configuration.md) and [Security model](ict-security-model.md).

**Encrypted container images.** Container image layers can be encrypted following the Open Container Initiative (OCI) image encryption specification. The Nitro Sandbox decrypts encrypted layers using AWS KMS. If you configured the task with an attestation policy, the sandbox automatically generates the attestation document that AWS KMS compares with the expected PCR values. The parent instance transfers the encrypted blobs but never accesses the plaintext image contents. The attestation policy ensures the parent can't access the image after it has been decrypted inside the sandbox. For more information about encrypted container images, see [Encrypted container images](ict-encrypted-container-images.md).

**Shared responsibility.** AWS is responsible for the Nitro Hypervisor, the Nitro Sandbox boundary, and the guest system image. You are responsible for your container images, task definitions, AWS KMS key policies, and application code. For more information about the security model, see [Security model](ict-security-model.md).

## Credentials and instance metadata
<a name="ict-credentials-and-instance-metadata"></a>

Tasks running in a Nitro Sandbox cannot reach services in the parent instance's network directly. The sandbox provides local surrogates for instance metadata and task credentials so that workloads behave the same as tasks running on a standard Managed Instance. The surrogates can be accessed in the same way as regular ECS tasks.

### Instance metadata
<a name="ict-instance-metadata"></a>

The Nitro Sandbox exposes the Amazon ECS task metadata endpoint and an IMDSv2-only metadata surrogate. Workloads that use the AWS SDKs or query metadata for region and placement information work without changes. The metadata surrogate serves only placement metadata (Region, Availability Zone, and Availability Zone ID) and service endpoint metadata (service domain and partition). All other paths return a 404 response. IMDSv1 (tokenless) requests are rejected.

### Task IAM roles
<a name="ict-task-iam-roles"></a>

Tasks in Nitro Sandboxes access AWS credentials through the task IAM role and the task execution IAM role, the same way as regular ECS tasks. The task credential endpoint is available inside the sandbox and returns credentials for the task's IAM role. You don't need additional configuration. If your task definition specifies a task role, it works in a Nitro Sandbox without changes.

## Storage
<a name="ict-storage"></a>

Tasks running in Nitro Sandboxes support several storage options. The Nitro Sandbox handles each volume type differently depending on whether the storage is a block device, a network filesystem, or host-populated content.

### Ephemeral storage and image caching
<a name="ict-ephemeral-storage-and-image-caching"></a>

Each task gets 20 GiB of ephemeral storage. This value is not configurable with the `ephemeralStorage` task definition parameter. Amazon ECS encrypts ephemeral storage at rest with AES-256 using Amazon EBS encryption. Amazon ECS stores the pulled, compressed, and uncompressed container image on ephemeral storage, and the remainder is available to the task.

Amazon ECS caches container images and offers a cached image to the next task of the same task definition only; it never offers other cached images. This behavior preserves isolation between tasks.

To support ephemeral storage, Amazon ECS attaches Amazon EBS volumes to the Nitro Sandbox as raw block devices. The per-instance Amazon EBS data volume defaults to 80 GiB and is configurable in the capacity provider (minimum 30 GiB, maximum 16,384 GiB), consistent with existing Amazon ECS Managed Instances storage configuration. Amazon ECS attaches an Amazon EBS volume for each instance. All tasks on an instance share the volume throughput and IOPS; there is no isolation-specific performance impact.

### Using Amazon EBS volumes
<a name="ict-amazon-ebs-volumes"></a>

Attaching an Amazon EBS volume to an individual task is not supported, including task definition volumes that set `configuredAtLaunch` to `true`. For shared read-write persistent storage across tasks, use Amazon EFS instead. For more information about storage considerations, see [Considerations and limitations](ict-considerations-and-limitations.md).

### Amazon EFS volumes
<a name="ict-amazon-efs-volumes"></a>

Amazon EFS provides shared read-write persistent storage across tasks. The Nitro Sandbox performs the Network File System (NFS) mount and terminates TLS, so the parent instance does not sit on the data path. Data stored on Amazon EFS is not protected from the parent instance, which can mount the same filesystem out of band with its own IAM identity. Do not write confidential data to Amazon EFS unless your application encrypts it first. For more information, see [Security model](ict-security-model.md).

## Next steps
<a name="ict-overview-next-steps"></a>

To get started, see [Getting started](ict-getting-started.md).
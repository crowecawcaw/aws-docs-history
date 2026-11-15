

# Considerations and limitations
<a name="ict-considerations-and-limitations"></a>

Consider the following when you run isolated and confidential tasks.

## Behavioral considerations
<a name="ict-behavioral-considerations"></a>
+ **No application changes** – You do not need application changes unless you use attestation. Isolated and confidential tasks use the same container runtime as regular Amazon ECS Managed Instances.
+ **Supported integrations** – You can attach Amazon EFS storage, route traffic through Elastic Load Balancing and VPC Lattice, and use native Amazon ECS deployments. Most Amazon ECS Managed Instances capabilities work the same way.
+ **Managed daemons** – Amazon ECS runs managed daemons in the parent. These agents have access to the EC2 host and tasks running in `SHARED` isolation mode on the EC2 instance. They do not have access to isolated and confidential tasks running inside Nitro Sandboxes.
+ **Privileged capabilities** – Privileged Linux capabilities apply only to the Linux operating system stack inside the Nitro Sandbox, not to the host. For example, an eBPF application inspects only traffic to and from that Nitro Sandbox.
+ **Patching** – Amazon ECS patches Amazon ECS Managed Instances by launching new Amazon EC2 instances with patched AMIs, shifting traffic, and draining old instances. Amazon ECS updates the OS and managed components that run inside the sandbox together with the host Amazon EC2 AMI patching.

## Networking
<a name="ict-considerations-networking"></a>
+ Isolated and confidential tasks require the `awsvpc` network mode. Each task gets a dedicated elastic network interface (ENI) with a private IP address.
+ The `host` network mode is not supported. It requires sharing the host network stack, which conflicts with task isolation.
+ Per-task security groups, VPC Flow Logs, and integrations with Application Load Balancer, Network Load Balancer, and VPC Lattice are retained.
+ Amazon ECS Service Connect is not supported.

## Capacity provider requirements
<a name="ict-capacity-provider-requirements"></a>
+ **Enable Nitro Sandbox on the capacity provider** – Set `nitroEnclavesEnabled` to `true` in the capacity provider's `InstanceLaunchTemplate` to launch instances that can run `ISOLATED_SANDBOX` or `CONFIDENTIAL_SANDBOX` tasks. The default is `false`.
+ **At least one supporting instance type** – When `nitroEnclavesEnabled` is `true`, the capacity provider must include at least one instance type that supports Nitro Sandbox.
+ **Not compatible with local storage** – You cannot enable `nitroEnclavesEnabled` together with local storage (the `useLocalStorage` setting in `localStorageConfiguration`).
+ **Managed Instances only** – Isolated and confidential tasks are supported only for Amazon ECS Managed Instances.

## Storage
<a name="ict-considerations-storage"></a>
+ **Ephemeral storage** – Each task gets 20 GiB of ephemeral storage. Ephemeral storage is backed by Amazon EBS and is encrypted at rest with AES-256 using Amazon EBS encryption.
+ **Per-instance Amazon EBS data volume** – Defaults to 80 GiB and is configurable in the capacity provider. The minimum size is 30 GiB and the maximum size is 16,384 GiB.
+ **Amazon EBS volumes attached to tasks** – Attaching an Amazon EBS volume to an individual task is not supported, including task definition volumes that set `configuredAtLaunch` to `true`.
+ **Ephemeral storage performance** – Matches equivalent Amazon EBS performance. Amazon ECS attaches an Amazon EBS volume for each instance. All tasks on an instance share the volume throughput and IOPS. There is no isolation-specific performance impact.
+ **Image caching** – Amazon ECS offers a cached container image only to the next task of the same task definition, and never offers other cached images. This preserves isolation between tasks.

## CPU, memory, and oversubscription
<a name="ict-cpu-memory-and-oversubscription"></a>
+ Specify a CPU and memory value at the task level. You specify CPU in units (1,024 units = 1 vCPU), up to 256 vCPUs, and you can use fractional vCPUs. Memory is independent of vCPU, from 4 MiB up to the maximum the Amazon EC2 instance supports.
+ Amazon ECS reserves additional memory for each isolated environment for the Linux kernel, the microVM, containerd, and the ECS sandbox agent, on top of the memory you request for the task. For example, a task with 2 vCPU and 8 GiB of memory has a total memory footprint of about 8.7 GiB on the instance, so about 7 such tasks fit on an `m7i.4xlarge` (16 vCPU, 64 GiB).

## CPU scheduling on SMT instances
<a name="ict-smt-core-scheduling"></a>

On instances that use simultaneous multithreading (SMT), each physical core presents two vCPUs as sibling hardware threads. For security, the Nitro Sandbox runtime uses core scheduling so that two different sandboxes never run on the two sibling threads of the same physical core at the same time, which prevents cross-sandbox side-channel leakage. When two sandboxes share a core, they cannot use their vCPUs at the same time, so on an SMT instance the compute available to sandboxed tasks is bounded by the number of physical cores, roughly half the instance's advertised vCPUs. For example, on a 4-vCPU Intel instance (two physical cores), four tasks that each request one vCPU are placed two to a core. Because the two sandboxes sharing a core can't run at the same time, only about two of the four requested vCPUs are active at once – roughly half the instance's advertised vCPUs.

This applies to instance types with two threads per physical core, including most Intel instances and SMT-enabled AMD instances. Instance types with a single thread per core, such as AWS Graviton (Arm) instances, are not subject to it. To check an instance type, call the [DescribeInstanceTypes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceTypes.html) API and read the `DefaultThreadsPerCore` value: 1 is a single thread per core, and 2 is SMT.

To get full performance, size each task to a whole physical core. On a two-thread-per-core instance, request CPU in multiples of two vCPUs so that a single sandbox owns both sibling threads of each core it uses; threads within one sandbox can run at the same time because they share a trust domain. Alternatively, run on instance types with one thread per core, such as AWS Graviton, where each vCPU is already a full physical core.

## GPU support
<a name="ict-gpu-support"></a>

Isolated and confidential tasks do not support GPUs. You can use GPUs on select GPU instances, but only tasks that run in `SHARED` isolation mode have access to GPUs.

## Supported instance types
<a name="ict-supported-instance-types"></a>

Isolation is available on most Nitro-based instance types that Amazon ECS Managed Instances qualifies, from the 5th-generation families and later. Isolation does not support burstable performance instances, which include the T family and -flex instance types.

Isolated and confidential tasks require instance types that support AWS Nitro Enclaves. For more information about supported instance types, see [AWS Nitro Enclaves](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html).

## Pricing
<a name="ict-considerations-pricing"></a>

There is no additional fee for isolated and confidential tasks. You pay for the underlying Amazon EC2 instances and the standard Amazon ECS management fee. There is no premium charge.
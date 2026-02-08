# How AgentCore Tools session isolation works

Amazon Bedrock AgentCore Tools provide Code Interpreter and Browser capabilities that enable AI
agents to execute code and interact with web content in secure, isolated environments. This
page describes the session isolation architecture that ensures complete separation between
customer requests through the use of Firecracker microVMs.

## Session isolation overview

Amazon Bedrock AgentCore Tools implement a strict one-session-one-microVM isolation model. When
you invoke a Code Interpreter or Browser session, the service provisions a dedicated
Firecracker microVM that executes exclusively for that session. The microVM runs the
requested operations, returns the results to your application, and is then completely
terminated when requested by user. This architecture ensures that no execution state,
filesystem artifacts, or memory contents persist between sessions.

Each microVM operates as an independent virtual machine with its own Linux kernel, memory
space, and network namespace. The service does not share execution environments across
sessions, nor does it reuse microVMs after they complete their designated work. Upon session
termination, the service destroys all session-specific resources including the writable
filesystem layer, in-memory state, and network configurations.

## Why session isolation is critical for Amazon Bedrock AgentCore Tools

Amazon Bedrock AgentCore Tools enable isolation of each user session and safe reuse of context
across multiple invocations within a user session. Session isolation is critical for Code
Interpreter and Browser workloads due to their unique operational characteristics:

Complete execution environment separation

Each user session receives its own dedicated microVM with isolated compute, memory,
and filesystem resources. This prevents one user's code execution or browser activity
from accessing another user's data. After session completion, the entire microVM is
terminated and memory is sanitized to remove all session data, eliminating cross-session
contamination risks.

Stateful tool operations

Unlike stateless function invocations, Amazon Bedrock AgentCore Tools maintain complex
contextual state throughout their execution cycle. Code Interpreter sessions preserve
variables, imported libraries, and generated artifacts across multiple code executions
within the same session. Browser sessions maintain cookies, local storage, and page
navigation history. The isolation architecture preserves this state securely within a
session while ensuring complete separation between different users, enabling continuity
of tool operations without compromising data boundaries.

Privileged tool operations

Amazon Bedrock AgentCore Tools perform operations that require elevated privileges and
access to sensitive resources. Code Interpreter executes arbitrary code with filesystem
access and network connectivity. Browser navigates to external websites and handles
authentication credentials. The isolation model ensures these tool operations maintain
proper security contexts and prevents credential sharing or permission escalation
between different user sessions.

Deterministic security for non-deterministic processes

Tool execution patterns can vary based on the code being run or websites being
accessed. Amazon Bedrock AgentCore Tools provide consistent, deterministic isolation boundaries
regardless of tool execution patterns, delivering the predictable security properties
required for enterprise deployments.

###### Note

Amazon Bedrock AgentCore Tools do not enforce session-to-user mappings. Your application
backend should maintain the relationship between users and their session IDs. Additionally,
your application backend should implement logic for user to session lifecycle management
such as maximum number of sessions per user.

## Firecracker microVM architecture

Firecracker is an open-source virtualization technology developed by AWS that creates
lightweight virtual machines with strong security properties. Firecracker leverages the
Kernel-based Virtual Machine (KVM) hypervisor to provide hardware-level isolation while
maintaining minimal resource overhead and fast startup times.

Firecracker enables you to deploy workloads in lightweight virtual machines, called
microVMs, which provide enhanced security and workload isolation over traditional VMs, while
enabling the speed and resource efficiency of containers. Firecracker was developed to
improve the customer experience of services like Lambda, and now Amazon Bedrock AgentCore.

Firecracker is a virtual machine monitor (VMM) that uses the Linux Kernel-based Virtual
Machine (KVM) to create and manage microVMs. Firecracker has a minimalist design. It excludes
unnecessary devices and guest functionality to reduce the memory footprint and attack surface
area of each microVM. This improves security, decreases the startup time, and increases
hardware utilization.

Firecracker provides multi-layered security isolation through Linux KVM virtualization
combined with process-level constraints including seccomp filters, cgroups, namespaces, and
privilege dropping. Seccomp filters automatically restrict Firecracker to only essential
system calls needed for operation, loaded per-thread before executing guest code. The jailer
process establishes privileged resources (cgroups, chroot), then drops privileges before
exec'ing into Firecracker, ensuring it runs unprivileged with access only to explicitly
granted resources. Cgroups enable resource isolation by pinning microVMs to specific CPU
nodes via cpuset and guaranteeing fair CPU time allocation through dedicated quotas,
preventing performance degradation from migration and resource contention.

### Additional resources

For more information about Firecracker and the underlying technologies used in
Amazon Bedrock AgentCore Tools:

- Firecracker GitHub repository: [https://github.com/firecracker-microvm/firecracker](https://github.com/firecracker-microvm/firecracker "https://github.com/firecracker-microvm/firecracker")
- Firecracker design documentation: [https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md](https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md "https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md")
- AWS security best practices: [https://aws.amazon.com/security/](https://aws.amazon.com/security/ "https://aws.amazon.com/security/")



# Security model
<a name="ict-security-model"></a>

This section describes the trust boundaries of isolated and confidential tasks — what the parent instance controls, what it cannot observe, and the assumptions your workload should make.

## Overview
<a name="ict-security-model-overview"></a>

Isolated and confidential tasks run your workload inside a Nitro Sandbox, which provides hardware-enforced isolation from the parent instance. However, the parent instance still controls resources that the sandbox depends on: CPU, memory, network, and storage. This page describes what the parent instance can and cannot do, and what assumptions your workload code should make.

## Trust boundary and supported inputs
<a name="ict-trust-boundary-and-supported-inputs"></a>

Isolated and confidential tasks treat the Nitro Sandbox as the security boundary. The feature is designed to run untrusted container images: the binaries, libraries, and scripts that execute inside the container can come from an untrusted source, and the sandbox contains them so a compromised workload cannot reach the parent instance or other tasks. It is not designed to run untrusted task definitions.

The task definition and the attestation policy generated from it are trusted inputs. This includes the container image references, `command` and container entry point, environment variables, volumes and mounts, Linux security settings, and resource requirements. You, the workload owner, author these values, and the Amazon ECS control plane delivers them. Isolated and confidential tasks do not defend against an adversary who can register or run an arbitrary task definition in your cluster.

**Important**  
Restrict who can register task definitions and run tasks that enable isolation, using IAM. An actor who can author a task definition chooses the image, the mounts, and (for isolated tasks) the container admission fields. Treat task definition registration and `RunTask`/`CreateService` as privileged operations.

For confidential tasks (`isolationMode` = `CONFIDENTIAL_SANDBOX`), the parent instance is untrusted, but the task definition and the `attestationPolicy` you author remain trusted: the policy is measured into a PCR and pins the container admission fields, so a compromised parent instance cannot substitute a different specification without changing the attestation. This guarantee still depends on you authoring a correct policy. ECS provides a tool to generate the attestation policy for your task definition.

## The guest workload is outside the confidentiality boundary
<a name="ict-the-guest-workload-is-outside-the-confidentiality-boundary"></a>

Confidential mode protects the workload's data from the parent instance. It does not protect that data from the workload itself. The attestation policy, the Nitro Sandbox boundary, and the attestation-gated AWS KMS release all constrain what the parent instance can observe or influence. None of them constrain what the workload does with its own data after decrypting it.

A workload running inside a confidential sandbox can defeat its own confidentiality guarantees in ways the runtime cannot prevent. For example:
+ Writing secrets to stdout or stderr, or to any file the parent instance can otherwise read.
+ Writing plaintext secrets to an Amazon EFS volume. The parent instance can mount the same filesystem directly with its own IAM identity and read anything the workload writes.
+ Sending secrets to an attacker-controlled endpoint over the network. TLS hides the traffic from the parent instance, but the destination the workload chose to connect to receives the plaintext. In particular, the parent instance can inject arbitrary IAM task role credentials and redirect AWS API calls to an attacker-controlled AWS account.
+ Loading and executing untrusted code at runtime (for example, `curl | sh`, a plugin downloaded on start, or a user-supplied script) that then exfiltrates data through any of the paths above.

Confidential tasks assume the workload code cooperates with its own confidentiality goals. This is a property of the container image and the application logic, not of the runtime. Confidentiality guarantees extend only as far as the workload owner's own code preserves them.

**Important**  
When you use confidential tasks to protect sensitive data, you are responsible for auditing the container images, application code, and any runtime-loaded extensions that handle that data.

## Why external attestation verification is required
<a name="ict-why-external-attestation-verification-is-required"></a>

For confidential tasks, the ECS sandbox agent measures the environment and the task's policy into PCRs, but measurement alone is passive: no component inside the sandbox or on the parent instance verifies the measurement against an expected value. A cluster operator can change the configuration, and the sandbox still starts. The attestation changes, but nothing rejects the task on its own.

The trust loop is closed only when an external service checks the attestation document before releasing secrets. AWS KMS serves this role. When you configure a KMS key policy that requires attestation and gates decryption on the expected measurements, KMS validates the attestation document attached to each `Decrypt` request and releases the data key only if the measurements match. A modified environment or `attestationPolicy` produces different measurements, so KMS refuses to decrypt, and the workload cannot access its secrets. For the AWS KMS key policy condition keys that gate decryption on attestation, and how to configure them, see [Confidential policy configuration](ict-confidential-policy-configuration.md).

Without this external verification step:
+ The attestation measurement is recorded but never checked.
+ A cluster operator who modifies the task's configuration can run a sandbox with different admission rules. The sandbox starts successfully and the workload runs, but it cannot decrypt secrets gated on the original PCR values.
+ Confidential mode provides process isolation from the parent instance, but does not provide confidentiality for secrets unless those secrets are released only after attestation verification.

**Important**  
Always require attestation on any AWS KMS key that protects confidential workload data. This is the mechanism that enforces the integrity of the task's policy and system image against modification by the cluster operator or a compromised parent instance. Attestation without a verifier is a measurement without enforcement.

## Container admission in isolated tasks
<a name="ict-container-admission-in-isolated-tasks"></a>

For isolated tasks, the auto-generated attestation policy does not restrict which containers can run inside the Nitro Sandbox. Any valid container spec is accepted. This is intentional: isolated tasks treat the task definition as a trusted input. The Nitro Sandbox boundary is the primary isolation mechanism, where the Nitro Hypervisor prevents a container from accessing the parent instance's memory, CPU state, or local storage regardless of what capabilities or images it uses. The container retains network access subject to its security groups and any network controls you configure.

The practical implication is that if an actor can run an `ISOLATED_SANDBOX` task in your cluster, that actor can run any container image with any capabilities inside the sandbox. The Nitro Hypervisor prevents the container from escaping to the parent instance, but there is no restriction on what runs inside the sandbox itself. If your threat model requires defense in depth, for example, restricting which images can run even when the sandbox boundary is intact, use `CONFIDENTIAL_SANDBOX` tasks with an `attestationPolicy` that pins the container admission fields. For more information, see [Confidential policy configuration](ict-confidential-policy-configuration.md).

## What the parent instance cannot do
<a name="ict-what-the-parent-instance-cannot-do"></a>

The Nitro Hypervisor enforces the following guarantees:
+ The parent instance cannot read or write guest memory.
+ The parent instance cannot access CPU register state inside the sandbox.
+ The parent instance cannot forge attestation documents or NSM measurements.
+ The parent instance cannot decrypt encrypted image layers. Decryption keys exist only inside the sandbox.
+ For confidential tasks, the parent instance cannot read the container writable layer or ephemeral volumes. These are stored on an encrypted overlay inside the Nitro Sandbox, with authentication tags held in guest memory rather than on disk. As a result, the parent instance cannot roll the layer back by restoring an earlier snapshot. The restored data no longer matches the tags, so the read fails. For isolated tasks, the overlay is unencrypted to allow faster task startup, and the parent instance can read and write the ephemeral layer.
+ The parent instance cannot read or modify NFS traffic between the sandbox and Amazon EFS mount targets. The guest terminates TLS to the mount target and verifies the server certificate, so the parent instance sees only ciphertext on the wire.

These guarantees hold even if the parent instance operating system is compromised.

## What the parent instance can do
<a name="ict-what-the-parent-instance-can-do"></a>

The parent instance controls the resources that the sandbox depends on. A malicious or compromised parent instance can:

**Deny service.** The parent instance can terminate the sandbox, starve it of CPU or memory, drop network packets, or corrupt storage. No technical mitigation can prevent a malicious parent instance from denying service to the guest.

**Provide false placement metadata.** The parent instance provides Region, Availability Zone, and Availability Zone ID to the sandbox. A malicious parent instance can send false values. Your workload should not make security decisions based on placement metadata.

**Manipulate network traffic.** The parent instance can observe, delay, drop, or modify unencrypted network traffic. This includes DNS: the parent instance can observe DNS queries and respond with arbitrary addresses, redirecting your workload to attacker-controlled servers. The parent instance also writes `/etc/hosts`, so it can point `localhost` at an address outside the task. Your workload should use TLS for all sensitive communication and verify server certificates, and should use `127.0.0.1` rather than `localhost`.

**Read or write shared storage with its own credentials.** The parent instance has network access to the VPC and its own IAM identity. It can mount any Amazon EFS filesystem that its credentials permit and read or write the data directly, bypassing the guest. TLS termination inside the sandbox prevents the parent from reading NFS traffic in flight, but not from accessing the same filesystem out of band. Restrict access with Amazon EFS filesystem policies and parent-side IAM policies. If you require confidentiality from the parent, encrypt data inside the application before writing it to shared storage.

**Provide incorrect time.** The parent instance controls the guest's clock source and proxies time synchronization. A malicious parent instance can skew time forward or backward. Your workload should not rely on wall-clock time for security decisions (for example, replay protection) without additional safeguards.

**Deliver arbitrary content for allowed paths.** The attestation policy controls which file paths the parent instance can write into the guest (for example, configuration files and projected content), but not the content. Treat all such configuration as untrusted and rely on application-level verification for sensitive values.

## Shared responsibility
<a name="ict-shared-responsibility"></a>

With isolated and confidential tasks, AWS is responsible for the Nitro Hypervisor, the Nitro Sandbox boundary, and the guest system image. You are responsible for your container images, task definitions and policies, AWS KMS key policies, and application code.
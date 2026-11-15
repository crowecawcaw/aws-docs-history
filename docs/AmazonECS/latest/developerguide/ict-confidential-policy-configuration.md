

# Confidential policy configuration
<a name="ict-confidential-policy-configuration"></a>

A confidential task's attestation policy defines what the parent is allowed to do when communicating with the Nitro Sandbox: container admission (which containers can start and with what settings), runtime operations (task exec, log streaming), and service access (instance metadata, task credentials). You supply it as the `attestationPolicy` field of the task definition's `TrustedExecutionConfiguration`. The ECS sandbox agent enforces the policy; the parent instance cannot bypass it.

**Note**  
**API model.** `TrustedExecutionConfiguration.attestationPolicy` is *the base64-encoded attestation policy envelope for the task. The attestation policy specifies which containers are allowed to run and the runtime configuration that is cryptographically attested. This parameter is required to run a confidential task.*

## When you need a policy
<a name="ict-when-you-need-a-policy"></a>

Isolated tasks  
When `isolationMode` is `ISOLATED_SANDBOX`, no `attestationPolicy` is used. Container admission is not pinned; any valid container spec in the task definition is accepted, and the Nitro Sandbox boundary is the isolation mechanism.

Confidential tasks  
When `isolationMode` is `CONFIDENTIAL_SANDBOX`, an `attestationPolicy` is required. Admission fields are pinned and attestation gates AWS KMS access. The task's `trustedExecutionSummary.attestationPolicyStatus` reports `CONFIGURED` when a policy is in place.

## Generating a policy
<a name="ict-generate-a-policy"></a>

Amazon ECS provides a command line tool, `ecs-nitro-sandbox-genpolicy`, that generates the attestation policy from your task definition and prints the base64-encoded policy envelope. For instructions on downloading and verifying the tool, see [Getting the CLI tools](ict-get-cli-tools.md).

Run the following `ecs-nitro-sandbox-genpolicy` command to produce the policy envelope, then set the output as the `attestationPolicy` in your task definition:

```
ecs-nitro-sandbox-genpolicy --task-definition my-task-def.json
```

The `--task-definition` value can be a local JSON or YAML file (either a bare task definition or `describe-task-definition` output) or an Amazon ECS task definition ARN. When you pass an ARN, the tool calls `DescribeTaskDefinition` to fetch it, using credentials from the default AWS provider chain and the Region from the ARN:

Replace {{aa-example-1}}, {{111122223333}}, and {{my-family}} with your values:

```
ecs-nitro-sandbox-genpolicy \
  --task-definition arn:aws:ecs:aa-example-1:111122223333:task-definition/my-family:1
```

This minimal command pins every container admission field the tool can derive. To relax specific pins, require image signatures, or permit ECS Exec, see the sections that follow. To print the generated Cedar policy or the predicted PCR values instead of the envelope, use the `--output` option.

## Attestation and PCR values
<a name="ict-attestation-and-pcr-values"></a>

At environment launch, the ECS sandbox agent measures the environment and the task's attestation policy into Platform Configuration Registers (PCRs). AWS KMS gates decryption on these measurements, so it releases a data key only to a task that runs the exact policy and environment you expect.

You don't compute the PCR values by hand. The `ecs-nitro-sandbox-genpolicy` tool predicts them from your task definition, so you can configure your AWS KMS key policy before you launch a task. Run the tool with `--output pcrs` to print the KMS key policy condition for the task:

```
ecs-nitro-sandbox-genpolicy \
  --task-definition my-task-def.json \
  --output pcrs
```

The tool prints a ready-to-paste KMS key policy condition:

```
--- KMS Key Policy Condition ---
"Condition": {
  "StringEqualsIgnoreCase": {
    "kms:RecipientAttestation:PCR17": "3f2e1d...9c8b",
    "kms:RecipientAttestation:PCR8:ServiceName": "ecs.amazonaws.com"
  }
}
```

The condition pins two PCR values:
+ **PCR17** measures the attestation policy set in the task definition, the same policy envelope you set as `attestationPolicy`.
+ **PCR8** measures the certificate that signed the environment image the task runs on. The environment image includes the kernel, the kernel parameters, and the root filesystem. Amazon ECS provides and signs the image, and keeps it patched with the latest security updates.

**Important**  
Always use the `kms:RecipientAttestation:PCR8:ServiceName` condition rather than `kms:RecipientAttestation:PCR8`. Amazon ECS rotates the signing certificate on a regular cadence, which changes the raw PCR8 value; a task that gates on `kms:RecipientAttestation:PCR8` is denied access to AWS KMS when the certificate rotates. The `:ServiceName` form stays valid across rotations.

For more information about AWS KMS condition keys for Nitro Enclaves, see [Condition keys for Nitro Enclaves](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclave.html).

## Updating the policy when the task changes
<a name="ict-update-the-policy-when-the-task-changes"></a>

The attestation policy pins your task definition's configuration, so any change that affects a pinned field makes the existing policy stale. For example, adding a sidecar container — such as a Fluent Bit log router or a CloudWatch agent — changes the task definition. Updating a container image can change the generated policy as well, even when the task definition itself is unchanged. Until you regenerate the policy, set it as the `attestationPolicy`, and update the PCR17 condition on your AWS KMS key, the ECS sandbox agent denies the container at launch and the task fails to start.

### Checking whether the policy matches the task definition
<a name="ict-check-policy-in-sync"></a>

Run `ecs-nitro-sandbox-genpolicy` with the `--check` option to compare the `attestationPolicy` already embedded in a task definition against the policy that the current task definition would generate:

```
ecs-nitro-sandbox-genpolicy --check --task-definition my-task-def.json
```

The tool reports whether the two are in sync, and if they differ, shows the differences. Use it to:
+ Decide whether a change to the task definition or a container image needs a new policy, and therefore a new PCR17 value on your AWS KMS key condition. If `--check` reports that the policy is in sync, no AWS KMS update is needed.
+ Debug a confidential task that is denied at launch. A difference shows that the embedded policy no longer matches the task definition, and identifies the field that drifted.

### Allowing both policies during a deployment
<a name="ict-allow-both-policies-during-a-deployment"></a>

When you deploy a task definition revision that changes the policy, the old and new tasks run at the same time during the rollout. The two revisions produce different PCR17 values, so your AWS KMS key must allow *both* values while both are running. Otherwise, one set of tasks is denied the data key and cannot decrypt.

The `kms:RecipientAttestation:PCR17` condition key is single-valued in the request: each task presents exactly one PCR17 measurement. To accept more than one value, list them on a single `StringEqualsIgnoreCase` operator, which matches when the task's value equals any entry in the list. Do not use the `ForAnyValue` or `ForAllValues` set operators here; those are for keys that carry multiple values in the request, and using them with a single-valued key can make the policy overly permissive. For more information about single-valued versus multivalued context keys, see [Single-valued versus multivalued context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-single-vs-multi-valued-context-keys.html) in the *IAM User Guide*.

```
"Condition": {
    "StringEqualsIgnoreCase": {
        "kms:RecipientAttestation:PCR17": [
            "old-policy-PCR17-value",
            "new-policy-PCR17-value"
        ],
        "kms:RecipientAttestation:PCR8:ServiceName": "ecs.amazonaws.com"
    }
}
```

After the deployment finishes and the old tasks have drained, remove the old PCR17 value so that only the current policy is allowed.

### Reviewing the PCR values a task used
<a name="ict-review-pcr-values-cloudtrail"></a>

AWS KMS records the attestation measurements a task presents in CloudTrail events. When a confidential task calls AWS KMS to decrypt a data key, the recorded event includes the PCR values from the request, including PCR17 (the attestation policy) and PCR8 (the Amazon ECS signing certificate). Reviewing these values lets you confirm which policy a running task actually used — useful for a security audit, or for debugging why a particular task was or was not granted access to a key. For more information about monitoring AWS KMS keys with CloudTrail for Nitro Enclaves, see [Monitoring AWS KMS keys with CloudTrail for Nitro Enclaves](https://docs.aws.amazon.com/kms/latest/developerguide/ct-nitro-enclave.html) in the *AWS KMS Developer Guide*.

## Customizing container admission
<a name="ict-customize-container-admission"></a>

When a task runs in `CONFIDENTIAL_SANDBOX` mode, the attestation policy pins the container admission fields so that a compromised parent instance cannot substitute a different specification at runtime. The ECS policy generation tool, `ecs-nitro-sandbox-genpolicy`, derives these pins automatically from your task definition, so you do not enumerate them yourself. It reads the task definition (a local JSON or YAML file, or fetched from Amazon ECS by task definition ARN), resolves each container image, and emits the base64-encoded policy envelope that you set as `attestationPolicy`. It pins the fields that determine what runs and how, including:
+ **Image digest** – Each image reference is resolved to its digest and pinned; an image presented with a different digest is denied.
+ **Process arguments** – The container entry point and command, including the init-process wrapper that `initProcessEnabled` adds.
+ **Environment variables** – Declared values are pinned, and secret names are pinned by name.
+ **Working directory.**
+ **User and group** – The numeric user ID, group ID, and supplemental group IDs. Unless the container user is a numeric `uid:gid`, they are resolved from the image's `/etc/passwd` and `/etc/group` the same way the container runtime resolves them. With a numeric user or no user, an image without those files, such as one built `FROM scratch`, resolves to group 0.
+ **Linux capabilities** – The capability sets resolved from `linuxParameters.capabilities`.
+ **Mounts** – The task's volumes and mount points, pinned as an exact set.
+ **Security settings** – The read-only root filesystem flag and the rest of the Open Container Initiative (OCI) security posture, such as no-new-privileges, masked and read-only paths, seccomp, SELinux labels, namespaces, and system controls.

You do not need to list these fields yourself. Beyond the fields you set in the task definition, the tool pins the entire predicted OCI runtime specification, so the parent instance cannot alter any part of the container specification without changing the attestation measurement. Runtime defaults, such as the default seccomp action, the masked-path defaults, and the device cgroup deny rule, become exact pins.

You can relax or skip specific pins when a field can't be resolved in your environment, or when a workload needs a pin relaxed on purpose, such as letting an image evolve. Each of the following flags overrides part of the default pinning. Relaxing a pin widens what the parent instance can change without detection, so compensate; for example, require an image signature (see [Image signature verification](#ict-image-signature-verification)) when you drop an image digest pin.

### Skipping the image digest pin
<a name="ict-skip-the-image-digest-pin"></a>

By default, each container's image is pinned to its digest, so only that exact image can start. To let the image change without regenerating the policy, drop the digest pin for a container with `--skip-image-ref-container` and rely on an image signature instead. Because trust then comes from the signature, `--skip-image-ref-container` requires `--require-any-signer` or `--require-all-signers`. For more information, see [Image signature verification](#ict-image-signature-verification).

Replace {{aa-example-1}}, {{111122223333}}, {{my\_profile}}, and {{my-container-name}} with your values:

```
ecs-nitro-sandbox-genpolicy \
  --task-definition my-task-def.json \
  --require-any-signer arn:aws:signer:aa-example-1:111122223333:/signing-profiles/my_profile \
  --skip-image-ref-container my-container-name
```

### Generating without network access
<a name="ict-generate-without-network-access"></a>

To pin the image-derived fields, the tool reads each container's image from the registry. Two flags cut this network access (for an offline run, an unreachable registry, or to avoid pulling large layers), each at the cost of a weaker policy:
+ `--skip-image-fetch` – Skips all registry access. The image-derived fields (process arguments, working directory, and user) are left unpinned. Use this for a fully offline run.
+ `--disable-layer-pull` – Still fetches the small image configuration, so the process arguments and working directory are still pinned; it only skips pulling image layers to read the image's `/etc/passwd` and `/etc/group`. The one thing it gives up is the ability to resolve the user and its groups from those files, so any user other than a numeric `uid:gid` is left unpinned. Use this when the registry is reachable but you want to avoid the layer download.

For example, to generate a policy with no registry access:

```
ecs-nitro-sandbox-genpolicy \
  --task-definition my-task-def.json \
  --skip-image-fetch
```

**Note**  
These flags leave image-derived fields unpinned, which weakens host-tampering protection. For example, if a container's user is anything other than a numeric `uid:gid`, generation still fails closed on the unresolved identity. Add `--allow-unpinned-identity` to accept the unpinned policy.

### Pinning a single architecture
<a name="ict-pin-a-single-architecture"></a>

By default, the tool resolves image configuration for every Linux platform in a multi-architecture image, and those platforms must agree on the policy-relevant fields. To resolve and pin a single architecture, pass `--image-architecture` with `amd64` or `arm64`. Only nodes of that architecture can then run the image.

```
ecs-nitro-sandbox-genpolicy \
  --task-definition my-task-def.json \
  --image-architecture arm64
```

### Allowing an unpinned identity
<a name="ict-allow-an-unpinned-identity"></a>

When a container's user can't be resolved to a numeric user and group ID (for example, the image isn't fetched, or encrypted layers hide `/etc/passwd`), policy generation fails rather than guess. To let generation proceed and leave the user and group unpinned, pass `--allow-unpinned-identity`. This flag doesn't apply to a user that the container runtime can't resolve at all, such as a name that isn't in the image's `/etc/passwd`.

On an image with encrypted layers, declaring a numeric `uid:gid` is sufficient on its own: the user, the group, and the supplemental group set (the primary group only) are all pinned exactly.

```
ecs-nitro-sandbox-genpolicy \
  --task-definition my-task-def.json \
  --allow-unpinned-identity
```

### Allowing additional environment variables
<a name="ict-allow-additional-environment-variables"></a>

By default, the environment variable set is pinned, so a container is denied if it starts with any variable the policy didn't pin. If the runtime injects environment variables that the tool can't predict at generation time, pass `--allow-additional-env` so the policy tolerates variables beyond the ones it pinned.

```
ecs-nitro-sandbox-genpolicy \
  --task-definition my-task-def.json \
  --allow-additional-env
```

## Allowing ECS Exec
<a name="ict-allow-ecs-exec"></a>

By default, a confidential task's policy permits no `exec` beyond an `exec` health-check probe declared in the task definition. If you run the task with ECS Exec (for example, a task or service created with `enableExecuteCommand`), the policy must also permit the `exec` that launches the ECS Exec SSM agent, or the task is denied at startup. Pass `--allow-exec-command` when you generate the policy to permit that one exec, and only that exec.

```
ecs-nitro-sandbox-genpolicy \
  --task-definition my-task-def.json \
  --allow-exec-command
```

**Note**  
Generate the policy with `--allow-exec-command` whenever the task or service sets `enableExecuteCommand`. Without it, the attested policy does not permit the ECS Exec agent, and you cannot add the permission later without regenerating the policy and updating its PCR17 measurement.

## Image signature verification
<a name="ict-image-signature-verification"></a>

By default, the policy generation tool pins each container image by its digest, as described in the container admission pins earlier in this section. A digest pin is exact: only that one image can start. It is also brittle. Every time you update the image, its digest changes, so you must regenerate the attestation policy, update the task definition's `attestationPolicy`, and update the PCR17 condition on your AWS KMS key policy. For an image that is rebuilt often, this becomes a per-deployment chore.

As an alternative, you can require that an image carries a trusted AWS Signer signature. The ECS sandbox agent verifies the signature inside the Nitro Sandbox before allowing a container to start; if verification fails or the image is unsigned, container creation is denied. Because trust comes from the signature rather than a fixed digest, you can drop the digest pin and let the image evolve: as long as each new image is signed by the same signing profile, it runs without regenerating the attestation policy.

### Requiring an AWS Signer signature
<a name="ict-require-an-aws-signer-signature"></a>

Generate the policy with one or more signer flags. Use `--require-any-signer` when a signature from any one of several profiles is sufficient (OR logic), or `--require-all-signers` when the image must be signed by every listed profile (AND logic, for example dual approval). Give each flag a profile-level AWS Signer signing profile ARN. The signature condition applies in addition to the image digest pins.

```
ecs-nitro-sandbox-genpolicy \
  --task-definition my-task-def.json \
  --require-any-signer arn:aws:signer:aa-example-1:111122223333:/signing-profiles/my_profile
```

To let the image evolve without regenerating the policy, also pass `--skip-image-ref-container` to drop the digest pin for that container and rely on the signature alone. Any image signed by the required profile then runs, without a policy change:

Replace {{aa-example-1}}, {{111122223333}}, {{my\_profile}}, and {{my-container-name}} with your values:

```
ecs-nitro-sandbox-genpolicy \
  --task-definition my-task-def.json \
  --require-any-signer arn:aws:signer:aa-example-1:111122223333:/signing-profiles/my_profile \
  --skip-image-ref-container my-container-name
```

For more information about setting up your signing profile, see the [AWS Signer Developer Guide](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html).

The following table lists the task IAM role permissions required for signature verification.


| Action | Purpose | 
| --- | --- | 
| signer:GetRevocationStatus | Check whether an individual signing job or certificate has been revoked. | 
| signer:GetSigningProfile | Check whether the signing profile has been revoked. | 

Both actions are required; if either call fails or returns a permission error, verification fails closed and container creation is denied.

**Note**  
Signature verification requires network access from the Nitro Sandbox to the AWS Signer endpoint. Ensure your VPC and the task security group are configured to allow access to the AWS Signer endpoint.

## How policies are enforced
<a name="ict-how-policies-are-enforced"></a>

1. Amazon ECS delivers the attestation policy to the ECS sandbox agent when the task starts.

1. The agent evaluates it on every operation: container creation, task exec, log reads, and service access.

1. If an operation is denied, the agent returns an error and the operation fails.

1. The ECS sandbox agent measures the policy and environment into a PCR. A compromised parent instance cannot substitute a different policy without changing the attestation measurement.

### Why attestation measurement alone is not sufficient
<a name="ict-why-attestation-measurement-alone-is-not-sufficient"></a>

Attestation measurement is passive: it records what is running, but does not by itself enforce that a specific configuration must be used. Enforcement happens remotely. When the sandbox calls AWS KMS to decrypt an image layer or an application secret, KMS checks the attestation document against your key policy conditions. If the configuration was modified (producing different PCR values), KMS refuses to release the key. A KMS key policy (or an equivalent external verifier) must check attestation. Without it, the measurement is recorded but never acted upon. For more information, see [Security model](ict-security-model.md).
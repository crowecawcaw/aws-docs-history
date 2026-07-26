# Configure node lifecycle actions in AWS PCS

You define node lifecycle actions in your compute node group configuration. This topic
describes how to define a script, control whether it re-runs on reboot, store it, pass it
arguments, handle failures, cache it, validate its integrity, and read its logs.

###### Agent version requirement

Node lifecycle actions require AWS PCS agent version 1.5.0-1 or later. If your compute nodes
use a custom AMI with an older agent version, update the agent before you configure lifecycle
actions. For more information, see [AWS PCS agent versions](pcs-agent-versions.md "pcs-agent-versions.md").

## How to define a script

Each script has a `name`, a `scriptSource`, optional
`arguments`, an `onError` policy, and an `executionPolicy`. The
location and integrity fields are grouped under `scriptSource`.

```
{
  "name": "My script",
  "scriptSource": {
    "scriptLocation": "s3://`my-bucket`/`my-script`.sh",
    "s3VersionId": "optional, S3 only",
    "checksum": "optional 64-char SHA-256 hex"
  },
  "arguments": ["`arg1`", "`arg2`"],
  "onError": "TERMINATE",
  "executionPolicy": "FIRST_BOOT_ONLY"
}
```

## Add lifecycle actions to a compute node group

You can add lifecycle actions when you create or update a compute node group. Use the
AWS Management Console or the AWS CLI.

AWS Management Console

###### To add lifecycle actions using the console

1. Open the [AWS PCS
   console](https://console.aws.amazon.com/pcs/home#/clusters "https://console.aws.amazon.com/pcs/home#/clusters").
2. Open the create or update page for a compute node group.
3. In the **Node lifecycle actions** section, choose **Add
   script**.
4. Select the script source:

   1. **Add from AWS PCS scripts library** – Reference an
      AWS-maintained script. For more information, see [Use AWS-maintained scripts for node lifecycle actions in AWS PCS](cng-node-lifecycle-actions-vetted-scripts.md "cng-node-lifecycle-actions-vetted-scripts.md").
   2. **Add via S3** – Reference a script by its Amazon S3 URI.
   3. **Add via HTTPS** – Reference a script by its HTTPS URL.

5. Select the node stage.
6. For a script that you add via S3 or HTTPS, specify these settings:

   1. **Script location** – Enter the S3 URI or HTTPS URL for the
      script.
   2. **Name** – Enter a name for the script.
   3. (Optional) **Checksum** – Enter a SHA-256 checksum to verify
      the script's integrity. For more information, see [Script integrity (checksums)](#cng-node-lifecycle-actions-configure-checksums "#cng-node-lifecycle-actions-configure-checksums").
   4. (Optional) For a script that you add via S3, enter a version to reference a specific
      version of the object.

7. For all script sources, specify these settings:

   1. **Error handling behavior** – Select `TERMINATE`,
      `STOP_SEQUENCE`, or `CONTINUE`.
   2. **Execution policy** – Select `FIRST_BOOT_ONLY` or
      `EVERY_BOOT`.
   3. (Optional) **Arguments** – Add arguments to pass to the
      script.

8. To add more scripts, repeat these steps.
9. Scripts run from top to bottom within a stage. To change the execution order, choose
   **Actions** for a script, and then choose **Move
   up** or **Move down**.
10. For **Caching policy**, select `CACHE_ONCE` or
    `REFRESH_ON_REBOOT`. The caching policy applies to all scripts. For more
    information, see [Script caching and updates](#cng-node-lifecycle-actions-configure-caching "#cng-node-lifecycle-actions-configure-caching").

AWS CLI
Use the `--node-lifecycle-actions` parameter with the
`create-compute-node-group` or `update-compute-node-group` command. For
the parameter structure, see [NodeLifecycleActionsRequest](../APIReference/API_NodeLifecycleActionsRequest.md "../APIReference/API_NodeLifecycleActionsRequest.md") in the _AWS PCS API Reference_. For
example commands, see [Node lifecycle action examples for AWS PCS](cng-node-lifecycle-actions-examples.md "cng-node-lifecycle-actions-examples.md").

## Controlling reboot behavior

Set `executionPolicy` per script to control whether it re-runs on reboot.

| **Value**                   | **Behavior**                                                                          | **When to use**                                                                                                                             |
| --------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `FIRST_BOOT_ONLY` (default) | Run the script once, on the node's first boot. Skip it on every subsequent<br>reboot. | One-time setup, such as installing packages, joining a domain, or initializing<br>storage. You don't have to make these scripts idempotent. |
| `EVERY_BOOT`                | Run the script on first boot *_and_<br>• on every<br>reboot.                          | Configuration that must be reapplied after a restart, such as re-mounting an<br>ephemeral file system or reasserting node state.            |

Scripts set to `FIRST_BOOT_ONLY` run once and are skipped on reboot. Scripts
set to `EVERY_BOOT` run on every boot and should be idempotent (safe to run more than
once with the same result).

## Script storage locations

You can store scripts in **Amazon S3** or serve them over
**HTTPS**. Scripts can't be uploaded inline through the API, and each
script must be no larger than 2 MiB — the agent rejects any script that exceeds this
size.

- **Amazon S3 (`s3://`bucket`/`key``)** — The instance IAM profile must have
  `s3:GetObject` on the object. With an S3 gateway VPC endpoint, nodes in private
  subnets can retrieve scripts through the VPC endpoint. Pin a specific version with
  `scriptSource.s3VersionId` (S3 locations only).
- **HTTPS
  (`https://`hostname`/`path``)**
  — The host must be
  publicly readable (no authentication) and the node needs outbound internet access (internet
  gateway, NAT gateway, or HTTP proxy). This is useful for scripts hosted on GitHub or other
  public repositories.

External storage provides version control, auditability, and reuse across teams. Inline or
uploaded scripts are not supported.

## Passing arguments to scripts

Pass arguments as an ordered array. They reach your script as positional command-line
parameters.

```
arguments: ["fs-12345678", "/shared", "nfs4"]
# script.sh fs-12345678 /shared nfs4   ($1=fs-12345678, $2=/shared, $3=nfs4)
```

The agent exports environment variables to every script. These variables contain cluster and
node metadata.

| **Variable**                                                   | **Description**                                                                                                     |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `PCS_CLUSTER_ID` / `PCS_CLUSTER_NAME`                          | Cluster identifier / name                                                                                           |
| `PCS_COMPUTE_NODE_GROUP_ID` /<br>`PCS_COMPUTE_NODE_GROUP_NAME` | Compute node group identifier / name                                                                                |
| `PCS_NODE_ID`                                                  | Node identifier                                                                                                     |
| `PCS_IS_FIRST_BOOT`                                            | `1` on the node's first boot, `0` on every subsequent<br>reboot. Use it to branch behavior in `EVERY_BOOT` scripts. |

```
#!/usr/bin/env bash
echo "Configuring node $PCS_NODE_ID in cluster $PCS_CLUSTER_NAME"
```

## Error handling

Each script has an `onError` field that controls what happens when
a script exits non-zero or is killed by a signal.

| **Value**             | **Behavior**                                                     | **When to use**                                                                              |
| --------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `TERMINATE` (default) | Mark the node failed and terminate it.                           | Critical setup (storage mounts, Active Directory join). Prevents paying for broken<br>nodes. |
| `STOP_SEQUENCE`       | Stop the remaining scripts in the stage; leave the node running. | Debugging — inspect the instance after a failure.                                            |
| `CONTINUE`            | Log the error and run the next script.                           | Optional or best-effort tasks.                                                               |

A script fails if it exits non-zero or is killed by a signal (for example,
`SIGSEGV`). **Scripts are not retried.** If an
operation might experience transient failures, add retry logic inside the script.
Script _retrieval_ (download), however, is retried — up to 3 attempts with
exponential backoff (approximately 17 seconds maximum) — before the `onError`
behavior applies.

## Script caching and updates

The agent downloads each script to the instance on first boot and stores it locally.
Two fields control behavior on reboot: `scriptCachingPolicy` controls
re-download and `executionPolicy` controls re-execution.

- **`CACHE_ONCE` (default)** — Download once
  at first boot; never refetch. Behavior is identical across reboots. Updating script
  _content_ requires instance replacement.
- **`REFRESH_ON_REBOOT`** — Re-download on
  every reboot, overwriting the cache. This lets you ship script fixes through a reboot.
  It requires network access on each boot; if a refresh fails, the download is treated
  as a retrieval failure and the script's `onError` behavior applies (there is no
  fallback to the cached copy). A refreshed script only actually re-runs on reboot if its
  `executionPolicy` is `EVERY_BOOT`.

The lifecycle _configuration_ (which scripts run, their arguments, error
handling, and execution policy) is always immutable per instance. Changing it through
`UpdateComputeNodeGroup` affects only **new** instances
and triggers the `DRAIN` strategy so running jobs finish before nodes are
replaced.

## Script integrity (checksums)

Optionally provide a SHA-256 `checksum` in a script's `scriptSource`,
as a 64-character hexadecimal string. The agent validates it on download; a mismatch is treated
as a download failure and triggers `onError`. We recommend a checksum for production,
especially for scripts from shared or external sources.

```
sha256sum mount-efs.sh   # use the 64-char hex hash as the checksum value
```

## Logging and debugging

Each script writes to its own log file, and the agent keeps its own operational log.

```
# agent: download, caching, checksum, orchestration
/var/log/amazon/pcs/lifecycle/actions/executor.log
# each script's stdout/stderr
/var/log/amazon/pcs/lifecycle/actions/<stage>/<script-name>.log
```

The log filename uses the script name as you defined it. Spaces are preserved. For example, a
script named `Mount EFS home directory` writes to `Mount EFS home
 directory.log`. Connect with SSH or
AWS Systems Manager Session Manager to read them — both are available by the
`nodeBootstrapped` stage. Because nodes that fail with `TERMINATE` are replaced,
forward logs off-instance for debugging after termination: add a node bootstrapped script that configures the
Amazon CloudWatch agent to ship the lifecycle log directory to Amazon CloudWatch Logs. The AWS-maintained
`configure-cloudwatch-logs.sh` script does this. For more information, see [Use AWS-maintained scripts for node lifecycle actions in AWS PCS](cng-node-lifecycle-actions-vetted-scripts.md "cng-node-lifecycle-actions-vetted-scripts.md").

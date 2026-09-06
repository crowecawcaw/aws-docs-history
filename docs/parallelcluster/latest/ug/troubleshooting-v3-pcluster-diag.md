# Troubleshooting with `pcluster-diag`

`pcluster-diag` is a diagnostics tool that verifies a set of conditions that a healthy AWS ParallelCluster node is expected to
satisfy.

Use `pcluster-diag` as a first step when a cluster misbehaves at runtime. The tool emits a JSON diagnostics report to help you
understand the problems that are affecting your cluster. If you can't resolve a problem, attach the report to an AWS Support case.

The tool is included in every AWS ParallelCluster AMI starting with version 3.16.0, both the official AMIs and the custom AMIs that you build
with `pcluster build-image`. If you use an older AWS ParallelCluster version, you can still install the tool by following the steps in
[Versions older than 3.16.0](#troubleshooting-v3-pcluster-diag-updates-older "#troubleshooting-v3-pcluster-diag-updates-older").

You can run `pcluster-diag` on any cluster node. If you don't know where the problem is, run it on the head node.

###### Key characteristics

- Context aware – at startup it reads the node type and the deployed cluster configuration, then runs only
  the checks that apply. Checks for features that your cluster doesn't use are reported as skipped.
- Read-only by default – it never changes the configuration of your cluster. A check that isn't read-only
  requires your explicit approval before it runs, and records it as skipped if you decline.
- Complete in a single run – a check that fails never stops the others. Every applicable check runs on
  every invocation, so one run gives you the complete picture of the node, according to the available checks.

## Show available checks

To see which checks the tool will execute, use the `describe-checks` subcommand, which returns a JSON array of every registered
check, each with its id and description.

```
`$` `pcluster-diag describe-checks`
`[
 {
 "check_id": "...",
 "check_description": "..."
 },
 ...
]`
```

## Execute the checks

Connect to the node that you want to diagnose, and then execute the `run` subcommand as root.

```
`$` `sudo pcluster-diag run`
```

`pcluster-diag` writes two separate streams:

- A progress log to standard error.
- The JSON report to standard output. The same report is also saved to a timestamped file under
  `./pcluster-diag-output/` in the current directory.

The following options are available.

`--output-file` `path`

The file that the JSON report is written to. The default is a timestamped file under
`./pcluster-diag-output/`, for example
`./pcluster-diag-output/pcluster-diag-report-2026-08-04T10-12-00.json`.

`-y`, `--yes`

Approve every check that requires confirmation, without prompting. Use this when you run `pcluster-diag` from a script.

`--version`

Print the `pcluster-diag` version.

`--help`

Print the usage information. `pcluster-diag run --help` prints the options of the `run` subcommand.

## Interpret the report

`pcluster-diag` emits a JSON report that accounts for every check it ran, whether the check passed, warned, failed, or was skipped.
`context` describes the node that was diagnosed. The general structure of the report is as follows:

```
`{
 "context": { ... },
 "results": [
 {
 "check_id": "...",
 "check_description": "...",
 "status": "...",
 "errors": [ { "code": "...", "message": "..." } ],
 "warnings": [ { "code": "...", "message": "..." } ],
 "infos": [ { "code": "...", "message": "..." } ]
 }
 ]
}`
```

### Check statuses

The `status` of each check tells you what to do with it.

| Status                   | Meaning                                                                     | What to do                                                                                                                           |
| ------------------------ | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `PASSED`                 | This check found no problem.                                                | -                                                                                                                                    |
| `WARNING`                | This check found something that might cause a problem on the node.          | Review the `warnings` list and address anything that might be important.                                                             |
| `FAILURE`                | This check found a problem on the node.                                     | Review the `errors` list and address all the problems.                                                                               |
| `CHECK_ERROR`            | The check couldn't complete, so status couldn't be confirmed.               | Treat it as inconclusive, not as a problem. Report the error to AWS Support because it might be the signal of an unhandled<br>error. |
| `SKIPPED_NOT_APPLICABLE` | The check doesn't apply to this node type or to your cluster configuration. | Nothing. This is the expected status for features that your cluster doesn't use.                                                     |
| `SKIPPED_BY_USER`        | The check required your confirmation and you declined it.                   | Rerun `pcluster-diag`, approving the check when prompted.                                                                            |

If every check reports `PASSED`, `pcluster-diag` found no problems. However, the coverage of `pcluster-diag`
is not comprehensive and will grow with every release. A healthy diagnosis does not guarantee that the cluster is healthy.

### Check findings

A check result can carry three kinds of findings, each with a `code` and a `message`.

- `errors`, coded `E`n``, are the reasons a check failed. The reserved code `E0` is
  used only for internal errors that prevented the correct execution of the check.
- `warnings`, coded `W`n``, are non-fatal observations.
- `infos`, coded `I`n``, are contextual notes.

## Get the latest `pcluster-diag` from GitHub

`pcluster-diag` is available on all AWS ParallelCluster versions 3.16.0 and later, and can also be installed on older versions with
some additional steps.

New checks and improved diagnostic messages land in the [aws-parallelcluster-cookbook](https://github.com/aws/aws-parallelcluster-cookbook "https://github.com/aws/aws-parallelcluster-cookbook")
repository on the GitHub website. To use the latest checks without waiting for the next AWS ParallelCluster release, follow the steps for your
AWS ParallelCluster version.

### Versions 3.16.0 and later

In AWS ParallelCluster versions 3.16.0 and later, the `pcluster-diag` command is installed and available on `PATH`.

To update the tool from the `develop` branch, run the following on the node where you want to execute the tool.

```
`$` `curl -fL https://github.com/aws/aws-parallelcluster-cookbook/archive/refs/heads/develop.tar.gz \
 | sudo tar -xz --strip-components=5 -C /opt/parallelcluster/sources/pcluster-diag \
 --wildcards '*/cookbooks/aws-parallelcluster-platform/files/pcluster-diag/*'`
```

Verify the tool is functional:

```
`$` `sudo pcluster-diag describe-checks`
```

To use a version other than the tip of `develop`, replace `develop` in the URL with the branch or the tag you want, for
example a `release-*` branch.

Keep the following in mind:

- The refresh applies only to the node that you run it on. Repeat it on every node that you want to diagnose with the newer checks.
- The tool source is baked into the AMI, so a node that gets replaced comes back with the version from the AMI.

### Versions older than 3.16.0

In AWS ParallelCluster versions older than 3.16.0, the `pcluster-diag` command isn't installed on the node.

To install the tool from the `develop` branch, run the following on the node where you want to execute the tool.

```
`$` `sudo mkdir -p /opt/parallelcluster/sources/pcluster-diag
curl -fL https://github.com/aws/aws-parallelcluster-cookbook/archive/refs/heads/develop.tar.gz \
 | sudo tar -xz --strip-components=5 -C /opt/parallelcluster/sources/pcluster-diag \
 --wildcards '*/cookbooks/aws-parallelcluster-platform/files/pcluster-diag/*'`
```

Verify the tool is functional:

```
`$` `PYTHONPATH=/opt/parallelcluster/sources/pcluster-diag /opt/parallelcluster/pyenv/versions/`3.12.8`/envs/cookbook_virtualenv/bin/python3 -m pcluster_diag.cli describe-checks`
```

**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Generate CIS compliance reports from Kubernetes nodes using kubectl debug

This topic describes how to generate CIS (Center for Internet Security) compliance reports for Amazon EKS nodes using the `kubectl debug` command.
The command allows you to temporarily create a debugging container on a Kubernetes node and run CIS compliance checks using the `apiclient` tool. The `apiclient` tool is part of Bottlerocket OS, the OS used by EKS Auto Mode nodes.

## Prerequisites

Before you begin, ensure you have:

- Access to an Amazon EKS cluster with `kubectl` configured (version must be at least v1.32.0; type `kubectl version` to check).
- The appropriate IAM permissions to debug nodes.
- A valid profile that allows debug operations (e.g., `sysadmin`).

For more information about using debugging profiles with `kubectl`, see [Debugging a Pod or Node while applying a profile](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/#debugging-profiles "https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/#debugging-profiles") in the Kubernetes documentation.

## Procedure

1. Determine the AWS Instance ID of the node you want to run the report on. Use the following command to list the nodes in the cluster. The instance ID is found in the name column, and begins with `i-`:

```
kubectl get nodes
```

```
NAME                  STATUS   ROLES    AGE   VERSION
i-0ea0ba0f8ef9ad609   Ready    <none>   62s   v1.30.10-eks-1a9dacd
```

2. Run the following command, replacing `<instance-id>` with the instance ID of the node you want to query:

```
kubectl debug node/<instance-id> -it --profile=sysadmin --image=public.ecr.aws/amazonlinux/amazonlinux:2023 -- bash -c "yum install -q -y util-linux-core; nsenter -t 1 -m apiclient report cis --level 1 --format text"
```

Components of this command include:

    * `kubectl debug node/<instance-id>` — Creates a debugging session on the specified EC2 instance ID.
    * `-it` — Allocates a TTY (command line shell) and keeps stdin open for interactive usage.
    * `--profile=sysadmin` — Uses the specified `kubectl` profile with appropriate permissions.
    * `--image=public.ecr.aws/amazonlinux/amazonlinux:2023` — Uses `amazonlinux:2023` as the container image for debugging.
    * `bash -c "…​"` — Executes the following commands in a bash shell:




    	+ `yum install -q -y util-linux-core` — Quietly installs the required utilities package.
    	+ `nsenter -t 1 -m` — Runs `nsenter` to enter the namespace of the host process (PID 1).
    	+ `apiclient report cis --level 1 --format text` — Runs the CIS compliance report at level 1 with text output.

3. Review the report text output.

## Interpreting the output

The command generates a text-based report showing the compliance status of various CIS controls. The output includes:

- Individual CIS control IDs
- Description of each control
- Pass, Fail, or Skip status for each check
- Details that explain any compliance issues

Here is an example of output from the report run on a Bottlerocket instance:

```
Benchmark name:  CIS Bottlerocket Benchmark
Version:         v1.0.0
Reference:       https://www.cisecurity.org/benchmark/bottlerocket
Benchmark level: 1
Start time:      2025-04-11T01:40:39.055623436Z

[SKIP] 1.2.1     Ensure software update repositories are configured (Manual)
[PASS] 1.3.1     Ensure dm-verity is configured (Automatic)[PASS] 1.4.1     Ensure setuid programs do not create core dumps (Automatic)
[PASS] 1.4.2     Ensure address space layout randomization (ASLR) is enabled (Automatic)
[PASS] 1.4.3     Ensure unprivileged eBPF is disabled (Automatic)
[PASS] 1.5.1     Ensure SELinux is configured (Automatic)
[SKIP] 1.6       Ensure updates, patches, and additional security software are installed (Manual)
[PASS] 2.1.1.1   Ensure chrony is configured (Automatic)
[PASS] 3.2.5     Ensure broadcast ICMP requests are ignored (Automatic)
[PASS] 3.2.6     Ensure bogus ICMP responses are ignored (Automatic)
[PASS] 3.2.7     Ensure TCP SYN Cookies is enabled (Automatic)
[SKIP] 3.4.1.3   Ensure IPv4 outbound and established connections are configured (Manual)
[SKIP] 3.4.2.3   Ensure IPv6 outbound and established connections are configured (Manual)
[PASS] 4.1.1.1   Ensure journald is configured to write logs to persistent disk (Automatic)
[PASS] 4.1.2     Ensure permissions on journal files are configured (Automatic)

Passed:          11
Failed:          0
Skipped:         4
Total checks:    15
```

For information about the benchmark, see [Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes/ "https://www.cisecurity.org/benchmark/kubernetes/") from the Center for Internet Security (CIS).

## Related resources

- [Bottlerocket CIS Benchmark](https://bottlerocket.dev/en/os/1.34.x/api/reporting/cis/ "https://bottlerocket.dev/en/os/1.34.x/api/reporting/cis/") in Bottlerocket OS Documentation.
- [Debug Running Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/ "https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/") in the Kubernetes Documentation.
- [Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes/ "https://www.cisecurity.org/benchmark/kubernetes/") from the Center for Internet Security (CIS)

# Prerequisites for Amazon EKS cluster

support

This section includes the prerequisites for monitoring runtime behavior of your Amazon EKS
resources. These prerequisites are crucial for the GuardDuty agent to function as expected. After
these prerequisites are met, see [Enabling GuardDuty Runtime Monitoring](runtime-monitoring-configuration.md "runtime-monitoring-configuration.md") to start monitoring your resources.

## Support for Amazon EKS features

Runtime Monitoring **supports** Amazon EKS clusters running on Amazon EC2
instances and Amazon EKS Auto Mode.

Runtime Monitoring **doesn't support** Amazon EKS clusters with
Amazon EKS Hybrid Nodes, and those running on AWS Fargate.

For information about these Amazon EKS features, see [What is Amazon EKS?](../../../eks/latest/userguide/what-is-eks.md "../../../eks/latest/userguide/what-is-eks.md") in the
**Amazon EKS User Guide**.

## Validating architectural

requirements

The platform that you use may impact how GuardDuty security agent supports GuardDuty in receiving
the runtime events from your EKS clusters. You must validate that you're using one of the
verified platforms. If you're managing the GuardDuty agent manually, ensure that the Kubernetes version
supports the GuardDuty agent version that is currently in use.

### Verified platforms

The OS distribution, kernel version, and CPU architecture affect the support provided by
the GuardDuty security agent. Kernel support includes `eBPF`, `Tracepoints`
and `Kprobe`. For CPU architectures, Runtime Monitoring supports AMD64 (`x64`) and
ARM64(Graviton2 and above)[1](#runtime-monitoring-eks-graviton-2-support "#runtime-monitoring-eks-graviton-2-support").

The following table shows the verified configuration for deploying the GuardDuty security
agent and configuring EKS Runtime Monitoring.

| OS distribution**[2](#runtime-monitoring-eks-os-support "#runtime-monitoring-eks-os-support")** | Kernel version**[3](#runtime-monitoring-eks-kernel-version-required-flag "#runtime-monitoring-eks-kernel-version-required-flag")** | Supported Kubernetes version |
| ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| Bottlerocket                                                                                    | 5.4, 5.10, 5.15, 6.1[4](#v6.1-kernel-dns-findings-unsupported-eks "#v6.1-kernel-dns-findings-unsupported-eks")                     | v1.23<br>• v1.34             |
| Ubuntu                                                                                          | 5.4, 5.10, 5.15, 6.1[4](#v6.1-kernel-dns-findings-unsupported-eks "#v6.1-kernel-dns-findings-unsupported-eks")                     | v1.21<br>• v1.34             |
| Amazon Linux 2                                                                                  | 5.4, 5.10, 5.15, 6.1[4](#v6.1-kernel-dns-findings-unsupported-eks "#v6.1-kernel-dns-findings-unsupported-eks")                     | v1.21<br>• v1.34             |
| Amazon Linux 2023*[5](#runtime-eks-al2023-support-v1.6.0 "#runtime-eks-al2023-support-v1.6.0")* | 5.4, 5.10, 5.15, 6.1[4](#v6.1-kernel-dns-findings-unsupported-eks "#v6.1-kernel-dns-findings-unsupported-eks")                     | v1.21<br>• v1.34             |
| RedHat 9.4                                                                                      | 5.14[4](#v6.1-kernel-dns-findings-unsupported-eks "#v6.1-kernel-dns-findings-unsupported-eks")                                     | v1.21<br>• v1.34             |
| Fedora 34                                                                                       | 5.11, 5,17                                                                                                                         | v1.21<br>• v1.34             |
| Fedora 40                                                                                       | 6.8                                                                                                                                | v1.28<br>• v1.34             |
| Fedora 41                                                                                       | 6.12                                                                                                                               | v1.28<br>• v1.34             |
| CentOS Stream 9                                                                                 | 5.14                                                                                                                               | v1.21<br>• v1.34             |

1. Runtime Monitoring for Amazon EKS clusters doesn't support the first generation Graviton instance such
   as A1 instance types.
2. Support for various operating systems - GuardDuty has verified Runtime Monitoring
   support for the operating distribution listed in the preceding table. While the GuardDuty security agent may
   run on operating systems not listed in the preceding table, the GuardDuty team cannot guarantee the
   expected security value.
3. For any kernel version, you must set the `CONFIG_DEBUG_INFO_BTF` flag to `y` (meaning _true_). This is required so that
   the GuardDuty security agent can run as expected.
4. Presently, with Kernel version `6.1`, GuardDuty can't generate [GuardDuty Runtime Monitoring finding types](findings-runtime-monitoring.md "findings-runtime-monitoring.md") that are
   related to [Domain Name System (DNS) events](runtime-monitoring-collected-events.md#eks-runtime-dns-events "runtime-monitoring-collected-events.md#eks-runtime-dns-events").
5. Runtime Monitoring supports AL2023 with the release of the GuardDuty security agent v1.6.0 and above.
   For more information, see [GuardDuty security agent versions for Amazon EKS resources](runtime-monitoring-agent-release-history.md#eks-runtime-monitoring-agent-release-history "runtime-monitoring-agent-release-history.md#eks-runtime-monitoring-agent-release-history").

#### Kubernetes versions supported by GuardDuty security

agent

The following table shows the Kubernetes versions for your EKS clusters that are supported by
GuardDuty security agent.

| Amazon EKS add-on GuardDuty security agent version                               | Kubernetes version |
| -------------------------------------------------------------------------------- | ------------------ |
| v1.12.1 (latest<br>• v1.12.1-eksbuild.2)                                         | 1.28<br>• 1.34     |
| v1.11.0 (latest<br>• v1.11.0-eksbuild.2)                                         | 1.28<br>• 1.34     |
| v1.10.0 (latest<br>• v1.10.0-eksbuild.2)                                         | 1.21<br>• 1.33     |
| v1.9.0 (latest<br>• v1.9.0-eksbuild.2)<br>v1.8.1 (latest<br>• v1.8.1-eksbuild.2) | 1.21<br>• 1.32     |
| v1.7.1<br>v1.7.0<br>v1.6.1                                                       | 1.21<br>• 1.31     |
| v1.6.0<br>v1.5.0<br>v1.4.1<br>v1.4.0<br>v1.3.1                                   | 1.21<br>• 1.29     |
| v1.3.0<br>v1.2.0                                                                 | 1.21<br>• 1.28     |
| v1.1.0                                                                           | 1.21<br>• 1.26     |
| v1.0.0                                                                           | 1.21<br>• 1.25     |

Some of the GuardDuty security agent versions will reach
end of standard support.

For information about the agent release versions, see [GuardDuty security agent versions for Amazon EKS resources](runtime-monitoring-agent-release-history.md#eks-runtime-monitoring-agent-release-history "runtime-monitoring-agent-release-history.md#eks-runtime-monitoring-agent-release-history").

### CPU and memory limits

The following table shows the CPU and memory limits for the Amazon EKS add-on for GuardDuty
(`aws-guardduty-agent`).

| Parameter | Minimum limit | Maximum limit |
| --------- | ------------- | ------------- |
| CPU       | 200m          | 1000m         |
| Memory    | 256 Mi        | 1024 Mi       |

When you use Amazon EKS add-on version 1.5.0 or above, GuardDuty provides the capability to
configure the add-on schema for your CPU and memory values. For information about the
configurable range, see [Configurable parameters and
values](guardduty-configure-security-agent-eks-addon.md#gdu-eks-addon-configure-parameters-values "guardduty-configure-security-agent-eks-addon.md#gdu-eks-addon-configure-parameters-values").

After you enable EKS Runtime Monitoring and assess the coverage status of your EKS clusters, you can
set up and view the container insight metrics. For more information, see [Setting up CPU and memory
monitoring](runtime-monitoring-setting-cpu-mem-monitoring.md "runtime-monitoring-setting-cpu-mem-monitoring.md").

## Validating your organization service control

policy

If you have set up a service control policy (SCP) to manage permissions in your
organization, validate that permissions boundary is not restricting
`guardduty:SendSecurityTelemetry`. It is required for GuardDuty to support Runtime Monitoring
across different resource types.

If you are a member account, connect with the associated delegated administrator. For
information about managing SCPs for your organization, see [Service control policies
(SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md").

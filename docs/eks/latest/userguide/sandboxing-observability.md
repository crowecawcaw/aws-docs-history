

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Observability
<a name="sandboxing-observability"></a>

Running a pod inside a Nitro Sandbox changes what you can observe and how. What you can see depends on the pod’s mode, because the Cedar policy controls which operations the parent instance can perform.

## Logs and exec
<a name="sandboxing-observability-logs-exec"></a>

 `kubectl logs` works for sandboxed pods in both isolated and confidential mode. Container logs stream over the vsock channel to the parent instance. The container’s termination message and container stats (`kubectl top`) are also available by default in both modes.

 `kubectl exec` (along with `kubectl attach`, `stdin`, and process listing) depends on the mode:
+  **Isolated mode** permits `exec`, `stdin`, and process listing, so interactive debugging works the same as for a standard pod.
+  **Confidential mode** denies `exec`, `stdin`, and process listing by default, so the parent instance cannot introspect the guest. You can permit specific exec commands when you generate the Cedar policy. For more information, see [Run a pod in confidential mode](sandboxing-confidential-setup.md).

## Node-level monitoring agents
<a name="sandboxing-observability-agents"></a>

The Amazon CloudWatch Observability agent can collect container logs and metrics from sandboxed pods. These logs and metrics surface through the standard kubelet location, which the agent reads. The Amazon GuardDuty agent, whose runtime monitoring inspects host processes and cgroups, cannot observe activity inside a Nitro Sandbox. The sandbox isolates the pod from the node. GuardDuty continues to monitor standard pods and node-level activity on the same node. For more information, see [Monitor cluster data with Amazon CloudWatch](cloudwatch.md) and [Detect threats with Amazon GuardDuty](integration-guardduty.md).
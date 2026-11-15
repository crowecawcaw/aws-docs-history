

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Network isolation
<a name="sandboxing-network-isolation"></a>

Set `sandbox.amazonaws.com/network-isolated: "true"` on a pod to remove all network access from the Nitro Sandbox. The sandbox boots with no network interface, no DNS, no NTP, no IMDS, and no Pod Identity credentials. Isolation applies in both directions: the pod cannot reach the network, and no traffic from the network reaches the workload.

```
metadata:
  annotations:
    sandbox.amazonaws.com/network-isolated: "true"
spec:
  runtimeClassName: isolated-sandbox
```

## Behavior with network isolation
<a name="sandboxing-network-isolation-behavior"></a>
+ There is no path from the pod network namespace into the Nitro Sandbox, so `kubectl port-forward` does not work.
+ Kubelet HTTP or TCP probes cannot succeed. Use exec probes instead.
+ Services that select the pod cannot reach the workload. Connections are refused rather than silently dropped, because the pod IP is still configured in the pod network namespace.
+ Logs, `exec`, `stdin`, and stats continue to work over the vsock channel.
+ Encrypted images are not available because they require Pod Identity credentials for AWS KMS access.

**vsock channel is accessible inside the guest**  
The vsock device used for shim-to-agent communication is accessible to all processes inside the guest, including container workloads. A container process can call `bind()` on AF\_VSOCK ports. The shim does not connect to guest-bound ports, but any process on the parent instance with access to the Firecracker vsock Unix domain socket can. This creates a potential data channel that bypasses the absence of a network device.
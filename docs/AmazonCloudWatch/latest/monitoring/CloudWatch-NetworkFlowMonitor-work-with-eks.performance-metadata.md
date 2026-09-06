

# Additional network path metadata included for Amazon EKS
<a name="CloudWatch-NetworkFlowMonitor-work-with-eks.performance-metadata"></a>

When Network Flow Monitor gathers performance metrics for network flows between Amazon EKS components, it includes additional metadata information about the network path, to help you better understand how the network paths for your workload are performing.

You can view detailed information about Amazon EKS network flow performance by creating a monitor for the network flows that you're interested in, and then viewing details on the **Historical explorer** tab.

With Network Flow Monitor, you can measure network performance between the following Amazon EKS components, to better understand how your workload is performing with your Amazon EKS configuration and determine where there are bottlenecks or impairments.
+ Pod to pod on the same node
+ Node to node on the same cluster
+ Pod to pod on a different cluster
+ Node to node on different clusters
+ With and without Network Load Balancer

The following table lists the information that Network Flow Monitor returns for each network flow scenario.


<table>
<thead>
  <tr><th colspan="4"><b>Connection information</b></th><th colspan="6"><b>Metadata information</b></th></tr>
  <tr><th colspan="4"></th><th colspan="3"><b>Local</b></th><th colspan="3"><b>Remote</b></th></tr>
  <tr><th><b>Scenario</b></th><th><b>Initiated by</b></th><th><b>Local</b></th><th><b>Remote</b></th><th><b>Pod name</b></th><th><b>Service</b></th><th><b>Namespace</b></th><th><b>Pod name</b></th><th><b>Service</b></th><th><b>Namespace</b></th></tr>
</thead>
<tbody>
  <tr><td>Local pod connecting to cluster IP of another internal cluster service</td><td>Local</td><td>Local pod IP address</td><td>Remote pod IP address<br />(through cluster IP address)</td><td>✓</td><td>✓</td><td>✓</td><td>✓ ¹</td><td>✓</td><td>✓</td></tr>
  <tr><td>Local pod in a node network namespace connecting to cluster IP of another internal cluster service</td><td>Local</td><td>Local node IP address</td><td>Remote pod IP address<br />(through cluster IP address)</td><td>✓ ²</td><td>✓ ²</td><td>✓ ²</td><td>✓ ¹</td><td>✓</td><td>✓</td></tr>
  <tr><td>Local pod connecting to individual pod IP address of another pod (headless service)</td><td>Local</td><td>Local pod IP address</td><td>Remote pod IP address</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Local pod connecting to individual pod IP address of another pod in node network namespace (headless service)</td><td>Local</td><td>Local pod IP address</td><td>Remote node IP address</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Local pod connecting to remote pod in another cluster</td><td>Local</td><td>Local pod IP address</td><td>Remote pod IP address<br />(another cluster)</td><td>✓</td><td>✓</td><td>✓</td><td>✗</td><td>✗</td><td>✗</td></tr>
  <tr><td>Local pod connecting to an external network address</td><td>Local</td><td>Local pod IP address</td><td>External IP address</td><td>✓</td><td>✓</td><td>✓</td><td>N/A</td><td>N/A</td><td>N/A</td></tr>
  <tr><td>Local pod operating in a node network namespace connecting to an external network IP address</td><td>Local</td><td>Local node IP address</td><td>External IP address</td><td>✓ ²</td><td>✓ ²</td><td>✓ ²</td><td>N/A</td><td>N/A</td><td>N/A</td></tr>
  <tr><td>Remote pod connecting to local pod through cluster IP address</td><td>Remote</td><td>Local pod IP address<br />(through cluster IP address)</td><td>Remote pod IP address</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Remote pod in a node network namespace connecting to local pod</td><td>Remote</td><td>Local pod IP address<br />(through cluster IP address)</td><td>Remote node IP address</td><td>✓</td><td>✓</td><td>✓</td><td>✓ ³</td><td>✓ ³</td><td>✓ ³</td></tr>
  <tr><td>Remote pod connecting to local pod (headless service)</td><td>Remote</td><td>Local pod IP address</td><td>Remote pod IP address</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>External pod connecting to a local pod</td><td>Remote</td><td>Local pod IP address</td><td>Remote pod IP address</td><td>✓</td><td>✓</td><td>✓</td><td>✗</td><td>✗</td><td>✗</td></tr>
  <tr><td>External resource connecting through NodePort or a Load Balancer to a local pod</td><td>Remote</td><td>Local pod IP address</td><td>External IP address ⁴</td><td>✓</td><td>✓</td><td>✓</td><td>N/A</td><td>N/A</td><td>N/A</td></tr>
  <tr><td>External resource connecting through NodePort or a Load Balancer to a local pod operating in a node network namespace</td><td>Remote</td><td>Local node IP address</td><td>External IP address ⁴</td><td>✓</td><td>✓</td><td>✓</td><td>N/A</td><td>N/A</td><td>N/A</td></tr>
</tbody>
</table>


Be aware of the following additional information corresponding to the items marked with footnotes in the preceding table.

1. Pod name is not visible in this scenario for pods with other owners, such as a Kubernetes service managed by the EKS control plane.

1. Local pod name, service, and namespace are not resolved if other pods are present in node network namespace.

1. Remote pod name, service, and namespace are not resolved if other pods are present in node network namespace.

1. If service is using NodePort or LoadBalancer in instance mode, and `ExternalTrafficPolicy` is set to `Cluster`, then this IP address will be reported as the IP address of the node that receives the NodePort connection.
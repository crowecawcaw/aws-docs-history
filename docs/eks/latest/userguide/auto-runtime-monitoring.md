

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Monitor the EKS Auto Mode runtime
<a name="auto-runtime-monitoring"></a>

Amazon EKS Auto Mode provides a streamlined experience for running Kubernetes on AWS. It automatically provisions nodes by using AWS-managed AMIs and Karpenter. EKS Auto Mode also runs a set of controllers in the control plane that aren’t visible to you. To close the observability gap this can create, EKS delivers [AWS-managed component logs](auto-managed-component-logs.md) for the control plane controllers. In addition, because the EKS Auto Mode runtime components are installed in the AMI and run on your nodes, you can configure your own log and metrics collectors to gather their logs and metrics.

This topic describes how to collect logs and metrics from the components that run on EKS Auto Mode nodes. For information about logs from the AWS-managed controllers that run in the control plane, see [Access AWS-Managed Component Logs For EKS Auto](auto-managed-component-logs.md).

## Runtime component logs
<a name="_runtime_component_logs"></a>

EKS Auto Mode removes the need for you to run critical add-ons such as CoreDNS, `kube-proxy`, and the Amazon VPC CNI. These add-ons are baked into the EKS Auto Mode AMIs and run as `systemd` services on your nodes. To collect logs from these components, use [Fluent Bit](https://fluentbit.io/) through the [Amazon CloudWatch Observability add-on](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.html), or the log aggregator of your choice.

Fluent Bit is configured with a `ConfigMap`. Within the configuration, you specify the `systemd` services you want to monitor by using `Systemd_Filter` entries in a `systemd` input. The following snippet illustrates the concept.

```
  dataplane-log.conf: |
    [INPUT]
      Name                systemd
      Tag                 dataplane.systemd.*
      Systemd_Filter      _SYSTEMD_UNIT=containerd.service
      Systemd_Filter      _SYSTEMD_UNIT=kubelet.service
      Systemd_Filter      _SYSTEMD_UNIT=coredns.service
      Systemd_Filter      _SYSTEMD_UNIT=kube-proxy.service
      Systemd_Filter      _SYSTEMD_UNIT=eks-ebs-csi-driver.service
      Systemd_Filter      _SYSTEMD_UNIT=eks-pod-identity-agent.service
      Systemd_Filter      _SYSTEMD_UNIT=eks-node-monitoring-agent.service
      DB                  /var/fluent-bit/state/systemd.db
      Path                /var/log/journal
      Read_From_Tail      ${READ_FROM_TAIL}
```

You can also collect file-based logs written by the VPC CNI components under `/var/log/aws-routed-eni/`. These include `ipamd`, `network-policy-agent`, `plugin`, and `ebpf-sdk` logs. To collect them, add a `tail` input to the configuration.

**Note**  
The preceding example is shortened for clarity. For a complete `ConfigMap` that collects application, runtime, and host logs and ships them to CloudWatch Logs, see the Container Insights Fluent Bit configuration in the Amazon CloudWatch documentation.

For point-in-time log collection from a single node, you can use a `NodeDiagnostic` resource to gather a log bundle instead of streaming logs continuously. For more information, see [Retrieve node logs using kubectl and Amazon S3](auto-get-logs.md). The Node Monitoring Agent also runs on every EKS Auto Mode node. It reports node health and surfaces issues as node conditions and events. For more information, see [Troubleshoot EKS Auto Mode](auto-troubleshoot.md).

## Runtime component metrics
<a name="_runtime_component_metrics"></a>

Metric collection in EKS Auto Mode is similar to metric collection in self-managed EKS on Amazon EC2 nodes. The components that run on your nodes expose Prometheus metrics endpoints that you can collect with the scraper of your choice.

**Note**  
This list covers the metrics that are most useful to monitor today. EKS is expanding the metrics that runtime components expose, so the available metrics might change over time.

The following table shows the metrics endpoint (port and path) for each component.


| Component | Metrics endpoint (port/path) | 
| --- | --- | 
| CoreDNS |  `9153/metrics`  | 
|  `kube-proxy`  |  `10249/metrics`  | 
| IPAM daemon (`ipamd`) |  `61678/metrics`  | 
| Network Policy Agent |  `8900/metrics`  | 
| Node Monitoring Agent |  `8801/metrics`  | 
| Pod Identity Agent |  `2705/metrics`  | 

### Access a node to run diagnostic commands
<a name="_access_a_node_to_run_diagnostic_commands"></a>

EKS Auto Mode nodes are secured and don’t allow direct SSH or SSM access. To run commands such as `curl` or `netstat` on a node, open an interactive shell in a debug container that runs on the node. The following command starts a debug container, where `node-name` is the name of the node.

```
kubectl debug node/node-name -it --profile=sysadmin --image=public.ecr.aws/amazonlinux/amazonlinux:2023
```

Run the commands in the following section from the shell that this command opens. For more information about debugging nodes, see [Troubleshoot EKS Auto Mode](auto-troubleshoot.md).

### Querying a metrics endpoint
<a name="_querying_a_metrics_endpoint"></a>

You can query an endpoint from a node to confirm that metrics are being served. The following example uses `curl` to read the CoreDNS metrics endpoint.

```
curl localhost:9153/metrics
```

The output includes the Prometheus metrics exposed by the component.

```
# HELP coredns_build_info A metric with a constant '1' value labeled by version, revision, and goversion from which CoreDNS was built.
# TYPE coredns_build_info gauge
coredns_build_info{goversion="go1.26.3",revision="",version="1.13.2"} 1
# HELP coredns_cache_entries The number of elements in the cache.
# TYPE coredns_cache_entries gauge
...
```

To confirm which ports the node components are listening on, use `netstat`.

```
netstat -tulpn | grep 127.0.0.1
```

```
tcp        0      0 127.0.0.1:9153          0.0.0.0:*               LISTEN      2198/coredns
tcp        0      0 127.0.0.1:50051         0.0.0.0:*               LISTEN      1921/ipamd
tcp        0      0 127.0.0.1:8901          0.0.0.0:*               LISTEN      2043/aws-network-po
tcp        0      0 127.0.0.1:8900          0.0.0.0:*               LISTEN      2043/aws-network-po
tcp        0      0 127.0.0.1:2705          0.0.0.0:*               LISTEN      1744/eks-pod-identi
tcp        0      0 127.0.0.1:2703          0.0.0.0:*               LISTEN      1744/eks-pod-identi
tcp        0      0 127.0.0.1:8801          0.0.0.0:*               LISTEN      1647/eks-node-monit
tcp        0      0 127.0.0.1:8800          0.0.0.0:*               LISTEN      1647/eks-node-monit
tcp        0      0 127.0.0.1:61679         0.0.0.0:*               LISTEN      1921/ipamd
tcp        0      0 127.0.0.1:61678         0.0.0.0:*               LISTEN      1921/ipamd
tcp        0      0 127.0.0.1:10256         0.0.0.0:*               LISTEN      1697/kube-proxy
tcp        0      0 127.0.0.1:10249         0.0.0.0:*               LISTEN      1697/kube-proxy
tcp        0      0 127.0.0.1:10248         0.0.0.0:*               LISTEN      1770/kubelet
```

### Elastic Fabric Adapter and node-level network metrics
<a name="_elastic_fabric_adapter_and_node_level_network_metrics"></a>

For clusters that use Elastic Fabric Adapter (EFA) for high-performance networking, you can monitor EFA and node-level network performance through the following sources:
+  **Container Insights** – Collects and surfaces node and Pod metrics for your cluster. For more information, see the Container Insights link in the following section.
+  **Network Flow Monitor** – Scrapes network performance metrics for Pods and worker nodes from the Network Flow Monitor agent that runs in your cluster. For more information, see [Monitor Kubernetes workload traffic with Container Network Observability](network-observability.md).
+  **Node-level counters** – EFA and network device counters that are exposed on the node, which you can scrape with your metrics collector.

## Related resources
<a name="_related_resources"></a>
+  [Access AWS-Managed Component Logs For EKS Auto](auto-managed-component-logs.md) 
+  [Amazon CloudWatch Observability add-on](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.html) 
+  [Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights.html) 
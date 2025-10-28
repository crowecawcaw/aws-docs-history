**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Monitor Kubernetes DNS resolution with CoreDNS metrics

CoreDNS as an EKS add-on exposes the metrics from CoreDNS on port `9153` in the Prometheus format in the `kube-dns` service. You can use Prometheus, the Amazon CloudWatch agent, or any other compatible system to scrape (collect) these metrics.

For an example _scrape configuration_ that is compatible with both Prometheus and the CloudWatch agent, see [CloudWatch agent configuration for Prometheus](../../../AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup-configure.md "../../../AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup-configure.md") in the _Amazon CloudWatch User Guide_.

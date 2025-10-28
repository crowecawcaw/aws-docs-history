# Using vertical autoscaling with Amazon EMR Spark jobs

Amazon EMR on EKS vertical autoscaling automatically tunes memory and CPU resources to adapt to
the needs of the workload that you provide for Amazon EMR Spark applications. This simplifies
resource management.

To track the real-time and historic resource utilization of your Amazon EMR Spark applications,
vertical autoscaling leverages the Kubernetes [Vertical
Pod Autoscaler (VPA)](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler "https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler"). The vertical autoscaling capability uses the data that VPA
collects to automatically tune the memory and CPU resources assigned to your Spark
applications. This simplified process enhances reliability and optimizes cost.

###### Topics

- [Setting up](jobruns-vas-setup.md "jobruns-vas-setup.md")
- [Getting started](jobruns-vas-gs.md "jobruns-vas-gs.md")
- [Configuration](jobruns-vas-configure.md "jobruns-vas-configure.md")
- [Monitoring the recommendations](jobruns-vas-monitor.md "jobruns-vas-monitor.md")
- [Uninstalling](jobruns-vas-uninstall-operator.md "jobruns-vas-uninstall-operator.md")



 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# EKS-optimized accelerated AMIs for AI/ML workloads
<a name="ml-eks-optimized-amis-overview"></a>

**Tip**  
 [Register](https://events.eksworkshop.com/workshops/genai/) for upcoming Amazon EKS AI/ML workshops.

Running AI/ML workloads on Amazon EKS requires an operating system image that includes the GPU drivers, kernel modules, and container runtime configuration that accelerated instances depend on. Amazon EKS publishes EKS-optimized accelerated AMIs that bundle these components with the standard EKS node components, so your nodes can run GPU-accelerated containers as soon as they join the cluster.

This section covers the accelerated AMI options for both node operating systems:
+  [Use EKS-optimized accelerated Linux AMIs for GPU instances](ml-eks-optimized-ami.md) — The EKS-optimized Amazon Linux and Bottlerocket accelerated AMIs, which include the NVIDIA and AWS Neuron drivers for `G`, `P`, Inferentia, and Trainium instances. This topic also covers which instance types each AMI variant supports and how to find the latest AMI IDs.
+  [Build EKS-optimized Windows AMIs for GPU instances](ml-eks-windows-optimized-ami.md) — The options for GPU-accelerated Windows containers, including building a custom EKS Windows optimized AMI with the GPU drivers pre-installed, or installing the drivers on worker nodes after launch.
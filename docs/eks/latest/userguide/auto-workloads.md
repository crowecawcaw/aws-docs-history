**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Run sample workloads in EKS Auto Mode clusters

This chapter provides examples of how to deploy different types of workloads to Amazon EKS clusters running in Auto Mode. The examples demonstrate key workload patterns including sample applications, load-balanced web applications, stateful workloads using persistent storage, and workloads with specific node placement requirements. Each example includes complete manifests and step-by-step deployment instructions that you can use as templates for your own applications.

Before proceeding with the examples, ensure that you have an EKS cluster running in Auto Mode and that you have installed the AWS CLI and kubectl. For more information, see [Set up to use Amazon EKS](setting-up.md "setting-up.md"). The examples assume basic familiarity with Kubernetes concepts and kubectl commands.

You can use these use case-based samples to run workloads in EKS Auto Mode clusters.

[Deploy a sample inflate workload to an Amazon EKS Auto Mode cluster](automode-workload.md "automode-workload.md")

Shows how to deploy a sample workload to an EKS Auto Mode cluster using `kubectl` commands.

[Deploy a Sample Load Balancer Workload to EKS Auto Mode](auto-elb-example.md "auto-elb-example.md")

Shows how to deploy a containerized version of the 2048 game on Amazon EKS.

[Deploy a sample stateful workload to EKS Auto Mode](sample-storage-workload.md "sample-storage-workload.md")

Shows how to deploy a sample stateful application to an EKS Auto Mode cluster.

[Deploy an accelerated workload](auto-accelerated.md "auto-accelerated.md")

Shows how to deploy hardware-accelerated workloads to nodes managed by EKS Auto Mode.

[Control if a workload is deployed on EKS Auto Mode nodes](associate-workload.md "associate-workload.md")

Shows how to use an annotation to control if a workload is deployed to nodes managed by EKS Auto Mode.

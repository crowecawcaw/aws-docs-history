

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Scale cluster compute with Karpenter and Cluster Autoscaler

Autoscaling is a function that automatically scales your resources out and in to meet changing demands. This is a major Kubernetes function that would otherwise require extensive human resources to perform manually.

## EKS Auto Mode
<a name="_eks_auto_mode"></a>

Amazon EKS Auto Mode automatically scales cluster compute resources. If a pod can’t fit onto existing nodes, EKS Auto Mode creates a new one. EKS Auto Mode also consolidates workloads and deletes nodes. EKS Auto Mode builds upon Karpenter.

For more information, see:
+  [Automate cluster infrastructure with EKS Auto Mode](automode.md) 
+  [Create a Node Pool for EKS Auto Mode](create-node-pool.md) 
+  [Deploy a sample inflate workload to an Amazon EKS Auto Mode cluster](automode-workload.md) 

## Additional Solutions
<a name="_additional_solutions"></a>

Amazon EKS supports two additional autoscaling products:

 **Karpenter**   
Karpenter is a flexible, high-performance Kubernetes cluster autoscaler that helps improve application availability and cluster efficiency. Karpenter launches right-sized compute resources (for example, Amazon EC2 instances) in response to changing application load in under a minute. Through integrating Kubernetes with AWS, Karpenter can provision just-in-time compute resources that precisely meet the requirements of your workload. Karpenter automatically provisions new compute resources based on the specific requirements of cluster workloads. These include compute, storage, acceleration, and scheduling requirements. Amazon EKS supports clusters using Karpenter, although Karpenter works with any conformant Kubernetes cluster. For more information, see the [Karpenter](https://karpenter.sh/docs/) documentation.  
Karpenter is open-source software which AWS customers are responsible for installing, configuring, and managing in their Kubernetes clusters. AWS provides technical support when Karpenter is run unmodified using a compatible version in Amazon EKS clusters. It is essential that customers maintain the availability and security of the Karpenter controller as well as appropriate testing procedures when upgrading it or the Kubernetes cluster in which it’s running, just like any other customer-managed software. There is no AWS Service Level Agreement (SLA) for Karpenter and customers are responsible for ensuring that the EC2 instances launched by Karpenter meet their business requirements.

 **Cluster Autoscaler**   
The Kubernetes Cluster Autoscaler automatically adjusts the number of nodes in your cluster when pods fail or are rescheduled onto other nodes. The Cluster Autoscaler uses Auto Scaling groups. For more information, see [Cluster Autoscaler on AWS](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md).

## Autoscaling with Nitro Sandboxes
<a name="_autoscaling_with_nitro_sandboxes"></a>

When you run isolated or confidential pods with Nitro Sandboxes, provisioning works with both EKS Auto Mode and Karpenter. When a pod sets `runtimeClassName` to `isolated-sandbox` or `confidential-sandbox`, the RuntimeClass automatically counts the pod against the node’s `eks.amazonaws.com/nitro-sandbox` slots through its overhead. You do not request this resource in your pod spec. The autoscaler then provisions a Nitro Enclaves-enabled node of a supported instance type. Keep the following in mind when you size and scale sandbox capacity:
+  **Sandbox density.** Two separate caps apply. The total vCPUs allocated across all sandboxes on a node cannot exceed 5 times the node’s vCPU count, and the number of sandboxes on a node cannot exceed 5 times the node’s vCPU count. The node’s maximum pods still applies. A node fits more single-vCPU sandboxes than large multi-vCPU sandboxes. For example, a 4-vCPU node has a 20-vCPU sandbox budget.
+  **Memory overhead.** Each sandbox pod carries a fixed RuntimeClass memory overhead that the scheduler adds to the pod’s own memory request: 256 MiB for `isolated-sandbox` and 512 MiB for `confidential-sandbox`. Size pods with this overhead included, and expect fewer sandbox pods per node than the raw memory of the instance type suggests.
+  **Instance types.** The autoscaler selects from instance types that support Nitro Enclaves.

For more information, see [Sandboxing on Amazon EKS with isolated and confidential pods](sandboxing.md).
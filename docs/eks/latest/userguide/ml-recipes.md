

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Recipes to optimize your Amazon EKS cluster for AI/ML workloads
<a name="ml-recipes"></a>

**Tip**  
 [Register](https://events.eksworkshop.com/workshops/genai/) for upcoming Amazon EKS AI/ML workshops.

This section is designed to provide bite-sized recipes for optimizing your Amazon EKS cluster, particularly for AI/ML workloads involving specialized hardware. Each recipe includes prerequisites, step-by-step procedures, and deployment considerations.
+  [Target AI/ML workloads to specific nodes with labels](ml-workload-placement.md) — Target workloads to the right nodes using the labels that Amazon EKS applies automatically.
+  [Place distributed AI/ML workloads with network topology labels](ml-workload-topology.md) — Place the Pods of a distributed job close to each other using network topology labels.
+  [Prevent Pods from being scheduled on accelerated nodes](ml-workload-taints.md) — Keep workloads off accelerated nodes by adding taints, with EKS Auto Mode, Karpenter, and managed node groups.
+  [Configure hugepages in Amazon EKS clusters](ml-hugepages.md) — Configure hugepages for memory-intensive workloads.
+  [Use AWS Inferentia instances with Amazon EKS for Machine Learning](ml-inferentia.md) — Create an inference cluster with AWS Inferentia instances.
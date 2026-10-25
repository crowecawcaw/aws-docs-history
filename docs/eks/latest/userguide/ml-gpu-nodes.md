

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create GPU nodes for AI/ML workloads on Amazon EKS
<a name="ml-gpu-nodes"></a>

**Tip**  
 [Register](https://events.eksworkshop.com/workshops/genai/) for upcoming Amazon EKS AI/ML workshops.

After you set up the cluster infrastructure in [Set up Amazon EKS cluster for AI/ML workloads](ml-cluster-setup.md), the next step is GPU compute. This section defines the EKS Auto Mode or Karpenter NodePools that dynamically provision Amazon EC2 GPU instances, so that nodes are created as GPU workloads are scheduled and removed when they are no longer needed.

Create NodePools based on your workload type, because each type places different demands on GPU capacity:
+  **Inference** — Favors smaller G-family instances with Spot capacity and scale-to-zero behavior, which keeps GPUs idle-free between traffic peaks. For a walkthrough, see [Create a GPU NodePool for AI/ML inference](ml-inference-gpu-nodepool.md).

Each walkthrough builds on the cluster you created in the [Set up Amazon EKS cluster for AI/ML workloads](ml-cluster-setup.md) section. Complete that section first, then choose the same path (EKS Auto Mode or self-managed Karpenter) that you used to create your cluster.
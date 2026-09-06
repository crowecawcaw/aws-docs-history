

# Amazon EKS - Resource Tagging
<a name="eks-best-practices"></a>

Amazon EKS clusters run containerized applications on a set of nodes. Customers pay for EKS cluster hours and the underlying AWS resources including nodes (EC2 instances), load balancers, and EBS volumes. To measure revenue with Partner Revenue Measurement, you must tag both the Kubernetes cluster and its underlying AWS resources.

**Note**  
The tag value must use the format `pc:{{product-code}}`, where `{{product-code}}` is your AWS Marketplace product code. To retrieve your product code, see [Product Code Retrieval](product-code-retrieval.md).

## Tagging the Kubernetes cluster
<a name="eks-tagging-cluster"></a>

You can add tags to new or existing Kubernetes clusters using the Amazon EKS console, `eksctl`, AWS CLI, AWS API, or infrastructure-as-code tools like Terraform.
+ **New clusters** – Apply tags during cluster creation using the `tags` parameter on the `CreateCluster` API action.
+ **Existing clusters** – Apply tags using the `TagResource` API, or the **Tags** tab in the Amazon EKS console.
+ **Terraform** – Use the `tags` argument when creating an EKS cluster. For more information, see [Terraform EKS cluster resource](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/eks_cluster).

```
aws eks tag-resource \
  --resource-arn arn:aws:eks:{{region}}:{{account-id}}:cluster/{{cluster-name}} \
  --tags aws-apn-id=pc:{{5ugbbrmu7ud3u5hsipfzug61p}}
```

## Tagging nodes within a node group
<a name="eks-tagging-nodes"></a>

Amazon EKS clusters can schedule pods on any combination of self-managed nodes and EKS managed nodes. In all cases, ensure nodes are tagged with `aws-apn-id` using the format `pc:{{product-code}}`.
+ **Managed nodes** – Use a custom launch template with the `TagSpecification` parameter to specify tags to apply to nodes (EC2 instances) in the node group. For example:

  ```
  "TagSpecifications": [
    {
      "ResourceType": "instance",
      "Tags": [
        {
          "Key": "aws-apn-id",
          "Value": "pc:{{5ugbbrmu7ud3u5hsipfzug61p}}"
        }
      ]
    }
  ]
  ```

  You can launch a managed node group with a custom launch template using the EKS API, AWS CLI, CloudFormation, or the EKS console. For more information, see [Launch template support](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html).
+ **Self-managed nodes** – Apply tags by creating a node group with `eksctl` using the `tags` parameter. Tags are applied to all EC2 instances created as part of the node group. You can also apply tags using the AWS Management Console. For more information, see [Tagging your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html).

## Tagging load balancers
<a name="eks-tagging-load-balancers"></a>

The AWS Load Balancer Controller manages Elastic Load Balancers for a Kubernetes cluster.
+ **Application Load Balancer (ALB)** – The controller creates an ALB when you create a Kubernetes Ingress. To tag ALBs, add the following annotation to the Ingress:

  ```
  alb.ingress.kubernetes.io/tags: aws-apn-id=pc:{{5ugbbrmu7ud3u5hsipfzug61p}}
  ```

  For more information, see [Application load balancing on Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/alb-ingress.html).
+ **Network Load Balancer (NLB)** – The controller creates an NLB when you create a Kubernetes Service of type `LoadBalancer` using IP targets. To tag NLBs, add the following annotation to the Service:

  ```
  service.beta.kubernetes.io/aws-load-balancer-additional-resource-tags: aws-apn-id=pc:{{5ugbbrmu7ud3u5hsipfzug61p}}
  ```

  For more information, see [Network load balancing on Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/network-load-balancing.html).

## Tagging EBS volumes
<a name="eks-tagging-ebs"></a>

The Amazon EBS Container Storage Interface (CSI) driver provides a CSI interface that allows Amazon EKS clusters to manage the lifecycle of EBS volumes. To add tags to dynamically provisioned EBS volumes, use the `--extra-tags` command option in the CSI driver. For detailed instructions, see the [Amazon EBS CSI driver documentation](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html).

## Fargate on EKS
<a name="eks-fargate"></a>

Fargate on EKS is not supported for Partner Revenue Measurement resource tagging.

## Isolating partner solution resources on a shared EKS cluster
<a name="eks-shared-cluster"></a>

If a customer runs both partner solution workloads and other workloads in the same EKS cluster, you cannot tag the cluster itself (the control plane). Instead, tag only the load balancers and the nodes running partner solution workloads. To isolate the workloads, use Kubernetes affinities and taints.

1. **Create a partner-solution-only node group.**
   + Tag this node group following the instructions in [Tagging nodes within a node group](#eks-tagging-nodes).
   + Add a taint with effect `NO_SCHEDULE`.
   + Add a label (for example, `partner-solution: "true"`).

1. **Create partner solution pods.**
   + Add a toleration to the pods with a key/value matching the taint from step 1 and an effect of `NoSchedule`.
   + Add a `requiredDuringSchedulingIgnoredDuringExecution` affinity with a `matchExpression` that matches the label from step 1.

Steps 1 and 2a prevent non-partner-solution pods from deploying on partner solution nodes. Steps 1b and 2b prevent partner solution pods from deploying on non-partner-solution nodes. No changes are required to existing non-partner-solution pods or nodes.

For more information, see:
+ [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
+ [Node Affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity)
+ [Taints on EKS managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html)
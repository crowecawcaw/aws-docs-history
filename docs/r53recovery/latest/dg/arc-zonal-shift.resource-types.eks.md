

# Amazon Elastic Kubernetes Service
<a name="arc-zonal-shift.resource-types.eks"></a>

Amazon EKS provides features that enable you to make your applications more resilient to events such as the degraded health or the impairment of an Availability Zone. When you run your workloads in an Amazon EKS cluster, you can further improve fault tolerance and application recovery by using zonal shift or zonal autoshift. For more information, see [Learn about ARC Zonal Shift in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html) in the *Amazon Elastic Kubernetes Service User Guide*.

## Using zonal shift with Amazon Elastic Kubernetes Service
<a name="using-eks-zs"></a>

To enable zonal shift, use one of the following methods. For more information, see [Learn about ARC zonal shift](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift-enable.html#zone-shift-enable-steps) in the *Amazon Elastic Kubernetes Service User Guide*.

------
#### [ Console ]

**To enable zonal shift on a new Amazon EKS cluster (Console)**

1. Find the name and Region of the Amazon EKS cluster that you want to register with ARC.

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home\#/clusters](https://console.aws.amazon.com/eks/home#/clusters).

1. Select your cluster.

1. On the **Cluster info** page, select the **Overview** tab.

1. Under **Zonal shift**, choose **Manage**.

1. For **EKS Zonal Shift**, choose **Enable** or **Disable**.

------
#### [ AWS CLI ]

**To enable zonal shift on a new Amazon EKS cluster (AWS CLI)**
+ Enter the following command:

  ```
  aws eks create-cluster --name {{my-eks-cluster}} --role-arn {{my-role-arn-to-create-cluster}} --resources-vpc-config subnetIds=string,string,securityGroupIds=string,string,endpointPublicAccess=boolean,endpointPrivateAccess=boolean,publicAccessCidrs=string,string --zonal-shift-config enabled=true
  ```

**To enable zonal shift on an existing Amazon EKS cluster (AWS CLI)**
+ Enter the following command:

  ```
  aws eks update-cluster-config --name {{my-eks-cluster}} --zonal-shift-config enabled=true
  ```

------

You can start a zonal shift for an Amazon EKS cluster, or you can allow AWS to do it for you, by enabling zonal autoshift. After your Amazon EKS cluster zonal shift enabled with ARC, you can start a zonal shift or enable zonal autoshift using the ARC Console, the AWS CLI, or the zonal shift and zonal autoshift APIs. 

For more information on starting a zonal shift, see [Starting, updating, or canceling a zonal shift](arc-zonal-shift.start-cancel.md).

For more information on enabling Amazon EKS with zonal shift, see [Learn about ARC Zonal Shift in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html) in the *Amazon Elastic Kubernetes Service User Guide*. 

## How zonal shift works for Amazon Elastic Kubernetes Service
<a name="how-it-works-eks-zs"></a>

During an Amazon EKS zonal shift, the following automatically takes place for all Amazon EKS clusters:
+ All the nodes in the impacted AZ are cordoned. This prevents the Kubernetes Scheduler from scheduling new Pods onto the nodes in the unhealthy AZ.
+ If you’re using [Managed Node Groups](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html), [Availability Zone rebalancing](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html#AutoScalingBehavior.InstanceUsage) is suspended, and your Auto Scaling group is updated to ensure that new Amazon EKS data plane nodes are only launched in healthy AZs.
+ The nodes in the unhealthy AZ are not terminated and the Pods are not evicted from these nodes. This is to ensure that when a zonal shift expires or is canceled, your traffic can be safely returned to the AZ that still has full capacity.
+ The EndpointSlice controller finds all the Pod endpoints in the impaired AZ and removes them from the relevant EndpointSlices. This ensures that only Pod endpoints in healthy AZs are targeted to receive network traffic. When a zonal shift is canceled or expires, the EndpointSlice controller updates the EndpointSlices to include the endpoints in the restored AZ.

If you are using EKS Auto Mode or self-managed Karpenter, the Karpenter controller also does the following during a zonal shift:
+ Stops provisioning new capacity in the impaired AZ by marking all compute offerings in that zone as unavailable.
+ Stops voluntary disruption (consolidation and drift) on nodes in the impaired AZ.
+ Prevents launch attempts for pods with strict scheduling requirements (such as EBS volume affinity) that require the impaired AZ.
+ Resumes normal behavior when the zonal shift is canceled or expires.

For more information about Amazon EKS zonal shift, see the [AWS Containers blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-amazon-application-recovery-controller/) on the AWS website.
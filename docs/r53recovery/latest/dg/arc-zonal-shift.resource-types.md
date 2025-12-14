# Amazon Elastic Kubernetes Service

Amazon EKS provides features that enable you to make your applications more resilient to events such as the degraded health or the impairment of an Availability Zone.
When you run your workloads in an Amazon EKS cluster, you can further improve your application environment’s fault tolerance and application recovery by using zonal shift
or zonal autoshift.

## Using zonal shift with Amazon Elastic Kubernetes Service

To enable zonal shift, use one of the following methods. For more information, see [Learn about ARC zonal shift](../../../eks/latest/userguide/zone-shift-enable.md#zone-shift-enable-steps "../../../eks/latest/userguide/zone-shift-enable.md#zone-shift-enable-steps") in the _Amazon Elastic Kubernetes Service User Guide_.

Console

###### To enable zonal shift on a new Amazon EKS cluster (Console)

1. Find the name and Region of the Amazon EKS cluster that you want to register with ARC.
2. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
3. Select your cluster.
4. On the **Cluster info** page, select the **Overview** tab.
5. Under **Zonal shift**, choose **Manage**.
6. For **EKS Zonal Shift**, choose **Enable** or **Disable**.

AWS CLI

###### To enable zonal shift on a new Amazon EKS cluster (AWS CLI)

- Enter the following command:

```
aws eks create-cluster --name `my-eks-cluster` --role-arn `my-role-arn-to-create-cluster` --resources-vpc-config subnetIds=string,string,securityGroupIds=string,string,endpointPublicAccess=boolean,endpointPrivateAccess=boolean,publicAccessCidrs=string,string --zonal-shift-config enabled=true
```

###### To enable zonal shift on an existing Amazon EKS cluster (AWS CLI)

- Enter the following command:

```
aws eks update-cluster-config --name `my-eks-cluster` --zonal-shift-config enabled=true
```

You can start a zonal shift for an Amazon EKS cluster, or you can allow AWS to
do it for you, by enabling zonal autoshift. After your Amazon EKS cluster zonal shift
enabled with ARC, you can start a zonal shift or enable zonal autoshift
using the ARC Console, the AWS CLI, or the zonal shift and zonal
autoshift APIs.

For more information on starting a zonal shift, see [Starting, updating, or canceling a zonal shift](arc-zonal-shift.md "arc-zonal-shift.md").

For more information on enabling Amazon EKS with zonal shift, see [Learn about
ARC Zonal Shift in Amazon EKS](../../../eks/latest/userguide/zone-shift.md "../../../eks/latest/userguide/zone-shift.md") in the _Amazon Elastic Kubernetes Service User Guide_.

## How zonal shift works for Amazon Elastic Kubernetes Service

During an Amazon EKS zonal shift, the following automatically takes place:

- All the nodes in the impacted AZ are cordoned.
  This prevents the Kubernetes Scheduler from scheduling new Pods onto the nodes in the unhealthy AZ.
- If you’re using [Managed Node Groups](../../../eks/latest/userguide/managed-node-groups.md "../../../eks/latest/userguide/managed-node-groups.md"), [Availability Zone rebalancing](../../../autoscaling/ec2/userguide/auto-scaling-benefits.md#AutoScalingBehavior.InstanceUsage "../../../autoscaling/ec2/userguide/auto-scaling-benefits.md#AutoScalingBehavior.InstanceUsage")
  is suspended, and your Amazon EC2 Auto Scaling group is updated to ensure that new Amazon EKS data plane nodes are only launched in healthy AZs.
- The nodes in the unhealthy AZ are not terminated and the Pods are not evicted from these nodes. This is to ensure that when a
  zonal shift expires or is canceled, your traffic can be safely returned to the AZ that still has full capacity.
- The EndpointSlice controller finds all the Pod endpoints in the impaired AZ and removes them from the relevant
  EndpointSlices. This ensures that only Pod endpoints in healthy AZs are targeted to receive network traffic.
  When a zonal shift is canceled or expires, the EndpointSlice controller updates the EndpointSlices to include the
  endpoints in the restored AZ.

For more information, see the [AWS
Containers blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-amazon-application-recovery-controller/ "https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-amazon-application-recovery-controller/").

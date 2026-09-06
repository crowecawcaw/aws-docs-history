

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Launch low-latency EKS clusters with AWS Local Zones
<a name="local-zones"></a>

An [AWS Local Zone](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) is an extension of an AWS Region in geographic proximity to your users. Local Zones have their own connections to the internet and support [AWS Direct Connect](https://aws.amazon.com/directconnect/). Resources created in a Local Zone can serve local users with low-latency communications. For more information, see the [AWS Local Zones User Guide](https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html) and [Local Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-local-zones) in the *Amazon EC2 User Guide*.

Amazon EKS supports certain resources in Local Zones. This includes [managed node groups](managed-node-groups.md), [self-managed Amazon EC2 nodes](worker.md), Amazon EBS volumes, and Application Load Balancers (ALBs). We recommend that you consider the following when using Local Zones as part of your Amazon EKS cluster.
+ You can’t create Fargate nodes in Local Zones with Amazon EKS.
+ The Amazon EKS managed Kubernetes control plane always runs in the AWS Region. The Amazon EKS managed Kubernetes control plane can’t run in the Local Zone. Because Local Zones appear as a subnet within your VPC, Kubernetes sees your Local Zone resources as part of that subnet.
+ The Amazon EKS Kubernetes cluster communicates with the Amazon EC2 instances you run in the AWS Region or Local Zone using Amazon EKS managed [elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html). To learn more about Amazon EKS networking architecture, see [Configure networking for Amazon EKS clusters](eks-networking.md).
+ Unlike Regional subnets, Amazon EKS can’t place cross-account elastic network interfaces into your Local Zone subnets. These interfaces are used for control plane to node communication. This means that you must not specify Local Zone subnets when you create your cluster. However, you can have worker nodes in multiple Local Zones connected to the same cluster.
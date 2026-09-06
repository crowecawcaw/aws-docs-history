

# Local Clusters for Amazon EKS on AWS Outposts
<a name="local-clusters-for-amazon-eks-on-aws-outposts"></a>

Publication date: **June 02, 2023 ([Diagram history](#diagram-history))**

This reference architecture diagram helps you deploy a local cluster for Amazon Elastic Kubernetes Service (Amazon EKS) on AWS Outposts.

## Local Clusters for Amazon EKS on AWS Outposts Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how you can use AWS services to deploy a local cluster for Amazon EKS on AWS Outposts.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/local-clusters-for-amazon-eks-on-aws-outposts/images/local-clusters-for-amazon-eks-on-aws-outposts.png)


1. Ensure that you have a reliable network connection between AWS Outposts and its parent Region. Use a highly available, low-latency connectivity, such as AWS Direct Connect. 

1. Create the Amazon Elastic Kubernetes Service (Amazon EKS) [local cluster VPC and its required constructs](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-vpc-subnet-requirements.html). 

1. Create a [local Amazon EKS cluster](https://aws.amazon.com/blogs/containers/fully-private-local-clusters-for-amazon-eks-on-aws-outposts-powered-by-vpc-endpoints/), specifying the Kubernetes control plane subnet on AWS Outposts. 

1. Create [self-managed](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-self-managed-nodes.html) Amazon EKS nodes on AWS Outposts, following the recommended [prerequisites](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-local-cluster-create.html). 

1. Allow administrative access from the on-premises network to the Amazon EKS cluster endpoint using the local gateway (LGW). For more information, refer to [Local gateway basics](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html). 

1. Refer to the local cluster for Amazon EKS on AWS Outposts [considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-network-disconnects.html). 

**Note**  
Deploying a local cluster for Amazon EKS is currently only available through the [AWS Outposts Rack](https://aws.amazon.com/outposts/rack/) offering.

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | June 2, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
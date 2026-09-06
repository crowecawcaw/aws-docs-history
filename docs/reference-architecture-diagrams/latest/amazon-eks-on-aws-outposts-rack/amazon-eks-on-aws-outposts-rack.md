

# Amazon Elastic Kubernetes Service on AWS Outposts Rack
<a name="amazon-eks-on-aws-outposts-rack"></a>

Publication date: **October 31, 2022 ([Diagram history](#diagram-history))**

This reference architecture diagram shows how to deploy [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) (Amazon EKS) on an [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html) rack.

## Amazon Elastic Kubernetes Service on AWS Outposts Rack
<a name="diagram1"></a>

![Reference architecture diagram showing how to deploy Amazon EKS on an AWS Outposts rack with a private cluster control plane, self-managed nodes, and local gateway connectivity.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/amazon-eks-on-aws-outposts-rack/images/amazon-eks-on-aws-outposts-rack.png)


1. Ensure a reliable network connection between your AWS Outpost and its parent Region. Highly available, low-latency connectivity, such as [https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html).

1. Create a private Amazon EKS cluster control plane, selecting subnets in the Region where Amazon EKS managed elastic network interfaces (ENIs) will be placed.

1. For private subnets without a path to the internet, create VPC endpoints for [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) (Amazon EC2), [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) (Amazon S3), and Amazon Elastic Container Registry (Amazon ECR). Depending on which other AWS services you plan to use, additional endpoints might be needed.

1. Create self-managed Amazon EKS nodes on AWS Outposts, following the prerequisites.

1. Expose Amazon EKS nodes to your local network through a local gateway (LGW). See [how Local gateways](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html) work.

1. Use [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) (IAM) to manage user and role access to your cluster.

1. AWS Outposts supports Amazon CloudWatch metrics. For a list of supported metrics, see [CloudWatch metrics for AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-cloudwatch-metrics.html).

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS Outposts product page](https://aws.amazon.com/outposts/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | October 31, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
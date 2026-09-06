

# Containers services
<a name="sns-event-sources-containers"></a>

The following table describes how Amazon SNS integrates with AWS container services such as Amazon EKS Distro and Amazon ECS, allowing you to track updates and security patches for Amazon EKS clusters and receive notifications for new ECS-optimized AMI releases. 

You can leverage these integrations to maintain the security and efficiency of your container deployments by staying informed about important updates and changes.


| AWS service | Benefit of using with Amazon SNS | 
| --- | --- | 
| [Amazon EKS Distro](https://docs.aws.amazon.com/eks/latest/userguide/eks-distro.html) – Lets you create reliable and secure clusters wherever your applications are deployed. | Track updates and security patches for clusters created with Amazon EKS Distro. For more information, see [Introducing Amazon EKS Distro - an open source Kubernetes distribution used by Amazon EKS](https://aws.amazon.com/about-aws/whats-new/2020/12/introducing-amazon-eks-distro/). | 
| [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) – Enables you to run, stop, and manage containers on a cluster. | Receive notifications when a new Amazon ECS-optimized AMI is available. For more information, see [Subscribing to Amazon ECS-optimized AMI update notifications](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS-AMI-SubscribeTopic.html) in the *Amazon Elastic Container Service Developer Guide*. | 
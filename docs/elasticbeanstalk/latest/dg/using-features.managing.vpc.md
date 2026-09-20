

# Configuring Amazon Virtual Private Cloud (Amazon VPC) with Elastic Beanstalk
<a name="using-features.managing.vpc"></a>

[Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/) (Amazon VPC) lets you run your AWS Elastic Beanstalk environment in an isolated virtual network. If you don't specify a VPC when you create your environment, Elastic Beanstalk uses the default VPC. How you configure networking, and which resources run in your subnets, depends on your environment's mode.
+ With **Beanstalk Standard**, you configure the VPC, subnets, and IP settings for your environment's Amazon EC2 instances and load balancer. See [Configuring Amazon Virtual Private Cloud (Amazon VPC) with Beanstalk Standard environments](configuring-standard-vpc.md).
+ With **Beanstalk Cluster**, your environment runs on an Amazon EKS cluster whose nodes run in the subnets you select. For those subnets, for load balancing, and for how your environments address each other inside the cluster, see [Configuring networking for Beanstalk Cluster environments](configuring-cluster-networking.md).